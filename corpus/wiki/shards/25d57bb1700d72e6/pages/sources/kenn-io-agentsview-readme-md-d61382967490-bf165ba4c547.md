---
access: public
aliases: []
claim_ids:
- clm_05c05b4bedad0c143adad02e640e6452966319f73b93b6f6d9ea0a6effba7739
- clm_099faebbe18e45737952f8e7a174d17fcc457581cc224c4fb942fa2932601407
- clm_29356ed5e49796a2076775b733278f93cef66b6fd06a3424fd7a8e24710ffb19
- clm_3686de3a820e69c33aa043f1c1580406b363f125289c331cd94f8a09a6625f29
- clm_4d17d6f78b46a3de9f5bd69a9b6949bf0288e6e9707cd3816721f4985ff17c7d
- clm_640dd262d68ca7da7aa53ab7bccdbe923d4f7be5dbf33c1a8b9f5c8cf6f9201d
- clm_6ce2f92e4a3970e44b739456383b225f4252b2dfa59c3eeaba44289e6b6faf5c
- clm_86463de79669ddfbde84cc02ed0c760a395d2d0254da8e8aa39017ee0baf0313
- clm_87ca86287f73e1f716674024cb7222c856290d65af2b6b057b75ebd5c487d6a7
- clm_ac32f679f03cc9b3ebad6b87ae22d66db2d45e22010111893e5118c04fa4b158
- clm_b6225177e28586c668ee0b049c5331280f1227a75a42b64c5770a1e4f3942b5d
- clm_cc052e76cf6eb1774c899bf8742a6e32424828218569cd07bf4b73073bca894e
- clm_cd048aa49803752ea4798a064394a5344b8920fc5b061cbcd645020261c5a54f
- clm_d844ae94cca37cc6718e46b5afebbea603f0229efaf0444f880a8b6b4831ce80
- clm_de37c7dc35293f2a170cfaedfe106a6cbf20d59fb93e29745ca25a8172105080
maturity: draft
page_id: pg_18138a23838a5ec38cfabf165ba4c547
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cf70a40a4c61502c9cd2a2c0a0015f4c
title: kenn-io/agentsview/README.md @ d61382967490
updated_at: '2026-09-14T04:02:35Z'
---

# kenn-io/agentsview/README.md @ d61382967490

<!-- rcw:begin owner=source:src_cf70a40a4c61502c9cd2a2c0a0015f4c block=evidence -->
- Telemetry is a limited anonymous daemon_active ping to PostHog at startup and every 24 hours, excluding session, project, prompt, file path, account, or machine identity, and can be disabled via environment variables. [@claim:clm_05c05b4bedad0c143adad02e640e6452966319f73b93b6f6d9ea0a6effba7739]
- The CLI offers serve, daemon (start/status/restart/stop), session list, and usage daily subcommands; on first run it discovers sessions, syncs them into local SQLite, and serves a web UI at http://127.0.0.1:8080. [@claim:clm_099faebbe18e45737952f8e7a174d17fcc457581cc224c4fb942fa2932601407]
- The server binds to loopback by default and validates the request Host header to guard against DNS-rebinding; forwarded access needs --public-url, and exposure beyond loopback should enable --require-auth. [@claim:clm_29356ed5e49796a2076775b733278f93cef66b6fd06a3424fd7a8e24710ffb19]
- Aider is opt-in because it has no central session directory, Amp support is deprecated since current Amp releases may store threads server-side, and JetBrains Copilot requires an external exporter tool. [@claim:clm_3686de3a820e69c33aa043f1c1580406b363f125289c331cd94f8a09a6625f29]
- Repository development practice: make bench-backends requires Docker and testcontainers to benchmark SQLite, DuckDB, and PostgreSQL store reads on a default fixture of 1,000 sessions and 64,000 messages, scalable via BENCH_BACKENDS_* env vars. [@claim:clm_4d17d6f78b46a3de9f5bd69a9b6949bf0288e6e9707cd3816721f4985ff17c7d]
- The project layout includes a cmd/agentsview CLI entrypoint, internal Go packages (config, db, parser, server, sync, postgres), a Svelte 5 SPA frontend, and a Tauri desktop wrapper. [@claim:clm_640dd262d68ca7da7aa53ab7bccdbe923d4f7be5dbf33c1a8b9f5c8cf6f9201d]
- DuckDB search currently falls back to substring/regex behavior; SQLite FTS5 remains the indexed search path for primary local serving. [@claim:clm_6ce2f92e4a3970e44b739456383b225f4252b2dfa59c3eeaba44289e6b6faf5c]
- A REST endpoint GET /api/v1/sessions/{id}/usage returns fields such as total_output_tokens, peak_context_tokens, and cost as an integer microdollar object; existing sessions return 200 and missing ones 404. [@claim:clm_86463de79669ddfbde84cc02ed0c760a395d2d0254da8e8aa39017ee0baf0313]
- The tool discovers sessions from multiple coding agents including Aider, Amp, Antigravity, Goose, Grok, and Copilot, with per-agent session directories and env-var overrides such as AIDER_DIR, GROK_DIR, and GOOSE_PATH_ROOT. [@claim:clm_87ca86287f73e1f716674024cb7222c856290d65af2b6b057b75ebd5c487d6a7]
- Quack serving uses conservative defaults: local serving binds to loopback, requires a token, and rejects non-loopback plain HTTP unless --allow-insecure is explicitly passed. [@claim:clm_ac32f679f03cc9b3ebad6b87ae22d66db2d45e22010111893e5118c04fa4b158]
- Building the project requires Go 1.27+ with CGO and Node.js 24.11+. [@claim:clm_b6225177e28586c668ee0b049c5331280f1227a75a42b64c5770a1e4f3942b5d]
- SQLite is the primary local archive with FTS5 search and a writable UI; PostgreSQL is an optional shared team backend served read-only, and DuckDB is an optional mirror file or Quack endpoint served read-only. [@claim:clm_cc052e76cf6eb1774c899bf8742a6e32424828218569cd07bf4b73073bca894e]
- The daemon is a single process hosting the web UI, API, session sync, and file watchers; background daemons self-exit after an idle period unless a client request or daemon-owned job is active. [@claim:clm_cd048aa49803752ea4798a064394a5344b8920fc5b061cbcd645020261c5a54f]
- Cost calculation uses LiteLLM and OpenRouter pricing rates with an offline fallback, and reports authoritative Copilot CLI billing totals when session logs provide them. [@claim:clm_d844ae94cca37cc6718e46b5afebbea603f0229efaf0444f880a8b6b4831ce80]
- Repository development practice: building and testing use make targets (make dev, make build, make test with CGO and fts5 tags, make lint, make e2e for Playwright), with prek-based pre-commit hooks installed via make lint-tools and make install-hooks. [@claim:clm_de37c7dc35293f2a170cfaedfe106a6cbf20d59fb93e29745ca25a8172105080]
<!-- rcw:end owner=source:src_cf70a40a4c61502c9cd2a2c0a0015f4c block=evidence -->

## Researcher notes

