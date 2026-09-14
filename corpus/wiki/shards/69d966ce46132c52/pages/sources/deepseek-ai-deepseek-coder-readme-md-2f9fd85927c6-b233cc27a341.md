---
access: public
aliases: []
claim_ids:
- clm_041b5795a50b02d94e40cd0beb2c99f2a3a372ab9a83afa34e6da9409ff2eb23
- clm_15617a6394ec7fc373f5a4d86cf29bfb533d58964384f80a13323d5b2447f4a7
- clm_2139a0e0303628af308709529a2fa96b713f0cdc278765da79fe5c538bd47281
- clm_2af58c2f12c526016fbcbed9c26511608dda3a30648957e92fcf60bb6df7db31
- clm_70b9f42d2dea1889ad0566d14843c46f997ddd649a478c22d62212855950da86
- clm_790e1e8f928f3e77a6e70781d9c16e574b240ee70cdb0b68036f33daffed2e32
- clm_795d03b603224b187fb107323aeeb804ad453038eb67c16e21c28e318c42d08d
- clm_7a0f169414c28f5dbe08dfaba4c8a5d726d5b448e687d4565d2b88141035ec14
- clm_7fc5dda84dc1d28d709a88478466850d7691a3df2df031f38093f16b97623e39
- clm_87aab6bb4f1507975911116c1807ff65f1f1793c2840faa8e7ae592315042be3
- clm_8d72249d24057527b23ad5226e9715116c32652c069195252107411691af39a7
- clm_947963ca918fcb1740c9f7bd7f862a0b4149040a4ab002ecdfa134602aea3cbd
- clm_ba39d0160645c16e15a73c0356450cadd253d1f95b1f624ba6d5bb74fff27b3e
- clm_c8a392f2518a8150cca38f0a238300fbd9c2108347959668df2ed8a4b052c287
- clm_cee11e51868fdecffda485e54ddb81f3f0e6397a483e00d7be81e88297d75e6e
- clm_d256bbcd45c5276722e6c19e8f81d45a57d5b39403f52d317640544ab4104b9c
- clm_de25cc0aaf9c3715da271363cd704b72ff140e870f28445cdad62a3a416a5b87
- clm_f7f6ed15aef6e4e56fd001d6ce79a912ff57fbbaf4734f2d718e9c1a2b22b5fc
maturity: draft
page_id: pg_f5e222427320547a9254b233cc27a341
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cc5563571ec15770b20d47349e375aff
title: deepseek-ai/DeepSeek-Coder/README.md @ 2f9fd85927c6
updated_at: '2026-09-14T03:45:33Z'
---

# deepseek-ai/DeepSeek-Coder/README.md @ 2f9fd85927c6

