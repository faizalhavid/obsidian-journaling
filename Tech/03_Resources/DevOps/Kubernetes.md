---
aliases: [Kubernetes, K8s]
tags: [concept, devops, data-engineering]
status: to-learn
area: DevOps
topic: Orchestration
source: 
created: 2026-08-21
reviewed: 
difficulty: advanced
---

# ☸️ Kubernetes

## 📖 Definisi
> Sistem [[Orchestration]] open-source untuk mengotomasi deployment, scaling, dan operasional [[Docker]] container di banyak host. Menjadi standar de facto container orchestration.

## 🔑 Poin Inti
- **Pod** — unit terkecil (biasanya 1 container).
- **Deployment** — pengelola replika Pod (self-healing, rolling update).
- **Service** — endpoint stabil ke Pod.
- **Ingress** — HTTP routing dari luar cluster.
- **ConfigMap / Secret** — konfigurasi & [[Secrets Management]].

## 💡 Manifest Minimal
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web
spec:
  replicas: 3
  selector: { matchLabels: { app: web } }
  template:
    metadata: { labels: { app: web } }
    spec:
      containers:
        - name: web
          image: ghcr.io/org/web:1.2.3
          ports: [{ containerPort: 8080 }]
```

## 🔗 Related Concepts
- [[Docker]]
- [[Orchestration]]
- [[Helm]]
- [[CI-CD]]
- [[Container Security]]
- [[Secrets Management]]

## 🗺️ Part of
- [[MOC - DevOps]]
- [[MOC - Data Engineering]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- https://kubernetes.io/docs
