---
aliases: [Vault Context, Agent Context, Vault Map]
tags: [index, meta]
status: reviewed
area: Meta
created: 2026-08-25
last_updated: 2026-08-25
---

# 🗺️ VAULT-CONTEXT — Tech Vault Agent Reference

> Dokumen ini adalah **referensi lengkap vault Tech** untuk AI agent. Berisi peta folder, inventaris note, konvensi penulisan, skema frontmatter, dan cara navigasi. Baca ini sebelum membuat, mengedit, atau mencari note apapun.

---

## 1. Identitas Vault

- **Nama vault**: Tech
- **Tujuan**: Personal knowledge base bidang software engineering, DevOps, database, cyber security, data engineering, dan AI engineering.
- **Arsitektur**: PARA-inspired + MOC-centric + backlink-first + Obsidian Bases-ready.
- **Bahasa**: Bahasa Indonesia (prose) + English (technical terms — jangan diterjemahkan).

---

## 2. Struktur Folder

```
Tech/
├── 00_Inbox/           Capture mentah — jangan tulis langsung ke sini
├── 02_Areas/           MOC hub notes (satu per domain knowledge)
├── 03_Resources/       Atomic concept notes, dikelompokkan per area
│   ├── AI-Engineering/
│   ├── Cyber-Security/
│   ├── Data-Engineering/
│   ├── Database/
│   ├── DevOps/
│   ├── Diagrams/       Excalidraw drawings
│   └── Software-Engineering/
├── 04_Courses/         Structured learning (sub-folder per area)
│   └── AI-Engineering/
├── 05_Projects/        Goal-driven project notes dengan deadline
├── 06_Research/        Deep-dive research, staging sebelum ke 03_Resources/
├── 07_Playground/      Notebook & skrip eksperimen (berpasangan dengan courses/concepts)
├── 99_Templates/       Template Templater — JANGAN tulis note di sini
├── MOC - HOME.md       Titik masuk utama vault
└── VAULT-CONTEXT.md    File ini
```

---

## 3. Inventaris Note Lengkap

### 🗺️ MOC Hub (02_Areas/) — 6 notes

| File | Domain |
|---|---|
| `MOC - AI Engineering.md` | LLM, agent, RAG, MCP, Claude Code |
| `MOC - Cyber Security.md` | OWASP, CIA Triad, secrets, container security |
| `MOC - Data Engineering.md` | ETL, pipeline, warehouse, Kafka |
| `MOC - Database.md` | SQL, relational model, ACID |
| `MOC - DevOps.md` | Docker, Kubernetes, CI/CD |
| `MOC - Software Engineering.md` | Git, paradigma, arsitektur |

---

### 🧠 AI Engineering (03_Resources/AI-Engineering/) — 12 notes

| Note | Topik Singkat |
|---|---|
| `AI Agent.md` | Autonomous agent loop, tool use |
| `CLAUDE.md file.md` | Claude Code project instructions |
| `Claude Code Hooks.md` | Lifecycle hooks di Claude Code |
| `Claude Code.md` | CLI tool Anthropic |
| `Embeddings.md` | Vector representasi teks |
| `Fine-tuning.md` | Adaptasi model ke domain spesifik |
| `Large Language Model.md` | Arsitektur dan cara kerja LLM |
| `MCP.md` | Model Context Protocol |
| `Prompt Engineering.md` | Teknik merancang prompt efektif |
| `RAG.md` | Retrieval-Augmented Generation |
| `Sub-agent.md` | Orchestrasi multi-agent |
| `Vector Database.md` | Database untuk embedding similarity search |

---

### 🛡️ Cyber Security (03_Resources/Cyber-Security/) — 5 notes

| Note | Topik Singkat |
|---|---|
| `CIA Triad.md` | Confidentiality, Integrity, Availability |
| `Container Security.md` | Keamanan Docker/Kubernetes container |
| `OWASP Top 10.md` | 10 kerentanan web paling umum |
| `Secrets Management.md` | Pengelolaan API key, credential, secret |
| `SQL Injection.md` | Serangan injeksi SQL dan mitigasi |

---

### 📊 Data Engineering (03_Resources/Data-Engineering/) — 6 notes

| Note | Topik Singkat |
|---|---|
| `Apache Kafka.md` | Distributed event streaming platform |
| `Data Modeling.md` | Skema, normalisasi, dimensional modeling |
| `Data Pipeline.md` | Alur transformasi data end-to-end |
| `Data Warehouse.md` | Penyimpanan analitik terpusat |
| `ETL.md` | Extract, Transform, Load pattern |
| `n8n.md` | Low-code workflow automation |

---

### 🧾 Database (03_Resources/Database/) — 3 notes

| Note | Topik Singkat |
|---|---|
| `ACID.md` | Atomicity, Consistency, Isolation, Durability |
| `Relational Model.md` | Tabel, relasi, kunci, normalisasi |
| `SQL.md` | Query language untuk relational DB |

---

### 🔁 DevOps (03_Resources/DevOps/) — 3 notes

| Note | Topik Singkat |
|---|---|
| `CI-CD.md` | Continuous Integration / Continuous Delivery |
| `Docker.md` | Containerization |
| `Kubernetes.md` | Container orchestration |

---

### 💻 Software Engineering (03_Resources/Software-Engineering/) — 1 note

