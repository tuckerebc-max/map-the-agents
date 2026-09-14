---
access: public
aliases: []
claim_ids:
- clm_0d357c052d843528ea07559319f62c1d64884cd4efa2700dad547cd4890cc888
- clm_113d6f121a171335ae7fd44c9d962089d7e599d915f1cec9087a0068f65f49e1
- clm_25db8c44618426b8d12e4300c57404eceb8e81fe468ac2bad320e91e8069db94
- clm_568698fd2a3b3568e797b535ebc6cd690fa961d98e0fd489ca06f6996ccdf26b
- clm_5b14d127cc72868755179b0141b2a536513d2fe3b611445fce9335ef11a4ebce
- clm_5d4cf839d4539515946bf27a1eaba09375c004b633f18602b6cabbe36e62ba1a
- clm_6908fc685944ea3923cc9b8b33c3d519d9f0529c6f250a223b7bd7fdd0521c58
- clm_7d94761a68f8a13d6c6243005996eee3aeafce0bca759aad68c2385414fbaa71
- clm_a8ed31d8c315b2832e4ec528423260c1b7d6fd65004b9aa7471a609b09ee1bee
- clm_a984bff9470fe2895e2c6e5bc855ab4845bd0cfd6cc02242599aa55c5891b867
- clm_b4abafb70a8aa09ec0b810e67d96da5be3753e2fbdea76584fb73e7561865707
- clm_c3c1c92e2836b3bb83cd82f864e33355c083d595f6ba3e94d333234cb0e82433
- clm_d69004abb51cbc67384c18602feb0912b46e44bff2112a6034e0cc87384bae3f
- clm_e0fccb14444994a71e86869def5bb0bdd7672d17248f8833754cb546918090d9
- clm_e3a95e3aa99da90b588b26e3b93685d0d534d7ad38dde61aec9e9bb8047250ad
- clm_e5e82a466b29a985bdbac154675912bd14dfac76eb610222411132fcb31612d2
maturity: draft
page_id: pg_0485f273025d55bdb518000c9bfb4059
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_dbfa286b0bcd5220b4ecca7d32254027
title: DevCoreXOfficial/core-termux/README.md @ 72446370343c
updated_at: '2026-09-14T03:46:52Z'
---

# DevCoreXOfficial/core-termux/README.md @ 72446370343c

<!-- rcw:begin owner=source:src_dbfa286b0bcd5220b4ecca7d32254027 block=evidence -->
- The README badges identify the project as version 4.27.2, MIT-licensed, and targeting the Termux/Android platform. [@claim:clm_0d357c052d843528ea07559319f62c1d64884cd4efa2700dad547cd4890cc888]
- The Next.js template installs dependencies such as zod, zustand, react-hook-form, and Tailwind CSS, plus arm64-linux native bindings for LightningCSS and Tailwind oxide. [@claim:clm_113d6f121a171335ae7fd44c9d962089d7e599d915f1cec9087a0068f65f49e1]
- The product exposes a single CLI named `core` with subcommands including install, update, uninstall, reinstall, list, show, open, agent, brain, env, voice, pg, and init. [@claim:clm_25db8c44618426b8d12e4300c57404eceb8e81fe468ac2bad320e91e8069db94]
- `core voice` requires the Termux:API package and app plus Neovim, and it automatically runs termux-api-start before capturing audio. [@claim:clm_568698fd2a3b3568e797b535ebc6cd690fa961d98e0fd489ca06f6996ccdf26b]
- `core agent` is a local AI assistant backed by an OpenAI-compatible endpoint, defaulting to a gemma model served by Cactus Engine at 127.0.0.1:8000/v1; if the server is down it starts cactus in the background and stops it when the interactive shell exits. [@claim:clm_5b14d127cc72868755179b0141b2a536513d2fe3b611445fce9335ef11a4ebce]
- In agent run mode, model-generated commands execute only after a y/N confirmation; `-y` auto-approves, and plan mode is read-only, blocking file writes and write commands. [@claim:clm_5d4cf839d4539515946bf27a1eaba09375c004b633f18602b6cabbe36e62ba1a]
- `core pg` manages PostgreSQL with start/stop/restart/status, database create/drop/list, a psql shell, and logs under ~/.cache/core-termux/postgresql.log. [@claim:clm_6908fc685944ea3923cc9b8b33c3d519d9f0529c6f250a223b7bd7fdd0521c58]
- Modules include lang (Node.js, Python, Rust, Go, etc.), db (PostgreSQL, MariaDB, SQLite, MongoDB, Redis), ai, editor, dev, npm, shell, ui, and auto (n8n). [@claim:clm_7d94761a68f8a13d6c6243005996eee3aeafce0bca759aad68c2385414fbaa71]
- Uninstall and reinstall support per-module and per-tool targeting but deliberately offer no 'uninstall all' or 'reinstall all' operation. [@claim:clm_a8ed31d8c315b2832e4ec528423260c1b7d6fd65004b9aa7471a609b09ee1bee]
- The lang module installs programming languages and runtimes via the pkg package manager. [@claim:clm_a984bff9470fe2895e2c6e5bc855ab4845bd0cfd6cc02242599aa55c5891b867]
- The project is designed exclusively for Termux on Android and is documented as not supported on other platforms. [@claim:clm_b4abafb70a8aa09ec0b810e67d96da5be3753e2fbdea76584fb73e7561865707]
- The ai module installs many coding agents via per-agent flags, including Qwen Code, Gemini CLI, Claude Code, Ollama, Codex CLI, and OpenCode, either all at once or selected ones. [@claim:clm_c3c1c92e2836b3bb83cd82f864e33355c083d595f6ba3e94d333234cb0e82433]
- `core voice` captures microphone audio, lets the user review the prompt in nvim, and launches one of several supported agents such as opencode, claude-code, codex, or gemini-cli. [@claim:clm_d69004abb51cbc67384c18602feb0912b46e44bff2112a6034e0cc87384bae3f]
- `core brain` stores personal memories as AI-consumable markdown files with frontmatter (title, tags, category, related), organized in category folders, optionally synced to a private GitHub repo via `gh`. [@claim:clm_e0fccb14444994a71e86869def5bb0bdd7672d17248f8833754cb546918090d9]
- `core env` interactively manages environment variables in .zshrc or .bashrc, hides typed values with ● characters, and warns before replacing existing variables. [@claim:clm_e3a95e3aa99da90b588b26e3b93685d0d534d7ad38dde61aec9e9bb8047250ad]
- `core init` scaffolds projects from next, react, nest, and express templates, detecting the package manager (npm, pnpm, yarn, or bun) and preserving existing package.json scripts. [@claim:clm_e5e82a466b29a985bdbac154675912bd14dfac76eb610222411132fcb31612d2]
<!-- rcw:end owner=source:src_dbfa286b0bcd5220b4ecca7d32254027 block=evidence -->

## Researcher notes

