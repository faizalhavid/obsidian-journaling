---
aliases: [Apache Kafka, Kafka]
tags: [concept, data-engineering, devops]
status: to-learn
area: Data Engineering
topic: Streaming
source: 
created: 2026-08-21
reviewed: 
difficulty: advanced
---

# 📨 Apache Kafka

## 📖 Definisi
> Distributed **event streaming platform** yang menyimpan aliran event dalam topic tahan lama (append-only log) dan mendistribusikannya ke banyak consumer secara horizontal-scalable.

## 🔑 Poin Inti
- **Topic → Partition → Offset**.
- **Producer** menulis, **Consumer** membaca dari offset tertentu (replay-able).
- Delivery: at-least-once (default), exactly-once (dengan transactions + idempotent producer).
- Fondasi arsitektur event-driven ([[Event-Driven Architecture]]) & real-time [[Data Pipeline]].

## 🔗 Related Concepts
- [[Data Pipeline]]
- [[Apache Spark]]
- [[Event-Driven Architecture]]
- [[Batch vs Streaming]]
- [[Docker]]
- [[Kubernetes]]

## 🗺️ Part of
- [[MOC - Data Engineering]]
- [[MOC - Software Engineering]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- https://kafka.apache.org/documentation/
