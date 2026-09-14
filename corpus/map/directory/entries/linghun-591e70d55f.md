# Linghun (`linghun`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: linghungegeg
- License: Apache-2.0
- Language: TypeScript
- Interface: platforms=IDE; install=npm install -g @linghun/cli
- Model providers: OpenAI-compatible, DeepSeek, Anthropic Messages-style endpoints
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: unknown (unknown)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: unknown (unknown)

Repository map entry: [linghungegeg/linghun](../../repos/linghungegeg/linghun.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first, evidence-first AI coding terminal with an anti-hallucination system enforcing evidence-first engineering (reading facts, verifying, distinguishing verification scopes, refusing unverified claims, and expressing uncertainty as runtime constraints); Chinese and Windows are first-class citizens

(captured site page body (agents/linghun.md), not a verified repo-code finding)
Linghun's premise is that hallucinated success is the worst failure mode of coding agents, so it enforces evidence as a runtime constraint rather than a prompt instruction: answers are classified PASS/PARTIAL/FAIL against what was actually read and verified, and the final-answer gate refuses unverified claims. The harness adds workspace snapshots, git stable points and worktrees, controlled memory with failure learning, multi-model role routing, and an App Bridge capability runtime for connecting external applications via manifests and local HTTP connectors. Windows, PowerShell, and Chinese paths are first-class, reflecting its user base. It ships as an npm-distributed Apache-2.0 CLI with a published whitepaper in Chinese and English.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/linghun.md)
