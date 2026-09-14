# agent-of-empires/agent-of-empires

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: njbrake/agent-of-empires (github id 1131238324).
Latest snapshot: commit bdf21c256673 @ 22bc1106b960b799

## Summary (orientation draft, not independently verified)

Agent of Empires (AoE) is a Rust-based session manager for AI coding agents on Linux/macOS, wrapping tmux sessions with a TUI, web dashboard, CLI, and HTTP API. Evidence covers its runtime features, HTTP API surface, skills management, configuration layering, and development commands. Evidence coverage: 134 of 344 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 56 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] AoE is described as a session manager for AI coding agents on Linux and macOS, running agents in parallel across branches with persistent sessions and optional worktree or container isolation. -- evidence: [README.md#L25-L27](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/README.md#L25-L27)
- components (1 claim(s)):
  - [observation/documented] The product exposes TUI, web, CLI, and HTTP API surfaces, with status detection, notifications, persistent tmux sessions, git worktrees, multi-repo workspaces, and Docker/Podman/Apple Containers sandboxing. -- evidence: [README.md#L52-L57](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/README.md#L52-L57)
- design-choices (1 claim(s)):
  - [observation/documented] Configuration is layered: global config, per-profile config, and repo-level .agent-of-empires/config.toml, with later layers overriding earlier ones only for explicitly set fields. -- evidence: [docs/guides/configuration.md#L9-L9](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/guides/configuration.md#L9-L9), [docs/guides/configuration.md#L5-L7](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/guides/configuration.md#L5-L7), [docs/guides/configuration.md#L3-L3](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/guides/configuration.md#L3-L3)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README's Development section lists cargo build, cargo test, cargo fmt, cargo clippy, and cargo build --features web, with docs/development.md as the full reference. -- evidence: [README.md#L145-L145](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/README.md#L145-L145), [README.md#L137-L143](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/README.md#L137-L143)
- skills-patterns (2 claim(s)):
  - [observation/documented] AoE discovers Agent Skills packages from a managed store and user-level agent directories (e.g. ~/.claude/skills, ~/.agents/skills, ~/.gemini/skills); a skill is a directory with a SKILL.md containing name and description frontmatter. -- evidence: [docs/api.md#L25-L28](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L25-L28), [docs/api.md#L32-L40](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L32-L40)
  - [observation/documented] Skill sync propagates managed skills into agents' own directories with a never-overwrite rule: hand-edited copies are reported as conflicts and left untouched unless explicitly named in a `replace` list; automatic syncs never replace anything. -- evidence: [docs/api.md#L147-L154](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L147-L154), [docs/api.md#L130-L130](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L130-L130), [docs/api.md#L122-L128](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L122-L128)
- interfaces (3 claim(s)):
  - [observation/documented] `aoe serve` exposes an HTTP API so external orchestrators such as other agents, MCP tools, or CI scripts can drive sessions without attaching to a terminal; the web dashboard uses the same API plus internal routes. -- evidence: [docs/api.md#L3-L6](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L3-L6)
  - [observation/documented] Session status values are PascalCase on the wire (Starting, Running, Waiting, Idle, Error, Stopped, Unknown, Deleting, Creating), differing from the lowercase form used by the CLI and status-hook env vars. -- evidence: [docs/api.md#L204-L209](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L204-L209), [docs/api.md#L211-L221](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L211-L221)
- memory-state (1 claim(s)):
More evidence: [full detail](agent-of-empires.detail.md)

Metadata and full claim list: [full detail](agent-of-empires.detail.md)
Human notes ([notes](agent-of-empires.notes.md), never overwritten by build)

[Back to map index](../../index.md)
