# local-ai-code-assistant (`local-ai-code-assistant`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: MIKOTOKAWAII25
- License: MIT
- Language: HTML
- Interface: install=Download from release page; extract; run executable; select models from built-in model browser or point to local files
- Model providers: Hugging Face, Ollama, local GGUF/GPTQ
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: False (reported)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [mikotokawaii25/local-ai-code-assistant](../../repos/mikotokawaii25/local-ai-code-assistant.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Desktop AI 'weaver' (CodeLoom) for multi-model development; orchestrates multiple open-source LLMs (Mistral, Llama, Phi) into a single fully offline desktop coding environment; multi-weave architecture with up to 5 concurrent model sessions; contextual thread fusion between models; privacy-first with no telemetry; cross-platform with 12-language UI

(captured site page body (agents/local-ai-code-assistant.md), not a verified repo-code finding)
CodeLoom is built for developers who want multi-model AI assistance with zero cloud dependency: all inference runs locally through llama.cpp, ExLlama, or MLX backends, with no telemetry, accounts, or network calls. The loom metaphor is structural, not decorative - warp slots hold large models for architecture and refactoring while weft slots run 1-3B models for fast completion, and a cross-thread shuttle passes context between them so a small model's draft can be refined by a larger one. Up to five concurrent sessions can debate or collaborate, and prompt looms fan one task out to several models for parallel review. Models import from Hugging Face, Ollama, or local GGUF/GPTQ files with automatic quantization selection based on available VRAM. The repository is primarily a distribution and marketing page (the actual code ships as release downloads), and its Claude-related SEO tags contradict the open-models pitch, warranting caution.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/local-ai-code-assistant.md)
