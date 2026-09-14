---
access: public
aliases: []
claim_ids:
- clm_0c52b5e9fa3c5908562badbbc1a9ff895266ea12d234b218523ca3003e54c890
- clm_504f648f05aeb4939c03e141cbaf147f4e77bf628a6adfdeaa346afb6bce4fff
- clm_5aeedf5a8c7c529d4885e79023445d6b7ea0ccb320c4434272c3f4fb81309542
- clm_6f3de731e7a42cf1e2d117a1297a4837fb3c6feaf2a24000a9af19a720d5fffd
- clm_90d08d1fb750a1e91da15903c5aefc90e3ad49f24092630935967588041a2201
- clm_94d78c25a498fcad49d89b45d05e174f2926ca8cbac3eeeb0ede5c775f3fdfac
- clm_95412ace5f12b83315def870104145fffb95a11cfb725736c30c60f80fa8d8e8
- clm_a42471615f9e043609df3b25db5a2ac4366448d94b35bb0353c0cced01632b30
- clm_d496e2732aac8432cfddf70194315f9729284807c5799199f227bdfe490ba9ab
- clm_fee01852baee4e1725f417e41810c0a20f4a1e2975d17c7605f0b18bc375d17a
maturity: draft
page_id: pg_262e160ca7d25690bf870e0df0cea517
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_eef50f07ee655226b1f596c57191d43f
title: EmilianoMusso/EntwineLLM/README.md @ 05d11506b780
updated_at: '2026-09-14T02:00:55Z'
---

# EmilianoMusso/EntwineLLM/README.md @ 05d11506b780

<!-- rcw:begin owner=source:src_eef50f07ee655226b1f596c57191d43f block=evidence -->
- The extension requires a local or Docker-hosted open LLM implementation such as Ollama or LMStudio, running and exposing an API endpoint reachable from Visual Studio. [@claim:clm_0c52b5e9fa3c5908562badbbc1a9ff895266ea12d234b218523ca3003e54c890]
- The product is a Visual Studio extension whose commands appear under the Extensions menu (moved there in v1.9.0; earlier versions placed them under Tools). [@claim:clm_504f648f05aeb4939c03e141cbaf147f4e77bf628a6adfdeaa346afb6bce4fff]
- The project ships a docker-compose file and a sample nginx configuration to test an LLM behind an authenticating reverse proxy locally. [@claim:clm_5aeedf5a8c7c529d4885e79023445d6b7ea0ccb320c4434272c3f4fb81309542]
- Generated output can overwrite the selected code via an Apply button or be saved to a dynamically named file in the current project folder via a Save button. [@claim:clm_6f3de731e7a42cf1e2d117a1297a4837fb3c6feaf2a24000a9af19a720d5fffd]
- The Follow-up feature lets users submit additional prompts that build on a prior code generation, sending the follow-up to the LLM for updated results. [@claim:clm_90d08d1fb750a1e91da15903c5aefc90e3ad49f24092630935967588041a2201]
- Configuration options in the Visual Studio Options menu let users set the LLM base URL, choose a model per command, set HTTP request timeouts, and pick the answer language. [@claim:clm_94d78c25a498fcad49d89b45d05e174f2926ca8cbac3eeeb0ede5c775f3fdfac]
- Prompts target multiple languages (C#, Python, Java), reject non-coding requests, and enforce Clean Code principles with raw, comment-free output following Allman-style braces. [@claim:clm_95412ace5f12b83315def870104145fffb95a11cfb725736c30c60f80fa8d8e8]
- Since v1.13, an optional authentication token setting makes the extension send an Authorization: Bearer header on all LLM API requests; when empty, the header is omitted for backward compatibility. [@claim:clm_a42471615f9e043609df3b25db5a2ac4366448d94b35bb0353c0cced01632b30]
- The list of selectable LLM models is obtained by querying Ollama APIs, so users must install needed models beforehand. [@claim:clm_d496e2732aac8432cfddf70194315f9729284807c5799199f227bdfe490ba9ab]
- Available commands include Refactor code, Generate unit tests, Follow-up, and Document code, which query the configured LLM and show results in a window. [@claim:clm_fee01852baee4e1725f417e41810c0a20f4a1e2975d17c7605f0b18bc375d17a]
<!-- rcw:end owner=source:src_eef50f07ee655226b1f596c57191d43f block=evidence -->

## Researcher notes

