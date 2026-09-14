# xmudeeplit/legalgraphrag

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a3c9c3070cad @ 5a8097f9031a88cf

## Summary (orientation draft, not independently verified)

Selected evidence records: The framework computes legal judgment prediction metrics: charge and law-article exact-match accuracy and Micro-F1, plus imprisonment term exact match and mean absolute error in months. Evaluation aggregation follows the paper's scripts: charge and law predictions are scored per entry in judge_res, while imprisonment uses the first judgment for each of the 568 CAIL cases.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The core package contains a main LegalGraphRAG class plus modules for models (transformers and OpenAI-compatible), graph construction, legal judgment, preprocessing, prompts, and utilities. -- evidence: [README.md#L31-L52](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L31-L52)
- design-choices (2 claim(s)):
  - [observation/documented] The default embedding endpoint is http://localhost:11434/api/embed with model bge-m3; both are configurable in configs/main.env and used by graph construction and retrieval. -- evidence: [README.md#L93-L93](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L93-L93)
  - [observation/documented] The main retrieval corpus combines 3,512 CAIL test, 5,752 JuDGE, and 4,785 CMDL cases with sequential IDs, and a small amount of LeCaRDv2 data was incorporated as untagged supplementary material. -- evidence: [docs/TABLE2_REPRODUCTION.md#L26-L30](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/docs/TABLE2_REPRODUCTION.md#L26-L30), [docs/TABLE2_REPRODUCTION.md#L36-L39](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/docs/TABLE2_REPRODUCTION.md#L36-L39)
- workflows (1 claim(s)):
  - [observation/documented] Repository setup workflow: install requirements via pip, copy env.example to .env, and verify bundled experiment assets with sha256sum -c SHA256SUMS. -- evidence: [README.md#L79-L82](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L79-L82), [README.md#L154-L154](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L154-L154)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] run.py exposes CLI arguments including --model, --datasets, --dotenv_path, --datasets_path, --devices, --no-build-graph, and --force-rebuild. -- evidence: [README.md#L200-L206](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L200-L206)
  - [observation/documented] Supported model choices include qwen3, qwen2_5, gemma3, internlm3, glm4, deepseek_v3, and gpt4o_mini; prompt_language=zh or en in .env selects Chinese or English prompts. -- evidence: [README.md#L200-L206](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L200-L206), [README.md#L208-L209](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L208-L209)
- memory-state (1 claim(s)):
  - [observation/documented] The constructed graph is persisted to a pickle file (e.g. outputs/main_experiment/qwen3_graph_db.pkl); later runs can skip construction, and changing the construction model requires --force-rebuild or a different graph_db_path. -- evidence: [README.md#L117-L117](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L117-L117), [README.md#L106-L106](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L106-L106)
- orchestration (1 claim(s)):
  - [observation/documented] Multi-GPU execution is supported by passing several devices to run.py, and cases are automatically distributed across the selected devices. -- evidence: [README.md#L262-L264](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L262-L264), [README.md#L266-L266](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L266-L266)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (4 claim(s)):
  - [observation/documented] The framework computes legal judgment prediction metrics: charge and law-article exact-match accuracy and Micro-F1, plus imprisonment term exact match and mean absolute error in months. -- evidence: [README.md#L18-L21](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L18-L21), [README.md#L139-L141](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L139-L141)
  - [observation/documented] Evaluation aggregation follows the paper's scripts: charge and law predictions are scored per entry in judge_res, while imprisonment uses the first judgment for each of the 568 CAIL cases. -- evidence: [README.md#L143-L143](https://github.com/XMUDeepLIT/LegalGraphRAG/blob/a3c9c3070cadb72ec317d2ecc2cce99da4b37c57/README.md#L143-L143)
- dependencies (1 claim(s)):
More evidence: [full detail](legalgraphrag.detail.md)

Metadata and full claim list: [full detail](legalgraphrag.detail.md)
Human notes ([notes](legalgraphrag.notes.md), never overwritten by build)

[Back to map index](../../index.md)
