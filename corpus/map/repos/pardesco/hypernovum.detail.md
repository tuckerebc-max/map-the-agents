# pardesco/hypernovum -- full detail

[Back to orientation](hypernovum.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/pardesco/hypernovum/e6469da5b6805965e696379c433b2fef4a068296/be1c689a4163012b.json](../../../wiki/dossiers/pardesco/hypernovum/e6469da5b6805965e696379c433b2fef4a068296/be1c689a4163012b.json)

## specifications (1 claim(s))

- [observation/documented] Projects are detected by a frontmatter tag 'project' or 'type: project' (tag configurable in settings), with fields including status, priority, category, stack, tasks, questions, depends_on, blocked_by and projectDir. -- evidence: [README.md#L144-L154](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L144-L154), [README.md#L141-L142](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L141-L142), [README.md#L27-L36](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L27-L36) (`clm_8686c668cbc29dea2fced77cdae51b5ef3650dbbab2b6a326fda929cc079d8da`)

## components (2 claim(s))

- [observation/documented] The city visualization includes a bin-packed district layout, seven procedural silhouette families, a cyberpunk shader system with bloom, CSS2D labels, hover tooltips, a central Neural Core geodesic sphere, and animated Data Arteries on file changes. -- evidence: [README.md#L71-L75](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L71-L75), [README.md#L6-L9](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L6-L9), [README.md#L105-L107](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L105-L107) (`clm_1b96dcc960e23365e78bfc048dadbbd7658a1304e0aded762729ca85b7e5dd50`)
- [observation/documented] Agent integration includes an Activity Monitor polling per-session snapshots in .hypernovum/agents/, a terminal launcher for Claude Code, GPT Codex, Antigravity CLI or a custom command, and a SETUP.md context handoff written before launch. -- evidence: [README.md#L110-L115](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L110-L115) (`clm_2806e6686436aa0a2edcdd29f1a1381c1ddf24c2a295291fcf6a2494a4450017`)

## design-choices (1 claim(s))

- [observation/documented] An untagged vault renders as a whole-vault fallback (folders as districts, notes as buildings, height from incoming links); tagging one note switches the city to project mode, and the fallback only applies at zero projects. -- evidence: [CHANGELOG.md#L84-L88](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/CHANGELOG.md#L84-L88), [README.md#L22-L25](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L22-L25) (`clm_505d8f63fec9079e5484f9bfa60ce49193e1f3c6df85502174c7c56977f80bc3`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: development uses npm scripts (dev, build, typecheck, vitest tests), releases are cut from the root manifest.json with check-versions.mjs mirroring versions, and CI typechecks and tests before building. -- evidence: [README.md#L217-L220](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L217-L220), [README.md#L209-L215](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L209-L215), [CHANGELOG.md#L204-L213](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/CHANGELOG.md#L204-L213) (`clm_ba216a48a59ed43f4c54b99667f3b94b94dc87032a86a988ee362ba5b09b3ea7`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The plugin exposes an 'Open code city' command-palette command and a ribbon cube; the city view supports single-click select/focus, double-click to open the note, right-click menus, search/filters, scan lenses, lens presets, and EDGES chips. -- evidence: [README.md#L88-L98](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L88-L98), [README.md#L15-L16](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L15-L16) (`clm_366b2bfdb4ebb46d796b737808f956301b20c4d16e8a653d8430c69829b16d02`)
- [observation/documented] The heartbeat script is invoked as node <vault>/.hypernovum/heartbeat.js with --vault plus either --hook (reading session_id, tool_name and cwd from stdin JSON) or explicit --id/--name/--state/--file flags, and --stop to finish a session. -- evidence: [README.md#L176-L179](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L176-L179), [README.md#L192-L193](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L192-L193), [README.md#L183-L184](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L183-L184), [README.md#L187-L189](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L187-L189) (`clm_200b366b3b1999a3f37be5fe40c7d50d6e12a10dfd30aa37062359155289297f`)

## memory-state (1 claim(s))

- [observation/documented] Heartbeat v2 writes one snapshot file per session (.hypernovum/agents/<sessionId>.json) so concurrent agents don't clobber each other; orbs are colored by state and overlapping --file values on one project surface a deterministic conflict. -- evidence: [README.md#L195-L201](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L195-L201) (`clm_f8b30caa3c027d50fb9e8777ae1a91683ce5261ae48862a81728f6730b10ffb5`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] The plugin makes no network requests of any kind; all reads and writes are local. It runs read-only git commands in projectDir-linked folders, opens terminals only on explicit Launch agent clicks, and never reads the clipboard. -- evidence: [README.md#L50-L51](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L50-L51), [README.md#L53-L62](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L53-L62) (`clm_ab340a9235558648930a5dee7f95863068977816f6789a64433067ac7dae5d26`)
- [observation/documented] A vault mode turns the entire agent layer off — no process execution and no reads outside the vault — while the city, lenses, filters and backlink graph keep working; first run asks whether to enable the agent layer. -- evidence: [README.md#L64-L66](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L64-L66), [CHANGELOG.md#L176-L188](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/CHANGELOG.md#L176-L188) (`clm_ff6067f92da0b04d90126e2cbaf7c510913d9e7f3005d2af7efbba900a6b2383`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The plugin is built with Three.js, Zustand, and the Obsidian Plugin API, and requires Obsidian minAppVersion 1.6.0. -- evidence: [README.md#L222-L222](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L222-L222), [CHANGELOG.md#L176-L188](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/CHANGELOG.md#L176-L188) (`clm_98b4bf59fe92ee7111c8c22afeff2b9e362d39a71c879635b0aac74fce151282`)

## limitations (1 claim(s))

- [observation/documented] The plugin is desktop-only because its agent-ops half talks to local git and the terminal; it has no built-in AI, relying on external CLI agents that read SCHEMA.md and write frontmatter to vault notes. -- evidence: [README.md#L18-L18](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L18-L18), [README.md#L164-L164](https://github.com/Pardesco/hypernovum/blob/e6469da5b6805965e696379c433b2fef4a068296/README.md#L164-L164) (`clm_051e3f315377b23b9e8fe3bf65090e8fdb348d13bdd43e2b11e5976df52684ee`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

