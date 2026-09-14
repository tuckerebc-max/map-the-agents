---
access: public
aliases: []
claim_ids:
- clm_214b475617afe5ab5a8a10dd6bacc31f783e10bea3da90ccb87d15e32be4f071
- clm_57f3791bdbb4242ee1c2fb1d66cf8b7b6b01494e3fce24c6380526f3e5c0f06d
- clm_64928a2bb42f68b8759f757088018a623622d77883003b4f345b7a2aaab973d4
- clm_82d2db532e160c6d10531ca68f5ac597cda6c776478eb6426caa8f2ebc2f3da0
- clm_9b381d0a85d3702e1ef45d0da39de55edc64335af7d8b33f7c4d4e436f122294
- clm_b6fe8d95a9225345d04da83f13c9dfe92ed6bef7abb28678c2cbf0681013678b
- clm_bd0249cf9595c292e704a3b2f10b7b0adfb47460bd4e3724a046a87ebc39c83d
- clm_fbfbc55506c3fcfbd5e825f61177e82e5fd819f48623321b8855bb0d9ee6c595
maturity: draft
page_id: pg_19a15a0637a85d55bd261acdd3a1d8e4
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1d11d5883c665d4cbcd02544bbe24b18
title: yanhua1010/build-your-own-coding-agent/README.md @ 1e607dbb2f08
updated_at: '2026-09-14T04:32:51Z'
---

# yanhua1010/build-your-own-coding-agent/README.md @ 1e607dbb2f08

<!-- rcw:begin owner=source:src_1d11d5883c665d4cbcd02544bbe24b18 block=evidence -->
- The series uses pi (TypeScript, MIT, ~78k stars) as the main teaching text, with codex (Rust, ~101k stars) and grok-build (Rust, ~23k stars) used for architecture comparison. [@claim:clm_214b475617afe5ab5a8a10dd6bacc31f783e10bea3da90ccb87d15e32be4f071]
- The repository code is MIT licensed; quoted third-party snippets follow their original licenses (pi: MIT; codex and grok-build: Apache-2.0), with copyright retained by the original authors. [@claim:clm_57f3791bdbb4242ee1c2fb1d66cf8b7b6b01494e3fce24c6380526f3e5c0f06d]
- The repository is a tutorial series that dissects the internals of coding agents layer by layer while building a runnable mini-agent, using three open-source coding agent projects as references. [@claim:clm_64928a2bb42f68b8759f757088018a623622d77883003b4f345b7a2aaab973d4]
- The mini-agent likely exposes a terminal/TUI interface, since a TUI is listed among the capabilities progressively added in later steps. [@claim:clm_82d2db532e160c6d10531ca68f5ac597cda6c776478eb6426caa8f2ebc2f3da0]
- The series uses domestic Chinese model APIs (DeepSeek, GLM, Kimi), and the code is stated to run directly locally. [@claim:clm_9b381d0a85d3702e1ef45d0da39de55edc64335af7d8b33f7c4d4e436f122294]
- Each article maps to an independently runnable stage under steps/, starting from a ~100-line minimal loop and progressively adding tool execution, context management, and a TUI. [@claim:clm_b6fe8d95a9225345d04da83f13c9dfe92ed6bef7abb28678c2cbf0681013678b]
- Six published articles cover the agent loop, unified LLM API and error contracts, tool calling, context compaction and session persistence, and permission/security philosophy, each linked to notes and runnable code. [@claim:clm_bd0249cf9595c292e704a3b2f10b7b0adfb47460bd4e3724a046a87ebc39c83d]
- A step can be run by exporting DEEPSEEK_API_KEY and executing 'cd steps/01-minimal-loop && npm install && npm start'. [@claim:clm_fbfbc55506c3fcfbd5e825f61177e82e5fd819f48623321b8855bb0d9ee6c595]
<!-- rcw:end owner=source:src_1d11d5883c665d4cbcd02544bbe24b18 block=evidence -->

## Researcher notes

