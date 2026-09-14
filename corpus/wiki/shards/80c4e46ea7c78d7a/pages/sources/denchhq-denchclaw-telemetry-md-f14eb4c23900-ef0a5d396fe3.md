---
access: public
aliases: []
claim_ids:
- clm_04b81301411a384071e95bf4e09b85c2e19f15bbe1fcacba99ca0cc60ab7c5bc
- clm_20d4974bb838a9ec25213f07d71eadb0e0c77a82771be3245b92f7ae9b9b0220
- clm_f957eaee971edd9c099b2cf40e25160ef50c16e6e4ebf5a28b954df2960ee995
maturity: draft
page_id: pg_d5e4baab738d594aa270ef0a5d396fe3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_abc60c6bc26154ee94e014267e92efd8
title: DenchHQ/DenchClaw/TELEMETRY.md @ f14eb4c23900
updated_at: '2026-09-14T03:45:14Z'
---

# DenchHQ/DenchClaw/TELEMETRY.md @ f14eb4c23900

<!-- rcw:begin owner=source:src_abc60c6bc26154ee94e014267e92efd8 block=evidence -->
- Telemetry is anonymous and optional, split into product telemetry (CLI/web usage events) and AI observability via a PostHog LLM analytics plugin; both share opt-out controls and privacy mode, which is on by default and redacts message content and tool parameters. [@claim:clm_04b81301411a384071e95bf4e09b85c2e19f15bbe1fcacba99ca0cc60ab7c5bc]
- The posthog-analytics OpenClaw plugin runs in-process with the gateway, hooks agent lifecycle events (e.g. before_model_resolve, before_tool_call, agent_end), and emits PostHog AI events; it is installed automatically during bootstrap when a PostHog project key is available. [@claim:clm_20d4974bb838a9ec25213f07d71eadb0e0c77a82771be3245b92f7ae9b9b0220]
- PostHog Evaluations can score captured $ai_generation events using LLM-as-a-judge or deterministic Hog-based checks, storing pass/fail results with reasoning, configured entirely in the PostHog dashboard. [@claim:clm_f957eaee971edd9c099b2cf40e25160ef50c16e6e4ebf5a28b954df2960ee995]
<!-- rcw:end owner=source:src_abc60c6bc26154ee94e014267e92efd8 block=evidence -->

## Researcher notes

