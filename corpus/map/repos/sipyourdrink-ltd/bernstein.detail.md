# sipyourdrink-ltd/bernstein -- full detail

[Back to orientation](bernstein.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/sipyourdrink-ltd/bernstein/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/fa9ff58cd4c4ac48.json](../../../wiki/dossiers/sipyourdrink-ltd/bernstein/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/fa9ff58cd4c4ac48.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] A janitor verifies task completion via concrete signals (files exist, tests pass, content matches) and moves tasks to done/ or failed/ without trusting agent claims; a separate LLM reviewer runs afterward and can push corrections back into the queue. -- evidence: [docs/architecture/ARCHITECTURE.md#L132-L132](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L132-L132), [docs/architecture/ARCHITECTURE.md#L136-L136](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L136-L136) (`clm_587f4e0bee99f1d4a569b68b5914f1ab5d931735e118a675b35b9b3bbdc01b6c`)
- [observation/documented] The Task Server is a FastAPI REST application on port 8052 exposing /tasks, /status, and /metrics, with routes split across roughly 70 modules in core/routes/ and state checkpointed to .sdd/runtime/tasks.jsonl. -- evidence: [docs/architecture/ARCHITECTURE.md#L108-L108](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L108-L108), [docs/architecture/ARCHITECTURE.md#L15-L33](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L15-L33) (`clm_1f1dc01c0820dba305326130bbf571201bdaadab1e6d52f74cd6bec1699931f9`)
- [observation/documented] A LineageSpine provides an always-on Merkle+HMAC provenance chain; every adapter artifact write routes through LineageSpine.record at a single write boundary, appending hash-chained rows to .sdd/lineage/<run_id>/spine.jsonl. -- evidence: [docs/architecture/ARCHITECTURE.md#L228-L231](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L228-L231) (`clm_30baedf91f92c1f02efc97178cb0e217e8876fe0cc41365e146b423d57b5bc55`)

## design-choices (2 claim(s))

- [observation/documented] The orchestrator is deterministic Python with no model in the coordination loop; only one planning LLM call happens up front, and the same plan replays to a byte-identical task graph. -- evidence: [README.md#L40-L40](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L40-L40), [docs/architecture/ARCHITECTURE.md#L7-L7](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L7-L7), [docs/architecture/ARCHITECTURE.md#L205-L220](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L205-L220) (`clm_86720398fff7f344e1d1b38cfcd51aed69ca2788453df3828eba6e18d87da653`)
- [observation/documented] All state is stored as files under .sdd/ with no databases or hidden memory, chosen for inspectability, recoverability, auditability, and git-friendliness; runtime state under .sdd/runtime/ is ephemeral. -- evidence: [docs/architecture/ARCHITECTURE.md#L51-L54](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L51-L54), [docs/architecture/ARCHITECTURE.md#L56-L56](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L56-L56), [docs/architecture/ARCHITECTURE.md#L49-L49](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L49-L49) (`clm_5d1e66f623075314a51fcf11be130f3b3b8a31bfd9796e1654645e763070de4f`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI surface includes bernstein init, -g, live, run plan.yaml, stop, workflow run/resume, replay/lineage/audit verification commands, and bernstein verify receipt for offline receipt checking. -- evidence: [README.md#L196-L203](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L196-L203), [README.md#L135-L140](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L135-L140), [README.md#L148-L151](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L148-L151), [README.md#L165-L175](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L165-L175), [README.md#L209-L212](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L209-L212) (`clm_bfc7ebce5ce6e4415806c3018a6a5963ee577342abc517038d699d809e1e5a1e`)
- [observation/documented] Runs are declared in YAML manifests defining phases, roles, node dependencies, conditional edges, and retry policies; workflow resume validates the manifest digest at start and refuses a changed spec. -- evidence: [README.md#L61-L68](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L61-L68), [README.md#L98-L106](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L98-L106), [README.md#L55-L55](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L55-L55), [README.md#L214-L214](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L214-L214) (`clm_24b48cfaf202ca21249154cfe5d376d482f770b9e5743a3908602581d21a96f9`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] Pluggable sandbox backends implement a SandboxBackend/SandboxSession protocol; first-party options are worktree (default), docker, e2b Firecracker microVMs, and modal serverless containers, with third parties registering via an entry-point group. -- evidence: [docs/architecture/ARCHITECTURE.md#L242-L261](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/docs/architecture/ARCHITECTURE.md#L242-L261) (`clm_f6f971e5b4d98701fbd3d303301d5dde08acb83da7ac3bfefdce9a5f55675b4c`)
- [observation/documented] Volunteer compute tasks are constrained by a volunteer.json manifest declaring sandbox backend, network allowlist, and wall-clock/memory ceilings; a donor's own limits can only narrow, never widen, the declared containment. -- evidence: [README.md#L226-L226](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L226-L226) (`clm_9a4dd64a7a3eecb1a0aed8ed6d90bf6af73529b3ec4bb9f4f62d3ec8b92780cb`)

## evaluation (1 claim(s))

- [observation/documented] bernstein bench run <suite> --reliability k (also spelled bernstein eval) runs each task k times under fixed coordination and reports a pass^k floor alongside pass@1, sealing the result in a signed receipt that can be re-verified offline. -- evidence: [README.md#L181-L181](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L181-L181) (`clm_ec6127f7c96f95933f033be31f1faa794485ef1a6cda73a9abe39dbfc7e10088`)

## dependencies (1 claim(s))

- [observation/documented] The project targets Python 3.12+ per its README badge, is published on PyPI and GHCR, and is licensed Apache-2.0. -- evidence: [README.md#L19-L28](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L19-L28), [README.md#L273-L273](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L273-L273) (`clm_13ac6865f2dc9682ee16f009703530addada0796f1539cf0d1828b475a359a66`)

## limitations (1 claim(s))

- [observation/documented] The project is beta, solo-maintained, and under active development; minor versions may change interfaces, and users are advised to pin versions. The volunteer one-command runner and the hosted api.bernstein.run service are not yet available. -- evidence: [README.md#L38-L38](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L38-L38), [README.md#L233-L233](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L233-L233), [README.md#L239-L249](https://github.com/sipyourdrink-ltd/bernstein/blob/ce5c5217c1dcf0ef9ccfb0d69d1379836f458306/README.md#L239-L249) (`clm_aacb4e5277f4c603c2fb561322cfad94c777f5c72965b6ee1da0bcf98c4c310d`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

