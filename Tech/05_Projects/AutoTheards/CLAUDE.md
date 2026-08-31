# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Purpose

Flask API gateway that scrapes web content and processes it via Anthropic Claude.
Clients hit local Flask endpoints → endpoints scrape target URLs → Claude summarizes/extracts.

## Architecture

App factory pattern. Entry point: `app.py` (create if missing).

```
AutoTheards/
├── app.py                   # create_app() factory, loads .env
├── core/
│   ├── __init__.py          # app factory lives here
│   ├── routes.py            # blueprint registration only
│   └── services/
│       ├── scraper.py       # all httpx + BS4 logic
│       └── ai_gateway.py    # all Anthropic SDK calls
├── tests/
├── .env                     # secrets (gitignored)
└── .env.example
```

**Rule:** Routes call services. No business logic in `routes.py`.

## Tech Stack

| Package | Purpose |
|---|---|
| Flask 3.1.3 | HTTP framework |
| playwright | Browser automation for authenticated scraping |
| anthropic | Claude API client (deferred) |
| python-dotenv | Load `.env` into `os.environ` |
| ruff | Linter / formatter |
| pytest + pytest-flask | Testing |

## Dev Commands

```bash
# Activate venv (Windows)
.venv\Scripts\activate

# Install all deps
pip install -r requirements.txt

# Run dev server
flask --app app run --debug

# Lint + format
ruff check .
ruff format .

# Tests
python -m pytest
python -m pytest tests/test_routes.py -k "test_scrape"
```

## Environment Variables

Create `.env` in project root (never commit). Required:

```
ANTHROPIC_API_KEY=sk-...
FLASK_SECRET_KEY=change-me-in-prod
FLASK_ENV=development
ANTHROPIC_BASE_URL=https://api.nextgen-beta.ica.ibm.com/ica
```

> `ANTHROPIC_BASE_URL` is set globally in `~/.claude/settings.json` for Claude Code sessions.
> For standalone `flask run`, it must also be present in `.env`.

## Playwright Login Pattern

`core/services/scraper.py` exposes one public interface:

```python
from core.services.scraper import authenticate, LoginSession

session: LoginSession = authenticate()
try:
    page = session.page  # authenticated Playwright Page
    # do scraping here
finally:
    session.close()  # closes browser + stops Playwright subprocess
```

`authenticate()` handles: session cookie reuse, Microsoft SSO login, both post-login
modals, and session save. On failure it saves `error_screenshot.png` and prints a
`playwright codegen` command for re-recording the login flow.

> Run `playwright install chromium` once after `pip install playwright`.

## Playwright Modal Selectors

The LMS shows two modals after every login. Current selectors are best-guess —
update them after running `playwright codegen https://lms.binus.ac.id/lms/dashboard`:

- Modal 1 (redirect confirm): `button:has-text('OK'), button:has-text('Lanjut')`
- Modal 2 (welcome close): `button:has-text('Close'), button:has-text('Tutup'), [aria-label='Close']`

## Sub-agents

Two specialized agents are available in `.claude/agents/`:

- **scraper-researcher** — researches how to scrape a target site before writing code (robots.txt, selectors, JS detection, API endpoints)
- **api-tester** — tests running Flask endpoints via curl, validates response shapes and error handling
