---
access: public
aliases: []
claim_ids:
- clm_0033f403061d1fcd65a53659f6a29b0db8154a50c7f1e67c4b944c44290eb9d1
- clm_0c4d60a1490d8accd9e220c00e9b0f2b38c5b4addaaa71031528cc263ade3e99
- clm_108f48d0af773248d06641ebeb5ba4e7569d86c768659edd76ee1edb39f410c3
- clm_1afe1f84d910bdc2750434ec146a76b632d9c4b508a0d8a8b6e4c2ccf6ac7a8a
- clm_1b44954215456db181435ebd6f1d5594c5e9dee32ebc8974d1c33de4c2829bb8
- clm_2ace9cc7463af402aed1ac779f0b4264c4d94066f742ef78cf6ca7acc379b71a
- clm_4452831a294aa151c7597473296fd2bfaec3d5fc41f4180a9e04161fdecbf0d3
- clm_501f196bd2976c0d357d8f4f5bc916c6a43edf2554e6c7391f1847534e5482da
- clm_5f8e67187f605287fceff8497556b07ba7cc355861fe2a5f7457e60b68fec3a0
- clm_8069d8372df06538b2c1c7b3fde1e1f59c88207188e1dbe7bd42cfdb8de2f070
- clm_875620f8d8be213726cb6b23a92683f08dd62fbfe6931f5ebea93653520bb1d4
- clm_9ef92e1cb7f5544b14d523f0ec508e729692d4eb228be6885c7a2220c74047b6
- clm_bafb075e18422d7b049382327a8b22195e3ad3626b9181d9175553aab650c188
- clm_c487bff315a8566467bfc106adaadce4e00114698e3688cec0f7c2ce292bd714
- clm_c76187eedf2a776c182839941f859ef5e0a4e2ecbb0e276d65e141e1f0c8dd79
- clm_e8dd87589465e420d15b1242aea80672aa91435e6564d5169cce667669d5965c
- clm_ec3407f15420378be2f4267fbe90627330ac76ace1963f7a9270b87e0fe055db
- clm_f34931e1a6a9ce2d1a87a7a94feb49fc536c11d46cab9276ef2c87e5699da537
maturity: draft
page_id: pg_6fa6d3936663545f8072431d67d3a74a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f5a5af977b98529a99d0e932a0b32ae7
title: 2389-research/tracker/README.md @ de156192ce90
updated_at: '2026-09-14T01:58:51Z'
---

# 2389-research/tracker/README.md @ de156192ce90

<!-- rcw:begin owner=source:src_f5a5af977b98529a99d0e932a0b32ae7 block=evidence -->
- Secret inputs are staged to a 0600 file and ${inputs.<name>} resolves only to the path, so secret values never enter prompts, the provider wire, traces, or checkpoints. [@claim:clm_0033f403061d1fcd65a53659f6a29b0db8154a50c7f1e67c4b944c44290eb9d1]
- Workflows can declare environmental requirements via a requires: header line; as of v0.29.0 only git is checked, and unrecognized entries warn and continue. [@claim:clm_0c4d60a1490d8accd9e220c00e9b0f2b38c5b4addaaa71031528cc263ade3e99]
- Headless operation is supported via --webhook-url: human gates are POSTed as JSON and the pipeline resumes on callback, with flags for timeout, timeout action, and auth header. [@claim:clm_108f48d0af773248d06641ebeb5ba4e7569d86c768659edd76ee1edb39f410c3]
- Tracker targets teams running multi-agent LLM build/review pipelines, offering human gates, budget ceilings, audit trails, and front-ends for terminal, TUI, and Slack. [@claim:clm_1afe1f84d910bdc2750434ec146a76b632d9c4b508a0d8a8b6e4c2ccf6ac7a8a]
- The engine supports eight node types: agent, human gate, tool, parallel, fan_in, subgraph, manager_loop, and conditional. [@claim:clm_1b44954215456db181435ebd6f1d5594c5e9dee32ebc8974d1c33de4c2829bb8]
- Git artifact commits per terminal node outcome are enabled only via the library's WithGitArtifacts(true) option; the README states there is no CLI flag for this today. [@claim:clm_2ace9cc7463af402aed1ac779f0b4264c4d94066f742ef78cf6ca7acc379b71a]
- Each agent node runs a fresh LLM session; data flows between nodes via context keys (ctx.*, params.*, graph.*), not conversation history, with per-node scoping available. [@claim:clm_4452831a294aa151c7597473296fd2bfaec3d5fc41f4180a9e04161fdecbf0d3]
- Tracker supports four LLM providers: anthropic, openai, gemini, and openai-compat, configured via tracker setup or environment variables stored in ~/.config/2389/tracker/.env. [@claim:clm_501f196bd2976c0d357d8f4f5bc916c6a43edf2554e6c7391f1847534e5482da]
- Agent, tool, and interview nodes can declare writes:/reads: context keys; missing declared writes hard-fail the node, and reads: pins fidelity of upstream keys. [@claim:clm_5f8e67187f605287fceff8497556b07ba7cc355861fe2a5f7457e60b68fec3a0]
- All providers can be routed through Cloudflare AI Gateway via TRACKER_GATEWAY_URL or --gateway-url, with per-provider base-URL overrides taking precedence over the gateway. [@claim:clm_8069d8372df06538b2c1c7b3fde1e1f59c88207188e1dbe7bd42cfdb8de2f070]
- Variable expansion is single-pass so resolved values are never re-scanned, preventing recursive expansion; unknown --param keys hard-fail at startup. [@claim:clm_875620f8d8be213726cb6b23a92683f08dd62fbfe6931f5ebea93653520bb1d4]
- The superspec workflow includes per-phase mechanical quality gates (build, test, lint, coverage, complexity) and a final TraceabilityAudit gate verifying spec requirements map to implementation and test coverage. [@claim:clm_9ef92e1cb7f5544b14d523f0ec508e729692d4eb228be6885c7a2220c74047b6]
- Tracker is a three-layer stack: an LLM client with provider adapters, an agent session with turn loop and context compaction, and a pipeline engine with graph execution, checkpoints, and TUI. [@claim:clm_bafb075e18422d7b049382327a8b22195e3ad3626b9181d9175553aab650c188]
- The working_dir attribute for per-node working directories is validated against path traversal and shell metacharacters. [@claim:clm_c487bff315a8566467bfc106adaadce4e00114698e3688cec0f7c2ce292bd714]
- Human gates support five modes: choice, freeform, hybrid, yes/no, and interview, with interview answers stored as JSON plus a markdown summary. [@claim:clm_c76187eedf2a776c182839941f859ef5e0a4e2ecbb0e276d65e141e1f0c8dd79]
- The core engine is UI-agnostic: TUI, Slack bot, and terminal REPL are peers on one library boundary sharing a transport-neutral transport/chatops core. [@claim:clm_e8dd87589465e420d15b1242aea80672aa91435e6564d5169cce667669d5965c]
- Both build workflows run a SpecLint preflight (dangling refs, contradictory constants, contract mismatches) that fails closed before decomposition. [@claim:clm_ec3407f15420378be2f4267fbe90627330ac76ace1963f7a9270b87e0fe055db]
- Pipelines are defined in .dip files using the Dippin DSL, with workflow headers declaring goal, start, exit, defaults (model/provider), and edges between nodes. [@claim:clm_f34931e1a6a9ce2d1a87a7a94feb49fc536c11d46cab9276ef2c87e5699da537]
<!-- rcw:end owner=source:src_f5a5af977b98529a99d0e932a0b32ae7 block=evidence -->

## Researcher notes

