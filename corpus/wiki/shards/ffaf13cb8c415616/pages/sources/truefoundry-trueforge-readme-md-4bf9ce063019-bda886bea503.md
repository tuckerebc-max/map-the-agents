---
access: public
aliases: []
claim_ids:
- clm_093f811e18a7a7f0a85629e6a9f7dfe7f85aea0d18e7165abdfff6ff2958ce65
- clm_20253b23d80da82a0ea8f881cc79829cbf1b3a0bd160debad7f942525bb80008
- clm_6a0415fe45b851d4d066d9d809f8b1428afe6f9cb9252e534806fae6db2c95d4
- clm_78f9d7a12d59986c836ec66817d65ddd1827c03778fd1fc146ce118a18081657
- clm_7b4d2344119d1b2a05de17c62ee1d9f80c5d801f6e2c39e7e3c00a1e43fab86c
- clm_8bd2e81d588e3eca3a493ebabda623dc68d2b006af856c2a343748598d1772f6
- clm_99f4b979158eba961984bec1d22ca7c98a82f33ec9ed483588a9a68f4eab5fd6
maturity: draft
page_id: pg_86953f47754850dcad65bda886bea503
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7bbdab5e2b995489b8288bd030c53b41
title: truefoundry/trueforge/README.md @ 4bf9ce063019
updated_at: '2026-09-14T03:19:56Z'
---

# truefoundry/trueforge/README.md @ 4bf9ce063019

<!-- rcw:begin owner=source:src_7bbdab5e2b995489b8288bd030c53b41 block=evidence -->
- Repository development practice: fork PRs should change source only while maintainers regenerate the SDK after merge; releases use Changesets on main, npm trusted publishing via OIDC (no NPM_TOKEN), and a chart-release pipeline triggered after the trueforge npm publish. [@claim:clm_093f811e18a7a7f0a85629e6a9f7dfe7f85aea0d18e7165abdfff6ff2958ce65]
- TrueForge is an open-source agent harness that runs the agent execution loop (model calls, MCP tools, skills, sandboxing, approvals, context management, session state) and exposes it as a chat UI, an HTTP API with a TypeScript SDK, and an embeddable UI SDK. [@claim:clm_20253b23d80da82a0ea8f881cc79829cbf1b3a0bd160debad7f942525bb80008]
- The harness provides context-engineering features including subagents, deferred tool loading, Code Mode, large-result offloading, and compaction, plus human checkpoints such as tool approval, ask-user-questions, and Generative UI in chat. [@claim:clm_6a0415fe45b851d4d066d9d809f8b1428afe6f9cb9252e534806fae6db2c95d4]
- The project requires Node.js >= 22.14, is MIT-licensed, and its Helm chart bundles optional Bitnami Postgres and Redis subcharts that can be disabled via postgresql.enabled=false / redis.enabled=false. [@claim:clm_78f9d7a12d59986c836ec66817d65ddd1827c03778fd1fc146ce118a18081657]
- MCP tool connectivity supports remote servers with header auth or OAuth, including in-chat authorization; sandbox provider configuration requires a Daytona API key with snapshot-create permission, and the sandbox is off by default per agent. [@claim:clm_7b4d2344119d1b2a05de17c62ee1d9f80c5d801f6e2c39e7e3c00a1e43fab86c]
- TrueForge runs in local mode (single process, SQLite, no login by default, intended for localhost only) or hosted mode (Postgres + Redis) deployable via Docker Compose, Helm, or Railway. [@claim:clm_8bd2e81d588e3eca3a493ebabda623dc68d2b006af856c2a343748598d1772f6]
- The README reports benchmarks comparing TrueForge against Claude Managed Agents and deepagents on the same tasks, tools, and model, claiming equal accuracy at lower cost, with reproduction materials in the benchmark/ directory. [@claim:clm_99f4b979158eba961984bec1d22ca7c98a82f33ec9ed483588a9a68f4eab5fd6]
<!-- rcw:end owner=source:src_7bbdab5e2b995489b8288bd030c53b41 block=evidence -->

## Researcher notes

