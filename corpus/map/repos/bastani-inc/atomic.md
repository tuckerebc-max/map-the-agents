# bastani-inc/atomic

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ca64fa07885f @ cc096d4fbf9ff28b

## Summary (orientation draft, not independently verified)

Atomic is a TypeScript-based verifiable coding-agent runtime built around explicit workflow execution graphs, skills, and specialized subagents, distributed as an npm package or self-contained release archive. All cited evidence is documentation (README.md, DESIGN.md); no source-code slices are present in this snapshot. Evidence coverage: 126 of 262 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Workflows are authored as TypeScript workflow({...}) definitions whose stage dependencies must form a directed acyclic graph; cyclic graphs are unsupported, and loop/repair iterations must create distinct tracked work per iteration. -- evidence: [README.md#L898-L898](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L898-L898), [README.md#L958-L958](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L958-L958)
- components (1 claim(s)):
  - [observation/documented] Atomic ships three top-level building blocks: workflows, skills, and specialized subagents, with nine bundled subagent definitions such as worker, debugger, and codebase-analyzer. -- evidence: [README.md#L954-L954](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L954-L954), [README.md#L996-L1006](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L996-L1006), [README.md#L994-L994](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L994-L994)
- design-choices (1 claim(s)):
  - [observation/documented] The terminal UI uses a Catppuccin Mocha role-mapped palette with Catppuccin Blue as the sole accent, status colors mapped one-to-one to orchestrator session statuses, and Unicode-only iconography with no emoji. -- evidence: [DESIGN.md#L125-L132](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/DESIGN.md#L125-L132), [DESIGN.md#L139-L139](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/DESIGN.md#L139-L139), [DESIGN.md#L166-L166](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/DESIGN.md#L166-L166)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Atomic implements the Agent Skills standard and can use configured Claude Code or Codex skill directories without rewriting them; skills can be auto-selected from descriptions or invoked with /skill:<name>. -- evidence: [README.md#L974-L974](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L974-L974), [README.md#L351-L351](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L351-L351)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI exposes workflow management commands including /workflow list, inputs, status, connect, quit, and resume; quitting pauses a run so it can resume later. -- evidence: [README.md#L970-L970](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L970-L970)
  - [observation/documented] Non-interactive use is supported via atomic -p "<prompt>", which prints the response and exits; provider credentials are stored in ~/.atomic/agent/auth.json with owner-only permissions where the platform supports them. -- evidence: [README.md#L334-L334](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L334-L334)
- memory-state (1 claim(s)):
  - [observation/documented] Workflows persist artifacts such as plans, logs, transcripts, reviewer notes, check output, and summaries; research commonly lives in research/ and specs in specs/. -- evidence: [README.md#L1047-L1047](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L1047-L1047)
- orchestration (1 claim(s)):
  - [observation/documented] Stages can prompt an agent, run tools, call MCP servers, save artifacts, branch, retry, run in parallel, or pause for approval; specialized subagents handle focused work while a parent agent or workflow controls the larger task. -- evidence: [README.md#L894-L894](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L894-L894), [README.md#L904-L904](https://github.com/bastani-inc/atomic/blob/ca64fa07885f0a1ef2d04a99f4e682de082a9341/README.md#L904-L904)
- tools-permissions (1 claim(s)):
More evidence: [full detail](atomic.detail.md)

Metadata and full claim list: [full detail](atomic.detail.md)
Human notes ([notes](atomic.notes.md), never overwritten by build)

[Back to map index](../../index.md)
