---
access: public
aliases: []
claim_ids:
- clm_0e4916e227129b564798719821fdf45f20a4444b2390eb7a2ece73d60ccdb77f
- clm_142959b40873bf1780db22802ccd05deabbb1eac7acb41c77c8f3d6aa03a604c
- clm_3c99fbdc92be9da27c0f27f88a0f16cafcf6c8d79fb973e51790cfaf381965cc
- clm_4079e9a5f95e0f3a68aeaa244c07444fee8c706f7b4003a5a4b6cf4148ffcd16
- clm_41133572ef6271fd9d303657818fc1ba77699a88ed22e07ec8da62460df96c7d
- clm_4cccb0839fb0030b547acebb00d394882f4a00927ac4ff178f986e7b87911777
- clm_550ede2b76eb3a639a2676d9d0646c05a3f514ada8f4a8c5e1e969a2f5032dc7
- clm_c8c2f278665120378adb7d10eddff598ed0a1fb289a0d7309d00dc19dd6abf35
- clm_d591cc9ad2d9be8715ff3625b17813939ba929df41d0cb128a12d335cf4829d5
maturity: draft
page_id: pg_973aadf123b9595a8eb4ece93e8b1aa1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_80d4998ef6cd5ba6a6d0b958e8d0ec75
title: agnusdei1207/opencode-orchestrator/README.md @ 572c7bef8ca0
updated_at: '2026-09-14T03:31:50Z'
---

# agnusdei1207/opencode-orchestrator/README.md @ 572c7bef8ca0

<!-- rcw:begin owner=source:src_80d4998ef6cd5ba6a6d0b958e8d0ec75 block=evidence -->
- Subagents inherit the primary agent's model unless agent.<name>.model is set, and context-window alerts use the window OpenCode reports for the active model, overridable via a contextMaxTokens integer option. [@claim:clm_0e4916e227129b564798719821fdf45f20a4444b2390eb7a2ece73d60ccdb77f]
- A bundled Rust CLI provides an optional multi-session TCP shell listener TUI for authorized testing environments, invoked as orchestrator shell-listener with --bind and --port flags. [@claim:clm_142959b40873bf1780db22802ccd05deabbb1eac7acb41c77c8f3d6aa03a604c]
- Repository development practice: contributors verify the TypeScript side with npm run build, npx tsc --noEmit, and npm test, and the Rust side with cargo test --workspace plus clippy with -D warnings. [@claim:clm_3c99fbdc92be9da27c0f27f88a0f16cafcf6c8d79fb973e51790cfaf381965cc]
- Memory is local-first: an on-disk Ebbinghaus decay model combining BM25, tags, and graph connections, explicitly avoiding external vector databases. [@claim:clm_4079e9a5f95e0f3a68aeaa244c07444fee8c706f7b4003a5a4b6cf4148ffcd16]
- Plugin options include per-agent concurrency limits (commander, planner, worker, reviewer) and missionLoop toggles for ledger and markdownMemory, configured in opencode.jsonc. [@claim:clm_41133572ef6271fd9d303657818fc1ba77699a88ed22e07ec8da62460df96c7d]
- The architecture defines four agents: Commander (orchestrates missions and loop state), Planner (orders file-level tasks), Worker (isolated TDD edits), and Reviewer (verifies test evidence and builds). [@claim:clm_4cccb0839fb0030b547acebb00d394882f4a00927ac4ff178f986e7b87911777]
- OpenCode Orchestrator is an MIT-licensed npm package (opencode-orchestrator) at version 1.7.17, described as multi-agent mission control for OpenCode with four agent roles. [@claim:clm_550ede2b76eb3a639a2676d9d0646c05a3f514ada8f4a8c5e1e969a2f5032dc7]
- The npm install hook automatically registers the plugin in opencode.json or opencode.jsonc, and a cleanup:plugin script exists for removal before uninstalling. [@claim:clm_c8c2f278665120378adb7d10eddff598ed0a1fb289a0d7309d00dc19dd6abf35]
- Users start a mission with /task <objective>, halt it with /stop or /cancel, and pause loop continuation with Esc interrupt; missions persist under .opencode/. [@claim:clm_d591cc9ad2d9be8715ff3625b17813939ba929df41d0cb128a12d335cf4829d5]
<!-- rcw:end owner=source:src_80d4998ef6cd5ba6a6d0b958e8d0ec75 block=evidence -->

## Researcher notes

