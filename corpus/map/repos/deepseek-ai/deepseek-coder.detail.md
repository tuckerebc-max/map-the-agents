# deepseek-ai/deepseek-coder -- full detail

[Back to orientation](deepseek-coder.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/deepseek-ai/deepseek-coder/2f9fd85927c669dae3c0fbb2d607274023af243e/aa5921a58e7ce67b.json](../../../wiki/dossiers/deepseek-ai/deepseek-coder/2f9fd85927c669dae3c0fbb2d607274023af243e/aa5921a58e7ce67b.json)

## specifications (2 claim(s))

- [observation/documented] DeepSeek Coder is a series of code language models trained from scratch on 2T tokens (87% code, 13% natural language in English and Chinese), offered in sizes from 1B to 33B. -- evidence: [README.md#L13-L13](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L13-L13) (`clm_2139a0e0303628af308709529a2fa96b713f0cdc278765da79fe5c538bd47281`)
- [observation/documented] Released model sizes are listed as 1B, 5.7B, 6.7B, and 33B, so users can pick the setup fitting their requirements. -- evidence: [README.md#L21-L21](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L21-L21) (`clm_ba39d0160645c16e15a73c0356450cadd253d1f95b1f624ba6d5bb74fff27b3e`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] Pretraining uses a 16K window size plus an extra fill-in-the-blank task to support project-level code completion and infilling. -- evidence: [README.md#L25-L25](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L25-L25), [README.md#L13-L13](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L13-L13) (`clm_2af58c2f12c526016fbcbed9c26511608dda3a30648957e92fcf60bb6df7db31`)
- [observation/documented] The tokenizer is a HuggingFace Bytelevel-BPE with specially designed pre-tokenizers; the README states there is no direct way to convert it to SentencePiece. -- evidence: [README.md#L388-L388](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L388-L388) (`clm_70b9f42d2dea1889ad0566d14843c46f997ddd649a478c22d62212855950da86`)
- [observation/documented] For code completion with instruct models, users should set eos_token_id to 32014 instead of the default 32021 so the model recognizes sequence ends differently. -- evidence: [README.md#L417-L417](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L417-L417) (`clm_8d72249d24057527b23ad5226e9715116c32652c069195252107411691af39a7`)

## workflows (3 claim(s))

- [observation/documented] A finetune/finetune_deepseekcoder.py script supports DeepSpeed training; training data must be JSON lines with 'instruction' and 'output' fields, with DATA_PATH and OUTPUT_PATH specified. -- evidence: [README.md#L283-L284](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L283-L284), [README.md#L275-L275](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L275-L275), [README.md#L286-L288](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L286-L288), [README.md#L277-L277](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L277-L277) (`clm_790e1e8f928f3e77a6e70781d9c16e574b240ee70cdb0b68036f33daffed2e32`)
- [observation/documented] Training data was built by collecting GitHub code with StarCoder-style filtering, reordering files by intra-repo dependencies, repo-level minhash deduplication, and filtering low-quality code. -- evidence: [README.md#L50-L53](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L50-L53) (`clm_15617a6394ec7fc373f5a4d86cf29bfb533d58964384f80a13323d5b2447f4a7`)
- [observation/documented] Training proceeded in stages: 1.8T tokens at 4K window, then 200B more tokens at 16K window yielding Base models, then 2B tokens of instruction fine-tuning yielding Instruct models. -- evidence: [README.md#L59-L61](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L59-L61) (`clm_d256bbcd45c5276722e6c19e8f81d45a57d5b39403f52d317640544ab4104b9c`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Models are loaded via HuggingFace transformers AutoTokenizer/AutoModelForCausalLM with trust_remote_code=True and torch_dtype=torch.bfloat16 on CUDA. -- evidence: [README.md#L76-L100](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L76-L100), [README.md#L130-L138](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L130-L138) (`clm_7fc5dda84dc1d28d709a88478466850d7691a3df2df031f38093f16b97623e39`)
- [observation/documented] Instruct models are prompted with tokenizer.apply_chat_template using role/content messages, and generation stops at the tokenizer's eos_token_id. -- evidence: [README.md#L140-L145](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L140-L145), [README.md#L130-L138](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L130-L138) (`clm_947963ca918fcb1740c9f7bd7f862a0b4149040a4ab002ecdfa134602aea3cbd`)
- [observation/documented] Code insertion is performed by placing FIM special tokens (<|fim▁begin|>, <|fim▁hole|>, <|fim▁end|>) in the input text. -- evidence: [README.md#L103-L127](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L103-L127) (`clm_87aab6bb4f1507975911116c1807ff65f1f1793c2840faa8e7ae592315042be3`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (2 claim(s))

- [observation/documented] The README reports pass@1 results on HumanEval (Python and Multilingual), MBPP, and DS-1000, and claims state-of-the-art performance among open-source code models on several benchmarks. -- evidence: [README.md#L31-L32](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L31-L32), [README.md#L23-L23](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L23-L23) (`clm_c8a392f2518a8150cca38f0a238300fbd9c2108347959668df2ed8a4b052c287`)
- [observation/documented] Reported: DeepSeek-Coder-Base-33B leads CodeLlama-34B by 7.9% (HumanEval Python), 9.3% (HumanEval Multilingual), 10.8% (MBPP), and 5.9% (DS-1000); Instruct-33B outperforms GPT35-turbo on HumanEval. -- evidence: [README.md#L39-L41](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L39-L41) (`clm_795d03b603224b187fb107323aeeb804ad453038eb67c16e21c28e318c42d08d`)

## dependencies (5 claim(s))

- [observation/documented] vLLM is supported for high-throughput inference with tensor parallelism, for both text completion and chat completion using the tokenizer's eos token as a stop string. -- evidence: [README.md#L377-L378](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L377-L378), [README.md#L335-L335](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L335-L335), [README.md#L364-L368](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L364-L368), [README.md#L342-L345](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L342-L345) (`clm_de25cc0aaf9c3715da271363cd704b72ff140e870f28445cdad62a3a416a5b87`)
- [observation/documented] A PR was submitted to llama.cpp to support the model's HuggingFace pre-tokenizers for GGUF conversion; until merged, a forked branch with convert-hf-to-gguf.py is documented. -- evidence: [README.md#L392-L392](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L392-L392), [README.md#L394-L394](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L394-L394), [README.md#L404-L404](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L404-L404) (`clm_7a0f169414c28f5dbe08dfaba4c8a5d726d5b448e687d4565d2b88141035ec14`)
- [observation/documented] exllamav2 has added support for the HuggingFace tokenizer; users are told to pull the latest version and set RoPE scaling to 4 for correct output. -- evidence: [README.md#L411-L411](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L411-L411), [README.md#L413-L413](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L413-L413) (`clm_f7f6ed15aef6e4e56fd001d6ce79a912ff57fbbaf4734f2d718e9c1a2b22b5fc`)
- [observation/documented] requirements.txt pins transformers==4.35.0, torch>=2.0, tokenizers>=0.14.0, plus accelerate, sympy==1.12, pebble, timeout-decorator, and attrdict. -- evidence: [requirements.txt#L1-L8](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/requirements.txt#L1-L8) (`clm_aae1898409e2dfa25b2f672fab517818b979f61214e332328fde561bd34eba04`)
- [observation/documented] The code repository is MIT licensed; model use is subject to a separate Model License, and DeepSeek Coder supports commercial use. -- evidence: [README.md#L426-L426](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L426-L426), [README.md#L424-L424](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L424-L424) (`clm_041b5795a50b02d94e40cd0beb2c99f2a3a372ab9a83afa34e6da9409ff2eb23`)

## limitations (1 claim(s))

- [observation/documented] The instruct chat template instructs the model to answer only computer-science questions and to refuse politically sensitive, security, privacy, and other non-CS questions. -- evidence: [README.md#L164-L166](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L164-L166) (`clm_cee11e51868fdecffda485e54ddb81f3f0e6397a483e00d7be81e88297d75e6e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

