# sr5434/codegebragpt

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 780307f4b361 @ a78afedb2d7017e3

## Summary (orientation draft, not independently verified)

The snapshot is mostly a README describing CodegebraGPT, a planned multimodal STEM LLM finetuned from SOLAR-10.7B-Instruct via QLoRA on ~100k samples drawn from many public datasets, plus a Contributor Covenant code of conduct. No code, evaluation, or runtime behavior is evidenced.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 7 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

7 claim(s) across 4 facet(s); 9 facet(s) unknown.

- specifications (3 claim(s)):
  - [observation/documented] The project's stated purpose is finetuning multimodal LLMs on STEM datasets. -- evidence: [README.md#L2-L2](https://github.com/sr5434/CodegebraGPT/blob/780307f4b361db1f885fc192a00cd563b10bfaaa/README.md#L2-L2)
  - [observation/documented] The README says about 100k samples are used for training (the 100k-text subset) out of roughly one million combined samples, to save costs. -- evidence: [README.md#L8-L22](https://github.com/sr5434/CodegebraGPT/blob/780307f4b361db1f885fc192a00cd563b10bfaaa/README.md#L8-L22)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the project adopts a Contributor Covenant v2.0 code of conduct defining acceptable behavior, an enforcement ladder (warning through permanent ban), and reporting via the maintainer's Instagram handle. -- evidence: [CODE_OF_CONDUCT.md#L112-L113](https://github.com/sr5434/CodegebraGPT/blob/780307f4b361db1f885fc192a00cd563b10bfaaa/CODE_OF_CONDUCT.md#L112-L113), [CODE_OF_CONDUCT.md#L88-L93](https://github.com/sr5434/CodegebraGPT/blob/780307f4b361db1f885fc192a00cd563b10bfaaa/CODE_OF_CONDUCT.md#L88-L93), [CODE_OF_CONDUCT.md#L117-L119](https://github.com/sr5434/CodegebraGPT/blob/780307f4b361db1f885fc192a00cd563b10bfaaa/CODE_OF_CONDUCT.md#L117-L119), [CODE_OF_CONDUCT.md#L79-L81](https://github.com/sr5434/CodegebraGPT/blob/780307f4b361db1f885fc192a00cd563b10bfaaa/CODE_OF_CONDUCT.md#L79-L81), [CODE_OF_CONDUCT.md#L61-L64](https://github.com/sr5434/CodegebraGPT/blob/780307f4b361db1f885fc192a00cd563b10bfaaa/CODE_OF_CONDUCT.md#L61-L64)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Training data is drawn from public Hugging Face datasets including MetaMathQA, Camel AI math/chemistry/physics/biology, GSM8K, MMLU, Evol Instruct Code, Glaive code assistant, arXiv-derived instruct sets, and ScienceQA. -- evidence: [README.md#L8-L22](https://github.com/sr5434/CodegebraGPT/blob/780307f4b361db1f885fc192a00cd563b10bfaaa/README.md#L8-L22)
  - [observation/documented] The planned base model for finetuning is upstage/SOLAR-10.7B-Instruct-v1.0, using the QLoRA method. -- evidence: [README.md#L4-L6](https://github.com/sr5434/CodegebraGPT/blob/780307f4b361db1f885fc192a00cd563b10bfaaa/README.md#L4-L6)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
  - [observation/documented] The model is named after the author's earlier Codegebra equation-solving program and is intended as its successor with a more natural interface and expanded abilities. -- evidence: [README.md#L24-L24](https://github.com/sr5434/CodegebraGPT/blob/780307f4b361db1f885fc192a00cd563b10bfaaa/README.md#L24-L24)

(1 additional claim(s) omitted for length; see [full detail](codegebragpt.detail.md) for every claim.)

Metadata and full claim list: [full detail](codegebragpt.detail.md)
Human notes ([notes](codegebragpt.notes.md), never overwritten by build)

[Back to map index](../../index.md)
