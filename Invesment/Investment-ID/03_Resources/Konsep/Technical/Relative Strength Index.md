---
aliases: [RSI]
tags: [concept, technical, oscillator]
status: draft
kategori: Technical
created: 2026-08-21
last_updated: 2026-08-21
---

# Relative Strength Index (RSI)

> Oscillator momentum yang mengukur kecepatan & magnitude pergerakan harga.

---

## 🧭 Definisi

RSI (14-period) dikembangkan J. Welles Wilder. Range: 0-100.

```
RSI = 100 - (100 / (1 + RS))
RS = Average Gain / Average Loss (dalam 14 periode)
```

---

## 📊 Interpretasi

| RSI | Signal |
|-----|--------|
| > 70 | Overbought (potensi koreksi) |
| 50-70 | Bullish momentum |
| 30-50 | Neutral / bearish |
| < 30 | Oversold (potensi rebound) |

Namun dalam **strong trend**, RSI bisa stuck di > 70 (uptrend) atau < 30 (downtrend) untuk waktu lama.

---

## 🔄 Divergence

**Bullish Divergence:** harga lower low, RSI higher low → sinyal reversal ke atas
**Bearish Divergence:** harga higher high, RSI lower high → sinyal reversal ke bawah

Divergence adalah salah satu sinyal paling powerful dari RSI.

---

## ⚠️ Pitfall

1. **Overbought ≠ langsung jual** — bisa tetap overbought lama
2. **False signal di sideways** — kombinasi dengan trend indicator
3. **Timeframe matters** — RSI daily beda dengan weekly

---

## 💼 Aplikasi

- [[COIN - Technical]]
- [[MBMA - Technical]]
- [[BUVA - Technical]]

## 🔗 Related

- [[MACD]]
- [[Stochastic Oscillator]]
- [[MOC - Technical Analysis]]
