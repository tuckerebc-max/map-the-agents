---
access: public
aliases: []
claim_ids:
- clm_15fa2933e27c06a6d714e47105d6b91de091d2898f5d847455d8a4f98e0e28cb
- clm_19d82156d2fc3d870135b0b41cd29afb4535b3a1ef4fbd842e133e3376dc68bb
- clm_535e1bfb1eab9bace3ae8c248b38fb7a67f3e9f44a911fe520ad1305fce40421
- clm_694d6565274dc346fd837da59454ac7a77ec868ab0c740616abdab1ca043a6b7
- clm_801c52babd80e87168e314d0880b38a03cac435dd4c3decaff5f09a3a29f609c
- clm_8aa0e30eb1b671167cefb24112324b8f7a2653d7e081512d05752e8e8b51fc0d
- clm_961c74e6d9aced6bca3ea111c029bbc38b7782e70c1c09d365ce0b800b7b0811
- clm_be3a0061485e4445bf9f578396e641edf67870d25d0fc6ef14f1bc3a95162984
- clm_c0717e38f5552f9a7e4dd2b615590b307cc5dcc7008916ef9e81e914cdcdfa19
- clm_db101c06b220ca423ece0da336cf784530718a49b4604c5ad283184a3281a9b5
- clm_faaffa4602291bda137cbc7b1805486c72599f759b38ee556bebde40da8255c8
- clm_fb09015479d39d329ec53cea10d07167f66958c77d25402e26aacec6bd385943
maturity: draft
page_id: pg_0ca1b36c3958591b9d43eafe3a50914b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_57c50fe133b15750951cafc126703663
title: junkyard22/Orca/ARCHITECTURE.md @ 115d36b6cf51
updated_at: '2026-09-14T02:08:27Z'
---

# junkyard22/Orca/ARCHITECTURE.md @ 115d36b6cf51

<!-- rcw:begin owner=source:src_57c50fe133b15750951cafc126703663 block=evidence -->
- Task permissions can only add filesystem-write or shell capabilities, and when both fileWrite and shellExec are false the runtime removes write, shell, and github-write groups regardless of role baseline. [@claim:clm_15fa2933e27c06a6d714e47105d6b91de091d2898f5d847455d8a4f98e0e28cb]
- The desktop adapter still retains an inline agent loop as its primary path pending full unification with the shared agent-loop-core package, per the architecture doc's stated current state. [@claim:clm_19d82156d2fc3d870135b0b41cd29afb4535b3a1ef4fbd842e133e3376dc68bb]
- The desktop composer's Cargo tray accepts /repo, /file, /task, /connect, /context, /status commands plus @repo/@file/@task/@connector references, storing resources as typed references rather than raw contents. [@claim:clm_535e1bfb1eab9bace3ae8c248b38fb7a67f3e9f44a911fe520ad1305fce40421]
- The product ships two frontends: an Electron desktop GUI (settings UI, chat view, session history) and a CLI runner that accepts prompts as arguments or via stdin piping. [@claim:clm_694d6565274dc346fd837da59454ac7a77ec868ab0c740616abdab1ca043a6b7]
- Dewey persists a session-independent typed ContextManifest in ~/.orca/userContext.json storing resource locators and labels, never raw file or connector contents; raw contents load only via explicitly permitted tool calls. [@claim:clm_801c52babd80e87168e314d0880b38a03cac435dd4c3decaff5f09a3a29f609c]
- MCP servers are declared in orca-settings.json under mcpServers[] with stdio transport; by default each server's tools are namespaced with a ${id}_ prefix to avoid collisions. [@claim:clm_8aa0e30eb1b671167cefb24112324b8f7a2653d7e081512d05752e8e8b51fc0d]
- Repository development practice: ARCHITECTURE.md directs contributors to run a contract-check checklist before coding tasks touching orchestration, LLM paths, gates, QC, or role contracts, and mandates that agent-loop changes go only in packages/agent-loop-core. [@claim:clm_961c74e6d9aced6bca3ea111c029bbc38b7782e70c1c09d365ce0b800b7b0811]
- Roles include brain (decompose/route), strong_model, cheap_model, reviewer, narrator, planner_deep, debugger, reader, and vision; several roles are optional with documented fallbacks (e.g. planner_deep falls back to brain). [@claim:clm_be3a0061485e4445bf9f578396e641edf67870d25d0fc6ef14f1bc3a95162984]
- Miranda's before_tool_run gate checks calls against allowedTools and the runtime enforces taskSpec.permissions.toolsAllowed uniformly for MCP tools; filtered tools' schemas are never serialized into prompts. [@claim:clm_c0717e38f5552f9a7e4dd2b615590b307cc5dcc7008916ef9e81e914cdcdfa19]
- The runtime is organized as packages: benson-core (intent parsing), orca-core (runtime, event bus, SQLite persistence), maestro-core (role routing), pappy-core (QC verdicts), miranda-core (compliance gate), workbench-core (tool execution), and dewey-core (context store). [@claim:clm_db101c06b220ca423ece0da336cf784530718a49b4604c5ad283184a3281a9b5]
- The pipeline routes user input through Benson (intent parsing) to an Orca Runtime that orchestrates Maestro role routing, Pappy QC (PASS/WARN/FAIL), and Miranda compliance with a repair loop. [@claim:clm_faaffa4602291bda137cbc7b1805486c72599f759b38ee556bebde40da8255c8]
- Role tool access is capability-scoped: tools resolve into named groups (filesystem-read/write, shell, github-read/write, web, documentation), and unclassifiable tool names are excluded from every role with no allow-by-default fallback. [@claim:clm_fb09015479d39d329ec53cea10d07167f66958c77d25402e26aacec6bd385943]
<!-- rcw:end owner=source:src_57c50fe133b15750951cafc126703663 block=evidence -->

## Researcher notes

