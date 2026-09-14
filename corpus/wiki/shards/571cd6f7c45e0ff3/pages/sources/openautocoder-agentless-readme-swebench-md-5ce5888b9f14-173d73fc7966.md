---
access: public
aliases: []
claim_ids:
- clm_26431d3167774d453f21f3f0d6cc485651a9a38155f63fccc0c05e54fae50996
- clm_44e59be57b2f874052be59b9133920cb4f4054210d85b168b6f04d2e63404e41
- clm_5c1b40b678c008fbaadd96e618ef4eac364ed69af1f7d6d3533b3c5d498b616e
- clm_8c6b77670962c4fdc5666434dd14d3270f94de24ddd205c1821bfcfe6c116cbe
- clm_a72d597e3d509cc7383c4a2406b18d4b5f4257f3833cd6a77c180f0d22c11895
- clm_be892d20062dc631b9474dbf2160838bd9bf9391131841f9eb34e9bdfa48f3b1
- clm_ca3c3a89874780b424d41fb68f2146326b1e460d34bdbafac0ee087440018ae2
- clm_ed3ce18c5b72eb6be11eb06fef3ca810f7d69e53c7d5cc26956a9fce0cbbe64b
- clm_f0e5e51d052be817ae8712f42304656f921c343d5e04e1a47b9ff2117769ec16
maturity: draft
page_id: pg_7fb653b1ca8955d0a323173d73fc7966
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_250162f4fa4f55e59e05634f77d12fab
title: OpenAutoCoder/Agentless/README_swebench.md @ 5ce5888b9f14
updated_at: '2026-09-14T04:13:59Z'
---

# OpenAutoCoder/Agentless/README_swebench.md @ 5ce5888b9f14

<!-- rcw:begin owner=source:src_250162f4fa4f55e59e05634f77d12fab block=evidence -->
- Repair samples multiple candidate patches per bug in a simple diff format, with context windows around each edit location. [@claim:clm_26431d3167774d453f21f3f0d6cc485651a9a38155f63fccc0c05e54fae50996]
- File-level localization combines LLM-predicted suspicious files with embedding-based retrieval, after LLM-identified irrelevant folders are filtered out. [@claim:clm_44e59be57b2f874052be59b9133920cb4f4054210d85b168b6f04d2e63404e41]
- Regression tests are chosen from all tests passing on the original repository rather than the benchmark's PASS_TO_PASS field. [@claim:clm_5c1b40b678c008fbaadd96e618ef4eac364ed69af1f7d6d3533b3c5d498b616e]
- Embedding-based retrieval uses OpenAI's text-embedding-3-small model. [@claim:clm_8c6b77670962c4fdc5666434dd14d3270f94de24ddd205c1821bfcfe6c116cbe]
- Localization is hierarchical: faults are first localized to files, then to classes/functions, then to fine-grained edit locations. [@claim:clm_a72d597e3d509cc7383c4a2406b18d4b5f4257f3833cd6a77c180f0d22c11895]
- The tool requires an OpenAI API key exported as OPENAI_API_KEY, and requirements include openai, anthropic, tiktoken, libcst, llama-index, and the SWE-bench package. [@claim:clm_be892d20062dc631b9474dbf2160838bd9bf9391131841f9eb34e9bdfa48f3b1]
- The benchmark dataset is selectable via --dataset, defaulting to SWE-bench Lite, with SWE-bench Verified also supported. [@claim:clm_ca3c3a89874780b424d41fb68f2146326b1e460d34bdbafac0ee087440018ae2]
- The tool is operated via CLI scripts (e.g., agentless/fl/localize.py, repair/repair.py, rerank.py) with flags like --dataset, --target_id, --num_threads, and --max_samples. [@claim:clm_ed3ce18c5b72eb6be11eb06fef3ca810f7d69e53c7d5cc26956a9fce0cbbe64b]
- Patch validation runs selected regression tests plus generated reproduction tests, and results are used to re-rank and select the final patch. [@claim:clm_f0e5e51d052be817ae8712f42304656f921c343d5e04e1a47b9ff2117769ec16]
<!-- rcw:end owner=source:src_250162f4fa4f55e59e05634f77d12fab block=evidence -->

## Researcher notes

