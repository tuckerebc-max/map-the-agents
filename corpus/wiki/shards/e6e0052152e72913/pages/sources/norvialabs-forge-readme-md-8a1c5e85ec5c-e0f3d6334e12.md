---
access: public
aliases: []
claim_ids:
- clm_00f42cfcc0b379883aaaeecde4e70528988009e3f419d37b2d9b0dcf0bd2396c
- clm_258d1f7c307c6485d625c5e905f073f8ded7623b61fa492ac3a4ed1acefff646
- clm_2bd9adf3c6409ae8bbc9a0427adb94f8964331ed8a290cb59f5fa2717ffc2f3e
- clm_329d4d587ab06c1de9527723944f91bdebdb923df166e7c19d052cd93396dcb3
- clm_36ad4581810a9b3ba367fe9537726bf8263a1b1a873ee7a1830e6ac5b7ed8d6c
- clm_3a49fbf0a2901f77043dfa1125fb220fa55b3e5dde68153e2d4e45de5c5b33cd
- clm_44790f6e238d6f684721058537202ab184ad2ca2faae0c54a5402860211a23df
- clm_4c0151c114a9c6cff8e06e509deccdc9d39182f24734c4ffb908c25ee3ef9533
- clm_575f64b10a34fc4f795dc20341257980e7b8276348252b4a6c946d9ca189e831
- clm_59070727be783aac589a7d99229d4f6816f4a4d4b8ddaeaf9f8019347bd29880
- clm_67640a0e890da21b03556ddc5384e06873f35d807db5ddd49ce0d9cd099f667f
- clm_8dabe99f628269fcc9df8fd081fbbc9fa831e954d274b63a42a533887f568276
- clm_8f9e074f5905c940945bf1c2385b5fd1eb77dab5fd165bb7fb7c49bf543e6a43
- clm_9e3af8244a399c9f3eb7c4ea4dbfed9c3a92356209e70f61777d686269145c48
- clm_a2ade14295af315d95c6976d9acaad90f58486b83c2d96147f32573119c9ee4c
- clm_d86aed90dcb22d75feb37762f854c5875bdb35d1aa2c0371bab5e645679b7263
- clm_e8b1ab54a7767968ef7d016dd5901c93c862096a3aa551c5868fc04edd750dc2
- clm_fb4701a399e7d8cd1af279124588feefdbf202127eb9d51b4e6f8a65f6ea989e
maturity: draft
page_id: pg_c5fb480a1ed15dc88e3ce0f3d6334e12
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_baf994dcafae5fa59ab3a0c74139341e
title: NorviaLabs/forge/README.md @ 8a1c5e85ec5c
updated_at: '2026-09-14T02:23:41Z'
---

# NorviaLabs/forge/README.md @ 8a1c5e85ec5c

