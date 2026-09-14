---
access: public
aliases: []
claim_ids:
- clm_10436225c91522b6d72002002493ca0b7f21522a857462ad0d3393858840b1af
- clm_431feadeb20e4f2b25dce59860e57404d1451dc2bd6695ab70ca0aa28d5a070c
- clm_61f99d2df2455d24385ff0fbbeeaa1665bbf1e6b721be2ffb5e7bb5dd9e7fe30
- clm_ff261e7a169eac0533978874ee0637e9d83797ec57b9a6b4343afaa2282743c8
maturity: draft
page_id: pg_3b0f3598dff8501b99df80124462dac6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c5748391262a51cab022cc676bb13071
title: aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/AGENTS.md @
  b48bcb476d08
updated_at: '2026-09-14T03:05:41Z'
---

# aws-samples/sample-multi-agent-orchestration-chat-on-agentcore/AGENTS.md @ b48bcb476d08

<!-- rcw:begin owner=source:src_c5748391262a51cab022cc676bb13071 block=evidence -->
- Repository development practice: the repo is an npm-workspaces monorepo of 8 packages using Node.js 22, TypeScript ~5.7, jest/vitest tests, eslint+prettier, and a solution-style tsc build that must run before cdk synth/deploy. [@claim:clm_10436225c91522b6d72002002493ca0b7f21522a857462ad0d3393858840b1af]
- The agent runs as a Docker container on AgentCore Runtime using the Strands Agents SDK (TypeScript), implemented as an Express server on port 8080. [@claim:clm_431feadeb20e4f2b25dce59860e57404d1451dc2bd6695ab70ca0aa28d5a070c]
- Real-time streaming is achieved via AppSync Events (WebSocket), and a session-stream-handler Lambda relays DynamoDB Streams to AppSync. [@claim:clm_61f99d2df2455d24385ff0fbbeeaa1665bbf1e6b721be2ffb5e7bb5dd9e7fe30]
- Repository development practice: CI runs secret scanning via detect-secrets through ASH, with test files excluded by globs in .ash/ash.yaml and documented pragma/ignore_paths handling for false positives. [@claim:clm_ff261e7a169eac0533978874ee0637e9d83797ec57b9a6b4343afaa2282743c8]
<!-- rcw:end owner=source:src_c5748391262a51cab022cc676bb13071 block=evidence -->

## Researcher notes

