---
aliases: [Claude Code Hooks, CC Hooks]
tags: [concept, ai, devops, automation]
status: reviewed
area: Software Engineering
topic: AI-Assisted Development
source: Anthropic Docs
created: 2026-08-21
reviewed: 2026-08-21
difficulty: intermediate
---

# 🪝 Claude Code Hooks

## 📖 Definisi
> Mekanisme kontrol **deterministik** untuk perilaku [[Claude Code]] — perintah shell yang dijalankan otomatis pada event tertentu (sebelum/sesudah tool call, saat prompt masuk, saat sesi berhenti).

## 🔑 Poin Inti
Available events:
- **PreToolUse** — sebelum tool call → gunakan untuk blokir operasi berbahaya.
- **PostToolUse** — setelah tool call → gunakan untuk auto-format, logging.
- **UserPromptSubmit** — saat user submit prompt.
- **Stop** — saat Claude selesai merespons.
- **Notification** — saat notifikasi dikirim.

## 💡 Konfigurasi
- Via slash command `/hooks` atau edit langsung `settings.json`.
- Commit ke repo → seluruh tim otomatis dapat.

## 🔗 Related Concepts
- [[Claude Code]]
- [[AI Agent]]
- [[MCP]]
- [[CI-CD]]
- [[CLAUDE.md]]

## 🗺️ Part of
- [[MOC - Software Engineering]]
- [[MOC - DevOps]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- Original capture: `Agent.md` bagian "Hooks"
