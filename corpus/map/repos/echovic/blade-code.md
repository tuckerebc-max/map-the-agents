# echovic/blade-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8917e4e0ef61 @ 4784f9b274c8ce01

## Summary (orientation draft, not independently verified)

Selected evidence records: The product ships as an interactive CLI ('blade'), a Web UI ('blade web'), a headless HTTP server ('blade serve'), non-interactive modes '--headless' with JSONL output, and a single-turn '--print' mode. In-session slash commands include /model add and /model switch, /cost, /compact, /btw for side questions, /memory list, /tasks, and /goal to start Goal mode.

## Source coverage

Source coverage (partial): 6 of 330 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repository layout places the agent core and execution loop in packages/cli/src/agent, the pi-ai adapter in services/pi, a TypeBox-based tool system, a Hono web server, and a React+Vite web UI. -- evidence: [README.md#L130-L145](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/README.md#L130-L145)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors clone the repo and run 'bun install && bun run dev' to develop locally, and a CONTRIBUTING.md guide is referenced. -- evidence: [README.md#L7-L10](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/README.md#L7-L10), [README.md#L160-L163](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/README.md#L160-L163)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are described as a dynamic prompt extension mechanism that lets the AI automatically invoke specialized capabilities based on user requests. -- evidence: [docs/guides/skills.md#L3-L3](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/guides/skills.md#L3-L3)
- interfaces (2 claim(s)):
  - [observation/documented] The product ships as an interactive CLI ('blade'), a Web UI ('blade web'), a headless HTTP server ('blade serve'), non-interactive modes '--headless' with JSONL output, and a single-turn '--print' mode. -- evidence: [README.md#L101-L111](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/README.md#L101-L111), [README.md#L69-L70](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/README.md#L69-L70)
  - [observation/documented] In-session slash commands include /model add and /model switch, /cost, /compact, /btw for side questions, /memory list, /tasks, and /goal to start Goal mode. -- evidence: [README.md#L115-L124](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/README.md#L115-L124)
- memory-state (5 claim(s)):
  - [observation/documented] Auto Memory persists project knowledge across sessions: the first 200 lines of MEMORY.md are injected into the system prompt at session start, knowledge is saved via MemoryWrite, and read on demand via MemoryRead. -- evidence: [docs/en/guides/memory.md#L3-L3](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/guides/memory.md#L3-L3), [docs/guides/memory.md#L7-L10](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/guides/memory.md#L7-L10)
  - [observation/documented] Memory files live under ~/.blade/projects/{escaped-path}/memory/ with per-project isolation, containing a MEMORY.md index plus topic files such as patterns.md, debugging.md, and architecture.md. -- evidence: [docs/en/guides/memory.md#L54-L54](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/guides/memory.md#L54-L54), [docs/guides/memory.md#L42-L49](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/guides/memory.md#L42-L49)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (4 claim(s)):
  - [observation/documented] The runtime offers four permission modes (default, autoEdit, plan, yolo); Shift+Tab cycles the first three in the TUI, while yolo requires an explicit command, launch argument, or setting. -- evidence: [docs/en/configuration/permissions.md#L17-L18](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/en/configuration/permissions.md#L17-L18), [docs/configuration/permissions.md#L17-L18](https://github.com/echoVic/blade-code/blob/8917e4e0ef6112f3cd47314e45c898284e99fd86/docs/configuration/permissions.md#L17-L18)
More evidence: [full detail](blade-code.detail.md)

Metadata and full claim list: [full detail](blade-code.detail.md)
Human notes ([notes](blade-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
