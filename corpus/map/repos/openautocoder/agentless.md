# openautocoder/agentless

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5ce5888b9f14 @ 0ded953bb5955e7b

## Summary (orientation draft, not independently verified)

Agentless is an agentless, three-phase (localization, repair, patch validation) tool for solving software issues, evaluated on SWE-bench Lite/Verified, driven by CLI scripts and OpenAI models. Evidence covers its pipeline, CLI interface, dependencies, and reported benchmark results.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (4 claim(s)):
  - [observation/documented] Localization is hierarchical: faults are first localized to files, then to classes/functions, then to fine-grained edit locations. -- evidence: [README.md#L25-L28](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README.md#L25-L28), [README_swebench.md#L62-L64](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L62-L64)
  - [observation/documented] File-level localization combines LLM-predicted suspicious files with embedding-based retrieval, after LLM-identified irrelevant folders are filtered out. -- evidence: [README_swebench.md#L81-L81](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L81-L81), [README_swebench.md#L68-L68](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L68-L68), [README_swebench.md#L83-L83](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L83-L83), [README_swebench.md#L108-L108](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L108-L108)
- design-choices (2 claim(s)):
  - [observation/documented] Agentless solves software development issues without an agent loop, using a three-phase process: localization, repair, and patch validation. -- evidence: [README.md#L25-L28](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README.md#L25-L28)
  - [observation/documented] Regression tests are chosen from all tests passing on the original repository rather than the benchmark's PASS_TO_PASS field. -- evidence: [README_swebench.md#L251-L255](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L251-L255)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are asked to install a pre-commit hook for standardized code style. -- evidence: [README.md#L49-L50](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README.md#L49-L50)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The tool is operated via CLI scripts (e.g., agentless/fl/localize.py, repair/repair.py, rerank.py) with flags like --dataset, --target_id, --num_threads, and --max_samples. -- evidence: [README_swebench.md#L38-L42](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L38-L42), [README_swebench.md#L72-L77](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L72-L77), [README_swebench.md#L50-L54](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L50-L54), [README_swebench.md#L194-L205](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L194-L205), [README_swebench.md#L56-L58](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L56-L58), [README_swebench.md#L353-L359](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L353-L359)
  - [observation/documented] The benchmark dataset is selectable via --dataset, defaulting to SWE-bench Lite, with SWE-bench Verified also supported. -- evidence: [README_swebench.md#L38-L42](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L38-L42), [README_swebench.md#L11-L12](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L11-L12)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] Reported results: with Claude 3.5 Sonnet, 40.7% and 50.8% solve rates on SWE-bench Lite and Verified; v1.0 achieved 27.3% (82 fixes) on SWE-bench Lite at ~$0.34 per issue. -- evidence: [README.md#L19-L21](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README.md#L19-L21)
- dependencies (2 claim(s)):
  - [observation/documented] Embedding-based retrieval uses OpenAI's text-embedding-3-small model. -- evidence: [README_swebench.md#L95-L95](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L95-L95)
  - [observation/documented] The tool requires an OpenAI API key exported as OPENAI_API_KEY, and requirements include openai, anthropic, tiktoken, libcst, llama-index, and the SWE-bench package. -- evidence: [README.md#L55-L58](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README.md#L55-L58), [requirements.txt#L1-L9](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/requirements.txt#L1-L9), [README_swebench.md#L28-L31](https://github.com/OpenAutoCoder/Agentless/blob/5ce5888b9f149beaace393957a55ea8ee46c9f71/README_swebench.md#L28-L31)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(2 additional claim(s) omitted for length; see [full detail](agentless.detail.md) for every claim.)

Metadata and full claim list: [full detail](agentless.detail.md)
Human notes ([notes](agentless.notes.md), never overwritten by build)

[Back to map index](../../index.md)
