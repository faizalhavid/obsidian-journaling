---
aliases: [Sub-agent, Subagent]
tags: [concept, ai, software-engineering]
status: reviewed
area: Software Engineering
topic: AI-Assisted Development
source: Anthropic Docs
created: 2026-08-21
reviewed: 2026-08-21
difficulty: intermediate
---

# 🧩 Sub-agent

## 📖 Definisi
> Agent turunan yang dijalankan di background untuk mengerjakan sub-task berat, hanya mengembalikan hasil ringkas ke context utama — menjaga [[Claude Code]] tetap fokus dan hemat context window.

## 🔑 Poin Inti
- **Isolated context**: sub-agent tidak membebani main window.
- **Ideal use**: [[Code Review]], riset multi-file, refactor besar.
- **Persistent memory** (opsional): retain memory antar sesi.
- **Preload skills** via key `skill` — seluruh skill di-load ke sub-agent context.

## 🔗 Related Concepts
- [[AI Agent]]
- [[Claude Code]]
- [[Prompt Engineering]]
- [[CLAUDE.md]]

## 🗺️ Part of
- [[MOC - Software Engineering]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- Original capture: `Agent.md` bagian "Subagent"
