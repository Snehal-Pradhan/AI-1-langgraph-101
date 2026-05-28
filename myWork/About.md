# LangGraph 101 — About This Repo

This is **LangGraph 101**, the official hands-on tutorial repository from [LangChain](https://langchain.com) for learning how to build LLM-powered agents.

## What It Teaches

The repo covers **three frameworks** that form a stack:

| Framework | Purpose |
|---|---|
| **LangChain** | LLM application building blocks (models, tools, prompts, memory) |
| **LangGraph** | Graph-based agent orchestration with cycles, state, and control flow |
| **DeepAgents** | High-level agent harness with built-in filesystem, skills, sub-agents, and long-term memory |

## Learning Tracks

### 101 — Fundamentals (`notebooks/101/`)
- Build your first agent with tools, memory, and streaming
- Middleware, guardrails, and human-in-the-loop (HITL) patterns

### 201 — Production Patterns (`notebooks/201/`)
- Stateful email triage agent
- Multi-agent supervisor + sub-agent systems (music store)
- Deep research agent with parallel sub-researchers
- DeepAgents: AGENTS.md, skills, backends, memory, HITL

## Agents (`agents/`)

Standalone agent implementations deployable in LangGraph Studio:

- `agents/101/` — Simple weather + recommendation agent
- `agents/email_agent/` — Email triage + response agent
- `agents/music_store/` — Multi-agent system (supervisor + catalog + invoice sub-agents) with memory and interrupt variants
- `agents/researcher/` — Deep research agent with supervisor subgraph and parallel researchers
- `agents/deep_agent/` — Full DeepAgents example with AGENTS.md identity, skills (LinkedIn, Twitter), long-term memory, and HITL

## Shared Infrastructure

- `utils/models.py` — Centralized LLM config (default: Anthropic Claude; supports OpenAI, Azure, Bedrock, Vertex)
- `utils/utils.py` — Shared utilities (graph visualization, DB helpers)
- `langgraph.json` — Agent registry for `langgraph dev` (local API + Studio UI)

## Tech Stack

- Python 3.11+, LangChain ≥1.0, LangGraph ≥1.0, DeepAgents ≥0.5.3
- Jupyter notebooks for interactive learning
- LangGraph Studio for visual agent debugging
- MCP (Model Context Protocol) for tool integration
- Tavily for web search, Open-Meteo for weather
- Support for OpenAI, Anthropic, Azure, Bedrock, Vertex AI models
