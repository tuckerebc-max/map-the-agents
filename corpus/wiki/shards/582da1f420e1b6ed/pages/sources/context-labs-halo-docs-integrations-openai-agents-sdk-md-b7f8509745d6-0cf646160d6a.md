---
access: public
aliases: []
claim_ids:
- clm_198a146ae41ab9d1b32ff045c8bf5804e594ccad82fef1ca108b482751b10c3e
- clm_fd62ac594fe5a1a08da02d6eb1ad53b140e96b4eef647e2b80f4154b61b0bbd8
maturity: draft
page_id: pg_93a4e21fd03c5370be090cf646160d6a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_aaee50048e1d5762bc2580c2b7829062
title: context-labs/HALO/docs/integrations/openai-agents-sdk.md @ b7f8509745d6
updated_at: '2026-09-14T03:42:54Z'
---

# context-labs/HALO/docs/integrations/openai-agents-sdk.md @ b7f8509745d6

<!-- rcw:begin owner=source:src_aaee50048e1d5762bc2580c2b7829062 block=evidence -->
- The integration writes one JSONL span per line with OTLP identity fields, resource/scope blocks, and inference.* projection attributes (project_id, observation_kind, token counts, tool/agent attributes) that the Engine indexes on, filtering on inference.project_id. [@claim:clm_198a146ae41ab9d1b32ff045c8bf5804e594ccad82fef1ca108b482751b10c3e]
- The OpenAI Agents SDK integration's tracing.py is a self-contained ~450-line module using only stdlib plus openai-agents, with no OpenTelemetry packages, exporter, collector, or instrumentor required. [@claim:clm_fd62ac594fe5a1a08da02d6eb1ad53b140e96b4eef647e2b80f4154b61b0bbd8]
<!-- rcw:end owner=source:src_aaee50048e1d5762bc2580c2b7829062 block=evidence -->

## Researcher notes

