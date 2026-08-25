---
aliases:
  - Anthropic Skilljar Mod 3
  - Building with Claude API
tags: [course, ai-engineering]
status: in-progress
area: AI Engineering
course: Anthropic Skilljar
module: 3 - Building with the Claude API
source: Anthropic Docs
instructor: 
created: 2026-08-25
last_updated: 2026-08-25
progress: 40%
---

# 📘 Module 3 - Building with the Claude API

## 📖 Ringkasan
> Modul ini membahas seluruh siklus request ke Claude API: dari arsitektur server yang aman, manajemen conversation history, system prompts, temperature, response streaming, hingga teknik mendapat structured output bersih.

## 🔑 Poin Inti
- **Request lifecycle (5 tahap)** — client → server → Anthropic API → model processing → response balik ke client. API key hanya boleh ada di server, tidak pernah di client-side.
- **`client.messages.create()`** — tiga field wajib: `model`, `max_tokens` (safety cap, bukan target), `messages` (list dict dengan `role` + `content`).
- **Claude stateless** — tidak menyimpan riwayat percakapan. Setiap request harus menyertakan full conversation history secara manual.
- **System prompt** — string yang dipass via `system=` untuk mengatur tone, role, dan batasan respons Claude.
- **Temperature (0.0–1.0)** — rendah = deterministik/faktual, tinggi = kreatif/variatif. Default `1.0`.
- **Streaming** — `client.messages.stream()` mengirim teks chunk-per-chunk sehingga user melihat respons muncul secara real-time.
- **Structured output** — kombinasi assistant message prefilling + `stop_sequences` untuk mengekstrak JSON/kode bersih tanpa prose tambahan.
- **Token lifecycle** — input diproses lewat tokenization → embedding → contextualization → generation (probabilistik, bukan deterministik penuh).

## 📝 Catatan Detail

### B. Accessing the API — Request Lifecycle

Lima tahap setiap request:
1. Client app → server (via HTTPS)
2. Server → Anthropic API (dengan API key tersimpan aman di server)
3. Anthropic API → Claude model
4. Model output → Anthropic API response
5. Server → client app

**Kenapa harus lewat server:** API key adalah secret. Kalau diekspos di client (browser/mobile), siapapun bisa mengekstraknya dan membuat request tidak sah.

**Proses dalam model:**
- **Tokenization** — input dipecah jadi token (kata/sub-kata/simbol)
- **Embedding** — tiap token dikonversi ke vektor numerik yang merepresentasikan semua kemungkinan makna
- **Contextualization** — embedding diperhalus berdasarkan konteks kalimat sekitarnya
- **Generation** — output layer menghitung probabilitas setiap token berikutnya; Claude memilih berdasarkan probabilitas + randomness terkontrol

**Claude berhenti generate saat:** max tokens tercapai, natural end-of-sequence token muncul, atau stop sequence ditemukan.

**API Response berisi:** `message` (generated text), `usage` (input/output token count), `stop_reason`.

---

### C. Making Request — Setup & Create Function

```python
%pip install anthropic python-dotenv
```

Simpan API key di `.env` (jangan commit ke git):
```
ANTHROPIC_API_KEY="sk-ant-..."
```

Buat client:
```python
from dotenv import load_dotenv
from anthropic import Anthropic

load_dotenv()
client = Anthropic()
model = "claude-sonnet-4-0"
```

`max_tokens` adalah **safety cap** — Claude berhenti jika mencapai limit ini, bukan target untuk diisi penuh.

Akses teks respons: `message.content[0].text`

---

### D. Multi-Turn Conversations — State Management

Claude tidak punya memory antar-request. Untuk percakapan multi-turn, developer harus:
1. Maintain list `messages` secara lokal
2. Append setiap pesan user DAN respons Claude ke list
3. Kirim list lengkap di setiap request berikutnya

Helper functions standar:
```python
def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})
```

---

### E. System Prompts

System prompt dipass via parameter `system=` (terpisah dari `messages`). Claude mencoba merespons sesuai role/instruksi yang diberikan.