| Note | Topik Singkat |
|---|---|
| `Git.md` | Version control system |

---

### 🎓 Courses (04_Courses/) — 1 note

| File | Course | Modul | Progress |
|---|---|---|---|
| `AI-Engineering/Anthropic Skilljar.md` | Anthropic Skilljar | 3 - Building with the Claude API | 40% |

---

### 📁 Projects & Research — kosong (siap diisi)

- `05_Projects/` — gunakan `Template - Project.md`
- `06_Research/` — gunakan `Template - Research.md`

---

## 4. Template Inventory (99_Templates/)

| Template | Untuk | Folder tujuan |
|---|---|---|
| `Template - Concept.md` | Atomic concept note | `03_Resources/<Area>/` |
| `Template - MOC.md` | Map of Content hub | `02_Areas/` |
| `Template - Project.md` | Project aktif | `05_Projects/` |
| `Template - Research.md` | Deep-dive research | `06_Research/` |
| `Template - Daily Note.md` | Catatan harian | `04_Journal/Daily/` |
| `Template - Course Overview.md` | Master course note | `04_Courses/<Area>/<Course>/` |
| `Template - Course Module.md` | Per-modul course note | `04_Courses/<Area>/<Course>/` |
| `Dashboard.base` | Obsidian Bases index | (bukan template note) |

---

## 5. Frontmatter Skema Cepat

### Concept note
```yaml
aliases: []
tags: [concept, <area-tag>]
status: to-learn | draft | reviewed
area: <Area Name>
topic: <sub-topic>
source: <URL or "">
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
reviewed:
difficulty: beginner | intermediate | advanced
```

### MOC note
```yaml
tags: [moc, <area-tag>]
status: draft | reviewed
area: Meta
created: YYYY-MM-DD
```

### Project note
```yaml
tags: [project]
status: active | completed | on-hold
area: <Area Name>
deadline: YYYY-MM-DD
progress: 0%
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
```

### Research note
```yaml
tags: [research, <area-tag>]
status: draft | reviewed
area: <Area Name>
topic: <sub-topic>
source: <URL or "">
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
```

### Course module note
```yaml
tags: [course, <area-tag>]
status: to-learn | in-progress | completed
area: <Area Name>
course: <Course Name>
module: <Module Number - Title>
source: <URL>
instructor:
progress: 0%
created: YYYY-MM-DD
last_updated: YYYY-MM-DD
```

---

## 6. Area Tags & Known MOC Areas

| Folder name | `area:` value (exact) | Tag |
|---|---|---|
| AI-Engineering | `AI Engineering` | `ai-engineering` |
| Cyber-Security | `Cyber Security` | `cyber-security` |
| Data-Engineering | `Data Engineering` | `data-engineering` |
| Database | `Database` | `database` |
| DevOps | `DevOps` | `devops` |
| Software-Engineering | `Software Engineering` | `software-engineering` |

`area:` value di frontmatter **harus persis** sama dengan nilai di atas — dipakai untuk filter di Obsidian Bases.

---

## 7. Wikilink & Syntax Conventions

- Internal link: `[[Note Name]]` — selalu gunakan wikilink, bukan markdown link `[text](path)` untuk note internal.
- Aliased: `[[Note Name|display text]]`
- Embed image: `![[image.png]]`
- Blockquote: `>` biasa — **jangan** gunakan `> [!note]` callout syntax.
- Code block: selalu sertakan language tag (` ```python`, ` ```yaml`, dll).
- Horizontal rule: `---` (dipakai di Invesment vault antar section; opsional di Tech).
- Tidak boleh ada ` ```dataview ` blocks — gunakan Obsidian Bases.

---

## 8. Cara Navigasi Vault

```
Mulai dari: MOC - HOME
    ↓
Area MOC (02_Areas/) — misal: MOC - AI Engineering
    ↓
Concept notes (03_Resources/AI-Engineering/)
    ↓
Cross-links ke concept notes lain atau ke course notes (04_Courses/)
```

**Hubungan antar area** (cross-domain links yang sudah ada di MOC - HOME):
- AI Engineering ↔ Data Engineering → `[[Embeddings]]`, `[[Vector Database]]`, `[[RAG]]`
- AI Engineering ↔ Software Engineering → `[[AI Agent]]`, `[[Prompt Engineering]]`, `[[MCP]]`
- DevOps ↔ Cyber Security → `[[Secrets Management]]`, `[[Container Security]]`
- Database ↔ Data Engineering → `[[SQL]]`, `[[Data Modeling]]`, `[[ETL]]`
- Software Engineering ↔ Cyber Security → `[[OWASP Top 10]]`, `[[SQL Injection]]`

---

## 9. Aturan Penulisan untuk AI Agent

1. **Output shape**: saat memproduksi note, emit `PATH:` line diikuti fenced markdown block. Tidak ada prose sebelum atau sesudahnya.
2. **Jangan tulis ke**: `00_Inbox/`, `99_Templates/`.
3. **Jangan mengarang**: ticker, nama perusahaan, angka finansial yang tidak ada di input → `TODO`.
4. **Setiap note harus backlink** ke area MOC dan `[[MOC - HOME]]`.
5. **Inferred values** ditandai `<!-- inferred -->`.
6. **Spec lengkap**: lihat `AI-CONTEXT.md` di root repo (satu folder di atas `Tech/`).
