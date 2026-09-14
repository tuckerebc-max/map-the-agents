---
access: public
aliases: []
claim_ids:
- clm_282c65fb898dbc36c04ca741468f17d4fe306b35cfe25c16f96733339b435d11
- clm_7a57cadd1c414fb6b86affaf23659e238323b1f38ce4fc1872cd33a8db67904e
- clm_b681d68111c5abe390647f360132cd7da05640b2c7eb469edf57a106aa232433
maturity: draft
page_id: pg_c4d72c023cfb59088c3cef8e7393a903
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_fa7cb92e480157b48a7e8c3e9b4754f4
title: sondera-ai/sondera-coding-agent-hooks/docs/deployment.md @ 9efefedd249e
updated_at: '2026-09-14T04:22:24Z'
---

# sondera-ai/sondera-coding-agent-hooks/docs/deployment.md @ 9efefedd249e

<!-- rcw:begin owner=source:src_fa7cb92e480157b48a7e8c3e9b4754f4 block=evidence -->
- Enabling the LLM classifiers adds latency to every decision they touch, and with guardrails enabled event content is sent to the configured provider. [@claim:clm_282c65fb898dbc36c04ca741468f17d4fe306b35cfe25c16f96733339b435d11]
- Enforcement hooks fail closed: a hook that cannot reach the harness denies preventive events and never proceeds unadjudicated, so losing the server blocks the agent rather than ungoverning it. [@claim:clm_7a57cadd1c414fb6b86affaf23659e238323b1f38ce4fc1872cd33a8db67904e]
- Neither gRPC surface authenticates its caller: adjudication is plain HTTP/2 gRPC and the console returns the whole local store and exposes agent deletion, so the bind address should stay on loopback or behind an authenticating proxy. [@claim:clm_b681d68111c5abe390647f360132cd7da05640b2c7eb469edf57a106aa232433]
<!-- rcw:end owner=source:src_fa7cb92e480157b48a7e8c3e9b4754f4 block=evidence -->

## Researcher notes

