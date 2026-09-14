# hyperaiteam/clitrigger -- full detail

[Back to orientation](clitrigger.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/hyperaiteam/clitrigger/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/2cd220238205759b.json](../../../wiki/dossiers/hyperaiteam/clitrigger/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/2cd220238205759b.json)

## specifications (1 claim(s))

- [observation/documented] CLITrigger is described as an IDE for AI CLI agents, unifying docs, plans, terminals, autonomous agents, and git into one workspace instead of five scattered tools. -- evidence: [README.md#L9-L9](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L9-L9), [README.md#L11-L11](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L11-L11) (`clm_f5af571164d34eee0f755d1b16eff8109c4efaee79f58fcd241013caa77672b4`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The product is organized around a five-stage pipeline — Docs, Plan, Terminal, Autonomous Tasks, Version Control — where each stage consumes the previous stage's context, with lessons feeding back into docs. -- evidence: [README.md#L73-L73](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L73-L73), [README.md#L45-L51](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L45-L51), [README.md#L53-L60](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L53-L60) (`clm_d0b6452cc89868c6017a62f6866c4a0f8fdadbeefeb3febb9adb5a3d04cd11c4`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: running from source involves cloning, npm install in root and src/client, copying .env.example to .env, and `npm run dev` with the dev server at localhost:5173; tests run via `npm test` or scripts/test.bat. -- evidence: [README.md#L280-L285](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L280-L285), [README.md#L258-L259](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L258-L259), [README.md#L247-L250](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L247-L250), [README.md#L253-L253](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L253-L253), [README.md#L261-L261](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L261-L261), [README.md#L267-L274](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L267-L274) (`clm_b7ad30713d375143d8ff701028221e480c29f59bfe4ac4a652cf2ee989262546`)
- [observation/documented] Repository development practice: contributors are invited to file issues, open PRs (starting with 'good first issue' labels), and share workflows in Discussions; docs include CICD.md for GitHub Actions CI/CD and TESTING.md. -- evidence: [README.md#L334-L336](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L334-L336), [README.md#L318-L324](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L318-L324) (`clm_d8367185a792a2bd37202cf94ef2ead0f25a45e5b89574d8545b1a4715057248`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] An MCP server exposes CLITrigger over HTTP so MCP clients like Claude Desktop or Claude Code can list projects, create and run tasks, and check status; config (URL + token) is copied from Settings. -- evidence: [README.md#L183-L183](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L183-L183) (`clm_423517dc21921beaa51919df3b3ae53c85df4752e1902f9e9c5d7f8f2e6bbbb9`)
- [observation/documented] The CLI supports configuration commands such as `clitrigger config port 8080` to change the port and `clitrigger config tunnel on` to enable Cloudflare tunnel sharing. -- evidence: [README.md#L231-L233](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L231-L233) (`clm_41a7b15c702f4d49687c0aee5d4efa3f0d4a36d96f279b6a73e1f5990b9c6597`)
- [observation/documented] The web UI includes a browser-based Git client for staging, committing, pushing, and managing branches and diffs, plus a keyboard-driven morning review queue for triaging overnight TODOs. -- evidence: [README.md#L156-L156](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L156-L156), [README.md#L153-L153](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L153-L153) (`clm_737eb151c36bd60655ceddc02cef5f66989ced4456e01374d1d7631649ba02c9`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (3 claim(s))

- [observation/documented] Each TODO runs in its own isolated git worktree, with Claude, Antigravity, and Codex executing in parallel, plus dependency chains and merge control. -- evidence: [README.md#L77-L80](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L77-L80), [README.md#L129-L129](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L129-L129) (`clm_9af4c9128b2828cb9a3f721e0d573ec6f6ac0b2e1882b6b653705f01e004311e`)
- [observation/documented] A multi-agent discussion feature has architect, developer, and reviewer agents debate before implementation, then commit code or send action items to the planner. -- evidence: [README.md#L132-L132](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L132-L132), [README.md#L77-L80](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L77-L80) (`clm_42b405f9d38406b46a804a7e1a2ab184d6a9e12de520ca07e7ac1400d1b362df`)
- [observation/documented] Tasks can run on cron or one-off schedules, with automatic retry at the rate-limit reset time. -- evidence: [README.md#L140-L140](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L140-L140), [README.md#L77-L80](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L77-L80) (`clm_17a463ac0ad9b26cf0915ce118d1ecb68f5d47ccc376ff231d8d742b83de700a`)

## tools-permissions (1 claim(s))

- [observation/documented] A strict sandbox mode confines file access to the worktree; the AI CLI (Claude/Antigravity/Codex) can be chosen per project, TODO, or agent. -- evidence: [README.md#L148-L148](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L148-L148) (`clm_7b6666f3927420da85480a76a717dbf049424828059df8c41fa4fe859032c16a`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The documented stack: Node.js/Express/TypeScript/SQLite/WebSocket backend, React 18/Vite/Tailwind/Recharts frontend, simple-git for worktrees, node-cron for scheduling, node-pty and xterm.js for terminals, and optional Cloudflare Tunnel. -- evidence: [README.md#L189-L197](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L189-L197) (`clm_f607375b6d0d652980ffddd426c393d1624608c2e82976e34f0ac2c9bc6e2eba`)
- [observation/documented] Prerequisites are Node.js 22+ (LTS recommended), Git, and at least one AI CLI (Claude, Antigravity, or Codex); the desktop app bundles Node.js and native modules like better-sqlite3 and node-pty. -- evidence: [README.md#L235-L238](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L235-L238), [README.md#L211-L211](https://github.com/HyperAITeam/CLITrigger/blob/d9dabe2c719d7e04c8e2e784305d6553334cc6e2/README.md#L211-L211) (`clm_75de7558ef2e45b03050bfd12d5ef911d089c7036062753b94d64ea9b2227df3`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

