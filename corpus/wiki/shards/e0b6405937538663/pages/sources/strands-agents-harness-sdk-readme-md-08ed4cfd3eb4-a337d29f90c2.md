---
access: public
aliases: []
claim_ids:
- clm_3a98356aa9a0390d66d4c63dd8d9fa696be1cfbbeef5b30500eb0b712d42d176
- clm_46a8396e4030180a315d9c65774de6117a253a280d6d23af1fbd8521578fbedc
- clm_4bd8d53a4df2a3ec99c5caa037f41288f05c956b7434d534e7e8e4669fe27945
- clm_7e4f4ea495565e041471b73b7d868344c1a26582855938dd2fa51fd992be0330
- clm_ae57a5994f8bd2176772555ecdf0981db5d22912e45b959a8abfa1862f9a4947
- clm_b075c076ac554db140a78adcf2bd371507ad8240b1d94d004525cb90d964d5d7
- clm_e0599e473447529d8f7f81d8e0075ac5edc80ef89a63fe309fef74685d4b5d1f
- clm_fa43c72c94be5d058e1fd1403c454b534cd48de3fdb1317a5602006a86dcef5e
maturity: draft
page_id: pg_578b1698b38b552388e8a337d29f90c2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7e796086bcac5249b6de15675759c2b8
title: strands-agents/harness-sdk/README.md @ 08ed4cfd3eb4
updated_at: '2026-09-14T04:23:42Z'
---

# strands-agents/harness-sdk/README.md @ 08ed4cfd3eb4

<!-- rcw:begin owner=source:src_7e796086bcac5249b6de15675759c2b8 block=evidence -->
- The Python SDK requires Python 3.10+ and is installed via pip as strands-agents (with strands-agents-tools); the TypeScript SDK requires Node.js 22+ and installs as @strands-agents/sdk via npm. [@claim:clm_3a98356aa9a0390d66d4c63dd8d9fa696be1cfbbeef5b30500eb0b712d42d176]
- Repository development practice: Python SDK tests and formatting run via hatch test and hatch fmt in strands-py; the TypeScript SDK uses npm ci, npm run build, and npm test; the docs site runs with npm install and npm run dev in site/; git operations are done from the repo root. [@claim:clm_46a8396e4030180a315d9c65774de6117a253a280d6d23af1fbd8521578fbedc]
- Both SDKs default to the Amazon Bedrock model provider, requiring AWS credentials and model access for Claude Sonnet; other providers such as Anthropic, OpenAI, Gemini, and Ollama are covered in the quickstart. [@claim:clm_4bd8d53a4df2a3ec99c5caa037f41288f05c956b7434d534e7e8e4669fe27945]
- Repository development practice: contributions are guided by CONTRIBUTING.md covering bug reports, development setup, pull requests, code of conduct, and security issue reporting; doc PRs are welcome alongside code changes. [@claim:clm_7e4f4ea495565e041471b73b7d868344c1a26582855938dd2fa51fd992be0330]
- The SDK advertises built-in lifecycle controls (turn limits, token budgets, cancellation, stop reasons), tools, structured output, MCP, multi-agent patterns, memory, sessions, model portability, streaming, guardrails, tracing, and evals. [@claim:clm_ae57a5994f8bd2176772555ecdf0981db5d22912e45b959a8abfa1862f9a4947]
- The Python API exposes an Agent class constructed with a tools list and invoked by calling it with a prompt string; the TypeScript API exposes an Agent with an awaitable invoke(prompt) method. [@claim:clm_b075c076ac554db140a78adcf2bd371507ad8240b1d94d004525cb90d964d5d7]
- Strands Agents is an open-source SDK for building and running AI agents in Python and TypeScript, positioned as a replacement for a hand-rolled agent loop that runs in the user's process with no hosted control plane. [@claim:clm_e0599e473447529d8f7f81d8e0075ac5edc80ef89a63fe309fef74685d4b5d1f]
- The monorepo contains strands-py (Python SDK), strands-ts (TypeScript SDK), site (Astro/Starlight documentation site), and team (governance and cross-SDK process docs including designs/ proposals). [@claim:clm_fa43c72c94be5d058e1fd1403c454b534cd48de3fdb1317a5602006a86dcef5e]
<!-- rcw:end owner=source:src_7e796086bcac5249b6de15675759c2b8 block=evidence -->

## Researcher notes

