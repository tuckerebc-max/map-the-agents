---
access: public
aliases: []
claim_ids:
- clm_0983bbf29b4045e2d726bd156f2c8ae292df3a38e4410c80b6029ca6347f58f7
- clm_22d61fd874fb6916074dfc80070a3ba9bba39877dc3123c94ccef49116297ee9
- clm_4a6d50386ec2f86137b83748c2588be1b36378f8848e55907c76fa8ec401a4ba
- clm_5a194948e06165e8044e794a22cdcac4add585894c6760c4df609e0587f23b2a
- clm_5d4577bb8e47f59b43b6c9e29ce955b3c5f2dcd3ada059091118a36dc69dae12
- clm_6ee9ffd4d6d73ead1fc400701983c223c8b139a5b2358d68a627471c3ff5829d
- clm_9f8c09e23b31b6a7fb4aff90a02b34b539773ad5c9b8b2bd71b8c6301498ee75
- clm_af0fe9f9166a6e7b9c2f52fa9a919e46a1c8857e668601461f3ca209cc1af38c
- clm_b6db8eaf021a8a578de9f07c29be4e9c4f173f63707086d01ea18bfd1aa0af2f
- clm_ffe8d231e17839decbf44cf7b6d6a4d2a535b68f0dd2b8ead70800d65e63db5a
maturity: draft
page_id: pg_1e36dafb1e895ff1ac3ea043674ee928
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_980c78f9cbf456a4be1b45d98936912c
title: open-multi-agent/open-multi-agent/README.md @ eaeb420c4364
updated_at: '2026-09-14T02:26:17Z'
---

# open-multi-agent/open-multi-agent/README.md @ eaeb420c4364

<!-- rcw:begin owner=source:src_980c78f9cbf456a4be1b45d98936912c block=evidence -->
- An OpenMultiAgent instance is constructed with a default provider/model and an onToolCall callback that can return 'suspend' for consequential tool calls or 'allow' otherwise. [@claim:clm_0983bbf29b4045e2d726bd156f2c8ae292df3a38e4410c80b6029ca6347f58f7]
- Repository development practice: issues and pull requests are welcome, with CONTRIBUTING.md covering workspace boundaries, validation, and submission guidance. [@claim:clm_22d61fd874fb6916074dfc80070a3ba9bba39877dc3123c94ccef49116297ee9]
- Egress policy supports 'offline' or 'allowlist' modes checked before a built-in adapter connects; child policies can only tighten parents, unenforceable transports fail closed, and process/ACP backends sit outside the policy. [@claim:clm_4a6d50386ec2f86137b83748c2588be1b36378f8848e55907c76fa8ec401a4ba]
- With governanceIntent 'required', runs are judged on an execution receipt of roles, ordering, dependency edges, and independent review; the evaluator never sees agent output text, and a successful run can still report 'unsatisfied'. [@claim:clm_5a194948e06165e8044e794a22cdcac4add585894c6760c4df609e0587f23b2a]
- The runtime records every model block, tool call, and context rewrite in a journal; verifyRun() checks offline that each block reproduces byte for byte, reporting evicted windows as inconclusive rather than failures. [@claim:clm_5d4577bb8e47f59b43b6c9e29ce955b3c5f2dcd3ada059091118a36dc69dae12]
- Consequential actions pause for durable approvals: a suspend request is stored beside the checkpoint, bound to a SHA-256 hash of what the reviewer saw, decisions are atomic and first-wins, and tampered requests fail closed. [@claim:clm_6ee9ffd4d6d73ead1fc400701983c223c8b139a5b2358d68a627471c3ff5829d]
- runTeam() uses one model call to turn a goal into a task graph with assignees and dependencies, a deterministic scheduler executes it, and a second call writes the final answer; the coordinator is not consulted mid-run. [@claim:clm_9f8c09e23b31b6a7fb4aff90a02b34b539773ad5c9b8b2bd71b8c6301498ee75]
- The project requires Node.js 20 or newer; Node 20 is upstream-EOL, kept only as a migration window, and will be removed in the next major release no earlier than 2026-10-31. [@claim:clm_af0fe9f9166a6e7b9c2f52fa9a919e46a1c8857e668601461f3ca209cc1af38c]
- Built-in provider adapters cover Anthropic, OpenAI, Azure OpenAI, Bedrock, Gemini, Grok, Copilot, several Chinese providers, plus Ollama, vLLM, and llama-server via baseURL and any OpenAI-compatible or Vercel AI SDK endpoint. [@claim:clm_b6db8eaf021a8a578de9f07c29be4e9c4f173f63707086d01ea18bfd1aa0af2f]
- The core package exposes three run modes: runAgent() for a single agent, runTasks() for an explicit pipeline, and runTeam() which plans from a goal. [@claim:clm_ffe8d231e17839decbf44cf7b6d6a4d2a535b68f0dd2b8ead70800d65e63db5a]
<!-- rcw:end owner=source:src_980c78f9cbf456a4be1b45d98936912c block=evidence -->

## Researcher notes

