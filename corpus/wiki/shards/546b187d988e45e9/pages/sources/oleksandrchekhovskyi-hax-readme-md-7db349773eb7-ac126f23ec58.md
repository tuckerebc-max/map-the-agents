---
access: public
aliases: []
claim_ids:
- clm_0f36525f32f17b453ee4879d1d93804220d1cbd4626418aa397337225ec83e72
- clm_30bcf644ee94d3af4f80a09281ab902a760de0c5d924057511c412a6f0240cb9
- clm_362da9659487f20a7268af2e770bc0e5fa0d6edf7fced28afd16b535c1ef1db2
- clm_63e789213d56068885577357f057d841d23bb86aa233dcce102425a6838d7f49
- clm_6b6385776d48222ef924641d5e9da65f1842e55b08ac8557f774829c385966c9
- clm_87b02669371e24fa28b69b6621de571692886c9c379d2e014c867058acb9e174
- clm_97e1694f9ea8308f67ad197642023ca9026e25398050262352d0d71c1840b615
- clm_defc6b4ab2f30fe75377dab8c4d6c2a1adfd56a0545a2f1f11d41873e00aa16f
- clm_e89eb6ec1c02f1fa6269c0cd31c8271d35076382d550e55de55c8ba5876ede2a
maturity: draft
page_id: pg_297be6070c2a5995af29ac126f23ec58
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0495887c31cc5dab983967fddfa22b1e
title: OleksandrChekhovskyi/hax/README.md @ 7db349773eb7
updated_at: '2026-09-14T02:24:52Z'
---

# OleksandrChekhovskyi/hax/README.md @ 7db349773eb7

<!-- rcw:begin owner=source:src_0495887c31cc5dab983967fddfa22b1e block=evidence -->
- The CLI supports an interactive REPL, one-shot `-p` prompts (including stdin input), `-c` to continue the latest session, and `--resume`/`--resume=ID` session selection. [@claim:clm_0f36525f32f17b453ee4879d1d93804220d1cbd4626418aa397337225ec83e72]
- In the REPL, slash commands such as `/provider`, `/model`, `/effort`, `/preset`, `/config`, and `/preset-save` select providers and settings; Ctrl-T opens a transcript view in $PAGER and Ctrl-O shows the conversation as displayed. [@claim:clm_30bcf644ee94d3af4f80a09281ab902a760de0c5d924057511c412a6f0240cb9]
- The bash tool runs commands through a configurable shell with a default 2-minute timeout before detaching; the maximum timeout a model may request defaults to 30 minutes, and no per-command permission prompts exist by design. [@claim:clm_362da9659487f20a7268af2e770bc0e5fa0d6edf7fced28afd16b535c1ef1db2]
- The product runs on Linux, macOS, FreeBSD, and OpenBSD; on Windows it is used under WSL, and the BSDs are build-from-source only. [@claim:clm_63e789213d56068885577357f057d841d23bb86aa233dcce102425a6838d7f49]
- Provider support includes OpenAI and compatible endpoints, Anthropic and compatible endpoints, Codex via ChatGPT login, OpenRouter, OpenCode Zen/Go, llama.cpp, ollama, and custom endpoints configured through providers.<id> blocks. [@claim:clm_6b6385776d48222ef924641d5e9da65f1842e55b08ac8557f774829c385966c9]
- Building from source requires a C compiler, libcurl, jansson, meson, ninja, and pkg-config; fzf is additionally used for @file completion when available. [@claim:clm_87b02669371e24fa28b69b6621de571692886c9c379d2e014c867058acb9e174]
- hax is described as a minimalist, terminal-native coding agent implemented as a single native C binary with a small dependency set and low memory use. [@claim:clm_97e1694f9ea8308f67ad197642023ca9026e25398050262352d0d71c1840b615]
- The project deliberately omits MCP marketplaces, a plugin runtime, IDE panels, and per-command permission prompts, composing instead via subprocesses and documenting each omission in docs/philosophy.md. [@claim:clm_defc6b4ab2f30fe75377dab8c4d6c2a1adfd56a0545a2f1f11d41873e00aa16f]
- By design hax lacks MCP marketplaces, a plugin runtime, IDE panels, and per-command permission prompts; the philosophy doc explains each omission and the pattern covering the need. [@claim:clm_e89eb6ec1c02f1fa6269c0cd31c8271d35076382d550e55de55c8ba5876ede2a]
<!-- rcw:end owner=source:src_0495887c31cc5dab983967fddfa22b1e block=evidence -->

## Researcher notes

