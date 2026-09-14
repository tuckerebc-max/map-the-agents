# deepseek-ai/deepseek-coder

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 2f9fd85927c6 @ aa5921a58e7ce67b

## Summary (orientation draft, not independently verified)

README-documented code language model series (1B–33B) trained on 2T tokens with 16K-window fill-in-the-blank pretraining, HuggingFace/vLLM inference, a DeepSpeed finetuning script, and reported benchmark results; corrections fix the DS-1000 figure, the uncited <|EOT|> clause, and the overstated quantization claim.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 19 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

19 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] DeepSeek Coder is a series of code language models trained from scratch on 2T tokens (87% code, 13% natural language in English and Chinese), offered in sizes from 1B to 33B. -- evidence: [README.md#L13-L13](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L13-L13)
  - [observation/documented] Released model sizes are listed as 1B, 5.7B, 6.7B, and 33B, so users can pick the setup fitting their requirements. -- evidence: [README.md#L21-L21](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L21-L21)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] Pretraining uses a 16K window size plus an extra fill-in-the-blank task to support project-level code completion and infilling. -- evidence: [README.md#L25-L25](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L25-L25), [README.md#L13-L13](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L13-L13)
  - [observation/documented] The tokenizer is a HuggingFace Bytelevel-BPE with specially designed pre-tokenizers; the README states there is no direct way to convert it to SentencePiece. -- evidence: [README.md#L388-L388](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L388-L388)
- workflows (3 claim(s)):
  - [observation/documented] A finetune/finetune_deepseekcoder.py script supports DeepSpeed training; training data must be JSON lines with 'instruction' and 'output' fields, with DATA_PATH and OUTPUT_PATH specified. -- evidence: [README.md#L283-L284](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L283-L284), [README.md#L275-L275](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L275-L275), [README.md#L286-L288](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L286-L288), [README.md#L277-L277](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L277-L277)
  - [observation/documented] Training data was built by collecting GitHub code with StarCoder-style filtering, reordering files by intra-repo dependencies, repo-level minhash deduplication, and filtering low-quality code. -- evidence: [README.md#L50-L53](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L50-L53)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Models are loaded via HuggingFace transformers AutoTokenizer/AutoModelForCausalLM with trust_remote_code=True and torch_dtype=torch.bfloat16 on CUDA. -- evidence: [README.md#L76-L100](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L76-L100), [README.md#L130-L138](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L130-L138)
  - [observation/documented] Instruct models are prompted with tokenizer.apply_chat_template using role/content messages, and generation stops at the tokenizer's eos_token_id. -- evidence: [README.md#L140-L145](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L140-L145), [README.md#L130-L138](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L130-L138)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (2 claim(s)):
  - [observation/documented] The README reports pass@1 results on HumanEval (Python and Multilingual), MBPP, and DS-1000, and claims state-of-the-art performance among open-source code models on several benchmarks. -- evidence: [README.md#L31-L32](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L31-L32), [README.md#L23-L23](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L23-L23)
  - [observation/documented] Reported: DeepSeek-Coder-Base-33B leads CodeLlama-34B by 7.9% (HumanEval Python), 9.3% (HumanEval Multilingual), 10.8% (MBPP), and 5.9% (DS-1000); Instruct-33B outperforms GPT35-turbo on HumanEval. -- evidence: [README.md#L39-L41](https://github.com/deepseek-ai/DeepSeek-Coder/blob/2f9fd85927c669dae3c0fbb2d607274023af243e/README.md#L39-L41)
- dependencies (5 claim(s)):
More evidence: [full detail](deepseek-coder.detail.md)

Metadata and full claim list: [full detail](deepseek-coder.detail.md)
Human notes ([notes](deepseek-coder.notes.md), never overwritten by build)

[Back to map index](../../index.md)
