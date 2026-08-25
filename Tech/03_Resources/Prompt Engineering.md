---
aliases: [Prompt Engineering, Prompting]
tags: [concept, ai-engineering]
status: to-learn
area: AI Engineering
topic: Core Practice
source: 
created: 2026-08-22
reviewed: 
difficulty: beginner
---

# ✍️ Prompt Engineering

## 📖 Definisi
> **Prompt Engineering** adalah praktik merancang instruksi (prompt) agar LLM menghasilkan output yang akurat, konsisten, dan sesuai tujuan — tanpa mengubah bobot model.

## 🔑 Poin Inti
- **Clarity**: prompt yang spesifik & tidak ambigu menghasilkan output lebih baik.
- **Structure**: gunakan role, context, task, constraint, output format.
- **Few-shot vs Zero-shot**: beri contoh untuk task yang kompleks.
- **Chain-of-Thought**: minta model "berpikir langkah demi langkah" untuk reasoning.

## 💡 Teknik Umum
- Role prompting: `"You are a senior Python engineer..."`
- XML tags untuk struktur (khas Claude): `<task>...</task>`
- Output formatting: minta JSON / Markdown / tabel.
- Prompt chaining: pecah task besar menjadi beberapa prompt bertahap.

## 🔗 Related Concepts
- [[Large Language Model]]
- [[AI Agent]]
- [[Context Window]]
- [[RAG]]
- [[Fine-tuning]]

## 🗺️ Part of
- [[MOC - AI Engineering]]
- [[MOC - Software Engineering]]

## 📝 Sumber & Referensi
- Anthropic Prompt Engineering Guide
