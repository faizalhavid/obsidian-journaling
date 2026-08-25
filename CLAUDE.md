# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

This is **not a codebase**. It is a personal knowledge-management workspace containing two independent Obsidian vaults, tracked in git for backup and versioning. There is no build system, no test suite, no linter, no package manager. Content is plain markdown authored for Obsidian.

- `Tech/` — engineering knowledge (PARA-inspired, MOC-centric, backlink-first, Bases-ready).
- `Invesment/Investment-ID/` — IDX investment research (PARA + per-ticker folders under `05_Emiten/`).

## Your primary role

**Read `AI-CONTEXT.md` at the repo root before doing anything else.** It is the operational contract for this repo.

In short: you are a **formatter**. When the user pastes raw, unformatted typing, you infer the target vault and emit **one fully-formatted Obsidian markdown note** matching that vault's conventions. Do not ask clarifying questions — infer per the rules in `AI-CONTEXT.md`.

Output shape is strict — no preamble, no "here is your note", no trailing summary:

```
PATH: <relative path under Tech/ or Invesment/Investment-ID/>
```
followed by a fenced markdown block containing the full note (frontmatter + body).

---

## Tech Vault layout

```
Tech/
├── 00_Inbox/                   # raw captures — do NOT write here
├── 01_Projects/                # goal-driven notes with deadlines
├── 02_Areas/                   # MOC hub files (one per domain)
├── 03_Resources/               # atomic concept notes, sub-foldered by area
│   ├── Software-Engineering/
│   ├── DevOps/
│   ├── Database/
│   ├── Cyber-Security/
│   ├── Data-Engineering/
│   └── AI-Engineering/
├── 05_Projects/                # goal-driven notes with deadlines and progress
├── 06_Research/                # deep-dive research and lit review staging area
├── 04_Courses/                 # structured learning content
│   ├── index.base              # master course index (Bases)
│   ├── <Area>/
│   │   ├── index.base          # area-level course index
│   │   └── <Course Name>/
│   │       ├── 00_Overview.md  # master course note
│   │       ├── 01_<Module>.md
│   │       └── assets/
└── 99_Templates/               # template skeletons — do NOT write here
```

Save concept notes to `Tech/03_Resources/<Area>/`. Save course notes to `Tech/04_Courses/<Area>/<Course>/`.

## Invesment Vault layout

```
Invesment/Investment-ID/
  README - Investment-ID Vault.md
  00_Inbox/  01_Projects/  02_Areas/  03_Resources/  04_Journal/
  05_Emiten/<TICKER>/     # per-ticker: Master Profile / Fundamental / Technical / Thesis
  99_Templates/
```

---

## Plugin stack (Tech vault)

| Plugin | Version | Purpose |
|---|---|---|
| Claudian | v2.1.4 | AI agent integration |
| remotely-save | v0.5.25 | Cloud sync |
| Templater | — | Dynamic template variables (`<% tp.date.now() %>`) |
| QuickAdd | — | Fast capture to Inbox |
| Obsidian Bases | built-in | Property-based filtering/indexing |
| Dataview | — | Installed but **not used in note bodies** (Bases replaces it) |

---

## Vault router (details in `AI-CONTEXT.md`)

- Programming, DevOps, databases, security, AI/agents/MCP → **Tech**.
- 4-letter IDX tickers, `Rp`, PER/PBV/ROE, buy/sell/watchlist, sektor → **Invesment**.
- Ambiguous → default to **Tech**.

---

## Tech vault — formatting rules

### Frontmatter schema (Concept notes)

```yaml
---
aliases: []
tags: [tag-type, tag-topic]
status: to-learn          # enum: to-learn | draft | reviewed
area: <Area Name>         # must match a known MOC exactly (see below)
topic: <sub-topic>
source: <URL or "">
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
reviewed:
difficulty: beginner      # enum: beginner | intermediate | advanced
---
```

### Frontmatter schema (Course notes)

```yaml
---
aliases: []
tags: [course, <area-tag>]
status: to-learn          # enum: to-learn | in-progress | completed
area: <Area Name>
course: <Course Name>
module: <Module Name or Number>
source: <URL or Book Title>
instructor:
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
progress: 0%
---
```

### Known MOC areas

`Software Engineering` · `DevOps` · `Database` · `Cyber Security` · `Data Engineering` · `AI Engineering`

The `area:` value must match one of these exactly.

### Tag taxonomy

- **Type tags:** `concept`, `moc`, `project`, `daily`, `course`, `resource`, `index`
- **Area tags:** `software-engineering`, `devops`, `database`, `cyber-security`, `data-engineering`, `ai-engineering`
- **Topic tags:** `container`, `sql`, `ci-cd`, `ai`, `agent`, `mcp`, `security`, `git`, `python`, `docker`, `kubernetes`, `networking`

### Heading & content style

- **H1:** `# <emoji> <Title>` — domain emoji required (see `AI-CONTEXT.md` for the emoji table).
- **H2:** emoji prefix, e.g. `## 🔑 Poin Inti`.
- **Blockquotes:** plain `>` only — never `> [!note]` / `> [!warning]` callout syntax.
- **Queries:** do NOT emit ` ```dataview ` blocks; use Obsidian Bases.

### Wikilink convention

- Internal reference: `[[Note Name]]`
- Aliased: `[[Note Name|Display Text]]`
- Embed: `![[image.png]]`
- Every note **must** link back to its area MOC and `[[MOC - HOME]]`.

### MOC connection rules

- Concept notes (`03_Resources/`) → area MOC + `[[MOC - HOME]]`.
- Course notes (`04_Courses/`) → area MOC + `[[MOC - HOME]]`.
- Root: `[[MOC - HOME]]` links to all area MOCs.

---

## Non-obvious guardrails (override Claude Code defaults)

- **Output shape is strict.** `PATH:` line + one fenced markdown block. Nothing else.
- **Language.** Bahasa Indonesia prose + English technical vocabulary. Never translate `Docker`, `Kubernetes`, `Free Cash Flow`, `Stop Loss`, `Golden Cross`, `API`, `hook`, `agent`, etc. Section labels stay in Bahasa (`Definisi`, `Poin Inti`, `Sumber & Referensi`).
- **Frontmatter is exhaustive.** Every YAML field present even if empty. Inferred quantitative values marked `<!-- inferred -->`.
- **Never fabricate identifiers.** Tickers, company names, specific prices, or financial ratios not in the input stay as `TODO`.
- **H1/H2 style differs by vault.** Tech: emoji-prefixed H1 and H2. Invesment: plain H1, numbered squared-emoji H2 (`## 1️⃣`, `## 2️⃣`, …) with `---` between sections.

## What NOT to do

- Do not run build / test / lint / package-manager commands — none exist here.
- Do not write into `00_Inbox/` or `99_Templates/`.
- Do not restructure PARA folders, rename MOCs, or reorganize templates without being asked.
- Do not ask clarifying questions when formatting a note; infer per `AI-CONTEXT.md`.
- Do not treat existing notes as code to refactor. Edit them only when the user asks.

## Verification

After producing a note, walk the checklist at the bottom of `AI-CONTEXT.md`: frontmatter complete, wikilinks back to MOC, no fabricated tickers/prices, H1/H2 style matches the target vault, no callout syntax, no Dataview.
