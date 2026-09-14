# kenn-io/agentsview -- full detail

[Back to orientation](agentsview.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/kenn-io/agentsview/d61382967490e72608ae8064d7a06bec3468b1d6/854bb9d72f0e0765.json](../../../wiki/dossiers/kenn-io/agentsview/d61382967490e72608ae8064d7a06bec3468b1d6/854bb9d72f0e0765.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The project layout includes a cmd/agentsview CLI entrypoint, internal Go packages (config, db, parser, server, sync, postgres), a Svelte 5 SPA frontend, and a Tauri desktop wrapper. -- evidence: [README.md#L747-L752](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L747-L752) (`clm_640dd262d68ca7da7aa53ab7bccdbe923d4f7be5dbf33c1a8b9f5c8cf6f9201d`)

## design-choices (3 claim(s))

- [observation/documented] The daemon is a single process hosting the web UI, API, session sync, and file watchers; background daemons self-exit after an idle period unless a client request or daemon-owned job is active. -- evidence: [README.md#L86-L90](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L86-L90), [README.md#L56-L61](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L56-L61) (`clm_cd048aa49803752ea4798a064394a5344b8920fc5b061cbcd645020261c5a54f`)
- [observation/documented] The server binds to loopback by default and validates the request Host header to guard against DNS-rebinding; forwarded access needs --public-url, and exposure beyond loopback should enable --require-auth. -- evidence: [README.md#L141-L143](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L141-L143), [README.md#L99-L103](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L99-L103), [README.md#L116-L122](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L116-L122) (`clm_29356ed5e49796a2076775b733278f93cef66b6fd06a3424fd7a8e24710ffb19`)
- [observation/documented] Telemetry is a limited anonymous daemon_active ping to PostHog at startup and every 24 hours, excluding session, project, prompt, file path, account, or machine identity, and can be disabled via environment variables. -- evidence: [README.md#L689-L696](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L689-L696) (`clm_05c05b4bedad0c143adad02e640e6452966319f73b93b6f6d9ea0a6effba7739`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: building and testing use make targets (make dev, make build, make test with CGO and fts5 tags, make lint, make e2e for Playwright), with prek-based pre-commit hooks installed via make lint-tools and make install-hooks. -- evidence: [README.md#L725-L731](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L725-L731), [README.md#L741-L743](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L741-L743), [README.md#L718-L723](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L718-L723) (`clm_de37c7dc35293f2a170cfaedfe106a6cbf20d59fb93e29745ca25a8172105080`)
- [observation/documented] Repository development practice: make bench-backends requires Docker and testcontainers to benchmark SQLite, DuckDB, and PostgreSQL store reads on a default fixture of 1,000 sessions and 64,000 messages, scalable via BENCH_BACKENDS_* env vars. -- evidence: [README.md#L733-L739](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L733-L739) (`clm_4d17d6f78b46a3de9f5bd69a9b6949bf0288e6e9707cd3816721f4985ff17c7d`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI offers serve, daemon (start/status/restart/stop), session list, and usage daily subcommands; on first run it discovers sessions, syncs them into local SQLite, and serves a web UI at http://127.0.0.1:8080. -- evidence: [README.md#L42-L50](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L42-L50), [README.md#L52-L54](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L52-L54) (`clm_099faebbe18e45737952f8e7a174d17fcc457581cc224c4fb942fa2932601407`)
- [observation/documented] A REST endpoint GET /api/v1/sessions/{id}/usage returns fields such as total_output_tokens, peak_context_tokens, and cost as an integer microdollar object; existing sessions return 200 and missing ones 404. -- evidence: [README.md#L253-L255](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L253-L255), [README.md#L257-L264](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L257-L264) (`clm_86463de79669ddfbde84cc02ed0c760a395d2d0254da8e8aa39017ee0baf0313`)
- [observation/documented] The tool discovers sessions from multiple coding agents including Aider, Amp, Antigravity, Goose, Grok, and Copilot, with per-agent session directories and env-var overrides such as AIDER_DIR, GROK_DIR, and GOOSE_PATH_ROOT. -- evidence: [README.md#L408-L413](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L408-L413), [README.md#L346-L406](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L346-L406), [README.md#L465-L466](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L465-L466), [README.md#L415-L419](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L415-L419), [README.md#L340-L344](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L340-L344) (`clm_87ca86287f73e1f716674024cb7222c856290d65af2b6b057b75ebd5c487d6a7`)

## memory-state (1 claim(s))

- [observation/documented] SQLite is the primary local archive with FTS5 search and a writable UI; PostgreSQL is an optional shared team backend served read-only, and DuckDB is an optional mirror file or Quack endpoint served read-only. -- evidence: [README.md#L669-L672](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L669-L672) (`clm_cc052e76cf6eb1774c899bf8742a6e32424828218569cd07bf4b73073bca894e`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Quack serving uses conservative defaults: local serving binds to loopback, requires a token, and rejects non-loopback plain HTTP unless --allow-insecure is explicitly passed. -- evidence: [README.md#L659-L665](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L659-L665) (`clm_ac32f679f03cc9b3ebad6b87ae22d66db2d45e22010111893e5118c04fa4b158`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Cost calculation uses LiteLLM and OpenRouter pricing rates with an offline fallback, and reports authoritative Copilot CLI billing totals when session logs provide them. -- evidence: [README.md#L225-L232](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L225-L232) (`clm_d844ae94cca37cc6718e46b5afebbea603f0229efaf0444f880a8b6b4831ce80`)
- [observation/documented] Building the project requires Go 1.27+ with CGO and Node.js 24.11+. -- evidence: [README.md#L716-L716](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L716-L716) (`clm_b6225177e28586c668ee0b049c5331280f1227a75a42b64c5770a1e4f3942b5d`)

## limitations (2 claim(s))

- [observation/documented] Aider is opt-in because it has no central session directory, Amp support is deprecated since current Amp releases may store threads server-side, and JetBrains Copilot requires an external exporter tool. -- evidence: [README.md#L454-L458](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L454-L458), [README.md#L340-L344](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L340-L344) (`clm_3686de3a820e69c33aa043f1c1580406b363f125289c331cd94f8a09a6625f29`)
- [observation/documented] DuckDB search currently falls back to substring/regex behavior; SQLite FTS5 remains the indexed search path for primary local serving. -- evidence: [README.md#L676-L685](https://github.com/kenn-io/agentsview/blob/d61382967490e72608ae8064d7a06bec3468b1d6/README.md#L676-L685) (`clm_6ce2f92e4a3970e44b739456383b225f4252b2dfa59c3eeaba44289e6b6faf5c`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

