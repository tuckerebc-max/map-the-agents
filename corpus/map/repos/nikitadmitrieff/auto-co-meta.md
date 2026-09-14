# nikitadmitrieff/auto-co-meta

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5e6bb8a8765e @ 953e0670bb31dedd

## Summary (orientation draft, not independently verified)

auto-co is described as a bash loop that invokes Claude Code every two minutes, letting 14 AI agents debate, decide, build, and deploy software continuously without human supervision. Key runtime files include auto-loop.sh (the loop with monitoring, error handling, and adaptive frequency), PROMPT.md (per-cycle system prompt), memories/consensus.md, .claude/agents/*.md personas, and a Makefile of commands. Evidence coverage: 172 of 198 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] auto-co is described as a bash loop that invokes Claude Code every two minutes, letting 14 AI agents debate, decide, build, and deploy software continuously without human supervision. -- evidence: [README.md#L22-L22](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/README.md#L22-L22)
- components (1 claim(s)):
  - [observation/documented] Key runtime files include auto-loop.sh (the loop with monitoring, error handling, and adaptive frequency), PROMPT.md (per-cycle system prompt), memories/consensus.md, .claude/agents/*.md personas, and a Makefile of commands. -- evidence: [README.md#L131-L136](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/README.md#L131-L136)
- design-choices (1 claim(s)):
  - [observation/documented] The design deliberately avoids a database, server, or framework: state persists in markdown files plus git, with Claude Code as the sole dependency. -- evidence: [README.md#L138-L138](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/README.md#L138-L138), [README.md#L30-L30](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/README.md#L30-L30)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: CLAUDE.md instructs the operating agent instance to make auto-co production-ready, act autonomously without waiting for human approval, treat CEO (Bezos) as final decision-maker, and never modify safety red lines or break the loop. -- evidence: [CLAUDE.md#L42-L47](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/CLAUDE.md#L42-L47), [CLAUDE.md#L5-L5](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/CLAUDE.md#L5-L5), [CLAUDE.md#L10-L10](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/CLAUDE.md#L10-L10), [CLAUDE.md#L16-L20](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/CLAUDE.md#L16-L20)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The Makefile exposes operational commands such as make start, monitor, status, health, history, export, stop, pause, and resume, plus a Next.js dashboard runnable on port 3000. -- evidence: [docs/devops/runbook.md#L242-L245](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L242-L245), [docs/devops/runbook.md#L49-L50](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L49-L50), [docs/devops/runbook.md#L39-L42](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L39-L42), [docs/devops/runbook.md#L240-L240](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L240-L240), [README.md#L156-L162](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/README.md#L156-L162), [docs/devops/runbook.md#L62-L65](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L62-L65)
  - [observation/documented] Configuration is environment-based via .env, with documented variables including MODEL (default sonnet), LOOP_INTERVAL (120s), CYCLE_TIMEOUT_SECONDS (1800s), MAX_CONSECUTIVE_ERRORS (3), and COOLDOWN_SECONDS (300). -- evidence: [docs/devops/runbook.md#L107-L107](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L107-L107), [docs/devops/runbook.md#L109-L117](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L109-L117)
- memory-state (2 claim(s)):
  - [observation/documented] Consensus.md acts as the relay baton carrying state between cycles, written atomically via a .consensus.tmp temp file and rename, with a .bak backup restored automatically on cycle failure. -- evidence: [PROMPT.md#L47-L51](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/PROMPT.md#L47-L51), [docs/devops/runbook.md#L255-L255](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L255-L255), [docs/devops/runbook.md#L251-L253](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/devops/runbook.md#L251-L253)
  - [observation/documented] Agents append structured records to four append-only JSONL files under state/: decisions, tasks, metrics, and artifacts, each with a defined schema; these files must never be overwritten or truncated. -- evidence: [PROMPT.md#L124-L124](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/PROMPT.md#L124-L124), [docs/plans/2026-03-07-v2-improvements-design.md#L21-L21](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/plans/2026-03-07-v2-improvements-design.md#L21-L21), [docs/plans/2026-03-07-v2-improvements-design.md#L23-L26](https://github.com/NikitaDmitrieff/auto-co-meta/blob/5e6bb8a8765e10c482ba5e124bb0f2da4e6dc27e/docs/plans/2026-03-07-v2-improvements-design.md#L23-L26)
- orchestration (2 claim(s)):
More evidence: [full detail](auto-co-meta.detail.md)

Metadata and full claim list: [full detail](auto-co-meta.detail.md)
Human notes ([notes](auto-co-meta.notes.md), never overwritten by build)

[Back to map index](../../index.md)
