# Bandit Stealth (`bandit-stealth`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: BurtsonLabs
- License: Apache-2.0
- Language: unknown
- Interface: platforms=IDE; install=Install from Open VSX
- Model providers: Ollama, Qwen
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [burtson-labs/bandit-agent-framework](../../repos/burtson-labs/bandit-agent-framework.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Local-first coding agent running Ollama models with tool use, diff approvals, and voice

(captured site page body (agents/bandit-stealth.md), not a verified repo-code finding)
Bandit Stealth is a coding agent extension for VS Code and OpenVSX-compatible editors that runs locally on any Ollama model - Gemma, Qwen, Devstral, or a custom fine-tune - keeping code entirely on the user's machine by default. The agent autonomously explores the codebase, reads and writes files, and runs shell commands, with every write gated behind a unified-diff approval and inline diffs streaming into the editor as it works. Distinctive mechanics include agent-authored skills, plan preview with go/no-go confirmation, session checkpoints with /rewind, hooks for CI guardrails, and pre-write language validation for TypeScript, Python, JSON, and C#. Voice is fully pluggable and provider-independent (Bandit cloud, Whisper-compatible servers, ElevenLabs, or a local Piper server), and the composer accepts queued input while the agent streams. A companion CLI ships on npm, and an optional hosted gateway offers managed inference. It targets developers who want a real agentic loop without cloud subscriptions or code leaving the device.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/bandit-stealth.md)
