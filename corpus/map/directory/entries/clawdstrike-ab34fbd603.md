# clawdstrike (`clawdstrike`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: backbay-labs
- License: Apache-2.0
- Language: Rust, TypeScript, Python, Go
- Interface: platforms=Autonomous; install=brew install backbay-labs/tap/clawdstrike; npm install @clawdstrike/sdk; pip install clawdstrike; cargo add clawdstrike
- Model providers: OpenAI, Anthropic (Claude), Vercel AI, LangChain, OpenClaw
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [backbay-labs/clawdstrike](../../repos/backbay-labs/clawdstrike.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Policy engine / EDR / signed audit chain for AI agents and OS-level events. Treats AI tool calls in the same taxonomy as kernel events (file access, process exec, network flow, etc.). Fail-closed defaults, Ed25519-signed causal graph, formally verified (Lean 4).

(captured site page body (agents/clawdstrike.md), not a verified repo-code finding)
Clawdstrike exists because agent tool calls have OS-level blast radius but no OS-level enforcement: it applies the EDR model to AI agents, evaluating tool calls and OS events against a policy of guards (forbidden paths, egress allowlists, secret-leak detection, MCP tool gates, prompt-injection detection) that defaults to deny when configuration or evaluation fails. Every verdict produces an Ed25519-signed receipt hashed into a per-session causal graph, and enterprise deployments chain receipts over NATS into a tamper-evident audit log. Core decision logic carries Lean 4 formal verification differentially tested against the Rust implementation. Security teams deploying Claude Code, Cursor, or OpenClaw use it to fail closed rather than trust model behavior.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/clawdstrike.md)
