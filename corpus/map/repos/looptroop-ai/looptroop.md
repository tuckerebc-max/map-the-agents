# looptroop-ai/looptroop

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b96f5448251c @ 3f7a06becba16b57

## Summary (orientation draft, not independently verified)

LoopTroop is a local GUI orchestrator that turns coding tickets into planned, agent-executed pull requests via LLM-council planning, bead decomposition, OpenCode worktree execution, and Ralph-style retry loops. Evidence is mostly README documentation plus contributor guides; no source code is shown.

## Source coverage

Source coverage (partial): 3 of 6 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The product converts a ticket into a PRD with Epics and User Stories plus decomposed implementation steps, stored as a durable artifact for later bead execution. -- evidence: [README.md#L288-L288](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L288-L288)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] Planning uses an LLM Council where multiple model instances draft plans, score each other with a weighted rubric, vote, and the winner refines and verifies coverage. -- evidence: [README.md#L271-L274](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L271-L274), [README.md#L269-L269](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L269-L269)
  - [observation/documented] Work is decomposed into 'beads' — small independently implementable units with purpose, acceptance criteria, dependencies, target files, and validation steps. -- evidence: [README.md#L303-L303](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L303-L303), [README.md#L296-L301](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L296-L301)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: contributors run `npm install` and `npm run dev` (dev server at localhost:5173), with lint, typecheck, and test scripts available, and a preview mode serving a built bundle. -- evidence: [CONTRIBUTING.md#L35-L37](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L35-L37), [CONTRIBUTING.md#L22-L27](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L22-L27), [CONTRIBUTING.md#L29-L29](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L29-L29), [CONTRIBUTING.md#L45-L49](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L45-L49)
  - [observation/documented] Repository development practice: pull requests should stay focused, include a summary, rationale, affected workflow areas, tests run, and doc/changelog updates, avoiding unrelated refactors mixed with behavior changes. -- evidence: [CONTRIBUTING.md#L84-L84](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L84-L84), [CONTRIBUTING.md#L92-L92](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L92-L92), [CONTRIBUTING.md#L86-L90](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/CONTRIBUTING.md#L86-L90)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] A CLI is provided: `looptroop open` starts the app in the background if not running, and `looptroop start` runs the service without a browser. -- evidence: [README.md#L66-L69](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L66-L69), [README.md#L71-L72](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L71-L72)
  - [observation/documented] A local GUI dashboard lets users manage attached repositories, configure implementer and council models, answer interview questions, and track ticket, bead, and execution-log state. -- evidence: [README.md#L35-L36](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L35-L36), [README.md#L41-L42](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L41-L42), [README.md#L26-L27](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L26-L27), [README.md#L32-L33](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L32-L33), [README.md#L29-L30](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L29-L30)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] Execution runs each bead via OpenCode in isolated Git worktrees; on failure a Ralph-style loop logs the trace, resets the worktree, discards the session, and retries fresh until tests pass or limits are hit. -- evidence: [README.md#L315-L315](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L315-L315), [README.md#L311-L313](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L311-L313), [README.md#L309-L309](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L309-L309)
  - [observation/documented] The ticket pipeline flows from codebase discovery through council planning, an approval gate, isolated bead execution, final tests, optional manual QA, and integration/PR review, with QA failures spawning fix beads. -- evidence: [README.md#L239-L251](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L239-L251), [README.md#L253-L253](https://github.com/looptroop-ai/LoopTroop/blob/b96f5448251cbe88cd845cd5f262adda02701413/README.md#L253-L253)
- tools-permissions (1 claim(s)):
More evidence: [full detail](looptroop.detail.md)

Metadata and full claim list: [full detail](looptroop.detail.md)
Human notes ([notes](looptroop.notes.md), never overwritten by build)

[Back to map index](../../index.md)
