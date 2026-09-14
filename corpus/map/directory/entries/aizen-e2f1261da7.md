# aizen (`aizen`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: aizen-stack
- License: Apache-2.0
- Language: Rust
- Interface: platforms=Autonomous; install=curl -fsSL https://raw.githubusercontent.com/aizen-stack/aizen/main/install.sh | sh (Linux/macOS) | irm ...install.ps1 | iex (Windows) | cargo install --git
- Model providers: Any OpenAI-compatible (OpenAI, OpenRouter, local llama.cpp/vLLM, Anthropic gateway)
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry (renamed): original lead [aizen-stack/aizen](https://github.com/aizen-stack/aizen) (source: backing, field: `source_code_url`) now resolves to [talmetis-labs/aizen](../../repos/talmetis-labs/aizen.md) (github id 1289932122, verified [https://github.com/talmetis-labs/aizen](https://github.com/talmetis-labs/aizen)).

## Description

Highlight (site page `what_makes_it_special`): Single 34 MB static binary with zero runtime deps (no Node/Python/Docker/cloud), ~10 ms cold start, runs on 512 MB VPS or Raspberry Pi; verify-gate runs tests/typecheck and fixes failures before reporting done; offline BM25-ranked memory brain + durable SOUL identity persona; OS-level sandbox (Landlock+seccomp on Linux, Seatbelt on macOS, Job-Object on Windows) with deny-by-default networking; phone-controlled remote operation via Telegram/Discord ...

(captured site page body (agents/aizen.md), not a verified repo-code finding)
Aizen targets the ops-light end of the spectrum: one static binary that runs on a 512 MB VPS or Raspberry Pi with no cloud account, driven by any OpenAI-compatible endpoint (OpenAI, OpenRouter, local llama.cpp/vLLM, Anthropic gateways). The loop pairs a chat REPL with parallel reads, LSP-powered symbolic edits, and a verify gate that must pass tests and typechecks before the agent claims completion; a workflow command fans out role-scoped subagents and synthesizes the result. Sandboxing is layered under approvals — Landlock plus seccomp on Linux, Seatbelt on macOS, Job Objects on Windows — with network denied by default and API keys withheld from child processes. Extras include git-backed /timemachine checkpoints, Telegram/Discord-driven headless mode (aizen serve), and BM25 offline memory; versions after v0.5.5 are Apache-2.0, actively released (v0.6.1).
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/aizen.md)
