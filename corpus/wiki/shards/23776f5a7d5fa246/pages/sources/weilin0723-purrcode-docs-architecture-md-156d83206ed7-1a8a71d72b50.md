---
access: public
aliases: []
claim_ids:
- clm_86d62b313efbde48d7a496c122a8635013e556fa3a7fa4135473d0c71e61da27
- clm_9e1ea18de2a265f9ddefe5ce33d2a8a30ba18c64dd2408acee3103dd6ea3b96e
- clm_a7726638ccbcdda382c04e7437a79979e71f1c287e1b708a694dc34c40f5cb8f
maturity: draft
page_id: pg_10678dd2898b58709a501a8a71d72b50
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e2d41f37bd355ba3bd839e1af20688f5
title: Weilin0723/PurrCode/docs/architecture.md @ 156d83206ed7
updated_at: '2026-09-14T03:22:45Z'
---

# Weilin0723/PurrCode/docs/architecture.md @ 156d83206ed7

<!-- rcw:begin owner=source:src_e2d41f37bd355ba3bd839e1af20688f5 block=evidence -->
- Authorization is stored in append-only SQLite with exact action/constraint digest verification and atomic single-use consumption; NineLives owns durable events, checkpoints, restart reconciliation, and conservative recovery that never blindly replays interrupted actions. [@claim:clm_86d62b313efbde48d7a496c122a8635013e556fa3a7fa4135473d0c71e61da27]
- The architecture defines four subsystems: PawGate (policy/judgment/authorization), Claw (tool execution and sandboxing), Whisker (repository context and risk signals), and NineLives (checkpoints, recovery, rollback). [@claim:clm_9e1ea18de2a265f9ddefe5ce33d2a8a30ba18c64dd2408acee3103dd6ea3b96e]
- Actions are strongly typed (Command, RepositoryRead, WriteFile, DeleteFile, ExternalTool) with no shell-string parsing in the trusted path; ExternalTool actions are MCP-only and always require approval. [@claim:clm_a7726638ccbcdda382c04e7437a79979e71f1c287e1b708a694dc34c40f5cb8f]
<!-- rcw:end owner=source:src_e2d41f37bd355ba3bd839e1af20688f5 block=evidence -->

## Researcher notes

