# momo-code (`momo-code`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: momozi1996
- License: MIT
- Language: TypeScript
- Interface: install=curl -fsSL https://momozi.cc/install | bash; or from source: git clone, npm install, npm run build (requires Node.js \>= 20.0.0; Python for simulation)
- Model providers: 25+ providers: Deepseek, Zhipu (GLM), Moonshot (Kimi), Anthropic (Claude), OpenAI (GPT-4), Google (Gemini), Doubao, OpenRouter, Groq, Mistral, custom OpenAI-compatible
- Feature flags (directory-reported):
  - mcp_support: True (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: True (reported)
  - subagents: True (reported)
  - hooks: True (reported)
  - plan_mode: True (reported)

Repository map entry: [momozi1996/momo-code](../../repos/momozi1996/momo-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): AI coding agent built on opencode with a dual-speed self-evolution system based on the Pioneer Agent research paper: a fast loop (/evolve) that learns tactics in seconds via KEP prompt injection with Thompson sampling, and a slow loop (/fine-tune) that improves model weights over hours via Monte Carlo Graph Search + LoRA with a ratchet gate ensuring monotonic improvement. Also ...

(captured site page body (agents/momo-code.md), not a verified repo-code finding)
momo-code starts from the opencode harness and adds machinery for the agent to learn from its own sessions. The fast loop observes session signals — test pass/fail, edit acceptance, user corrections — distills them into Tactic cards, selects candidates with Thompson sampling, and injects them into subsequent prompts; high-confidence tactics graduate into training curricula for the slow loop, where Monte Carlo Graph Search over pipeline configurations produces LoRA weight updates gated by a ratchet that rejects regressions, with spend bounded by a budget variable. A graph engine compiles long-horizon tasks into dependency DAGs whose nodes run as parallel child processes with state persisted to disk, so runs resume after restarts, and simulation-typed nodes can mix in physics-simulation agents. Claude Code migration is deliberately frictionless: existing MCP servers, settings, and prompts are inherited wholesale unless disabled. The tool stays local-first with sessions auditable on disk, targets developers of Chinese providers (GLM, Kimi, Doubao, DeepSeek) alongside Western ones, and remains a single-release v1.0.0 project from one maintainer.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/momo-code.md)
