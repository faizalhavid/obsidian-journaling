---
aliases: [ETL, Extract Transform Load]
tags: [concept, data-engineering]
status: to-learn
area: Data Engineering
topic: Pipeline
source: 
created: 2026-08-21
reviewed: 
difficulty: intermediate
---

# 🚚 ETL (Extract, Transform, Load)

## 📖 Definisi
> Pola klasik data pipeline: **Extract** dari sumber → **Transform** (cleaning, join, aggregate) → **Load** ke [[Data Warehouse]] / [[Data Lake]].

## 🔑 Poin Inti
- Cocok saat compute mahal & warehouse ekspensif (harus siap-load).
- Kontras dengan [[ELT]] — transform di dalam warehouse setelah load (modern approach dengan Snowflake/BigQuery).
- Umumnya diorkestrasi via [[Airflow]] atau [[dbt]] (untuk ELT).
- Ideal untuk [[Batch vs Streaming]] batch job harian/jam.

## 💡 Contoh Sederhana
```python
# Extract
df = pd.read_sql("SELECT * FROM raw_orders", src)
# Transform
df["total"] = df["qty"] * df["price"]
df = df[df["total"] > 0]
# Load
df.to_sql("fact_orders", target, if_exists="append")
```

## 🔗 Related Concepts
- [[ELT]]
- [[Data Pipeline]]
- [[Airflow]]
- [[dbt]]
- [[Data Warehouse]]
- [[SQL]]

## 🗺️ Part of
- [[MOC - Data Engineering]]
- [[MOC - Database]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- 
