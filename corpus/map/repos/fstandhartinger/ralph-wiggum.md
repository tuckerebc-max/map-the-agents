# fstandhartinger/ralph-wiggum

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3f15f0fb83b8 @ e715ed74bb1d3916

## Summary (orientation draft, not independently verified)

Selected evidence records: The tool runs an iterative loop: each iteration orients from specs, picks one task, implements and tests it, verifies criteria, commits and pushes, then repeats until a DONE marker appears. The product is driven by shell scripts: ralph-loop.sh (default build mode) and an optional 'plan' mode invoked as ralph-loop.sh plan, with matching PowerShell .ps1 variants.

## Source coverage

Source coverage (partial): 3 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] Completion is gated on a magic phrase: the agent outputs <promise>DONE</promise> only when acceptance criteria are verified, tests pass, and changes are committed and pushed; the loop retries otherwise. -- evidence: [README.md#L83-L83](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L83-L83), [README.md#L282-L282](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L282-L282), [README.md#L78-L81](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L78-L81)
  - [observation/documented] Specs are expected to carry specific, testable acceptance criteria, and tests, lints, and builds act as backpressure that the agent must satisfy before signaling completion. -- evidence: [README.md#L279-L279](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L279-L279), [README.md#L148-L148](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L148-L148), [README.md#L143-L146](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L143-L146)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md and CLAUDE.md instruct contributing agents to read .specify/memory/constitution.md on every session as the single source of all project instructions, including workflow configuration and autonomy settings. -- evidence: [AGENTS.md#L3-L3](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/AGENTS.md#L3-L3), [AGENTS.md#L13-L13](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/AGENTS.md#L13-L13), [AGENTS.md#L5-L11](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/AGENTS.md#L5-L11), [CLAUDE.md#L3-L3](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/CLAUDE.md#L3-L3), [CLAUDE.md#L5-L5](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/CLAUDE.md#L5-L5)
  - [observation/documented] Repository development practice: agent instructions define context detection between Ralph-loop mode (implement specs, output the DONE promise) and interactive chat mode (guide the user, create specs). -- evidence: [AGENTS.md#L20-L22](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/AGENTS.md#L20-L22), [AGENTS.md#L31-L31](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/AGENTS.md#L31-L31), [AGENTS.md#L24-L24](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/AGENTS.md#L24-L24), [CLAUDE.md#L7-L7](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/CLAUDE.md#L7-L7), [AGENTS.md#L27-L29](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/AGENTS.md#L27-L29)
- skills-patterns (1 claim(s)):
  - [observation/documented] The repo follows the Agent Skills specification and can be installed via Vercel add-skill, OpenSkills, or Skillset, and is advertised as working with Claude Code, Cursor, Codex, Windsurf, Amp, and OpenCode. -- evidence: [README.md#L311-L311](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L311-L311), [README.md#L303-L303](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L303-L303), [README.md#L305-L309](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L305-L309)
- interfaces (2 claim(s)):
  - [observation/documented] The product is driven by shell scripts: ralph-loop.sh (default build mode) and an optional 'plan' mode invoked as ralph-loop.sh plan, with matching PowerShell .ps1 variants. -- evidence: [README.md#L94-L95](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L94-L95), [README.md#L89-L92](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L89-L92)
  - [observation/documented] Build mode can take an iteration-count argument, e.g. ralph-loop.sh 20 for a maximum of 20 iterations, or run unlimited by default. -- evidence: [README.md#L160-L163](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L160-L163)
- memory-state (2 claim(s)):
  - [observation/documented] State persists on disk between loops: IMPLEMENTATION_PLAN.md is read to pick tasks and updated with progress, while each iteration starts with a fresh context window. -- evidence: [README.md#L276-L276](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L276-L276), [README.md#L273-L273](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L273-L273), [README.md#L37-L41](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L37-L41)
  - [observation/documented] A constitution file at .specify/memory/constitution.md is described as the single source of truth for agent behavior, with optional features configured there rather than in scripts. -- evidence: [README.md#L245-L264](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L245-L264), [README.md#L266-L266](https://github.com/fstandhartinger/ralph-wiggum/blob/3f15f0fb83b8c2e0ac8d11abdae0e83ab8204981/README.md#L266-L266)
- orchestration (1 claim(s)):
More evidence: [full detail](ralph-wiggum.detail.md)

Metadata and full claim list: [full detail](ralph-wiggum.detail.md)
Human notes ([notes](ralph-wiggum.notes.md), never overwritten by build)

[Back to map index](../../index.md)
