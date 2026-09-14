# nicepkg/auto-company

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 125292073565 @ 3916683b1363d27f

## Summary (orientation draft, not independently verified)

The product is described as a fully autonomous AI company of 14 agents that conceives products, makes decisions, writes code, deploys, and markets with no human involvement, driven by Claude Code Agent Teams. A launchd-managed auto-loop.sh runs an endless cycle: read PROMPT.md and consensus.md, drive one work period via `claude -p`, then handle failures (rate-limit waits, circuit breaker, consensus rollback) and sleep before the next round.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The product is described as a fully autonomous AI company of 14 agents that conceives products, makes decisions, writes code, deploys, and markets with no human involvement, driven by Claude Code Agent Teams. -- evidence: [README.md#L7-L8](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L7-L8), [README.md#L10-L10](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L10-L10)
- components (1 claim(s)):
  - [observation/documented] The repo ships 14 agent persona definitions under .claude/agents (e.g. ceo-bezos, cto-vogels, critic-munger, fullstack-dhh, qa-bach, devops-hightower, cfo-campbell, research-thompson) plus 30+ skills under .claude/skills. -- evidence: [README.md#L47-L62](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L47-L62), [README.md#L64-L64](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L64-L64), [README.md#L175-L193](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L175-L193), [CLAUDE.md#L37-L37](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/CLAUDE.md#L37-L37)
- design-choices (2 claim(s)):
  - [observation/documented] Agents are prompted as real-world luminaries (e.g. 'you are DHH' rather than 'you are a developer') to activate the LLM's deep domain knowledge, and the charter sets decision principles like Ship > Plan > Discuss and monolith-first boring technology. -- evidence: [README.md#L45-L45](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L45-L45), [CLAUDE.md#L80-L86](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/CLAUDE.md#L80-L86)
  - [inference/documented] Human steering appears to be intentionally limited to editing the 'Next Action' in memories/consensus.md (plus pause/resume), since the charter says humans guide direction only through that file while everything else stays autonomous. -- evidence: [README.md#L143-L148](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L143-L148), [CLAUDE.md#L17-L17](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/CLAUDE.md#L17-L17)
- workflows (1 claim(s)):
  - [observation/documented] Six standard collaboration chains are defined (new product evaluation, feature development, launch, pricing, weekly review, opportunity discovery), and convergence rules force concrete output: cycle 1 brainstorm, cycle 2 GO/NO-GO pre-mortem, and from cycle 3 onward pure discussion is forbidden. -- evidence: [README.md#L130-L137](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L130-L137), [PROMPT.md#L61-L65](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/PROMPT.md#L61-L65), [CLAUDE.md#L92-L97](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/CLAUDE.md#L92-L97), [README.md#L122-L126](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L122-L126)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Users control the loop through make targets: start, start-awake, stop, status, monitor, last, cycles, awake, install/uninstall (launchd daemon), pause, and resume. -- evidence: [README.md#L87-L101](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L87-L101)
- memory-state (1 claim(s)):
  - [observation/documented] Each cycle is an independent `claude -p` call, and memories/consensus.md is stated to be the only cross-cycle state, like a relay baton; the prompt requires updating it before each cycle ends with fields such as Current Phase, Key Decisions, Active Projects, Next Action, and Company State. -- evidence: [PROMPT.md#L26-L26](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/PROMPT.md#L26-L26), [README.md#L41-L41](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L41-L41), [PROMPT.md#L44-L44](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/PROMPT.md#L44-L44), [PROMPT.md#L47-L47](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/PROMPT.md#L47-L47), [PROMPT.md#L35-L35](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/PROMPT.md#L35-L35), [PROMPT.md#L50-L53](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/PROMPT.md#L50-L53)
- orchestration (1 claim(s)):
More evidence: [full detail](auto-company.detail.md)

Metadata and full claim list: [full detail](auto-company.detail.md)
Human notes ([notes](auto-company.notes.md), never overwritten by build)

[Back to map index](../../index.md)
