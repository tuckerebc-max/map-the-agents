# kenn-io/kata -- full detail

[Back to orientation](kata.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/kenn-io/kata/f41a33383aba48941cb94b987124f5cd14840029/f7283538f30a32a1.json](../../../wiki/dossiers/kenn-io/kata/f41a33383aba48941cb94b987124f5cd14840029/f7283538f30a32a1.json)

## specifications (1 claim(s))

- [observation/documented] kata is a durable task ledger for coding agents and humans: agents create, claim, relate, and close issues with evidence via CLI, while humans supervise in a terminal UI. -- evidence: [README.md#L3-L3](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L3-L3), [README.md#L5-L20](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L5-L20) (`clm_2ea7f8f489d5b6ec35b8382ef7a8e28bf02a6179c72919e880d6269ccf334bea`)

## components (2 claim(s))

- [observation/documented] The product ships as one Go binary with a CLI, a long-lived daemon, a TUI, and a browser UI served by the daemon with no separate backend. -- evidence: [docs/design/architecture.md#L11-L13](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L11-L13), [README.md#L109-L120](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L109-L120) (`clm_7558ec539179c9b0b5fb17d46dba15625093c92aca35bbcbfbbfb1866c250621`)
- [observation/documented] By default issue state lives in a local SQLite database under KATA_HOME; teams can opt into a remote daemon or federation, and a shared daemon can use Postgres via KATA_DSN. -- evidence: [README.md#L5-L20](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L5-L20), [README.md#L109-L120](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L109-L120) (`clm_00e40100e2d03306aae4a59f12b46d255a26fd1fb10d9dd744ec3f3b94cdeb7f`)

## design-choices (4 claim(s))

- [observation/documented] Projects are bound to workspaces explicitly via a committed .kata.toml, never inferred from the current directory; outside a bound workspace every command except kata init fails with project_not_initialized. -- evidence: [docs/design/architecture.md#L89-L100](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L89-L100), [docs/design/architecture.md#L86-L87](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L86-L87) (`clm_9a667136be04ff445a4314681169935c2946185001a53320c731d2f92174a6d3`)
- [observation/documented] Workspace identity derives from the normalized git remote URL rather than the filesystem path, so clones resolve to the same project; one git repository attaches to exactly one project. -- evidence: [docs/design/architecture.md#L104-L112](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L104-L112) (`clm_3d3002806729950234aaffc9759ad092cfbd88ac69489d08cef8df52280d327b`)
- [observation/documented] Closing an issue is an explicit API mutation carrying a reason, message, typed evidence, and actor attribution; kata never infers closure from git history. -- evidence: [docs/design/architecture.md#L167-L170](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L167-L170), [README.md#L109-L120](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L109-L120), [docs/design/architecture.md#L172-L179](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L172-L179) (`clm_0069618a1905deb33c4a79b04f7b94e692c96adbd183f122581c028cddf9779a`)
- [observation/documented] The surface is deliberately small: three relationship types, labels, owners, comments, and a constrained integer priority 0-4; there is no in_progress status, severity field, threaded replies, reactions, attachments, or markdown rendering. -- evidence: [docs/design/architecture.md#L25-L32](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L25-L32) (`clm_3e3425fb2166eb68f9fdb901185b35e92b3106eab6b25f1057027a73901f37c1`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors should see docs/development/contributing.md for repository layout and local checks including make test, make lint, make vet, and make nilaway. -- evidence: [README.md#L228-L230](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L228-L230) (`clm_960e338f85662cc0c11127b6beb4ae253fe01e2900c159e686918c1478ef2d5a`)
- [observation/documented] kata quickstart (alias kata agent-instructions) prints an operating contract for coding agents: search before creating, pass idempotency keys, prefer --agent output, claim work, and close only verified work with evidence. -- evidence: [README.md#L178-L183](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L178-L183) (`clm_ba58060823cb522ae4a6d787c5fda77807758d646cc0968665252665c62fd0eb`)
- [observation/documented] kata init --with-agents writes a managed briefing into AGENTS.md/CLAUDE.md without overwriting existing content, and --with-codex-hooks installs structured Codex SessionStart hooks in .codex/hooks.json. -- evidence: [README.md#L100-L105](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L100-L105), [README.md#L221-L224](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L221-L224) (`clm_668d7dd62c30f29502c922545840f93b4560fba604e36c08db8b26a90b460872`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] All reads and writes go through kata's HTTP API; no client opens SQLite or Postgres directly, and a Go app can mount the listener-free service in-process. -- evidence: [docs/design/architecture.md#L47-L53](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L47-L53), [README.md#L5-L20](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L5-L20) (`clm_2a93491b1c047b51d85a89b0e727b42c6a4d70169445e82ef1e16ead53e4c486`)
- [observation/documented] The CLI offers agent-oriented ergonomics: stable short refs, --json and --agent output, idempotent creates, semantic-aware search, a claim flow, and predictable failure modes. -- evidence: [docs/design/architecture.md#L15-L18](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L15-L18), [README.md#L109-L120](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L109-L120) (`clm_22c69789f13d00e4cc72b49dc5ad28928c01efea182316a37a049d6e99ab22d5`)

## memory-state (1 claim(s))

- [observation/documented] Every state change appends to an immutable event log with the actor recorded; actors are free-form snapshots on events, not foreign keys, and there is no global user registry. -- evidence: [docs/design/architecture.md#L20-L23](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L20-L23), [docs/design/architecture.md#L160-L163](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L160-L163) (`clm_1d761045d120ea8923262dbdeef993672c801706f18f46f8bb703e82304d9a4b`)

## orchestration (2 claim(s))

- [observation/documented] Hooks run local commands after database commit on a bounded worker pool, invoked without a shell via exec.Command with event data as JSON on stdin; hooks are not a sandbox and run with the daemon's OS user. -- evidence: [docs/design/architecture.md#L186-L195](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L186-L195), [docs/design/architecture.md#L183-L184](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L183-L184) (`clm_970a78ae79337d59265c6517bb5db2f6b618efc17772bf26735c3df95c7e145b`)
- [observation/documented] Clients auto-start a local daemon when none is reachable; an autostart_idle_timeout lets such a narrowly scoped daemon exit after foreground use stops, while explicit daemons remain long-running. -- evidence: [docs/design/autostart-idle-shutdown.md#L23-L27](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/autostart-idle-shutdown.md#L23-L27), [docs/design/autostart-idle-shutdown.md#L3-L9](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/autostart-idle-shutdown.md#L3-L9) (`clm_16169b53e2cc0e4832f4a8f9eee939ee0aa5b6f4c8d37ddc2a7e78cae1340972`)

## tools-permissions (2 claim(s))

- [observation/documented] Local mode trusts the OS user with no authentication on a Unix socket or loopback listener; shared/remote modes require a bearer token and explicit trust opt-in before credentials cross a plaintext non-loopback connection. -- evidence: [docs/design/architecture.md#L141-L149](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L141-L149), [docs/design/architecture.md#L120-L125](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L120-L125) (`clm_8c52c55eccbd5b2c6970defb70c71ad8b502d7ea2e24c19825928526eb60a8e3`)
- [observation/documented] The loopback HTTP server rejects non-empty Origin headers, requires application/json Content-Type on mutations, and emits no CORS headers to resist drive-by browser requests. -- evidence: [docs/design/architecture.md#L120-L125](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L120-L125) (`clm_89e6452e8b4e8fd72736a2a91c39c87bf02b8a3ac5d94656580e0409a83deccc`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] kata uses pure-Go SQLite via modernc.org/sqlite with no CGO, a Huma-based HTTP API over a Unix socket, and claims no runtime dependencies beyond the single binary. -- evidence: [docs/design/architecture.md#L36-L43](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L36-L43), [README.md#L109-L120](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L109-L120) (`clm_4e78ed48a486b339474f3c80394ef7cb852392df2973ed88bd44f00e912a91e4`)
- [observation/documented] Building from source requires Go 1.27 or later; module-source installs include the CLI, daemon, and TUI but not the compiled browser bundle needed for `kata ui`. -- evidence: [README.md#L69-L71](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L69-L71), [README.md#L60-L63](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L60-L63) (`clm_ea2766fb551d3f1dade01d0efad98044e1306d493c4a47acb41a524aee85aab8`)

## limitations (3 claim(s))

- [observation/documented] kata is intentionally not a project-management suite, git workflow engine, agent worker pool, or SaaS tracker; it does not ride git remotes for sharing, relying on the remote daemon and federation instead. -- evidence: [README.md#L124-L126](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L124-L126), [README.md#L136-L144](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/README.md#L136-L144) (`clm_7dbb4dd46e57259ad759c2c67680af5cc34dab6e9cfbd95fda4154a0cd21a92f`)
- [observation/documented] Permanent non-goals include workspace-local behavior overrides, per-issue SSE subscriptions, bulk mutation endpoints, remote webhooks, and a (kata-#N) commit-message convention. -- evidence: [docs/design/architecture.md#L216-L223](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/architecture.md#L216-L223) (`clm_6535b61aee64a46d6b5d041021467c3238e8df80651fc688e233d709c10108e2`)
- [observation/documented] On an idle-enabled auto-start daemon, scheduled work is opportunistic: timers do not keep the process resident, so continuous sync, federation, timed claims, embeddings, or hooks need an explicit service-managed daemon. -- evidence: [docs/design/autostart-idle-shutdown.md#L135-L139](https://github.com/kenn-io/kata/blob/f41a33383aba48941cb94b987124f5cd14840029/docs/design/autostart-idle-shutdown.md#L135-L139) (`clm_2cb762dd951f0df0bc2aa614f13ca8aa4c7feaf13a95ec1136cdf1683d910641`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

