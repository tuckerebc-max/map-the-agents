---
access: public
aliases: []
claim_ids:
- clm_0ce59c42ae9eb4d649d02ef1a15400170ec5236e0c4612d006d3b1da880fb160
- clm_34f54d8b9a5ebf57910ac32e7949fcbf7840411d305551770e9e13772a8201f5
- clm_7daba09d4c9d196c92e3a6214a8fbb587eeba46a6dd793b3e26ef45728990dd1
- clm_ae7cc88cc46ec8df800819b1cbc2174a01476345df240f1722a1aeb88cb60b23
- clm_b6ef33a419da9b6a4754696182b48949da68678461ff6d67210f042d8e355858
- clm_cbf9163feda76f637f22834f0145cccd52552d5ab51967614e85160c15d985a1
- clm_dde1f11e32a47a9519330fb4b72cd4f5db5114039e8d2fce8f5d25c6f58519c2
- clm_fc2956f870a29f84b57798055cc5fa63e7450eb920f6e4f6548956a723ea6134
maturity: draft
page_id: pg_49d5e23b23585c219ddb6e12440c6520
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_713f4f24bf0c550fb7498b9a778269e1
title: neovateai/neovate-code/docs/designs/2025-01-27-bash-background-execution.md
  @ 0a24b363ecbe
updated_at: '2026-09-14T02:22:03Z'
---

# neovateai/neovate-code/docs/designs/2025-01-27-bash-background-execution.md @ 0a24b363ecbe

<!-- rcw:begin owner=source:src_713f4f24bf0c550fb7498b9a778269e1 block=evidence -->
- The planned BackgroundTaskManager stores tasks in a Map with fields id, command, pid, optional pgid, status (running/completed/killed/failed), createdAt, output, and exitCode, generating ids prefixed 'task_'. [@claim:clm_0ce59c42ae9eb4d649d02ef1a15400170ec5236e0c4612d006d3b1da880fb160]
- Because the bash background execution material is a step-by-step implementation plan with TDD instructions, the described tools and behavior appear to be proposed rather than verified as already shipped in this snapshot. [@claim:clm_34f54d8b9a5ebf57910ac32e7949fcbf7840411d305551770e9e13772a8201f5]
- The planned bash_output tool takes a task_id and returns the task's command, status, PID, creation time, accumulated output, and exit code when set. [@claim:clm_7daba09d4c9d196c92e3a6214a8fbb587eeba46a6dd793b3e26ef45728990dd1]
- Background detection runs a command in background if user-requested, or if elapsed time exceeds a 2000ms threshold with output and the command root matches a dev-command list (npm, pnpm, yarn, node, python, go, cargo, docker, vite, jest, pytest, and others). [@claim:clm_ae7cc88cc46ec8df800819b1cbc2174a01476345df240f1722a1aeb88cb60b23]
- A 2025-01-27 plan proposes background bash execution so the LLM can monitor and control long-running development tasks, extending the bash tool with a BackgroundTaskManager plus bash_output and kill_bash tools. [@claim:clm_b6ef33a419da9b6a4754696182b48949da68678461ff6d67210f042d8e355858]
- The plan adds a run_in_background boolean parameter to the bash tool and documents that dev-pattern commands auto-move to background after 2 seconds if producing output, returning a task_id for bash_output and kill_bash. [@claim:clm_cbf9163feda76f637f22834f0145cccd52552d5ab51967614e85160c15d985a1]
- In the planned design, bash_output requires no approval (category 'read', needsApproval returns false), while kill_bash refuses to terminate tasks whose status is not 'running'. [@claim:clm_dde1f11e32a47a9519330fb4b72cd4f5db5114039e8d2fce8f5d25c6f58519c2]
- The planned killTask uses taskkill on Windows; otherwise it signals the process group with SIGTERM, then SIGKILL after 200ms if still running, falling back to killing the pid directly. [@claim:clm_fc2956f870a29f84b57798055cc5fa63e7450eb920f6e4f6548956a723ea6134]
<!-- rcw:end owner=source:src_713f4f24bf0c550fb7498b9a778269e1 block=evidence -->

## Researcher notes

