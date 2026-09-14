# devcorexofficial/core-termux -- full detail

[Back to orientation](core-termux.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/devcorexofficial/core-termux/72446370343cab50c34bb8ee5152082ff031cc61/422ed5b5e17364df.json](../../../wiki/dossiers/devcorexofficial/core-termux/72446370343cab50c34bb8ee5152082ff031cc61/422ed5b5e17364df.json)

## specifications (1 claim(s))

- [observation/documented] The README badges identify the project as version 4.27.2, MIT-licensed, and targeting the Termux/Android platform. -- evidence: [README.md#L11-L21](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L11-L21) (`clm_0d357c052d843528ea07559319f62c1d64884cd4efa2700dad547cd4890cc888`)

## components (2 claim(s))

- [observation/documented] Modules include lang (Node.js, Python, Rust, Go, etc.), db (PostgreSQL, MariaDB, SQLite, MongoDB, Redis), ai, editor, dev, npm, shell, ui, and auto (n8n). -- evidence: [README.md#L92-L102](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L92-L102) (`clm_7d94761a68f8a13d6c6243005996eee3aeafce0bca759aad68c2385414fbaa71`)
- [observation/documented] The ai module installs many coding agents via per-agent flags, including Qwen Code, Gemini CLI, Claude Code, Ollama, Codex CLI, and OpenCode, either all at once or selected ones. -- evidence: [README.md#L115-L153](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L115-L153), [README.md#L110-L113](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L110-L113), [README.md#L108-L108](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L108-L108) (`clm_c3c1c92e2836b3bb83cd82f864e33355c083d595f6ba3e94d333234cb0e82433`)

## design-choices (2 claim(s))

- [observation/documented] The project is designed exclusively for Termux on Android and is documented as not supported on other platforms. -- evidence: [README.md#L48-L49](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L48-L49) (`clm_b4abafb70a8aa09ec0b810e67d96da5be3753e2fbdea76584fb73e7561865707`)
- [observation/documented] Uninstall and reinstall support per-module and per-tool targeting but deliberately offer no 'uninstall all' or 'reinstall all' operation. -- evidence: [README.md#L545-L545](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L545-L545), [README.md#L523-L523](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L523-L523) (`clm_a8ed31d8c315b2832e4ec528423260c1b7d6fd65004b9aa7471a609b09ee1bee`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] The product exposes a single CLI named `core` with subcommands including install, update, uninstall, reinstall, list, show, open, agent, brain, env, voice, pg, and init. -- evidence: [README.md#L69-L84](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L69-L84), [README.md#L46-L46](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L46-L46) (`clm_25db8c44618426b8d12e4300c57404eceb8e81fe468ac2bad320e91e8069db94`)
- [observation/documented] `core env` interactively manages environment variables in .zshrc or .bashrc, hides typed values with ● characters, and warns before replacing existing variables. -- evidence: [README.md#L233-L233](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L233-L233), [README.md#L244-L247](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L244-L247) (`clm_e3a95e3aa99da90b588b26e3b93685d0d534d7ad38dde61aec9e9bb8047250ad`)
- [observation/documented] `core voice` captures microphone audio, lets the user review the prompt in nvim, and launches one of several supported agents such as opencode, claude-code, codex, or gemini-cli. -- evidence: [README.md#L362-L362](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L362-L362), [README.md#L380-L395](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L380-L395) (`clm_d69004abb51cbc67384c18602feb0912b46e44bff2112a6034e0cc87384bae3f`)
- [observation/documented] `core init` scaffolds projects from next, react, nest, and express templates, detecting the package manager (npm, pnpm, yarn, or bun) and preserving existing package.json scripts. -- evidence: [README.md#L601-L601](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L601-L601), [README.md#L618-L623](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L618-L623), [README.md#L610-L614](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L610-L614) (`clm_e5e82a466b29a985bdbac154675912bd14dfac76eb610222411132fcb31612d2`)
- [observation/documented] `core pg` manages PostgreSQL with start/stop/restart/status, database create/drop/list, a psql shell, and logs under ~/.cache/core-termux/postgresql.log. -- evidence: [README.md#L579-L590](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L579-L590), [README.md#L592-L595](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L592-L595) (`clm_6908fc685944ea3923cc9b8b33c3d519d9f0529c6f250a223b7bd7fdd0521c58`)

## memory-state (1 claim(s))

- [observation/documented] `core brain` stores personal memories as AI-consumable markdown files with frontmatter (title, tags, category, related), organized in category folders, optionally synced to a private GitHub repo via `gh`. -- evidence: [README.md#L306-L313](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L306-L313), [README.md#L285-L285](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L285-L285), [README.md#L322-L326](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L322-L326) (`clm_e0fccb14444994a71e86869def5bb0bdd7672d17248f8833754cb546918090d9`)

## orchestration (1 claim(s))

- [observation/documented] `core agent` is a local AI assistant backed by an OpenAI-compatible endpoint, defaulting to a gemma model served by Cactus Engine at 127.0.0.1:8000/v1; if the server is down it starts cactus in the background and stops it when the interactive shell exits. -- evidence: [README.md#L176-L176](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L176-L176) (`clm_5b14d127cc72868755179b0141b2a536513d2fe3b611445fce9335ef11a4ebce`)

## tools-permissions (1 claim(s))

- [observation/documented] In agent run mode, model-generated commands execute only after a y/N confirmation; `-y` auto-approves, and plan mode is read-only, blocking file writes and write commands. -- evidence: [README.md#L189-L200](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L189-L200), [README.md#L204-L209](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L204-L209), [README.md#L213-L213](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L213-L213) (`clm_5d4cf839d4539515946bf27a1eaba09375c004b633f18602b6cabbe36e62ba1a`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (3 claim(s))

- [observation/documented] `core voice` requires the Termux:API package and app plus Neovim, and it automatically runs termux-api-start before capturing audio. -- evidence: [README.md#L371-L374](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L371-L374), [README.md#L376-L376](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L376-L376) (`clm_568698fd2a3b3568e797b535ebc6cd690fa961d98e0fd489ca06f6996ccdf26b`)
- [observation/documented] The Next.js template installs dependencies such as zod, zustand, react-hook-form, and Tailwind CSS, plus arm64-linux native bindings for LightningCSS and Tailwind oxide. -- evidence: [README.md#L681-L704](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L681-L704) (`clm_113d6f121a171335ae7fd44c9d962089d7e599d915f1cec9087a0068f65f49e1`)
- [observation/documented] The lang module installs programming languages and runtimes via the pkg package manager. -- evidence: [README.md#L802-L802](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L802-L802) (`clm_a984bff9470fe2895e2c6e5bc855ab4845bd0cfd6cc02242599aa55c5891b867`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

