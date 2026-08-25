---
aliases: [Secrets Management, Secret Management]
tags: [concept, cyber-security, devops]
status: to-learn
area: Cyber Security
topic: Operational Security
source: 
created: 2026-08-21
reviewed: 
difficulty: intermediate
---

# 🔑 Secrets Management

## 📖 Definisi
> Praktik menyimpan, mendistribusikan, dan merotasi **kredensial sensitif** (API keys, DB password, TLS cert, token) di luar source code — dengan audit trail dan akses terkontrol.

## 🔑 Poin Inti
- **Never commit secrets** to Git — pakai pre-commit scanner (gitleaks, trufflehog).
- Solusi umum:
  - **Vault** (HashiCorp Vault)
  - **Cloud KMS** (AWS Secrets Manager, GCP Secret Manager, Azure Key Vault)
  - **[[Kubernetes]] Secret** (base64-encoded → wajib gabung dengan sealed-secrets / external-secrets).
- **Rotasi otomatis** & **least privilege** wajib.
- Kompatibel dengan [[Twelve-Factor App]] (config in environment).

## 🔗 Related Concepts
- [[Container Security]]
- [[Docker]]
- [[Kubernetes]]
- [[CI-CD]]
- [[Authentication]]
- [[CIA Triad]]

## 🗺️ Part of
- [[MOC - Cyber Security]]
- [[MOC - DevOps]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- 
