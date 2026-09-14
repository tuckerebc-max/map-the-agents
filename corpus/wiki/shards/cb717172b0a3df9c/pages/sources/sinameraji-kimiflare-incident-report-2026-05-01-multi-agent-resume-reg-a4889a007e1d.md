---
access: public
aliases: []
claim_ids:
- clm_1e20bc3a0b273bd7210aaf6f7b0403fe91970a482a0f70ddd8ce043006ea3741
- clm_d9b8792bee3ab4db4dc5b5adf94a8cd63853fa1d4d88b126ae3fad6ab5dc2595
maturity: draft
page_id: pg_91019a25769c59e68517a4889a007e1d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_9fd5d62550a557be90bb5d68eeb49ce8
title: sinameraji/kimiflare/incident-report-2026-05-01-multi-agent-resume-regression.md
  @ efe84a2e65dc
updated_at: '2026-09-14T02:40:52Z'
---

# sinameraji/kimiflare/incident-report-2026-05-01-multi-agent-resume-regression.md @ efe84a2e65dc

<!-- rcw:begin owner=source:src_9fd5d62550a557be90bb5d68eeb49ce8 block=evidence -->
- An incident report documents that v0.29.0's multi-agent mode broke legacy /resume context, omitted system prompts for built-in agents, and crashed auto-compact; a fix was implemented but pending merge at report time. [@claim:clm_1e20bc3a0b273bd7210aaf6f7b0403fe91970a482a0f70ddd8ce043006ea3741]
- A multi-agent feature (PR #220, v0.29.0) uses an AgentOrchestrator with per-agent message buffers and built-in research/coding/generalist agents. [@claim:clm_d9b8792bee3ab4db4dc5b5adf94a8cd63853fa1d4d88b126ae3fad6ab5dc2595]
<!-- rcw:end owner=source:src_9fd5d62550a557be90bb5d68eeb49ce8 block=evidence -->

## Researcher notes

