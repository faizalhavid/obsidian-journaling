---
aliases: [Git, Version Control]
tags: [concept, software-engineering, devops]
status: to-learn
area: Software Engineering
topic: Version Control
source: 
created: 2026-08-21
reviewed: 
difficulty: beginner
---

# 🌿 Git

## 📖 Definisi
> Sistem **distributed version control** yang melacak setiap perubahan file dalam bentuk commit ber-hash. Fondasi kolaborasi kode modern dan syarat mutlak [[CI-CD]].

## 🔑 Poin Inti
- **Working tree → Staging → Commit → Push**.
- **Branch murah** — dorong feature-branch workflow.
- **Merge vs Rebase** — dua strategi integrasi, trade-off history vs linearity.
- **Remote** (origin, upstream) — sinkronisasi antar developer.

## 💡 Alur Sehari-hari
```bash
git checkout -b feat/new-endpoint
# ...edit code
git add -p
git commit -m "feat: add /users search endpoint"
git push -u origin feat/new-endpoint
# buat PR / MR
```

## 🔗 Related Concepts
- [[CI-CD]]
- [[Code Review]]
- [[GitHub Actions]]
- [[Version Control]]

## 🗺️ Part of
- [[MOC - Software Engineering]]
- [[MOC - DevOps]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- https://git-scm.com/book
