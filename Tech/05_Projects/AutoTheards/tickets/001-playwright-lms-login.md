---
title: Playwright — Successful Login to Binus LMS
label: ready-for-agent
status: open
---

## Problem Statement

Accessing assignment todos on the Binus LMS (`lms.binus.ac.id`) requires manually opening a browser, completing a Microsoft SSO login, clicking through two post-login modals, and navigating to the dashboard — a slow, repetitive process that blocks automated extraction of course todos.

## Solution

A Playwright-driven login service that fully automates the Microsoft SSO authentication flow, handles both post-login modals, and reliably lands a headed browser session on the authenticated LMS dashboard. Session cookies are persisted to disk so subsequent runs skip the login entirely.

## User Stories

1. As a developer running `flask scrape`, I want Playwright to open a headed browser and navigate to the LMS dashboard automatically, so that I can watch the flow and confirm it works.
2. As a developer, I want the scraper to check for a saved session file before attempting login, so that re-runs don't repeat the full SSO flow unnecessarily.
3. As a developer, I want the session cookies saved to `.sessions/binus_session.json` after a successful login, so that the next run reuses the authenticated state.
4. As a developer, I want the scraper to detect a stale/expired session (by checking if the current URL redirects to the login page), so that it automatically re-authenticates without manual intervention.
5. As a developer, I want the login credentials read from `.env` (`BINUS_USERNAME`, `BINUS_PASSWORD`), so that secrets are never hardcoded.
6. As a developer, I want step-by-step terminal logs during login (e.g. `[1/5] Loading session... [2/5] Navigating to dashboard...`), so that I can follow what Playwright is doing in real time.
7. As a developer, I want the scraper to click the first post-login modal ("confirm redirect to LMS") and the second modal ("close welcome/alert") in sequence, so that the browser reliably reaches the dashboard after every SSO login.
8. As a developer, I want an `error_screenshot.png` saved to the project root whenever the login flow fails, so that I can diagnose SSO issues by inspecting the exact page state at failure.
9. As a developer, I want the scraper to raise a descriptive exception on auth failure (not swallow it), so that `flask scrape` exits with a clear message instead of silently producing empty results.
10. As a developer, when login fails, I want the terminal to print a ready-to-run `playwright codegen` command, so that I can re-record the login flow and capture a fresh session without having to look up the command myself.
11. As a developer, I want the `.sessions/` folder gitignored, so that session cookies are never accidentally committed.

## Implementation Decisions

- **Browser**: Playwright Chromium, always headed (`headless=False`). No env flag — headed is the only mode.
- **Credentials**: `BINUS_USERNAME` and `BINUS_PASSWORD` loaded from `.env` via `python-dotenv`. Both are required; missing either raises `EnvironmentError` at startup, not mid-scrape.
- **Session persistence**: Playwright `BrowserContext.storage_state()` serialized to `.sessions/binus_session.json`. On next run, context is created with `storage_state=path` to restore cookies.
- **Auth check flow**:
  1. Load existing session file if it exists → create context with saved state
  2. Navigate to `https://lms.binus.ac.id/lms/dashboard`
  3. If current URL contains `/login` → session is expired or absent → run full SSO login
  4. After successful login → save new session state to disk
- **Microsoft SSO login steps** (only run when session is absent/expired):
  1. The LMS redirects to `https://login.microsoftonline.com/...` automatically
  2. Fill email field with `BINUS_USERNAME`, click Next
  3. Fill password field with `BINUS_PASSWORD`, click Sign In
  4. Wait for redirect back to `https://binusmaya.binus.ac.id/`
- **Modal handling** (always executed after SSO, never skipped):
  1. Click "confirm redirect to LMS" modal button
  2. Wait for system auth verification (wait for network idle or specific URL)
  3. Click "close welcome/alert" modal button
- **Error handling**: wrap entire login sequence in try/except; on any exception: call `page.screenshot(path="error_screenshot.png")`, print the recovery hint (see below), then re-raise with message `"Login failed — see error_screenshot.png"`
- **Codegen recovery hint**: after saving the screenshot, print a ready-to-copy command to stdout:
  ```
  Login failed. To re-record the login flow, run:
    playwright codegen https://lms.binus.ac.id/lms/dashboard --save-storage=.sessions/binus_session.json
  Then re-run `flask scrape`.
  ```
  This lets the developer open a headed browser, manually complete the SSO, and save a fresh session — without touching any code.
- **Logging**: `print()` statements with step prefix `[N/N]` — no logging framework needed at this stage.
- **Module boundary**: all Playwright logic lives in `core/services/scraper.py`. The `authenticate()` function is the single public interface — it accepts no arguments, returns an authenticated `Page` object ready for scraping.

## Testing Decisions

- **What makes a good test here**: test the observable outcome (is the returned `Page` on the LMS dashboard URL?) not the implementation (which selectors were clicked). Avoid mocking Playwright internals — they change with versions.
- **Session save/load** (unit-testable): test that if `.sessions/binus_session.json` exists and contains valid JSON, the context is initialized with `storage_state` rather than a fresh context. Mock `playwright.chromium.launch` to avoid a real browser.
- **Auth detection** (unit-testable): test the URL-check logic in isolation — given a URL string containing `/login`, the function should return `False` for `is_authenticated()`.
- **End-to-end login** (integration test): a single `@pytest.mark.integration` test that calls `authenticate()` against the live site using real credentials from `.env`. Skipped automatically if `BINUS_USERNAME` is not set. This is the primary acceptance test.
- **No prior art** in the codebase yet — this is the first test file.

## Out of Scope

- MFA / two-factor authentication (not required for this account)
- Headless mode
- Scheduled or automatic re-runs
- Any data extraction beyond landing on the authenticated dashboard
- Notification or alerting on login failure
- Claude / Anthropic AI integration (deferred)

## Further Notes

- The Microsoft SSO URL in the flow diagram includes `prompt=select_account` — Playwright may encounter an account-picker step if multiple Microsoft accounts are cached. The scraper should target the email input directly and fill `BINUS_USERNAME`, bypassing the picker.
- The two post-login modals are always shown (confirmed in design session) — no conditional logic needed.
- `playwright install chromium` must be run once after `pip install playwright`. Add this to the onboarding instructions in CLAUDE.md.
