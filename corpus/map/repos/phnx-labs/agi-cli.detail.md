# phnx-labs/agi-cli -- full detail

[Back to orientation](agi-cli.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/phnx-labs/agi-cli/148a9795a4cdd431a920e28f0f183b66bea56323/ac41ecdac71c4c24.json](../../../wiki/dossiers/phnx-labs/agi-cli/148a9795a4cdd431a920e28f0f183b66bea56323/ac41ecdac71c4c24.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] `agents insights perf` reads a disposable SQLite warehouse at ~/.agents/.cache/perf/perf.db containing hook, command, and run timing rollups, which is deletable at any time. -- evidence: [README.md#L141-L141](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L141-L141) (`clm_2277423d17abfcd40e73d697f5790786e8ae5f4f8ae11f9fbeecad002c266c2d`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI is installed as @phnx-labs/agents-cli via npm (or bun, or a curl one-liner) and every command works under both the `agents` and `ag` aliases. -- evidence: [README.md#L81-L81](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L81-L81), [README.md#L49-L54](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L49-L54), [README.md#L56-L56](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L56-L56) (`clm_fefc74ec51495c7c19803e4618b5ade4c8752b530f08a2ad356842769127ae15`)
- [observation/documented] `agents run <harness> "task"` dispatches work to harnesses such as claude, codex, and antigravity, with modes (plan/edit/auto/skip), JSON output, timeouts, and Unix-pipeline chaining of agents. -- evidence: [README.md#L177-L181](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L177-L181), [README.md#L235-L238](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L235-L238), [README.md#L240-L240](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L240-L240) (`clm_e8f39358ed2621db76a6c499a2ab855120caa08e6f3d366f92c29f1e7a00e609`)
- [observation/documented] With `--acp`, runs route through the Agent Client Protocol to emit a typed event stream (agent_message_chunk, tool_call, plan_update, stop_reason) instead of raw stdout; ACP adapters are documented for claude, codex, cursor, opencode, openclaw, and grok. -- evidence: [README.md#L290-L290](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L290-L290), [README.md#L285-L286](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L285-L286), [README.md#L288-L288](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L288-L288) (`clm_a6966c28799b1a0bc1df7098808278d7c4916b61f7dc321ba187434690bc8642`)

## memory-state (2 claim(s))

- [observation/documented] Session search is backed by a SQLite + FTS5 index at ~/.agents/.history/sessions/sessions.db with incremental scanning; tool queries read SQLite only, with no embeddings, vector database, or model calls. -- evidence: [README.md#L359-L359](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L359-L359) (`clm_9b5b78e79aff9ea25a37ee323cc7931c149e6c4eccc044b6e01b5a51f14e5d87`)
- [observation/documented] Live sessions resolve to states such as working, waiting_input, idle, orphaned, crashed, closed, abandoned, queued, or unknown, with matching filter flags that imply --active; orphan/crashed detection reads tmux attached-client counts and editor registry heartbeats. -- evidence: [README.md#L395-L395](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L395-L395), [README.md#L403-L403](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L403-L403) (`clm_06d45a14fed620bd53d45cae89b944e2e1cdc1f39454601f4b0b650b62e04084`)

## orchestration (3 claim(s))

- [observation/documented] `agents run` supports a rate-limit fallback chain (--fallback codex,antigravity) and account-selection strategies such as --strategy balanced that spread work across accounts and exclude session-limited accounts until their stated reset time. -- evidence: [README.md#L203-L203](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L203-L203), [README.md#L216-L216](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L216-L216), [README.md#L196-L197](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L196-L197) (`clm_6dc73b37960686f3cac7653b1d72a3d010894506e82acdcfde7a642b5371e502`)
- [observation/documented] `agents run auto` picks across device, harness, and account layers, excluding harnesses whose accounts are all rate-limited or signed out, and exits nonzero naming the earliest reset when nothing is healthy. -- evidence: [README.md#L227-L227](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L227-L227), [README.md#L223-L225](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L223-L225) (`clm_8c1b762845dcc0815d082e9e8dc7ef2adef776b465ec937c12fa331fb27ac701`)
- [observation/documented] `agents watchdog` detects stalled sessions, resolves the exact terminal split (tmux, iTerm, VSCodium, or raw pty), and injects a nudge; it is dry-run by default, with a device-local daemon pass every three minutes and in-place account rotation on hard limits. -- evidence: [README.md#L543-L543](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L543-L543), [README.md#L534-L539](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L534-L539), [README.md#L541-L541](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L541-L541) (`clm_c0edd4472903aa72c670e24edf0e783f0f29465e976bc4851647d378b57370af`)

## tools-permissions (2 claim(s))

- [observation/documented] In direct-exec runs, `--mode skip` forwards each harness's native bypass flag (e.g. --dangerously-skip-permissions for Claude Code, --yolo for Gemini); under `--acp`, skip is granted at the ACP protocol layer by selecting allow_always or the first offered permission option. -- evidence: [README.md#L244-L250](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L244-L250), [README.md#L265-L268](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L265-L268), [README.md#L252-L263](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L252-L263) (`clm_a421735020fdb4ff2089c3396bab41eac97494f091ad0232a197eb4dc3a2bf6d`)
- [observation/documented] Codex runs use managed permission profiles: edit and auto share a sandbox with writable workspace, ~/.agents, and caches plus network access, differing only in approvals; explicit plan mode keeps the filesystem read-only, and skip removes the sandbox entirely. -- evidence: [README.md#L270-L279](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L270-L279) (`clm_c00d2a3ea46b0eb46bcc6973501f4451abc115b46d4547fc330361f92a935c1f`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Setup clones the phnx-labs/.agents-system system repo into ~/.agents/.system, fast-forwarding from its verified canonical origin on `agents use`; AGENTS_SYSTEM_REPO can point to a user fork and --no-system-repo skips the clone. -- evidence: [README.md#L61-L73](https://github.com/phnx-labs/agi-cli/blob/148a9795a4cdd431a920e28f0f183b66bea56323/README.md#L61-L73) (`clm_262aa291f15cf8ddb3e49e8d7215f6e7eba6cac128dcc65d3e37178fc6ca0f7c`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

