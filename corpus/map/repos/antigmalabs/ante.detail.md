# antigmalabs/ante -- full detail

[Back to orientation](ante.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/antigmalabs/ante/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/631707f027372ad4.json](../../../wiki/dossiers/antigmalabs/ante/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/631707f027372ad4.json)

## specifications (1 claim(s))

- [observation/documented] Ante is described as a self-contained terminal coding agent shipped as a single Rust executable with zero runtime dependencies, about 15MB compressed. -- evidence: [README.md#L21-L21](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L21-L21), [README.md#L112-L112](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L112-L112) (`clm_633323cd60bd8dbf0b5e51bb911a536eb4ba0dc43acbf914e6d1ef4b7e8b9ca2`)

## components (2 claim(s))

- [observation/documented] The curated `pi` profile reduces Ante to four tools (Read, Write, Edit, Bash) plus a short replacement system prompt, with file search via `rg`, subagents via `ante -p`, and web access via `curl`. -- evidence: [README.md#L169-L169](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L169-L169) (`clm_86cb6729e9f973bcf4b81f2ba401b8d48fbce44023b7a072bb8b65b41974b636`)
- [observation/documented] The repo contains `ante-harbor/`, a Harbor agent adapter behind the Terminal-Bench results, intended for reproducing published runs. -- evidence: [README.md#L221-L223](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L221-L223) (`clm_de3f3f725a7df0302bd66cf270827256a60512242103c4b058bf4523d9b5015d`)

## design-choices (1 claim(s))

- [observation/documented] A settings profile can define the whole agent, including a replacement system prompt, tool set, skills, and memory; `--profile <name>` swaps profiles per run, and a built-in `bare` profile strips skills, MCP, session saving, and auto-memory. -- evidence: [README.md#L32-L32](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L32-L32), [README.md#L167-L167](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L167-L167), [README.md#L176-L176](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L176-L176) (`clm_136e843f432ec1c67ad21c7a6db0b98e983ef024ccca329ef301b822a3df396c`)

## workflows (1 claim(s))

- [observation/documented] Repository source (including SDK and protocol crates) is Apache 2.0 licensed, while the prebuilt binary is governed by separate Binary Preview Terms permitting free commercial use during the preview. -- evidence: [BINARY-TERMS.md#L3-L6](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/BINARY-TERMS.md#L3-L6), [README.md#L319-L323](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L319-L323), [README.md#L316-L317](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L316-L317), [BINARY-TERMS.md#L8-L10](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/BINARY-TERMS.md#L8-L10) (`clm_2d447f1d23848a421c2606881695f450e4a1dd8b6984baa41cace57fa1e00a40`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Ante offers four run modes: interactive TUI (`ante`), headless one-shot (`ante -p`), server daemon (`ante serve`) over a JSONL protocol, and gateway mode for Slack/Discord bots. -- evidence: [README.md#L126-L131](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L126-L131), [README.md#L307-L308](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L307-L308) (`clm_f0622cb95d5a23580c9f3807daf37140ce092b8f8983bbfdbe963b2354008b51`)
- [observation/documented] The `crates/protocol-shape` crate defines the schema and wire messages spoken by `ante serve`, and `crates/ante-sdk` is a Rust SDK/client for building against agent runtimes. -- evidence: [README.md#L221-L223](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L221-L223) (`clm_a2bf168f136c18ae234133ddd641f8a7376615fbb77658a99eebfb3424ac96f8`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The documented architecture is client-daemon: TUI, headless, and serve clients connect to a daemon organized as Session, Turn, Step, with tools, permissions, and skills/agents, above a provider layer. -- evidence: [README.md#L231-L258](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L231-L258), [README.md#L229-L229](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L229-L229) (`clm_abcdfda918bd3df3f660890a56980d01438816dd1c94ba3b1c4736c7f269164a`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] Ante is evaluated continuously on Terminal-Bench 2.1 under official leaderboard constraints (89 tasks, 5 trials each); the latest reported full run scored 82.7% with DeepSeek V4 Flash 0731, with raw Harbor runs linked for audit. -- evidence: [README.md#L36-L36](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L36-L36) (`clm_77475212e9c7f7b83fbcc2d08c9ca3213503bee5fd2ca6cd387a1dcd62fb068d`)

## dependencies (3 claim(s))

- [observation/documented] Local inference uses a pinned, managed llama.cpp engine that runs GGUF models entirely on-machine with no API key or internet; the `--offline-model` flag points at a GGUF file. -- evidence: [README.md#L295-L296](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L295-L296), [README.md#L56-L59](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L56-L59), [README.md#L54-L54](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L54-L54) (`clm_270dcd4075f63ed3b3b179c11a9bf71c90bf1041efadbfd685f150625d1a53b1`)
- [observation/documented] Ante ships 17 maintained provider presets (Anthropic, OpenAI, Gemini, Grok, DeepSeek, Open Router, local GGUF, and others) and supports custom endpoints via a `~/.ante/catalog.json` config with wire_style, auth style, headers, and extra_body. -- evidence: [README.md#L301-L302](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L301-L302), [README.md#L197-L197](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L197-L197), [README.md#L186-L195](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L186-L195), [README.md#L184-L184](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L184-L184) (`clm_1536617fa91d3fba8018238f5fd0778001e9960dbbaf5a8895db43e0d1f47b28`)
- [inference/documented] The core harness source is not in this repository; it is developed privately during alpha and shipped as a prebuilt binary, with core libraries like `crates/exec` added progressively as they stabilize. -- evidence: [README.md#L227-L227](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L227-L227), [README.md#L319-L323](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L319-L323) (`clm_641ee45bafd5670951441f4ab944b80c1500611c2138eed08ecb577bfe4e3f19`)

## limitations (2 claim(s))

- [observation/documented] The project is a beta preview with expected breaking changes and incomplete functionality, and supports macOS and Linux only, with WSL suggested on Windows. -- evidence: [README.md#L18-L19](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/README.md#L18-L19) (`clm_a2b28fa2c6bb4302a640e36d3f631ef7a1bd11133ec1368317210e3c90eba2c1`)
- [observation/documented] The prebuilt binary is alpha preview software under Binary Preview Terms: features may change or be removed and distribution may be discontinued at any time, with no warranty. -- evidence: [BINARY-TERMS.md#L16-L20](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/BINARY-TERMS.md#L16-L20), [BINARY-TERMS.md#L25-L27](https://github.com/AntigmaLabs/ante/blob/0dabfd1973d97c6d5a74cbd88d4cbd4129787493/BINARY-TERMS.md#L25-L27) (`clm_4cd5aefcb1d0235b83f48a1b9d97071051254eb3ba4bd8290e6884c0cfd9cd58`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

