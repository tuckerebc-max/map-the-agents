# UltraGameStudio (`ultragamestudio`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: wellingfeng
- License: MIT
- Language: TypeScript, Rust
- Interface: install=cd app && npm install && npm run dev (web) or npm run desktop; or ./run.sh (macOS/Linux), run.bat (Windows)
- Model providers: Claude Code, Codex, Gemini, NVIDIA NIM, OpenRouter, GitHub Models, Hugging Face, SambaNova, Together AI, DeepSeek, Mistral, Groq, Fireworks, Cerebras, Ollama, LM Studio, llama.cpp
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: True (reported)
  - hooks: no (no)
  - plan_mode: True (reported)

Repository map entry: [wellingfeng/ultragamestudio](../../repos/wellingfeng/ultragamestudio.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI coding agent built specifically for game development. Speaks game-engine language (materials, blueprints, terrain, UMG, skeletal animation, packaging), generates all game asset types (images, 3D models, 2D sprites, atlases, audio, rigging, video) from the same chat surface, ships 40+ game-dev expert roles across Unity/Unreal/Godot/Web, and routes routine work through 20+ free/low-cost channels to save premium quota.

(captured site page body (agents/ultragamestudio.md), not a verified repo-code finding)
UltraGameStudio exists because general-purpose coding agents do not speak game engines: they cannot reason about materials, blueprints, or skeletal animation, and they cannot produce the assets games require, forcing developers back to bespoke pipelines for every asset type. The app wraps the coding-agent pattern in a game-first surface: chat requests route to engine-specialist expert roles spanning Unity, Unreal, Godot, and web projects, while slash commands generate sprites, meshes, atlases, music, and video inline. A /studio command assembles a per-task execution harness with parallel subagents, adversarial verification, and acceptance gates, and a local Rust proxy translates between provider protocols so free channels — NVIDIA NIM, OpenRouter, keyless gateways, local runtimes — absorb routine work and fail over automatically. Game developers working in Unity, Unreal, Godot, or web engines use it; it is MIT-licensed, free, and stores sessions and keys locally.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/ultragamestudio.md)