<!-- rcw:begin owner=source:src_cc5563571ec15770b20d47349e375aff block=evidence -->
- The code repository is MIT licensed; model use is subject to a separate Model License, and DeepSeek Coder supports commercial use. [@claim:clm_041b5795a50b02d94e40cd0beb2c99f2a3a372ab9a83afa34e6da9409ff2eb23]
- Training data was built by collecting GitHub code with StarCoder-style filtering, reordering files by intra-repo dependencies, repo-level minhash deduplication, and filtering low-quality code. [@claim:clm_15617a6394ec7fc373f5a4d86cf29bfb533d58964384f80a13323d5b2447f4a7]
- DeepSeek Coder is a series of code language models trained from scratch on 2T tokens (87% code, 13% natural language in English and Chinese), offered in sizes from 1B to 33B. [@claim:clm_2139a0e0303628af308709529a2fa96b713f0cdc278765da79fe5c538bd47281]
- Pretraining uses a 16K window size plus an extra fill-in-the-blank task to support project-level code completion and infilling. [@claim:clm_2af58c2f12c526016fbcbed9c26511608dda3a30648957e92fcf60bb6df7db31]
- The tokenizer is a HuggingFace Bytelevel-BPE with specially designed pre-tokenizers; the README states there is no direct way to convert it to SentencePiece. [@claim:clm_70b9f42d2dea1889ad0566d14843c46f997ddd649a478c22d62212855950da86]
- A finetune/finetune_deepseekcoder.py script supports DeepSpeed training; training data must be JSON lines with 'instruction' and 'output' fields, with DATA_PATH and OUTPUT_PATH specified. [@claim:clm_790e1e8f928f3e77a6e70781d9c16e574b240ee70cdb0b68036f33daffed2e32]
- Reported: DeepSeek-Coder-Base-33B leads CodeLlama-34B by 7.9% (HumanEval Python), 9.3% (HumanEval Multilingual), 10.8% (MBPP), and 5.9% (DS-1000); Instruct-33B outperforms GPT35-turbo on HumanEval. [@claim:clm_795d03b603224b187fb107323aeeb804ad453038eb67c16e21c28e318c42d08d]
- A PR was submitted to llama.cpp to support the model's HuggingFace pre-tokenizers for GGUF conversion; until merged, a forked branch with convert-hf-to-gguf.py is documented. [@claim:clm_7a0f169414c28f5dbe08dfaba4c8a5d726d5b448e687d4565d2b88141035ec14]
- Models are loaded via HuggingFace transformers AutoTokenizer/AutoModelForCausalLM with trust_remote_code=True and torch_dtype=torch.bfloat16 on CUDA. [@claim:clm_7fc5dda84dc1d28d709a88478466850d7691a3df2df031f38093f16b97623e39]
- Code insertion is performed by placing FIM special tokens (<|fim▁begin|>, <|fim▁hole|>, <|fim▁end|>) in the input text. [@claim:clm_87aab6bb4f1507975911116c1807ff65f1f1793c2840faa8e7ae592315042be3]
- For code completion with instruct models, users should set eos_token_id to 32014 instead of the default 32021 so the model recognizes sequence ends differently. [@claim:clm_8d72249d24057527b23ad5226e9715116c32652c069195252107411691af39a7]
- Instruct models are prompted with tokenizer.apply_chat_template using role/content messages, and generation stops at the tokenizer's eos_token_id. [@claim:clm_947963ca918fcb1740c9f7bd7f862a0b4149040a4ab002ecdfa134602aea3cbd]
- Released model sizes are listed as 1B, 5.7B, 6.7B, and 33B, so users can pick the setup fitting their requirements. [@claim:clm_ba39d0160645c16e15a73c0356450cadd253d1f95b1f624ba6d5bb74fff27b3e]
- The README reports pass@1 results on HumanEval (Python and Multilingual), MBPP, and DS-1000, and claims state-of-the-art performance among open-source code models on several benchmarks. [@claim:clm_c8a392f2518a8150cca38f0a238300fbd9c2108347959668df2ed8a4b052c287]
- The instruct chat template instructs the model to answer only computer-science questions and to refuse politically sensitive, security, privacy, and other non-CS questions. [@claim:clm_cee11e51868fdecffda485e54ddb81f3f0e6397a483e00d7be81e88297d75e6e]
- Training proceeded in stages: 1.8T tokens at 4K window, then 200B more tokens at 16K window yielding Base models, then 2B tokens of instruction fine-tuning yielding Instruct models. [@claim:clm_d256bbcd45c5276722e6c19e8f81d45a57d5b39403f52d317640544ab4104b9c]
- vLLM is supported for high-throughput inference with tensor parallelism, for both text completion and chat completion using the tokenizer's eos token as a stop string. [@claim:clm_de25cc0aaf9c3715da271363cd704b72ff140e870f28445cdad62a3a416a5b87]
- exllamav2 has added support for the HuggingFace tokenizer; users are told to pull the latest version and set RoPE scaling to 4 for correct output. [@claim:clm_f7f6ed15aef6e4e56fd001d6ce79a912ff57fbbaf4734f2d718e9c1a2b22b5fc]
<!-- rcw:end owner=source:src_cc5563571ec15770b20d47349e375aff block=evidence -->

## Researcher notes

