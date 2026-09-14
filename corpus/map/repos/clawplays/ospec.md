# clawplays/ospec

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit be449f2ce698 @ 01de477712b27c38

## Summary (orientation draft, not independently verified)

OSpec is a spec-driven CLI workflow framework (@clawplays/ospec-cli, command `ospec`) that stores change/goal state as repository artifacts, with a lightweight change flow and a controller-based goal workflow using native subagent dispatch and loop commands. All claims below are documentation-based; no runtime code was inspected in this snapshot.

## Source coverage

Source coverage (partial): 6 of 26 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] New projects initialized by `ospec init` default to a nested layout: root .skillrc and README.md with OSpec-managed files under .ospec/, while CLI shorthand like changes/active/<name> still resolves to .ospec/ paths. -- evidence: [README.md#L88-L99](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L88-L99)
  - [observation/documented] A user-selected Change stays a Change regardless of complexity or risk; the full goal workflow is entered via `ospec goal` or explicit opt-in, and the classic change flow has no controller layer or subagents. -- evidence: [README.md#L194-L194](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L194-L194), [README.md#L133-L133](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L133-L133)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The official npm package is @clawplays/ospec-cli and the command is `ospec`; documented subcommands include init, change, goal, verify, finalize, session, execute, loop, docs, update, and layout migrate. -- evidence: [SKILL.md#L74-L81](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/SKILL.md#L74-L81), [README.md#L200-L202](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L200-L202), [README.md#L244-L249](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L244-L249), [README.md#L240-L242](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L240-L242), [README.md#L218-L218](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L218-L218), [README.md#L24-L24](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L24-L24), [README.md#L170-L173](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L170-L173)
  - [observation/documented] `ospec init` accepts flags such as --summary, --tech-stack, --architecture, and --document-language (en-US, zh-CN, ja-JP, or ar) to shape generated project docs. -- evidence: [README.md#L88-L99](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L88-L99), [README.md#L79-L84](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L79-L84)
- memory-state (3 claim(s)):
  - [observation/documented] Workflow state lives in repository artifacts: active changes hold proposal.md, tasks.md, state.json, verification.md, and review.md; goals add design.md, implementation-plan.md, task-graph.json, worker/reviewer/evidence artifacts, so later sessions can resume without replaying chat. -- evidence: [README.md#L39-L42](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L39-L42), [README.md#L309-L314](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L309-L314), [README.md#L214-L214](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L214-L214)
  - [observation/documented] The chosen document language is persisted in .skillrc and reused for for-ai guidance, `ospec change`, and `ospec update`; CLI language resolution falls back through explicit flag, persisted settings, existing docs, then en-US. -- evidence: [README.md#L88-L99](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L88-L99)
- orchestration (3 claim(s)):
  - [observation/documented] The goal controller dispatches native subagents per harness (Codex spawn_agent with bounded waits, Claude Code background Task polling, Gemini @generalist, OpenCode @mention), with 60-second poll boundaries, heartbeats, and immediate persistence of completed children. -- evidence: [README.md#L147-L147](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L147-L147)
  - [observation/documented] OSpec never launches agent CLIs as a fallback; if the harness lacks native subagents, executable dispatch blocks until a supported harness reports capability, and IDE controller dispatch fails clearly. -- evidence: [README.md#L147-L147](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L147-L147), [README.md#L216-L216](https://github.com/clawplays/ospec/blob/be449f2ce6986c62410a34b3bd4521d2f952a19c/README.md#L216-L216)
- tools-permissions (1 claim(s)):
More evidence: [full detail](ospec.detail.md)

Metadata and full claim list: [full detail](ospec.detail.md)
Human notes ([notes](ospec.notes.md), never overwritten by build)

[Back to map index](../../index.md)
