# Task 04 — Infrastructure & Setup

## What to Study

- `utils/models.py`
- `utils/utils.py`
- `langgraph.json`
- `mcp/email_tools.py`
- `pyproject.toml`

## Learning Objectives

- How centralized model configuration works — switch between OpenAI, Anthropic, Azure, Bedrock, Vertex AI by editing one file
- How `init_chat_model()` with provider prefix (`"anthropic:claude-haiku-4-5"`) simplifies multi-provider setup
- How environment variables and `.env` files manage API keys securely
- How `langgraph.json` registers agents for `langgraph dev` — maps agent names to file paths
- How MCP (Model Context Protocol) tools integrate with LangGraph agents
- How `pyproject.toml` manages dependencies with `uv` and pre-release packages
- How `utils/utils.py` provides `show_graph()` for visualizing StateGraph structures and database helpers

## Action Items

- Read `utils/models.py` and understand the provider switch pattern
- Open `langgraph.json` and map each entry to the actual agent file it references
- Run `langgraph dev` and explore the LangGraph Studio UI
- Examine `mcp/email_tools.py` to see how MCP tools are defined
- Review `pyproject.toml` and note the key dependencies (langchain, langgraph, deepagents)
- Experiment: switch the model provider in `utils/models.py` (e.g. to OpenAI) and verify the agents still work

## Mini Project — Scaffold Your Own LangGraph Project

Create a new LangGraph project from scratch to prove you understand the infra:

- **pyproject.toml**: define dependencies using the same pattern (langchain, langgraph, deepagents)
- **utils/models.py**: copy the centralized model config with multiple provider options
- **langgraph.json**: register at least 2 agents for Studio
- **mcp/my_tool.py**: create a custom MCP tool (e.g. a file search tool, a database query tool)
- **utils/utils.py**: add a `show_graph()` wrapper and any shared helpers
- **Agent**: write a simple agent that uses your MCP tool and runs via `langgraph dev`
