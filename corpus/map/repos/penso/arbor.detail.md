# penso/arbor -- full detail

[Back to orientation](arbor.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/penso/arbor/d8d82b7eec6cba3682374875d8f13407c7181ef0/d474fbdce083e54b.json](../../../wiki/dossiers/penso/arbor/d8d82b7eec6cba3682374875d8f13407c7181ef0/d474fbdce083e54b.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (4 claim(s))

- [observation/documented] Arbor is a fully native agentic-coding app built with Rust and GPUI, with a shared daemon powering the desktop app, web UI, CLI, and MCP server. -- evidence: [README.md#L18-L19](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L18-L19), [README.md#L23-L25](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L23-L25) (`clm_cbd69af5384e250e8f707a97989e029c7e9d161e5cb89dfdc8a5930107bff01c`)
- [observation/documented] The workspace includes crates such as arbor-core, arbor-gui, arbor-httpd, arbor-mcp, arbor-cli, arbor-mosh, arbor-ssh, arbor-symphony, arbor-terminal-emulator, and arbor-web-ui. -- evidence: [README.md#L137-L150](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L137-L150) (`clm_518fdf5eb52cd03610d211627acb375cc5b45a1dd96a2914a31ab85b85c18971`)
- [observation/documented] The app manages worktrees across repositories, including creation from GitHub/GitLab issues, branch naming rules, delete confirmation with unpushed-commit detection, and issue linking to branches and PRs. -- evidence: [README.md#L30-L38](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L30-L38) (`clm_89daf8847ae49389cd321c29e7367ae2c10a6c5b56d5c3f3cebb2adac0f36ada`)
- [observation/documented] Arbor embeds a PTY terminal with truecolor and xterm-256color support, multiple tabs per worktree, persistent daemon-based sessions, and managed processes from Procfile and arbor.toml. -- evidence: [README.md#L41-L49](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L41-L49) (`clm_28d1085fd35bdbec1c2f178a8c51be43c06fbe4684a00b55bb77862616f6c819`)

## design-choices (2 claim(s))

- [observation/documented] Repo-local behavior is configured via <repo>/arbor.toml, which supplies presets, managed processes, worktree scripts, scheduled tasks, branch naming rules, agent defaults, and notification routing. -- evidence: [README.md#L154-L155](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L154-L155) (`clm_4e6eb13a9a87f123e0a4c681dbe1ac38880ca7e9c4e8247d1137033f471148dc`)
- [observation/documented] An experimental embedded Ghostty terminal engine is opt-in behind the ghostty-vt-experimental feature flag and disabled by default; when built in, it is used by default and selectable via config. -- evidence: [README.md#L309-L311](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L309-L311), [README.md#L300-L301](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L300-L301), [README.md#L41-L49](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L41-L49) (`clm_f5177d924f1ea27acf10b95dba4332de1deb54cc8134e5c421fad650e0184c60`)

## workflows (5 claim(s))

- [observation/documented] Repository development practice: AGENTS.md instructs coding agents to run just format and just lint before committing, prefer just recipes, and run relevant checks for touched code before handoff. -- evidence: [AGENTS.md#L13-L16](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/AGENTS.md#L13-L16) (`clm_1e8864d4bbd86577feffb3445a16134bf099a794f3e50df25b84e14cdb9ec3ee`)
- [observation/documented] Repository development practice: CLAUDE.md requires just format, just lint (zero warnings), and just test before committing, and forbids Co-Authored-By trailers in conventional commits. -- evidence: [CLAUDE.md#L29-L31](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/CLAUDE.md#L29-L31), [CLAUDE.md#L33-L34](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/CLAUDE.md#L33-L34), [CLAUDE.md#L38-L39](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/CLAUDE.md#L38-L39) (`clm_1e1a0befdb0e4fd8a217f904ef8da3fbd1c6b7f562c9b0386e78ed353b39c0b0`)
- [observation/documented] Repository development practice: the project uses bd (beads) for all issue tracking, with bd ready/claim/close commands and discovered-from dependency links instead of markdown TODOs. -- evidence: [AGENTS.md#L200-L205](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/AGENTS.md#L200-L205), [AGENTS.md#L217-L223](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/AGENTS.md#L217-L223), [AGENTS.md#L145-L145](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/AGENTS.md#L145-L145) (`clm_0fdf1a0da26b64c9ec94532109788a9e343319079875e27d7592a8169e781b48`)
- [observation/documented] Repository development practice: Rust rules forbid unwrap()/expect() outside tests, require SessionId/WorkspaceId newtypes, and prohibit shelling out to CLIs like gh or git for GitHub API calls in favor of Rust crates. -- evidence: [CLAUDE.md#L43-L49](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/CLAUDE.md#L43-L49), [AGENTS.md#L48-L53](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/AGENTS.md#L48-L53) (`clm_f44e363f3102d4abd8d5b5753aee83f7259d20a01a79197f19b4b3226bd390ca`)
- [observation/documented] Repository development practice: UI changes are implemented in the native GPUI app first, then ported to the web UI to keep the two surfaces in parity, with screenshot-based verification via screencapture. -- evidence: [CLAUDE.md#L88-L88](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/CLAUDE.md#L88-L88), [CLAUDE.md#L92-L92](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/CLAUDE.md#L92-L92), [AGENTS.md#L20-L23](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/AGENTS.md#L20-L23), [AGENTS.md#L115-L115](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/AGENTS.md#L115-L115) (`clm_880295c9cad60a9094632fa898cf13ae9400a6b5606405bcf54542f11b930f5f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] arbor-cli exposes daemon-backed health, repo, worktree, terminal, process, and task commands, with JSON output options like worktrees list --json. -- evidence: [README.md#L76-L87](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L76-L87), [README.md#L208-L213](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L208-L213) (`clm_dfd3976276f697e81335961fc16d0dbb4b36b832acefc0466d12a9f39071d4ee`)
- [observation/documented] arbor-mcp is a stdio MCP server enabled by the crate's default stdio-server feature, talking to arbor-httpd, which must be reachable first. -- evidence: [README.md#L217-L217](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L217-L217) (`clm_92151ef64b8e5f361a3ceb4794595924f35ad96305ae18cb9fd66cf2599895f8`)
- [observation/documented] Agent chat supports ACP agents (Claude, Codex, Pi, Gemini via acpx) and OpenAI-compatible /v1/chat/completions providers, with SSE streaming and startup model discovery via /v1/models. -- evidence: [README.md#L60-L67](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L60-L67) (`clm_4bdba20c71d5eeb96a18f1155a673484fa1bb3cc160b4e15343e82e962dbac57`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Daemon access control: loopback requests need no token, while non-loopback requests require an Authorization bearer token configured via ARBOR_DAEMON_AUTH_TOKEN. -- evidence: [README.md#L237-L237](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L237-L237), [README.md#L227-L228](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L227-L228), [README.md#L232-L235](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L232-L235) (`clm_2759cd6bf99ff1b03149118eac877b099c4267b0c488d84c849176012a6a2119`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project targets Rust nightly-2025-11-30 and uses the just task runner; UI icons require a Caskaydia/Cascadia Nerd Font variant. -- evidence: [README.md#L266-L268](https://github.com/penso/arbor/blob/d8d82b7eec6cba3682374875d8f13407c7181ef0/README.md#L266-L268) (`clm_fc34099f5cec000a7681859f64302961db1588de9cc8d95b410f9487ae0f38b7`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

