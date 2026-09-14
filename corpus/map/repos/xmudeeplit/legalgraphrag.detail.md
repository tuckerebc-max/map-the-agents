# xmudeeplit/legalgraphrag -- full detail

[Back to orientation](legalgraphrag.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/xmudeeplit/legalgraphrag/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/5a8097f9031a88cf.json](../../../wiki/dossiers/xmudeeplit/legalgraphrag/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/5a8097f9031a88cf.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The core package contains a main LegalGraphRAG class plus modules for models (transformers and OpenAI-compatible), graph construction, legal judgment, preprocessing, prompts, and utilities. -- evidence: [README.md#L31-L52](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L31-L52) (`clm_8bc3bd61011719de6c1bb3967f9167fa420f29a6798ee049fc4b43cfaa10db7d`)

## design-choices (2 claim(s))

- [observation/documented] The default embedding endpoint is http://localhost:11434/api/embed with model bge-m3; both are configurable in configs/main.env and used by graph construction and retrieval. -- evidence: [README.md#L93-L93](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L93-L93) (`clm_2638e2eca2b71744afad6bfde96cadb892cca5a2a8d10ed60f8f2efc92f90acf`)
- [observation/documented] The main retrieval corpus combines 3,512 CAIL test, 5,752 JuDGE, and 4,785 CMDL cases with sequential IDs, and a small amount of LeCaRDv2 data was incorporated as untagged supplementary material. -- evidence: [docs/TABLE2_REPRODUCTION.md#L26-L30](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/docs/TABLE2_REPRODUCTION.md#L26-L30), [docs/TABLE2_REPRODUCTION.md#L36-L39](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/docs/TABLE2_REPRODUCTION.md#L36-L39) (`clm_ef0faa80a8e793e4a990e7f2c0b49b8d50b6bcaebb6586f9942ad35cc03f4318`)

## workflows (1 claim(s))

- [observation/documented] Repository setup workflow: install requirements via pip, copy env.example to .env, and verify bundled experiment assets with sha256sum -c SHA256SUMS. -- evidence: [README.md#L79-L82](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L79-L82), [README.md#L154-L154](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L154-L154) (`clm_b09d479d537bb5ec2c7ed371f02004229ac8a3363025de02f6e0de003fee8551`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] run.py exposes CLI arguments including --model, --datasets, --dotenv_path, --datasets_path, --devices, --no-build-graph, and --force-rebuild. -- evidence: [README.md#L200-L206](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L200-L206) (`clm_c2ce61504f925f38815abacc83f66e0662c1f2d7a9bed036dee9f36201257a56`)
- [observation/documented] Supported model choices include qwen3, qwen2_5, gemma3, internlm3, glm4, deepseek_v3, and gpt4o_mini; prompt_language=zh or en in .env selects Chinese or English prompts. -- evidence: [README.md#L200-L206](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L200-L206), [README.md#L208-L209](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L208-L209) (`clm_7dfabf1b7d113fd9093664ff4388bb23dc5d965c4fc71bca532a14965288d19c`)

## memory-state (1 claim(s))

- [observation/documented] The constructed graph is persisted to a pickle file (e.g. outputs/main_experiment/qwen3_graph_db.pkl); later runs can skip construction, and changing the construction model requires --force-rebuild or a different graph_db_path. -- evidence: [README.md#L117-L117](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L117-L117), [README.md#L106-L106](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L106-L106) (`clm_3deeee6918b08e5091745913ea9dc4decb462e0fe2c434e7a90f2365a2c71cb9`)

## orchestration (1 claim(s))

- [observation/documented] Multi-GPU execution is supported by passing several devices to run.py, and cases are automatically distributed across the selected devices. -- evidence: [README.md#L262-L264](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L262-L264), [README.md#L266-L266](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L266-L266) (`clm_aa0533e83e020de0ba11accedef3a51076cfd804d35119d3f7bbf0cc57a95031`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (4 claim(s))

- [observation/documented] The framework computes legal judgment prediction metrics: charge and law-article exact-match accuracy and Micro-F1, plus imprisonment term exact match and mean absolute error in months. -- evidence: [README.md#L18-L21](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L18-L21), [README.md#L139-L141](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L139-L141) (`clm_43bbceab113b58c7ba6290df541a0bda88203cb3cf67f3f03f3f628e5980aba8`)
- [observation/documented] Evaluation aggregation follows the paper's scripts: charge and law predictions are scored per entry in judge_res, while imprisonment uses the first judgment for each of the 568 CAIL cases. -- evidence: [README.md#L143-L143](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L143-L143) (`clm_8f8e243c7894aaae7c07105812ae913a893272e617db9e7e8da5ae678ff61d00`)
- [observation/documented] The evaluator accepts current judge_result.charge_name predictions and the legacy Table 2 judge_res[].crime format; each CMDL defendant row is scored once, giving judgment_count 1,374. -- evidence: [docs/TABLE2_REPRODUCTION.md#L116-L119](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/docs/TABLE2_REPRODUCTION.md#L116-L119) (`clm_ea9c87f62f69143d57dcc344525ea199b1ccebc69180d9a16862e411c4a17fbf`)
- [observation/documented] As a regression check, evaluating the archived Table 2 Qwen3 CMDL output yields Accuracy 0.5756914119359534 and Micro-F1 0.617426820966644. -- evidence: [docs/TABLE2_REPRODUCTION.md#L121-L122](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/docs/TABLE2_REPRODUCTION.md#L121-L122) (`clm_cff985d61b758b2344aa0323b0cb397543f9d8073f2d81a081e6098355905b0f`)

## dependencies (1 claim(s))

- [observation/documented] Declared dependencies include torch>=2.6.0, transformers>=4.51.0, accelerate, numpy, scipy, networkx, tqdm, requests, python-dotenv, and openai>=1.0.0 for the DeepSeek/GPT-4o-mini API client. -- evidence: [requirements.txt#L13-L13](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/requirements.txt#L13-L13), [requirements.txt#L2-L10](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/requirements.txt#L2-L10) (`clm_7bcf281d59c4c4eb0f8b23ad8d84584d263161c473053741723deda57ca97bd0`)

## limitations (1 claim(s))

- [observation/documented] Baseline systems such as HippoRAG2, RAPTOR, LightRAG, LegalDelta, and ADAPT are not included in the repository; their outputs can be compared externally if converted to the same result schema. -- evidence: [docs/TABLE2_REPRODUCTION.md#L3-L5](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/docs/TABLE2_REPRODUCTION.md#L3-L5), [README.md#L145-L145](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L145-L145) (`clm_76fa19e420250ca5f943589b6273de2b3d3684a1b472083a6f3b004453f33ef5`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

