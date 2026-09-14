---
access: public
aliases: []
claim_ids:
- clm_23f50ed15deba6890b12b61e5c6ada497f2c7092d25be5e1a92792e6ba3c9f24
- clm_2b112b20ca0981723b10b5e603b3ded72a761fb8a66a7ff7576eb138982298f2
- clm_416af15c0b2a2c51afa8d50b00b8778c507d445b52fbd1482db9c3731221e14d
- clm_58f56cbaf277905d8b57b4f1c3216f279d024bfbe49cd69b86cbf58cc31fbe9a
- clm_592fb050a727d5071ae34f4e91f9412fc86a82b9c36e922f7b65adde2bec7f08
- clm_5f7998296dd7ec0f51b6b8768262f8c605089f5147cd30e0a719b0b14977caa4
- clm_ad7233bfa6f3332b5da88037ba9092c6a82acb797e9c3b368b6243a44b54e59e
- clm_c922d34785fb9357893436180f3de376ba410ea063c6ed000ac3dc7209228fe0
- clm_e81dad8ddfe30c4d4bae66a54eba4bb095557541d088f16abeced467728bf904
- clm_f9b5aeedf37e09bd917a10126b8bd6f3e7957bb87879dbb0bce5df4b70c19466
maturity: draft
page_id: pg_7d541bdda14351f395bf00971e2c807a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6cb767a6725956c1835cb224b4aa575c
title: andyrewlee/amux/README.md @ f94362f6c25f
updated_at: '2026-09-14T01:33:26Z'
---

# andyrewlee/amux/README.md @ f94362f6c25f

<!-- rcw:begin owner=source:src_6cb767a6725956c1835cb224b4aa575c block=evidence -->
- Project-supplied workspace scripts are gated: amux records an approval of .amux/workspaces.json content before running it, and edits invalidate the approval until re-trusted; user-entered scripts are never gated. [@claim:clm_23f50ed15deba6890b12b61e5c6ada497f2c7092d25be5e1a92792e6ba3c9f24]
- Agent definitions are configured per-user in ~/.amux/config.json, where users can add assistants or override built-ins; workspace metadata and trusted-script approvals live under ~/.amux. [@claim:clm_2b112b20ca0981723b10b5e603b3ded72a761fb8a66a7ff7576eb138982298f2]
- Both write actions (commit and merge) are available from the UI and each is placed behind an explicit confirmation. [@claim:clm_416af15c0b2a2c51afa8d50b00b8778c507d445b52fbd1482db9c3731221e14d]
- Workspaces are configured via a project-level .amux/workspaces.json defining setup-workspace, run, and archive commands, with environment variables like AMUX_WORKSPACE_NAME and AMUX_PORT exposed to those scripts. [@claim:clm_58f56cbaf277905d8b57b4f1c3216f279d024bfbe49cd69b86cbf58cc31fbe9a]
- amux is a terminal UI (Bubble Tea v2) for running multiple coding agents in parallel, using a workspace-first model that can import git worktrees. [@claim:clm_592fb050a727d5071ae34f4e91f9412fc86a82b9c36e922f7b65adde2bec7f08]
- amux requires tmux (minimum 3.2); each agent runs in its own tmux session for terminal isolation and persistence, and the tool is supported on Linux/macOS only. [@claim:clm_5f7998296dd7ec0f51b6b8768262f8c605089f5147cd30e0a719b0b14977caa4]
- amux runs git with repository hooks and core.fsmonitor disabled so a checked-out repo cannot execute code merely because amux touched it; AMUX_ALLOW_GIT_HOOKS=1 re-enables hooks, while git-lfs filters are never disabled. [@claim:clm_ad7233bfa6f3332b5da88037ba9092c6a82acb797e9c3b368b6243a44b54e59e]
- Repository development practice: contributors run ./scripts/install-hooks.sh to enable pre-commit fmt/lint checks and a pre-push lint-parity gate, and build the pinned golangci-lint via make lint-tools before make devcheck. [@claim:clm_c922d34785fb9357893436180f3de376ba410ea063c6ed000ac3dc7209228fe0]
- Windows is not supported; the tool requires tmux and targets Linux/macOS. [@claim:clm_e81dad8ddfe30c4d4bae66a54eba4bb095557541d088f16abeced467728bf904]
- Commit (key 'c') stages and commits on the workspace's own branch without pushing; merge (key 'M') uses git merge --no-ff in the primary checkout, refusing if the base branch is not checked out there, and lists conflicted files on conflict. [@claim:clm_f9b5aeedf37e09bd917a10126b8bd6f3e7957bb87879dbb0bce5df4b70c19466]
<!-- rcw:end owner=source:src_6cb767a6725956c1835cb224b4aa575c block=evidence -->

## Researcher notes

