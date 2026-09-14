# axflow/axflow

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 46ed2a000a44 @ c40d8b59470d8c68

## Summary (orientation draft, not independently verified)

The snapshot documents Axflow, a TypeScript monorepo of AI development modules (@axflow/models, axgen, axeval) with detailed documentation for axeval's LLM-output evaluation framework; evidence is mostly README/docs text with no source code slices.

## Source coverage

Source coverage (partial): 6 of 30 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Axflow ships as a set of modules: @axflow/models (an SDK with React hooks and streaming utilities), axgen (connecting data to LLMs), and axeval (evaluating LLM output quality). -- evidence: [docs/documentation.md#L23-L25](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation.md#L23-L25), [README.md#L13-L15](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/README.md#L13-L15)
  - [observation/documented] Additional modules are planned but in progress: extract (document loading/transform/chunking for vector search), serve (LLM serving with throttling, analytics, logging middleware), and finetune. -- evidence: [README.md#L17-L17](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/README.md#L17-L17), [README.md#L19-L21](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/README.md#L19-L21)
- design-choices (2 claim(s)):
  - [observation/documented] The framework takes a code-first approach emphasizing developer flexibility and control, aiming to break LLM workflows into manageable, intuitive components. -- evidence: [docs/documentation.md#L17-L19](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation.md#L17-L19), [README.md#L27-L29](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/README.md#L27-L29)
  - [observation/documented] Modules are designed for incremental, independent adoption, which also minimizes bundle size; together they form an end-to-end AI application framework. -- evidence: [docs/documentation.md#L29-L29](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation.md#L29-L29), [README.md#L8-L9](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/README.md#L8-L9)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the repository displays a GitHub CI workflow badge, indicating a CI pipeline for the repo. -- evidence: [README.md#L5-L6](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/README.md#L5-L6)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Axeval's API centers on EvalCases (prompt plus one or more evaluators), evaluators that score a prompt/response pair from 0 to 1, EvalResults with metadata like score and latency, Reports, and a Runner that executes suites against models. -- evidence: [docs/documentation/axeval.md#L39-L39](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L39-L39), [docs/documentation/axeval.md#L27-L27](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L27-L27), [docs/documentation/axeval.md#L47-L47](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L47-L47), [docs/documentation/axeval.md#L23-L23](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L23-L23), [docs/documentation/axeval.md#L43-L43](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L43-L43), [docs/documentation/axeval.md#L19-L19](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L19-L19)
  - [observation/documented] Built-in evaluators include match, includes, isValidJSON, and llmRubric, and users can write custom evaluators. -- evidence: [docs/documentation/axeval.md#L29-L33](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L29-L33), [docs/documentation/axeval.md#L35-L35](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L35-L35)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] Axeval is a framework for test-driven LLM engineering: it supports unit-testing prompts, data-driven prompt iteration, and comparing models on latency, cost, and accuracy. -- evidence: [docs/documentation/axeval.md#L5-L7](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L5-L7), [docs/documentation/axeval.md#L3-L3](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L3-L3)
- dependencies (2 claim(s)):
  - [observation/documented] The @axflow/models SDK is documented as zero-dependency and modular. -- evidence: [docs/documentation.md#L23-L25](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation.md#L23-L25), [docs/index.md#L17-L24](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/index.md#L17-L24), [README.md#L13-L15](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/README.md#L13-L15)
  - [observation/documented] Modules are installed independently via npm (npm i axeval; npm install @axflow/models, axgen, axeval). -- evidence: [docs/documentation.md#L31-L35](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation.md#L31-L35), [docs/documentation/axeval.md#L13-L15](https://github.com/axflow/axflow/blob/46ed2a000a4418c85704ca04a6a6ae93f17bf230/docs/documentation/axeval.md#L13-L15)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
More evidence: [full detail](axflow.detail.md)

Metadata and full claim list: [full detail](axflow.detail.md)
Human notes ([notes](axflow.notes.md), never overwritten by build)

[Back to map index](../../index.md)
