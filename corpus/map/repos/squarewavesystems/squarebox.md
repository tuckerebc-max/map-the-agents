# squarewavesystems/squarebox

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8c1f97fcfb57 @ 49d1143036d8e9ff

## Summary (orientation draft, not independently verified)

README and one ADR describe squarebox, a Docker/Podman container packaging CLI/TUI tools, AI coding assistants, and SDKs with lifecycle commands (sqrbx-*), persistent state via a named volume, and fail-closed artifact installation. Evidence is documentation-only; no dev-practice or evaluation material appears. Evidence coverage: 132 of 156 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 24 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] squarebox packages a terminal development environment—CLI tools, AI coding assistants, language SDKs, and shell aliases—into a single Docker container (Podman experimental), runnable on desktop, VPS, or Codespace. -- evidence: [README.md#L8-L12](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L8-L12)
- components (2 claim(s)):
  - [observation/documented] The image ships CLI tools including bat, delta, difftastic, eza, fd, fzf, gh, glow, jq, just, mise, nano, ripgrep, starship, and bubblewrap (used by the Codex CLI sandbox). -- evidence: [README.md#L222-L243](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L222-L243)
  - [observation/documented] Optional first-run selections include AI assistants (Claude Code, Copilot CLI, Gemini CLI, Codex CLI, opencode, Pi, Oh My Pi), editors (micro, edit, fresh, helix, nvim), TUI tools, and multiplexers (tmux, zellij, herdr). -- evidence: [README.md#L272-L278](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L272-L278), [README.md#L297-L301](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L297-L301), [README.md#L256-L265](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L256-L265), [README.md#L286-L291](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L286-L291)
- design-choices (3 claim(s)):
  - [observation/documented] The box defines opinionated aliases (ls→eza, cat→bat, git shorthands) and generates *-yolo aliases for selected AI tools that disable approval prompts; codex-yolo additionally disables Codex's sandbox. -- evidence: [README.md#L371-L395](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L371-L395), [README.md#L397-L400](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L397-L400)
  - [observation/documented] SDKs are managed exclusively through mise, with selections written to ~/.config/mise/config.toml and shims wired into bash, zsh, and fish via mise activate. -- evidence: [README.md#L337-L340](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L337-L340)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Installers accept flags --build, --edge, --adopt, --verbose and environment variables such as SQUAREBOX_DIR, SQUAREBOX_TAG, SQUAREBOX_RUNTIME, PUID/PGID, and non-interactive toolset selectors like SQUAREBOX_AI and SQUAREBOX_SDKS. -- evidence: [README.md#L97-L107](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L97-L107), [README.md#L94-L95](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L94-L95), [README.md#L113-L120](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L113-L120)
  - [observation/documented] Inside the container, sqrbx-setup re-runs the configuration wizard (sections git, github, ai, editors, tuis, multiplexers, sdks, shell), sqrbx-update manages tool updates, and sqrbx-help lists the sqrbx-* commands. -- evidence: [README.md#L362-L366](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L362-L366), [README.md#L449-L449](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L449-L449), [README.md#L353-L357](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L353-L357)
- memory-state (1 claim(s)):
  - [observation/documented] Per-user state (shell history, GitHub CLI auth, AI-assistant data, mise toolchains) lives in the squarebox-home named Docker volume that survives container replacement, while code lives on the host at the workspace bind mount. -- evidence: [README.md#L179-L186](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L179-L186), [README.md#L206-L210](https://github.com/SquareWaveSystems/squarebox/blob/8c1f97fcfb571473ea85251e78e5f020017e6d4f/README.md#L206-L210)
- orchestration (1 claim(s)):
More evidence: [full detail](squarebox.detail.md)

Metadata and full claim list: [full detail](squarebox.detail.md)
Human notes ([notes](squarebox.notes.md), never overwritten by build)

[Back to map index](../../index.md)
