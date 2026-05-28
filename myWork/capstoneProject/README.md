# Capstone Project — Personal Research & Content OS

A single agent system that ties together concepts from all 4 tasks. The agent takes a research topic, gathers information in parallel, generates content in multiple formats, gets human approval, delivers it, and remembers everything for next time.

## Workflow

```
User Topic → Clarify (HITL) → Research (parallel) → Draft (skills) → Review (HITL) → Deliver (email/MCP) → Remember (memory)
```

## Concepts Used

| Task | Concepts Applied |
|---|---|
| **Task 01** | `@tool` for custom tools, `create_agent()`, streaming responses |
| **Task 02** | StateGraph with conditional routing, supervisor + sub-agents |
| **Task 03** | `create_deep_agent()`, AGENTS.md, skills, CompositeBackend, research subgraph, `interrupt_on` |
| **Task 04** | langgraph.json registration, multi-provider model config, MCP tool integration |

## Project Structure

```
myWork/capstoneProject/
├── agents/
│   └── research_os/
│       ├── agent.py              # create_deep_agent() entry point
│       ├── AGENTS.md             # Agent identity & workflow instructions
│       ├── skills/
│       │   ├── newsletter/SKILL.md
│       │   ├── twitter-thread/SKILL.md
│       │   └── blog-post/SKILL.md
│       └── memories/             # Long-term memory (StoreBackend)
├── utils/
│   ├── models.py                 # Centralized multi-provider model config
│   └── tools.py                  # Custom tools (web search, storage, analytics)
├── mcp/
│   └── email_mcp.py              # MCP email delivery tool
├── langgraph.json                # Agent registration for langgraph dev
├── pyproject.toml                # Dependencies
└── .env.example                  # API key template
```

## Implementation Steps

### Phase 1 — Scaffold
1. Create `pyproject.toml` with langchain, langgraph, deepagents, tavily dependencies
2. Create `langgraph.json` registering the agent
3. Create `.env.example` with API key placeholders

### Phase 2 — Infrastructure
4. Create `utils/models.py` with centralized multi-provider model init (OpenAI, Anthropic, Azure, Bedrock, Vertex)
5. Create `utils/tools.py` with custom tools: tavily_search, store_content, get_content_history, content_analytics
6. Create `mcp/email_mcp.py` with an MCP tool for sending email via SMTP

### Phase 3 — Agent Identity & Skills
7. Write `AGENTS.md` defining the agent's identity and workflow:
   - Plan → Research → Draft → Review → Deliver → Remember
8. Write 3 skill files:
   - `skills/newsletter/SKILL.md` — format research as a newsletter with sections and links
   - `skills/twitter-thread/SKILL.md` — format as a threaded Twitter/X post
   - `skills/blog-post/SKILL.md` — format as a full blog post with headings

### Phase 4 — Agent Core
9. Write `agent.py` using `create_deep_agent()`:
   - Bind model from utils/models.py
   - Register tools from utils/tools.py
   - Load identity from `AGENTS.md`
   - Load skills from `./skills/`
   - Add a research sub-agent for delegated parallel work
   - Configure `CompositeBackend` (FilesystemBackend + StoreBackend for memories)
   - Set `interrupt_on` for write_file and edit_file to get HITL approval on drafts

### Phase 5 — Run
10. Start with `langgraph dev` and test in LangGraph Studio

## Stretch Goals

- **Quality guardrails**: add a middleware layer that scores content quality and rejects drafts below a threshold, asking the agent to revise
- **Parallel research**: embed a supervisor subgraph (like `agents/researcher/graph.py`) to run multiple research queries concurrently with `asyncio.gather`
- **Feedback loop**: after delivery, prompt the user for feedback and store it in `/memories/feedback/`. On next run for a similar topic, incorporate past feedback
- **Scheduled delivery**: add a `schedule_content` tool that queues content for delivery at a future time using a background scheduler
- **Multi-channel delivery**: beyond email, add MCP tools for Slack, Discord, or Notion — let the agent choose the channel based on content type
- **Content versioning**: store every draft version in `/memories/versions/` so the user can roll back or compare revisions
