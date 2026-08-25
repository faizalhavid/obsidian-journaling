---
aliases: [CI/CD, CI-CD, Continuous Integration, Continuous Deployment, Continuous Delivery]
tags: [concept, devops, software-engineering]
status: to-learn
area: DevOps
topic: Automation
source: 
created: 2026-08-21
reviewed: 
difficulty: intermediate
---

# 🔁 CI/CD

## 📖 Definisi
> **Continuous Integration** = merge kode secara sering ke branch utama dengan auto-build & test.
> **Continuous Delivery / Deployment** = otomasi release ke staging (delivery) atau production (deployment) setelah CI hijau.

## 🔑 Poin Inti
- **CI** butuh: [[Git]], [[Testing]] (unit + integration), pipeline (GitHub Actions / GitLab CI / Jenkins).
- **CD** butuh: artifact registry, environment config, [[Deployment Strategies]] (blue-green, canary, rolling).
- Tujuan: **feedback loop pendek** — bug ketahuan menit, bukan minggu.
- Ini adalah **kontrak** antar [[MOC - Software Engineering]] dan [[MOC - DevOps]].

## 💡 Pipeline Sederhana
```yaml
# .github/workflows/ci.yml
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - run: npm ci
      - run: npm test
      - run: npm run build
```

## 🔗 Related Concepts
- [[Git]]
- [[Testing]]
- [[Docker]]
- [[Kubernetes]]
- [[GitHub Actions]]
- [[Deployment Strategies]]

## 🗺️ Part of
- [[MOC - DevOps]]
- [[MOC - Software Engineering]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- 
