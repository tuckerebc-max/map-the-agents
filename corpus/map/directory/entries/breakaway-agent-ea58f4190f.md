# Breakaway Agent (`breakaway-agent`)

[Back to directory index](../index.md)

Directory membership: published+pages.

- Category: agent
- Provider/maker: 2389-research
- License: unknown
- Language: TypeScript
- Interface: platforms=CLI; install=git clone, bun install
- Model providers: OpenAI-compatible (configurable via .env)
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (swappable policy, context strategy, tools, system prompt) (yes)
  - claude_code_plugin: no (no)
  - subagents: yes (spawn_agent tool with depth cap) (yes)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [2389-research/breakaway-agent](../../repos/2389-research/breakaway-agent.md) (source: page, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Deliberately tiny, hackable code agent and experiment platform with a policy-blind core loop (~165 lines in src/agent.ts) where all behavior is injected via a Policy object — error policy, max turns, context strategy, and tools are all user-editable. Runs in YOLO mode with no permission prompts, supports self-modification via SIGHUP/SIGUSR2 hot-reload, and detached subagents.

(captured site page body (agents/breakaway-agent.md), not a verified repo-code finding)
Breakaway Agent is a deliberately small experiment bed for people who want to study and reshape the agent loop itself. Built on Bun, the core loop lives in roughly 165 lines of TypeScript and exposes only five tools — read_file, write_file, edit_file, bash, and spawn_agent — with every behavioral knob (error policy, max turns, context strategy, system prompt, tool set) injected through a swappable Policy object rather than hardcoded. It runs in YOLO mode with no permission prompts, so it is comfortable executing long unattended runs, and it treats its own code as mutable: a SIGHUP or SIGUSR2 hot-reload re-reads its configuration and policy without dropping the session, making self-modification part of the workflow. Detached subagents fan out via spawn_agent under a depth cap. The audience is researchers and tinkerers exploring agent-loop design, not users who want a polished out-of-the-box coding assistant.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/breakaway-agent.md)
