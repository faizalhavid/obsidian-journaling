---
aliases: [ACID, ACID Properties]
tags: [concept, database]
status: to-learn
area: Database
topic: Transactions
source: 
created: 2026-08-21
reviewed: 
difficulty: intermediate
---

# 🔒 ACID

## 📖 Definisi
> Empat properti fundamental yang menjamin **integritas transaksi** dalam sistem [[Relational Model]]: **A**tomicity, **C**onsistency, **I**solation, **D**urability.

## 🔑 Poin Inti
- **Atomicity** — transaksi berjalan penuh atau tidak sama sekali.
- **Consistency** — state DB tetap valid sebelum & sesudah transaksi.
- **Isolation** — transaksi paralel tidak saling mengganggu ([[Isolation Levels]]).
- **Durability** — begitu commit sukses, hasil bertahan meski crash.

## 💡 Trade-off
Sistem distribusi sering memilih [[BASE]] (Basically Available, Soft-state, Eventually consistent) daripada ACID demi ketersediaan. Lihat [[CAP Theorem]].

## 🔗 Related Concepts
- [[Transactions]]
- [[Isolation Levels]]
- [[BASE]]
- [[CAP Theorem]]
- [[PostgreSQL]]

## 🗺️ Part of
- [[MOC - Database]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- 
