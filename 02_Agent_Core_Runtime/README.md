<div align="center">

# 🤖 Agent Core Runtime
### *Artifact 02 — Agentic AI System*

[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--4o--mini-412991?style=for-the-badge&logo=openai&logoColor=white)](https://platform.openai.com/)
[![License](https://img.shields.io/badge/License-MIT-22c55e?style=for-the-badge)](LICENSE)
[![Status](https://img.shields.io/badge/Status-Active-22c55e?style=for-the-badge)]()

<br/>

> **A minimal autonomous agent loop powered by an LLM.**
> The agent repeatedly **Observes** its state, **Thinks** by querying GPT, **Acts** on the response, and **Updates** its history — forming the core engine of every agentic AI system.

</div>

---

## ✨ Highlights

| | Feature | Description |
|---|---|---|
| 🔭 | **Observe** | Gathers current goal + action history |
| 🧠 | **Think** | Queries the LLM for a structured decision (JSON) |
| ⚡ | **Act** | Dispatches the chosen action (`search` / `finish`) |
| 📝 | **Update State** | Logs thought, action & result into memory |
| 🔁 | **Iteration Cap** | Stops after `max_iterations` to prevent infinite loops |

---

## 🧠 Core Concept — The Agent Loop

Every iteration of the agent follows a strict **four-phase cycle**:

```
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│   ┌──────────┐    ┌──────────┐    ┌──────────┐    ┌─────────────┐   │
│   │  OBSERVE │ →  │  THINK   │ →  │   ACT    │ →  │UPDATE STATE │   │
│   │          │    │  (LLM)   │    │          │    │             │   │
│   │ Gather   │    │ Reason & │    │ Execute  │    │ Log thought,│   │
│   │ goal +   │    │ choose   │    │ the      │    │ action &    │   │
│   │ history  │    │ action   │    │ action   │    │ result      │   │
│   └──────────┘    └──────────┘    └──────────┘    └─────────────┘   │
│                                                         │           │
│   ◀─────────────────── Repeat until done ───────────────┘           │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

The LLM is not just generating text — it is **deciding what to do next**, returning structured JSON with a `thought`, an `action`, and an `input`.

---

## 📁 File Structure

```
02_Agent_Core_Runtime/
├── agent_runtime.py      ← 🤖  Core Agent class — the autonomous loop
├── llm_inference.py      ← 🔌  LLM client (reused from 01_LLM_Inference)
└── README.md             ← 📖  You are here
```

---

## 🔍 Deep Dive — File Breakdown

### 🤖 `agent_runtime.py` — The Agent Brain

This is where all the magic happens. The `Agent` class encapsulates the full autonomous loop.

```python
class Agent:
    def __init__(self, goal: str, max_iterations: int = 5):
        self.goal = goal
        self.max_iterations = max_iterations
        self.llm = LLMClient()
        self.state = {
            "goal": goal,
            "history": [],
            "iteration": 0,
            "done": False
        }
```

| Method | Phase | Role |
|---|---|---|
| `observe()` | 🔭 Observe | Packages goal + history into an observation dict |
| `think(observation)` | 🧠 Think | Sends observation to the LLM, gets structured JSON back |
| `act(reasoning)` | ⚡ Act | Dispatches the chosen action (`search` or `finish`) |
| `update_state(reasoning, result)` | 📝 Update | Appends the step record to the agent's history |
| `run()` | 🔁 Loop | Orchestrates the full Observe→Think→Act→Update cycle |

#### The LLM Prompt Strategy

The agent instructs the LLM with a strict **system prompt** that:
- Defines its autonomous agent role
- Enforces **structured JSON output** — no free-form text allowed
- Lists the available actions explicitly

```json
{
  "thought": "I should search for creative ideas related to the goal",
  "action": "search",
  "input": "Agentic AI project ideas"
}
```

This is what separates an _agent_ from a _chatbot_ — the LLM is producing **machine-parseable decisions**, not human-readable prose.

---

### 🔌 `llm_inference.py` — The LLM Interface Layer

A lightweight OpenAI client that exposes three clean methods:

| Method | What it does |
|---|---|
| `chat(messages)` | Raw message-list-based chat |
| `send_prompt(system, user)` | Simple system + user prompt shorthand |
| `structured_chat(system, user)` | Returns **parsed JSON** — used by the agent |

The `structured_chat` method is the key integration point — it automatically appends a JSON instruction to the system prompt and parses the response, making it the perfect bridge between the LLM and the agent loop.

---

## 🚀 Quick Start

### 1 · Install dependencies

```bash
pip install -r requirements.txt
```

### 2 · Set your API key

```env
# .env at project root
OPENAI_API_KEY=sk-...
```

### 3 · Run the agent

```bash
cd 02_Agent_Core_Runtime
python agent_runtime.py
```

### Example Output

```
Agent started
Goal: Find ideas for Agentic AI projects

-----------------------------
Iteration 0
-----------------------------
Thought: I should search for creative Agentic AI ideas.
Action: search
Input: Agentic AI project ideas
Result: Simulated search results for 'Agentic AI project ideas'

-----------------------------
Iteration 1
-----------------------------
Thought: I have enough information to respond.
Action: finish
Input: Here are the top ideas...
Result: Goal completed.

Agent finished.
```

---

## 🔧 API Reference

### `Agent(goal, max_iterations)`

| Parameter | Type | Default | Description |
|---|---|---|---|
| `goal` | `str` | — | The objective the agent works toward |
| `max_iterations` | `int` | `5` | Maximum reasoning steps before stopping |

### Methods

<details>
<summary><b>🔭 <code>observe()</code></b> — Gather current context</summary>

```python
def observe() -> Dict[str, Any]
```

Packages the current `goal` and `history` into an observation dict that gets sent to the LLM.

</details>

<details>
<summary><b>🧠 <code>think(observation)</code></b> — Query the LLM for a decision</summary>

```python
def think(observation: Dict[str, Any]) -> Dict[str, Any]
```

Sends the observation to the LLM and returns a structured JSON decision:

```json
{
  "thought": "I should search for relevant information.",
  "action": "search",
  "input": "Agentic AI project ideas"
}
```

</details>

<details>
<summary><b>⚡ <code>act(reasoning)</code></b> — Execute the chosen action</summary>

```python
def act(reasoning: Dict[str, Any]) -> str
```

Dispatches the action from the LLM's decision. Supported actions:

| Action | Behaviour |
|---|---|
| `search` | Returns simulated search results |
| `finish` | Marks the goal as complete and stops the loop |

</details>

<details>
<summary><b>📝 <code>update_state(reasoning, result)</code></b> — Log the step</summary>

```python
def update_state(reasoning: Dict[str, Any], result: str)
```

Appends a full step record (thought, action, input, result) to `state["history"]` so the LLM has context on the next iteration.

</details>

<details>
<summary><b>🔁 <code>run()</code></b> — Start the agent loop</summary>

```python
def run() -> Dict[str, Any]
```

Orchestrates the full **Observe → Think → Act → Update** cycle until `action == "finish"` or `max_iterations` is reached. Returns the final state dict.

</details>

---

## 📦 Dependencies

```txt
openai
python-dotenv
```

```bash
pip install -r requirements.txt
```

---

## 🗂️ Part of the Agentic AI System

This is **Artifact 02** in a progressive series that builds toward a full agentic pipeline.

```
Agentic-AI-System/
└── 01_LLM_Inference/         ✅ Done
└── 02_Agent_Core_Runtime/    ◀ You are here
└── 03_Tool_System/
└── 04_Memory_System/
└── 05_Planner/
```

---

<div align="center">

Made with ❤️ · [Agentic AI System](../)

</div>
