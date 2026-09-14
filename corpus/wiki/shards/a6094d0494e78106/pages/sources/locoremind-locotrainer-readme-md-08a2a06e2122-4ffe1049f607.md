---
access: public
aliases: []
claim_ids:
- clm_0237cffb75ee9d567d6eee3d9c91565059affce0015b4512dedcd1da50762ce1
- clm_064e83b2c3099b75e6e1a1b6b4cc23fbb12d3a5712cee1df7f2f28ef11c5b4f5
- clm_1549f40f863df3c418096736d013847881514aa9f3275232203f733d5a11db98
- clm_1c72e224967adf210e6535bf25b4ab81ae999e25c1312950ea5c0fded0fb13e3
- clm_29e97af210a2b08be49d2611de49b8e80d76c6e0394ac529367b161a0e3dc611
- clm_4c0eab9e4411514de0aa070559bf1633e1e85a5052276c44090911b834993c63
- clm_9c9e5e939370a6dc95ea24e3970e714033227e2ded8cec266a5bd1cadc972f3a
- clm_c76f78899878b51e353ed46333fb4d9ce88da054d3012a6e9f5bf832b0f30415
- clm_dc61070f5634b4aca6218a4dbeee86bf4ffde5afd6ee5be49e69a5cb95bc034c
- clm_de976b8224b49454f4339ccc8c66cc82ecaaf00f78c0ae02ce4eb52035c0a556
- clm_f9cd9ae874ceed0b9498fe3d2c5dc700794bfc74ae53682c71207a6eee1dbd19
- clm_fd8af98bae195ea6abd56bedd8657e418a9accf3e38a5189dee77f5f64346f8e
maturity: draft
page_id: pg_e73a70364f9457529b624ffe1049f607
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0495ebe5297654968d49be4b71fd32a7
title: LocoreMind/LocoTrainer/README.md @ 08a2a06e2122
updated_at: '2026-09-14T02:13:32Z'
---

# LocoreMind/LocoTrainer/README.md @ 08a2a06e2122

<!-- rcw:begin owner=source:src_0495ebe5297654968d49be4b71fd32a7 block=evidence -->
- The CLI exposes `locotrainer run` with options -q (question), -c (codebase path), -o (output dir), -m (model), --max-turns (default 20), and --quiet. [@claim:clm_0237cffb75ee9d567d6eee3d9c91565059affce0015b4512dedcd1da50762ce1]
- The model was trained with full-parameter SFT on 361,830 samples (agent trajectories, MS-SWIFT knowledge, project paths) at 32,768 max sequence length on 8x H100 80GB for about 25 hours. [@claim:clm_064e83b2c3099b75e6e1a1b6b4cc23fbb12d3a5712cee1df7f2f28ef11c5b4f5]
- The framework simulates a Claude Code-style agent environment, matching what LocoTrainer-4B was trained on, and injects absolute paths into user content plus tolerant tool argument parsing for reliability. [@claim:clm_1549f40f863df3c418096736d013847881514aa9f3275232203f733d5a11db98]
- The framework comprises modules for prompts (SYSTEM_PROMPT, get_system_reminder), a ToolExecutor (Read/Grep/Glob/Write/Bash), an agent loop, config loading, ms-swift auto-clone logic, and a Click CLI. [@claim:clm_1c72e224967adf210e6535bf25b4ab81ae999e25c1312950ea5c0fded0fb13e3]
- The project is MIT-licensed and distributed on PyPI with model weights (full and GGUF) on Hugging Face, plus a Colab notebook. [@claim:clm_29e97af210a2b08be49d2611de49b8e80d76c6e0394ac529367b161a0e3dc611]
- Documented limitations: specialization to MS-SWIFT with untested performance elsewhere, 4B scale possibly limiting complex multi-hop reasoning, and framework-structure knowledge tied to the training-data snapshot that may drift. [@claim:clm_4c0eab9e4411514de0aa070559bf1633e1e85a5052276c44090911b834993c63]
- LocoTrainer-4B is described as a 4B-parameter MS-SWIFT domain expert agent distilled from Qwen3-Coder-Next, combining tool-calling with framework knowledge. [@claim:clm_9c9e5e939370a6dc95ea24e3970e714033227e2ded8cec266a5bd1cadc972f3a]
- The product requires an OpenAI-compatible API endpoint (e.g., DashScope, OpenRouter, or a local llama.cpp server) and auto-clones the ms-swift repository on first use when no codebase path is given. [@claim:clm_c76f78899878b51e353ed46333fb4d9ce88da054d3012a6e9f5bf832b0f30415]
- Configuration uses environment variables such as LOCOTRAINER_API_KEY, LOCOTRAINER_BASE_URL (default OpenAI endpoint), LOCOTRAINER_MODEL (default gpt-4o), LOCOTRAINER_MAX_TURNS, LOCOTRAINER_MAX_TOKENS, LOCOTRAINER_ENABLE_THINKING, LOCOTRAINER_CODEBASE, and LOCOTRAINER_OUTPUT_DIR. [@claim:clm_dc61070f5634b4aca6218a4dbeee86bf4ffde5afd6ee5be49e69a5cb95bc034c]
- Reported evaluation on MS-SWIFT analysis tasks across 3 iterations shows Read success rising from 0% (relative paths) to 100% (absolute paths), and Write success reaching 100% only with tolerant argument parsing, with the final test producing a 225-line report in 9 turns. [@claim:clm_de976b8224b49454f4339ccc8c66cc82ecaaf00f78c0ae02ce4eb52035c0a556]
- The agent loop sends tool calls (Read/Grep/Glob/Bash) against the real filesystem, feeds results back for the next turn, and writes a final markdown report plus a full trajectory JSON to the output directory. [@claim:clm_f9cd9ae874ceed0b9498fe3d2c5dc700794bfc74ae53682c71207a6eee1dbd19]
- The agent emits structured tool-call JSON for Read, Grep, Glob, Bash, and Write tools executed against the target codebase. [@claim:clm_fd8af98bae195ea6abd56bedd8657e418a9accf3e38a5189dee77f5f64346f8e]
<!-- rcw:end owner=source:src_0495ebe5297654968d49be4b71fd32a7 block=evidence -->

## Researcher notes

