---
access: public
aliases: []
claim_ids:
- clm_1ccfd0076f73d0bb71465a20caafa5558b3a55e827a97e9d82f4ef8eae063fca
- clm_3529ea2f0de70e51c51306f82ff22ae3d9e367fbc254f32e6494d984b3bd79fd
- clm_3ed4198bbe8af27dc97a01940e85a1ec3b8f355b306502a7bdbcb3b939de538f
- clm_4029304457e35d873077cee9d7b3b0c20cd5d6365de7bf49abb8e629db8c9be5
- clm_421884eda0507e4ffbdb07f809454b1c3241d527ffa6c45be2292f0bb5541773
- clm_60d20b25f9a9f84e0723590a99a9b1fa48c0a1b33843d876f8d1edf55368d1a8
- clm_73adba42ac7dec4170d0e27e2bb947fa157d45106e04aca6ad49c0063679c632
- clm_7e1ec0c2c41fb7bfad252edf12129df250a049707e15c1a8fd5e138cf653529b
- clm_ad870fd66fc869a3aeec03b38542a82af72cfbd410ddc93cb28b13c564551351
- clm_af4ed06a3d0ecf5abe3a988961ef50816d7d778e21950f6db4d8d49511e12dd9
- clm_ca5564e2ed5d0a27d625c7d9726fb64a35e4fd52cc9702699d0ed8a394706617
- clm_cf163466062182349dd9c2a91d342fb232b6f74e2d9b1ea686aac1f06a5cd485
- clm_d5d0df3977ea968e85ff9aa055b1d7d16240dd89ddfbe0cf82b4e9dd01b5cdc9
maturity: draft
page_id: pg_0a1204b09a9352338d3b98fd7e626bb2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5798aa0d88df580a8f651f873b7c9af8
title: IvanWng97/pixtuoid/README.md @ 61fa3012895f
updated_at: '2026-09-14T02:05:53Z'
---

# IvanWng97/pixtuoid/README.md @ 61fa3012895f

<!-- rcw:begin owner=source:src_5798aa0d88df580a8f651f873b7c9af8 block=evidence -->
- Pressing s opens a Sources panel to connect an agent CLI without a separate install step; disconnecting there removes the character, and broken hooks are flagged, with `pixtuoid doctor` providing a health report. [@claim:clm_1ccfd0076f73d0bb71465a20caafa5558b3a55e827a97e9d82f4ef8eae063fca]
- The dependency set is audited for advisories daily using cargo-deny. [@claim:clm_3529ea2f0de70e51c51306f82ff22ae3d9e367fbc254f32e6494d984b3bd79fd]
- The hook shim is designed to never block the agent: it performs a 200ms fire-and-forget write and can be invoked without blocking the agent CLI. [@claim:clm_3ed4198bbe8af27dc97a01940e85a1ec3b8f355b306502a7bdbcb3b939de538f]
- pixtuoid is a terminal-based tool that visualizes AI coding agents as pixel-art coworkers in an office, with each session shown as a character at a desk. [@claim:clm_4029304457e35d873077cee9d7b3b0c20cd5d6365de7bf49abb8e629db8c9be5]
- Pressing t opens a live-preview theme picker across six built-in palettes, and the chosen theme persists across sessions. [@claim:clm_421884eda0507e4ffbdb07f809454b1c3241d527ffa6c45be2292f0bb5541773]
- The project is a Rust workspace of five crates, with the core having no terminal dependencies. [@claim:clm_60d20b25f9a9f84e0723590a99a9b1fa48c0a1b33843d876f8d1edf55368d1a8]
- The TUI exposes keyboard shortcuts: q quit, p pause, s sources panel, t themes, m sound, Tab agent dashboard, ? help, and arrow/jk/PgUp/PgDn floor navigation. [@claim:clm_73adba42ac7dec4170d0e27e2bb947fa157d45106e04aca6ad49c0063679c632]
- Windows support for Claude Code and Codex CLI is marked experimental, with limited testing and unsigned binaries. [@claim:clm_7e1ec0c2c41fb7bfad252edf12129df250a049707e15c1a8fd5e138cf653529b]
- Agent events arrive via two transports — a hook shim writing to a Unix socket (named pipe on Windows) with a 200ms fire-and-forget bound, and JSONL transcript watching — feeding one channel whose reducer folds events into office state for a half-block pixel-art renderer. [@claim:clm_ad870fd66fc869a3aeec03b38542a82af72cfbd410ddc93cb28b13c564551351]
- Character shirt and pants colors derive from the working directory so same-repo agents share colors; hair and skin vary per agent across 16 curated outfits. [@claim:clm_af4ed06a3d0ecf5abe3a988961ef50816d7d778e21950f6db4d8d49511e12dd9]
- Configuration lives in ~/.config/pixtuoid/config.toml, created on first launch with all keys optional; CLI flags such as `pixtuoid run --theme dracula` override the file. [@claim:clm_ca5564e2ed5d0a27d625c7d9726fb64a35e4fd52cc9702699d0ed8a394706617]
- Each desk's monitor glows with the color of the tool currently in use (e.g. Edit blue). [@claim:clm_cf163466062182349dd9c2a91d342fb232b6f74e2d9b1ea686aac1f06a5cd485]
- The tool is described as local-only and telemetry-free: it makes no network connections, ships no analytics, and reads agent transcripts read-only. [@claim:clm_d5d0df3977ea968e85ff9aa055b1d7d16240dd89ddfbe0cf82b4e9dd01b5cdc9]
<!-- rcw:end owner=source:src_5798aa0d88df580a8f651f873b7c9af8 block=evidence -->

## Researcher notes

