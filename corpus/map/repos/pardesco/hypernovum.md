# pardesco/hypernovum

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e6469da5b680 @ be1c689a4163012b

## Summary (orientation draft, not independently verified)

Selected evidence records: Projects are detected by a frontmatter tag 'project' or 'type: project' (tag configurable in settings), with fields including status, priority, category, stack, tasks, questions, depends_on, blocked_by and projectDir. The plugin exposes an 'Open code city' command-palette command and a ribbon cube; the city view supports single-click select/focus, double-click to open the note, right-click menus, search/filters, scan lenses, lens presets, and EDGES chips.

## Source coverage

Source coverage (partial): 3 of 20 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Projects are detected by a frontmatter tag 'project' or 'type: project' (tag configurable in settings), with fields including status, priority, category, stack, tasks, questions, depends_on, blocked_by and projectDir. -- evidence: [README.md#L144-L154](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L144-L154), [README.md#L141-L142](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L141-L142), [README.md#L27-L36](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L27-L36)
- components (2 claim(s)):
  - [observation/documented] The city visualization includes a bin-packed district layout, seven procedural silhouette families, a cyberpunk shader system with bloom, CSS2D labels, hover tooltips, a central Neural Core geodesic sphere, and animated Data Arteries on file changes. -- evidence: [README.md#L71-L75](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L71-L75), [README.md#L6-L9](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L6-L9), [README.md#L105-L107](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L105-L107)
  - [observation/documented] Agent integration includes an Activity Monitor polling per-session snapshots in .hypernovum/agents/, a terminal launcher for Claude Code, GPT Codex, Antigravity CLI or a custom command, and a SETUP.md context handoff written before launch. -- evidence: [README.md#L110-L115](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L110-L115)
- design-choices (1 claim(s)):
  - [observation/documented] An untagged vault renders as a whole-vault fallback (folders as districts, notes as buildings, height from incoming links); tagging one note switches the city to project mode, and the fallback only applies at zero projects. -- evidence: [CHANGELOG.md#L84-L88](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/CHANGELOG.md#L84-L88), [README.md#L22-L25](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L22-L25)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: development uses npm scripts (dev, build, typecheck, vitest tests), releases are cut from the root manifest.json with check-versions.mjs mirroring versions, and CI typechecks and tests before building. -- evidence: [README.md#L217-L220](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L217-L220), [README.md#L209-L215](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L209-L215), [CHANGELOG.md#L204-L213](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/CHANGELOG.md#L204-L213)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The plugin exposes an 'Open code city' command-palette command and a ribbon cube; the city view supports single-click select/focus, double-click to open the note, right-click menus, search/filters, scan lenses, lens presets, and EDGES chips. -- evidence: [README.md#L88-L98](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L88-L98), [README.md#L15-L16](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L15-L16)
  - [observation/documented] The heartbeat script is invoked as node <vault>/.hypernovum/heartbeat.js with --vault plus either --hook (reading session_id, tool_name and cwd from stdin JSON) or explicit --id/--name/--state/--file flags, and --stop to finish a session. -- evidence: [README.md#L176-L179](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L176-L179), [README.md#L192-L193](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L192-L193), [README.md#L183-L184](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L183-L184), [README.md#L187-L189](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L187-L189)
- memory-state (1 claim(s)):
More evidence: [full detail](hypernovum.detail.md)

Metadata and full claim list: [full detail](hypernovum.detail.md)
Human notes ([notes](hypernovum.notes.md), never overwritten by build)

[Back to map index](../../index.md)
