---
access: public
aliases: []
claim_ids:
- clm_0669a2918efe2b3bbe229bf1e2cd227505afc17fb703682f74b8f3d77c2309b7
- clm_0af4a68a9a2a063a502e99296e8c0e14797c3ba1ee5e7258f7515438a40f8f8d
- clm_1697f6426196f78e5bdc083cba6dd69bedae86504b33ecb9fbb64c827fd2ffc2
- clm_1c622fc1c8c16a6b3ba6f70d5cf850bad1d174ae8a73dd49da86f6c41a210aee
- clm_1c6d041065aed4ab3163efa38033512a8335ed9a76949b0a8d7aa2da0ce4197c
- clm_230e19c5a41cde4c7efd4c9c760ae32fe221591076cc572b1fb5fce3e07f2a6f
- clm_38bd97424f2d210a3fbcecf31f4f28435fffff36f7a1e20c5764296a17806164
- clm_395c04de3d710c3c3f26bd5abf6ca7b0f680bc6b7de2fcf500829e5e9cfb3f42
- clm_68ab3e9a8301c1533457d28b25e0d37e9908ecc395cb8836eac1cac1223933e3
- clm_a33800bde0e9b57c7595b23457de3c1376eaac5cd922bea213a0ac072c47f807
- clm_b15961f97440d26e692f3deeb449170f976bf8b2c53cb620fd198a7235870c43
- clm_b6f64e332a9b6a820e12924f7e841411ea4ecd4746900d41f6eb6c5d1006a303
- clm_bd69a74a59cca981a56b9959eacc51ed171d208c89927800ba67ad147c8d00e7
- clm_c005faee2e77868104178371290efc16184f5ad643f01b26cc346a0d90d8bac0
- clm_c25e436df16c4a07762110583c4f849376dd9ab88744315e689e3b67351d3b31
- clm_c8a7e6fac2f3d9f4d2c44f3d283449a20d7bc91ba021611839a19a91945b208b
- clm_cfcbc40afae974ee5755b71094894318ff43cc0a18c6f7db5169788be59e223e
- clm_d573bbdabe2fc0dc667bb475bba7b69e4e41bbdd9fcf92961feb6118554c3127
- clm_d664ecbe1b56ea1e7c5a686c41fe7f976ff1a7637a5365ca2b5755e8a7879534
- clm_fb192f8a528f6cafb37cc43d0340eeb099f7378d952127097ae29ea7119dfdd4
maturity: draft
page_id: pg_0ac2bf33ef2a502a86171ad89071ad7a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a0a81e8bfa695153bbd3b68547ec1533
title: patriceckhart/zot/README.md @ f60e492e5518
updated_at: '2026-09-14T02:30:01Z'
---

# patriceckhart/zot/README.md @ f60e492e5518

