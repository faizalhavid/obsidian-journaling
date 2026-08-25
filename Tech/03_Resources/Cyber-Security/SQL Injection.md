---
aliases: [SQL Injection, SQLi]
tags: [concept, cyber-security, database]
status: to-learn
area: Cyber Security
topic: Application Security
source: OWASP
created: 2026-08-21
reviewed: 
difficulty: intermediate
---

# 💉 SQL Injection

## 📖 Definisi
> Kelas serangan yang menyisipkan **[[SQL]] statement jahat** melalui input aplikasi karena query dirakit lewat konkatenasi string, bukan parameterized query. Bagian dari kategori Injection [[OWASP Top 10]].

## 🔑 Poin Inti
- **Root cause**: user input dipercaya masuk ke SQL secara mentah.
- **Mitigasi utama**: **parameterized queries / prepared statements** — bukan input sanitization.
- Gunakan **least privilege** DB user + WAF sebagai lapisan tambahan.
- Setara di NoSQL: **NoSQL injection** (e.g. `$where` di MongoDB).

## 💡 Contoh Rentan vs Aman
```python
# ❌ RENTAN
cursor.execute(f"SELECT * FROM users WHERE name = '{name}'")

# ✅ AMAN — parameterized
cursor.execute("SELECT * FROM users WHERE name = %s", (name,))
```

## 🔗 Related Concepts
- [[OWASP Top 10]]
- [[Secure Coding]]
- [[SQL]]
- [[XSS]]
- [[Authentication]]

## 🗺️ Part of
- [[MOC - Cyber Security]]
- [[MOC - Database]]
- [[MOC - Software Engineering]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- https://owasp.org/www-community/attacks/SQL_Injection
