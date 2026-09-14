# maxkle1nz/m1nd -- full detail

[Back to orientation](m1nd.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/maxkle1nz/m1nd/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/6b14714f4ee27673.json](../../../wiki/dossiers/maxkle1nz/m1nd/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/6b14714f4ee27673.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The runtime is a single Rust binary fetched as a signed release by the npm installer package @maxkle1nz/m1nd; cargo install m1nd-mcp is an alternative. -- evidence: [README.md#L7-L7](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L7-L7), [README.md#L177-L177](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L177-L177), [README.md#L181-L181](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L181-L181), [README.md#L198-L198](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L198-L198) (`clm_d8fa316303943e746c310a035765d7ea0737813033af4f211105c458812fdaec`)

## design-choices (1 claim(s))

- [observation/documented] Everything runs locally with no telemetry, no account, and no cloud; memory is stored as plain markdown under agent-memory/ so it survives without m1nd installed. -- evidence: [README.md#L7-L7](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L7-L7), [README.md#L206-L206](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L206-L206), [README.md#L117-L117](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L117-L117) (`clm_c50ca6dafd1c03c228cdbfd6aeff4a2202c07649a4cdc341cb4e7a9653f206ed`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the demo smoke path (initialize, tools/list, trust_selftest, ingest, seek, doctor, recovery) can be run via cargo build -p m1nd-mcp and m1nd smoke --repo . --transport stdio. -- evidence: [docs/AGENT-FIRST-DEMO.md#L9-L11](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/docs/AGENT-FIRST-DEMO.md#L9-L11), [docs/AGENT-FIRST-DEMO.md#L17-L20](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/docs/AGENT-FIRST-DEMO.md#L17-L20) (`clm_4d55eb659a611af4b74522dd2291fc383938f3c836d645194c75261801371648`)

## skills-patterns (1 claim(s))

- [observation/documented] The repo ships installable agent skills (m1nd-first, m1nd-operator, a portable universal pack) teaching an OMEGA loop: north-first orientation, calibrated verdicts, memorize-at-close. -- evidence: [docs/AGENT-PACKS.md#L11-L19](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/docs/AGENT-PACKS.md#L11-L19), [docs/AGENT-PACKS.md#L94-L98](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/docs/AGENT-PACKS.md#L94-L98) (`clm_42a96c854c2af7b03e03191f219220215eed526c2cea5e17fa8acd142798a952`)

## interfaces (2 claim(s))

- [observation/documented] The MCP surface exposes verbs including impact, seek, why, north, ghost_edges, xray_gate, antibody_scan, missing, trust_selftest, and predict. -- evidence: [README.md#L53-L53](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L53-L53) (`clm_72e784b7e8fc046e68ce2ee2ff3421d210952fb1cb5aa1adefef53154043eadd`)
- [observation/documented] north(task) is described as the front door returning one orientation packet with binding trust, memory, sufficiency, next_move, and honest_gaps. -- evidence: [README.md#L152-L152](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L152-L152), [README.md#L159-L169](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L159-L169), [docs/AGENT-PACKS.md#L64-L92](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/docs/AGENT-PACKS.md#L64-L92) (`clm_41354846212bfe2d2c0eb3ddb7aa401a71744e658dfa67ed7af6273e4ed18856`)

## memory-state (2 claim(s))

- [observation/documented] Each repository gets one brain with its own graph and memory bound to a repo root; a served owner on port 1337 hosts many brains and refuses unhosted repos with a typed refusal. -- evidence: [README.md#L129-L129](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L129-L129), [README.md#L131-L136](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L131-L136) (`clm_10d099761f7f5460768fafb68fd9b14af0e1454c21eefc7185d900e9dfd95767`)
- [observation/documented] Conclusions memorized with evidence persist across sessions and agents, are flagged stale if code changed, and confirmed results reinforce edges Hebbian-style. -- evidence: [README.md#L67-L67](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L67-L67), [README.md#L171-L171](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L171-L171), [README.md#L31-L31](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L31-L31) (`clm_c6d255fff9cc69c930dcb5477ccfe7f9f6932c6071c2ac51f110f846cbd45925`)

## orchestration (2 claim(s))

- [observation/documented] Multiple agents on one repo register presences with TTLs; overlapping work triggers collision warnings in both agents' orientation packets before changes land. -- evidence: [README.md#L91-L91](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L91-L91), [README.md#L93-L98](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L93-L98) (`clm_e85e3ed4e6a2db8394ba311936c20f589e68d905f9822b8cb3c013442ae96c83`)
- [observation/documented] Mission tools (mission_start, mission_event, mission_next, mission_verify, mission_handoff, mission_close) create repo-scoped routes and budgets and reject graph-only claims. -- evidence: [docs/AGENT-PACKS.md#L100-L110](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/docs/AGENT-PACKS.md#L100-L110), [README.md#L101-L101](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L101-L101) (`clm_2552fd49b8b2ccd8c8892cf40461ac07757a8fb1118270813e2d76b7d242584c`)

## tools-permissions (1 claim(s))

- [observation/documented] xray_gate can return blocked only from a human-ratified boundary manifest; other signals arrive as warnings with reasons, and the transplant money zone fails closed server-side. -- evidence: [README.md#L75-L75](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L75-L75), [README.md#L103-L103](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L103-L103) (`clm_1cee31dc802b3e7790c8bdb275e59b7996950f3719c8f8974c81817b4bb3b61a`)

## evaluation (1 claim(s))

- [inference/documented] The docs reference benchmark artifacts and an 'm1nd-trained' loop, suggesting some benchmark evaluation exists, but no benchmark results or harness details appear in the provided evidence. -- evidence: [docs/AGENT-PACKS.md#L321-L321](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/docs/AGENT-PACKS.md#L321-L321), [docs/AGENT-PACKS.md#L94-L98](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/docs/AGENT-PACKS.md#L94-L98) (`clm_f88044cbedd83b1cd2d4aca015c09174c7b895f7313dff05bb0e8f9401dd3cc3`)

## dependencies (1 claim(s))

- [observation/documented] Release installation verifies signatures with cosign plus SHA-256 and size checks, refusing unverified paths rather than falling back. -- evidence: [README.md#L202-L202](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L202-L202), [README.md#L198-L198](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L198-L198) (`clm_041ae54109a30f0111f1cc3ff9b37b14ca3b6908a9285d3c9fc538c9075048a7`)

## limitations (2 claim(s))

- [observation/documented] Transplant v1 is documented as Rust-only, top-level fn only, same-crate, requiring an existing destination file, and blind to references born inside macros. -- evidence: [README.md#L87-L87](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L87-L87) (`clm_ba7ae6e5e0e3580a29a9a0f55ee2d4f59b6b5e24ac5c5d207ca3aab2792c50aa`)
- [observation/documented] There is no uninstall command yet; hosts plan serves as the list of what to remove by hand. -- evidence: [README.md#L198-L198](https://github.com/maxkle1nz/m1nd/blob/5e208d6ccdff03e1cf0cde982fb1866d6ae7ab2a/README.md#L198-L198) (`clm_880a355988391a86b97106740b5c21dafed99e8a07723c6bc19bfe3c1057b5b2`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

