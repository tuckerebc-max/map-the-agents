---
access: public
aliases: []
claim_ids:
- clm_06d45a14fed620bd53d45cae89b944e2e1cdc1f39454601f4b0b650b62e04084
- clm_2277423d17abfcd40e73d697f5790786e8ae5f4f8ae11f9fbeecad002c266c2d
- clm_262aa291f15cf8ddb3e49e8d7215f6e7eba6cac128dcc65d3e37178fc6ca0f7c
- clm_6dc73b37960686f3cac7653b1d72a3d010894506e82acdcfde7a642b5371e502
- clm_8c1b762845dcc0815d082e9e8dc7ef2adef776b465ec937c12fa331fb27ac701
- clm_9b5b78e79aff9ea25a37ee323cc7931c149e6c4eccc044b6e01b5a51f14e5d87
- clm_a421735020fdb4ff2089c3396bab41eac97494f091ad0232a197eb4dc3a2bf6d
- clm_a6966c28799b1a0bc1df7098808278d7c4916b61f7dc321ba187434690bc8642
- clm_c00d2a3ea46b0eb46bcc6973501f4451abc115b46d4547fc330361f92a935c1f
- clm_c0edd4472903aa72c670e24edf0e783f0f29465e976bc4851647d378b57370af
- clm_e8f39358ed2621db76a6c499a2ab855120caa08e6f3d366f92c29f1e7a00e609
- clm_fefc74ec51495c7c19803e4618b5ade4c8752b530f08a2ad356842769127ae15
maturity: draft
page_id: pg_f98602870aee53589c9a689cbb382b1e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e87cc4e1fbe65a77931ceb13adb020ef
title: phnx-labs/agi-cli/README.md @ 148a9795a4cd
updated_at: '2026-09-14T04:16:10Z'
---

# phnx-labs/agi-cli/README.md @ 148a9795a4cd

<!-- rcw:begin owner=source:src_e87cc4e1fbe65a77931ceb13adb020ef block=evidence -->
- Live sessions resolve to states such as working, waiting_input, idle, orphaned, crashed, closed, abandoned, queued, or unknown, with matching filter flags that imply --active; orphan/crashed detection reads tmux attached-client counts and editor registry heartbeats. [@claim:clm_06d45a14fed620bd53d45cae89b944e2e1cdc1f39454601f4b0b650b62e04084]
- `agents insights perf` reads a disposable SQLite warehouse at ~/.agents/.cache/perf/perf.db containing hook, command, and run timing rollups, which is deletable at any time. [@claim:clm_2277423d17abfcd40e73d697f5790786e8ae5f4f8ae11f9fbeecad002c266c2d]
- Setup clones the phnx-labs/.agents-system system repo into ~/.agents/.system, fast-forwarding from its verified canonical origin on `agents use`; AGENTS_SYSTEM_REPO can point to a user fork and --no-system-repo skips the clone. [@claim:clm_262aa291f15cf8ddb3e49e8d7215f6e7eba6cac128dcc65d3e37178fc6ca0f7c]
- `agents run` supports a rate-limit fallback chain (--fallback codex,antigravity) and account-selection strategies such as --strategy balanced that spread work across accounts and exclude session-limited accounts until their stated reset time. [@claim:clm_6dc73b37960686f3cac7653b1d72a3d010894506e82acdcfde7a642b5371e502]
- `agents run auto` picks across device, harness, and account layers, excluding harnesses whose accounts are all rate-limited or signed out, and exits nonzero naming the earliest reset when nothing is healthy. [@claim:clm_8c1b762845dcc0815d082e9e8dc7ef2adef776b465ec937c12fa331fb27ac701]
- Session search is backed by a SQLite + FTS5 index at ~/.agents/.history/sessions/sessions.db with incremental scanning; tool queries read SQLite only, with no embeddings, vector database, or model calls. [@claim:clm_9b5b78e79aff9ea25a37ee323cc7931c149e6c4eccc044b6e01b5a51f14e5d87]
- In direct-exec runs, `--mode skip` forwards each harness's native bypass flag (e.g. --dangerously-skip-permissions for Claude Code, --yolo for Gemini); under `--acp`, skip is granted at the ACP protocol layer by selecting allow_always or the first offered permission option. [@claim:clm_a421735020fdb4ff2089c3396bab41eac97494f091ad0232a197eb4dc3a2bf6d]
- With `--acp`, runs route through the Agent Client Protocol to emit a typed event stream (agent_message_chunk, tool_call, plan_update, stop_reason) instead of raw stdout; ACP adapters are documented for claude, codex, cursor, opencode, openclaw, and grok. [@claim:clm_a6966c28799b1a0bc1df7098808278d7c4916b61f7dc321ba187434690bc8642]
- Codex runs use managed permission profiles: edit and auto share a sandbox with writable workspace, ~/.agents, and caches plus network access, differing only in approvals; explicit plan mode keeps the filesystem read-only, and skip removes the sandbox entirely. [@claim:clm_c00d2a3ea46b0eb46bcc6973501f4451abc115b46d4547fc330361f92a935c1f]
- `agents watchdog` detects stalled sessions, resolves the exact terminal split (tmux, iTerm, VSCodium, or raw pty), and injects a nudge; it is dry-run by default, with a device-local daemon pass every three minutes and in-place account rotation on hard limits. [@claim:clm_c0edd4472903aa72c670e24edf0e783f0f29465e976bc4851647d378b57370af]
- `agents run <harness> "task"` dispatches work to harnesses such as claude, codex, and antigravity, with modes (plan/edit/auto/skip), JSON output, timeouts, and Unix-pipeline chaining of agents. [@claim:clm_e8f39358ed2621db76a6c499a2ab855120caa08e6f3d366f92c29f1e7a00e609]
- The CLI is installed as @phnx-labs/agents-cli via npm (or bun, or a curl one-liner) and every command works under both the `agents` and `ag` aliases. [@claim:clm_fefc74ec51495c7c19803e4618b5ade4c8752b530f08a2ad356842769127ae15]
<!-- rcw:end owner=source:src_e87cc4e1fbe65a77931ceb13adb020ef block=evidence -->

## Researcher notes

