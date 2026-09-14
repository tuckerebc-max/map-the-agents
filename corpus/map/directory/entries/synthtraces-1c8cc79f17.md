# synthtraces (`synthtraces`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: julien-c
- License: MIT
- Language: TypeScript
- Interface: install=Node/TypeScript project (pnpm); runs the Pi coding agent per session
- Model providers: Remote hosted open models (DeepSeek-V4-Pro, gpt-oss-120b, Qwen3.6-27B, GLM-5.1, etc.), Local models via llama.cpp
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [julien-c/synthtraces](../../repos/julien-c/synthtraces.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Generates synthetic coding agent session traces by pairing two models: a remote open model as the coding agent and a local llama.cpp model as the user, across 20 codebases x 20 starting questions = 24,000 total sessions.

(captured site page body (agents/synthtraces.md), not a verified repo-code finding)
Synthtraces exists to supply realistic multi-turn interaction data for coding-agent research without proprietary logs. Each generated session boots the Pi coding agent with read, write, edit, and bash tools inside one of twenty real codebases (transformers, diffusers, lerobot, candle, and others), pairs it with a remotely hosted open model, and has a local llama.cpp model play the user starting from one of twenty seed questions such as 'How is CI set up in this repo?'. The released dataset is the cross product of 20 agent models, 3 local user models, 20 codebases, and 20 questions — 24,000 sessions — published on Hugging Face alongside this small TypeScript generator. Because both sides are models, the traces capture authentic tool-use dynamics (edits, shell runs, follow-up questions) without any human transcription effort. Researchers studying agent behavior across model families or training interaction models are the intended consumers.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/synthtraces.md)
