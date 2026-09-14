# agent-of-empires/agent-of-empires -- full detail

[Back to orientation](agent-of-empires.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/agent-of-empires/agent-of-empires/bdf21c256673c10cdf8e548a6a652b1bedf621cb/22bc1106b960b799.json](../../../wiki/dossiers/agent-of-empires/agent-of-empires/bdf21c256673c10cdf8e548a6a652b1bedf621cb/22bc1106b960b799.json)

## specifications (1 claim(s))

- [observation/documented] AoE is described as a session manager for AI coding agents on Linux and macOS, running agents in parallel across branches with persistent sessions and optional worktree or container isolation. -- evidence: [README.md#L25-L27](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/README.md#L25-L27) (`clm_53e4b08c3ca90b122284cbbf1ff159126de02cb17b279e4880d5a17d22b48c19`)

## components (1 claim(s))

- [observation/documented] The product exposes TUI, web, CLI, and HTTP API surfaces, with status detection, notifications, persistent tmux sessions, git worktrees, multi-repo workspaces, and Docker/Podman/Apple Containers sandboxing. -- evidence: [README.md#L52-L57](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/README.md#L52-L57) (`clm_3c30ecddfee0b9a69b8e49f97128fd9594ff50b02f46c6d6d1942bdcc9975751`)

## design-choices (1 claim(s))

- [observation/documented] Configuration is layered: global config, per-profile config, and repo-level .agent-of-empires/config.toml, with later layers overriding earlier ones only for explicitly set fields. -- evidence: [docs/guides/configuration.md#L9-L9](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/guides/configuration.md#L9-L9), [docs/guides/configuration.md#L5-L7](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/guides/configuration.md#L5-L7), [docs/guides/configuration.md#L3-L3](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/guides/configuration.md#L3-L3) (`clm_8a9aa4196aa788aebf4c267c42ab6ad1a199421c24621c2e6c14c32e4029c598`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README's Development section lists cargo build, cargo test, cargo fmt, cargo clippy, and cargo build --features web, with docs/development.md as the full reference. -- evidence: [README.md#L145-L145](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/README.md#L145-L145), [README.md#L137-L143](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/README.md#L137-L143) (`clm_05a07e1178e8c5e7d9ded916316bfc503229a19baf78017ffda9dd363ecdfea1`)

## skills-patterns (2 claim(s))

- [observation/documented] AoE discovers Agent Skills packages from a managed store and user-level agent directories (e.g. ~/.claude/skills, ~/.agents/skills, ~/.gemini/skills); a skill is a directory with a SKILL.md containing name and description frontmatter. -- evidence: [docs/api.md#L25-L28](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L25-L28), [docs/api.md#L32-L40](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L32-L40) (`clm_e11b39d8b2fbcd856ced9908a2d0d741b702180dd5852ed46954256e297b99e0`)
- [observation/documented] Skill sync propagates managed skills into agents' own directories with a never-overwrite rule: hand-edited copies are reported as conflicts and left untouched unless explicitly named in a `replace` list; automatic syncs never replace anything. -- evidence: [docs/api.md#L147-L154](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L147-L154), [docs/api.md#L130-L130](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L130-L130), [docs/api.md#L122-L128](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L122-L128) (`clm_2a131aa5ca522dc99601d54d6a811461b6c9497152a456bdeada6cbcdf4018c0`)

## interfaces (3 claim(s))

- [observation/documented] `aoe serve` exposes an HTTP API so external orchestrators such as other agents, MCP tools, or CI scripts can drive sessions without attaching to a terminal; the web dashboard uses the same API plus internal routes. -- evidence: [docs/api.md#L3-L6](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L3-L6) (`clm_7113bde0f45b0da92bbb4996fd1f6dbab00a8bb93db8c3aed13e2e5f26bd835f`)
- [observation/documented] Session status values are PascalCase on the wire (Starting, Running, Waiting, Idle, Error, Stopped, Unknown, Deleting, Creating), differing from the lowercase form used by the CLI and status-hook env vars. -- evidence: [docs/api.md#L204-L209](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L204-L209), [docs/api.md#L211-L221](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L211-L221) (`clm_a6811946eda9ac369ac397b5883cacc6cfaaa6cf2c204704cda8ef51fd81ae30`)
- [observation/documented] GET /api/sessions/{id}/output returns a tmux pane snapshot with configurable trailing-line count (clamped 1..=2000) and text or ansi format, and works under read-only mode. -- evidence: [docs/api.md#L324-L327](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L324-L327), [docs/api.md#L339-L340](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L339-L340) (`clm_ad41e2d9e7e91d51623c3539bec180871338261fee67b92bd0280621cb5c1f93`)

## memory-state (1 claim(s))

- [observation/documented] Each agent runs in its own tmux session, so sessions persist when the TUI closes, SSH disconnects, or the terminal crashes; sessions are only removed when explicitly deleted. -- evidence: [README.md#L117-L117](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/README.md#L117-L117), [README.md#L65-L65](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/README.md#L65-L65) (`clm_808c47044ffa994cf6887b5978fb0bc576968d4b56b9190a6fd00e1889727a7a`)

## orchestration (2 claim(s))

- [observation/documented] POST /api/sessions supports callback_url (fired on Waiting/Idle/Error transitions with loopback/private address rejection and fire-and-forget delivery) and idempotency_key so retries return the existing session instead of duplicating it. -- evidence: [docs/api.md#L248-L251](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L248-L251) (`clm_6157dcd8aa7837420527ecf6abe3255d81d8ade69b6438cef458dca2553578f5`)
- [observation/documented] The send and output endpoints together form a documented primitive for driving an AoE session as a controlled subagent: send a prompt, poll output until stable or status returns to Idle, then capture the reply. -- evidence: [docs/api.md#L355-L359](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L355-L359), [docs/api.md#L352-L353](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L352-L353) (`clm_cd49d6f3f5ff4ea1ea8c43a96af2cc9d4596ccc1b141ad622b664bccef1825fd`)

## tools-permissions (1 claim(s))

- [observation/documented] All HTTP endpoints require a token unless the server starts with --no-auth; the token is printed by `aoe serve` and accepted via bearer header, query parameter, or cookie. A --read-only mode blocks write endpoints with 403. -- evidence: [docs/api.md#L20-L21](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L20-L21), [docs/api.md#L10-L12](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L10-L12), [docs/api.md#L14-L18](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/docs/api.md#L14-L18) (`clm_85e23c8e780bebe07c64698b34364a98dd16ff6259c98d519d335c97b2e64bf6`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] tmux is a required prerequisite and Docker is optional for sandboxing; the project is built with cargo, and native Windows is unsupported because AoE depends on tmux and POSIX process handling (WSL2 only). -- evidence: [README.md#L71-L71](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/README.md#L71-L71), [README.md#L86-L88](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/README.md#L86-L88), [README.md#L129-L129](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/README.md#L129-L129) (`clm_699d4bde830e954b2e3c8af759257034d25781422d9e591e222b18c6a0dc934f`)
- [observation/documented] The project is MIT licensed, with one file (src/tui/hyperlink.rs) containing code derived from the herdr project under Apache License 2.0. -- evidence: [README.md#L157-L157](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/README.md#L157-L157), [README.md#L159-L162](https://github.com/agent-of-empires/agent-of-empires/blob/bdf21c256673c10cdf8e548a6a652b1bedf621cb/README.md#L159-L162) (`clm_8b08a05cf45d14ccc99b06a37c22da5d09aa63970b0f2b0f29c7c5440b2ef0af`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

