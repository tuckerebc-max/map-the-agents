---
access: public
aliases: []
claim_ids:
- clm_0069618a1905deb33c4a79b04f7b94e692c96adbd183f122581c028cddf9779a
- clm_1d761045d120ea8923262dbdeef993672c801706f18f46f8bb703e82304d9a4b
- clm_22c69789f13d00e4cc72b49dc5ad28928c01efea182316a37a049d6e99ab22d5
- clm_2a93491b1c047b51d85a89b0e727b42c6a4d70169445e82ef1e16ead53e4c486
- clm_3d3002806729950234aaffc9759ad092cfbd88ac69489d08cef8df52280d327b
- clm_3e3425fb2166eb68f9fdb901185b35e92b3106eab6b25f1057027a73901f37c1
- clm_4e78ed48a486b339474f3c80394ef7cb852392df2973ed88bd44f00e912a91e4
- clm_6535b61aee64a46d6b5d041021467c3238e8df80651fc688e233d709c10108e2
- clm_7558ec539179c9b0b5fb17d46dba15625093c92aca35bbcbfbbfb1866c250621
- clm_89e6452e8b4e8fd72736a2a91c39c87bf02b8a3ac5d94656580e0409a83deccc
- clm_8c52c55eccbd5b2c6970defb70c71ad8b502d7ea2e24c19825928526eb60a8e3
- clm_970a78ae79337d59265c6517bb5db2f6b618efc17772bf26735c3df95c7e145b
- clm_9a667136be04ff445a4314681169935c2946185001a53320c731d2f92174a6d3
maturity: draft
page_id: pg_eb5cc7ca5f605bf49c6f7ef86223719b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f8e530c979eb5711b2ebbde75659c344
title: kenn-io/kata/docs/design/architecture.md @ f41a33383aba
updated_at: '2026-09-14T04:02:20Z'
---

# kenn-io/kata/docs/design/architecture.md @ f41a33383aba

<!-- rcw:begin owner=source:src_f8e530c979eb5711b2ebbde75659c344 block=evidence -->
- Closing an issue is an explicit API mutation carrying a reason, message, typed evidence, and actor attribution; kata never infers closure from git history. [@claim:clm_0069618a1905deb33c4a79b04f7b94e692c96adbd183f122581c028cddf9779a]
- Every state change appends to an immutable event log with the actor recorded; actors are free-form snapshots on events, not foreign keys, and there is no global user registry. [@claim:clm_1d761045d120ea8923262dbdeef993672c801706f18f46f8bb703e82304d9a4b]
- The CLI offers agent-oriented ergonomics: stable short refs, --json and --agent output, idempotent creates, semantic-aware search, a claim flow, and predictable failure modes. [@claim:clm_22c69789f13d00e4cc72b49dc5ad28928c01efea182316a37a049d6e99ab22d5]
- All reads and writes go through kata's HTTP API; no client opens SQLite or Postgres directly, and a Go app can mount the listener-free service in-process. [@claim:clm_2a93491b1c047b51d85a89b0e727b42c6a4d70169445e82ef1e16ead53e4c486]
- Workspace identity derives from the normalized git remote URL rather than the filesystem path, so clones resolve to the same project; one git repository attaches to exactly one project. [@claim:clm_3d3002806729950234aaffc9759ad092cfbd88ac69489d08cef8df52280d327b]
- The surface is deliberately small: three relationship types, labels, owners, comments, and a constrained integer priority 0-4; there is no in_progress status, severity field, threaded replies, reactions, attachments, or markdown rendering. [@claim:clm_3e3425fb2166eb68f9fdb901185b35e92b3106eab6b25f1057027a73901f37c1]
- kata uses pure-Go SQLite via modernc.org/sqlite with no CGO, a Huma-based HTTP API over a Unix socket, and claims no runtime dependencies beyond the single binary. [@claim:clm_4e78ed48a486b339474f3c80394ef7cb852392df2973ed88bd44f00e912a91e4]
- Permanent non-goals include workspace-local behavior overrides, per-issue SSE subscriptions, bulk mutation endpoints, remote webhooks, and a (kata-#N) commit-message convention. [@claim:clm_6535b61aee64a46d6b5d041021467c3238e8df80651fc688e233d709c10108e2]
- The product ships as one Go binary with a CLI, a long-lived daemon, a TUI, and a browser UI served by the daemon with no separate backend. [@claim:clm_7558ec539179c9b0b5fb17d46dba15625093c92aca35bbcbfbbfb1866c250621]
- The loopback HTTP server rejects non-empty Origin headers, requires application/json Content-Type on mutations, and emits no CORS headers to resist drive-by browser requests. [@claim:clm_89e6452e8b4e8fd72736a2a91c39c87bf02b8a3ac5d94656580e0409a83deccc]
- Local mode trusts the OS user with no authentication on a Unix socket or loopback listener; shared/remote modes require a bearer token and explicit trust opt-in before credentials cross a plaintext non-loopback connection. [@claim:clm_8c52c55eccbd5b2c6970defb70c71ad8b502d7ea2e24c19825928526eb60a8e3]
- Hooks run local commands after database commit on a bounded worker pool, invoked without a shell via exec.Command with event data as JSON on stdin; hooks are not a sandbox and run with the daemon's OS user. [@claim:clm_970a78ae79337d59265c6517bb5db2f6b618efc17772bf26735c3df95c7e145b]
- Projects are bound to workspaces explicitly via a committed .kata.toml, never inferred from the current directory; outside a bound workspace every command except kata init fails with project_not_initialized. [@claim:clm_9a667136be04ff445a4314681169935c2946185001a53320c731d2f92174a6d3]
<!-- rcw:end owner=source:src_f8e530c979eb5711b2ebbde75659c344 block=evidence -->

## Researcher notes

