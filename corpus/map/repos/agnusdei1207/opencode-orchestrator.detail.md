# agnusdei1207/opencode-orchestrator -- full detail

[Back to orientation](opencode-orchestrator.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/agnusdei1207/opencode-orchestrator/572c7bef8ca00788bb4b986292558e6344681b39/f055556af9cc5147.json](../../../wiki/dossiers/agnusdei1207/opencode-orchestrator/572c7bef8ca00788bb4b986292558e6344681b39/f055556af9cc5147.json)

## specifications (1 claim(s))

- [observation/documented] OpenCode Orchestrator is an MIT-licensed npm package (opencode-orchestrator) at version 1.7.17, described as multi-agent mission control for OpenCode with four agent roles. -- evidence: [README.md#L192-L192](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L192-L192), [README.md#L6-L14](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L6-L14), [README.md#L33-L35](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L33-L35), [README.md#L1-L4](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L1-L4) (`clm_550ede2b76eb3a639a2676d9d0646c05a3f514ada8f4a8c5e1e969a2f5032dc7`)

## components (2 claim(s))

- [observation/documented] The architecture defines four agents: Commander (orchestrates missions and loop state), Planner (orders file-level tasks), Worker (isolated TDD edits), and Reviewer (verifies test evidence and builds). -- evidence: [README.md#L156-L161](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L156-L161) (`clm_4cccb0839fb0030b547acebb00d394882f4a00927ac4ff178f986e7b87911777`)
- [observation/documented] A bundled Rust CLI provides an optional multi-session TCP shell listener TUI for authorized testing environments, invoked as orchestrator shell-listener with --bind and --port flags. -- evidence: [README.md#L169-L171](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L169-L171), [README.md#L167-L167](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L167-L167) (`clm_142959b40873bf1780db22802ccd05deabbb1eac7acb41c77c8f3d6aa03a604c`)

## design-choices (1 claim(s))

- [observation/documented] Memory is local-first: an on-disk Ebbinghaus decay model combining BM25, tags, and graph connections, explicitly avoiding external vector databases. -- evidence: [docs/adr/0001-second-brain-knowledge-graph-rag.md#L9-L11](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/docs/adr/0001-second-brain-knowledge-graph-rag.md#L9-L11), [README.md#L24-L27](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L24-L27) (`clm_4079e9a5f95e0f3a68aeaa244c07444fee8c706f7b4003a5a4b6cf4148ffcd16`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors verify the TypeScript side with npm run build, npx tsc --noEmit, and npm test, and the Rust side with cargo test --workspace plus clippy with -D warnings. -- evidence: [README.md#L184-L186](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L184-L186), [README.md#L179-L181](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L179-L181) (`clm_3c99fbdc92be9da27c0f27f88a0f16cafcf6c8d79fb973e51790cfaf381965cc`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Users start a mission with /task <objective>, halt it with /stop or /cancel, and pause loop continuation with Esc interrupt; missions persist under .opencode/. -- evidence: [README.md#L112-L116](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L112-L116), [README.md#L108-L110](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L108-L110) (`clm_d591cc9ad2d9be8715ff3625b17813939ba929df41d0cb128a12d335cf4829d5`)
- [observation/documented] Plugin options include per-agent concurrency limits (commander, planner, worker, reviewer) and missionLoop toggles for ledger and markdownMemory, configured in opencode.jsonc. -- evidence: [README.md#L75-L96](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L75-L96) (`clm_41133572ef6271fd9d303657818fc1ba77699a88ed22e07ec8da62460df96c7d`)
- [observation/documented] The npm install hook automatically registers the plugin in opencode.json or opencode.jsonc, and a cleanup:plugin script exists for removal before uninstalling. -- evidence: [README.md#L64-L67](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L64-L67), [README.md#L37-L37](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L37-L37) (`clm_c8c2f278665120378adb7d10eddff598ed0a1fb289a0d7309d00dc19dd6abf35`)
- [observation/documented] Subagents inherit the primary agent's model unless agent.<name>.model is set, and context-window alerts use the window OpenCode reports for the active model, overridable via a contextMaxTokens integer option. -- evidence: [README.md#L98-L100](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/README.md#L98-L100) (`clm_0e4916e227129b564798719821fdf45f20a4444b2390eb7a2ece73d60ccdb77f`)

## memory-state (1 claim(s))

- [observation/documented] Mission-loop state is synced to markdown notes such as scratchpad.md, knowledge-map.canvas, and episodic notes, which were made self-contained with a lightweight inline frontmatter parser. -- evidence: [AGENT_MEMORY.md#L38-L40](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/AGENT_MEMORY.md#L38-L40), [AGENT_MEMORY.md#L11-L29](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/AGENT_MEMORY.md#L11-L29) (`clm_e679a07acdc5d75945d27c248aefa8379dc9f72c9ea91efb4fbee202bad0fe71`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] ADR-0001 established a constraint of no GPU, no external model, and no external API, keeping the knowledge plane CPU-only and local. -- evidence: [docs/adr/0001-second-brain-knowledge-graph-rag.md#L23-L26](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/docs/adr/0001-second-brain-knowledge-graph-rag.md#L23-L26) (`clm_68bea434bb774ec6fbf41c2092ccdf970c965cb65b40e25e2843c39c2ed9d326`)

## limitations (1 claim(s))

- [inference/documented] The Knowledge Search deep-dive documents a BM25/tag/graph RRF pipeline, but AGENT_MEMORY states all 14 knowledge RAG modules were deleted per ADR-0019, so that documented pipeline likely no longer exists in the current version. -- evidence: [docs/KNOWLEDGE-SEARCH-DEEP-DIVE.md#L87-L98](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/docs/KNOWLEDGE-SEARCH-DEEP-DIVE.md#L87-L98), [AGENT_MEMORY.md#L11-L29](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/AGENT_MEMORY.md#L11-L29), [docs/KNOWLEDGE-SEARCH-DEEP-DIVE.md#L3-L5](https://github.com/agnusdei1207/opencode-orchestrator/blob/572c7bef8ca00788bb4b986292558e6344681b39/docs/KNOWLEDGE-SEARCH-DEEP-DIVE.md#L3-L5) (`clm_add84c8bc349ce6124a5d44d071b691113167c8e407b272f1f2fdc24946b3fb9`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

