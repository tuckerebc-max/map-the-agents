# phodal/routa -- full detail

[Back to orientation](routa.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/phodal/routa/e48861ab81e2b30378fd32f05204a3ab424c4fec/53e7bdcd26858588.json](../../../wiki/dossiers/phodal/routa/e48861ab81e2b30378fd32f05204a3ab424c4fec/53e7bdcd26858588.json)

## specifications (1 claim(s))

- [observation/documented] Routa is described as a workspace-first multi-agent coordination platform for software delivery, keeping goals, tasks, sessions, traces, evidence, and review state visible on a board rather than in one chat thread. -- evidence: [README.md#L23-L23](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L23-L23), [README.md#L7-L7](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L7-L7) (`clm_5ee473c51bfe5e67818cdde7ebbe30a87126f3433c6b2d4e37c533a57556b84c`)

## components (2 claim(s))

- [observation/documented] The implementation is intentionally dual-backend: a Next.js web app in src/, a Tauri desktop shell backed by an Axum server in crates/routa-server, sharing semantics defined by api-contract.yaml. -- evidence: [README.md#L47-L47](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L47-L47), [README.md#L49-L52](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L49-L52) (`clm_38a6d9c7056885d8526445cbb1fb0b6aafbaa10f2cc8c884805403277a8bbfeb`)
- [observation/documented] Repository map includes crates/routa-core (shared Rust runtime foundation), crates/routa-cli (CLI entrypoints and ACP serving), and crates/harness-monitor (run observation and operator-facing harness monitor). -- evidence: [README.md#L231-L244](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L231-L244) (`clm_cd8623e22d4b5467b9d32111b6fb11424b31d8a09601ae0199645abfff5ddc2b`)

## design-choices (2 claim(s))

- [observation/documented] Each downstream lane is deliberately stricter than the previous one; cards accumulate artifacts (story YAML, execution brief, dev evidence, review verdict, completion summary) as they move forward. -- evidence: [README.md#L108-L108](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L108-L108), [README.md#L110-L114](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L110-L114), [README.md#L116-L116](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L116-L116), [README.md#L77-L77](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L77-L77) (`clm_cac67e64e405953ff060de1a04427ac8c3a78ae6608a1d73bd2708a48ef0f881`)
- [observation/documented] The review gate is a stacked decision path with three layers: Harness Monitor (what happened), Entrix Fitness (what should be true, hard gates and evidence requirements), and Gate Specialist (whether the card can move). -- evidence: [README.md#L60-L62](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L60-L62), [README.md#L58-L58](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L58-L58) (`clm_ee5e3b746d38d78181ea6990be01595949421d4a1d729363f5cd049499a23f54`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors must run entrix validation before PR using docs/fitness/README.md as the canonical rulebook, with tiers fast and normal, and build via cargo build -p entrix. -- evidence: [AGENTS.md#L41-L41](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/AGENTS.md#L41-L41), [AGENTS.md#L43-L47](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/AGENTS.md#L43-L47), [AGENTS.md#L49-L51](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/AGENTS.md#L49-L51) (`clm_952115dfe6cd75f7ad3c372b404ec9c77686c9fc4d1eddd72194dcdbf59750c2`)
- [observation/documented] Repository development practice: commits must follow Conventional Commits with one concern per commit, under 10 files and 1000 changed lines, exactly one co-author line, and UI PRs should include screenshots or recordings. -- evidence: [AGENTS.md#L64-L66](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/AGENTS.md#L64-L66), [AGENTS.md#L82-L83](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/AGENTS.md#L82-L83), [AGENTS.md#L57-L60](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/AGENTS.md#L57-L60) (`clm_34a75e150c9bc04939dbbc2d67eda5a741d7e21963d839e501db193a6c732e2f`)

## skills-patterns (1 claim(s))

- [observation/documented] Built-in lane prompts live under resources/specialists/workflows/kanban/*.yaml, and core role prompts (routa, crafter, gate) under resources/specialists/core/. -- evidence: [README.md#L124-L124](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L124-L124) (`clm_57d083d4ae653f8acbbbe7de9eaa2400a2a87243c6aee1c97555ee073279f11d`)

## interfaces (2 claim(s))

- [observation/documented] Integration surfaces listed include ACP, MCP, A2A, AG-UI, A2UI, REST, and SSE. -- evidence: [README.md#L49-L52](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L49-L52) (`clm_d11b0ec7559c88ef159c25f0445fa0562d4e978d624bdc1668358fac7f975d08`)
- [observation/documented] The CLI is distributed as routa-cli on npm and crates.io, with commands such as routa --help, routa acp list, and routa workspace list. -- evidence: [README.md#L173-L177](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L173-L177), [README.md#L9-L15](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L9-L15) (`clm_22916abf5c50d08ac92b0f56e6f60002200e80c9147cdda686877440656a4818`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Work flows through Kanban lanes Backlog, Todo, Dev, Review, Done, each backed by a specialist prompt (Backlog Refiner, Todo Orchestrator, Dev Crafter, Review Guard, Done Reporter), with a Blocked Resolver for blocked work. -- evidence: [README.md#L66-L75](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L66-L75), [README.md#L77-L77](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L77-L77), [README.md#L86-L93](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L86-L93) (`clm_6490c16d69edc7484e597dc3cf3403030a9a20783b848c953a1669955b758e5d`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Badges indicate TypeScript 5.9, Next.js 16.2, and Rust with Axum; the project is MIT licensed. -- evidence: [README.md#L259-L259](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L259-L259), [README.md#L9-L15](https://github.com/phodal/routa/blob/e48861ab81e2b30378fd32f05204a3ab424c4fec/README.md#L9-L15) (`clm_df0add6a4692c86d54c96c19f328dd61f4469d558a075367d6c3ec3c471980df`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

