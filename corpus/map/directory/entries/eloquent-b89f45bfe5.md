# Eloquent (`eloquent`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: boneylizard
- License: AGPL-3.0
- Language: Python
- Interface: platforms=IDE; install=Clone repo, run install.bat then run.bat (Windows only). Requires Python 3.11/3.12, Node.js v21.7.3, NVIDIA GPU.
- Model providers: Local (llama.cpp GGUF), OpenAI-compatible APIs
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: True (reported)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: False (reported)
  - plan_mode: False (reported)

No repository record: repository source unavailable in this directory capture, not an absence of capability.

## Description

Highlight (site page `what_makes_it_special`): Local AI workstation combining LLM chat/roleplay, in-house Stable Diffusion image generation, voice cloning, research-grade model ELO testing, forensic linguistics, and a tool-calling code editor into a single application running entirely locally without subscriptions. Features working multi-GPU inference, multi-role chat with story state tracking, voice cloning with paralinguistic cues, and a built-in model ELO testing framework.

(captured site page body (agents/eloquent.md), not a verified repo-code finding)
Eloquent consolidates the local-AI stack that users otherwise assemble from half a dozen separate tools, motivated by the position that chat, image generation, voice, and coding should share one local runtime with no subscriptions and no third-party data flow. The code editor embeds a tool-calling agent with seven tools covering file operations, automatic .bak backups, and optionally sandboxed shell execution, with chain-of-thought visualization, hallucination rescue, and loop detection to keep long runs usable on local models. The rest of the app serves the same single-machine philosophy: local Stable Diffusion (SD 1.5, SDXL, FLUX) with optional cloud fallback, voice cloning, an ELO-testing framework for comparing models, and forensic linguistics tools. It targets Windows users with NVIDIA GPUs who want experimentation without cloud dependencies or subscriptions.
Sources: [published index (sha256:5b67dbf818cd)](https://alltheagents.org/agents.json); [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/eloquent.md)
