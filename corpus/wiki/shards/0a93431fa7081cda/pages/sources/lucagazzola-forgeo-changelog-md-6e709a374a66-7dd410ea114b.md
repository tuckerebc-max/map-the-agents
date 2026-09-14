---
access: public
aliases: []
claim_ids:
- clm_033db32ad36c6264814c50f9fbd2b4c45cc2c89f0b92d9a7cf898db5bb4ee497
- clm_05a85f0e27f653315e7806b989bdfaced92fc2efab2ed2f7c78e6c6fdb6093bb
- clm_2befd9e1af1a0fbed374262864d41fbd66b8f4f415c96a2a4bea2f547bc336f4
- clm_45865eca87b7c24ad6b3cc32463f495ffb164e7a68286a6d013da838481257a5
- clm_502eb40bb2bfa12d35a0c2bbb8886fb3c50303cdab94f239c9b2271ea829dbef
- clm_7dbff1382a95bee2b761e38d4b87fc5af4618dcdd69efb81870625934e13d092
- clm_d3ab0ad618a850d3121b80de9a49700266442b0db7cb0a8a8abf0bea23f9c2fb
maturity: draft
page_id: pg_f7728cdc6b395e22b3927dd410ea114b
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ac1bd9db6607570886182b4a80dfa269
title: lucaGazzola/forgeo/CHANGELOG.md @ 6e709a374a66
updated_at: '2026-09-14T02:15:16Z'
---

# lucaGazzola/forgeo/CHANGELOG.md @ 6e709a374a66

<!-- rcw:begin owner=source:src_ac1bd9db6607570886182b4a80dfa269 block=evidence -->
- Optional review_mode: branch commits successful agent work to a forgeo/review/<TASK_ID> branch, marks the task REVIEW, and waits for a human merge/Complete or Request-changes action instead of committing directly to main. [@claim:clm_033db32ad36c6264814c50f9fbd2b4c45cc2c89f0b92d9a7cf898db5bb4ee497]
- Task selection picks the oldest OPEN task whose dependencies are all COMPLETED (or whose run_at schedule is due); REVIEW blocks dependants while independent tasks keep running. [@claim:clm_05a85f0e27f653315e7806b989bdfaced92fc2efab2ed2f7c78e6c6fdb6093bb]
- The dashboard supports optional bearer-token auth via forgeo web --token (or a token in ~/.config/forgeo/web.toml), returning 401 on /api/* routes without it; without a flag or token file it stays open by default. [@claim:clm_2befd9e1af1a0fbed374262864d41fbd66b8f4f415c96a2a4bea2f547bc336f4]
- Forgeo persists runtime state in .forgeo/ (backlog, logs, blockers) plus runs.jsonl run history, daemon.state.json, and rotating backlog.json.bak snapshots restored when the backlog is found corrupt. [@claim:clm_45865eca87b7c24ad6b3cc32463f495ffb164e7a68286a6d013da838481257a5]
- Backlog providers are file, HTTP, GitHub, GitLab, and Jira; file/HTTP exchange the full document while Jira/GitHub/GitLab sync issues individually, with engine state stored in a hidden forgeo block or issue properties. [@claim:clm_502eb40bb2bfa12d35a0c2bbb8886fb3c50303cdab94f239c9b2271ea829dbef]
- A silent no-change success (exit 0 with unchanged tree) marks the task BLOCKED for human review rather than FAILED, unless the agent opts in via no_changes_exit_code. [@claim:clm_7dbff1382a95bee2b761e38d4b87fc5af4618dcdd69efb81870625934e13d092]
- The central dashboard (forgeo web) defaults to 0.0.0.0:8790, aggregates all registered instances, and exposes a per-instance HTTP API under /api/instances/<name>/ including task create/edit/delete, reopen, config PUT, and daemon start/stop/restart endpoints. [@claim:clm_d3ab0ad618a850d3121b80de9a49700266442b0db7cb0a8a8abf0bea23f9c2fb]
<!-- rcw:end owner=source:src_ac1bd9db6607570886182b4a80dfa269 block=evidence -->

## Researcher notes

