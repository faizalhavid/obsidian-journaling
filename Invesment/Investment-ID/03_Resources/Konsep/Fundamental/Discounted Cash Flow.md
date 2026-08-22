---
aliases: [DCF]
tags: [concept, fundamental, valuation]
status: draft
kategori: Fundamental
created: 2026-08-21
last_updated: 2026-08-21
---

# Discounted Cash Flow (DCF)

> Menilai intrinsic value perusahaan berdasarkan present value dari future cash flows.

---

## 🧭 Definisi

DCF mendiskonto proyeksi Free Cash Flow (FCF) ke present value menggunakan discount rate (biasanya WACC).

```
Enterprise Value = Σ [FCFt / (1 + WACC)^t] + Terminal Value / (1 + WACC)^n
Equity Value = Enterprise Value - Net Debt
Fair Price per Share = Equity Value / Shares Outstanding
```

---

## 🔢 Komponen Utama

1. **FCF Projection (5-10 tahun)**
   - FCF = Operating CF - Capex
2. **Growth rate** per tahun proyeksi
3. **Terminal Value** — nilai perusahaan setelah tahun terakhir proyeksi
   - Gordon Growth: TV = FCF × (1 + g) / (WACC - g)
4. **Discount rate (WACC)** — cost of capital tertimbang

---

## 🧠 Kenapa Penting?

- Menghitung intrinsic value berdasarkan fundamental, bukan sentiment
- Membantu menentukan margin of safety
- Standard method di corporate finance & investment banking

---

## ⚠️ Pitfall Utama

1. **Garbage In, Garbage Out** — asumsi FCF terlalu optimis = valuasi tidak realistis
2. **Sensitivity ke Terminal Value** — TV bisa 60-80% dari total valuasi. Kecil beda di WACC atau growth = besar beda di TV.
3. **Sulit untuk perusahaan tanpa FCF stabil** (early-stage fintech, cyclical dalam)
4. **Discount rate arbitrary** — pilih WACC realistis (untuk emiten ID biasanya 10-15%)

---

## 📊 Rule of Thumb Sensitivity

Selalu buat 3 scenario:
- **Bear:** growth rendah, margin turun, WACC tinggi
- **Base:** asumsi realistis
- **Bull:** growth optimis, margin stabil

Kalau **bear case** masih > current price = margin of safety kuat.

---

## 💼 Aplikasi

- Untuk emiten cash flow stable (consumer staples, utility)
- Kurang cocok untuk early fintech / startup

## 🔗 Related

- [[P-E Ratio & PEG Ratio]]
- [[Dividend Discount Model]]
- [[MOC - Valuasi & Pricing]]

## 📚 Source

- Aswath Damodaran — DCF Model
- McKinsey — "Valuation" (Copeland & Koller)
