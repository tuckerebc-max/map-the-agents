# structuredllm/syncode -- full detail

[Back to orientation](syncode.md)

## Origins

- github-verified-rename
- alltheagents.org-backing

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/structuredllm/syncode/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/4cf25e2790b4916d.json](../../../wiki/dossiers/structuredllm/syncode/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/4cf25e2790b4916d.json)

## specifications (1 claim(s))

- [observation/documented] SynCode is a framework for grammar-guided LLM generation, claimed to ensure output is syntactically valid with respect to a context-free grammar, with stated soundness and completeness guarantees. -- evidence: [README.md#L24-L26](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L24-L26) (`clm_876f6ec8eb1b8825800b2a54c0c3558e4751b542610d2d576e2ae2911333053e`)

## components (1 claim(s))

- [observation/documented] Built-in CFGs are provided for Python, Go, Java, SQL, Math, JSON, and more, stored in the syncode/parsers/grammars directory. -- evidence: [README.md#L33-L33](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L33-L33), [README.md#L42-L48](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L42-L48) (`clm_83e985f8ba03db2e0b755776a77b601755f2e552da2ea0ead4c2bea53e1abdb3`)

## design-choices (2 claim(s))

- [observation/documented] SynCode's core is an offline-constructed DFA mask store built from regular expressions of grammar terminals, used with an incremental parser's accept sequences and remainder to mask invalid tokens during decoding. -- evidence: [README.md#L418-L418](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L418-L418) (`clm_4235412de0fcc3d0338775683b7c24c0d119277c825e75a27c2e67e8450a4188`)
- [observation/documented] Custom grammars can be supplied in an EBNF syntax adapted from Lark, either as a string of rules or a path to a .lark file. -- evidence: [README.md#L345-L345](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L345-L345), [README.md#L246-L246](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L246-L246) (`clm_15354823a1303363e7f148202928cfdd1500577b777776b64d8f7a53232e1f73`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] SynCode can be used as a HuggingFace logit processor: SyncodeLogitsProcessor is imported and passed to model.generate via the logits_processor argument. -- evidence: [README.md#L77-L77](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L77-L77), [README.md#L79-L91](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L79-L91) (`clm_0771e541ab4e11581a588abc0bec4ede583dbaa90ccbf823b2d27ac1049703c0`)
- [observation/documented] A SynCode class offers an infer() method taking prompt and task_id; if neither is given, it reads user input via stdin. -- evidence: [README.md#L105-L105](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L105-L105), [README.md#L95-L101](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L95-L101), [README.md#L103-L103](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L103-L103) (`clm_800bec99e0af6416a75c6ca5c5e8b146f55a1a28ecc6be5906e1e0b8bf07154c`)
- [observation/documented] The SynCode class accepts options including mode (grammar_mask, grammar_strict, original; default grammar_strict), grammar, parser (LR(1) or LALR(1), default lalr), quantize, device, num_samples, dev_mode, and log_level. -- evidence: [README.md#L184-L184](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L184-L184), [README.md#L206-L206](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L206-L206), [README.md#L202-L202](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L202-L202), [README.md#L194-L194](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L194-L194), [README.md#L192-L192](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L192-L192), [README.md#L200-L200](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L200-L200), [README.md#L190-L190](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L190-L190), [README.md#L188-L188](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L188-L188) (`clm_e79bb1ffe5cd4313ede82da11096a15dd6a0333a6ebd0b94710f9f97a07c9360`)
- [observation/documented] A CLI is available via python3 syncode/infer.py with flags for mode, model, device, dataset (mbxp, humaneval, mathqa-x, input), few-shot options, parser, and task_id. -- evidence: [README.md#L225-L243](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L225-L243) (`clm_f1531859ef4a36f10bb31d45ee0edcfb4e4ec075ea8188bf35b1b5247158a8ac`)

## memory-state (1 claim(s))

- [observation/documented] Cache directories can be configured via HF_CACHE and SYNCODE_CACHE environment variables, with defaults used otherwise; HF_ACCESS_TOKEN enables gated HuggingFace models. -- evidence: [README.md#L169-L178](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L169-L178) (`clm_95c1ba11db34834a25e728ef0c13c8778141076d503e0aeaf3b0e5067938acc9`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README reports SynCode achieving 99% JSON generation accuracy with Gemma-2b and being 10-20% faster than unconstrained generation, referencing an evaluation notebook. -- evidence: [README.md#L24-L26](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L24-L26) (`clm_bf8c6014d2368426b99eebc8f6abf98be82b00ec1d7415bbf57e28e01e88f9ed`)

## dependencies (2 claim(s))

- [observation/documented] SynCode v0.4.16 requires transformers v4.53.2 and Python 3.6-3.12; Python 3.13 is not supported due to dependency constraints. -- evidence: [README.md#L74-L74](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L74-L74), [README.md#L70-L72](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/README.md#L70-L72) (`clm_3ec5f6cac2574c294291dff5503ee33510bc9a29ffbbb765a2943539635eac3a`)
- [observation/documented] requirements.txt lists dependencies including transformers==4.53.2 (for Python < 3.13), torch, accelerate, interegular, regex, datasets, jsonschema, fire, and tqdm. -- evidence: [requirements.txt#L1-L9](https://github.com/structuredllm/syncode/blob/4d6c110a028d3fb9cbb5f1a6ac6446b696f3eac4/requirements.txt#L1-L9) (`clm_00b37219d9b4a36fd21f31028730e0607bb37fc83f9689c9d2b721d90000cd5c`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

