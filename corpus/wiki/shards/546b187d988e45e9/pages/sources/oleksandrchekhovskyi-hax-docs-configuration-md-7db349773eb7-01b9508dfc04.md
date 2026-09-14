---
access: public
aliases: []
claim_ids:
- clm_0eb128f3673858b61ac29b3ec092b37a95ce3fb8ae2d00f54822e11cd41a6aef
- clm_30bcf644ee94d3af4f80a09281ab902a760de0c5d924057511c412a6f0240cb9
- clm_362da9659487f20a7268af2e770bc0e5fa0d6edf7fced28afd16b535c1ef1db2
- clm_5b48e394d74fd4fa22e8c34b1d56a86245e86f2f59566d205b05e13fb73bab0d
- clm_643e2a0ab2ba1350b992425809e4d12e3230d8b478ae6c689b84a7e507d5b08c
- clm_6b6385776d48222ef924641d5e9da65f1842e55b08ac8557f774829c385966c9
- clm_9b59f4f15688487fb745cb0a2d3d2ba62e878be4b35204e34833b791474440f9
- clm_bc9b23f179cc2547507574b6a9ac45cc57bb72cbc7b4a1e7c28673849daa812f
- clm_c9d5a1b88cdac4f985913f789a56f9a7e6ca46b6f036521f66d9ef710fe1bc11
- clm_f236947bb815e2739c3fd0f79ebf9a5e98f648719e749328734746913f61a046
maturity: draft
page_id: pg_2157ec69dedf5894bd3c01b9508dfc04
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_afbde6178faf554e82c2127e95c35d59
title: OleksandrChekhovskyi/hax/docs/configuration.md @ 7db349773eb7
updated_at: '2026-09-14T02:24:52Z'
---

# OleksandrChekhovskyi/hax/docs/configuration.md @ 7db349773eb7

<!-- rcw:begin owner=source:src_afbde6178faf554e82c2127e95c35d59 block=evidence -->
- The agent manages background tasks with configurable wait timeout and a concurrency cap (default 32, up to 64), and bash commands detach after a default 2-minute timeout with a SIGTERM-to-SIGKILL grace period. [@claim:clm_0eb128f3673858b61ac29b3ec092b37a95ce3fb8ae2d00f54822e11cd41a6aef]
- In the REPL, slash commands such as `/provider`, `/model`, `/effort`, `/preset`, `/config`, and `/preset-save` select providers and settings; Ctrl-T opens a transcript view in $PAGER and Ctrl-O shows the conversation as displayed. [@claim:clm_30bcf644ee94d3af4f80a09281ab902a760de0c5d924057511c412a6f0240cb9]
- The bash tool runs commands through a configurable shell with a default 2-minute timeout before detaching; the maximum timeout a model may request defaults to 30 minutes, and no per-command permission prompts exist by design. [@claim:clm_362da9659487f20a7268af2e770bc0e5fa0d6edf7fced28afd16b535c1ef1db2]
- Presets can act as roles with description, system-prompt additions, and a tint; only presets with a description are advertised to the model as subagent delegation targets. [@claim:clm_5b48e394d74fd4fa22e8c34b1d56a86245e86f2f59566d205b05e13fb73bab0d]
- A wire-protocol trace can be collected via HAX_TRACE, capturing HTTP requests, statuses, and SSE events with credentials redacted; HAX_TRANSCRIPT mirrors the model-facing transcript to a file. [@claim:clm_643e2a0ab2ba1350b992425809e4d12e3230d8b478ae6c689b84a7e507d5b08c]
- Provider support includes OpenAI and compatible endpoints, Anthropic and compatible endpoints, Codex via ChatGPT login, OpenRouter, OpenCode Zen/Go, llama.cpp, ollama, and custom endpoints configured through providers.<id> blocks. [@claim:clm_6b6385776d48222ef924641d5e9da65f1842e55b08ac8557f774829c385966c9]
- Automatic compaction summarizes history near the context limit, triggered by a configurable percentage threshold (default 85), with the context limit overridable per model. [@claim:clm_9b59f4f15688487fb745cb0a2d3d2ba62e878be4b35204e34833b791474440f9]
- Settings resolve in order: current-process override, resumed conversation, environment, state.json, config.json, then default; the resumed tier covers provider, model, effort, and preset. [@claim:clm_bc9b23f179cc2547507574b6a9ac45cc57bb72cbc7b4a1e7c28673849daa812f]
- hax follows the XDG Base Directory specification: config at ~/.config/hax/config.json, remembered interactive selections and sessions under ~/.local/state/hax/, and a model-metadata cache at ~/.cache/hax/catalog.json. [@claim:clm_c9d5a1b88cdac4f985913f789a56f9a7e6ca46b6f036521f66d9ef710fe1bc11]
- Model metadata (context limits, image capability, estimated spend) is fetched from models.dev and cached, refreshed in the background only when a catalog-identified provider needs it and the cache is stale; fetching can be disabled via catalog.url or catalog.refresh. [@claim:clm_f236947bb815e2739c3fd0f79ebf9a5e98f648719e749328734746913f61a046]
<!-- rcw:end owner=source:src_afbde6178faf554e82c2127e95c35d59 block=evidence -->

## Researcher notes

