---
access: public
aliases: []
claim_ids:
- clm_3143a24bf47827b11ebaef5c10415e984df06a6786fe9250b1aaf5ee07e3ef75
- clm_387132402162083678b17ab5dfc856bd77ecd06fd5b861bbc9f7539349432432
- clm_834c5449ca673302c888da5ed60bd4150578ef77b440b160d1f53f9d9c1f4d89
- clm_ae66b098d51a65b6acaedc17838de1120965c3910ae0b55a9e365fd5335cf33b
- clm_d5c6ed66aec551da1a1b2b4ea80dba83a4be9f8321f7ef27a0f8f6f106cf2b57
maturity: draft
page_id: pg_9df204eec6b05bfbb66c5805df312fee
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5f515d7fbb135d969f75cacb71e7f0dd
title: cuga-project/cuga-agent/docs/examples/a2a_two_cuga/README.md @ 65bdf2fb376d
updated_at: '2026-09-14T04:55:58Z'
---

# cuga-project/cuga-agent/docs/examples/a2a_two_cuga/README.md @ 65bdf2fb376d

<!-- rcw:begin owner=source:src_5f515d7fbb135d969f75cacb71e7f0dd block=evidence -->
- The provider exposes an A2A surface: a JSON-RPC endpoint at /a2a and an AgentCard at /.well-known/agent.json, per the example's documented URLs. [@claim:clm_3143a24bf47827b11ebaef5c10415e984df06a6786fe9250b1aaf5ee07e3ef75]
- A consumer supervisor config declares an external agent with a2a_protocol.transport=http; CUGA fetches the provider's AgentCard at startup, surfaces it as a tool, and delegates via delegate_task_via_a2a_sdk as JSON-RPC. [@claim:clm_387132402162083678b17ab5dfc856bd77ecd06fd5b861bbc9f7539349432432]
- A registry component serves the digital_sales OpenAPI tool catalog on http://localhost:8001, started with 'cuga start registry' in the example. [@claim:clm_834c5449ca673302c888da5ed60bd4150578ef77b440b160d1f53f9d9c1f4d89]
- In the A2A example both CUGAs run with auth_required=false, and the auth-token forwarding integration test is marked xfail until v1. [@claim:clm_ae66b098d51a65b6acaedc17838de1120965c3910ae0b55a9e365fd5335cf33b]
- The provider side uses a supervisor YAML declaring one internal agent (digital_sales) that pulls tools from the registry; DYNACONF_A2A__ENABLED=true and a supervisor config path env var route inbound A2A requests through it. [@claim:clm_d5c6ed66aec551da1a1b2b4ea80dba83a4be9f8321f7ef27a0f8f6f106cf2b57]
<!-- rcw:end owner=source:src_5f515d7fbb135d969f75cacb71e7f0dd block=evidence -->

## Researcher notes

