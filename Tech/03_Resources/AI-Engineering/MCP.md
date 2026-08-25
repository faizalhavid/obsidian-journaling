---
aliases: [MCP, Model Context Protocol]
tags: [concept, ai, integration]
status: reviewed
area: Software Engineering
topic: AI-Assisted Development
source: Anthropic Docs
created: 2026-08-21
reviewed: 2026-08-21
difficulty: intermediate
---

# 🔌 MCP (Model Context Protocol)

## 📖 Definisi
> Protokol yang menghubungkan [[Claude Code]] ke tools & data sources eksternal (Slack, Jira, GitHub, database). MCP server memberi Claude "hands & eyes" ke sistem di luar filesystem lokal.

## 🔑 Poin Inti
- Tambah server: `claude mcp add`.
- Scope proyek: taruh di `.mcp.json` → seluruh tim otomatis dapat.
- **Watch context**: disable server yang tidak dipakai — masing-masing membawa schema tools.
- Cocok untuk integrasi observability, ticketing, chat, cloud provider.

## 🔗 Related Concepts
- [[Claude Code]]
- [[AI Agent]]
- [[Claude Code Hooks]]
- [[CLAUDE.md]]

## 🗺️ Part of
- [[MOC - Software Engineering]]
- [[MOC - DevOps]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- Original capture: `Agent.md` bagian "MCP"
