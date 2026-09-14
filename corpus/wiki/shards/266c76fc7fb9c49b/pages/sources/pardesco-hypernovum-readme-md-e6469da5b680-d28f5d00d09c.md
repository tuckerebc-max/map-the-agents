---
access: public
aliases: []
claim_ids:
- clm_051e3f315377b23b9e8fe3bf65090e8fdb348d13bdd43e2b11e5976df52684ee
- clm_1b96dcc960e23365e78bfc048dadbbd7658a1304e0aded762729ca85b7e5dd50
- clm_200b366b3b1999a3f37be5fe40c7d50d6e12a10dfd30aa37062359155289297f
- clm_2806e6686436aa0a2edcdd29f1a1381c1ddf24c2a295291fcf6a2494a4450017
- clm_366b2bfdb4ebb46d796b737808f956301b20c4d16e8a653d8430c69829b16d02
- clm_505d8f63fec9079e5484f9bfa60ce49193e1f3c6df85502174c7c56977f80bc3
- clm_8686c668cbc29dea2fced77cdae51b5ef3650dbbab2b6a326fda929cc079d8da
- clm_98b4bf59fe92ee7111c8c22afeff2b9e362d39a71c879635b0aac74fce151282
- clm_ab340a9235558648930a5dee7f95863068977816f6789a64433067ac7dae5d26
- clm_ba216a48a59ed43f4c54b99667f3b94b94dc87032a86a988ee362ba5b09b3ea7
- clm_f8b30caa3c027d50fb9e8777ae1a91683ce5261ae48862a81728f6730b10ffb5
- clm_ff6067f92da0b04d90126e2cbaf7c510913d9e7f3005d2af7efbba900a6b2383
maturity: draft
page_id: pg_e2ce1943500c5af2a057d28f5d00d09c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ab1f4787350d59339190b7e30439b8b5
title: Pardesco/hypernovum/README.md @ e6469da5b680
updated_at: '2026-09-14T02:29:03Z'
---

# Pardesco/hypernovum/README.md @ e6469da5b680

<!-- rcw:begin owner=source:src_ab1f4787350d59339190b7e30439b8b5 block=evidence -->
- The plugin is desktop-only because its agent-ops half talks to local git and the terminal; it has no built-in AI, relying on external CLI agents that read SCHEMA.md and write frontmatter to vault notes. [@claim:clm_051e3f315377b23b9e8fe3bf65090e8fdb348d13bdd43e2b11e5976df52684ee]
- The city visualization includes a bin-packed district layout, seven procedural silhouette families, a cyberpunk shader system with bloom, CSS2D labels, hover tooltips, a central Neural Core geodesic sphere, and animated Data Arteries on file changes. [@claim:clm_1b96dcc960e23365e78bfc048dadbbd7658a1304e0aded762729ca85b7e5dd50]
- The heartbeat script is invoked as node <vault>/.hypernovum/heartbeat.js with --vault plus either --hook (reading session_id, tool_name and cwd from stdin JSON) or explicit --id/--name/--state/--file flags, and --stop to finish a session. [@claim:clm_200b366b3b1999a3f37be5fe40c7d50d6e12a10dfd30aa37062359155289297f]
- Agent integration includes an Activity Monitor polling per-session snapshots in .hypernovum/agents/, a terminal launcher for Claude Code, GPT Codex, Antigravity CLI or a custom command, and a SETUP.md context handoff written before launch. [@claim:clm_2806e6686436aa0a2edcdd29f1a1381c1ddf24c2a295291fcf6a2494a4450017]
- The plugin exposes an 'Open code city' command-palette command and a ribbon cube; the city view supports single-click select/focus, double-click to open the note, right-click menus, search/filters, scan lenses, lens presets, and EDGES chips. [@claim:clm_366b2bfdb4ebb46d796b737808f956301b20c4d16e8a653d8430c69829b16d02]
- An untagged vault renders as a whole-vault fallback (folders as districts, notes as buildings, height from incoming links); tagging one note switches the city to project mode, and the fallback only applies at zero projects. [@claim:clm_505d8f63fec9079e5484f9bfa60ce49193e1f3c6df85502174c7c56977f80bc3]
- Projects are detected by a frontmatter tag 'project' or 'type: project' (tag configurable in settings), with fields including status, priority, category, stack, tasks, questions, depends_on, blocked_by and projectDir. [@claim:clm_8686c668cbc29dea2fced77cdae51b5ef3650dbbab2b6a326fda929cc079d8da]
- The plugin is built with Three.js, Zustand, and the Obsidian Plugin API, and requires Obsidian minAppVersion 1.6.0. [@claim:clm_98b4bf59fe92ee7111c8c22afeff2b9e362d39a71c879635b0aac74fce151282]
- The plugin makes no network requests of any kind; all reads and writes are local. It runs read-only git commands in projectDir-linked folders, opens terminals only on explicit Launch agent clicks, and never reads the clipboard. [@claim:clm_ab340a9235558648930a5dee7f95863068977816f6789a64433067ac7dae5d26]
- Repository development practice: development uses npm scripts (dev, build, typecheck, vitest tests), releases are cut from the root manifest.json with check-versions.mjs mirroring versions, and CI typechecks and tests before building. [@claim:clm_ba216a48a59ed43f4c54b99667f3b94b94dc87032a86a988ee362ba5b09b3ea7]
- Heartbeat v2 writes one snapshot file per session (.hypernovum/agents/<sessionId>.json) so concurrent agents don't clobber each other; orbs are colored by state and overlapping --file values on one project surface a deterministic conflict. [@claim:clm_f8b30caa3c027d50fb9e8777ae1a91683ce5261ae48862a81728f6730b10ffb5]
- A vault mode turns the entire agent layer off — no process execution and no reads outside the vault — while the city, lenses, filters and backlink graph keep working; first run asks whether to enable the agent layer. [@claim:clm_ff6067f92da0b04d90126e2cbaf7c510913d9e7f3005d2af7efbba900a6b2383]
<!-- rcw:end owner=source:src_ab1f4787350d59339190b7e30439b8b5 block=evidence -->

## Researcher notes

