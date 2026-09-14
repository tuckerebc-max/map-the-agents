---
access: public
aliases: []
claim_ids:
- clm_17cfd494612e019f235ee8c26ac4bb7241215c750aa4c0e5511885bf0e256f17
- clm_2b208af703c1309fb14678ddb1b7ef43ee00b56bbb84f4603add6d94b813f4e8
- clm_4350ee935bbe2b417106246efadca148d48c44ccbad14fa9ae7377c5a1dd2b92
- clm_59ddcfbeb481916d3b6946b5013ee2b96a275f36e1180002e410367686d3a887
- clm_5e6130c76f958b181253973a2144dcad524b001dad5c6d3229d075ef86daa7fb
- clm_834c894ec4750c146a70875c9668e9f65d391410dc5fa087059421ce06d2e324
- clm_996a0de973fd74e5a31437dedd19160c5089ba00a1795d1bfc807932414257ac
- clm_adb2dd625e4f4f78c5bf22b20786152810090a2ae97a76e0d5a48d73361732f5
- clm_ba4eb6720683133398e9d74a0b7448d09ffb76f5cf15343d24c31930336d01d4
- clm_c0254316595719bf4d7309a6333c3b2ad47fd4d18192cf89ce16862df5350254
- clm_d15804f92f7e1ee1bba4295ee9384bad14f7e4e4b819f430e2e1cc1a7d398bc5
- clm_e3f3cc373802532e8d253e4bc5de229305fe7150ec357f3d2b6b34787a9dcb4d
- clm_efbd9e32c74522b076cb6d5e75c71d85b485f5c9fc709f8e340aa7664e2cd9e7
- clm_f84a68605642efca20febf07e64953adaa33b80fd95f29ace6b5e951a4219855
maturity: draft
page_id: pg_af2daa3a8ac45dcf9b10db2f0f31cd21
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_980bbb35c5665b17a699fd87bef01b62
title: CoderLuii/HolyClaude/README.md @ 651c48fc01a9
updated_at: '2026-09-14T03:42:12Z'
---

# CoderLuii/HolyClaude/README.md @ 651c48fc01a9

<!-- rcw:begin owner=source:src_980bbb35c5665b17a699fd87bef01b62 block=evidence -->
- Ollama is supported as an alternative to an Anthropic subscription via ANTHROPIC_AUTH_TOKEN=ollama plus ANTHROPIC_BASE_URL pointing at the Ollama endpoint. [@claim:clm_17cfd494612e019f235ee8c26ac4bb7241215c750aa4c0e5511885bf0e256f17]
- Environment variables are documented as all optional, covering timezone (TZ), UID/GID remapping (PUID/PGID), Node heap size, SMB polling flags, Apprise notification URLs (Discord, Telegram, Slack, email, etc.), and AI provider API keys. [@claim:clm_2b208af703c1309fb14678ddb1b7ef43ee00b56bbb84f4603add6d94b813f4e8]
- Desloppify ships as a passive CLI in both images; it performs no scans or workspace edits unless invoked, and optional global skill setup at container start is controlled by HOLYCLAUDE_DESLOPPIFY_SETUP with values like off, claude, codex, gemini, all, or opencode (full image only). [@claim:clm_4350ee935bbe2b417106246efadca148d48c44ccbad14fa9ae7377c5a1dd2b92]
- Authentication is done through the CloudCLI web UI: Claude Max/Pro users sign in via OAuth and API-key users paste their key; the container relays no credentials, with tools reading them from container files, bind mounts, or environment variables. [@claim:clm_59ddcfbeb481916d3b6946b5013ee2b96a275f36e1180002e410367686d3a887]
- The compose templates set shm_size 2g because Chromium heavily uses /dev/shm and Docker's 64MB default causes tab crashes, and grant SYS_ADMIN, SYS_PTRACE, and seccomp=unconfined as the retained browser profile, with hardening described as a separate change. [@claim:clm_5e6130c76f958b181253973a2144dcad524b001dad5c6d3229d075ef86daa7fb]
- OpenAI API keys cannot authenticate Claude Code; they work with the bundled Codex CLI instead, and ChatGPT Plus/Pro subscribers authenticate Codex via codex login --device-auth, optionally exposing port 1455 for the browser callback flow. [@claim:clm_834c894ec4750c146a70875c9668e9f65d391410dc5fa087059421ce06d2e324]
- Persistence is via bind mounts: ./data/claude maps to /home/claude/.claude (holding settings, credentials, and Claude's memory) and ./workspace maps to /workspace; on every boot Git/gh config is linked into the .claude mount, and bootstrap.sh copies defaults only on first boot, marking it with .holyclaude-bootstrapped. [@claim:clm_996a0de973fd74e5a31437dedd19160c5089ba00a1795d1bfc807932414257ac]
- The image bundles Chromium with Xvfb and Playwright for headless browser screenshots and testing, plus database clients (psql, redis-cli, sqlite3, MariaDB-based mysql) and GitHub CLI. [@claim:clm_adb2dd625e4f4f78c5bf22b20786152810090a2ae97a76e0d5a48d73361732f5]
- The full image ships eight AI CLIs — Claude Code, Gemini, Codex, Cursor, TaskMaster, Junie, OpenCode, and Pi — while the slim image ships the five core ones (Claude Code, Gemini, Codex, Cursor, TaskMaster), with slim installing missing tools on demand. [@claim:clm_ba4eb6720683133398e9d74a0b7448d09ffb76f5cf15343d24c31930336d01d4]
- The container runs the official Anthropic Claude Code CLI (not a wrapper or proxy), served through a CloudCLI web UI on port 3001, with s6-overlay as PID 1 supervising Xvfb on :99 and optional sshd. [@claim:clm_c0254316595719bf4d7309a6333c3b2ad47fd4d18192cf89ce16862df5350254]
- The quick-start workflow is: create a docker-compose.yaml from a provided template, run docker compose up -d, then open http://localhost:3001 and create a CloudCLI account; no .env file is required. [@claim:clm_d15804f92f7e1ee1bba4295ee9384bad14f7e4e4b819f430e2e1cc1a7d398bc5]
- The web UI port is bound to 127.0.0.1 by default, and users needing remote access are directed to Tailscale or Cloudflare Tunnel rather than port forwarding. [@claim:clm_e3f3cc373802532e8d253e4bc5de229305fe7150ec357f3d2b6b34787a9dcb4d]
- Repository development practice: release-sensitive facts are published in contracts/product-facts.json, and the release workflow checks that contract against the Dockerfile and Compose files before building images. [@claim:clm_efbd9e32c74522b076cb6d5e75c71d85b485f5c9fc709f8e340aa7664e2cd9e7]
- Two image variants are published on Docker Hub: latest (full, everything pre-installed) and slim (core tools only, with Claude installing extras on demand), plus pinned X.Y.Z and X.Y.Z-slim tags for production stability. [@claim:clm_f84a68605642efca20febf07e64953adaa33b80fd95f29ace6b5e951a4219855]
<!-- rcw:end owner=source:src_980bbb35c5665b17a699fd87bef01b62 block=evidence -->

## Researcher notes

