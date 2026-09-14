# iwangjian/coding-tutor

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d1fa15b50e09 @ d3dc65a20551d0d7

## Summary (orientation draft, not independently verified)

Selected evidence records: The project proposes Traver (Trace-and-Verify), an agent workflow that incorporates knowledge tracing and turn-by-turn verification for coding tutoring. The work introduces DICT, an evaluation protocol combining student simulation with coding tests to assess tutoring performance.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The project proposes Traver (Trace-and-Verify), an agent workflow that incorporates knowledge tracing and turn-by-turn verification for coding tutoring. -- evidence: [README.md#L11-L11](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L11-L11)
  - [observation/documented] A trained verifier checkpoint (Verifier-7B) is released for download on Hugging Face. -- evidence: [README.md#L98-L98](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L98-L98)
- design-choices (1 claim(s)):
  - [observation/documented] Although coding tutoring is the example scenario, the authors state the method extends to other task-tutoring settings where content must adapt to users' varying background knowledge. -- evidence: [README.md#L11-L11](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L11-L11)
- workflows (3 claim(s)):
  - [observation/documented] Setup requires downloading EvoCodeBench-2403 and building its execution environment per that project's instructions, which the README notes can take a few hours. -- evidence: [README.md#L26-L26](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L26-L26)
  - [observation/documented] The project is installed via a Python 3.10 conda environment followed by pip install -r requirements.txt. -- evidence: [README.md#L28-L33](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L28-L33)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Users must configure their own Azure API key, data path, and model path based on files under scripts/run/ before use. -- evidence: [README.md#L37-L37](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L37-L37)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (4 claim(s)):
  - [observation/documented] The work introduces DICT, an evaluation protocol combining student simulation with coding tests to assess tutoring performance. -- evidence: [README.md#L11-L11](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L11-L11)
  - [observation/documented] The README reports that simulated students at different levels show distinct task-completion abilities, and presents DICT as a scalable, cost-effective proxy for human evaluation. -- evidence: [README.md#L133-L133](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L133-L133)
- dependencies (1 claim(s)):
  - [observation/documented] requirements.txt pins libraries including torch 2.4.0, transformers 4.44.2, vllm 0.5.4, deepspeed 0.15.0, flash-attn 2.7.2.post1, peft 0.13.2, and openai 1.35.12. -- evidence: [requirements.txt#L1-L25](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/requirements.txt#L1-L25)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
  - [observation/documented] The work was accepted to ACL Findings 2025 and released on arXiv (2502.13311) in February 2025. -- evidence: [README.md#L19-L21](https://github.com/iwangjian/Coding-Tutor/blob/d1fa15b50e0975e8071e7cfd59d3c8596de34f04/README.md#L19-L21)

(4 additional claim(s) omitted for length; see [full detail](coding-tutor.detail.md) for every claim.)

Metadata and full claim list: [full detail](coding-tutor.detail.md)
Human notes ([notes](coding-tutor.notes.md), never overwritten by build)

[Back to map index](../../index.md)
