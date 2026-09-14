# maxktz/hitch

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit bcbfca260225 @ a239af80cda50b58

## Summary (orientation draft, not independently verified)

Hitch is a Rust CLI distributed via npm as hitch-cli that shares a user's real terminal with AI coding agents, exposing agent commands like context, send-keys, and capture, with a SKILL.md agent skill and documented contributor workflows.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Hitch is not a terminal multiplexer UI like tmux; the terminal feels like a normal shell while Hitch proxies input/output, records context, and exposes agent-friendly commands. -- evidence: [README.md#L44-L44](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/README.md#L44-L44)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors run `cargo fmt -- --check` and `cargo test` before committing, and build locally with `cargo build --release`. -- evidence: [CONTRIBUTING.md#L9-L12](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/CONTRIBUTING.md#L9-L12), [CONTRIBUTING.md#L16-L18](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/CONTRIBUTING.md#L16-L18), [CONTRIBUTING.md#L7-L7](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/CONTRIBUTING.md#L7-L7)
  - [observation/documented] Repository development practice: releases use `npm run release -- <version>` and a tag push; GitHub Actions then builds native binaries, publishes hitch-cli to npm, and creates a GitHub release. -- evidence: [CONTRIBUTING.md#L24-L27](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/CONTRIBUTING.md#L24-L27), [CONTRIBUTING.md#L29-L29](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/CONTRIBUTING.md#L29-L29)
- skills-patterns (2 claim(s)):
  - [observation/documented] A SKILL.md (version 3) describes when agents should use hitch, e.g. before starting a dev server, watcher, tunnel, REPL, build, or log tail that may already be running. -- evidence: [SKILL.md#L1-L5](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L1-L5)
  - [observation/documented] The skill instructs agents to prefer `hitch context` first, avoid --all by default, use --wait instead of sleep polling, and only use hitch for collaboration rather than short tool calls. -- evidence: [SKILL.md#L99-L106](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L99-L106), [SKILL.md#L77-L77](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L77-L77), [SKILL.md#L29-L32](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L29-L32)
- interfaces (5 claim(s)):
  - [observation/documented] Hitch is a CLI for sharing the user's real terminal with AI coding agents; running `hitch` gives agents terminal context, ability to send keys or commands, and inspect output. -- evidence: [README.md#L40-L40](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/README.md#L40-L40)
  - [observation/documented] The `hitch context` command shows compact terminal state and recent output, with forms for all project terminals, a specific terminal, or `--all` including terminals outside the project. -- evidence: [SKILL.md#L21-L24](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L21-L24), [SKILL.md#L17-L17](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L17-L17)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Hitch refuses by default sending shell commands into terminals with running processes, printing terminal context instead; `--force` overrides this, and a sequence starting with C-c is allowed. -- evidence: [SKILL.md#L99-L106](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/SKILL.md#L99-L106)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Installation is via `npm install -g hitch-cli`; supported platforms are macOS and Linux on arm64 or x64. -- evidence: [README.md#L48-L51](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/README.md#L48-L51), [README.md#L55-L55](https://github.com/maxktz/hitch/blob/bcbfca2602259507245e776e366666fee89f4d6b/README.md#L55-L55)
More evidence: [full detail](hitch.detail.md)

Metadata and full claim list: [full detail](hitch.detail.md)
Human notes ([notes](hitch.notes.md), never overwritten by build)

[Back to map index](../../index.md)
