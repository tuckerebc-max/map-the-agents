---
access: public
aliases: []
claim_ids:
- clm_168b848b7ebf95aa1868213ed4d03d245b50fd2f9d2bfe05f27f32249504f841
- clm_40d5bb8a64c306397e6da56b3aa1c675896a744eda67e659b908a90327e8c5ac
- clm_5850eb64857cbbaa930373bbf7c31d5e80f4cd33460bec70bf3c7df71b368a1b
- clm_5b9d5600545f5220858939ea3417e86da143a7b283cc8a85fb8a3712153ffb37
- clm_5cafae43c4577479c02466722877edc3e3ea490026bb2faecc62b6bc63418329
- clm_7604e1a40a9cf1fe88d3d387040ab0b5522d9216c44788bd8f455829aa0884ec
- clm_791caa59fdd710b948dde264951813ffaa57c411368c4487ca6eab68ff5ae697
- clm_ad84df3d9746f185fa75e537ec1d4ff18e85f74a94fc26c49b9cbe170a73752d
- clm_aedd87fbc9cf6f31835f806b87af722d76ffb0bf21c3673f11012933508bcb34
- clm_b4d1faa6a900e594aa301c3ce235b06949db7f6a8222338d561185837ac6e409
- clm_b79ea5ea5719f84a59c689ca58f720dcd33e515a06d5118f08b0b7e7016b1d05
- clm_e6c423a8c04362db99fdc5c79457762e68cf6e40c447a6cbaf0b76ecf2b43671
- clm_ee537d7ba64eb56c6ccb0eccc48b1f17cdbbe4cbf72274f34d70d84c0a17a225
maturity: draft
page_id: pg_af02f7744e2c5585920ccc7e9b6c928a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_77f3016698c35bed84a0b7f4e56bbe23
title: dallay/agentsync/README.md @ 7102a4d56da0
updated_at: '2026-09-14T03:44:13Z'
---

# dallay/agentsync/README.md @ 7102a4d56da0

<!-- rcw:begin owner=source:src_77f3016698c35bed84a0b7f4e56bbe23 block=evidence -->
- Repository development practice: a Catalog E2E GitHub Actions workflow validates that every skill entry can be resolved, installed, and registered; it runs manually and weekly (Mondays 08:00 UTC), and locally via RUN_E2E=1 cargo test with an agents-skills sibling checkout, kept out of normal CI because it depends on external networks. [@claim:clm_168b848b7ebf95aa1868213ed4d03d245b50fd2f9d2bfe05f27f32249504f841]
- AgentSync targets teams using multiple AI coding assistants (Claude Code, Gemini CLI, Cursor, GitHub Copilot, OpenAI Codex, OpenCode) whose configuration files would otherwise be scattered across different locations and drift. [@claim:clm_40d5bb8a64c306397e6da56b3aa1c675896a744eda67e659b908a90327e8c5ac]
- On Windows, native symlink creation may require additional prerequisites; the project directs users to a dedicated setup guide covering prerequisites, WSL, verification, and recovery steps. [@claim:clm_5850eb64857cbbaa930373bbf7c31d5e80f4cd33460bec70bf3c7df71b368a1b]
- Configuration lives in a TOML file at .agents/agentsync.toml (the default lookup location), which defines the source of truth, gitignore handling, and per-assistant targets. [@claim:clm_5b9d5600545f5220858939ea3417e86da143a7b283cc8a85fb8a3712153ffb37]
- AgentSync ships a curated skill catalog of 200+ skills across 110+ technologies, sourced from the dallay/agents-skills repository plus external providers such as Angular, Vercel, Cloudflare, Expo, and Stripe. [@claim:clm_5cafae43c4577479c02466722877edc3e3ea490026bb2faecc62b6bc63418329]
- The repository is a monorepo containing a Rust core and CLI in src/, a TypeScript npm wrapper in npm/agentsync/, a Starlight documentation site, and integration tests in tests/. [@claim:clm_7604e1a40a9cf1fe88d3d387040ab0b5522d9216c44788bd8f455829aa0884ec]
- The status command accepts optional --project-root and --json flags, is sync-type aware (symlink vs symlink-contents), and exits 0 when no problems are found and 1 otherwise, described as CI-friendly. [@claim:clm_791caa59fdd710b948dde264951813ffaa57c411368c4487ca6eab68ff5ae697]
- Four target types are documented: symlink, symlink-contents (with optional glob pattern filtering), nested-glob for recursive discovery suited to monorepos, and module-map. [@claim:clm_ad84df3d9746f185fa75e537ec1d4ff18e85f74a94fc26c49b9cbe170a73752d]
- The apply command supports flags including --clean, --config, --dry-run, --no-gitignore, --agents (filtering), and --verbose, per documented usage examples. [@claim:clm_aedd87fbc9cf6f31835f806b87af722d76ffb0bf21c3673f11012933508bcb34]
- Gitignore management defaults to enabled with a configurable marker and automatically updates .gitignore; teams can explicitly opt out via [gitignore].enabled = false. [@claim:clm_b4d1faa6a900e594aa301c3ce235b06949db7f6a8222338d561185837ac6e409]
- The tool ships as a single static binary with no runtime dependencies, and can be installed via Node package managers (Node >=18), cargo from crates.io, pre-built GitHub release binaries with sha256 checksum verification, or built from source requiring Rust 1.89+ and Node.js 22.22.0+. [@claim:clm_b79ea5ea5719f84a59c689ca58f720dcd33e515a06d5118f08b0b7e7016b1d05]
- AgentSync can generate MCP configuration files for Claude Code, GitHub Copilot, OpenAI Codex CLI, Gemini CLI, Cursor, VS Code, and OpenCode; under merge strategy, TOML-defined servers win conflicts while other existing servers are preserved. [@claim:clm_e6c423a8c04362db99fdc5c79457762e68cf6e40c447a6cbaf0b76ecf2b43671]
- AgentSync uses symlinks rather than copies so changes propagate instantly, and it automatically backs up existing files before replacing them. [@claim:clm_ee537d7ba64eb56c6ccb0eccc48b1f17cdbbe4cbf72274f34d70d84c0a17a225]
<!-- rcw:end owner=source:src_77f3016698c35bed84a0b7f4e56bbe23 block=evidence -->

## Researcher notes

