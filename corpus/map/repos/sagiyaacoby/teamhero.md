# sagiyaacoby/teamhero

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 25466cdbfbcf @ d87a745d3ec5f54b

## Summary (orientation draft, not independently verified)

Evidence from README and CHANGELOG documents TeamHero as an MIT-licensed multi-agent orchestration platform with a dashboard, task lifecycle, agent memory, skills, and conflict prevention, requiring Node.js 18+ and the Claude CLI. CODE_OF_CONDUCT slices cover contributor conduct rules.

## Source coverage

Source coverage (partial): 3 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The platform includes a web dashboard for managing an agent team, a Command Center terminal for talking to an orchestrator agent, a task system with plans, versions, approvals and deliverable tracking, agent memory, a knowledge base, optional skills, and file-scope conflict prevention. -- evidence: [README.md#L23-L29](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L23-L29)
- design-choices (1 claim(s)):
  - [observation/documented] The project positions itself around managing agents rather than creating them, emphasizing plans before execution, tracked deliverables, conflict prevention, and a single source of truth for team state. -- evidence: [README.md#L35-L35](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L35-L35)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributions are welcome under guidelines in CONTRIBUTING.md, and a code of conduct adapted from the Contributor Covenant applies to issues, pull requests, and discussions, with violations reportable to conduct@myteamhero.com. -- evidence: [README.md#L86-L86](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L86-L86), [CODE_OF_CONDUCT.md#L34-L34](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/CODE_OF_CONDUCT.md#L34-L34), [CODE_OF_CONDUCT.md#L28-L28](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/CODE_OF_CONDUCT.md#L28-L28), [CODE_OF_CONDUCT.md#L24-L24](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/CODE_OF_CONDUCT.md#L24-L24)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are optional integrations such as browser automation and GitHub; the changelog also mentions a skills UI separating curated from user-installed skills and a Vercel CLI skill in the catalog. -- evidence: [CHANGELOG.md#L65-L74](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/CHANGELOG.md#L65-L74), [README.md#L23-L29](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L23-L29)
- interfaces (2 claim(s)):
  - [observation/documented] After launching via launch.bat on Windows or bash launch.sh on Mac/Linux, the dashboard is served at http://localhost:3777. -- evidence: [README.md#L75-L78](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L75-L78), [README.md#L80-L80](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L80-L80), [README.md#L70-L73](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L70-L73)
  - [observation/documented] The task lifecycle uses statuses including planning, pending_approval, working, done, and closed, with simplified transition actions (Accept, Improve, Hold, Cancel) and a done-to-closed auto-lifecycle on a 2-day timer. -- evidence: [CHANGELOG.md#L65-L74](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/CHANGELOG.md#L65-L74)
- memory-state (1 claim(s)):
  - [observation/documented] Each agent is documented to have persistent short- and long-term memory that carries across sessions. -- evidence: [CHANGELOG.md#L116-L119](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/CHANGELOG.md#L116-L119), [README.md#L23-L29](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L23-L29)
- orchestration (2 claim(s)):
  - [observation/documented] Tasks follow a plan, review, execute, and deliver lifecycle, and every file an agent will touch is declared upfront so agents do not overwrite each other's work. -- evidence: [README.md#L37-L37](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/README.md#L37-L37)
  - [observation/documented] The changelog documents autopilot scheduling with recurring and one-time timed tasks, smart model routing for cost-efficient execution, and dependency auto-triggering so tasks start when their dependencies complete. -- evidence: [CHANGELOG.md#L42-L44](https://github.com/sagiyaacoby/TeamHero/blob/25466cdbfbcf44577d78a287077aaa3a92071036/CHANGELOG.md#L42-L44)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](teamhero.detail.md)

Metadata and full claim list: [full detail](teamhero.detail.md)
Human notes ([notes](teamhero.notes.md), never overwritten by build)

[Back to map index](../../index.md)
