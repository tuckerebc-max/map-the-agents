# wienerdog-ai/wienerdog -- full detail

[Back to orientation](wienerdog.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/wienerdog-ai/wienerdog/91668da62822c73be6115a3e6d06c6ec51462509/10c545f38401b46b.json](../../../wiki/dossiers/wienerdog-ai/wienerdog/91668da62822c73be6115a3e6d06c6ec51462509/10c545f38401b46b.json)

## specifications (1 claim(s))

- [observation/documented] The architecture describes the product as a compiler plus prompts, not an application: a thin CLI, short-lived hook scripts, and scheduled jobs whose brain is claude -p or codex exec, targeting under ~4k LOC of plain Node 18+ with no build step. -- evidence: [docs/ARCHITECTURE.md#L5-L5](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L5-L5) (`clm_feed64bc9c0751c31cc18715057ab3dda50d967c176a0cf4e0f4aa767835c7b9`)

## components (1 claim(s))

- [observation/documented] The system map shows a canonical core at ~/.wienerdog/ (config.yaml, skills, prompts, bin, state, secrets, logs, install manifest) plus Claude and Codex adapters that sync compiles into ~/.claude/ and ~/.codex/. -- evidence: [docs/ARCHITECTURE.md#L9-L56](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L9-L56) (`clm_5084cbc38fbf325c2c253449fe2129491a83eb5d8564e4e063c78cd081dd5538`)

## design-choices (1 claim(s))

- [observation/documented] Wienerdog never owns the user's CLAUDE.md/AGENTS.md; it manages only a sentinel-delimited block, sync overwrites edits inside sentinels while leaving outside edits untouched, and uninstall removes exactly that region. -- evidence: [docs/ARCHITECTURE.md#L92-L92](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L92-L92) (`clm_63cca3a57de5d309700d1ff247d0d31033b7b0badf369524eff9c42c4d45ef5f`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the repo dogfoods its own product — its memory vault lives in memory/, its development conventions are its own CLAUDE.md, and most code is written by mid-tier AI models following its spec system in docs/specs/. -- evidence: [README.md#L86-L86](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/README.md#L86-L86) (`clm_588a8d3d19f7c73c174d2be20e1be32aa845e54e212ff82119ecb5e6f49b7f02`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] The wienerdog CLI exposes subcommands install, sync, doctor, dream, schedule, run-job, gws, and uninstall per the architecture system map. -- evidence: [docs/ARCHITECTURE.md#L9-L56](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L9-L56) (`clm_c4c09b1a3ea3f3c43ac6f9ce5dfc344b2e408628a25ec582ec23212e7c03168c`)

## memory-state (2 claim(s))

- [observation/documented] The memory vault defaults to ~/wienerdog/ with PARA-style folders (00-Inbox through 07-Daily, reports, .git); machine state such as watermarks, queue, and score cache lives in ~/.wienerdog/state/, never in the vault. -- evidence: [docs/ARCHITECTURE.md#L102-L115](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L102-L115), [docs/ARCHITECTURE.md#L154-L154](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L154-L154) (`clm_c614187fabbc61e893fa280980afd917e6d3a1ee9a3dbc42e0762f77a27e7378`)
- [observation/documented] Vault notes carry mandatory frontmatter provenance fields on every auto-write, including id, type, origin, source_sessions, confidence, recurrence, and a derived_from_untrusted flag. -- evidence: [docs/ARCHITECTURE.md#L117-L117](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L117-L117), [docs/ARCHITECTURE.md#L119-L133](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L119-L133) (`clm_3b3c9776c318f3a63ad61fc96b1fb72d05df66813fa51ecd26475d0fd6c13ed3`)

## orchestration (2 claim(s))

- [observation/documented] The dream job (default 03:30 local via run-job dream) scans harness transcripts since per-harness watermarks, redacts secret-looking strings, then runs a dream skill headlessly with tool restrictions: read scratch and vault, write vault only, no Bash, no network. -- evidence: [docs/ARCHITECTURE.md#L141-L141](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L141-L141), [docs/ARCHITECTURE.md#L143-L152](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L143-L152), [docs/ARCHITECTURE.md#L139-L139](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L139-L139) (`clm_08a95bc13672465450e1af9dc2e2077ece053a298f2d0fee5c4d0bce14218a94`)
- [observation/documented] Scheduled jobs use OS-native schedulers (launchd, systemd user timers, Task Scheduler) invoking short-lived run-job processes with watchdog timeout, rotated logging, catch-up, and fail-loud alerting; the design explicitly uses no daemon. -- evidence: [docs/ARCHITECTURE.md#L168-L170](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L168-L170), [docs/ARCHITECTURE.md#L166-L166](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L166-L166), [docs/ARCHITECTURE.md#L172-L172](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L172-L172) (`clm_6322c2e1d5d04d702f592aece3185e18c01908b2aaaff66f52f3b9d7ecb1e9a4`)

## tools-permissions (2 claim(s))

- [observation/documented] Outbound gws verbs such as gmail send execute only under a send grant: scoped routine-and-recipient-allowlist entries in config.yaml created only via an interactive typed-confirmation flow; ungranted sends degrade to a draft plus a notice. -- evidence: [docs/ARCHITECTURE.md#L160-L160](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L160-L160) (`clm_c4663723fad34d1e0516557f27bb418697a7b97c024ec4a171dd13b92637cbc3`)
- [observation/documented] Memory promotion uses tiered quality gates: daily logs need score >= 0.5, atomic notes >= 0.75, and Tier 3 (identity, preferences, skills, digest-fed content) requires score >= 0.85, recurrence across 3+ distinct sessions, and derived_from_untrusted false. -- evidence: [docs/ARCHITECTURE.md#L143-L152](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L143-L152) (`clm_688e4420a3e8bdb088dae1abc6c337a7b52584abfc71f3ef5fe3b4b9821638d4`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The architecture targets zero runtime dependencies except googleapis; the gws module is a thin ~600-LOC CLI over googleapis, with MCP, GAM, gcalcli, gmailctl, and the official Rust gws CLI evaluated and rejected for v1. -- evidence: [docs/ARCHITECTURE.md#L158-L158](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L158-L158), [docs/ARCHITECTURE.md#L5-L5](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/docs/ARCHITECTURE.md#L5-L5) (`clm_24633907624715683fc04b6f82804512c790651f2cd5ffc5fd1ed56ad889640a`)

## limitations (2 claim(s))

- [observation/documented] The project is at 0.x status; the README states installed file formats may still evolve until 1.0, treating the installed file layout as the public API. -- evidence: [README.md#L63-L63](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/README.md#L63-L63) (`clm_0c46e2b29c9d4fe95469be3f967596be579e388660cb637aaf431664b7d4dbc5`)
- [observation/documented] FIX-PLAN documents verified defects in the current code: the daily summary is injected as trusted-by-default context (a planned fix will fence it as untrusted data), and identity digest hashing has a TOCTOU window where injected content is read a second time after hashing. -- evidence: [FIX-PLAN.md#L110-L124](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/FIX-PLAN.md#L110-L124), [FIX-PLAN.md#L253-L262](https://github.com/wienerdog-ai/wienerdog/blob/91668da62822c73be6115a3e6d06c6ec51462509/FIX-PLAN.md#L253-L262) (`clm_725060de48e9af8ad2b6594f8776347459163e2ceb1364949ec3ce94658a9122`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

