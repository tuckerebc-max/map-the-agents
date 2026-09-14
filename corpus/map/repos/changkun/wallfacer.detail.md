# changkun/wallfacer -- full detail

[Back to orientation](wallfacer.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/changkun/wallfacer/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/d09ab0b6a912ca08.json](../../../wiki/dossiers/changkun/wallfacer/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/d09ab0b6a912ca08.json)

## specifications (1 claim(s))

- [observation/documented] Wallfacer is described as an autonomous engineering platform spanning chat, specs, task boards, and code, with agents operating at every abstraction level. -- evidence: [README.md#L13-L13](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L13-L13) (`clm_c9015b4119d240afdb1e979a0b8fa9e0903f896d7bb8d122a978650d33311bd1`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Specs serve as an intermediate representation: ideas become structured, versioned, reviewable specs that agents reason about and implement against, rather than going straight to code. -- evidence: [README.md#L33-L33](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L33-L33) (`clm_cf60fd9a8bb028ed440145187df1d19f71fb91fb9280c99d461ecd01cd5eb738`)
- [observation/documented] Specs follow a seven-state lifecycle (vague, drafted, validated, testing, complete, plus stale and archived) with a dependency DAG and atomic dispatch and undo. -- evidence: [README.md#L95-L95](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L95-L95), [README.md#L136-L139](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L136-L139) (`clm_2590d0d49472d28229ed6c4ef24d8119fc575a6c82c05b5f8167c8f276a0ab09`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: AGENTS.md requires a reproducible test for every bug fix, frequent small-scope commits, specs before big features, and register-specific writing conventions. -- evidence: [AGENTS.md#L1-L7](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/AGENTS.md#L1-L7) (`clm_4f6c6628b2b1fe8b514869b31aa68aca62696e36f1701e4215f45975820f7f59`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI surface includes wallfacer run, status, spec, auth, web, and doctor, with -help flags per command. -- evidence: [README.md#L65-L65](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L65-L65), [README.md#L213-L219](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L213-L219) (`clm_4d7e8a9fb96c733758a26537a268fb98ee4ca072a24a45ed94a7d825483a8779`)
- [observation/documented] The planning chat exposes slash commands such as /create, /validate, /break-down, and /dispatch to drive the spec lifecycle. -- evidence: [README.md#L95-L95](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L95-L95) (`clm_de753f0d1ff4bba374e8062c9f6b6528daee48cf9897bee35ba6273f5b71b823`)
- [observation/documented] User-authored agents and fleets are defined as YAML under ~/.wallfacer/{agents,flows}/ and edited on a unified Agent Graph surface without restarting the server. -- evidence: [README.md#L108-L108](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L108-L108) (`clm_4bfb4238e3b08aa99cf002e5a6e9b312975ac82ac5e682045d97d82601c389e2`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] Execution is built from agents (sub-roles like impl, test, commit-msg, title, oversight), flows composing agents into pipelines, tasks that pick a flow, and scheduled routines. -- evidence: [README.md#L103-L106](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L103-L106) (`clm_2668981d4fdf7c9838bca14c8b85605ddd9670824ca14194522bc22c226df6a5`)
- [observation/documented] Each task runs as a host process in its own git worktree, enabling parallel agent execution without conflicts. -- evidence: [README.md#L116-L116](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L116-L116), [README.md#L35-L35](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L35-L35) (`clm_f27ed7772d5e1925479c831eab57862470a7902808d3f643a20a49a7262392ef`)

## tools-permissions (1 claim(s))

- [observation/documented] Users control agent autonomy per task, spec, or project, from fully autonomous loops (implement, test, commit, push) to stepping in at any point. -- evidence: [README.md#L31-L31](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L31-L31) (`clm_19a7406c704a6ca45244343d8b40471d776f4f4abc55eb6b864a2f93586a3ba8`)

## evaluation (1 claim(s))

- [observation/documented] The product provides oversight tooling: per-task event timelines, diffs against the default branch, AI-generated oversight summaries, and token/cost tracking by task, activity, and turn. -- evidence: [README.md#L132-L132](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L132-L132), [README.md#L126-L126](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L126-L126) (`clm_1618d0c863512ddecae3a20455489038043eb3a765d0a875b558426c5ae895ab`)

## dependencies (1 claim(s))

- [observation/documented] The product is harness-agnostic, working with Claude Code, Codex, Cursor, OpenCode, and Pi via a pluggable harness layer, and users bring their own LLM provider. -- evidence: [README.md#L15-L15](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L15-L15), [README.md#L41-L41](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L41-L41) (`clm_848c248d4a02dd987968653d4cdc6c0159b48d9a8dbdd3ca784c2588c3232755`)

## limitations (2 claim(s))

- [observation/documented] Wallfacer is pre-1.0; the HTTP API, ~/.wallfacer on-disk layout, and WALLFACER_* environment variables may change between releases, and all Go packages live under internal/ with no importable public API. -- evidence: [README.md#L213-L219](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/README.md#L213-L219) (`clm_ca4ec86b62900a295ebab566ac1baaf7f035593a2fa23cc88c55fac1ffac1f4a`)
- [observation/documented] A known bug: the OAuth redirect_uri is derived from the requested address before a port fallback, so when the configured port is taken the redirect points at a port the server is not listening on. -- evidence: [BUGS.md#L26-L29](https://github.com/changkun/wallfacer/blob/9acd2b0925789ec6d7a54a1d94feb40b8fca752f/BUGS.md#L26-L29) (`clm_9fda7d3639d1533a8f88743c2143f09e309c3d3365026758a6a294cdc8297dd6`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