<!-- rcw:begin owner=source:src_a0a81e8bfa695153bbd3b68547ec1533 block=evidence -->
- zot is a coding agent harness written in Go and distributed as a single static binary. [@claim:clm_0669a2918efe2b3bbe229bf1e2cd227505afc17fb703682f74b8f3d77c2309b7]
- Sessions are JSONL transcripts resumable via --continue, --resume, --session, or /sessions; empty sessions are deleted on close, and `zot sessions prune` can remove sessions for vanished directories or by age. [@claim:clm_0af4a68a9a2a063a502e99296e8c0e14797c3ba1ee5e7258f7515438a40f8f8d]
- DeepSeek and Google Gemini have no subscription login path, only the API-key flow; reusing published OAuth client IDs from third-party tools may violate provider terms and be revoked. [@claim:clm_1697f6426196f78e5bdc083cba6dd69bedae86504b33ecb9fbb64c827fd2ffc2]
- A Go SDK is offered via the packages/agent/sdk import, where a Runtime per project exposes Prompt(ctx, text, images) returning a channel of events; both embedding paths share one event schema. [@claim:clm_1c622fc1c8c16a6b3ba6f70d5cf850bad1d174ae8a73dd49da86f6c41a210aee]
- Extensions run in any language via subprocess plus JSON-RPC, none installed by default, opted into with `zot ext install` or `zot --ext`; themes are user and extension JSON files. [@claim:clm_1c6d041065aed4ab3163efa38033512a8335ed9a76949b0a8d7aa2da0ce4197c]
- zotfile agents package instructions, skills, requirements, and enforced tool permissions; they can run from local directories, .zot archives, or temporary public GitHub downloads, with no built-in registry or allowlist. [@claim:clm_230e19c5a41cde4c7efd4c9c760ae32fe221591076cc572b1fb5fce3e07f2a6f]
- Built-in tools include read (with image inlining), write, edit, bash, and glob; a PowerShell tool exists on Windows, off by default and toggleable in /settings or via --tools. [@claim:clm_38bd97424f2d210a3fbcecf31f4f28435fffff36f7a1e20c5764296a17806164]
- The CLI supports interactive TUI, print, stream, piped-input, and JSON modes, plus an `zot rpc` long-lived subprocess speaking newline-delimited JSON for embedding in other applications. [@claim:clm_395c04de3d710c3c3f26bd5abf6ca7b0f680bc6b7de2fcf500829e5e9cfb3f42]
- Standing instructions come from AGENTS.md files (global plus root-to-cwd chain, deeper files overriding), while reusable instructions use SKILL.md files; SYSTEM.md replaces the built-in identity and --system-prompt wins per invocation. [@claim:clm_68ab3e9a8301c1533457d28b25e0d37e9908ecc395cb8836eac1cac1223933e3]
- PowerShell execution is blocked while /jail is active, and packaged agents require permissions.bash.mode "ask" for launch-time consent; allowlist and unknown modes deny PowerShell. [@claim:clm_a33800bde0e9b57c7595b23457de3c1376eaac5cd922bea213a0ac072c47f807]
- zot does not read CLAUDE.md; the only Claude-compatible input is skills under .claude/skills/, and migrating users are told to move content into AGENTS.md. [@claim:clm_b15961f97440d26e692f3deeb449170f976bf8b2c53cb620fd198a7235870c43]
- All data lives under $ZOT_HOME, including config.json, auth.json (mode 0600), per-cwd JSONL session transcripts, a 6h-TTL models cache, skills, themes, extensions, and logs. [@claim:clm_b6f64e332a9b6a820e12924f7e841411ea4ecd4746900d41f6eb6c5d1006a303]
- API keys can be fetched from a password manager via an api_key_command executed directly without a shell; output is cached in memory only, never written to disk, and capped at 64 KiB. [@claim:clm_bd69a74a59cca981a56b9959eacc51ed171d208c89927800ba67ad147c8d00e7]
- /swarm spawns background subagents as separate zot subprocesses sharing the host's working directory, with a dashboard, per-agent session files and unix-socket inboxes under $ZOT_HOME/swarm/agents/<id>/, and persistence across restarts as detached agents. [@claim:clm_c005faee2e77868104178371290efc16184f5ad643f01b26cc346a0d90d8bac0]
- An opt-in auto-swarm setting gives the main agent a swarm_spawn tool and prompt nudge to fork sub-agents for parallel work, injecting an update message when the batch finishes; it is off by default. [@claim:clm_c25e436df16c4a07762110583c4f849376dd9ab88744315e689e3b67351d3b31]
- Session export (.zotsession) covers only the main chat thread; swarm subagent transcripts and unix-socket inboxes are machine-local and cannot be revived from an exported file. [@claim:clm_c8a7e6fac2f3d9f4d2c44f3d283449a20d7bc91ba021611839a19a91945b208b]
- The /jail sandbox restricts filesystem tools to the session cwd (including symlink resolution) and blocks obvious bash escape patterns; it is documented as an accident-prevention guardrail, not a security boundary. [@claim:clm_cfcbc40afae974ee5755b71094894318ff43cc0a18c6f7db5169788be59e223e]
- The project targets Go 1.25+ and advertises built-in providers for Anthropic, OpenAI/Codex, Kimi, DeepSeek, Gemini/Vertex, GitHub Copilot, Bedrock, Azure, OpenRouter, Groq, and many others including Ollama local models. [@claim:clm_d573bbdabe2fc0dc667bb475bba7b69e4e41bbdd9fcf92961feb6118554c3127]
- Swarm subagents edit the same files as the host with no per-agent worktree or branch; parallel isolated edits must be arranged externally with git worktree. [@claim:clm_d664ecbe1b56ea1e7c5a686c41fe7f976ff1a7637a5365ca2b5755e8a7879534]
- OAuth tokens are refreshed automatically at credential lookup with a 60-second safety margin, and the telegram bridge refreshes once per turn; failed refreshes surface in the TUI or bot reply. [@claim:clm_fb192f8a528f6cafb37cc43d0340eeb099f7378d952127097ae29ea7119dfdd4]
<!-- rcw:end owner=source:src_a0a81e8bfa695153bbd3b68547ec1533 block=evidence -->

## Researcher notes

