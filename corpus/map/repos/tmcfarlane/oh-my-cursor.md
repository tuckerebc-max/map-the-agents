# tmcfarlane/oh-my-cursor

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5bad458bff4c @ 0945cff458e1ce6e

## Summary (orientation draft, not independently verified)

The project ships 8 agent manifests, 8 slash commands, hooks, and one orchestration rule as pure Markdown/config files for Cursor, with no external runtime or wrapper CLI. The orchestrator rule makes the root thread a pure dispatcher whose only permitted tools are Task, TodoWrite, AskQuestion, and SwitchMode, delegating all work to specialist agents. Evidence coverage: 157 of 294 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project ships 8 agent manifests, 8 slash commands, hooks, and one orchestration rule as pure Markdown/config files for Cursor, with no external runtime or wrapper CLI. -- evidence: [README.md#L18-L20](https://github.com/tmcfarlane/oh-my-cursor/blob/5bad458bff4c18c470a9907c1a02ba8bf87ace90/README.md#L18-L20), [README.md#L56-L56](https://github.com/tmcfarlane/oh-my-cursor/blob/5bad458bff4c18c470a9907c1a02ba8bf87ace90/README.md#L56-L56)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Per-agent model routing uses Cursor's model: frontmatter field; the default is composer-2.5-fast, with Sokka and Iroh on claude-opus-4-8-thinking-high and Zuko on gemini-3.1-pro. -- evidence: [README.md#L223-L223](https://github.com/tmcfarlane/oh-my-cursor/blob/5bad458bff4c18c470a9907c1a02ba8bf87ace90/README.md#L223-L223), [README.md#L310-L310](https://github.com/tmcfarlane/oh-my-cursor/blob/5bad458bff4c18c470a9907c1a02ba8bf87ace90/README.md#L310-L310), [README.md#L227-L231](https://github.com/tmcfarlane/oh-my-cursor/blob/5bad458bff4c18c470a9907c1a02ba8bf87ace90/README.md#L227-L231)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors clone the repo and run bash install.sh (or install.ps1 on Windows) to install from source; changes to agents, rules, commands, or hooks take effect after reinstalling. -- evidence: [README.md#L541-L541](https://github.com/tmcfarlane/oh-my-cursor/blob/5bad458bff4c18c470a9907c1a02ba8bf87ace90/README.md#L541-L541)
- skills-patterns (1 claim(s)):
  - [observation/documented] 19 community-sourced skills are vendored in-repo as SKILL.md directories that Cursor auto-discovers, installed by default with a --no-skills option to skip them. -- evidence: [README.md#L471-L471](https://github.com/tmcfarlane/oh-my-cursor/blob/5bad458bff4c18c470a9907c1a02ba8bf87ace90/README.md#L471-L471), [README.md#L473-L474](https://github.com/tmcfarlane/oh-my-cursor/blob/5bad458bff4c18c470a9907c1a02ba8bf87ace90/README.md#L473-L474)
- interfaces (2 claim(s)):
  - [observation/documented] Slash commands map to agents: /plan (Sokka), /build (Aang), /search (Toph), /fix (Katara), /tasks (Appa), /scout (Momo), /doc (Iroh), /image (Zuko), and /cactus-juice (swarm). -- evidence: [README.md#L334-L344](https://github.com/tmcfarlane/oh-my-cursor/blob/5bad458bff4c18c470a9907c1a02ba8bf87ace90/README.md#L334-L344)
  - [observation/documented] The installer supports user (default ~/.cursor) and project (./.cursor) scopes, plus --claude/--codex cross-tool installs, --dry-run, --force, --uninstall, and --disable/--enable orchestration flags. -- evidence: [README.md#L292-L298](https://github.com/tmcfarlane/oh-my-cursor/blob/5bad458bff4c18c470a9907c1a02ba8bf87ace90/README.md#L292-L298), [README.md#L248-L257](https://github.com/tmcfarlane/oh-my-cursor/blob/5bad458bff4c18c470a9907c1a02ba8bf87ace90/README.md#L248-L257)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (3 claim(s)):
  - [observation/documented] The orchestrator rule makes the root thread a pure dispatcher whose only permitted tools are Task, TodoWrite, AskQuestion, and SwitchMode, delegating all work to specialist agents. -- evidence: [README.md#L76-L76](https://github.com/tmcfarlane/oh-my-cursor/blob/5bad458bff4c18c470a9907c1a02ba8bf87ace90/README.md#L76-L76)
  - [observation/documented] A '/cactus-juice' swarm mode decomposes requests into 5-10 independent single-file micro-tasks and spawns up to 10 parallel fast-model subagents, with the root collecting and verifying results. -- evidence: [README.md#L364-L367](https://github.com/tmcfarlane/oh-my-cursor/blob/5bad458bff4c18c470a9907c1a02ba8bf87ace90/README.md#L364-L367), [README.md#L362-L362](https://github.com/tmcfarlane/oh-my-cursor/blob/5bad458bff4c18c470a9907c1a02ba8bf87ace90/README.md#L362-L362)
- tools-permissions (2 claim(s)):
  - [observation/documented] Hooks wired via .cursor/hooks.json include guard-shell.sh, which blocks destructive shell commands and commits containing anti-patterns like 'as any' or '@ts-ignore', returning allow/deny/ask decisions on beforeShellExecution. -- evidence: [README.md#L426-L430](https://github.com/tmcfarlane/oh-my-cursor/blob/5bad458bff4c18c470a9907c1a02ba8bf87ace90/README.md#L426-L430), [README.md#L416-L419](https://github.com/tmcfarlane/oh-my-cursor/blob/5bad458bff4c18c470a9907c1a02ba8bf87ace90/README.md#L416-L419)
More evidence: [full detail](oh-my-cursor.detail.md)

Metadata and full claim list: [full detail](oh-my-cursor.detail.md)
Human notes ([notes](oh-my-cursor.notes.md), never overwritten by build)

[Back to map index](../../index.md)
