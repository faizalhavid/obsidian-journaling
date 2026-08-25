---
aliases: [RAG, Retrieval-Augmented Generation]
tags: [concept, ai-engineering]
status: to-learn
area: AI Engineering
topic: Core Pattern
source: 
created: 2026-08-22
reviewed: 
difficulty: intermediate
---

# 🔎 Retrieval-Augmented Generation (RAG)

## 📖 Definisi
> **RAG** adalah pola arsitektur yang menggabungkan **retrieval** (pencarian dokumen relevan dari knowledge base) dengan **generation** (LLM) sehingga jawaban model berbasis data terkini/privat tanpa perlu fine-tuning.

## 🔑 Poin Inti
- **Indexing**: dokumen dipecah menjadi chunk → dibuat [[Embeddings]] → disimpan di [[Vector Database]].
- **Retrieval**: query user di-embed → cari top-k chunk paling mirip (cosine similarity).
- **Augmentation**: chunk relevan disisipkan ke prompt sebagai konteks.
- **Generation**: LLM menjawab berdasarkan konteks yang di-retrieve.

## 💡 Alur Sederhana
```
User Query
   │
   ▼
[Embedding] ──► [Vector DB search] ──► top-k chunks
                                          │
                                          ▼
                          Prompt + Context ──► LLM ──► Answer
```

## 🔗 Related Concepts
- [[Embeddings]]
- [[Vector Database]]
- [[Large Language Model]]
- [[Prompt Engineering]]
- [[Fine-tuning]]

## 🗺️ Part of
- [[MOC - AI Engineering]]
- [[MOC - Data Engineering]]

## 📝 Sumber & Referensi
- 
