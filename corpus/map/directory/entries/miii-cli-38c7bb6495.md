# miii-cli (`miii-cli`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: maruakshay
- License: MIT
- Language: TypeScript/Node.js
- Interface: platforms=CLI; install=macOS/Linux: curl -fsSL https://raw.githubusercontent.com/maruakshay/miii-cli/main/install.sh | sh; Windows: irm https://raw.githubusercontent.com/maruakshay/miii-cli/main/install.ps1 | iex; npm: npm install -g miii-agent
- Model providers: Ollama (default), any OpenAI-compatible local server (llama.cpp, LM Studio)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: True (reported)

Repository map entry: [maruakshay/miii-cli](../../repos/maruakshay/miii-cli.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): 100% local and private open-source terminal AI coding agent — code never leaves your machine, no cloud, no accounts, works fully offline. Free forever with no API keys or per-token metering. Lossless output spill: large tool outputs are written to disk and paged through by the model, never truncated. miii doctor grades installed local models on real engineering tasks. Plan ...

(captured site page body (agents/miii-cli.md), not a verified repo-code finding)
miii exists for engineers whose code cannot leave the machine: it talks only to local inference servers — Ollama by default, plus any OpenAI-compatible local endpoint like llama.cpp or LM Studio — so it works offline with no accounts and no per-token billing. The loop plans a task, acts through six permission-gated tools (read, write, edit, glob, grep, bash) confined to the workspace, and observes results before proceeding, with ~/.miii/permissions.json persisting approvals across sessions. Two implementation choices stand out: oversized tool output is written to disk and paged through the model rather than truncated, so long build logs survive intact, and MIII.md plays the role of CLAUDE.md as a per-repo conventions file read every turn. Model choice is hardware-bound — qwen2.5-coder 7b for 8 GB VRAM up to 32b at 48 GB+ — and miii doctor grades installed candidates on real tasks rather than trusting benchmarks. Privacy-sensitive codebases and offline environments are the audience; the project is a one-maintainer MVP at small star count but actively developed.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/miii-cli.md)
