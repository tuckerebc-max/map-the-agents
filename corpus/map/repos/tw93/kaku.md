# tw93/kaku

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 2b1b4c5906d0 @ e836c39c5c341f82

## Summary (orientation draft, not independently verified)

Kaku is an AI-friendly Mac terminal with sensible defaults, built on WezTerm with fonts, themes, shell integration, and Mac shortcuts preconfigured. The product exposes WezTerm's Lua configuration system so users can customize fonts, themes, shortcuts, and terminal behavior; e.g. window transparency via `config.window_background_opacity` in `~/.config/kaku/kaku.lua`.

## Source coverage

Source coverage (partial): 3 of 13 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Kaku is an AI-friendly Mac terminal with sensible defaults, built on WezTerm with fonts, themes, shell integration, and Mac shortcuts preconfigured. -- evidence: [README.md#L21-L21](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L21-L21), [README.md#L1-L5](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L1-L5)
- components (1 claim(s)):
  - [observation/documented] The AI assistant supports failed-command fix suggestions (applied with Cmd+Shift+E), natural-language `# <description>` to command generation, chat over terminal output and project files, and settings for tools like Claude Code, Codex, Gemini CLI, Copilot CLI, and Kimi Code. -- evidence: [README.md#L72-L75](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L72-L75)
- design-choices (1 claim(s)):
  - [observation/documented] The product exposes WezTerm's Lua configuration system so users can customize fonts, themes, shortcuts, and terminal behavior; e.g. window transparency via `config.window_background_opacity` in `~/.config/kaku/kaku.lua`. -- evidence: [README.md#L83-L83](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L83-L83), [README.md#L37-L43](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L37-L43)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors verify changes with make targets (fmt, fmt-check, check, test, app) and release scripts; `make fmt` requires the nightly toolchain, and `make check` does not run clippy, which CI checks separately. -- evidence: [AGENTS.md#L26-L37](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/AGENTS.md#L26-L37), [AGENTS.md#L39-L39](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/AGENTS.md#L39-L39), [AGENTS.md#L109-L119](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/AGENTS.md#L109-L119)
  - [observation/documented] Repository development practice: CI runs fmt, check, tests, and log/prompt guards on pushes to main and pull requests, with paths-ignore for markdown and assets so docs-only changes skip CI; clippy and a relay-check job gate separately. -- evidence: [AGENTS.md#L7-L22](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/AGENTS.md#L7-L22), [AGENTS.md#L109-L119](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/AGENTS.md#L109-L119)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The `kaku` CLI includes subcommands such as `kaku init` for optional tool setup, `kaku --version`, `kaku ai` for AI service configuration, `kaku chat`, `kaku config`, and `kaku doctor`. -- evidence: [README.md#L33-L33](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L33-L33), [README.md#L72-L75](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L72-L75), [README.md#L91-L95](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L91-L95), [README.md#L70-L70](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L70-L70)
  - [observation/documented] The terminal provides documented keyboard shortcuts including Cmd+T (new tab), Cmd+D / Cmd+Shift+D (pane splits), Cmd+, (settings), Cmd+Shift+A / Cmd+L (AI panel and chat), and Cmd+Click to open URLs or file paths. -- evidence: [README.md#L47-L64](https://github.com/tw93/Kaku/blob/2b1b4c5906d0bd06436b53213f50dd830c23ec75/README.md#L47-L64)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](kaku.detail.md)

Metadata and full claim list: [full detail](kaku.detail.md)
Human notes ([notes](kaku.notes.md), never overwritten by build)

[Back to map index](../../index.md)
