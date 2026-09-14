# whut09/opencode-plusplus

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 598767170bb7 @ 009551e19bce206c

## Summary (orientation draft, not independently verified)

OpenCode++ is a Windows-first in-process plugin for OpenCode Desktop that adds a verification control plane (context, guards, evidence, decisions) around the existing model's coding work, with CLI/MCP developer surfaces and local `.agent-context/` artifacts. Evidence is documentation-only; no source code slices are present. Evidence coverage: 127 of 183 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 118 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The architecture is described as Guard modules around coding agents: Context, Hallucination, Boundary, Regression, Evidence, Impact, and Loop Guards, plus an Executor Adapter and Trace Normalizer. -- evidence: [docs/concepts/architecture.md#L61-L68](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/docs/concepts/architecture.md#L61-L68)
  - [observation/documented] The v2 architecture has five responsibilities: Repo Scanner, Context Planner, Context Pack Composer, Agent Harness Layer, and an Integration Layer exposing CLI, stdio MCP server, and retriever adapters. -- evidence: [docs/concepts/architecture.md#L145-L149](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/docs/concepts/architecture.md#L145-L149)
- design-choices (2 claim(s)):
  - [observation/documented] By default the plugin works offline: it does not fetch remote Context sources or call a second model; remote sources or feedback transports must be explicitly enabled. -- evidence: [README.md#L48-L48](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L48-L48)
  - [observation/documented] The plugin runs in-process inside OpenCode Desktop, does not start a second model or CLI process, and does not expose hidden model chain-of-thought. -- evidence: [README.md#L44-L44](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L44-L44), [README.md#L92-L92](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L92-L92)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors fork, read AGENTS.md, add deterministic tests before behavior changes, keep runtime artifacts out of commits, and run npm run check, lint, format:check, docs:bilingual:check, and npm test. -- evidence: [README.md#L125-L131](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L125-L131)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The Windows installer adds a selectable OpenCode primary mode named OpenCode++ chosen from the mode picker, with no Slash Commands to remember. -- evidence: [README.md#L40-L40](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L40-L40)
  - [observation/documented] Documented MCP tools include opencode_plusplus_build, plan, pack, retrieve, tests, impact, verify, and explain, plus experimental runtime loop tools for start/evaluate/repair/finalize flows. -- evidence: [docs/concepts/architecture.md#L145-L149](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/docs/concepts/architecture.md#L145-L149)
- memory-state (2 claim(s)):
  - [observation/documented] Runtime artifacts are local per repository: traces, runs, loops, sidecar latest.md and visualization.json, plus cache, context-registry usage/feedback, annotations, and interventions directories under .agent-context/. -- evidence: [README.md#L80-L84](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L80-L84), [README.md#L104-L104](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/README.md#L104-L104)
  - [observation/documented] The loop state file records state, previousState, repository/context/diff hashes, lastAction, blocking nextAction, allowedActions, satisfiedEvidence, and missingEvidence for resumable runs. -- evidence: [docs/concepts/architecture.md#L334-L334](https://github.com/whut09/opencode-plusplus/blob/598767170bb73e869293c6a91526bcb852b696c0/docs/concepts/architecture.md#L334-L334)
- orchestration (2 claim(s)):
More evidence: [full detail](opencode-plusplus.detail.md)

Metadata and full claim list: [full detail](opencode-plusplus.detail.md)
Human notes ([notes](opencode-plusplus.notes.md), never overwritten by build)

[Back to map index](../../index.md)
