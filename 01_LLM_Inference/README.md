<div align="center">

# 🤖 LLM Inference
### *Artifact 01 — Agentic AI System*

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=for-the-badge&logo=openai&logoColor=white)](https://platform.openai.com/)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-22c55e?style=for-the-badge)]()

<br/>

> **A clean, reusable Python client for OpenAI chat-completions.**
> Abstracts raw API calls into typed, ergonomic methods — plain chat, prompt helpers, and structured JSON output — forming the **inference foundation** of the Agentic AI System.

</div>

---

## ✨ Highlights

| | Feature | Description |
|---|---|---|
| 💬 | **Chat Interface** | Pass role-keyed messages, get a clean string response |
| 🎯 | **Prompt Helper** | One-liner for system + user prompts |
| 🧱 | **Structured Output** | Auto-instructs the model to return JSON and parses it |
| ⚙️ | **Fully Configurable** | Model, temperature, max tokens — all tunable at init |
| 🔑 | **Env-Aware** | Auto-reads `OPENAI_API_KEY` from environment |

---

## 📁 Project Structure

```
01_LLM_Inference/
└── llm_inference.py     # Core LLMClient class
```

---

## 📁 Files

| File | Description |
|---|---|
| `llm_inference.py` | Core `LLMClient` class with `chat`, `send_prompt`, and `structured_chat` methods |

---

---

## 🚀 Quick Start

### 1 · Install

```bash
pip install openai
```

### 2 · Set your API key

```bash
# Option A — export in shell
export OPENAI_API_KEY="sk-..."

# Option B — add to .env at project root
echo 'OPENAI_API_KEY=sk-...' >> .env
```

### 3 · Run it

```python
from llm_inference import LLMClient

client = LLMClient(model="gpt-4o-mini", temperature=0.2, max_tokens=500)

# ── Plain prompt ────────────────────────────────────────
response = client.send_prompt(
    system_prompt="You are a helpful assistant.",
    user_prompt="Explain LLM inference in one sentence."
)
print(response)

# ── Structured JSON output ──────────────────────────────
data = client.structured_chat(
    system_prompt="Extract key entities from the text.",
    user_prompt="OpenAI was founded in San Francisco in 2015."
)
print(data)
# → {'entities': ['OpenAI', 'San Francisco', '2015']}
```

---

## 🔧 API Reference

### `LLMClient(model, temperature, max_tokens, api_key)`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `model` | `str` | `"gpt-4o-mini"` | OpenAI model identifier |
| `temperature` | `float` | `0.2` | Sampling temperature (0 = deterministic) |
| `max_tokens` | `int` | `500` | Maximum tokens in the response |
| `api_key` | `str` | `None` | API key (falls back to `OPENAI_API_KEY` env var) |




### Methods

<details>
<summary><b>💬 <code>chat(messages)</code></b> — Raw chat-completion call</summary>

```python
def chat(messages: List[Dict[str, str]]) -> str
```

Sends a raw messages list to the OpenAI chat-completions endpoint.

```python
response = client.chat([
    {"role": "system", "content": "You are concise."},
    {"role": "user",   "content": "What is 2 + 2?"}
])
```

</details>

<details>
<summary><b>🎯 <code>send_prompt(system_prompt, user_prompt)</code></b> — Convenience wrapper</summary>

```python
def send_prompt(system_prompt: str, user_prompt: str) -> str
```

Builds the system/user message structure and calls `chat()` — no boilerplate needed.

```python
reply = client.send_prompt("Be concise.", "What is Python?")
```

</details>

<details>
<summary><b>🧱 <code>structured_chat(system_prompt, user_prompt)</code></b> — JSON output</summary>

```python
def structured_chat(system_prompt: str, user_prompt: str) -> Dict[str, Any]
```

Appends a JSON instruction to the system prompt and auto-parses the response. Returns `{"error": ..., "raw_output": ...}` on parse failure.

```python
data = client.structured_chat(
    "Extract entities.",
    "Apple launched iPhone in 2007."
)
# → {"entities": ["Apple", "iPhone", "2007"]}
```

</details>

<details>
<summary><b>🔍 <code>parse_json(text)</code></b> — Safe JSON parser</summary>

```python
def parse_json(text: str) -> Dict[str, Any]
```

Internal helper. Safely parses any JSON string — returns an error dict instead of raising on failure.

</details>

---

## 📦 Dependencies

```txt
openai
```

Install all project dependencies from the root:

```bash
pip install -r requirements.txt
```

---

## 🗂️ Part of the Agentic AI System

This is **Artifact 01** in a progressive learning series that builds toward a full agentic pipeline.

```
Agentic-AI-System/
└── 01_LLM_Inference/    ◀ You are here
└── 02_Agent Core Loop/
└── 03_Tool System/
└── 04_Memory System/
└── 05_Planner/
└── ...
```

---

<div align="center">

Made with ❤️ · [Agentic AI System](../)

</div>
