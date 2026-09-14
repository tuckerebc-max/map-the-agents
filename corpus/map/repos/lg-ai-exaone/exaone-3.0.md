# lg-ai-exaone/exaone-3.0

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3edac90ae905 @ 4f3f4a45bd943a88

## Summary (orientation draft, not independently verified)

README-only evidence for EXAONE-3.0-7.8B-Instruct: a bilingual (English/Korean) 7.8B instruction-tuned language model from LG AI Research, with usage via HuggingFace transformers, benchmark comparisons, stated limitations, and a non-commercial license.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] EXAONE-3.0-7.8B-Instruct is a bilingual English/Korean generative model with 7.8 billion parameters, pre-trained on 8T curated tokens. -- evidence: [README.md#L13-L15](https://github.com/LG-AI-EXAONE/EXAONE-3.0/blob/3edac90ae9057cbb59eb04ea67783ed0d88b2007/README.md#L13-L15)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The model was post-trained with supervised fine-tuning followed by direct preference optimization. -- evidence: [README.md#L13-L15](https://github.com/LG-AI-EXAONE/EXAONE-3.0/blob/3edac90ae9057cbb59eb04ea67783ed0d88b2007/README.md#L13-L15)
  - [observation/documented] The instruction-tuned model was trained to use a system prompt, and the README highly recommends the provided system prompt in code examples. -- evidence: [README.md#L84-L86](https://github.com/LG-AI-EXAONE/EXAONE-3.0/blob/3edac90ae9057cbb59eb04ea67783ed0d88b2007/README.md#L84-L86)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Usage is via HuggingFace transformers AutoModelForCausalLM/AutoTokenizer with trust_remote_code=True, bfloat16 dtype, and a chat template applied to system/user messages. -- evidence: [README.md#L53-L59](https://github.com/LG-AI-EXAONE/EXAONE-3.0/blob/3edac90ae9057cbb59eb04ea67783ed0d88b2007/README.md#L53-L59), [README.md#L49-L51](https://github.com/LG-AI-EXAONE/EXAONE-3.0/blob/3edac90ae9057cbb59eb04ea67783ed0d88b2007/README.md#L49-L51), [README.md#L65-L74](https://github.com/LG-AI-EXAONE/EXAONE-3.0/blob/3edac90ae9057cbb59eb04ea67783ed0d88b2007/README.md#L65-L74)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] README reports benchmark results including MT-Bench 9.01, Arena-Hard-v0.1 46.8, WildBench 48.2, and Korean KoMT-Bench 8.92, compared against similar-size open models. -- evidence: [README.md#L30-L37](https://github.com/LG-AI-EXAONE/EXAONE-3.0/blob/3edac90ae9057cbb59eb04ea67783ed0d88b2007/README.md#L30-L37)
- dependencies (2 claim(s)):
  - [observation/documented] The model requires transformers>=4.41.0, with the latest version recommended. -- evidence: [README.md#L43-L43](https://github.com/LG-AI-EXAONE/EXAONE-3.0/blob/3edac90ae9057cbb59eb04ea67783ed0d88b2007/README.md#L43-L43)
  - [observation/documented] The model is licensed under the EXAONE AI Model License Agreement 1.1 - NC, revised in August 2024. -- evidence: [README.md#L108-L108](https://github.com/LG-AI-EXAONE/EXAONE-3.0/blob/3edac90ae9057cbb59eb04ea67783ed0d88b2007/README.md#L108-L108), [README.md#L21-L22](https://github.com/LG-AI-EXAONE/EXAONE-3.0/blob/3edac90ae9057cbb59eb04ea67783ed0d88b2007/README.md#L21-L22)
- limitations (2 claim(s)):
  - [observation/documented] Documented limitations include possible inappropriate or biased responses, statistically driven errors, and outdated knowledge leading to false or contradictory answers. -- evidence: [README.md#L94-L98](https://github.com/LG-AI-EXAONE/EXAONE-3.0/blob/3edac90ae9057cbb59eb04ea67783ed0d88b2007/README.md#L94-L98), [README.md#L92-L92](https://github.com/LG-AI-EXAONE/EXAONE-3.0/blob/3edac90ae9057cbb59eb04ea67783ed0d88b2007/README.md#L92-L92)
  - [observation/documented] Users are prohibited from malicious activities that could induce outputs violating LG AI's ethical principles. -- evidence: [README.md#L100-L102](https://github.com/LG-AI-EXAONE/EXAONE-3.0/blob/3edac90ae9057cbb59eb04ea67783ed0d88b2007/README.md#L100-L102)
- relevance (1 claim(s)):
  - [observation/documented] The 7.8B instruction-tuned model was released 2024.08.07 by LG AI Research, with a technical report at arXiv:2408.03541. -- evidence: [README.md#L114-L121](https://github.com/LG-AI-EXAONE/EXAONE-3.0/blob/3edac90ae9057cbb59eb04ea67783ed0d88b2007/README.md#L114-L121), [README.md#L21-L22](https://github.com/LG-AI-EXAONE/EXAONE-3.0/blob/3edac90ae9057cbb59eb04ea67783ed0d88b2007/README.md#L21-L22)

Every claim for this repository is shown above and in [full detail](exaone-3.0.detail.md).

Metadata and full claim list: [full detail](exaone-3.0.detail.md)
Human notes ([notes](exaone-3.0.notes.md), never overwritten by build)

[Back to map index](../../index.md)
