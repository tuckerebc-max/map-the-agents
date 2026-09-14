# QonQrete (`qonqrete`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: QonQrete
- License: unknown
- Language: unknown
- Interface: platforms=IDE; install=Install from the JetBrains Marketplace
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: yes (yes)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Deterministic AI coding agent in secure sandboxes

(captured site page body (agents/qonqrete.md), not a verified repo-code finding)
QonQrete starts from the premise that AI coding fails not because models are weak but because the process around them is uncontrolled, so it replaces free-form agent sessions with a deterministic pipeline: plain-English tasks in a tasq.md file are clarified, planned into concrete steps with completion criteria and cost estimates, built inside a containerized qage sandbox, then reviewed by a validator that produces a structured verdict and repair plan with capped iterations. Outputs land in staging paths rather than your repository until you explicitly sync them, and a no-sync mode keeps everything out of the repo entirely, which also keeps source code away from cloud AI services by default. Every run leaves an on-disk audit trail — timeline, event log, run manifest, validation artifacts — so any construction is reproducible and resumable. Per-agent model configuration supports Venice, DeepSeek, OpenRouter, and local MLX or llama.cpp runtimes, with API keys held in the OS keychain. Solo developers and small teams use it when they want AI-built code they can inspect, gate, and reproduce rather than auto-merged diffs.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/qonqrete.md)
