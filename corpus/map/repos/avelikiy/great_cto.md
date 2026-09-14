# avelikiy/great_cto

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5ca5a322ac7a @ 8463cdb3ab3d551e

## Summary (orientation draft, not independently verified)

great_cto is an MIT-licensed local orchestration layer for coding agents (Claude Code, partially Codex) that runs a gated build pipeline with human approval checkpoints, a localhost board, per-agent budgets, and a second-model cross-review. Evidence is mostly README documentation plus contributor instructions in AGENTS.md/CLAUDE.md.

## Source coverage

Source coverage (partial): 3 of 217 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 17 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

17 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The system uses about 70 specialized agents with their own review gates, plus critics for architecture, spec, and schema that run before planning. -- evidence: [README.md#L232-L264](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L232-L264)
- design-choices (2 claim(s)):
  - [observation/documented] An 'approval-level' setting in .great_cto/PROJECT.md controls where the pipeline stops, from 'auto' (0 stops) through the default 'gates-only' (3 stops) to 'ship-only' (1 stop at deploy). -- evidence: [README.md#L149-L155](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L149-L155)
  - [observation/documented] The product follows a rule that a thing which did not happen must never look like one that did: missing harnesses show 'unavailable', undecidable checks show 'unverifiable', unmeasured costs show 'unmeasured', and unassessed stages show 'null'. -- evidence: [README.md#L196-L201](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L196-L201)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md mandates the bd (beads) issue tracker for all task tracking, non-interactive shell flags, and a mandatory session-completion workflow ending in a successful git push. -- evidence: [AGENTS.md#L65-L77](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/AGENTS.md#L65-L77), [AGENTS.md#L3-L3](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/AGENTS.md#L3-L3), [AGENTS.md#L24-L26](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/AGENTS.md#L24-L26), [AGENTS.md#L55-L57](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/AGENTS.md#L55-L57)
  - [observation/documented] Repository development practice: CLAUDE.md sets code style rules (TypeScript strict mode, ESM only, Node >= 20 with node: prefix, zero runtime dependencies in packages/board/server.mjs) and a commit format '<type>: <description>'. -- evidence: [CLAUDE.md#L58-L62](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/CLAUDE.md#L58-L62)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Users interact via slash commands: /start to describe a product or feature and run the pipeline, /inbox for pending gates and blocked tasks, and /digest for weekly DORA metrics and cost roll-ups. -- evidence: [README.md#L96-L100](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L96-L100)
  - [observation/documented] A web board at localhost:3141 shows Decisions, Ledger (costs), Fleet, and Harness screens, and renders never-run scans as 'n/a' rather than a green zero. -- evidence: [README.md#L66-L69](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L66-L69)
- memory-state (1 claim(s)):
  - [observation/documented] Decisions, lessons, and promoted patterns persist per project and globally across sessions, and an interrupted run resumes knowing which stages already ran. -- evidence: [README.md#L232-L264](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L232-L264)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] Agents are scope-restricted at write time: an agent is described as physically unable to touch files outside its brief, refused at write rather than flagged at review. -- evidence: [README.md#L232-L264](https://github.com/avelikiy/great_cto/blob/5ca5a322ac7a2b6ddf5b7a187c3cad2fd822698c/README.md#L232-L264)
More evidence: [full detail](great_cto.detail.md)

Metadata and full claim list: [full detail](great_cto.detail.md)
Human notes ([notes](great_cto.notes.md), never overwritten by build)

[Back to map index](../../index.md)
