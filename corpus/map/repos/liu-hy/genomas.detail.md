# liu-hy/genomas -- full detail

[Back to orientation](genomas.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/liu-hy/genomas/d6365a700794587b53958db3bf22bb1fb80c3451/5c67da614f29c857.json](../../../wiki/dossiers/liu-hy/genomas/d6365a700794587b53958db3bf22bb1fb80c3451/5c67da614f29c857.json)

## specifications (1 claim(s))

- [observation/documented] GenoMAS analyzes transcriptomic datasets from GEO and TCGA to identify trait-related genes while accounting for confounders. -- evidence: [README.md#L63-L66](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L63-L66) (`clm_f9aee05364d355991297de85cc3f3b6231116a88070ade4eaa675d47ecd00f2d`)

## components (1 claim(s))

- [observation/documented] The repository contains two main components: a general multi-agent framework for automating scientific workflows, and a specialized GenoMAS implementation for gene expression analysis. -- evidence: [README.md#L61-L61](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L61-L61), [README.md#L46-L46](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L46-L46), [README.md#L49-L49](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L49-L49) (`clm_a7a0151c5f6c5f731e944a315ef1d975a2c9f9f9dad5bf9a5f3890fb2e7c69c4`)

## design-choices (1 claim(s))

- [observation/documented] The stated design philosophy balances controllability of traditional workflows with autonomous-agent flexibility, favoring minimal encapsulation for easier agent experiments. -- evidence: [README.md#L55-L58](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L55-L58) (`clm_47e3b0dc79dc4d57a86823b73e2e012122499bba756bfd64f69d04b2d641e17e`)

## workflows (1 claim(s))

- [observation/documented] Setup involves downloading ~42 GB of GenoTEX input data, validating it with download/validator.py, creating a Python 3.10 conda environment, and configuring API keys in a .env file copied from env.example. -- evidence: [README.md#L113-L113](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L113-L113), [README.md#L104-L109](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L104-L109), [README.md#L115-L117](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L115-L117), [README.md#L92-L92](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L92-L92), [README.md#L94-L98](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L94-L98) (`clm_4f7bfd89681142653de527c61693108beb18bc981a03f754888cc3f2f6abaad2`)

## skills-patterns (1 claim(s))

- [observation/documented] An --generate-action-units mode generates Action Unit prompts from agent guidelines, optionally pausing for manual editing, with a --non-interactive variant for automated pipelines. -- evidence: [README.md#L209-L213](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L209-L213), [README.md#L217-L226](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L217-L226), [README.md#L228-L228](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L228-L228), [README.md#L199-L207](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L199-L207) (`clm_d1a14f265dd464dde2a720b79002c411e4ce2e1e244cb0117a120bb3f3f4c993`)

## interfaces (2 claim(s))

- [observation/documented] The framework provides a typed messaging communication protocol for code-driven analysis, a notebook-style workflow where agents plan, write, execute, debug, and backtrack, and customizable agent roles. -- evidence: [README.md#L51-L53](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L51-L53) (`clm_42f4c4d8f12ac16be3ef03f265ead00eb322d28c3274ea2599890b989aee8708`)
- [observation/documented] The CLI supports per-role model overrides (e.g., --code-reviewer-model, --domain-expert-model, --statistician-model, --planning-model) that override the global --model and --api settings. -- evidence: [README.md#L136-L141](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L136-L141) (`clm_0f46e5e1bf9353cab532a97f3b9e2ba8657ea21221e2b1e0e73d11fe3de89fce`)

## memory-state (1 claim(s))

- [observation/documented] The system implements checkpoint resume logic: rerunning the same command after an interruption continues from where it left off, clearing outputs of half-finished tasks. -- evidence: [README.md#L295-L295](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L295-L295) (`clm_0e0829451014a6cbd00d03da3be23076b29e5dc7b0684c714d26d6986e4caba9`)

## orchestration (1 claim(s))

- [observation/documented] A --parallel-mode cohorts option with --max-workers enables concurrent cohort preprocessing, reducing wall-clock time, though large worker counts may hit API rate limits. -- evidence: [README.md#L128-L134](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L128-L134), [README.md#L186-L193](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L186-L193), [README.md#L195-L195](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L195-L195) (`clm_e27c3ba7837f16d2b6bd636480076c05a1a54f9e9fc23fb06d57219e45365ecc`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README reports a 60.38% F1 score on the GenoTEX benchmark, claimed to substantially outperform open-domain and generic biomedical agents. -- evidence: [README.md#L63-L66](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L63-L66) (`clm_d90d582e773bc9e5e0074062eb369753ce35b515820fe314c80bb4cd8878e7de`)

## dependencies (1 claim(s))

- [observation/documented] requirements.txt lists LLM client libraries (openai, anthropic, google-generativeai, ollama) plus scientific packages such as numpy, pandas, scikit_learn, statsmodels, biopython, and sparse_lmm. -- evidence: [requirements.txt#L1-L23](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/requirements.txt#L1-L23) (`clm_7b8850f413fc37bf264e1435d556fd582f847e54c55f55691b2df5661a8efab5`)

## limitations (1 claim(s))

- [observation/documented] A full benchmark run over all 1,384 GenoTEX trait-condition pairs is estimated at 3-5 days and $300+ in API cost; experiments require up to 20K input tokens, relevant for local GPU deployment. -- evidence: [README.md#L284-L284](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L284-L284), [README.md#L232-L235](https://github.com/Liu-Hy/GenoMAS/blob/d6365a700794587b53958db3bf22bb1fb80c3451/README.md#L232-L235) (`clm_a275697a9eb050747bfcc4ab6acfbb6ef15f63d17660afd8fa6a30b067d0b5fc`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

