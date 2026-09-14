# BLACKBOX AI (`blackbox-ai`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: BLACKBOXAI
- License: Proprietary
- Language: unknown
- Interface: platforms=IDE; install=Install from the VS Code Marketplace
- Model providers: Blackbox-hosted models plus Claude, GPT, Gemini, Grok endpoints via its router
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): AI coding assistant with real-time code completion, documentation, and debugging suggestions

(captured site page body (agents/blackbox-ai.md), not a verified repo-code finding)
Blackbox AI operates an enterprise inference platform and, increasingly, an agent-dispatch service on top of it. Its Agents API accepts a task over HTTP, runs it in an isolated cloud sandbox with full terminal, filesystem, and Git access, streams logs back to the caller, and opens pull requests with scoped branches and test evidence on GitHub, GitLab, or Bitbucket. A distinguishing capability is multi-agent orchestration: the same task can be dispatched in parallel to Blackbox, Claude Code, Codex, and Gemini agents, with a 'Chairman LLM' evaluating the implementations and a human able to override the selection. The company also ships an 'agentic terminal' CLI and a VS Code extension ('Blackbox Agent - Coding Copilot') that edits files and runs commands with per-step permission. Enterprise inference is the revenue engine — zero data retention at the gateway and single-tenant GPU deployments — with the coding agent layered on the same infrastructure for teams that want both from one vendor.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/blackbox-ai.md)
