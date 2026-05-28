# Task & Learning List

## 101 — Fundamentals

| Task | What You Learn |
|---|---|
| `notebooks/101/101_langchain_langgraph.ipynb` | Build your first agent: LLM models, tools (`@tool` decorator), memory, streaming, basic agent loop |
| `notebooks/101/102_middleware.ipynb` | Middleware patterns, guardrails, human-in-the-loop (HITL) with interrupts |

## 201 — Production Patterns

| Task | What You Learn |
|---|---|
| `notebooks/201/email_agent.ipynb` | Stateful email triage agent with structured routing (Pydantic schemas), tool-based response |
| `notebooks/201/multi_agent.ipynb` | Multi-agent systems: supervisor delegates to specialized sub-agents |
| `notebooks/201/research_agent.ipynb` | Deep research: parallel sub-researchers, supervisor subgraph, compression/synthesis pipeline |
| `notebooks/201/deep_agents.ipynb` | DeepAgents from scratch: AGENTS.md, skills, backends, long-term memory, HITL |
| `notebooks/201/deep_agents_extra.ipynb` | Additional DeepAgents patterns and exercises |

## Agent Implementations (`agents/`)

| Task | What You Learn |
|---|---|
| `agents/101/agent.py` | `create_agent()` with tools (weather, preferences, recommendations) |
| `agents/email_agent/graph.py` | StateGraph with conditional edges, triage router → response agent flow, `Commands` for goto/update |
| `agents/music_store/music_store_supervisor.py` | Multi-agent supervisor using `ToolRuntime` to share state with sub-agents |
| `agents/music_store/music_agent.py` | Music catalog sub-agent with database queries |
| `agents/music_store/invoice_agent.py` | Invoice sub-agent for purchase history |
| `agents/music_store/music_store_supervisor_with_interrupt.py` | HITL interrupt patterns in multi-agent systems |
| `agents/music_store/memory_enabled_music_store_supervisor_with_interrupt.py` | Long-term memory in multi-agent + interrupts combined |
| `agents/researcher/graph.py` | Advanced StateGraph: supervisor subgraph, parallel `asyncio.gather` research, structured output (Pydantic models), compression pipeline, retry logic, conditional termination |
| `agents/researcher/prompts.py` | Prompt engineering patterns for multi-stage research |
| `agents/researcher/models.py` | State schema design: input state, output state, intermediate state types |
| `agents/researcher/utils.py` | Shared tool setup, notes aggregation, web search detection, think tool |
| `agents/deep_agent/agent.py` | `create_deep_agent()` with CompositeBackend, skills directory, AGENTS.md memory, StoreBackend, filesystem, interrupt_on write/edit |
| `agents/deep_agent/AGENTS.md` | Agent identity and workflow instructions (replaces hardcoded system prompt) |
| `agents/deep_agent/skills/twitter-post/SKILL.md` | On-demand skill definition for Twitter/X posts |
| `agents/deep_agent/skills/linkedin-post/SKILL.md` | On-demand skill definition for LinkedIn posts |

## Infrastructure & Shared Code

| Task | What You Learn |
|---|---|
| `utils/models.py` | Centralized model initialization; multi-provider support (OpenAI, Anthropic, Azure, Bedrock, Vertex AI) |
| `utils/utils.py` | Graph visualization (`show_graph`), SQL database helpers |
| `langgraph.json` | Agent registry configuration for `langgraph dev` CLI |
| `mcp/email_tools.py` | MCP (Model Context Protocol) email tool integration |
| `pyproject.toml` | Dependency management with `uv` and pre-release packages |

## Key Concepts to Master

### LangChain
- `@tool` decorator, tool binding with `bind_tools`
- `create_agent()` with system prompts
- Chat model initialization and structured output (Pydantic `with_structured_output`)
- Messages (SystemMessage, HumanMessage, AIMessage, ToolMessage)
- `filter_messages`, `get_buffer_string`

### LangGraph
- `StateGraph` with `add_node`, `add_edge`, `add_conditional_edges`
- `MessagesState` and custom state schemas (TypedDict, Pydantic)
- Commands (`Command(goto=..., update=...)`)
- Interrupt / resume patterns for HITL
- Subgraph composition (supervisor → researcher subgraph)
- Conditional routing with `Literal` types
- `START` and `END` node markers

### DeepAgents
- `create_deep_agent()` harness
- `AGENTS.md` for agent identity
- Skills directory for on-demand capabilities
- `CompositeBackend` with route-based delegation (`FilesystemBackend` + `StoreBackend`)
- Long-term memory (`/memories/` → StoreBackend)
- `interrupt_on` for file write/edit safety
- Sub-agent delegation via `task()` tool

### Production Patterns
- Stateful multi-agent architectures
- Parallel execution with `asyncio.gather`
- Research → synthesis → report pipelines
- Compression techniques for long context
- Retry logic for structured output parsing
- Tool routing and error handling
