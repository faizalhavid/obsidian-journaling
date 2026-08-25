---
aliases: [AI Agent, Agent, LLM Agent]
tags: [concept, ai, software-engineering]
status: reviewed
area: Software Engineering
topic: AI-Assisted Development
source: Anthropic Claude Code Docs
created: 2026-08-19
reviewed: 2026-08-21
difficulty: intermediate
---

# 🤖 AI Agent

## 📖 Definisi
> AI Agent adalah perangkat lunak yang berinteraksi dengan lingkungannya dan mengambil aksi untuk mencapai tujuan tertentu. Intinya: sebuah **LLM yang beroperasi dalam loop** secara real-time, dengan akses ke tools, layanan eksternal, atau agent lain.

![[Pasted image 20260819192233.png]]

## 🔑 Poin Inti
- **Loop-based**: bekerja iteratif — prompt → gather context → action → verify → loop / done.
- **Tools access**: dapat memanggil tools (baca file, jalankan perintah, panggil API).
- **Sub-agent capable**: dapat mendelegasikan sub-task ke agent lain agar context window tetap bersih.
- **Verifiable**: setiap langkah divalidasi terhadap tujuan sebelum lanjut / berhenti.

## 🔁 Agentic Loop
1. User memasukkan prompt ke [[Claude Code]].
2. Model mengumpulkan konteks (mengembalikan teks atau tool call).
3. Claude Code mengeksekusi aksi (edit file / run command).
4. Verifikasi hasil terhadap tujuan.
5. Selesai → tunggu prompt berikutnya, atau ulang loop.

![[Pasted image 20260819192607.png]]

## 🧭 Context Management
- Gunakan `/compact` untuk merangkum sesi panjang.
- Gunakan `/clear` untuk memulai bersih.
- Prompt spesifik, monitor pemakaian context, delegasikan ke [[Sub-agent]] jika hanya butuh hasilnya.

## 🔗 Related Concepts
- [[Claude Code]]
- [[Prompt Engineering]]
- [[Sub-agent]]
- [[MCP]]
- [[Claude Code Hooks]]
- [[CLAUDE.md]]

## 🗺️ Part of
- [[MOC - Software Engineering]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- Anthropic Claude Code Documentation
- Original capture: `Agent.md` (2026-08-19)
