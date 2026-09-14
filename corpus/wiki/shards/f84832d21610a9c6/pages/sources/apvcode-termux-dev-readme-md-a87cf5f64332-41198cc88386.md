---
access: public
aliases: []
claim_ids:
- clm_5d5833651bae0f0f3ebdd684332aa980e91c81acf0b03e03b51186cc6863281a
- clm_647dc2d8eb48c5ce422dbc69c49274bba6739a78d93fe4d639e85772aa58c67a
- clm_674c4aac145bb50f5c1325440e0ee220aa249d1587f432ddee19e51c7548306a
- clm_697c5b6ca788b72153db48dbd62f0686e5bd2a31a647728d7da6306bdce4ca87
- clm_6abe701bd4b366c95fa7b82e291c5778daadd43f75085935a18e62574d442693
- clm_6b368929b40b0920853f3510b3220b797cb78986a2e658282c605f598f117575
- clm_6c87ec4d608e6d162a21a77e5a0abd4e5cbd20be8e82ffe72ddf5855c60d8f99
- clm_6ffbb6989f089444878c56ade2c873136f3a49e47dd1853771f56eae738f3aa3
- clm_73968487dbe74d608c459431c1c8cf6c4ad171b434f614925c61bb0ead017399
- clm_b0a51910994376a3d6e37d3266297c88f66c516546ba8368a9bb35a09d10b6c6
- clm_e3272f4eb8f05a68c35ab36bf91c86ab002ab2e9f1eeeee7397220358b1b82c4
- clm_f80693ebb1d80b677fa015b376cda64483823569f1efe7660f225169f263e9df
maturity: draft
page_id: pg_477dddd8e8d351c8866241198cc88386
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d8c8af915f6b50e8bf482cc39b71ba60
title: apvcode/Termux-Dev/README.md @ a87cf5f64332
updated_at: '2026-09-14T01:34:33Z'
---

# apvcode/Termux-Dev/README.md @ a87cf5f64332

<!-- rcw:begin owner=source:src_d8c8af915f6b50e8bf482cc39b71ba60 block=evidence -->
- The agent uses a dual-mode architecture: PLAN mode acts as a safe architect with a requirements questionnaire and no code edits, while AGENT mode autonomously edits files, runs terminal commands, and installs packages. [@claim:clm_5d5833651bae0f0f3ebdd684332aa980e91c81acf0b03e03b51186cc6863281a]
- Repository development practice: developers can build from source by cloning the GitHub repo, running npm install, and npm link; a CI workflow badge (ci.yml) is shown in the README. [@claim:clm_647dc2d8eb48c5ce422dbc69c49274bba6739a78d93fe4d639e85772aa58c67a]
- A persistent project memory bank is stored in `.devx/memory.md` and managed with `/memory add <rule>`, intended to carry project context across sessions. [@claim:clm_674c4aac145bb50f5c1325440e0ee220aa249d1587f432ddee19e51c7548306a]
- The CLI is launched as `devx`, supports starting in PLAN mode via `--plan`, and offers a headless one-shot mode using `-p "<prompt>"` with an optional `--yolo` flag. [@claim:clm_697c5b6ca788b72153db48dbd62f0686e5bd2a31a647728d7da6306bdce4ca87]
- Self-healing diagnostics run external checkers for TypeScript (tsc), JavaScript (node --check), Python (py_compile), and Rust (cargo check), with the AI fixing errors before finishing a turn. [@claim:clm_6abe701bd4b366c95fa7b82e291c5778daadd43f75085935a18e62574d442693]
- The project requires Node.js v20.0.0 or higher and a package manager (npm, pnpm, or yarn); it is distributed as the npm package termux-dev and is MIT licensed. [@claim:clm_6b368929b40b0920853f3510b3220b797cb78986a2e658282c605f598f117575]
- Sessions are saved and can be listed, resumed, or deleted via /resume, /session, and /session del; /resume reportedly renders the last 20 messages of a session. [@claim:clm_6c87ec4d608e6d162a21a77e5a0abd4e5cbd20be8e82ffe72ddf5855c60d8f99]
- The product includes a built-in local HTTP server (/serve, default port 3000) for previewing web apps and HTML5 games, opening on Android via termux-open-url. [@claim:clm_6ffbb6989f089444878c56ade2c873136f3a49e47dd1853771f56eae738f3aa3]
- Repository development practice: complete uninstall instructions cover removing the global npm package plus ~/.devx and ~/.devxrc.json on Unix-like systems, with equivalent PowerShell commands for Windows. [@claim:clm_73968487dbe74d608c459431c1c8cf6c4ad171b434f614925c61bb0ead017399]
- Keybindings include Tab to toggle PLAN/AGENT modes, Ctrl+P/Ctrl+V for clipboard image paste, @filename fuzzy file autocomplete, atomic Backspace deletion of paste badges, and Ctrl+C to stop generation. [@claim:clm_b0a51910994376a3d6e37d3266297c88f66c516546ba8368a9bb35a09d10b6c6]
- Finalized architectural plans are approved via a one-click `[Go / Other]` prompt, after which the coder agent begins implementation. [@claim:clm_e3272f4eb8f05a68c35ab36bf91c86ab002ab2e9f1eeeee7397220358b1b82c4]
- A slash-command palette (opened by typing `/`) includes commands such as /plan, /agent, /mcp, /usage, /export, /theme, /doctor, /image, /serve, /memory, /undo, /diff, /commit, /status, /session, /resume, /settings, and /update. [@claim:clm_f80693ebb1d80b677fa015b376cda64483823569f1efe7660f225169f263e9df]
<!-- rcw:end owner=source:src_d8c8af915f6b50e8bf482cc39b71ba60 block=evidence -->

## Researcher notes

