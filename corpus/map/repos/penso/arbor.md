# penso/arbor

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d8d82b7eec6c @ d474fbdce083e54b

## Summary (orientation draft, not independently verified)

Arbor is a native Rust/GPUI desktop app for agentic coding, backed by a shared daemon that also powers a web UI, CLI, and MCP server. Evidence covers product features (worktrees, terminals, agent chat, MCP), configuration, and contributor workflow rules in AGENTS.md/CLAUDE.md.

## Source coverage

Source coverage (partial): 3 of 20 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (4 claim(s)):
  - [observation/documented] Arbor is a fully native agentic-coding app built with Rust and GPUI, with a shared daemon powering the desktop app, web UI, CLI, and MCP server. -- evidence: [README.md#L18-L19](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L18-L19), [README.md#L23-L25](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L23-L25)
  - [observation/documented] The workspace includes crates such as arbor-core, arbor-gui, arbor-httpd, arbor-mcp, arbor-cli, arbor-mosh, arbor-ssh, arbor-symphony, arbor-terminal-emulator, and arbor-web-ui. -- evidence: [README.md#L137-L150](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L137-L150)
- design-choices (2 claim(s)):
  - [observation/documented] Repo-local behavior is configured via <repo>/arbor.toml, which supplies presets, managed processes, worktree scripts, scheduled tasks, branch naming rules, agent defaults, and notification routing. -- evidence: [README.md#L154-L155](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L154-L155)
  - [observation/documented] An experimental embedded Ghostty terminal engine is opt-in behind the ghostty-vt-experimental feature flag and disabled by default; when built in, it is used by default and selectable via config. -- evidence: [README.md#L309-L311](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L309-L311), [README.md#L300-L301](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L300-L301), [README.md#L41-L49](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L41-L49)
- workflows (5 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs coding agents to run just format and just lint before committing, prefer just recipes, and run relevant checks for touched code before handoff. -- evidence: [AGENTS.md#L13-L16](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/AGENTS.md#L13-L16)
  - [observation/documented] Repository development practice: CLAUDE.md requires just format, just lint (zero warnings), and just test before committing, and forbids Co-Authored-By trailers in conventional commits. -- evidence: [CLAUDE.md#L29-L31](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/CLAUDE.md#L29-L31), [CLAUDE.md#L33-L34](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/CLAUDE.md#L33-L34), [CLAUDE.md#L38-L39](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/CLAUDE.md#L38-L39)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] arbor-cli exposes daemon-backed health, repo, worktree, terminal, process, and task commands, with JSON output options like worktrees list --json. -- evidence: [README.md#L76-L87](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L76-L87), [README.md#L208-L213](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L208-L213)
  - [observation/documented] arbor-mcp is a stdio MCP server enabled by the crate's default stdio-server feature, talking to arbor-httpd, which must be reachable first. -- evidence: [README.md#L217-L217](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L217-L217)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Daemon access control: loopback requests need no token, while non-loopback requests require an Authorization bearer token configured via ARBOR_DAEMON_AUTH_TOKEN. -- evidence: [README.md#L237-L237](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L237-L237), [README.md#L227-L228](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L227-L228), [README.md#L232-L235](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L232-L235)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The project targets Rust nightly-2025-11-30 and uses the just task runner; UI icons require a Caskaydia/Cascadia Nerd Font variant. -- evidence: [README.md#L266-L268](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L266-L268)
More evidence: [full detail](arbor.detail.md)

Metadata and full claim list: [full detail](arbor.detail.md)
Human notes ([notes](arbor.notes.md), never overwritten by build)

[Back to map index](../../index.md)
