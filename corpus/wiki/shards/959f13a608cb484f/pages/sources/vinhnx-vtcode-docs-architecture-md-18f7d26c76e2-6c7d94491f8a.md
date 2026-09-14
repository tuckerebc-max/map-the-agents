---
access: public
aliases: []
claim_ids:
- clm_1e3bec124a4f73f70cdf323253c0b20a1b3e5515deefecf78676e391cf00e36a
- clm_48a6b59da80c47ab9878bd8c7835334964a4fd640576244c5919012c21f24dc0
- clm_60046b34315663cfb147fe9d6b65a77b114c523287e08877ed52c61fda45c7d6
- clm_6e5dbab108180acb00e3375600d1ea7b54fd606a3842be6720d12cccf0297428
- clm_6ef343e7928a4cf6ae926150393063eea497ee91f908e4d7e43fef9a518d0da1
- clm_7f3c0cc587b459a327597326855b28aedbc7c126ef8e0074808864109c192089
- clm_a30db75e4cf6eaa56af6b0f0b2b3580641747e16e5690c7ce11bacaf859a410a
maturity: draft
page_id: pg_32d0ac10b1965646a6976c7d94491f8a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9bc7d5b495a655f68373ea3e83f82d48
title: vinhnx/VTCode/docs/ARCHITECTURE.md @ 18f7d26c76e2
updated_at: '2026-09-14T03:21:46Z'
---

# vinhnx/VTCode/docs/ARCHITECTURE.md @ 18f7d26c76e2

<!-- rcw:begin owner=source:src_9bc7d5b495a655f68373ea3e83f82d48 block=evidence -->
- Default public tool surface includes exec_command (shell via policy/sandbox/approvals), write_stdin for live-session continuation, and apply_patch with workspace-boundary checks. [@claim:clm_1e3bec124a4f73f70cdf323253c0b20a1b3e5515deefecf78676e391cf00e36a]
- ThreadEvent (vtcode-exec-events) is the authoritative runtime event contract feeding replay, checkpoints, memory, and trajectory export; follow-up inputs queue and inject one at a time at idle boundaries. [@claim:clm_48a6b59da80c47ab9878bd8c7835334964a4fd640576244c5919012c21f24dc0]
- Delegation is modeled as explicit thread spawning: child agents do bounded sidecar work, their output is advisory until the parent validates and merges it into the SessionMemoryEnvelope at turn boundaries. [@claim:clm_60046b34315663cfb147fe9d6b65a77b114c523287e08877ed52c61fda45c7d6]
- The architecture separates the model (reasoning) from the harness (runtime supplying tools, context, sandboxing, state, and verification), organized as seven reinforcing subsystems. [@claim:clm_6e5dbab108180acb00e3375600d1ea7b54fd606a3842be6720d12cccf0297428]
- The CLI separates data on stdout from diagnostics on stderr, uses clap for argument parsing, isolates subcommands (ask, exec, chat) in dedicated modules, and handles SIGINT/SIGTERM gracefully. [@claim:clm_6ef343e7928a4cf6ae926150393063eea497ee91f908e4d7e43fef9a518d0da1]
- A persisted SessionMemoryEnvelope summarizes objective, constraints, touched files, grounded facts, verification status, and delegated findings for resume and summarized-fork handoff. [@claim:clm_7f3c0cc587b459a327597326855b28aedbc7c126ef8e0074808864109c192089]
- With agent.harness.orchestration_mode = plan_build_evaluate, a planner writes spec/contract artifacts, the generator runs on the main session, and an evaluator performs a skeptical post-build pass; failed evaluation triggers bounded revision rounds. [@claim:clm_a30db75e4cf6eaa56af6b0f0b2b3580641747e16e5690c7ce11bacaf859a410a]
<!-- rcw:end owner=source:src_9bc7d5b495a655f68373ea3e83f82d48 block=evidence -->

## Researcher notes

