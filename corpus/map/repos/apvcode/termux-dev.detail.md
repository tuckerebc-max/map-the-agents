# apvcode/termux-dev -- full detail

[Back to orientation](termux-dev.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/apvcode/termux-dev/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/0ede1806afb1f442.json](../../../wiki/dossiers/apvcode/termux-dev/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/0ede1806afb1f442.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The product includes a built-in local HTTP server (/serve, default port 3000) for previewing web apps and HTML5 games, opening on Android via termux-open-url. -- evidence: [README.md#L31-L54](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L31-L54) (`clm_6ffbb6989f089444878c56ade2c873136f3a49e47dd1853771f56eae738f3aa3`)
- [observation/documented] Self-healing diagnostics run external checkers for TypeScript (tsc), JavaScript (node --check), Python (py_compile), and Rust (cargo check), with the AI fixing errors before finishing a turn. -- evidence: [README.md#L31-L54](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L31-L54) (`clm_6abe701bd4b366c95fa7b82e291c5778daadd43f75085935a18e62574d442693`)

## design-choices (2 claim(s))

- [observation/documented] The agent uses a dual-mode architecture: PLAN mode acts as a safe architect with a requirements questionnaire and no code edits, while AGENT mode autonomously edits files, runs terminal commands, and installs packages. -- evidence: [README.md#L31-L54](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L31-L54) (`clm_5d5833651bae0f0f3ebdd684332aa980e91c81acf0b03e03b51186cc6863281a`)
- [observation/documented] Finalized architectural plans are approved via a one-click `[Go / Other]` prompt, after which the coder agent begins implementation. -- evidence: [README.md#L31-L54](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L31-L54) (`clm_e3272f4eb8f05a68c35ab36bf91c86ab002ab2e9f1eeeee7397220358b1b82c4`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: developers can build from source by cloning the GitHub repo, running npm install, and npm link; a CI workflow badge (ci.yml) is shown in the README. -- evidence: [README.md#L85-L90](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L85-L90), [README.md#L10-L15](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L10-L15) (`clm_647dc2d8eb48c5ce422dbc69c49274bba6739a78d93fe4d639e85772aa58c67a`)
- [observation/documented] Repository development practice: complete uninstall instructions cover removing the global npm package plus ~/.devx and ~/.devxrc.json on Unix-like systems, with equivalent PowerShell commands for Windows. -- evidence: [README.md#L94-L94](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L94-L94), [README.md#L101-L101](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L101-L101), [README.md#L104-L105](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L104-L105) (`clm_73968487dbe74d608c459431c1c8cf6c4ad171b434f614925c61bb0ead017399`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI is launched as `devx`, supports starting in PLAN mode via `--plan`, and offers a headless one-shot mode using `-p "<prompt>"` with an optional `--yolo` flag. -- evidence: [README.md#L117-L126](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L117-L126) (`clm_697c5b6ca788b72153db48dbd62f0686e5bd2a31a647728d7da6306bdce4ca87`)
- [observation/documented] A slash-command palette (opened by typing `/`) includes commands such as /plan, /agent, /mcp, /usage, /export, /theme, /doctor, /image, /serve, /memory, /undo, /diff, /commit, /status, /session, /resume, /settings, and /update. -- evidence: [README.md#L134-L161](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L134-L161), [README.md#L132-L132](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L132-L132) (`clm_f80693ebb1d80b677fa015b376cda64483823569f1efe7660f225169f263e9df`)
- [observation/documented] Keybindings include Tab to toggle PLAN/AGENT modes, Ctrl+P/Ctrl+V for clipboard image paste, @filename fuzzy file autocomplete, atomic Backspace deletion of paste badges, and Ctrl+C to stop generation. -- evidence: [README.md#L167-L171](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L167-L171) (`clm_b0a51910994376a3d6e37d3266297c88f66c516546ba8368a9bb35a09d10b6c6`)

## memory-state (2 claim(s))

- [observation/documented] A persistent project memory bank is stored in `.devx/memory.md` and managed with `/memory add <rule>`, intended to carry project context across sessions. -- evidence: [README.md#L31-L54](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L31-L54) (`clm_674c4aac145bb50f5c1325440e0ee220aa249d1587f432ddee19e51c7548306a`)
- [observation/documented] Sessions are saved and can be listed, resumed, or deleted via /resume, /session, and /session del; /resume reportedly renders the last 20 messages of a session. -- evidence: [README.md#L134-L161](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L134-L161), [README.md#L31-L54](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L31-L54) (`clm_6c87ec4d608e6d162a21a77e5a0abd4e5cbd20be8e82ffe72ddf5855c60d8f99`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project requires Node.js v20.0.0 or higher and a package manager (npm, pnpm, or yarn); it is distributed as the npm package termux-dev and is MIT licensed. -- evidence: [README.md#L66-L68](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L66-L68), [README.md#L61-L62](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L61-L62), [README.md#L10-L15](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L10-L15), [README.md#L339-L339](https://github.com/apvcode/Termux-Dev/blob/a87cf5f6433248e360a4fe3ad822d8fb55fef1db/README.md#L339-L339) (`clm_6b368929b40b0920853f3510b3220b797cb78986a2e658282c605f598f117575`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

