---
access: public
aliases: []
claim_ids:
- clm_65b7ca57b7e04f54978d8e21dbd08f485533eae2ea969aa8c1e0e7a438c09007
- clm_d2c20d571421fb60071f751de608eb7a21801a80ff28e944bb806d40a4832008
- clm_fca8982ef3065dd80bfa6153eda29e1ffd6dd3c6ddcb626f0e2906a25e96411c
- clm_fe5a5f4c8a1acaddc566865581f95a952cc0ee40235826056be2a4121408208a
maturity: draft
page_id: pg_8a980d37bbc458b48c27352a78a25699
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_17214af7ae105af48f573b3cafa9284d
title: SWE-agent/SWE-ReX/docs/architecture.md @ 5c995c365dfb
updated_at: '2026-09-14T04:24:36Z'
---

# SWE-agent/SWE-ReX/docs/architecture.md @ 5c995c365dfb

<!-- rcw:begin owner=source:src_17214af7ae105af48f573b3cafa9284d block=evidence -->
- Deployment classes start the target environment (e.g. a Docker container or AWS instance) and hand back a RemoteRuntime instance as the main interface for interacting with the environment. [@claim:clm_65b7ca57b7e04f54978d8e21dbd08f485533eae2ea969aa8c1e0e7a438c09007]
- Because LocalRuntime can be used directly when code runs locally or in a sandboxed environment, the framework appears to support fully local usage without a remote deployment. [@claim:clm_d2c20d571421fb60071f751de608eb7a21801a80ff28e944bb806d40a4832008]
- The Runtime class provides file read/write methods, an execute method for arbitrary commands, and a run_in_session method to run commands in an existing shell or interactive session. [@claim:clm_fca8982ef3065dd80bfa6153eda29e1ffd6dd3c6ddcb626f0e2906a25e96411c]
- A FastAPI server inside the container forwards requests from RemoteRuntime to LocalRuntime, which actually executes commands; the two classes share the same interface, are interchangeable, and exceptions from LocalRuntime are transferred transparently. [@claim:clm_fe5a5f4c8a1acaddc566865581f95a952cc0ee40235826056be2a4121408208a]
<!-- rcw:end owner=source:src_17214af7ae105af48f573b3cafa9284d block=evidence -->

## Researcher notes

