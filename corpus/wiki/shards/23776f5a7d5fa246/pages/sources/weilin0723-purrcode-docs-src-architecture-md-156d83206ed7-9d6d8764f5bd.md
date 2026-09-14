---
access: public
aliases: []
claim_ids:
- clm_3b8a94e5cfe6f5795bc5b5e474ecf2723dca41f43dc91df56f7c55b6c607077a
- clm_86d62b313efbde48d7a496c122a8635013e556fa3a7fa4135473d0c71e61da27
- clm_9e1ea18de2a265f9ddefe5ce33d2a8a30ba18c64dd2408acee3103dd6ea3b96e
- clm_dc882e293cc6bbf333c6cc8763fda4fbd852f066f70ab74ed02a8a299436960b
maturity: draft
page_id: pg_07d3b61cf3875b4fab769d6d8764f5bd
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_762f4e2667f3514d8ac9a56e4c2966f5
title: Weilin0723/PurrCode/docs/src/architecture.md @ 156d83206ed7
updated_at: '2026-09-14T03:22:45Z'
---

# Weilin0723/PurrCode/docs/src/architecture.md @ 156d83206ed7

<!-- rcw:begin owner=source:src_762f4e2667f3514d8ac9a56e4c2966f5 block=evidence -->
- TUI, IDE, and CLI share one daemon-owned session model; the IDE holds no session store, model state, permission state, or execution path, and the daemon exposes typed presentation endpoints (activity, validation, summary, usage). [@claim:clm_3b8a94e5cfe6f5795bc5b5e474ecf2723dca41f43dc91df56f7c55b6c607077a]
- Authorization is stored in append-only SQLite with exact action/constraint digest verification and atomic single-use consumption; NineLives owns durable events, checkpoints, restart reconciliation, and conservative recovery that never blindly replays interrupted actions. [@claim:clm_86d62b313efbde48d7a496c122a8635013e556fa3a7fa4135473d0c71e61da27]
- The architecture defines four subsystems: PawGate (policy/judgment/authorization), Claw (tool execution and sandboxing), Whisker (repository context and risk signals), and NineLives (checkpoints, recovery, rollback). [@claim:clm_9e1ea18de2a265f9ddefe5ce33d2a8a30ba18c64dd2408acee3103dd6ea3b96e]
- Model output is treated as a proposal, never authority: every native action is bound to a durable authorization, re-checked before execution, and followed by recorded validation; repository content, model output, and downloaded skills are untrusted. [@claim:clm_dc882e293cc6bbf333c6cc8763fda4fbd852f066f70ab74ed02a8a299436960b]
<!-- rcw:end owner=source:src_762f4e2667f3514d8ac9a56e4c2966f5 block=evidence -->

## Researcher notes

