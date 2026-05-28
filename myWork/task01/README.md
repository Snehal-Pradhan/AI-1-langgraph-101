# Task 01 — LangChain & LangGraph Fundamentals

## What to Study

- `notebooks/101/101_langchain_langgraph.ipynb`
- `notebooks/101/102_middleware.ipynb`
- `agents/101/agent.py`

## Learning Objectives

- How `create_agent()` wires up a model, tools, and system prompt
- How tools are defined with `@tool` and bound to the agent with `bind_tools`
- How memory and streaming work in LangChain
- How middleware and guardrails add safety layers
- How human-in-the-loop interrupts pause and resume execution
- Messages types: SystemMessage, HumanMessage, AIMessage, ToolMessage

## Action Items

- Read through `101_langchain_langgraph.ipynb` and understand each cell
- Read through `102_middleware.ipynb` to learn middleware + HITL patterns
- Compare the notebook code with `agents/101/agent.py` — notice the same pattern in a standalone file
- Trace how a user query flows: input → agent → tool call → tool result → agent response
- Experiment: add a new tool (e.g. a unit converter or calculator) and re-run

## Mini Project — Personal Assistant Agent

Build a personal assistant agent that bundles the 101 concepts:

- **Tools to create**: get_weather, add_note / get_notes (in-memory), get_time, calculator
- **Middleware**: add a guardrail that rejects off-topic queries (e.g. "hack a website")
- **HITL**: add an interrupt before sending an email or deleting a note — ask the user to confirm
- **Streaming**: stream the agent's responses token-by-token

This wires up everything from the 101 track: tools, guardrails, interrupts, and streaming.
