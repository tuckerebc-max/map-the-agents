---
access: public
aliases: []
claim_ids:
- clm_2638e2eca2b71744afad6bfde96cadb892cca5a2a8d10ed60f8f2efc92f90acf
- clm_3deeee6918b08e5091745913ea9dc4decb462e0fe2c434e7a90f2365a2c71cb9
- clm_43bbceab113b58c7ba6290df541a0bda88203cb3cf67f3f03f3f628e5980aba8
- clm_76fa19e420250ca5f943589b6273de2b3d3684a1b472083a6f3b004453f33ef5
- clm_7dfabf1b7d113fd9093664ff4388bb23dc5d965c4fc71bca532a14965288d19c
- clm_8bc3bd61011719de6c1bb3967f9167fa420f29a6798ee049fc4b43cfaa10db7d
- clm_8f8e243c7894aaae7c07105812ae913a893272e617db9e7e8da5ae678ff61d00
- clm_aa0533e83e020de0ba11accedef3a51076cfd804d35119d3f7bbf0cc57a95031
- clm_b09d479d537bb5ec2c7ed371f02004229ac8a3363025de02f6e0de003fee8551
- clm_c2ce61504f925f38815abacc83f66e0662c1f2d7a9bed036dee9f36201257a56
maturity: draft
page_id: pg_dddc23bc87ba5fe3a708324a6fa59387
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b5791b2764635c33b58ac93e89a92955
title: XMUDeepLIT/LegalGraphRAG/README.md @ a3c9c3070cad
updated_at: '2026-09-14T04:33:00Z'
---

# XMUDeepLIT/LegalGraphRAG/README.md @ a3c9c3070cad

<!-- rcw:begin owner=source:src_b5791b2764635c33b58ac93e89a92955 block=evidence -->
- The default embedding endpoint is http://localhost:11434/api/embed with model bge-m3; both are configurable in configs/main.env and used by graph construction and retrieval. [@claim:clm_2638e2eca2b71744afad6bfde96cadb892cca5a2a8d10ed60f8f2efc92f90acf]
- The constructed graph is persisted to a pickle file (e.g. outputs/main_experiment/qwen3_graph_db.pkl); later runs can skip construction, and changing the construction model requires --force-rebuild or a different graph_db_path. [@claim:clm_3deeee6918b08e5091745913ea9dc4decb462e0fe2c434e7a90f2365a2c71cb9]
- The framework computes legal judgment prediction metrics: charge and law-article exact-match accuracy and Micro-F1, plus imprisonment term exact match and mean absolute error in months. [@claim:clm_43bbceab113b58c7ba6290df541a0bda88203cb3cf67f3f03f3f628e5980aba8]
- Baseline systems such as HippoRAG2, RAPTOR, LightRAG, LegalDelta, and ADAPT are not included in the repository; their outputs can be compared externally if converted to the same result schema. [@claim:clm_76fa19e420250ca5f943589b6273de2b3d3684a1b472083a6f3b004453f33ef5]
- Supported model choices include qwen3, qwen2_5, gemma3, internlm3, glm4, deepseek_v3, and gpt4o_mini; prompt_language=zh or en in .env selects Chinese or English prompts. [@claim:clm_7dfabf1b7d113fd9093664ff4388bb23dc5d965c4fc71bca532a14965288d19c]
- The core package contains a main LegalGraphRAG class plus modules for models (transformers and OpenAI-compatible), graph construction, legal judgment, preprocessing, prompts, and utilities. [@claim:clm_8bc3bd61011719de6c1bb3967f9167fa420f29a6798ee049fc4b43cfaa10db7d]
- Evaluation aggregation follows the paper's scripts: charge and law predictions are scored per entry in judge_res, while imprisonment uses the first judgment for each of the 568 CAIL cases. [@claim:clm_8f8e243c7894aaae7c07105812ae913a893272e617db9e7e8da5ae678ff61d00]
- Multi-GPU execution is supported by passing several devices to run.py, and cases are automatically distributed across the selected devices. [@claim:clm_aa0533e83e020de0ba11accedef3a51076cfd804d35119d3f7bbf0cc57a95031]
- Repository setup workflow: install requirements via pip, copy env.example to .env, and verify bundled experiment assets with sha256sum -c SHA256SUMS. [@claim:clm_b09d479d537bb5ec2c7ed371f02004229ac8a3363025de02f6e0de003fee8551]
- run.py exposes CLI arguments including --model, --datasets, --dotenv_path, --datasets_path, --devices, --no-build-graph, and --force-rebuild. [@claim:clm_c2ce61504f925f38815abacc83f66e0662c1f2d7a9bed036dee9f36201257a56]
<!-- rcw:end owner=source:src_b5791b2764635c33b58ac93e89a92955 block=evidence -->

## Researcher notes

