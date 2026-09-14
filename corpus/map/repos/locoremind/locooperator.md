# locoremind/locooperator

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b185a4198e4a @ 85279ae690b3ef4c

## Summary (orientation draft, not independently verified)

The repository documents LocoOperator-4B, a distilled 4B tool-calling code-exploration agent model, plus a hybrid analysis pipeline (Claude Code + local llama.cpp server + routing proxy). Evidence is README-only documentation.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] LocoOperator-4B is a 4B-parameter tool-calling agent distilled from Qwen3-Coder-Next, built on the Qwen3-4B-Instruct-2507 base model. -- evidence: [README.md#L41-L41](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L41-L41), [README.md#L18-L18](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L18-L18), [README.md#L45-L54](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L45-L54)
- components (1 claim(s)):
  - [observation/documented] The repo ships a hybrid pipeline: a proxy (scripts/proxy.py) converts Anthropic Messages API to OpenAI Chat Completions, parses the model's tool-call output into tool_use blocks, and falls back to OpenRouter on context overflow. -- evidence: [README.md#L166-L169](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L166-L169), [README.md#L157-L157](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L157-L157)
- design-choices (1 claim(s)):
  - [observation/documented] The model is positioned as a local sub-agent (explorer) in a two-tier agent loop, with a main agent delegating codebase exploration to keep API cost and latency low. -- evidence: [README.md#L74-L74](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L74-L74), [README.md#L68-L68](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L68-L68)
- workflows (2 claim(s)):
  - [observation/documented] Usage workflow: place the GGUF at models/LocoOperator-4B-GGUF, put target repos under data/repos, add tab-separated query files, then run scripts/test_single.sh or scripts/analyze.sh for batch analysis. -- evidence: [README.md#L188-L188](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L188-L188), [README.md#L200-L202](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L200-L202), [README.md#L190-L190](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L190-L190), [README.md#L208-L214](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L208-L214), [README.md#L194-L196](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L194-L196)
  - [observation/documented] Recommended serving settings are a ~50K context size, max 10 turns, and temperature 0.7; .claude/settings.local.json is auto-generated from the .env key on first run. -- evidence: [README.md#L149-L153](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L149-L153), [README.md#L186-L186](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L186-L186)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] It emits structured tool-call JSON for Read, Grep, Glob, Bash, Write, Edit, and Task (subagent delegation). -- evidence: [README.md#L60-L64](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L60-L64)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] In the pipeline, the main agent runs as a cloud model while spawned subagents are routed by the proxy to the local llama-server, with automatic OpenRouter fallback if context limits or a 10-turn cap are exceeded. -- evidence: [README.md#L164-L164](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L164-L164), [README.md#L159-L162](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L159-L162)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (2 claim(s)):
  - [observation/documented] On 65 multi-turn samples from open-source projects, the model scored 100% tool-call presence alignment, 65.6% first tool-type match, and 100% JSON validity and argument syntax correctness. -- evidence: [README.md#L78-L78](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L78-L78), [README.md#L84-L89](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L84-L89)
  - [observation/documented] Compared to its teacher, the model produced 76 tool calls versus 89 across the 65 eval samples, and the teacher showed 87.6% argument syntax validity versus the student's 100%. -- evidence: [README.md#L115-L118](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L115-L118), [README.md#L99-L107](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L99-L107)
- dependencies (2 claim(s)):
  - [observation/documented] Prerequisites include Claude Code, llama.cpp, uv, and an OpenRouter API key; the GGUF model is served locally via llama-server. -- evidence: [README.md#L140-L145](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L140-L145), [README.md#L128-L131](https://github.com/LocoreMind/LocoOperator/blob/b185a4198e4a3a2d8655120513326d8b1b487872/README.md#L128-L131)
More evidence: [full detail](locooperator.detail.md)

Metadata and full claim list: [full detail](locooperator.detail.md)
Human notes ([notes](locooperator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
