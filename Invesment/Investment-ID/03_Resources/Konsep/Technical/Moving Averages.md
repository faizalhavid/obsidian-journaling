---
aliases: [MA, SMA, EMA]
tags: [concept, technical, indicator]
status: draft
kategori: Technical
created: 2026-08-21
last_updated: 2026-08-21
---

# Moving Averages (SMA & EMA)

> Meratakan pergerakan harga untuk melihat trend.

---

## 🧭 Definisi

- **SMA (Simple Moving Average):** rata-rata harga close X periode terakhir, bobot sama.
- **EMA (Exponential Moving Average):** rata-rata dengan bobot lebih besar ke data terbaru (lebih responsif).

Formula EMA:
```
EMA = (Close × Multiplier) + (Prev EMA × (1 - Multiplier))
Multiplier = 2 / (Period + 1)
```

---

## 🧠 Fungsi

1. **Trend identification** — Harga di atas MA = uptrend
2. **Dynamic support/resistance** — MA sering jadi level bounce
3. **Crossover signal** — Golden Cross / Death Cross

---

## 📊 Periode Populer

| MA | Fungsi |
|----|--------|
| SMA 20 | Short-term trend |
| SMA 50 | Medium-term trend |
| SMA 200 | Long-term trend (bull/bear market divider) |
| EMA 12, 26 | Dasar MACD |
| EMA 9 | Signal short-term momentum |

---

## 🔄 Crossover Signals

- **Golden Cross:** SMA 50 cross ke atas SMA 200 → bullish (long-term)
- **Death Cross:** SMA 50 cross ke bawah SMA 200 → bearish
- **Short-term:** EMA 12 cross EMA 26 → sinyal MACD

---

## ⚠️ Pitfall

1. **Lagging indicator** — sinyal terlambat
2. **Whipsaw** di market sideways — banyak false signal
3. **Period harus sesuai** dengan timeframe trading

---

## 💼 Aplikasi

- [[COIN - Technical]]
- [[MBMA - Technical]]
- [[BUVA - Technical]]

## 🔗 Related

- [[MACD]]
- [[Support & Resistance]]
- [[MOC - Technical Analysis]]
