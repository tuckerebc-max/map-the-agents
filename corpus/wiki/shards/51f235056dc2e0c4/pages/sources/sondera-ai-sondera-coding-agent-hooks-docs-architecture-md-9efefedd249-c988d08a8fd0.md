---
access: public
aliases: []
claim_ids:
- clm_2e75df0423716b7eb4c091eb3655c1c73464b5c8c6790a97c2d6d57a61e9f4d5
- clm_3a741e09d77fec14ba60d2e5a9ae0b274fa33b27303aa30df5d27b2d97db7b71
- clm_7783327bc069eb34f4f2ce168fe6716dc241982bfa659502336eedb6607d1c86
- clm_8767f500c0ffa2ddd79be00717321c6c9125448995e9b94ae40097ee222889ef
- clm_88ed8a71d007983c82e9c01c87da37e888b9248facff52d23c5abc89708dd93d
- clm_bf8497c681173ea7473cce5d7575717ec448844610374f088825240865108883
maturity: draft
page_id: pg_41a7ecf183b85ccdb377c988d08a8fd0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_01675cc58c7b54a0b51e577833b380da
title: sondera-ai/sondera-coding-agent-hooks/docs/architecture.md @ 9efefedd249e
updated_at: '2026-09-14T04:22:24Z'
---

# sondera-ai/sondera-coding-agent-hooks/docs/architecture.md @ 9efefedd249e

<!-- rcw:begin owner=source:src_01675cc58c7b54a0b51e577833b380da block=evidence -->
- The harness coordinates three guardrail subsystems: a YARA-X signature engine (always on and the only deterministic one), an optional LLM secure-code policy classifier, and optional LLM information-flow sensitivity labeling. [@claim:clm_2e75df0423716b7eb4c091eb3655c1c73464b5c8c6790a97c2d6d57a61e9f4d5]
- The optional LLM classifiers fail open when disabled, erroring, or slower than the adjudication budget — to compliant with no violations and to Public — so Cedar and the deterministic policies still decide. [@claim:clm_3a741e09d77fec14ba60d2e5a9ae0b274fa33b27303aa30df5d27b2d97db7b71]
- Agent execution is modeled as a trajectory of typed events in four categories: Action (pre-execution), Observation (post-execution), Control (lifecycle), and State (environment snapshots). [@claim:clm_7783327bc069eb34f4f2ce168fe6716dc241982bfa659502336eedb6607d1c86]
- The Cedar policy engine combines guardrail signals with entity state from a Turso (SQLite) local store and returns Allow, Deny, or Escalate adjudications back through the hook adapter. [@claim:clm_8767f500c0ffa2ddd79be00717321c6c9125448995e9b94ae40097ee222889ef]
- Agent-specific tool names normalize to shared event types (Claude's Bash, Cursor's shell hook, Copilot's and Gemini's bash all become ShellCommand), so one Cedar rule set governs every supported agent. [@claim:clm_88ed8a71d007983c82e9c01c87da37e888b9248facff52d23c5abc89708dd93d]
- Hook adapters speak stdin/stdout JSON with each agent, normalize the payload, and forward it over gRPC to `sondera serve` on loopback TCP, 127.0.0.1:50051 by default. [@claim:clm_bf8497c681173ea7473cce5d7575717ec448844610374f088825240865108883]
<!-- rcw:end owner=source:src_01675cc58c7b54a0b51e577833b380da block=evidence -->

## Researcher notes

