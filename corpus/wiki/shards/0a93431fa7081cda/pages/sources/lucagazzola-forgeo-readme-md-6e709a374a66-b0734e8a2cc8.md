---
access: public
aliases: []
claim_ids:
- clm_033db32ad36c6264814c50f9fbd2b4c45cc2c89f0b92d9a7cf898db5bb4ee497
- clm_05a85f0e27f653315e7806b989bdfaced92fc2efab2ed2f7c78e6c6fdb6093bb
- clm_2befd9e1af1a0fbed374262864d41fbd66b8f4f415c96a2a4bea2f547bc336f4
- clm_45865eca87b7c24ad6b3cc32463f495ffb164e7a68286a6d013da838481257a5
- clm_4c4fb2e9da456b43d8ae4916c3f92400c07fdf7f2979e1c4a543b41f743e8a29
- clm_502eb40bb2bfa12d35a0c2bbb8886fb3c50303cdab94f239c9b2271ea829dbef
- clm_594d2b0a06fb928745b63a6ab93dd90e231f50b1395cd9b99e74f52bd2a50d5a
- clm_87f5d225a4b747829d7c08e2d54ccc6932fcb867e8463f7afb3e43076b2cd91d
- clm_d3ab0ad618a850d3121b80de9a49700266442b0db7cb0a8a8abf0bea23f9c2fb
- clm_eba71376f94ccc43fdcd8122179470d2c36a8d98dcb3d0f5e06f1aef70882334
maturity: draft
page_id: pg_45652618d8b059c3b7ecb0734e8a2cc8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_155a1730fae459c39b9c865d4621123a
title: lucaGazzola/forgeo/README.md @ 6e709a374a66
updated_at: '2026-09-14T02:15:16Z'
---

# lucaGazzola/forgeo/README.md @ 6e709a374a66

<!-- rcw:begin owner=source:src_155a1730fae459c39b9c865d4621123a block=evidence -->
- Optional review_mode: branch commits successful agent work to a forgeo/review/<TASK_ID> branch, marks the task REVIEW, and waits for a human merge/Complete or Request-changes action instead of committing directly to main. [@claim:clm_033db32ad36c6264814c50f9fbd2b4c45cc2c89f0b92d9a7cf898db5bb4ee497]
- Task selection picks the oldest OPEN task whose dependencies are all COMPLETED (or whose run_at schedule is due); REVIEW blocks dependants while independent tasks keep running. [@claim:clm_05a85f0e27f653315e7806b989bdfaced92fc2efab2ed2f7c78e6c6fdb6093bb]
- The dashboard supports optional bearer-token auth via forgeo web --token (or a token in ~/.config/forgeo/web.toml), returning 401 on /api/* routes without it; without a flag or token file it stays open by default. [@claim:clm_2befd9e1af1a0fbed374262864d41fbd66b8f4f415c96a2a4bea2f547bc336f4]
- Forgeo persists runtime state in .forgeo/ (backlog, logs, blockers) plus runs.jsonl run history, daemon.state.json, and rotating backlog.json.bak snapshots restored when the backlog is found corrupt. [@claim:clm_45865eca87b7c24ad6b3cc32463f495ffb164e7a68286a6d013da838481257a5]
- An optional Docker sandbox runs the agent isolated, with a configurable image, network (default none), read-only mounts, and the repo bind-mounted at the same path. [@claim:clm_4c4fb2e9da456b43d8ae4916c3f92400c07fdf7f2979e1c4a543b41f743e8a29]
- Backlog providers are file, HTTP, GitHub, GitLab, and Jira; file/HTTP exchange the full document while Jira/GitHub/GitLab sync issues individually, with engine state stored in a hidden forgeo block or issue properties. [@claim:clm_502eb40bb2bfa12d35a0c2bbb8886fb3c50303cdab94f239c9b2271ea829dbef]
- Forgeo is described as a software factory for a coding agent: given a backlog and an agent CLI, it picks the next runnable task, runs the agent, commits the result, and tracks progress in plain files plus a web dashboard. [@claim:clm_594d2b0a06fb928745b63a6ab93dd90e231f50b1395cd9b99e74f52bd2a50d5a]
- CLI surface includes forgeo init, validate, start, once, run --task, status, stop, restart, instance add/list, and web, with the daemon running one cycle per interval_minutes. [@claim:clm_87f5d225a4b747829d7c08e2d54ccc6932fcb867e8463f7afb3e43076b2cd91d]
- The central dashboard (forgeo web) defaults to 0.0.0.0:8790, aggregates all registered instances, and exposes a per-instance HTTP API under /api/instances/<name>/ including task create/edit/delete, reopen, config PUT, and daemon start/stop/restart endpoints. [@claim:clm_d3ab0ad618a850d3121b80de9a49700266442b0db7cb0a8a8abf0bea23f9c2fb]
- The agent contract is agent-agnostic: any CLI that reads the FORGEO_TASK environment variable can be used, and the backlog task's acceptance criteria are rendered into that instruction. [@claim:clm_eba71376f94ccc43fdcd8122179470d2c36a8d98dcb3d0f5e06f1aef70882334]
<!-- rcw:end owner=source:src_155a1730fae459c39b9c865d4621123a block=evidence -->

## Researcher notes

