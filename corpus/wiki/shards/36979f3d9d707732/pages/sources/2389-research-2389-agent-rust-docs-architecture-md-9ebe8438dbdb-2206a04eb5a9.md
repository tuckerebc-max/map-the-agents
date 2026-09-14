---
access: public
aliases: []
claim_ids:
- clm_08094b898032f30087693c9da28d6e638d9bf0c3792e2890bfbcce87657dcba4
- clm_0e8319ee1c7a4658b65ec1218313a80514e3998cfe89b389333076ef4236cc57
- clm_1fb3cce3856d8599171fd91df82c91b29b7b646623c9e4896d45842692066fd9
- clm_3b5d917c455185f35669ddd1720db8f4053dd56edb676bc092c72b28dd78233c
- clm_40000d59be14b8c76d56b55f1beca7e77d0b0dfa088e8096c42f202ddd1cf026
- clm_a4c2a78039fc7ff988af0410b5cebc648537754390b8a637bc4b363bcdab023b
- clm_c6ce283c6a9311c402be2b9cb45ac246f41dd74cdc812a280afec3a3379c0e1d
- clm_fd4cc04f0f0c6bb196ea2241262581ce69d2ab73c38155a2b3c5358e65a098cc
maturity: draft
page_id: pg_8ff0ddec33e95217b3172206a04eb5a9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_137487f9e035524581ab74c136f065a2
title: 2389-research/2389-agent-rust/docs/ARCHITECTURE.md @ 9ebe8438dbdb
updated_at: '2026-09-14T02:48:40Z'
---

# 2389-research/2389-agent-rust/docs/ARCHITECTURE.md @ 9ebe8438dbdb

<!-- rcw:begin owner=source:src_137487f9e035524581ab74c136f065a2 block=evidence -->
- The threat model names four trust boundaries: the MQTT network perimeter, process isolation around tool execution, the LLM provider API boundary, and input validation at the data boundary. [@claim:clm_08094b898032f30087693c9da28d6e638d9bf0c3792e2890bfbcce87657dcba4]
- The Rust-language decision record acknowledges two consequences: a steeper learning curve for contributors unfamiliar with Rust, and longer compile times than an interpreted language would have. [@claim:clm_0e8319ee1c7a4658b65ec1218313a80514e3998cfe89b389333076ef4236cc57]
- The architecture doc describes this project as a Rust implementation of the 2389 Agent Protocol, with agents interoperating over MQTT and an emphasis on reliability and strict protocol compliance. [@claim:clm_1fb3cce3856d8599171fd91df82c91b29b7b646623c9e4896d45842692066fd9]
- A second accepted decision record names rumqttc as the MQTT client library, noting it avoids external C dependencies since it is a pure-Rust implementation. [@claim:clm_3b5d917c455185f35669ddd1720db8f4053dd56edb676bc092c72b28dd78233c]
- Documentation describes an explicit agent lifecycle moving through Uninitialized, Initializing, Running, Stopping and Stopped, with any state able to transition to an Error state on failure. [@claim:clm_40000d59be14b8c76d56b55f1beca7e77d0b0dfa088e8096c42f202ddd1cf026]
- An accepted architecture decision record states Rust was chosen for the core implementation, citing memory safety without garbage-collection overhead and strong async support as rationale. [@claim:clm_a4c2a78039fc7ff988af0410b5cebc648537754390b8a637bc4b363bcdab023b]
- Listed tool-execution security controls include JSON-schema validation of parameters, per-tool process isolation with timeouts, and restricting available tools to an allow-list. [@claim:clm_c6ce283c6a9311c402be2b9cb45ac246f41dd74cdc812a280afec3a3379c0e1d]
- The LLM integration layer is documented as provider-agnostic behind a shared trait, with Anthropic Claude and OpenAI GPT listed as the currently supported providers. [@claim:clm_fd4cc04f0f0c6bb196ea2241262581ce69d2ab73c38155a2b3c5358e65a098cc]
<!-- rcw:end owner=source:src_137487f9e035524581ab74c136f065a2 block=evidence -->

## Researcher notes

