---
aliases: [Vector DB, Vector Database, Vector Store]
tags: [concept, ai-engineering, database]
status: to-learn
area: AI Engineering
topic: Tools
source: 
created: 2026-08-22
reviewed: 
difficulty: intermediate
---

# 🗃️ Vector Database

## 📖 Definisi
> **Vector Database** adalah database yang menyimpan dan mengindeks [[Embeddings]] (vektor berdimensi tinggi) serta mendukung pencarian **similarity search** (mis. cosine / dot product / Euclidean) secara efisien.

## 🔑 Poin Inti
- **ANN Index**: menggunakan algoritma Approximate Nearest Neighbor (HNSW, IVF, PQ) untuk kecepatan.
- **Metadata filtering**: bisa gabungkan filter atribut + similarity search.
- **Building block** utama untuk sistem [[RAG]] dan semantic search.
- **Trade-off**: recall vs latency vs memory.

## 💡 Contoh Tools
- **Managed**: Pinecone, Weaviate Cloud, Qdrant Cloud.
- **Self-hosted**: Qdrant, Milvus, Chroma, pgvector (PostgreSQL extension).

## 🔗 Related Concepts
- [[Embeddings]]
- [[RAG]]
- [[SQL]]
- [[Data Pipeline]]

## 🗺️ Part of
- [[MOC - AI Engineering]]
- [[MOC - Database]]

## 📝 Sumber & Referensi
- 
