# tw93/kaku -- full detail

[Back to orientation](kaku.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tw93/kaku/2b1b4c5906d0bd06436b53213f50dd830c23ec75/e836c39c5c341f82.json](../../../wiki/dossiers/tw93/kaku/2b1b4c5906d0bd06436b53213f50dd830c23ec75/e836c39c5c341f82.json)

## specifications (1 claim(s))

- [observation/documented] Kaku is an AI-friendly Mac terminal with sensible defaults, built on WezTerm with fonts, themes, shell integration, and Mac shortcuts preconfigured. -- evidence: [README.md#L21-L21](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L21-L21), [README.md#L1-L5](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L1-L5) (`clm_6b8439813100ce27786af060f4c1938677a0ad6888c23dff683d9b760b81586b`)

## components (1 claim(s))

- [observation/documented] The AI assistant supports failed-command fix suggestions (applied with Cmd+Shift+E), natural-language `# <description>` to command generation, chat over terminal output and project files, and settings for tools like Claude Code, Codex, Gemini CLI, Copilot CLI, and Kimi Code. -- evidence: [README.md#L72-L75](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L72-L75) (`clm_75e815d4850d769f47eb42bd35195d9ea02beab9605651e381cdd5d6e7b69614`)

## design-choices (1 claim(s))

- [observation/documented] The product exposes WezTerm's Lua configuration system so users can customize fonts, themes, shortcuts, and terminal behavior; e.g. window transparency via `config.window_background_opacity` in `~/.config/kaku/kaku.lua`. -- evidence: [README.md#L83-L83](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L83-L83), [README.md#L37-L43](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L37-L43) (`clm_f1dcfbe583ad4c9ca783e7ceed18125eee96eca1592ca89597e6a5a0d659bfdc`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors verify changes with make targets (fmt, fmt-check, check, test, app) and release scripts; `make fmt` requires the nightly toolchain, and `make check` does not run clippy, which CI checks separately. -- evidence: [AGENTS.md#L26-L37](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/AGENTS.md#L26-L37), [AGENTS.md#L39-L39](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/AGENTS.md#L39-L39), [AGENTS.md#L109-L119](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/AGENTS.md#L109-L119) (`clm_e284be4e4a9c2796e8367470f9186e6c5cd36da6e34408798415e378a16771f7`)
- [observation/documented] Repository development practice: CI runs fmt, check, tests, and log/prompt guards on pushes to main and pull requests, with paths-ignore for markdown and assets so docs-only changes skip CI; clippy and a relay-check job gate separately. -- evidence: [AGENTS.md#L7-L22](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/AGENTS.md#L7-L22), [AGENTS.md#L109-L119](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/AGENTS.md#L109-L119) (`clm_56f97fe51cd609896e25dea16bf5190c5fff51ebec4bce81ed86c6783a039cce`)
- [observation/documented] Repository development practice: releases use `V0.x.x` tags with `scripts/release.sh` as source of truth, release notes titled from `.github/RELEASE_NOTES.md`, and a manual pre-release smoke checklist in `.agents/skills/release/SKILL.md` run on the built app before tagging. -- evidence: [AGENTS.md#L142-L142](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/AGENTS.md#L142-L142), [AGENTS.md#L136-L136](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/AGENTS.md#L136-L136) (`clm_3e6847cf3d6c9bbf4c649d944a9dc4192fd9af4415bf11f167bc31460c1fa388`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The `kaku` CLI includes subcommands such as `kaku init` for optional tool setup, `kaku --version`, `kaku ai` for AI service configuration, `kaku chat`, `kaku config`, and `kaku doctor`. -- evidence: [README.md#L33-L33](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L33-L33), [README.md#L72-L75](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L72-L75), [README.md#L91-L95](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L91-L95), [README.md#L70-L70](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L70-L70) (`clm_623eb519f5c17b60dde57d4387cab802bf14f1e25d6e936c98f257d536c563c8`)
- [observation/documented] The terminal provides documented keyboard shortcuts including Cmd+T (new tab), Cmd+D / Cmd+Shift+D (pane splits), Cmd+, (settings), Cmd+Shift+A / Cmd+L (AI panel and chat), and Cmd+Click to open URLs or file paths. -- evidence: [README.md#L47-L64](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L47-L64) (`clm_581ecdcd0b2c7ac153f3ae241061af97bdea7abc8087d25c751dcab0c3b5c1a2`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Kaku bundles JetBrains Mono, built-in zsh completion, syntax highlighting, and directory jumping, and offers shortcuts for optional Lazygit and Yazi installations; it is derived from WezTerm. -- evidence: [README.md#L21-L21](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L21-L21), [README.md#L37-L43](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L37-L43) (`clm_6fddb6db165884bd87f93d40c74a08e88c2c601afd7eefed68aff5f24454efcb`)

## limitations (2 claim(s))

- [observation/documented] Kaku is macOS-only; the FAQ states there is currently no Windows or Linux version. -- evidence: [README.md#L81-L81](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L81-L81) (`clm_c03120c5222ce1198d97f2679ce8b7fba5dbfa0e04b455d57a4cf15dcac5b872`)
- [observation/documented] Kaku does not provide or relay the AI service itself; users must configure their own AI service via `kaku ai` to use the built-in assistant. -- evidence: [README.md#L70-L70](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L70-L70) (`clm_e71f0622b4cfc55dbaf475e243ff2e2fc35d5609e3f6ac99b8889a650b07ec43`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

