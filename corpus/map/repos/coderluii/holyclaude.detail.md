# coderluii/holyclaude -- full detail

[Back to orientation](holyclaude.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/coderluii/holyclaude/651c48fc01a963acd605aa565bb9da8f9db9b340/ec0da588070ffb78.json](../../../wiki/dossiers/coderluii/holyclaude/651c48fc01a963acd605aa565bb9da8f9db9b340/ec0da588070ffb78.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (4 claim(s))

- [observation/documented] The container runs the official Anthropic Claude Code CLI (not a wrapper or proxy), served through a CloudCLI web UI on port 3001, with s6-overlay as PID 1 supervising Xvfb on :99 and optional sshd. -- evidence: [README.md#L58-L58](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L58-L58), [README.md#L765-L778](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L765-L778), [README.md#L195-L195](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L195-L195) (`clm_c0254316595719bf4d7309a6333c3b2ad47fd4d18192cf89ce16862df5350254`)
- [observation/documented] The image bundles Chromium with Xvfb and Playwright for headless browser screenshots and testing, plus database clients (psql, redis-cli, sqlite3, MariaDB-based mysql) and GitHub CLI. -- evidence: [README.md#L765-L778](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L765-L778), [README.md#L592-L606](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L592-L606) (`clm_adb2dd625e4f4f78c5bf22b20786152810090a2ae97a76e0d5a48d73361732f5`)
- [observation/documented] The full image ships eight AI CLIs — Claude Code, Gemini, Codex, Cursor, TaskMaster, Junie, OpenCode, and Pi — while the slim image ships the five core ones (Claude Code, Gemini, Codex, Cursor, TaskMaster), with slim installing missing tools on demand. -- evidence: [README.md#L613-L619](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L613-L619), [README.md#L632-L636](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L632-L636), [README.md#L683-L683](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L683-L683), [README.md#L693-L693](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L693-L693), [README.md#L621-L621](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L621-L621) (`clm_ba4eb6720683133398e9d74a0b7448d09ffb76f5cf15343d24c31930336d01d4`)
- [observation/documented] Desloppify ships as a passive CLI in both images; it performs no scans or workspace edits unless invoked, and optional global skill setup at container start is controlled by HOLYCLAUDE_DESLOPPIFY_SETUP with values like off, claude, codex, gemini, all, or opencode (full image only). -- evidence: [README.md#L731-L739](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L731-L739), [README.md#L718-L718](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L718-L718), [README.md#L729-L729](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L729-L729) (`clm_4350ee935bbe2b417106246efadca148d48c44ccbad14fa9ae7377c5a1dd2b92`)

## design-choices (3 claim(s))

- [observation/documented] The compose templates set shm_size 2g because Chromium heavily uses /dev/shm and Docker's 64MB default causes tab crashes, and grant SYS_ADMIN, SYS_PTRACE, and seccomp=unconfined as the retained browser profile, with hardening described as a separate change. -- evidence: [README.md#L272-L301](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L272-L301), [README.md#L313-L313](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L313-L313), [README.md#L315-L315](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L315-L315) (`clm_5e6130c76f958b181253973a2144dcad524b001dad5c6d3229d075ef86daa7fb`)
- [observation/documented] The web UI port is bound to 127.0.0.1 by default, and users needing remote access are directed to Tailscale or Cloudflare Tunnel rather than port forwarding. -- evidence: [README.md#L272-L301](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L272-L301), [README.md#L141-L141](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L141-L141), [README.md#L313-L313](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L313-L313) (`clm_e3f3cc373802532e8d253e4bc5de229305fe7150ec357f3d2b6b34787a9dcb4d`)
- [observation/documented] Two image variants are published on Docker Hub: latest (full, everything pre-installed) and slim (core tools only, with Claude installing extras on demand), plus pinned X.Y.Z and X.Y.Z-slim tags for production stability. -- evidence: [README.md#L251-L253](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L251-L253), [README.md#L236-L241](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L236-L241) (`clm_f84a68605642efca20febf07e64953adaa33b80fd95f29ace6b5e951a4219855`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: release-sensitive facts are published in contracts/product-facts.json, and the release workflow checks that contract against the Dockerfile and Compose files before building images. -- evidence: [README.md#L46-L46](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L46-L46) (`clm_efbd9e32c74522b076cb6d5e75c71d85b485f5c9fc709f8e340aa7664e2cd9e7`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Authentication is done through the CloudCLI web UI: Claude Max/Pro users sign in via OAuth and API-key users paste their key; the container relays no credentials, with tools reading them from container files, bind mounts, or environment variables. -- evidence: [README.md#L60-L63](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L60-L63), [README.md#L65-L65](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L65-L65), [README.md#L199-L202](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L199-L202), [README.md#L224-L224](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L224-L224) (`clm_59ddcfbeb481916d3b6946b5013ee2b96a275f36e1180002e410367686d3a887`)
- [observation/documented] The quick-start workflow is: create a docker-compose.yaml from a provided template, run docker compose up -d, then open http://localhost:3001 and create a CloudCLI account; no .env file is required. -- evidence: [README.md#L121-L123](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L121-L123), [README.md#L137-L137](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L137-L137), [README.md#L127-L129](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L127-L129), [README.md#L133-L135](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L133-L135), [README.md#L139-L139](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L139-L139) (`clm_d15804f92f7e1ee1bba4295ee9384bad14f7e4e4b819f430e2e1cc1a7d398bc5`)
- [observation/documented] Environment variables are documented as all optional, covering timezone (TZ), UID/GID remapping (PUID/PGID), Node heap size, SMB polling flags, Apprise notification URLs (Discord, Telegram, Slack, email, etc.), and AI provider API keys. -- evidence: [README.md#L493-L493](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L493-L493), [README.md#L484-L491](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L484-L491), [README.md#L505-L539](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L505-L539) (`clm_2b208af703c1309fb14678ddb1b7ef43ee00b56bbb84f4603add6d94b813f4e8`)
- [observation/documented] Ollama is supported as an alternative to an Anthropic subscription via ANTHROPIC_AUTH_TOKEN=ollama plus ANTHROPIC_BASE_URL pointing at the Ollama endpoint. -- evidence: [README.md#L753-L753](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L753-L753) (`clm_17cfd494612e019f235ee8c26ac4bb7241215c750aa4c0e5511885bf0e256f17`)

## memory-state (1 claim(s))

- [observation/documented] Persistence is via bind mounts: ./data/claude maps to /home/claude/.claude (holding settings, credentials, and Claude's memory) and ./workspace maps to /workspace; on every boot Git/gh config is linked into the .claude mount, and bootstrap.sh copies defaults only on first boot, marking it with .holyclaude-bootstrapped. -- evidence: [README.md#L798-L798](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L798-L798), [README.md#L272-L301](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L272-L301), [README.md#L796-L796](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L796-L796), [README.md#L780-L783](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L780-L783), [README.md#L794-L794](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L794-L794) (`clm_996a0de973fd74e5a31437dedd19160c5089ba00a1795d1bfc807932414257ac`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] OpenAI API keys cannot authenticate Claude Code; they work with the bundled Codex CLI instead, and ChatGPT Plus/Pro subscribers authenticate Codex via codex login --device-auth, optionally exposing port 1455 for the browser callback flow. -- evidence: [README.md#L206-L208](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L206-L208), [README.md#L210-L210](https://github.com/CoderLuii/HolyClaude/blob/651c48fc01a963acd605aa565bb9da8f9db9b340/README.md#L210-L210) (`clm_834c894ec4750c146a70875c9668e9f65d391410dc5fa087059421ce06d2e324`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

