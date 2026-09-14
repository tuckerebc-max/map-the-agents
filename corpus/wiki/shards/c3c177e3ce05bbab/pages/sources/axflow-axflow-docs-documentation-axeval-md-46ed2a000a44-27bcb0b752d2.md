---
access: public
aliases: []
claim_ids:
- clm_05cc58f2eda14f098414c627032783f3f317cccd92de46297fb8ecaf7130d824
- clm_1cef0102433248f9b952289a6deb3bb9621ebcad25da374b84dc7cc2c454d4aa
- clm_6db913c302b502e925f1e8e876d8e95ebcbf3ca835cb451a098a59e4de9979fa
- clm_c1c7d0002a9a44688b55054083c625bd2bfba24388d47cf3ecbe7832715dd7bf
- clm_fa69ee4b9c919429de4b8b5e20c4efd472a0d31159c3250e03fbe5d7ef2a8f92
maturity: draft
page_id: pg_9d47175f646a57629c3327bcb0b752d2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_eaf00bc5556d5b289b8649966db93ce8
title: axflow/axflow/docs/documentation/axeval.md @ 46ed2a000a44
updated_at: '2026-09-14T03:37:09Z'
---

# axflow/axflow/docs/documentation/axeval.md @ 46ed2a000a44

<!-- rcw:begin owner=source:src_eaf00bc5556d5b289b8649966db93ce8 block=evidence -->
- Modules are installed independently via npm (npm i axeval; npm install @axflow/models, axgen, axeval). [@claim:clm_05cc58f2eda14f098414c627032783f3f317cccd92de46297fb8ecaf7130d824]
- Axeval's API centers on EvalCases (prompt plus one or more evaluators), evaluators that score a prompt/response pair from 0 to 1, EvalResults with metadata like score and latency, Reports, and a Runner that executes suites against models. [@claim:clm_1cef0102433248f9b952289a6deb3bb9621ebcad25da374b84dc7cc2c454d4aa]
- Axeval is a framework for test-driven LLM engineering: it supports unit-testing prompts, data-driven prompt iteration, and comparing models on latency, cost, and accuracy. [@claim:clm_6db913c302b502e925f1e8e876d8e95ebcbf3ca835cb451a098a59e4de9979fa]
- Built-in evaluators include match, includes, isValidJSON, and llmRubric, and users can write custom evaluators. [@claim:clm_c1c7d0002a9a44688b55054083c625bd2bfba24388d47cf3ecbe7832715dd7bf]
- The Runner API lets users register named test suites bound to specific models (e.g., AnthropicCompletion 'claude-2', OpenAICompletion 'text-davinci-003') and run them, producing a report that can be output to formats such as stdout. [@claim:clm_fa69ee4b9c919429de4b8b5e20c4efd472a0d31159c3250e03fbe5d7ef2a8f92]
<!-- rcw:end owner=source:src_eaf00bc5556d5b289b8649966db93ce8 block=evidence -->

## Researcher notes

