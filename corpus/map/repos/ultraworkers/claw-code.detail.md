# ultraworkers/claw-code -- full detail

[Back to orientation](claw-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ultraworkers/claw-code/08106b0c3771ef5b4a5aa176acccd460e88b7325/3672b0345a23b5ad.json](../../../wiki/dossiers/ultraworkers/claw-code/08106b0c3771ef5b4a5aa176acccd460e88b7325/3672b0345a23b5ad.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The Rust workspace contains the main `claw` CLI (rusty-claude-cli), an `api` crate for provider clients and streaming, a `runtime` crate with sessions and permission policy/enforcer, a `tools` crate, `claw-analog`, and `claw-rag-service`. -- evidence: [concept.md#L74-L80](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L74-L80) (`clm_45ee35485f6fb08a9641f7fdbf320af99e88e35f867ef8d8b5e0bbd13b749fb8`)
- [observation/documented] claw-rag-service is a separate process that indexes a repository into SQLite chunks plus embeddings and exposes an HTTP API with routes including /, /health, /v1/stats, and /v1/query, plus a minimal web UI. -- evidence: [concept.md#L13-L15](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L13-L15), [concept.md#L74-L80](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L74-L80) (`clm_f9faca4de03ad88168dcc7b9fdfda5a72ca44e8f2328f8aad9de107c44c51907`)

## design-choices (1 claim(s))

- [observation/documented] Heavy indexing and embedding storage are deliberately kept out of claw-analog; the agent only calls retrieval over HTTP so the vector store and embedding secrets can be scaled or changed independently. -- evidence: [concept.md#L57-L57](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L57-L57) (`clm_27fb9b7b9870be1372716dbbee667b3005fdc2cd0a72ba2618c32c9873d04939`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README instructs building from source via `cargo build --workspace` in rust/, warns against `cargo install claw-code` (a deprecated stub), and says to run `cargo test --workspace` after verifying the binary. -- evidence: [README.md#L263-L263](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/README.md#L263-L263), [README.md#L125-L127](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/README.md#L125-L127), [README.md#L115-L121](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/README.md#L115-L121), [README.md#L265-L268](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/README.md#L265-L268) (`clm_b63bdd1252f44f770530105f49c0abbb4468ec8bede2531f73554ade123d25a2`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The main `claw` CLI is described as a full agent with a REPL, OAuth, an extended toolset including bash, MCP and plugins, streaming, and integration with Anthropic, OpenAI-compatible, and xAI providers. -- evidence: [concept.md#L13-L15](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L13-L15) (`clm_b59504dbc6a2e2fc2c5b091b4799ff2ae0f423adfcf2c99403f04520f9ca65fb`)
- [observation/documented] claw-analog is a lean agent on the same API layer with a narrow filesystem-only toolset (read_file, list_dir, glob_workspace, grep_workspace, git_diff, git_log, optional write_file and retrieve_context) and no arbitrary shell, MCP, or plugins. -- evidence: [concept.md#L13-L15](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L13-L15), [how_to_run.md#L180-L190](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L180-L190), [concept.md#L92-L92](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L92-L92), [concept.md#L90-L90](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L90-L90) (`clm_c3d8e4b253000de701b7c2fc4ab91385f78dcb218ff881074ae495b0471d9843`)
- [observation/documented] claw-analog exposes subcommands including doctor (config preview, env status, workspace search, optional build, TCP ping), config validate (offline TOML/profile check with --strict), and complete for shell completion in bash, zsh, fish, and powershell. -- evidence: [how_to_run.md#L43-L43](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L43-L43), [how_to_run.md#L22-L22](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L22-L22), [how_to_run.md#L45-L47](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L45-L47), [how_to_run.md#L24-L29](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L24-L29), [how_to_run.md#L58-L58](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L58-L58), [how_to_run.md#L65-L65](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L65-L65) (`clm_0337996feec59dd33c4b3d34b8c3696c00cea779d6897ef81fa7f83a0f43d5d6`)
- [observation/documented] claw-analog supports --output-format json emitting NDJSON on stdout for scripts and CI, --stream for SSE streaming, and explicit limits such as --max-turns (default 24), --max-read-bytes (262144), and glob/grep caps. -- evidence: [how_to_run.md#L204-L204](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L204-L204), [concept.md#L23-L29](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L23-L29), [how_to_run.md#L96-L112](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L96-L112) (`clm_6c92e9683047e7cc46371c8efb77ae3c8a9fdc89743ad0b7a5f5546bad0378ee`)

## memory-state (1 claim(s))

- [observation/documented] claw-analog supports JSON session files (version 1) holding workspace, model, optional preset, and API-format messages; history is loaded on resume and saved after each tool round, with a --save-session export path and warnings about secrets and token cost. -- evidence: [how_to_run.md#L158-L158](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L158-L158), [how_to_run.md#L160-L160](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L160-L160), [how_to_run.md#L162-L162](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L162-L162) (`clm_b5dd0e031cb9792a299221ab42700412b646fa9e72f6dce5e7483ecd9168e041`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] claw-analog enforces a canonical workspace root with relative paths, no `..`, and symlink/canonicalize containment checks; a PermissionPolicy and PermissionEnforcer gate tools, and dangerous modes are blocked in non-interactive runs unless explicitly accepted. -- evidence: [concept.md#L63-L68](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/concept.md#L63-L68), [how_to_run.md#L194-L198](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L194-L198), [how_to_run.md#L145-L150](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L145-L150) (`clm_ab162e8dc66e92a32ac979db517974f05fa7fa925f586657879566d9a5b12804`)
- [observation/documented] Permission modes include read-only, workspace-write, prompt, and danger-full-access/allow; write_file is unavailable in read-only and prompt modes, and danger modes are forbidden non-interactively without an explicit accept flag. -- evidence: [how_to_run.md#L145-L150](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L145-L150) (`clm_84d30e9a9f5496a3e59d34b72ac62b55cf4d7995dddbb03bbffad299ce02f9d8`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The harness requires a provider API key (e.g. ANTHROPIC_API_KEY or OPENAI_API_KEY); Claude subscription login is not a supported auth path, and claw-analog selects providers by model and environment variables. -- evidence: [how_to_run.md#L3-L3](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L3-L3), [README.md#L260-L261](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/README.md#L260-L261), [how_to_run.md#L9-L10](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/how_to_run.md#L9-L10) (`clm_533c81dd384a202572178406512950b400861323cee51997ca4c6a69a627fce7`)

## limitations (1 claim(s))

- [observation/documented] The README states claw-code does not yet ship an ACP/Zed daemon or JSON-RPC entrypoint; `claw acp serve` is only a discoverability alias returning status with exit code 0, with real ACP support tracked in the roadmap. -- evidence: [README.md#L99-L102](https://github.com/ultraworkers/claw-code/blob/08106b0c3771ef5b4a5aa176acccd460e88b7325/README.md#L99-L102) (`clm_cc0ca2b1acb13829948672687f021a4f5a2398436377757e0d766360e323ebc3`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

