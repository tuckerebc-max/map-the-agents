# rawwerks/recursive-coding-agents

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0c71127a731c @ 84739f8a75fa1e91

## Summary (orientation draft, not independently verified)

This repository is a companion artifact for a talk on Recursive Language Models for coding agents: a SvelteKit presentation website, a seven-gate RLM rubric with judging methodology, and verdict-shaped RLM/not-RLM example sets. Most development guidance (bun checks, deploy scripts, git hooks) is contributor workflow, not shipped runtime behavior.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The repo defines Recursive Language Models (RLMs) as systems that keep context as symbolic state, inspect and slice it with code, call models or agents over slices, and aggregate results verifiably. -- evidence: [README.md#L9-L9](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L9-L9)
  - [observation/documented] A one-line RLM definition states the task context moves into a persistent executable environment, the root model works through handles, and final answers return through the outer model-call interface. -- evidence: [README.md#L40-L40](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L40-L40)
- components (2 claim(s)):
  - [observation/documented] The repository contains four main parts: a SvelteKit web deck, an rlm-rubric directory, Claude Code workflow examples, and OpenProse program examples. -- evidence: [README.md#L26-L32](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L26-L32)
  - [observation/documented] The rubric directory includes an RLM definition, a seven-gate rubric, and a judging methodology document for evidence-based system judgment. -- evidence: [README.md#L15-L22](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L15-L22), [README.md#L26-L32](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L26-L32)
- design-choices (2 claim(s)):
  - [observation/documented] Example folders are verdict-shaped: files under rlm/ are passing or intended-passing examples, while not-rlm/ holds nearby negative controls. -- evidence: [README.md#L34-L34](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L34-L34)
  - [observation/documented] Judging is by run shape rather than product label: a full RLM requires externalized context behind handles, model-chosen decomposition, programmatic calls over slices, and symbolic aggregation. -- evidence: [README.md#L36-L36](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L36-L36)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: contributors run bun-based checks from web/ including svelte-check, design, social-metadata, and theme tests, plus a production build. -- evidence: [DEVELOPING.md#L21-L27](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/DEVELOPING.md#L21-L27)
  - [observation/documented] Repository development practice: pre-commit hooks run gitleaks on staged changes, and pre-push hooks only remind maintainers that deploys are explicit; hooks are activated via core.hooksPath. -- evidence: [DEVELOPING.md#L38-L38](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/DEVELOPING.md#L38-L38), [DEVELOPING.md#L40-L42](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/DEVELOPING.md#L40-L42), [DEVELOPING.md#L44-L46](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/DEVELOPING.md#L44-L46)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The live presentation is a website at https://recursivecodingagents.com, described as the public deck for the AI Engineer World's Fair 2026 talk. -- evidence: [README.md#L3-L3](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L3-L3), [README.md#L5-L5](https://github.com/rawwerks/recursive-coding-agents/blob/0c71127a731c33b1e2db458280aac1c4cdc254fe/README.md#L5-L5)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](recursive-coding-agents.detail.md)

Metadata and full claim list: [full detail](recursive-coding-agents.detail.md)
Human notes ([notes](recursive-coding-agents.notes.md), never overwritten by build)

[Back to map index](../../index.md)
