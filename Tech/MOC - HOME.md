---
aliases: [Home, Tech Hub, Peta Utama]
tags: [moc, home]
status: reviewed
area: Meta
created: 2026-08-21
---

# 🏠 MOC - HOME (Tech Vault)

> Titik masuk utama vault **"Tech"**. Semua bidang pengetahuan bercabang dari sini.
> Vault ini mengikuti struktur PARA-inspired + MOC-centric — folder hanya untuk penyimpanan fisik, koneksi ide dilakukan lewat backlinks.

---

## 🌐 Peta Bidang (Areas)

- [[MOC - Software Engineering]]
- [[MOC - Database]]
- [[MOC - DevOps]]
- [[MOC - Data Engineering]]
- [[MOC - Cyber Security]]

---

## 🔁 Interkoneksi Antar Bidang

- **Software Engineering ⇄ DevOps** → [[CI-CD]], [[Git]], [[Testing]]
- **Database ⇄ Data Engineering** → [[SQL]], [[Data Modeling]], [[ETL]]
- **DevOps ⇄ Cyber Security** → [[Network]], [[Secrets Management]], [[Container Security]]
- **Data Engineering ⇄ DevOps** → [[Docker]], [[Kubernetes]], [[Orchestration]]
- **Software Engineering ⇄ Cyber Security** → [[Secure Coding]], [[OWASP Top 10]]
- **Software Engineering ⇄ Data Engineering** → [[Python]], [[API Design]]

---

## 📥 Alur Kerja (Workflow)

```
Capture   →   00_Inbox          (catatan mentah, ide lepas)
Klasifikasi →  Tautkan ke MOC   (Areas/Resources)
Proyek    →   01_Projects        (goal aktif dengan deadline)
Arsip     →   Tetap di Resources (kalau evergreen)
```

- [[00_Inbox]] → proses catatan mentah
- [[01_Projects]] → proyek aktif
- Belum dikategorikan? Mulai dari sini, lalu link ke MOC bidang.

---

## 📊 Dashboard (Bases)

Lihat file `99_Templates/Dashboard.base` untuk tampilan database.
Views yang tersedia:

- **Semua Konsep Tech** — daftar seluruh atomic notes
- **Perlu Dipelajari** — filter `status: to-learn`
- **Sudah Direview** — filter `status: reviewed`
- **Per Bidang** — filter berdasarkan `area`

---

## 🧭 Panduan Cepat

- Buat catatan baru? Gunakan `[[99_Templates/Template - Concept]]`.
- Buat MOC baru? Gunakan `[[99_Templates/Template - MOC]]`.
- Buat proyek baru? Gunakan `[[99_Templates/Template - Project]]`.
- Jangan pernah buat catatan tanpa **minimal 1 backlink** ke MOC.

---

## 🔗 Meta

- Vault: **Tech** (single vault, shallow structure)
- Struktur: `00_Inbox / 01_Projects / 02_Areas / 03_Resources / 99_Templates`
- Prinsip: **MOC-centric, backlink-first, Bases-ready**
