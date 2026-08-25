---
aliases: [Embeddings, Vector Embeddings]
tags: [concept, ai-engineering]
status: to-learn
area: AI Engineering
topic: Foundations
source: 
created: 2026-08-22
reviewed: 
difficulty: intermediate
---

# 🧮 Embeddings

## 📖 Definisi
> **Embeddings** adalah representasi numerik (vektor berdimensi tinggi) dari teks, gambar, atau data lain — di mana kedekatan geometris (mis. cosine similarity) mencerminkan kemiripan semantik.

## 🔑 Poin Inti
- **Semantic space**: teks dengan makna serupa berdekatan di ruang vektor.
- **Fixed dimension**: setiap model punya ukuran tetap (mis. 1536, 3072).
- **Foundation for search**: dasar dari [[RAG]], semantic search, clustering, recommendation.
- **Model-specific**: embedding dari model berbeda tidak kompatibel.

## 💡 Contoh
```
"anjing"  → [0.12, -0.44, 0.87, ...]
"kucing"  → [0.15, -0.40, 0.85, ...]   # dekat
"mobil"   → [0.90,  0.12, -0.33, ...]  # jauh
```

## 🔗 Related Concepts
- [[Vector Database]]
- [[RAG]]
- [[Large Language Model]]
- [[Tokenization]]

## 🗺️ Part of
- [[MOC - AI Engineering]]
- [[MOC - Data Engineering]]

## 📝 Sumber & Referensi
- 
