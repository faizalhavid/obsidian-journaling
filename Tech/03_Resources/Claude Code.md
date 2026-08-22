---
aliases: [Claude Code, CC CLI]
tags: [concept, ai, tools, software-engineering]
status: reviewed
area: Software Engineering
topic: AI-Assisted Development
source: Anthropic Docs
created: 2026-08-21
reviewed: 2026-08-21
difficulty: beginner
---

# 🧠 Claude Code

## 📖 Definisi
> CLI resmi Anthropic untuk berinteraksi dengan Claude sebagai [[AI Agent]] di terminal, IDE, atau web. Menjalankan **agentic loop** dengan akses tools (file editing, shell, MCP, sub-agents).

## 🔑 Poin Inti
- **Multi-surface**: tersedia sebagai CLI, VS Code / JetBrains extension, Desktop, Web (claude.ai/code).
- **Slash commands**: `/compact`, `/clear`, `/hooks`, `/commit-push-pr`, `--from-pr`.
- **Extensible**: [[MCP]] untuk external tools, [[Claude Code Hooks]] untuk kontrol deterministik, [[Sub-agent]] untuk parallel work.
- **Configurable**: `settings.json` untuk hooks & permissions, [[CLAUDE.md]] untuk project context.

## 💡 Workflow Sederhana
```
User Prompt → Claude gathers context → Tool call / edit → Verify → Loop or Done
```

## 🔗 Related Concepts
- [[AI Agent]]
- [[Sub-agent]]
- [[CLAUDE.md]]
- [[MCP]]
- [[Claude Code Hooks]]
- [[Prompt Engineering]]

## 🗺️ Part of
- [[MOC - Software Engineering]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- https://docs.anthropic.com/claude/docs/claude-code
