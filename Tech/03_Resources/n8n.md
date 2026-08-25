---
aliases: [n8n, nodemation]
tags: [concept, automation, ai-engineering, devops]
status: to-learn
area: AI Engineering
topic: Automation & Workflow
source: 
created: 2026-08-22
reviewed: 
difficulty: beginner
---

# 🔄 n8n

## 📖 Definisi
> **n8n** (baca: *"n-eight-n"*, singkatan dari *nodemation*) adalah platform **workflow automation** open-source & self-hostable berbasis node — memungkinkan menghubungkan aplikasi, API, dan layanan AI ke dalam alur otomatis tanpa (atau dengan sedikit) kode.

## 🔑 Poin Inti
- **Node-based**: setiap langkah workflow = satu *node* (trigger, action, logic).
- **Fair-code license**: source terbuka, boleh self-host gratis untuk pemakaian internal.
- **400+ integrasi**: Slack, GitHub, Google Sheets, Postgres, HTTP, webhook, dll.
- **AI-native**: punya node khusus untuk [[Large Language Model|LLM]], [[AI Agent]], [[RAG]], [[Vector Database]].
- **Code when needed**: mendukung JavaScript / Python custom node bila perlu logika kompleks.
- **Self-hostable**: Docker / npm / n8n Cloud.

## 🧩 Konsep Utama
- **Trigger Node** → memicu workflow (cron, webhook, event app).
- **Action Node** → melakukan aksi (kirim email, tulis DB, panggil API).
- **Logic Node** → IF, Switch, Merge, Loop.
- **Credentials** → penyimpanan aman untuk API key & OAuth.
- **Executions** → riwayat run workflow (sukses/gagal) untuk debugging.

## 💡 Contoh Use Case
```
[Webhook: form submit]
      │
      ▼
[OpenAI/Claude node: klasifikasi intent]
      │
      ▼
[IF: urgent?] ── yes ──► [Slack: notify tim]
      │
      no
      ▼
[Google Sheets: append row]
```

Contoh lain:
- **AI Agent workflow**: chatbot yang query [[Vector Database]] lalu jawab via LLM.
- **ETL ringan**: sinkron data Airtable → Postgres tiap jam.
- **DevOps automation**: notifikasi Slack saat PR di-merge.

## 🆚 n8n vs Alternatif
| Tool | Model | Catatan |
|---|---|---|
| **n8n** | Fair-code, self-host | Fleksibel, AI-native, bisa custom code |
| Zapier | SaaS, closed | Paling mudah, tapi mahal & tanpa self-host |
| Make (Integromat) | SaaS | Visual, bagus untuk logika kompleks |
| Apache Airflow | Open-source | Fokus data pipeline / DAG, bukan integrasi app |

## 🔗 Related Concepts
- [[AI Agent]]
- [[RAG]]
- [[Large Language Model]]
- [[Vector Database]]
- [[Prompt Engineering]]
- [[Docker]]
- [[CI-CD]]

## 🗺️ Part of
- [[MOC - AI Engineering]]
- [[MOC - DevOps]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- Official docs: https://docs.n8n.io
- GitHub: https://github.com/n8n-io/n8n


---

