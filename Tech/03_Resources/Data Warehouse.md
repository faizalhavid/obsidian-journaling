---
aliases: [Data Warehouse, DWH, OLAP]
tags: [concept, data-engineering, database]
status: to-learn
area: Data Engineering
topic: Storage
source: 
created: 2026-08-21
reviewed: 
difficulty: intermediate
---

# 🏢 Data Warehouse

## 📖 Definisi
> Storage terpusat yang dioptimasi untuk **query analitik (OLAP)** — bukan transaksi (OLTP). Data biasanya sudah di-clean dan di-model (star / snowflake schema) via [[ETL]] / [[ELT]].

## 🔑 Poin Inti
- Column-oriented, kompresi tinggi, cocok untuk agregasi lintas jutaan baris.
- Kontras dengan [[Data Lake]] (raw, schema-on-read) dan [[Lakehouse]] (gabungan).
- Contoh modern: Snowflake, BigQuery, Redshift, ClickHouse.
- Modeling: **Kimball (star schema)** atau **Data Vault**.

## 🔗 Related Concepts
- [[Data Lake]]
- [[Lakehouse]]
- [[ETL]]
- [[ELT]]
- [[Data Modeling]]
- [[SQL]]

## 🗺️ Part of
- [[MOC - Data Engineering]]
- [[MOC - Database]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- Kimball, R. *The Data Warehouse Toolkit*.
