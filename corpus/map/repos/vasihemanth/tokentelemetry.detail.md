# vasihemanth/tokentelemetry -- full detail

[Back to orientation](tokentelemetry.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/vasihemanth/tokentelemetry/0d691ae343ed31991e504a738bb1b288eea3b2ee/584cdc952070dd60.json](../../../wiki/dossiers/vasihemanth/tokentelemetry/0d691ae343ed31991e504a738bb1b288eea3b2ee/584cdc952070dd60.json)

## specifications (1 claim(s))

- [observation/documented] TokenTelemetry is a free, open-source, 100% local observability dashboard tracking token usage, LLM costs, tool calls, session traces, and reasoning steps across AI coding agents, with no signup or cloud. -- evidence: [README.md#L5-L5](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L5-L5), [README.md#L15-L15](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L15-L15) (`clm_68b0c3e344fb183685739c8b58069a1b5973ce0fa73c6093178fe77ab591ccad`)

## components (1 claim(s))

- [observation/documented] The project structure includes a Python FastAPI backend that reads agent logs and serves a REST API, a Next.js 16 React frontend dashboard, a cross-platform bin/cli.js launcher, and install.sh/install.ps1 installers. -- evidence: [README.md#L335-L342](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L335-L342) (`clm_dcc2a07f58084c5a5c433d81272c1e7f82aeb1eb378c76093cf4fcad683a8d10`)

## design-choices (2 claim(s))

- [observation/documented] Budgets are observational by design: TokenTelemetry tracks spend against user-set limits and alerts at 80% and 100% thresholds but never blocks an agent. -- evidence: [README.md#L173-L173](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L173-L173), [README.md#L111-L123](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L111-L123) (`clm_a8151abc510ddd17b79baa7ea2860d8d31873c749d4b43250849136ef534d861`)
- [observation/documented] Plan-limit readings come from the provider's own login data on the machine rather than being estimated from history, and the UI distinguishes provider plan ceilings from user-defined project budgets. -- evidence: [README.md#L181-L181](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L181-L181), [README.md#L179-L179](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L179-L179), [README.md#L183-L183](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L183-L183) (`clm_b15ac39f424c74f9b3055310193167d06eca8b31ec65ff4491727c394c505e3f`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributions follow a branch-and-PR flow (feat/ branches, conventional commit messages), and ADR-0001 requires an architecture decision record in docs/adr/ committed in the same PR as the code it describes. -- evidence: [README.md#L436-L436](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L436-L436), [README.md#L442-L444](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L442-L444), [docs/adr/0001-record-architecture-decisions.md#L38-L44](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/docs/adr/0001-record-architecture-decisions.md#L38-L44), [docs/adr/0001-record-architecture-decisions.md#L19-L23](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/docs/adr/0001-record-architecture-decisions.md#L19-L23) (`clm_79be6ddfaadeee675fdc7effff93b4c9724d3f6ff99ae5110747602707c579b6`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Remote access is opt-in: --host 0.0.0.0 exposes the backend, a random auth token is auto-generated and printed once unless --auth-token or --insecure-no-auth is passed, and loopback clients never need the token. -- evidence: [README.md#L297-L301](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L297-L301), [README.md#L285-L285](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L285-L285) (`clm_706ef55e52cf12d2ef5cd096912a5e44098a56dc70a633f84ca5b821ec6acb6d`)
- [observation/documented] The Hermes dashboard plugin embeds TokenTelemetry as a tab inside Hermes's own web dashboard (port 9119 to 3000), is pure-frontend with no extra backend, and deep-links to Analytics, Projects, and All Agents pages. -- evidence: [README.md#L89-L89](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L89-L89), [README.md#L105-L105](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L105-L105) (`clm_7be3102974ebd2a6598b9688012b82c1920d734b3286e4faa6b6716455833b9c`)

## memory-state (2 claim(s))

- [observation/documented] State lives in ~/.tokentelemetry/ as hand-editable JSON files (aliases, hidden projects, preferences, billing, power, VERSION), with no database; a data directory can be relocated via --data-dir or TOKENTELEMETRY_DATA_DIR. -- evidence: [README.md#L218-L226](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L218-L226), [README.md#L243-L245](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L243-L245), [README.md#L235-L239](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L235-L239), [README.md#L216-L216](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L216-L216), [README.md#L228-L228](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L228-L228) (`clm_218e15edcc6f415087bcabd838011b9a0955da30cd668baed3cf0d9a3d2c1314`)
- [observation/documented] Per ADR-0002, a durable local SQLite store at ~/.tokentelemetry/history.db is upserted on every background scan, storing raw facts so analytics history survives agents pruning their transcripts; derived insights are recomputed at read time. -- evidence: [docs/adr/0002-durable-history-rollup.md#L25-L31](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/docs/adr/0002-durable-history-rollup.md#L25-L31), [docs/adr/0002-durable-history-rollup.md#L51-L64](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/docs/adr/0002-durable-history-rollup.md#L51-L64), [docs/adr/0002-durable-history-rollup.md#L33-L35](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/docs/adr/0002-durable-history-rollup.md#L33-L35) (`clm_3b105f84ba2154e987ae0ed3ec93550f58bb04873265bde7e0d18ddc587a405a`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Requirements are Node.js 20.9+, Python 3.9+, git, and at least one supported AI coding agent already installed; a badge also mentions Node 18+. -- evidence: [README.md#L9-L13](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L9-L13), [README.md#L207-L210](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L207-L210) (`clm_3c84438fa8653291dd4085852d5af5781d91abd671ab05ea36bf1d7d75e9fd45`)

## limitations (2 claim(s))

- [observation/documented] Per ADR-0002, history capture starts from the first run (already-pruned transcripts are unrecoverable), pruned sessions without archival show only in aggregates, and transcript archival currently resolves single-file transcripts only for claude/codex. -- evidence: [docs/adr/0002-durable-history-rollup.md#L51-L64](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/docs/adr/0002-durable-history-rollup.md#L51-L64) (`clm_e21e58a6811eb912023a3110359ae1675479d67c3a55ac9a7443bc11a165363a`)
- [observation/documented] Hermes support reads $HERMES_HOME (or ~/.hermes/) locally on the same host, with no remote-DB mode yet; Qoder support tracks credits rather than tokens because Qoder records none. -- evidence: [README.md#L46-L63](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L46-L63), [README.md#L85-L85](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L85-L85) (`clm_cacefcb6fb54ab215d891f43c7fe0c78c075932c9f93bde9483b81405aa9feab`)

## relevance (1 claim(s))

- [observation/documented] Unlike Langfuse, LangSmith, or Helicone, TokenTelemetry requires no code instrumentation, account, SDK, or API key — it works by reading the log files agents already write, fully locally. -- evidence: [README.md#L387-L396](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L387-L396), [README.md#L360-L361](https://github.com/VasiHemanth/tokentelemetry/blob/0d691ae343ed31991e504a738bb1b288eea3b2ee/README.md#L360-L361) (`clm_e3c30333f6ca868772cfa0db363aaac78e0d381ec03ab945876b97ff9e878de2`)