**Penting:** API Claude tidak menerima `system=None`. Gunakan conditional:
```python
if system:
    params["system"] = system
```

---

### F. Temperature

| Range | Karakter | Use Case |
|---|---|---|
| 0.0 – 0.3 | Deterministik | Factual Q&A, coding, data extraction, moderation |
| 0.4 – 0.7 | Seimbang | Summarization, education, problem-solving |
| 0.8 – 1.0 | Kreatif | Brainstorming, creative writing, marketing |

Temperature tidak menjamin output berbeda setiap saat — hanya mengubah distribusi probabilitas.

---

### G. Response Streaming

Stream events yang dikirim Claude:
- `MessageStart` → `ContentBlockStart` → `ContentBlockDelta` (teks aktual) → `ContentBlockStop` → `MessageDelta` → `MessageStop`

Simplified approach (hanya teks):
```python
with client.messages.stream(model=model, max_tokens=1000, messages=messages) as stream:
    for text in stream.text_stream:
        print(text, end="")
    final_message = stream.get_final_message()  # untuk disimpan ke DB
```

---

### H. Structured Data — Prefilling + Stop Sequences

Masalah: Claude default menambah prose/markdown wrapper di sekitar JSON.

Solusi: prefill assistant message + stop sequence:
```python
add_assistant_message(messages, "```json")
text = chat(messages, stop_sequences=["```"])
clean = json.loads(text.strip())
```

Cara kerjanya: Claude "berpikir" sudah mulai code block, lanjut isi JSON saja, lalu berhenti saat mau menutup ` ``` `. Berlaku juga untuk Python, CSV, bulleted list, dll.

## 💡 Contoh / Ilustrasi

Fungsi `chat` lengkap dengan semua fitur (system + temperature):

```python
from dotenv import load_dotenv
from anthropic import Anthropic
import json

load_dotenv()
client = Anthropic()
model = "claude-sonnet-4-0"

def add_user_message(messages, text):
    messages.append({"role": "user", "content": text})

def add_assistant_message(messages, text):
    messages.append({"role": "assistant", "content": text})

def chat(messages, system=None, temperature=1.0, stop_sequences=None):
    params = {
        "model": model,
        "max_tokens": 1000,
        "messages": messages,
        "temperature": temperature,
    }
    if system:
        params["system"] = system
    if stop_sequences:
        params["stop_sequences"] = stop_sequences
    message = client.messages.create(**params)
    return message.content[0].text

# Contoh: structured JSON output
messages = []
add_user_message(messages, "Generate a short EventBridge rule as JSON")
add_assistant_message(messages, "```json")
raw = chat(messages, stop_sequences=["```"])
result = json.loads(raw.strip())
```

## ❓ Pertanyaan
- Kenapa API key tidak boleh diletakkan langsung di frontend/client code?
- Apa yang terjadi kalau `max_tokens` tercapai sebelum Claude selesai menjawab?
- Apa bedanya `client.messages.create(stream=True)` vs `client.messages.stream()`?
- Bagaimana cara mempertahankan context percakapan padahal Claude stateless?
- Kapan sebaiknya menggunakan temperature rendah vs tinggi?

## ✅ Review Checklist
- [ ] Bisa membuat basic request ke Anthropic API dengan `client.messages.create()`.
- [ ] Bisa implement multi-turn conversation dengan menyimpan dan mengirim full message history.
- [ ] Bisa menulis system prompt yang mengubah behavior Claude secara konsisten.
- [ ] Bisa implement streaming dan mendapat `final_message` setelah stream selesai.
- [ ] Bisa mengekstrak clean JSON menggunakan assistant prefilling + stop sequences.
- [ ] Sudah mengisi [[Large Language Model]] dan [[Embeddings]] di 03_Resources/ dengan insight dari modul ini.

## ⏭️ Next
[[]] — Module 4 (Anthropic Skilljar).

## 🗺️ Part of
[[Anthropic Skilljar]] (Course Overview) · [[MOC - AI Engineering]] · [[MOC - HOME]]
