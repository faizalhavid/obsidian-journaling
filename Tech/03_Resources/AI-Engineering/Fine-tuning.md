---
aliases: [Fine-tuning, Model Fine-tuning]
tags: [concept, ai-engineering]
status: to-learn
area: AI Engineering
topic: Core Practice
source: 
created: 2026-08-22
reviewed: 
difficulty: advanced
---

# 🎯 Fine-tuning

## 📖 Definisi
> **Fine-tuning** adalah proses melanjutkan pelatihan model pretrained pada dataset spesifik (task/domain) sehingga bobot model beradaptasi untuk kasus penggunaan tertentu.

## 🔑 Poin Inti
- **Full fine-tuning**: memperbarui seluruh bobot — mahal & butuh compute besar.
- **PEFT (Parameter-Efficient)**: LoRA / QLoRA / Adapter — hanya latih sebagian kecil parameter.
- **Instruction tuning**: melatih model mengikuti format instruksi.
- **RLHF / DPO**: menyelaraskan output dengan preferensi manusia.

## 🆚 Kapan Fine-tuning vs RAG vs Prompt?
- **Prompt Engineering** → cukup instruksi, tanpa data privat.
- **RAG** → butuh knowledge terkini / privat, tidak perlu ubah gaya.
- **Fine-tuning** → butuh gaya/format konsisten, domain khusus, atau task terstruktur.

## 🔗 Related Concepts
- [[Large Language Model]]
- [[Prompt Engineering]]
- [[RAG]]
- [[Embeddings]]

## 🗺️ Part of
- [[MOC - AI Engineering]]
- [[MOC - HOME]]

## 📝 Sumber & Referensi
- 
