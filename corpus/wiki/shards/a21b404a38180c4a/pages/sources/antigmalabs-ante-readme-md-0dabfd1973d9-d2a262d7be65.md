---
access: public
aliases: []
claim_ids:
- clm_136e843f432ec1c67ad21c7a6db0b98e983ef024ccca329ef301b822a3df396c
- clm_1536617fa91d3fba8018238f5fd0778001e9960dbbaf5a8895db43e0d1f47b28
- clm_270dcd4075f63ed3b3b179c11a9bf71c90bf1041efadbfd685f150625d1a53b1
- clm_2d447f1d23848a421c2606881695f450e4a1dd8b6984baa41cace57fa1e00a40
- clm_633323cd60bd8dbf0b5e51bb911a536eb4ba0dc43acbf914e6d1ef4b7e8b9ca2
- clm_641ee45bafd5670951441f4ab944b80c1500611c2138eed08ecb577bfe4e3f19
- clm_77475212e9c7f7b83fbcc2d08c9ca3213503bee5fd2ca6cd387a1dcd62fb068d
- clm_86cb6729e9f973bcf4b81f2ba401b8d48fbce44023b7a072bb8b65b41974b636
- clm_a2b28fa2c6bb4302a640e36d3f631ef7a1bd11133ec1368317210e3c90eba2c1
- clm_a2bf168f136c18ae234133ddd641f8a7376615fbb77658a99eebfb3424ac96f8
- clm_abcdfda918bd3df3f660890a56980d01438816dd1c94ba3b1c4736c7f269164a
- clm_de3f3f725a7df0302bd66cf270827256a60512242103c4b058bf4523d9b5015d
- clm_f0622cb95d5a23580c9f3807daf37140ce092b8f8983bbfdbe963b2354008b51
maturity: draft
page_id: pg_380d717cdce450109874d2a262d7be65
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_53a4c530880d5a2789b0af4103de25fa
title: AntigmaLabs/ante/README.md @ 0dabfd1973d9
updated_at: '2026-09-14T01:34:29Z'
---

# AntigmaLabs/ante/README.md @ 0dabfd1973d9

<!-- rcw:begin owner=source:src_53a4c530880d5a2789b0af4103de25fa block=evidence -->
- A settings profile can define the whole agent, including a replacement system prompt, tool set, skills, and memory; `--profile <name>` swaps profiles per run, and a built-in `bare` profile strips skills, MCP, session saving, and auto-memory. [@claim:clm_136e843f432ec1c67ad21c7a6db0b98e983ef024ccca329ef301b822a3df396c]
- Ante ships 17 maintained provider presets (Anthropic, OpenAI, Gemini, Grok, DeepSeek, Open Router, local GGUF, and others) and supports custom endpoints via a `~/.ante/catalog.json` config with wire_style, auth style, headers, and extra_body. [@claim:clm_1536617fa91d3fba8018238f5fd0778001e9960dbbaf5a8895db43e0d1f47b28]
- Local inference uses a pinned, managed llama.cpp engine that runs GGUF models entirely on-machine with no API key or internet; the `--offline-model` flag points at a GGUF file. [@claim:clm_270dcd4075f63ed3b3b179c11a9bf71c90bf1041efadbfd685f150625d1a53b1]
- Repository source (including SDK and protocol crates) is Apache 2.0 licensed, while the prebuilt binary is governed by separate Binary Preview Terms permitting free commercial use during the preview. [@claim:clm_2d447f1d23848a421c2606881695f450e4a1dd8b6984baa41cace57fa1e00a40]
- Ante is described as a self-contained terminal coding agent shipped as a single Rust executable with zero runtime dependencies, about 15MB compressed. [@claim:clm_633323cd60bd8dbf0b5e51bb911a536eb4ba0dc43acbf914e6d1ef4b7e8b9ca2]
- The core harness source is not in this repository; it is developed privately during alpha and shipped as a prebuilt binary, with core libraries like `crates/exec` added progressively as they stabilize. [@claim:clm_641ee45bafd5670951441f4ab944b80c1500611c2138eed08ecb577bfe4e3f19]
- Ante is evaluated continuously on Terminal-Bench 2.1 under official leaderboard constraints (89 tasks, 5 trials each); the latest reported full run scored 82.7% with DeepSeek V4 Flash 0731, with raw Harbor runs linked for audit. [@claim:clm_77475212e9c7f7b83fbcc2d08c9ca3213503bee5fd2ca6cd387a1dcd62fb068d]
- The curated `pi` profile reduces Ante to four tools (Read, Write, Edit, Bash) plus a short replacement system prompt, with file search via `rg`, subagents via `ante -p`, and web access via `curl`. [@claim:clm_86cb6729e9f973bcf4b81f2ba401b8d48fbce44023b7a072bb8b65b41974b636]
- The project is a beta preview with expected breaking changes and incomplete functionality, and supports macOS and Linux only, with WSL suggested on Windows. [@claim:clm_a2b28fa2c6bb4302a640e36d3f631ef7a1bd11133ec1368317210e3c90eba2c1]
- The `crates/protocol-shape` crate defines the schema and wire messages spoken by `ante serve`, and `crates/ante-sdk` is a Rust SDK/client for building against agent runtimes. [@claim:clm_a2bf168f136c18ae234133ddd641f8a7376615fbb77658a99eebfb3424ac96f8]
- The documented architecture is client-daemon: TUI, headless, and serve clients connect to a daemon organized as Session, Turn, Step, with tools, permissions, and skills/agents, above a provider layer. [@claim:clm_abcdfda918bd3df3f660890a56980d01438816dd1c94ba3b1c4736c7f269164a]
- The repo contains `ante-harbor/`, a Harbor agent adapter behind the Terminal-Bench results, intended for reproducing published runs. [@claim:clm_de3f3f725a7df0302bd66cf270827256a60512242103c4b058bf4523d9b5015d]
- Ante offers four run modes: interactive TUI (`ante`), headless one-shot (`ante -p`), server daemon (`ante serve`) over a JSONL protocol, and gateway mode for Slack/Discord bots. [@claim:clm_f0622cb95d5a23580c9f3807daf37140ce092b8f8983bbfdbe963b2354008b51]
<!-- rcw:end owner=source:src_53a4c530880d5a2789b0af4103de25fa block=evidence -->

## Researcher notes

