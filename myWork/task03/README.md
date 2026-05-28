# Task 03 — Agent Implementations

## What to Study

- `agents/101/agent.py`
- `agents/email_agent/graph.py`
- `agents/music_store/music_store_supervisor.py`
- `agents/music_store/music_agent.py`
- `agents/music_store/invoice_agent.py`
- `agents/music_store/music_store_supervisor_with_interrupt.py`
- `agents/music_store/memory_enabled_music_store_supervisor_with_interrupt.py`
- `agents/researcher/graph.py`
- `agents/researcher/prompts.py`
- `agents/researcher/models.py`
- `agents/researcher/utils.py`
- `agents/deep_agent/agent.py`
- `agents/deep_agent/AGENTS.md`
- `agents/deep_agent/skills/twitter-post/SKILL.md`
- `agents/deep_agent/skills/linkedin-post/SKILL.md`

## Learning Objectives

- How `ToolRuntime` shares state between supervisor and sub-agents (music_store)
- How subgraph composition works — embedding one StateGraph inside another (researcher)
- How interrupt patterns work in multi-agent contexts (music_store variants)
- How long-term memory integrates with multi-agent systems
- How DeepAgents' `CompositeBackend` routes filesystem vs store operations
- How `AGENTS.md` defines agent identity and workflow — no hardcoded system prompt
- How skills provide on-demand capabilities (LinkedIn, Twitter)
- How the research agent structures prompts, models, and utilities for a complex pipeline
- How `interrupt_on` protects against unintended file writes/edits

## Action Items

- Read through all 15 files — they form a progression from simple to complex
- Compare `create_agent()` (101/email/music) vs `create_deep_agent()` (deep_agent)
- Trace the data flow in the researcher: clarify → write_brief → supervisor_subgraph → final_report
- Compare the three music_store variants: base, with_interrupt, memory_with_interrupt
- Experiment: write your own SKILL.md and add it to the deep_agent skills directory

## Mini Project — Multi-Agent Content Creation Pipeline

Build a pipeline that combines patterns from all agent implementations:

- **Research phase**: use the researcher pattern — supervisor delegates parallel research topics to sub-researchers (like `agents/researcher/`)
- **Draft phase**: use the deep_agent pattern — AGENTS.md instructs the agent to write drafts, skills provide format-specific output (blog post, Twitter thread, LinkedIn article)
- **Review phase**: use the email_agent triage pattern — route drafts for approval with HITL interrupts
- **Publication phase**: use the music_store supervisor pattern — orchestrate publishing sub-agents (social media poster, newsletter sender, blog publisher)
- **Memory**: persist content history and publication status using StoreBackend (like deep_agent)
