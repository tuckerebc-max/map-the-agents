# devcorexofficial/core-termux

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 72446370343c @ 422ed5b5e17364df

## Summary (orientation draft, not independently verified)

Core-Termux (v4.27.2, MIT) is a modular dev environment CLI for Termux on Android, exposing a single `core` command with subcommands for module installation, an AI agent, a markdown memory store, env-var management, voice input, PostgreSQL management, and project scaffolding. Evidence coverage: 173 of 248 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The README badges identify the project as version 4.27.2, MIT-licensed, and targeting the Termux/Android platform. -- evidence: [README.md#L11-L21](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L11-L21)
- components (2 claim(s)):
  - [observation/documented] Modules include lang (Node.js, Python, Rust, Go, etc.), db (PostgreSQL, MariaDB, SQLite, MongoDB, Redis), ai, editor, dev, npm, shell, ui, and auto (n8n). -- evidence: [README.md#L92-L102](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L92-L102)
  - [observation/documented] The ai module installs many coding agents via per-agent flags, including Qwen Code, Gemini CLI, Claude Code, Ollama, Codex CLI, and OpenCode, either all at once or selected ones. -- evidence: [README.md#L115-L153](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L115-L153), [README.md#L110-L113](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L110-L113), [README.md#L108-L108](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L108-L108)
- design-choices (2 claim(s)):
  - [observation/documented] The project is designed exclusively for Termux on Android and is documented as not supported on other platforms. -- evidence: [README.md#L48-L49](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L48-L49)
  - [observation/documented] Uninstall and reinstall support per-module and per-tool targeting but deliberately offer no 'uninstall all' or 'reinstall all' operation. -- evidence: [README.md#L545-L545](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L545-L545), [README.md#L523-L523](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L523-L523)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The product exposes a single CLI named `core` with subcommands including install, update, uninstall, reinstall, list, show, open, agent, brain, env, voice, pg, and init. -- evidence: [README.md#L69-L84](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L69-L84), [README.md#L46-L46](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L46-L46)
  - [observation/documented] `core env` interactively manages environment variables in .zshrc or .bashrc, hides typed values with ● characters, and warns before replacing existing variables. -- evidence: [README.md#L233-L233](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L233-L233), [README.md#L244-L247](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L244-L247)
- memory-state (1 claim(s)):
  - [observation/documented] `core brain` stores personal memories as AI-consumable markdown files with frontmatter (title, tags, category, related), organized in category folders, optionally synced to a private GitHub repo via `gh`. -- evidence: [README.md#L306-L313](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L306-L313), [README.md#L285-L285](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L285-L285), [README.md#L322-L326](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L322-L326)
- orchestration (1 claim(s)):
  - [observation/documented] `core agent` is a local AI assistant backed by an OpenAI-compatible endpoint, defaulting to a gemma model served by Cactus Engine at 127.0.0.1:8000/v1; if the server is down it starts cactus in the background and stops it when the interactive shell exits. -- evidence: [README.md#L176-L176](https://github.com/DevCoreXOfficial/core-termux/blob/72446370343cab50c34bb8ee5152082ff031cc61/README.md#L176-L176)
- tools-permissions (1 claim(s)):
More evidence: [full detail](core-termux.detail.md)

Metadata and full claim list: [full detail](core-termux.detail.md)
Human notes ([notes](core-termux.notes.md), never overwritten by build)

[Back to map index](../../index.md)
