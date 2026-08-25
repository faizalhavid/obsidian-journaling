---
aliases: [Container Security]
tags: [concept, cyber-security, devops]
status: to-learn
area: Cyber Security
topic: Operational Security
source: 
created: 2026-08-21
reviewed: 
difficulty: advanced
---

# 🐳🛡️ Container Security

## 📖 Definisi
> Praktik mengamankan seluruh **container supply chain** — dari base image, build, registry, runtime, hingga orchestrator ([[Kubernetes]]).

## 🔑 Poin Inti (Lapisan)
1. **Image**: pakai base minimal (distroless / alpine), pin versi, scan CVE (Trivy, Snyk).
2. **Build**: multi-stage, non-root user, no secret in layers.
3. **Registry**: signed image (cosign), private registry, image immutability.
4. **Runtime**: read-only FS, drop capabilities, seccomp / AppArmor.
5. **Orchestrator**: [[Kubernetes]] NetworkPolicy, PodSecurity, RBAC.
6. **Secrets**: pakai [[Secrets Management]] — jangan taruh di image.

## 🔗 Related Concepts
- [[Docker]]
- [[Kubernetes]]
- [[Secrets Management]]
- [[CI-CD]]
- [[Zero Trust]]

## 🗺️ Part of
- [[MOC - Cyber Security]]
- [[MOC - DevOps]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- NIST SP 800-190 — Application Container Security Guide
