---
access: public
aliases: []
claim_ids:
- clm_17a463ac0ad9b26cf0915ce118d1ecb68f5d47ccc376ff231d8d742b83de700a
- clm_41a7b15c702f4d49687c0aee5d4efa3f0d4a36d96f279b6a73e1f5990b9c6597
- clm_423517dc21921beaa51919df3b3ae53c85df4752e1902f9e9c5d7f8f2e6bbbb9
- clm_42b405f9d38406b46a804a7e1a2ab184d6a9e12de520ca07e7ac1400d1b362df
- clm_737eb151c36bd60655ceddc02cef5f66989ced4456e01374d1d7631649ba02c9
- clm_75de7558ef2e45b03050bfd12d5ef911d089c7036062753b94d64ea9b2227df3
- clm_7b6666f3927420da85480a76a717dbf049424828059df8c41fa4fe859032c16a
- clm_9af4c9128b2828cb9a3f721e0d573ec6f6ac0b2e1882b6b653705f01e004311e
- clm_b7ad30713d375143d8ff701028221e480c29f59bfe4ac4a652cf2ee989262546
- clm_d0b6452cc89868c6017a62f6866c4a0f8fdadbeefeb3febb9adb5a3d04cd11c4
- clm_d8367185a792a2bd37202cf94ef2ead0f25a45e5b89574d8545b1a4715057248
- clm_f5af571164d34eee0f755d1b16eff8109c4efaee79f58fcd241013caa77672b4
- clm_f607375b6d0d652980ffddd426c393d1624608c2e82976e34f0ac2c9bc6e2eba
maturity: draft
page_id: pg_f457531d9a75591885cb6a7b8cdd3104
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_fe192eb55d58547c9eb99e490d9f9e26
title: HyperAITeam/CLITrigger/README.md @ d9dabe2c719d
updated_at: '2026-09-14T02:04:38Z'
---

# HyperAITeam/CLITrigger/README.md @ d9dabe2c719d

<!-- rcw:begin owner=source:src_fe192eb55d58547c9eb99e490d9f9e26 block=evidence -->
- Tasks can run on cron or one-off schedules, with automatic retry at the rate-limit reset time. [@claim:clm_17a463ac0ad9b26cf0915ce118d1ecb68f5d47ccc376ff231d8d742b83de700a]
- The CLI supports configuration commands such as `clitrigger config port 8080` to change the port and `clitrigger config tunnel on` to enable Cloudflare tunnel sharing. [@claim:clm_41a7b15c702f4d49687c0aee5d4efa3f0d4a36d96f279b6a73e1f5990b9c6597]
- An MCP server exposes CLITrigger over HTTP so MCP clients like Claude Desktop or Claude Code can list projects, create and run tasks, and check status; config (URL + token) is copied from Settings. [@claim:clm_423517dc21921beaa51919df3b3ae53c85df4752e1902f9e9c5d7f8f2e6bbbb9]
- A multi-agent discussion feature has architect, developer, and reviewer agents debate before implementation, then commit code or send action items to the planner. [@claim:clm_42b405f9d38406b46a804a7e1a2ab184d6a9e12de520ca07e7ac1400d1b362df]
- The web UI includes a browser-based Git client for staging, committing, pushing, and managing branches and diffs, plus a keyboard-driven morning review queue for triaging overnight TODOs. [@claim:clm_737eb151c36bd60655ceddc02cef5f66989ced4456e01374d1d7631649ba02c9]
- Prerequisites are Node.js 22+ (LTS recommended), Git, and at least one AI CLI (Claude, Antigravity, or Codex); the desktop app bundles Node.js and native modules like better-sqlite3 and node-pty. [@claim:clm_75de7558ef2e45b03050bfd12d5ef911d089c7036062753b94d64ea9b2227df3]
- A strict sandbox mode confines file access to the worktree; the AI CLI (Claude/Antigravity/Codex) can be chosen per project, TODO, or agent. [@claim:clm_7b6666f3927420da85480a76a717dbf049424828059df8c41fa4fe859032c16a]
- Each TODO runs in its own isolated git worktree, with Claude, Antigravity, and Codex executing in parallel, plus dependency chains and merge control. [@claim:clm_9af4c9128b2828cb9a3f721e0d573ec6f6ac0b2e1882b6b653705f01e004311e]
- Repository development practice: running from source involves cloning, npm install in root and src/client, copying .env.example to .env, and `npm run dev` with the dev server at localhost:5173; tests run via `npm test` or scripts/test.bat. [@claim:clm_b7ad30713d375143d8ff701028221e480c29f59bfe4ac4a652cf2ee989262546]
- The product is organized around a five-stage pipeline — Docs, Plan, Terminal, Autonomous Tasks, Version Control — where each stage consumes the previous stage's context, with lessons feeding back into docs. [@claim:clm_d0b6452cc89868c6017a62f6866c4a0f8fdadbeefeb3febb9adb5a3d04cd11c4]
- Repository development practice: contributors are invited to file issues, open PRs (starting with 'good first issue' labels), and share workflows in Discussions; docs include CICD.md for GitHub Actions CI/CD and TESTING.md. [@claim:clm_d8367185a792a2bd37202cf94ef2ead0f25a45e5b89574d8545b1a4715057248]
- CLITrigger is described as an IDE for AI CLI agents, unifying docs, plans, terminals, autonomous agents, and git into one workspace instead of five scattered tools. [@claim:clm_f5af571164d34eee0f755d1b16eff8109c4efaee79f58fcd241013caa77672b4]
- The documented stack: Node.js/Express/TypeScript/SQLite/WebSocket backend, React 18/Vite/Tailwind/Recharts frontend, simple-git for worktrees, node-cron for scheduling, node-pty and xterm.js for terminals, and optional Cloudflare Tunnel. [@claim:clm_f607375b6d0d652980ffddd426c393d1624608c2e82976e34f0ac2c9bc6e2eba]
<!-- rcw:end owner=source:src_fe192eb55d58547c9eb99e490d9f9e26 block=evidence -->

## Researcher notes

