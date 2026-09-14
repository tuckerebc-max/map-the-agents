# ivanwng97/pixtuoid -- full detail

[Back to orientation](pixtuoid.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ivanwng97/pixtuoid/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/d6a2848ae934438e.json](../../../wiki/dossiers/ivanwng97/pixtuoid/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/d6a2848ae934438e.json)

## specifications (1 claim(s))

- [observation/documented] pixtuoid is a terminal-based tool that visualizes AI coding agents as pixel-art coworkers in an office, with each session shown as a character at a desk. -- evidence: [README.md#L41-L41](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L41-L41), [README.md#L7-L9](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L7-L9) (`clm_4029304457e35d873077cee9d7b3b0c20cd5d6365de7bf49abb8e629db8c9be5`)

## components (2 claim(s))

- [observation/documented] Agent events arrive via two transports — a hook shim writing to a Unix socket (named pipe on Windows) with a 200ms fire-and-forget bound, and JSONL transcript watching — feeding one channel whose reducer folds events into office state for a half-block pixel-art renderer. -- evidence: [README.md#L138-L138](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L138-L138) (`clm_ad870fd66fc869a3aeec03b38542a82af72cfbd410ddc93cb28b13c564551351`)
- [observation/documented] The project is a Rust workspace of five crates, with the core having no terminal dependencies. -- evidence: [README.md#L138-L138](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L138-L138), [CLAUDE.md#L28-L30](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/CLAUDE.md#L28-L30) (`clm_60d20b25f9a9f84e0723590a99a9b1fa48c0a1b33843d876f8d1edf55368d1a8`)

## design-choices (3 claim(s))

- [observation/documented] The hook shim is designed to never block the agent: it performs a 200ms fire-and-forget write and can be invoked without blocking the agent CLI. -- evidence: [README.md#L138-L138](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L138-L138) (`clm_3ed4198bbe8af27dc97a01940e85a1ec3b8f355b306502a7bdbcb3b939de538f`)
- [observation/documented] Character shirt and pants colors derive from the working directory so same-repo agents share colors; hair and skin vary per agent across 16 curated outfits. -- evidence: [README.md#L77-L95](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L77-L95) (`clm_af4ed06a3d0ecf5abe3a988961ef50816d7d778e21950f6db4d8d49511e12dd9`)
- [observation/documented] Each desk's monitor glows with the color of the tool currently in use (e.g. Edit blue). -- evidence: [README.md#L77-L95](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L77-L95) (`clm_cf163466062182349dd9c2a91d342fb232b6f74e2d9b1ea686aac1f06a5cd485`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: non-trivial work follows an arc (pick, design gate, spec, TDD build, self-review, merge gate) where the merge gate is a two-lens-review skill requiring 2+ differentiated lenses, green CI, and dispositioned bot findings, and a human performs the merge. -- evidence: [CLAUDE.md#L71-L76](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/CLAUDE.md#L71-L76) (`clm_9f7329ff90d50b620236a161562118674fb09717c57bfc51f908024416363ea3`)
- [observation/documented] Repository development practice: contributors use `just build`, `just test` (nextest), and `just preflight` as the pre-push gate running lint, clippy, hack, and test in CI order. -- evidence: [CLAUDE.md#L50-L55](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/CLAUDE.md#L50-L55) (`clm_2d0b20251ade98d5610c27842f56fd5668f5c06f92510d97ccceb32a35a99ebf`)
- [observation/documented] Repository development practice: committed repo skills include two-lens-review, beautify-decoration, add-source, add-theme, and procedural-lofi. -- evidence: [CLAUDE.md#L78-L79](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/CLAUDE.md#L78-L79) (`clm_7182be8fb87e29d4635428e9d7ac5b36deab44741467ab29a05829c4a0d6d353`)
- [observation/documented] Repository development practice: conventions require TDD-first, WHY-only comments, no magic numbers, no unwrap() outside tests, and no ratatui/crossterm dependencies in pixtuoid-core or pixtuoid-scene. -- evidence: [CLAUDE.md#L83-L94](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/CLAUDE.md#L83-L94), [CLAUDE.md#L120-L126](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/CLAUDE.md#L120-L126) (`clm_03cf0b6bfc8b07e8a53c4f9ccf4e8a33e83dddeea11ff2432251ea8f7e55a04c`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The TUI exposes keyboard shortcuts: q quit, p pause, s sources panel, t themes, m sound, Tab agent dashboard, ? help, and arrow/jk/PgUp/PgDn floor navigation. -- evidence: [README.md#L71-L71](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L71-L71) (`clm_73adba42ac7dec4170d0e27e2bb947fa157d45106e04aca6ad49c0063679c632`)
- [observation/documented] Pressing s opens a Sources panel to connect an agent CLI without a separate install step; disconnecting there removes the character, and broken hooks are flagged, with `pixtuoid doctor` providing a health report. -- evidence: [README.md#L69-L69](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L69-L69) (`clm_1ccfd0076f73d0bb71465a20caafa5558b3a55e827a97e9d82f4ef8eae063fca`)
- [observation/documented] Configuration lives in ~/.config/pixtuoid/config.toml, created on first launch with all keys optional; CLI flags such as `pixtuoid run --theme dracula` override the file. -- evidence: [README.md#L120-L122](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L120-L122) (`clm_ca5564e2ed5d0a27d625c7d9726fb64a35e4fd52cc9702699d0ed8a394706617`)
- [observation/documented] Pressing t opens a live-preview theme picker across six built-in palettes, and the chosen theme persists across sessions. -- evidence: [README.md#L124-L125](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L124-L125) (`clm_421884eda0507e4ffbdb07f809454b1c3241d527ffa6c45be2292f0bb5541773`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The tool is described as local-only and telemetry-free: it makes no network connections, ships no analytics, and reads agent transcripts read-only. -- evidence: [README.md#L144-L149](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L144-L149) (`clm_d5d0df3977ea968e85ff9aa055b1d7d16240dd89ddfbe0cf82b4e9dd01b5cdc9`)
- [observation/documented] The dependency set is audited for advisories daily using cargo-deny. -- evidence: [README.md#L144-L149](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L144-L149) (`clm_3529ea2f0de70e51c51306f82ff22ae3d9e367fbc254f32e6494d984b3bd79fd`)

## limitations (1 claim(s))

- [observation/documented] Windows support for Claude Code and Codex CLI is marked experimental, with limited testing and unsigned binaries. -- evidence: [README.md#L113-L114](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L113-L114), [README.md#L103-L107](https://github.com/IvanWng97/pixtuoid/blob/61fa3012895f5a3396ae7b9c69e9dc4fbce3f396/README.md#L103-L107) (`clm_7e1ec0c2c41fb7bfad252edf12129df250a049707e15c1a8fd5e138cf653529b`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