<!-- rcw:begin owner=source:src_baf994dcafae5fa59ab3a0c74139341e block=evidence -->
- Agent orchestration is enabled by default: the model can spawn child agents via spawn_agent, send_message, followup_task, wait_agent, list_agents, and interrupt_agent; children run in isolated worktrees, inherit parent model/governance/policy, and can be tool-narrowed with tool_allowlist. [@claim:clm_00f42cfcc0b379883aaaeecde4e70528988009e3f419d37b2d9b0dcf0bd2396c]
- Configuration is layered from defaults, a user config file, a forge.toml in the working directory, and environment variables, with environment variables overriding file configuration; MCP servers are configured in trusted user config or explicitly managed configuration. [@claim:clm_258d1f7c307c6485d625c5e905f073f8ded7623b61fa492ac3a4ed1acefff646]
- Forge ships native provider routes for OpenAI, Anthropic, xAI Grok (OAuth), OpenAI Codex subscriptions, OpenCode Go, OpenCode Zen, and local Ollama, configured via API-key environment variables or /connect. [@claim:clm_2bd9adf3c6409ae8bbc9a0427adb94f8964331ed8a290cb59f5fa2717ffc2f3e]
- Repository development practice: contributors are told to run cargo fmt --check, cargo clippy with -D warnings, and cargo test --workspace before submitting a change, with further guidance in CONTRIBUTING.md. [@claim:clm_329d4d587ab06c1de9527723944f91bdebdb923df166e7c19d052cd93396dcb3]
- There is no permission-mode setting: shell commands and file writes run unprompted with the sandbox as the boundary, MCP tools still prompt, and a deny pattern re-prompts even for shell; ACL denies are hard blocks. [@claim:clm_36ad4581810a9b3ba367fe9537726bf8263a1b1a873ee7a1830e6ac5b7ed8d6c]
- The TUI exposes in-app slash commands such as /connect, /model, /resume, /continue, /fork, /compact, /terminal, /theme, /effort, /thinking, /status, and /quit. [@claim:clm_3a49fbf0a2901f77043dfa1125fb220fa55b3e5dde68153e2d4e45de5c5b33cd]
- Forge is a Rust workspace whose main crates include forge-cli (entry point), forge-tui (terminal interface), forge-core (agent loop and session lifecycle), forge-model, forge-connect, forge-tools, and forge-durable (SQLite journals). [@claim:clm_44790f6e238d6f684721058537202ab184ad2ca2faae0c54a5402860211a23df]
- The README documents a residual Linux sandbox gap: read-only mounts do not stop Unix socket connections, so sockets under /var or /opt remain reachable despite masking of /run, /tmp, and home trees; tracked in issue #392. [@claim:clm_4c0151c114a9c6cff8e06e509deccdc9d39182f24734c4ffb908c25ee3ef9533]
- Permission rules come from a personal permissions.toml and a workspace .forge/permissions.toml; the repo-committed file's allow entries are ignored while its deny entries are always honored, so a checked-out repo cannot widen its own blast radius. [@claim:clm_575f64b10a34fc4f795dc20341257980e7b8276348252b4a6c946d9ca189e831]
- On Linux the installer installs the sandbox dependencies bubblewrap and socat if missing (supporting apt, dnf, yum, pacman, zypper, apk); macOS needs nothing extra, and building from source requires Git and Rust 1.97.1 or newer. [@claim:clm_59070727be783aac589a7d99229d4f6816f4a4d4b8ddaeaf9f8019347bd29880]
- A frontend-independent `forge bench` entry point accepts a piped prompt with flags like --workspace, --journal, --model, --route-id, --effort, and --approve-all, emitting one JSON response on stdout and logs on stderr. [@claim:clm_67640a0e890da21b03556ddc5384e06873f35d807db5ddd49ce0d9cd099f667f]
- There is no native Windows build; Forge runs under WSL2 using the Linux sandbox, and the PowerShell installer detects WSL2 and points to the Linux installer. [@claim:clm_8dabe99f628269fcc9df8fd081fbbc9fa831e954d274b63a42a533887f568276]
- Forge is an open-source terminal coding environment for working with AI agents, combining agent conversations, file explorer, Vim-style editing, shell, diffs, approvals, and multiple durable sessions in one keyboard-driven TUI. [@claim:clm_8f9e074f5905c940945bf1c2385b5fd1eb77dab5fd165bb7fb7c49bf543e6a43]
- Documented CLI forms include bare `forge`, `forge --continue`, `forge --resume [<session-id>]`, and `forge --fork <session-id>`; the default workspace is the current directory, overridable via FORGE_WORKSPACE. [@claim:clm_9e3af8244a399c9f3eb7c4ea4dbfed9c3a92356209e70f61777d686269145c48]
- Sessions preserve transcripts, task state, queued follow-ups, and unfinished work in a local SQLite journal so they survive process restarts; each managed session has its own durable state and isolated linked Git worktree. [@claim:clm_a2ade14295af315d95c6976d9acaad90f58486b83c2d96147f32573119c9ee4c]
- If the OS cannot confine (e.g. bubblewrap missing or unsupported platform), Forge refuses to start, printing the reason on stderr; there is no setting that turns oversight off without an enforcement floor. [@claim:clm_d86aed90dcb22d75feb37762f854c5875bdb35d1aa2c0371bab5e645679b7263]
- The project describes itself as alpha software and advises reviewing every approval prompt and using it first in a disposable or backed-up repository. [@claim:clm_e8b1ab54a7767968ef7d016dd5901c93c862096a3aa551c5868fc04edd750dc2]
- Agent shell commands run under an OS sandbox (Seatbelt on macOS, bubblewrap on Linux, WSL2's Linux sandbox on Windows) confined to the workspace, with network egress denied by default and opened only through explicit host rules via a filtering proxy. [@claim:clm_fb4701a399e7d8cd1af279124588feefdbf202127eb9d51b4e6f8a65f6ea989e]
<!-- rcw:end owner=source:src_baf994dcafae5fa59ab3a0c74139341e block=evidence -->

## Researcher notes

