# julien-c/synthtraces

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e5f8ec99d814 @ 255a7f2e31a09665

## Summary (orientation draft, not independently verified)

The repository is a minimal codebase for generating synthetic coding-agent session traces using Pi, pairing remote open agent models with local llama.cpp user models across a 24,000-session generation matrix. Evidence is limited to README and a model list; no code or workflow details are present.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The project is described as a minimal codebase that generates synthetic coding agent session traces using the Pi coding-agent package. -- evidence: [README.md#L14-L14](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L14-L14)
  - [observation/documented] The generation matrix comprises 20 agent models, 3 local user models, 20 codebases, and 20 starting questions, totaling 24,000 sessions. -- evidence: [README.md#L25-L31](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L25-L31)
- components (1 claim(s)):
  - [observation/documented] The full exchange is recorded as a trace, and the dataset is the cartesian product of agent model, user model, codebase, and starting question. -- evidence: [README.md#L21-L21](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L21-L21)
- design-choices (1 claim(s)):
  - [observation/documented] Each generated session pairs two models: a remotely hosted open model acting as the coding agent and a local llama.cpp model playing the user, within one of the project codebases. -- evidence: [README.md#L18-L19](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L18-L19), [README.md#L16-L16](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L16-L16)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The user model opens with one of the starting questions and drives the conversation with the agent over up to N turns, while the agent reads, edits, and runs against a locally cloned codebase. -- evidence: [README.md#L35-L54](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L35-L54), [README.md#L18-L19](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L18-L19)
- tools-permissions (1 claim(s)):
  - [observation/documented] The coding agent is equipped with the default Pi tools: read, write, edit, and bash. -- evidence: [README.md#L18-L19](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L18-L19)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The 20 remote agent models are served by providers including novita, featherless-ai, together, groq, and nscale, per the listed model table. -- evidence: [remote-models.md#L1-L22](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/remote-models.md#L1-L22)
  - [observation/documented] Local user models are GGUF quantizations (Q8_0) such as Qwen3.6-27B, Qwen3.6-35B-A3B-MTP, and gemma-4-26B-A4B-it, run via llama.cpp. -- evidence: [README.md#L25-L31](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L25-L31), [README.md#L18-L19](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L18-L19)
- limitations (1 claim(s)):
  - [observation/documented] The README's final statistics section is a TODO, to be populated after generation with success rate, turn counts, and token counts. -- evidence: [README.md#L58-L58](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L58-L58)
- relevance (1 claim(s)):
  - [observation/documented] The project is MIT-licensed, English-language, and links to a GitHub code repository and a Hugging Face dataset, both named julien-c/synthtraces. -- evidence: [README.md#L1-L8](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L1-L8), [README.md#L62-L64](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L62-L64), [README.md#L68-L69](https://github.com/julien-c/synthtraces/blob/e5f8ec99d8140bcf650b61d9401af996c0c70789/README.md#L68-L69)
More evidence: [full detail](synthtraces.detail.md)

Metadata and full claim list: [full detail](synthtraces.detail.md)
Human notes ([notes](synthtraces.notes.md), never overwritten by build)

[Back to map index](../../index.md)
