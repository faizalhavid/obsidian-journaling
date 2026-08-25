---
aliases: [Docker, Containerization]
tags: [concept, devops, data-engineering, cyber-security]
status: to-learn
area: DevOps
topic: Containerization
source: 
created: 2026-08-21
reviewed: 
difficulty: intermediate
---

# 🐳 Docker

## 📖 Definisi
> Platform containerization yang mengemas aplikasi + dependency-nya ke dalam **container image** yang portable dan reproducible. Menyelesaikan masalah "works on my machine".

## 🔑 Poin Inti
- **Image** — blueprint statis (layer-based).
- **Container** — instance runtime dari image.
- **Dockerfile** — resep build image.
- **Registry** — tempat menyimpan image (Docker Hub, GHCR, ECR).
- Cocok untuk [[CI-CD]], microservices, reproducible data pipelines.

## 💡 Contoh Dockerfile
```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD ["python", "main.py"]
```

## ⚠️ Security Notes
- Jangan pakai `:latest` di production.
- Scan image ([[Container Security]]) — Trivy, Snyk.
- Jangan simpan secret di image — pakai [[Secrets Management]].

## 🔗 Related Concepts
- [[Kubernetes]]
- [[Container Security]]
- [[CI-CD]]
- [[Orchestration]]
- [[Twelve-Factor App]]

## 🗺️ Part of
- [[MOC - DevOps]]
- [[MOC - Data Engineering]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- https://docs.docker.com
