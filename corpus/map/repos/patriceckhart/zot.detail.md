# patriceckhart/zot -- full detail

[Back to orientation](zot.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/patriceckhart/zot/f60e492e551892e737d24a7eaf7730f1f60b75af/17a5430f57315354.json](../../../wiki/dossiers/patriceckhart/zot/f60e492e551892e737d24a7eaf7730f1f60b75af/17a5430f57315354.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] zot is a coding agent harness written in Go and distributed as a single static binary. -- evidence: [README.md#L18-L18](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L18-L18), [README.md#L20-L29](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L20-L29) (`clm_0669a2918efe2b3bbe229bf1e2cd227505afc17fb703682f74b8f3d77c2309b7`)

## design-choices (3 claim(s))

- [observation/documented] Extensions run in any language via subprocess plus JSON-RPC, none installed by default, opted into with `zot ext install` or `zot --ext`; themes are user and extension JSON files. -- evidence: [README.md#L20-L29](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L20-L29) (`clm_1c6d041065aed4ab3163efa38033512a8335ed9a76949b0a8d7aa2da0ce4197c`)
- [observation/documented] API keys can be fetched from a password manager via an api_key_command executed directly without a shell; output is cached in memory only, never written to disk, and capped at 64 KiB. -- evidence: [README.md#L106-L106](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L106-L106), [README.md#L108-L108](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L108-L108), [README.md#L92-L92](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L92-L92) (`clm_bd69a74a59cca981a56b9959eacc51ed171d208c89927800ba67ad147c8d00e7`)
- [observation/documented] zotfile agents package instructions, skills, requirements, and enforced tool permissions; they can run from local directories, .zot archives, or temporary public GitHub downloads, with no built-in registry or allowlist. -- evidence: [README.md#L281-L281](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L281-L281), [README.md#L20-L29](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L20-L29), [README.md#L290-L290](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L290-L290) (`clm_230e19c5a41cde4c7efd4c9c760ae32fe221591076cc572b1fb5fce3e07f2a6f`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (2 claim(s))

- [observation/documented] Standing instructions come from AGENTS.md files (global plus root-to-cwd chain, deeper files overriding), while reusable instructions use SKILL.md files; SYSTEM.md replaces the built-in identity and --system-prompt wins per invocation. -- evidence: [README.md#L167-L167](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L167-L167), [README.md#L171-L172](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L171-L172), [README.md#L151-L151](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L151-L151), [README.md#L184-L190](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L184-L190), [README.md#L20-L29](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L20-L29) (`clm_68ab3e9a8301c1533457d28b25e0d37e9908ecc395cb8836eac1cac1223933e3`)
- [observation/documented] zot does not read CLAUDE.md; the only Claude-compatible input is skills under .claude/skills/, and migrating users are told to move content into AGENTS.md. -- evidence: [README.md#L192-L192](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L192-L192) (`clm_b15961f97440d26e692f3deeb449170f976bf8b2c53cb620fd198a7235870c43`)

## interfaces (2 claim(s))

- [observation/documented] The CLI supports interactive TUI, print, stream, piped-input, and JSON modes, plus an `zot rpc` long-lived subprocess speaking newline-delimited JSON for embedding in other applications. -- evidence: [README.md#L296-L297](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L296-L297), [README.md#L200-L212](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L200-L212), [README.md#L272-L277](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L272-L277) (`clm_395c04de3d710c3c3f26bd5abf6ca7b0f680bc6b7de2fcf500829e5e9cfb3f42`)
- [observation/documented] A Go SDK is offered via the packages/agent/sdk import, where a Runtime per project exposes Prompt(ctx, text, images) returning a channel of events; both embedding paths share one event schema. -- evidence: [README.md#L296-L297](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L296-L297), [README.md#L299-L299](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L299-L299) (`clm_1c622fc1c8c16a6b3ba6f70d5cf850bad1d174ae8a73dd49da86f6c41a210aee`)

## memory-state (3 claim(s))

- [observation/documented] All data lives under $ZOT_HOME, including config.json, auth.json (mode 0600), per-cwd JSONL session transcripts, a 6h-TTL models cache, skills, themes, extensions, and logs. -- evidence: [README.md#L84-L88](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L84-L88), [README.md#L137-L149](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L137-L149) (`clm_b6f64e332a9b6a820e12924f7e841411ea4ecd4746900d41f6eb6c5d1006a303`)
- [observation/documented] Sessions are JSONL transcripts resumable via --continue, --resume, --session, or /sessions; empty sessions are deleted on close, and `zot sessions prune` can remove sessions for vanished directories or by age. -- evidence: [README.md#L465-L465](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L465-L465), [README.md#L467-L467](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L467-L467), [README.md#L463-L463](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L463-L463) (`clm_0af4a68a9a2a063a502e99296e8c0e14797c3ba1ee5e7258f7515438a40f8f8d`)
- [observation/documented] OAuth tokens are refreshed automatically at credential lookup with a 60-second safety margin, and the telegram bridge refreshes once per turn; failed refreshes surface in the TUI or bot reply. -- evidence: [README.md#L131-L133](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L131-L133), [README.md#L129-L129](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L129-L129) (`clm_fb192f8a528f6cafb37cc43d0340eeb099f7378d952127097ae29ea7119dfdd4`)

## orchestration (2 claim(s))

- [observation/documented] /swarm spawns background subagents as separate zot subprocesses sharing the host's working directory, with a dashboard, per-agent session files and unix-socket inboxes under $ZOT_HOME/swarm/agents/<id>/, and persistence across restarts as detached agents. -- evidence: [README.md#L408-L408](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L408-L408), [README.md#L372-L372](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L372-L372), [README.md#L410-L410](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L410-L410), [README.md#L374-L374](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L374-L374) (`clm_c005faee2e77868104178371290efc16184f5ad643f01b26cc346a0d90d8bac0`)
- [observation/documented] An opt-in auto-swarm setting gives the main agent a swarm_spawn tool and prompt nudge to fork sub-agents for parallel work, injecting an update message when the batch finishes; it is off by default. -- evidence: [README.md#L420-L425](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L420-L425), [README.md#L414-L414](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L414-L414) (`clm_c25e436df16c4a07762110583c4f849376dd9ab88744315e689e3b67351d3b31`)

## tools-permissions (3 claim(s))

- [observation/documented] Built-in tools include read (with image inlining), write, edit, bash, and glob; a PowerShell tool exists on Windows, off by default and toggleable in /settings or via --tools. -- evidence: [README.md#L254-L254](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L254-L254), [README.md#L258-L260](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L258-L260), [README.md#L20-L29](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L20-L29), [README.md#L245-L248](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L245-L248) (`clm_38bd97424f2d210a3fbcecf31f4f28435fffff36f7a1e20c5764296a17806164`)
- [observation/documented] The /jail sandbox restricts filesystem tools to the session cwd (including symlink resolution) and blocks obvious bash escape patterns; it is documented as an accident-prevention guardrail, not a security boundary. -- evidence: [README.md#L459-L459](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L459-L459), [README.md#L457-L457](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L457-L457), [README.md#L250-L250](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L250-L250) (`clm_cfcbc40afae974ee5755b71094894318ff43cc0a18c6f7db5169788be59e223e`)
- [observation/documented] PowerShell execution is blocked while /jail is active, and packaged agents require permissions.bash.mode "ask" for launch-time consent; allowlist and unknown modes deny PowerShell. -- evidence: [README.md#L268-L268](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L268-L268) (`clm_a33800bde0e9b57c7595b23457de3c1376eaac5cd922bea213a0ac072c47f807`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project targets Go 1.25+ and advertises built-in providers for Anthropic, OpenAI/Codex, Kimi, DeepSeek, Gemini/Vertex, GitHub Copilot, Bedrock, Azure, OpenRouter, Groq, and many others including Ollama local models. -- evidence: [README.md#L20-L29](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L20-L29), [README.md#L1-L14](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L1-L14) (`clm_d573bbdabe2fc0dc667bb475bba7b69e4e41bbdd9fcf92961feb6118554c3127`)

## limitations (3 claim(s))

- [observation/documented] DeepSeek and Google Gemini have no subscription login path, only the API-key flow; reusing published OAuth client IDs from third-party tools may violate provider terms and be revoked. -- evidence: [README.md#L116-L123](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L116-L123), [README.md#L125-L125](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L125-L125) (`clm_1697f6426196f78e5bdc083cba6dd69bedae86504b33ecb9fbb64c827fd2ffc2`)
- [observation/documented] Session export (.zotsession) covers only the main chat thread; swarm subagent transcripts and unix-socket inboxes are machine-local and cannot be revived from an exported file. -- evidence: [README.md#L346-L349](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L346-L349), [README.md#L412-L412](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L412-L412) (`clm_c8a7e6fac2f3d9f4d2c44f3d283449a20d7bc91ba021611839a19a91945b208b`)
- [observation/documented] Swarm subagents edit the same files as the host with no per-agent worktree or branch; parallel isolated edits must be arranged externally with git worktree. -- evidence: [README.md#L374-L374](https://github.com/patriceckhart/zot/blob/f60e492e551892e737d24a7eaf7730f1f60b75af/README.md#L374-L374) (`clm_d664ecbe1b56ea1e7c5a686c41fe7f976ff1a7637a5365ca2b5755e8a7879534`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

