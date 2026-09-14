# OMK (`omk`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: dmae97
- License: MIT
- Language: TypeScript
- Interface: platforms=CLI, IDE; install=npm install -g open-multi-agent-kit --ignore-scripts; or npx --ignore-scripts open-multi-agent-kit; requires Node.js 22.19+
- Model providers: Codex, Claude Code, OpenCode, Kimi, GLM/ZAI, xAI/Grok, NVIDIA NIM, local providers
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry (renamed): original lead [dmae97/open-multi-agent-kit](https://github.com/dmae97/open-multi-agent-kit) (source: backing, field: `source_code_url`) now resolves to [dmae97/omk](../../repos/dmae97/omk.md) (github id 1225139405, verified [https://github.com/dmae97/omk](https://github.com/dmae97/omk)).

## Description

Highlight (site page `what_makes_it_special`): Provider-neutral multi-agent control plane with a 4-step loop (Scope, Route, Verify, Replay); turns goals into bounded DAGs with owned paths; evidence-gated completion prevents parallel agents from overwriting each other; keeps routing separate from execution contract

(captured site page body (agents/omk.md), not a verified repo-code finding)
OMK is a provider-neutral coding-agent harness organized around four phases: scope goals into bounded DAGs, route work through a provider-neutral model registry, verify completion with evidence-gated build/test/audit gates, and replay with durable receipts. Sandbox isolation is on by default, with network-blocked OS sandboxing for shell commands. The project is unusually explicit about its limits, documenting a prior release's fabricated evidence and refusing to treat prompt agreement as a correctness verdict. It builds on Mario Zechner's pi harness via the oh-my-pi fork, with optional orchestration extensions on top of the default single-agent loop. Release notes are detailed and development is active, though the contributor base is a single author.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/omk.md)
