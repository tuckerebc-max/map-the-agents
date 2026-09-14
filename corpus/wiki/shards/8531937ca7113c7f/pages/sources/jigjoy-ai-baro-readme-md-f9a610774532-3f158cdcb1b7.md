---
access: public
aliases: []
claim_ids:
- clm_105014d924b25e519cecc21d417b0d2de15a7cdb764de15ab0c6e84752a8697f
- clm_1a78f2e24d029f64423c450abc8fb39f316d40b40233281a4d59ed951fb7e376
- clm_31d494bd46599975f396e273b9c161237a5e8067e2bb73f2ce4cd14613a801eb
- clm_766911624b7300063f436a3c324000b42f9c0aee1fb1362034b1a4ca01d22eb9
- clm_92d2d411d0709701e7fd56b0da87655c88254493c97f754d78e2ff67f56fa2c1
- clm_a3e7704c988709fe7a6c2df6530d7718a051a5dbe007aee06cf28061a80d8ca2
- clm_ac7cfaff3f1e8029288f36cb28451ce63f696ff44703e632c0749bbe48f91958
- clm_cf08c9b4122ad876d30561aec0b4db4e355bcdc6c8d41d32d4170ff510a8fd1e
- clm_e6110d9ddb9d49432414558bbe8d4a4dc45ee554c44e9406e2bd440c0298a359
maturity: draft
page_id: pg_087b3b9de0665fb4ad0e3f158cdcb1b7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ddc01746f1165a62b36cb7b76b0fa1cc
title: jigjoy-ai/baro/README.md @ f9a610774532
updated_at: '2026-09-14T02:06:52Z'
---

# jigjoy-ai/baro/README.md @ f9a610774532

<!-- rcw:begin owner=source:src_ddc01746f1165a62b36cb7b76b0fa1cc block=evidence -->
- `--local-only` disables pushes and PRs but is explicitly not an OS or network sandbox, since story agents can execute arbitrary shell commands; a hard no-push boundary requires removing git remotes. [@claim:clm_105014d924b25e519cecc21d417b0d2de15a7cdb764de15ab0c6e84752a8697f]
- Merges are blocked behind fail-closed gates: declared tests, build-before-commit, an evidence critic judging captured command output, and write-surface ownership; the human reviews a PR the gates already accepted. [@claim:clm_1a78f2e24d029f64423c450abc8fb39f316d40b40233281a4d59ed951fb7e376]
- A cloud option runs the same fleet on a hosted site with isolated sandboxes and provider keys, or users can attach their own machine as a cloud runner via `baro login` and `baro connect --install-service`. [@claim:clm_31d494bd46599975f396e273b9c161237a5e8067e2bb73f2ce4cd14613a801eb]
- The tool requires Node 20+, git, and at least one LLM backend: the claude CLI (default), codex, or any OpenAI-compatible endpoint; `baro --doctor` checks the setup. [@claim:clm_766911624b7300063f436a3c324000b42f9c0aee1fb1362034b1a4ca01d22eb9]
- Flags include backend selection (--llm claude|codex|openai|opencode|pi|hybrid|jigjoy), model override, effort level, parallel agent count, execution mode, --quick, --local-only, per-command shell budget, custom OpenAI base URL, and per-tier backend mapping. [@claim:clm_92d2d411d0709701e7fd56b0da87655c88254493c97f754d78e2ff67f56fa2c1]
- CLI commands include headless detached runs printing a run id, `watch` and `logs` for following runs, `runs`/`stop` for listing and stopping, `--resume` (never re-plans), `--continue` (always re-plans), `--doctor`, `login`, and `connect`. [@claim:clm_a3e7704c988709fe7a6c2df6530d7718a051a5dbe007aee06cf28061a80d8ca2]
- The architecture is described as a Rust TUI host plus a TypeScript orchestrator whose bounded contexts communicate over the Mozaik event bus, with machine gates in front of every merge. [@claim:clm_ac7cfaff3f1e8029288f36cb28451ce63f696ff44703e632c0749bbe48f91958]
- Goals are compiled by an architect into machine-checkable invariants before coding, split into a DAG of stories built in parallel across isolated git worktrees, with runtime replanning able to add and rewire stories mid-run and failed gates spawning remediation stories. [@claim:clm_cf08c9b4122ad876d30561aec0b4db4e355bcdc6c8d41d32d4170ff510a8fd1e]
- The product is installed globally via npm as baro-ai and is invoked as `baro "<goal>"` inside a repository, opening a TUI where intake asks questions, the user confirms the plan, and the run proceeds. [@claim:clm_e6110d9ddb9d49432414558bbe8d4a4dc45ee554c44e9406e2bd440c0298a359]
<!-- rcw:end owner=source:src_ddc01746f1165a62b36cb7b76b0fa1cc block=evidence -->

## Researcher notes

