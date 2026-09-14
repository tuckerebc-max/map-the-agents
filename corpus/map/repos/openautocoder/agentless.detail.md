# openautocoder/agentless -- full detail

[Back to orientation](agentless.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/openautocoder/agentless/5ce5888b9f149beaace393957a55ea8ee46c9f71/0ded953bb5955e7b.json](../../../wiki/dossiers/openautocoder/agentless/5ce5888b9f149beaace393957a55ea8ee46c9f71/0ded953bb5955e7b.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (4 claim(s))

- [observation/documented] Localization is hierarchical: faults are first localized to files, then to classes/functions, then to fine-grained edit locations. -- evidence: [README.md#L25-L28](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README.md#L25-L28), [README_swebench.md#L62-L64](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L62-L64) (`clm_a72d597e3d509cc7383c4a2406b18d4b5f4257f3833cd6a77c180f0d22c11895`)
- [observation/documented] File-level localization combines LLM-predicted suspicious files with embedding-based retrieval, after LLM-identified irrelevant folders are filtered out. -- evidence: [README_swebench.md#L81-L81](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L81-L81), [README_swebench.md#L68-L68](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L68-L68), [README_swebench.md#L83-L83](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L83-L83), [README_swebench.md#L108-L108](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L108-L108) (`clm_44e59be57b2f874052be59b9133920cb4f4054210d85b168b6f04d2e63404e41`)
- [observation/documented] Repair samples multiple candidate patches per bug in a simple diff format, with context windows around each edit location. -- evidence: [README.md#L25-L28](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README.md#L25-L28), [README_swebench.md#L194-L205](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L194-L205), [README_swebench.md#L228-L228](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L228-L228) (`clm_26431d3167774d453f21f3f0d6cc485651a9a38155f63fccc0c05e54fae50996`)
- [observation/documented] Patch validation runs selected regression tests plus generated reproduction tests, and results are used to re-rank and select the final patch. -- evidence: [README.md#L25-L28](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README.md#L25-L28), [README_swebench.md#L349-L349](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L349-L349), [README_swebench.md#L236-L236](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L236-L236) (`clm_f0e5e51d052be817ae8712f42304656f921c343d5e04e1a47b9ff2117769ec16`)

## design-choices (2 claim(s))

- [observation/documented] Agentless solves software development issues without an agent loop, using a three-phase process: localization, repair, and patch validation. -- evidence: [README.md#L25-L28](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README.md#L25-L28) (`clm_ea4f1685fabc66a7ba2c25042f1702330a91fd6683a34494797a0b3eab05595b`)
- [observation/documented] Regression tests are chosen from all tests passing on the original repository rather than the benchmark's PASS_TO_PASS field. -- evidence: [README_swebench.md#L251-L255](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L251-L255) (`clm_5c1b40b678c008fbaadd96e618ef4eac364ed69af1f7d6d3533b3c5d498b616e`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors are asked to install a pre-commit hook for standardized code style. -- evidence: [README.md#L49-L50](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README.md#L49-L50) (`clm_d51faede34c1415543919d2a51badad21019a37c116123e50ef0634ff8f1dfec`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The tool is operated via CLI scripts (e.g., agentless/fl/localize.py, repair/repair.py, rerank.py) with flags like --dataset, --target_id, --num_threads, and --max_samples. -- evidence: [README_swebench.md#L38-L42](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L38-L42), [README_swebench.md#L72-L77](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L72-L77), [README_swebench.md#L50-L54](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L50-L54), [README_swebench.md#L194-L205](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L194-L205), [README_swebench.md#L56-L58](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L56-L58), [README_swebench.md#L353-L359](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L353-L359) (`clm_ed3ce18c5b72eb6be11eb06fef3ca810f7d69e53c7d5cc26956a9fce0cbbe64b`)
- [observation/documented] The benchmark dataset is selectable via --dataset, defaulting to SWE-bench Lite, with SWE-bench Verified also supported. -- evidence: [README_swebench.md#L38-L42](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L38-L42), [README_swebench.md#L11-L12](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L11-L12) (`clm_ca3c3a89874780b424d41fb68f2146326b1e460d34bdbafac0ee087440018ae2`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] Reported results: with Claude 3.5 Sonnet, 40.7% and 50.8% solve rates on SWE-bench Lite and Verified; v1.0 achieved 27.3% (82 fixes) on SWE-bench Lite at ~$0.34 per issue. -- evidence: [README.md#L19-L21](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README.md#L19-L21) (`clm_499cdd9aa559cbe400f9166db0da9acd32e9a0fe92b031516658c3e5fd974644`)

## dependencies (2 claim(s))

- [observation/documented] Embedding-based retrieval uses OpenAI's text-embedding-3-small model. -- evidence: [README_swebench.md#L95-L95](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L95-L95) (`clm_8c6b77670962c4fdc5666434dd14d3270f94de24ddd205c1821bfcfe6c116cbe`)
- [observation/documented] The tool requires an OpenAI API key exported as OPENAI_API_KEY, and requirements include openai, anthropic, tiktoken, libcst, llama-index, and the SWE-bench package. -- evidence: [README.md#L55-L58](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README.md#L55-L58), [requirements.txt#L1-L9](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/requirements.txt#L1-L9), [README_swebench.md#L28-L31](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L28-L31) (`clm_be892d20062dc631b9474dbf2160838bd9bf9391131841f9eb34e9bdfa48f3b1`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

