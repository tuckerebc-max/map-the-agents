# liu-hy/genomas

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d6365a700794 @ 5c67da614f29c857

## Summary (orientation draft, not independently verified)

The README documents GenoMAS, a multi-agent framework for code-driven gene expression analysis, with usage instructions, CLI configuration, cost estimates, and troubleshooting; evidence is limited to README text and requirements.txt.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] GenoMAS analyzes transcriptomic datasets from GEO and TCGA to identify trait-related genes while accounting for confounders. -- evidence: [README.md#L63-L66](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L63-L66)
- components (1 claim(s)):
  - [observation/documented] The repository contains two main components: a general multi-agent framework for automating scientific workflows, and a specialized GenoMAS implementation for gene expression analysis. -- evidence: [README.md#L61-L61](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L61-L61), [README.md#L46-L46](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L46-L46), [README.md#L49-L49](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L49-L49)
- design-choices (1 claim(s)):
  - [observation/documented] The stated design philosophy balances controllability of traditional workflows with autonomous-agent flexibility, favoring minimal encapsulation for easier agent experiments. -- evidence: [README.md#L55-L58](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L55-L58)
- workflows (1 claim(s)):
  - [observation/documented] Setup involves downloading ~42 GB of GenoTEX input data, validating it with download/validator.py, creating a Python 3.10 conda environment, and configuring API keys in a .env file copied from env.example. -- evidence: [README.md#L113-L113](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L113-L113), [README.md#L104-L109](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L104-L109), [README.md#L115-L117](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L115-L117), [README.md#L92-L92](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L92-L92), [README.md#L94-L98](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L94-L98)
- skills-patterns (1 claim(s)):
  - [observation/documented] An --generate-action-units mode generates Action Unit prompts from agent guidelines, optionally pausing for manual editing, with a --non-interactive variant for automated pipelines. -- evidence: [README.md#L209-L213](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L209-L213), [README.md#L217-L226](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L217-L226), [README.md#L228-L228](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L228-L228), [README.md#L199-L207](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L199-L207)
- interfaces (2 claim(s)):
  - [observation/documented] The framework provides a typed messaging communication protocol for code-driven analysis, a notebook-style workflow where agents plan, write, execute, debug, and backtrack, and customizable agent roles. -- evidence: [README.md#L51-L53](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L51-L53)
  - [observation/documented] The CLI supports per-role model overrides (e.g., --code-reviewer-model, --domain-expert-model, --statistician-model, --planning-model) that override the global --model and --api settings. -- evidence: [README.md#L136-L141](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L136-L141)
- memory-state (1 claim(s)):
  - [observation/documented] The system implements checkpoint resume logic: rerunning the same command after an interruption continues from where it left off, clearing outputs of half-finished tasks. -- evidence: [README.md#L295-L295](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L295-L295)
- orchestration (1 claim(s)):
  - [observation/documented] A --parallel-mode cohorts option with --max-workers enables concurrent cohort preprocessing, reducing wall-clock time, though large worker counts may hit API rate limits. -- evidence: [README.md#L128-L134](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L128-L134), [README.md#L186-L193](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L186-L193), [README.md#L195-L195](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L195-L195)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] The README reports a 60.38% F1 score on the GenoTEX benchmark, claimed to substantially outperform open-domain and generic biomedical agents. -- evidence: [README.md#L63-L66](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L63-L66)
- dependencies (1 claim(s)):
  - [observation/documented] requirements.txt lists LLM client libraries (openai, anthropic, google-generativeai, ollama) plus scientific packages such as numpy, pandas, scikit_learn, statsmodels, biopython, and sparse_lmm. -- evidence: [requirements.txt#L1-L23](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/requirements.txt#L1-L23)
- limitations (1 claim(s)):
More evidence: [full detail](genomas.detail.md)

Metadata and full claim list: [full detail](genomas.detail.md)
Human notes ([notes](genomas.notes.md), never overwritten by build)

[Back to map index](../../index.md)
