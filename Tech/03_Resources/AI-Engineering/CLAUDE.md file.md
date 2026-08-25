---
aliases: [CLAUDE.md, Project Context File]
tags: [concept, ai, software-engineering]
status: reviewed
area: Software Engineering
topic: AI-Assisted Development
source: Anthropic Docs
created: 2026-08-21
reviewed: 2026-08-21
difficulty: beginner
---

# 📄 CLAUDE.md file

## 📖 Definisi
> File konteks proyek yang dibaca [[Claude Code]] otomatis untuk memahami stack, konvensi, dan perintah proyek. Investasi kecil dengan return besar dalam produktivitas.

## 🔑 Poin Inti
- Berisi: **stack**, **preferences**, **commands**, **code style**, dan konvensi lokal.
- Dibaca setiap sesi — membuat agent segera "in-context" tanpa perlu re-explain.
- Dapat ditingkatkan iteratif seiring proyek berkembang.

## 💡 Contoh
```markdown
# Project
Next.js 15 dengan App Router, Tailwind, Drizzle ORM.

# Commands
- Dev server: `pnpm dev`
- Run tests: `pnpm test`
- Lint: `pnpm lint`

# Code Style
- 2-space indentation
- Named exports
- API routes di app/api/
- Prefer server actions
```

## 🔗 Related Concepts
- [[Claude Code]]
- [[AI Agent]]
- [[Sub-agent]]
- [[Prompt Engineering]]

## 🗺️ Part of
- [[MOC - Software Engineering]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- Original capture: `Agent.md` bagian "The CLAUDE.md File"
