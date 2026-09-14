---
access: public
aliases: []
claim_ids:
- clm_2759cd6bf99ff1b03149118eac877b099c4267b0c488d84c849176012a6a2119
- clm_28d1085fd35bdbec1c2f178a8c51be43c06fbe4684a00b55bb77862616f6c819
- clm_4bdba20c71d5eeb96a18f1155a673484fa1bb3cc160b4e15343e82e962dbac57
- clm_4e6eb13a9a87f123e0a4c681dbe1ac38880ca7e9c4e8247d1137033f471148dc
- clm_518fdf5eb52cd03610d211627acb375cc5b45a1dd96a2914a31ab85b85c18971
- clm_89daf8847ae49389cd321c29e7367ae2c10a6c5b56d5c3f3cebb2adac0f36ada
- clm_92151ef64b8e5f361a3ceb4794595924f35ad96305ae18cb9fd66cf2599895f8
- clm_cbd69af5384e250e8f707a97989e029c7e9d161e5cb89dfdc8a5930107bff01c
- clm_dfd3976276f697e81335961fc16d0dbb4b36b832acefc0466d12a9f39071d4ee
- clm_f5177d924f1ea27acf10b95dba4332de1deb54cc8134e5c421fad650e0184c60
- clm_fc34099f5cec000a7681859f64302961db1588de9cc8d95b410f9487ae0f38b7
maturity: draft
page_id: pg_3bd77b269c7b519cb0347ddc133e859a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_10f1fbd5103d5d62abe7cef3abc126a2
title: penso/arbor/README.md @ d8d82b7eec6c
updated_at: '2026-09-14T02:30:09Z'
---

# penso/arbor/README.md @ d8d82b7eec6c

<!-- rcw:begin owner=source:src_10f1fbd5103d5d62abe7cef3abc126a2 block=evidence -->
- Daemon access control: loopback requests need no token, while non-loopback requests require an Authorization bearer token configured via ARBOR_DAEMON_AUTH_TOKEN. [@claim:clm_2759cd6bf99ff1b03149118eac877b099c4267b0c488d84c849176012a6a2119]
- Arbor embeds a PTY terminal with truecolor and xterm-256color support, multiple tabs per worktree, persistent daemon-based sessions, and managed processes from Procfile and arbor.toml. [@claim:clm_28d1085fd35bdbec1c2f178a8c51be43c06fbe4684a00b55bb77862616f6c819]
- Agent chat supports ACP agents (Claude, Codex, Pi, Gemini via acpx) and OpenAI-compatible /v1/chat/completions providers, with SSE streaming and startup model discovery via /v1/models. [@claim:clm_4bdba20c71d5eeb96a18f1155a673484fa1bb3cc160b4e15343e82e962dbac57]
- Repo-local behavior is configured via <repo>/arbor.toml, which supplies presets, managed processes, worktree scripts, scheduled tasks, branch naming rules, agent defaults, and notification routing. [@claim:clm_4e6eb13a9a87f123e0a4c681dbe1ac38880ca7e9c4e8247d1137033f471148dc]
- The workspace includes crates such as arbor-core, arbor-gui, arbor-httpd, arbor-mcp, arbor-cli, arbor-mosh, arbor-ssh, arbor-symphony, arbor-terminal-emulator, and arbor-web-ui. [@claim:clm_518fdf5eb52cd03610d211627acb375cc5b45a1dd96a2914a31ab85b85c18971]
- The app manages worktrees across repositories, including creation from GitHub/GitLab issues, branch naming rules, delete confirmation with unpushed-commit detection, and issue linking to branches and PRs. [@claim:clm_89daf8847ae49389cd321c29e7367ae2c10a6c5b56d5c3f3cebb2adac0f36ada]
- arbor-mcp is a stdio MCP server enabled by the crate's default stdio-server feature, talking to arbor-httpd, which must be reachable first. [@claim:clm_92151ef64b8e5f361a3ceb4794595924f35ad96305ae18cb9fd66cf2599895f8]
- Arbor is a fully native agentic-coding app built with Rust and GPUI, with a shared daemon powering the desktop app, web UI, CLI, and MCP server. [@claim:clm_cbd69af5384e250e8f707a97989e029c7e9d161e5cb89dfdc8a5930107bff01c]
- arbor-cli exposes daemon-backed health, repo, worktree, terminal, process, and task commands, with JSON output options like worktrees list --json. [@claim:clm_dfd3976276f697e81335961fc16d0dbb4b36b832acefc0466d12a9f39071d4ee]
- An experimental embedded Ghostty terminal engine is opt-in behind the ghostty-vt-experimental feature flag and disabled by default; when built in, it is used by default and selectable via config. [@claim:clm_f5177d924f1ea27acf10b95dba4332de1deb54cc8134e5c421fad650e0184c60]
- The project targets Rust nightly-2025-11-30 and uses the just task runner; UI icons require a Caskaydia/Cascadia Nerd Font variant. [@claim:clm_fc34099f5cec000a7681859f64302961db1588de9cc8d95b410f9487ae0f38b7]
<!-- rcw:end owner=source:src_10f1fbd5103d5d62abe7cef3abc126a2 block=evidence -->

## Researcher notes

