---
aliases: []
tags:
  - ai-engineering
  - ai
  - claude
status: draft
area: AI Engineering
topic: Claude API
source: https://training.skilljar.com/anthropic
created: 2026-08-26
last_updated: 2026-08-26
---

# 🧪 Playground — Anthropic Skilljar

## 📑 Daftar Isi

- [Id Request](#id-request)
- [Response](#response)
- [Status Penyelesaian](#status-penyelesaian)
- [Token Usage](#token-usage)
- [Temperature 0.0 vs 1.0 (n=15 sampel)](#temperature-00-vs-10-n15-sampel)
  - [Setup Eksperimen](#setup-eksperimen)
  - [Data Hasil](#data-hasil)
  - [Temuan Utama](#temuan-utama)
  - [Kesimpulan Akhir](#kesimpulan-akhir)
- [🗺️ Part of](#️-part-of)

dari hasil run 
```python
message = client.messages.create(
    model=model,
    max_tokens=1000,
    messages=[
        {
            "role": "user",
            "content": "What is quantum computing? Answer in one sentence."

        }
    ]
)
print(message.content)
```

```json
{
  "id": "msg_bdrk_01L17Gn7Lp2P8SyJb8GGgDbs",
  "container": null,
  "content": [
    {
      "citations": null,
      "text": "Quantum computing is a type of computation that uses quantum mechanical phenomena like superposition and entanglement to perform calculations that would be impractical or impossible for classical computers.",
      "type": "text"
    }
  ],
  "model": "claude-sonnet-4-5",
  "role": "assistant",
  "stop_details": null,
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "type": "message",
  "usage": {
    "cache_creation": {
      "ephemeral_1h_input_tokens": 0,
      "ephemeral_5m_input_tokens": 0
    },
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0,
    "inference_geo": null,
    "input_tokens": 17,
    "output_tokens": 38,
    "output_tokens_details": null,
    "server_tool_use": null,
    "service_tier": null
  }
}
```

## Id Request
- **Message ID:** `msg_bdrk_01L17Gn7Lp2P8SyJb8GGgDbs`
- **Platform:** Amazon Bedrock (prefix `bdrk`)
- **Model:** `claude-sonnet-4-5`
- **Role:** assistant

## Response
- **Tipe konten:** 1 blok teks (`TextBlock`)
- **Jawaban:** Definisi quantum computing (superposition & entanglement)
- **Citations:** Tidak ada

## Status Penyelesaian
- **Stop reason:** `end_turn` → jawaban selesai natural, **tidak terpotong**
- **Stop sequence:** Tidak dipakai

## Token Usage
| Metrik | Nilai |
|---|---|
| Input tokens | 17 |
| Output tokens | 38 |
| Cache creation | 0 |
| Cache read | 0 |


# Temperature 0.0 vs 1.0 (n=15 sampel)

## Setup Eksperimen
- **Prompt:** "Give me a one-sentence movie plot idea." (dikirim ulang, messages tidak berubah)
- **Model:** claude-sonnet-4-5
- **Sampel:** 15x request per temperature

## Data Hasil

| Metrik | Temp 0.0 | Temp 1.0 |
|---|---|---|
| Total sampel | 15 | 15 |
| String identik persis (exact duplicate) | 0 pasang | 2 pasang (4 item) |
| Unique string | 15/15 | 13/15 |
| Distinct idea/tema | 7 | 9 |

## Temuan Utama

1. **Temperature tidak menjamin keunikan string** — Temp 1.0 justru menghasilkan 2 pasang kalimat yang identik kata-per-kata, sesuatu yang tidak terjadi sama sekali di Temp 0.0. Ini membuktikan temperature hanya mengubah *peluang* variasi, bukan *jaminan* variasi.

2. **Temperature memengaruhi keragaman tema, bukan mencegah pengulangan sepenuhnya** — Temp 1.0 menghasilkan lebih banyak ide unik (9 vs 7), tapi kedua temperature tetap didominasi tema yang sama: "time traveler mengancam eksistensi diri sendiri" — menunjukkan tema ini punya bobot probabilitas sangat dominan di data training untuk prompt jenis ini.

3. **Temp 0.0 cenderung mengulang ide, tapi dengan permukaan kalimat yang di-paraphrase** (kata berbeda, makna sama) — bukan berarti "selalu sama persis". Non-determinisme di level infrastruktur (floating-point GPU, load balancing) tetap memungkinkan variasi kecil meski secara teori argmax deterministik.

4. **Sample size n=15 belum cukup untuk generalisasi kuat** — pola yang terlihat bisa jadi spesifik untuk prompt ini (yang punya 1 tema super dominan), bukan berlaku umum untuk semua jenis prompt.

## Kesimpulan Akhir

> Temperature tinggi **meningkatkan keragaman tema**, tapi **tidak menjamin tidak ada duplikat** — bahkan bisa menghasilkan pengulangan persis karena sampling tetap berbasis probabilitas berbobot, bukan mekanisme "paksa beda". Klaim "temp 0 = sama, temp 1 = beda" terlalu simplistik; yang lebih akurat: **kedua temperature sama-sama tertarik ke attractor tema dominan**, dan temperature hanya mengatur seberapa sering model berhasil "kabur" darinya.

## 🗺️ Part of
[[Anthropic - Skilljar]] · [[MOC - Playground]] · [[MOC - AI Engineering]] · [[MOC - HOME]]
