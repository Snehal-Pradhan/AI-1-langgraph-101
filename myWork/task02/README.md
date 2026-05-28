# Task 02 — Production Patterns

## What to Study

- `notebooks/201/email_agent.ipynb`
- `notebooks/201/multi_agent.ipynb`
- `notebooks/201/research_agent.ipynb`
- `notebooks/201/deep_agents.ipynb`
- `notebooks/201/deep_agents_extra.ipynb`

## Learning Objectives

- How `StateGraph` works: nodes, edges, conditional routing
- How to build a triage router using structured output (Pydantic schemas with `with_structured_output`)
- How multi-agent supervisors delegate to specialized sub-agents
- How parallel research works with `asyncio.gather` and subgraph composition
- How DeepAgents provides AGENTS.md, skills, backends, and long-term memory out of the box
- How HITL interrupts work in production agent workflows

## Action Items

- Read each notebook in order — they build on each other
- Trace the graph structure in `email_agent`: triage_router → response_agent or END
- Study the research agent's subgraph pattern: supervisor → researcher_tools → compress → END
- Read the DeepAgents notebook to understand how AGENTS.md replaces hardcoded system prompts
- Experiment: modify the triage router's classification criteria or add a new category

## Mini Project — Customer Support Ticket System

Build a multi-agent support system that combines the 201 patterns:

- **Triage router**: classifies incoming tickets as billing, technical, or general (like email_agent triage)
- **Specialized sub-agents**: one for billing (invoice lookup, refund), one for tech support (knowledge base search), one for general inquiries
- **Supervisor**: routes tickets to the right sub-agent and synthesizes the final response (like music_store)
- **Parallel escalation**: if a ticket is urgent, research it in parallel across all sub-agents (like research_agent)
- **Long-term memory**: remember resolved tickets for faster future responses (DeepAgents memory)
