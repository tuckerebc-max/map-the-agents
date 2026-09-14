---
access: public
aliases: []
claim_ids:
- clm_2997ed0ba4e96f2f5ffb4631d9acf945bb0a46a9f0b2a815b8dea17b4da4a4c2
- clm_322c932866838250b1c026716928ebc10b193200b2978be15ba95b165d75b1d8
- clm_33944129e45cb908a9a37110b1a74fc440a964a49bcbb4c792db28cecf059aca
- clm_8b2ab68d870210ff235cb484e2e8612cedacee102d068334f30914f20513d08c
- clm_8f6a78a445246f4cfa675c9028c09718d38a2e2278561389d52c4a30a2b98379
- clm_9b8adc6e473988b91de43b21e2b92eed6d602ed5627a71b9cea7aca62f2997c0
- clm_9d07ff204b709f04d399425f08c613df4dbc61d9fbd96e4f937cd6046dbfafd0
- clm_e3ea0d966f27771d903ceb230a09c4abbb1636b8a608efb5b49b8bb5d1e5d038
- clm_f2000a24957a8e4d8cb8c74d6dd098f5f2247083be63ee756873cb098a51248e
maturity: draft
page_id: pg_fba1e665b0a05d4e9b6553ddeb815133
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9504e92061f2538886fa885257981a0d
title: ovh/shai/README.md @ f076f6128a82
updated_at: '2026-09-14T02:28:49Z'
---

# ovh/shai/README.md @ f076f6128a82

<!-- rcw:begin owner=source:src_9504e92061f2538886fa885257981a0d block=evidence -->
- Shai works with multiple LLM providers including OVHcloud (default, anonymous with rate limits), OpenAI, and other compatible endpoints; `shai auth` configures sign-in or provider selection. [@claim:clm_2997ed0ba4e96f2f5ffb4631d9acf945bb0a46a9f0b2a815b8dea17b4da4a4c2]
- Server options include `--port` (default 3000), `--ephemeral` to spawn a new agent per request, and an optional agent name for a persistent session. [@claim:clm_322c932866838250b1c026716928ebc10b193200b2978be15ba95b165d75b1d8]
- For OVHcloud, function-calling models (e.g. gpt-oss-120b, gpt-oss-20b, Mistral-Small-3.2-24B) are recommended, or any model with structured output forced via the `/set so` option. [@claim:clm_33944129e45cb908a9a37110b1a74fc440a964a49bcbb4c792db28cecf059aca]
- Project context is loaded from a `SHAI.md` file at the project root, which the agent automatically reads as additional context. [@claim:clm_8b2ab68d870210ff235cb484e2e8612cedacee102d068334f30914f20513d08c]
- Custom agents can be defined in separate config files placed under ~/.config/shai/agents/, listed with `shai agent list`, and run via `shai agent <name>`; MCP and OAuth are supported. [@claim:clm_8f6a78a445246f4cfa675c9028c09718d38a2e2278561389d52c4a30a2b98379]
- A shell-assistant mode hooks the terminal via `shai on`/`shai off`, sending the last command, output, and error code to the LLM provider to suggest fixes for failed commands. [@claim:clm_9b8adc6e473988b91de43b21e2b92eed6d602ed5627a71b9cea7aca62f2997c0]
- Running `shai` starts an interactive terminal coding agent for chatting, writing code, fixing bugs, and answering questions. [@claim:clm_9d07ff204b709f04d399425f08c613df4dbc61d9fbd96e4f937cd6046dbfafd0]
- Headless mode accepts a piped prompt and streams events to stderr; shai can be told to return the whole conversation as a trace, which enables chaining shai calls. [@claim:clm_e3ea0d966f27771d903ceb230a09c4abbb1636b8a608efb5b49b8bb5d1e5d038]
- `shai serve --port 3000` runs an HTTP service with SSE streaming and OpenAI-compatible endpoints including POST /v1/chat/completions and POST /v1/responses. [@claim:clm_f2000a24957a8e4d8cb8c74d6dd098f5f2247083be63ee756873cb098a51248e]
<!-- rcw:end owner=source:src_9504e92061f2538886fa885257981a0d block=evidence -->

## Researcher notes

