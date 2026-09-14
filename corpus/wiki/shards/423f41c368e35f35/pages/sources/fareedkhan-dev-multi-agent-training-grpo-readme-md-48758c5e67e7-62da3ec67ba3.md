---
access: public
aliases: []
claim_ids:
- clm_182f5fc591e4930b27cf89ccbec5306b9840efb047fad94277b50d3b8c5e2783
- clm_231a11370b0adf1e6857ec602bbde8981e9e8dee3277ce5c2f4030de8fdc8087
- clm_33cada1c29493fad7230c47babb74cae8304e4eca6f32aeb924e7aa96dd8689f
- clm_5938e0db067c81f5ec34e7348f766562e74ed3bb7b797d07621932dce84ce234
- clm_77cbfdd8444aaae10e28ccbe4c26d4f8c3fe0a796a2222b134d51a62542f3217
- clm_96ac528a0049f79ba9a5e4924781610eebc1281270d5e65748f34db8311214e8
- clm_a953c625edfae43d7cb6eba41ce23fe4a21f064d1e1f1d78732f1e3b6207681e
- clm_b5eba3c7d7a5c68fa847906a45f9a3d7997aec9eb7e141dbda9e2d75f66a30c2
- clm_bb336a938368bd6895b58328cb2c807cb3ad8be0d1ee054491cce29e60003d29
- clm_c1d69b4aeb6255b6a3938d4b0b715b2976b27bd9457e20568380145543e195d1
- clm_d1049be2257ea23bb11dc3158ad09cbc4b965d31d0844be22d7e25f4950d7b9d
maturity: draft
page_id: pg_ff04f60fb0085988911f62da3ec67ba3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4bfa8cc503ac5736bf465d93c8d86ac8
title: FareedKhan-dev/multi-agent-training-grpo/README.md @ 48758c5e67e7
updated_at: '2026-09-14T03:50:29Z'
---

# FareedKhan-dev/multi-agent-training-grpo/README.md @ 48758c5e67e7

<!-- rcw:begin owner=source:src_4bfa8cc503ac5736bf465d93c8d86ac8 block=evidence -->
- The planning model is served through a vLLM server with an OpenAI-compatible API; the example serves Qwen/Qwen2.5-7B-Instruct on port 8000 with an API key and 8192 max context length. [@claim:clm_182f5fc591e4930b27cf89ccbec5306b9840efb047fad94277b50d3b8c5e2783]
- Tool API keys are configured as placeholders: an OpenAI key is noted as needed for embeddings in the web search tool and a Google key for the Google search tool. [@claim:clm_231a11370b0adf1e6857ec602bbde8981e9e8dee3277ce5c2f4030de8fdc8087]
- The multi-agent architecture comprises stages including planning, tool use, execution, observation and reflection, iteration until a verifier agent determines the query is answered, and final synthesis. [@claim:clm_33cada1c29493fad7230c47babb74cae8304e4eca6f32aeb924e7aa96dd8689f]
- During GRPO training, an external judge scores each trajectory's final answer against ground truth with binary rewards (1.0 correct, 0.0 failed or hallucinated), and relative advantages are computed against the group mean. [@claim:clm_5938e0db067c81f5ec34e7348f766562e74ed3bb7b797d07621932dce84ce234]
- The project trains a multi-agent system with the GRPO reinforcement learning algorithm to improve planning and reduce hallucination and off-track results in long-horizon agentic tasks. [@claim:clm_77cbfdd8444aaae10e28ccbe4c26d4f8c3fe0a796a2222b134d51a62542f3217]
- The tutorial targets the planning phase for fine-tuning because it monitors the whole workflow across iterations, and uses an open-source vLLM-based server chosen for throughput and latency; the author used a single A100 80GB GPU. [@claim:clm_96ac528a0049f79ba9a5e4924781610eebc1281270d5e65748f34db8311214e8]
- Python dependencies include openai, pydantic, tenacity, beautifulsoup4, requests, wikipedia, google-genai, numpy, and json_repair, plus pandas and the Hugging Face datasets library for preprocessing. [@claim:clm_a953c625edfae43d7cb6eba41ce23fe4a21f064d1e1f1d78732f1e3b6207681e]
- An abstract EngineLM base class requires a generate method, with ChatVLLM as the concrete implementation that formats chat messages, retries failed calls, and can enforce structured JSON output by appending a Pydantic schema to the prompt. [@claim:clm_b5eba3c7d7a5c68fa847906a45f9a3d7997aec9eb7e141dbda9e2d75f66a30c2]
- GRPO is described as group-based: the agent attempts the same query multiple times, and strategies are reinforced relative to the group average rather than graded in isolation. [@claim:clm_bb336a938368bd6895b58328cb2c807cb3ad8be0d1ee054491cce29e60003d29]
- The preprocessing pipeline normalizes both datasets to a shared schema (id, question, chain, result, source, extra_info), concatenates them, shuffles with seed 42, re-indexes, and saves as Parquet; the combined training set totals 182,190 samples. [@claim:clm_c1d69b4aeb6255b6a3938d4b0b715b2976b27bd9457e20568380145543e195d1]
- The repository is a blog-style walkthrough by Fareed Khan explaining GRPO's role in agent systems and demonstrating building and training a multi-agentic system end to end, including a table of contents covering preprocessing through the optimized planning agent. [@claim:clm_d1049be2257ea23bb11dc3158ad09cbc4b965d31d0844be22d7e25f4950d7b9d]
<!-- rcw:end owner=source:src_4bfa8cc503ac5736bf465d93c8d86ac8 block=evidence -->

## Researcher notes

