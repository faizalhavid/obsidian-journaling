---
aliases: [SQL, Structured Query Language]
tags: [concept, database, data-engineering]
status: to-learn
area: Database
topic: Query Language
source: 
created: 2026-08-21
reviewed: 
difficulty: beginner
---

# 🧾 SQL

## 📖 Definisi
> Bahasa deklaratif untuk membaca dan memanipulasi data dalam sistem [[Relational Model]]. Standar de facto di seluruh RDBMS ([[PostgreSQL]], [[MySQL]], SQLite) dan sebagian besar [[Data Warehouse]].

## 🔑 Poin Inti
- **DDL** (Data Definition): `CREATE`, `ALTER`, `DROP`.
- **DML** (Data Manipulation): `SELECT`, `INSERT`, `UPDATE`, `DELETE`.
- **DCL / TCL**: `GRANT`, `REVOKE`, `COMMIT`, `ROLLBACK`.
- Optimasi bergantung pada [[Indexing]] & [[Query Optimization]].

## 💡 Contoh
```sql
SELECT u.name, COUNT(o.id) AS total_orders
FROM users u
LEFT JOIN orders o ON o.user_id = u.id
WHERE u.created_at >= '2026-01-01'
GROUP BY u.name
ORDER BY total_orders DESC
LIMIT 10;
```

## 🔗 Related Concepts
- [[Relational Model]]
- [[Data Modeling]]
- [[Indexing]]
- [[Query Optimization]]
- [[ETL]]
- [[ORM]]

## 🗺️ Part of
- [[MOC - Database]]
- [[MOC - Data Engineering]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- 
