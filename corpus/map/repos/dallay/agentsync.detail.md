# dallay/agentsync -- full detail

[Back to orientation](agentsync.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/dallay/agentsync/7102a4d56da001b173bea6644179e31132242de9/5a41a0627fdde6f2.json](../../../wiki/dossiers/dallay/agentsync/7102a4d56da001b173bea6644179e31132242de9/5a41a0627fdde6f2.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] AgentSync can generate MCP configuration files for Claude Code, GitHub Copilot, OpenAI Codex CLI, Gemini CLI, Cursor, VS Code, and OpenCode; under merge strategy, TOML-defined servers win conflicts while other existing servers are preserved. -- evidence: [README.md#L435-L444](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L435-L444), [README.md#L456-L459](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L456-L459), [README.md#L405-L406](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L405-L406) (`clm_e6c423a8c04362db99fdc5c79457762e68cf6e40c447a6cbaf0b76ecf2b43671`)
- [observation/documented] The repository is a monorepo containing a Rust core and CLI in src/, a TypeScript npm wrapper in npm/agentsync/, a Starlight documentation site, and integration tests in tests/. -- evidence: [README.md#L628-L628](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L628-L628), [README.md#L632-L635](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L632-L635) (`clm_7604e1a40a9cf1fe88d3d387040ab0b5522d9216c44788bd8f455829aa0884ec`)

## design-choices (3 claim(s))

- [observation/documented] AgentSync uses symlinks rather than copies so changes propagate instantly, and it automatically backs up existing files before replacing them. -- evidence: [README.md#L98-L105](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L98-L105) (`clm_ee537d7ba64eb56c6ccb0eccc48b1f17cdbbe4cbf72274f34d70d84c0a17a225`)
- [observation/documented] Configuration lives in a TOML file at .agents/agentsync.toml (the default lookup location), which defines the source of truth, gitignore handling, and per-assistant targets. -- evidence: [website/docs/src/content/docs/reference/configuration.mdx#L8-L8](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/website/docs/src/content/docs/reference/configuration.mdx#L8-L8), [website/docs/src/content/docs/reference/configuration.mdx#L10-L10](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/website/docs/src/content/docs/reference/configuration.mdx#L10-L10), [README.md#L366-L366](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L366-L366) (`clm_5b9d5600545f5220858939ea3417e86da143a7b283cc8a85fb8a3712153ffb37`)
- [observation/documented] Gitignore management defaults to enabled with a configurable marker and automatically updates .gitignore; teams can explicitly opt out via [gitignore].enabled = false. -- evidence: [README.md#L294-L294](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L294-L294), [README.md#L380-L382](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L380-L382) (`clm_b4d1faa6a900e594aa301c3ce235b06949db7f6a8222338d561185837ac6e409`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: a Catalog E2E GitHub Actions workflow validates that every skill entry can be resolved, installed, and registered; it runs manually and weekly (Mondays 08:00 UTC), and locally via RUN_E2E=1 cargo test with an agents-skills sibling checkout, kept out of normal CI because it depends on external networks. -- evidence: [README.md#L109-L110](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L109-L110), [README.md#L117-L121](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L117-L121), [README.md#L126-L127](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L126-L127), [README.md#L123-L124](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L123-L124), [README.md#L112-L115](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L112-L115) (`clm_168b848b7ebf95aa1868213ed4d03d245b50fd2f9d2bfe05f27f32249504f841`)

## skills-patterns (1 claim(s))

- [observation/documented] AgentSync ships a curated skill catalog of 200+ skills across 110+ technologies, sourced from the dallay/agents-skills repository plus external providers such as Angular, Vercel, Cloudflare, Expo, and Stripe. -- evidence: [README.md#L608-L608](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L608-L608), [README.md#L610-L611](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L610-L611) (`clm_5cafae43c4577479c02466722877edc3e3ea490026bb2faecc62b6bc63418329`)

## interfaces (3 claim(s))

- [observation/documented] The apply command supports flags including --clean, --config, --dry-run, --no-gitignore, --agents (filtering), and --verbose, per documented usage examples. -- evidence: [README.md#L331-L331](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L331-L331), [README.md#L325-L325](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L325-L325), [README.md#L328-L328](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L328-L328), [README.md#L313-L313](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L313-L313), [README.md#L322-L322](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L322-L322), [README.md#L319-L319](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L319-L319) (`clm_aedd87fbc9cf6f31835f806b87af722d76ffb0bf21c3673f11012933508bcb34`)
- [observation/documented] The status command accepts optional --project-root and --json flags, is sync-type aware (symlink vs symlink-contents), and exits 0 when no problems are found and 1 otherwise, described as CI-friendly. -- evidence: [README.md#L362-L362](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L362-L362), [README.md#L356-L356](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L356-L356), [README.md#L358-L360](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L358-L360), [README.md#L353-L354](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L353-L354), [README.md#L349-L351](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L349-L351) (`clm_791caa59fdd710b948dde264951813ffaa57c411368c4487ca6eab68ff5ae697`)
- [observation/documented] Four target types are documented: symlink, symlink-contents (with optional glob pattern filtering), nested-glob for recursive discovery suited to monorepos, and module-map. -- evidence: [README.md#L477-L479](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L477-L479), [README.md#L463-L468](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L463-L468), [README.md#L470-L473](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L470-L473) (`clm_ad84df3d9746f185fa75e537ec1d4ff18e85f74a94fc26c49b9cbe170a73752d`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The tool ships as a single static binary with no runtime dependencies, and can be installed via Node package managers (Node >=18), cargo from crates.io, pre-built GitHub release binaries with sha256 checksum verification, or built from source requiring Rust 1.89+ and Node.js 22.22.0+. -- evidence: [README.md#L187-L187](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L187-L187), [README.md#L98-L105](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L98-L105), [README.md#L213-L217](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L213-L217), [README.md#L195-L195](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L195-L195), [README.md#L209-L210](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L209-L210), [README.md#L231-L231](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L231-L231), [README.md#L133-L133](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L133-L133), [README.md#L189-L191](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L189-L191) (`clm_b79ea5ea5719f84a59c689ca58f720dcd33e515a06d5118f08b0b7e7016b1d05`)

## limitations (1 claim(s))

- [observation/documented] On Windows, native symlink creation may require additional prerequisites; the project directs users to a dedicated setup guide covering prerequisites, WSL, verification, and recovery steps. -- evidence: [README.md#L728-L728](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L728-L728), [README.md#L296-L296](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L296-L296) (`clm_5850eb64857cbbaa930373bbf7c31d5e80f4cd33460bec70bf3c7df71b368a1b`)

## relevance (1 claim(s))

- [observation/documented] AgentSync targets teams using multiple AI coding assistants (Claude Code, Gemini CLI, Cursor, GitHub Copilot, OpenAI Codex, OpenCode) whose configuration files would otherwise be scattered across different locations and drift. -- evidence: [README.md#L83-L91](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L83-L91), [README.md#L25-L25](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L25-L25), [README.md#L93-L94](https://github.com/dallay/agentsync/blob/7102a4d56da001b173bea6644179e31132242de9/README.md#L93-L94) (`clm_40d5bb8a64c306397e6da56b3aa1c675896a744eda67e659b908a90327e8c5ac`)

