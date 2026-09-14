# crewplaneai/crewplane

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit bc0b5eef5762 @ 321edf963f9ad975

## Summary (orientation draft, not independently verified)

Evidence consists of README and CHANGELOG slices describing Crewplane, an open-source Python 3.13+ workflow runner that orchestrates coding-agent CLIs via Markdown-defined workflows, plus a one-line AGENTS.md pointer. No source code is present in the snapshot, so claims are documentation-based. Evidence coverage: 138 of 182 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 59 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Crewplane is described as an open-source workflow runner for reviewable, resumable coding-agent workflows, with the whole process defined in Markdown including prompts, stages, agents, handoffs, and next-step rules. -- evidence: [README.md#L1-L19](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L1-L19)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Handoffs between stages are explicit template references such as {{plan.output}} rather than hidden session context, and sequential nodes can pair an executor with a reviewer role that may send blocking feedback into bounded fix attempts. -- evidence: [README.md#L276-L276](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L276-L276), [README.md#L295-L302](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L295-L302)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md is described as the canonical repository instructions for coding agents, and contributors are directed to CONTRIBUTING.md and a development guide for local checkout setup. -- evidence: [AGENTS.md#L3-L3](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/AGENTS.md#L3-L3), [README.md#L522-L525](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L522-L525)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product provides CLI commands including init, validate, run, onboarding, --update, and --version, and supports running specific task files via a --tasks flag. -- evidence: [README.md#L482-L490](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L482-L490), [README.md#L149-L152](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L149-L152), [README.md#L420-L423](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L420-L423), [README.md#L123-L127](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L123-L127)
  - [observation/documented] Workflows are Markdown files whose YAML frontmatter declares an execution graph with nodes, needs dependencies, parallel or sequential modes, and provider assignments, while Markdown sections define per-stage instructions. -- evidence: [README.md#L262-L266](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L262-L266), [README.md#L253-L260](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L253-L260), [README.md#L235-L237](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L235-L237), [README.md#L248-L251](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L248-L251)
- memory-state (1 claim(s)):
  - [observation/documented] Each run writes artifacts under .crewplane/ with execution-results per run-key for findings and final results and execution-stages for per-node inputs, outputs, logs, events, and manifests; identical inputs reuse the saved result unless --force is passed. -- evidence: [README.md#L135-L139](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L135-L139), [README.md#L194-L196](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L194-L196), [README.md#L174-L188](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L174-L188)
- orchestration (1 claim(s)):
  - [observation/documented] Crewplane validates and runs the declared workflow graph, fans work out in parallel, routes stages to different provider CLIs, enforces review gates, and reuses completed stages it can validate when resuming. -- evidence: [README.md#L384-L405](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L384-L405), [README.md#L370-L382](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L370-L382)
- tools-permissions (1 claim(s)):
  - [observation/documented] Crewplane invokes existing coding-agent CLIs but does not install, authenticate, or sandbox them; providers run with their own configuration and whatever permissions the user's environment grants, keeping models, tools, and credentials under native control. -- evidence: [README.md#L434-L437](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L434-L437), [README.md#L70-L73](https://github.com/crewplaneai/crewplane/blob/bc0b5eef57622a66e79bf70a2274016c4445c19a/README.md#L70-L73)
- evaluation (1 claim(s)):
More evidence: [full detail](crewplane.detail.md)

Metadata and full claim list: [full detail](crewplane.detail.md)
Human notes ([notes](crewplane.notes.md), never overwritten by build)

[Back to map index](../../index.md)
