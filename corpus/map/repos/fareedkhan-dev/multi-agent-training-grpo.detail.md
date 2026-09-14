# fareedkhan-dev/multi-agent-training-grpo -- full detail

[Back to orientation](multi-agent-training-grpo.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/fareedkhan-dev/multi-agent-training-grpo/48758c5e67e762494e23070de2e27e9bb9bc9a54/57f32112a4bb2240.json](../../../wiki/dossiers/fareedkhan-dev/multi-agent-training-grpo/48758c5e67e762494e23070de2e27e9bb9bc9a54/57f32112a4bb2240.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The preprocessing pipeline normalizes both datasets to a shared schema (id, question, chain, result, source, extra_info), concatenates them, shuffles with seed 42, re-indexes, and saves as Parquet; the combined training set totals 182,190 samples. -- evidence: [README.md#L438-L442](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L438-L442), [README.md#L432-L432](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L432-L432), [README.md#L182-L187](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L182-L187), [README.md#L218-L229](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L218-L229), [README.md#L364-L376](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L364-L376), [README.md#L466-L466](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L466-L466), [README.md#L416-L417](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L416-L417), [README.md#L451-L452](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L451-L452) (`clm_c1d69b4aeb6255b6a3938d4b0b715b2976b27bd9457e20568380145543e195d1`)
- [observation/documented] The multi-agent architecture comprises stages including planning, tool use, execution, observation and reflection, iteration until a verifier agent determines the query is answered, and final synthesis. -- evidence: [README.md#L477-L482](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L477-L482) (`clm_33cada1c29493fad7230c47babb74cae8304e4eca6f32aeb924e7aa96dd8689f`)
- [observation/documented] An abstract EngineLM base class requires a generate method, with ChatVLLM as the concrete implementation that formats chat messages, retries failed calls, and can enforce structured JSON output by appending a Pydantic schema to the prompt. -- evidence: [README.md#L622-L629](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L622-L629), [README.md#L568-L570](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L568-L570), [README.md#L566-L566](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L566-L566), [README.md#L582-L582](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L582-L582), [README.md#L584-L586](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L584-L586), [README.md#L576-L580](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L576-L580), [README.md#L600-L602](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L600-L602) (`clm_b5eba3c7d7a5c68fa847906a45f9a3d7997aec9eb7e141dbda9e2d75f66a30c2`)

## design-choices (3 claim(s))

- [observation/documented] The project trains a multi-agent system with the GRPO reinforcement learning algorithm to improve planning and reduce hallucination and off-track results in long-horizon agentic tasks. -- evidence: [README.md#L5-L5](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L5-L5), [README.md#L62-L62](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L62-L62), [README.md#L20-L20](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L20-L20) (`clm_77cbfdd8444aaae10e28ccbe4c26d4f8c3fe0a796a2222b134d51a62542f3217`)
- [observation/documented] GRPO is described as group-based: the agent attempts the same query multiple times, and strategies are reinforced relative to the group average rather than graded in isolation. -- evidence: [README.md#L52-L52](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L52-L52), [README.md#L12-L16](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L12-L16), [README.md#L56-L60](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L56-L60) (`clm_bb336a938368bd6895b58328cb2c807cb3ad8be0d1ee054491cce29e60003d29`)
- [observation/documented] The tutorial targets the planning phase for fine-tuning because it monitors the whole workflow across iterations, and uses an open-source vLLM-based server chosen for throughput and latency; the author used a single A100 80GB GPU. -- evidence: [README.md#L486-L486](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L486-L486), [README.md#L484-L484](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L484-L484) (`clm_96ac528a0049f79ba9a5e4924781610eebc1281270d5e65748f34db8311214e8`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The planning model is served through a vLLM server with an OpenAI-compatible API; the example serves Qwen/Qwen2.5-7B-Instruct on port 8000 with an API key and 8192 max context length. -- evidence: [README.md#L541-L541](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L541-L541), [README.md#L538-L538](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L538-L538), [README.md#L493-L497](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L493-L497), [README.md#L544-L544](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L544-L544) (`clm_182f5fc591e4930b27cf89ccbec5306b9840efb047fad94277b50d3b8c5e2783`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Tool API keys are configured as placeholders: an OpenAI key is noted as needed for embeddings in the web search tool and a Google key for the Google search tool. -- evidence: [README.md#L549-L551](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L549-L551) (`clm_231a11370b0adf1e6857ec602bbde8981e9e8dee3277ce5c2f4030de8fdc8087`)

## evaluation (1 claim(s))

- [observation/documented] During GRPO training, an external judge scores each trajectory's final answer against ground truth with binary rewards (1.0 correct, 0.0 failed or hallucinated), and relative advantages are computed against the group mean. -- evidence: [README.md#L56-L60](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L56-L60) (`clm_5938e0db067c81f5ec34e7348f766562e74ed3bb7b797d07621932dce84ce234`)

## dependencies (1 claim(s))

- [observation/documented] Python dependencies include openai, pydantic, tenacity, beautifulsoup4, requests, wikipedia, google-genai, numpy, and json_repair, plus pandas and the Hugging Face datasets library for preprocessing. -- evidence: [README.md#L501-L503](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L501-L503), [README.md#L521-L531](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L521-L531), [README.md#L94-L94](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L94-L94), [README.md#L90-L91](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L90-L91) (`clm_a953c625edfae43d7cb6eba41ce23fe4a21f064d1e1f1d78732f1e3b6207681e`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The repository is a blog-style walkthrough by Fareed Khan explaining GRPO's role in agent systems and demonstrating building and training a multi-agentic system end to end, including a table of contents covering preprocessing through the optimized planning agent. -- evidence: [README.md#L20-L20](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L20-L20), [README.md#L3-L3](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L3-L3), [README.md#L24-L39](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L24-L39), [README.md#L18-L18](https://github.com/FareedKhan-dev/multi-agent-training-grpo/blob/48758c5e67e762494e23070de2e27e9bb9bc9a54/README.md#L18-L18) (`clm_d1049be2257ea23bb11dc3158ad09cbc4b965d31d0844be22d7e25f4950d7b9d`)

