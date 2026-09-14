---
access: public
aliases: []
claim_ids:
- clm_0d85643aa9a1e57c9eacfcdf428c0105778f73da45c25a8f5884689154bca12d
- clm_14f1267daeb9aba6d0d8d7c3057ab2b2c5453a70b8fa71beb8df5e33dbbfe526
- clm_16f2f5b82b5dd0c8ab65d06e539aa52ec5ea23410909087dbe525fb665cf459e
- clm_2233b28f31493d43a446a1e3d3f441fd4bb6ce6be439a17d0f365e8bdf855917
- clm_22ba5b0dab1a2e4cfe42b86a03446c8b1391c2b0866153642af31951c89754b6
- clm_4d8456a7bdea1e471b1eca58cea45863d16ee1800d51f7ab710dad780818adba
- clm_74a2d79d27f90e8ae497a0c9b7b46bddf0a6411c3d1c794edb77d5c2f6605623
- clm_8f4dd52f2e57e4405b71f542ad1c7ff7f0d2f534a5c10f105819d6700621cec8
- clm_cb4ba6a79e752df37187c870718302fc4d1e612ded6898a23aae7c647ca70db2
maturity: draft
page_id: pg_9ff093e85630550eb5bf1205f2baa894
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4c80b1181148552895c35aa40d72a657
title: withastro/flue/README.md @ 1ae1c85dae55
updated_at: '2026-09-14T03:23:56Z'
---

# withastro/flue/README.md @ 1ae1c85dae55

<!-- rcw:begin owner=source:src_4c80b1181148552895c35aa40d72a657 block=evidence -->
- The CLI exposes a `flue` binary for local runs, blueprints, and offline docs; @flue/sdk is a client SDK for consuming deployed agent conversations. [@claim:clm_0d85643aa9a1e57c9eacfcdf428c0105778f73da45c25a8f5884689154bca12d]
- The repository ships @flue/runtime (harness, sessions, tools, sandbox), @flue/vite (build plugin), @flue/cli (flue binary), @flue/sdk (client for deployed agent conversations), @flue/opentelemetry, and @flue/postgres. [@claim:clm_14f1267daeb9aba6d0d8d7c3057ab2b2c5453a70b8fa71beb8df5e33dbbfe526]
- Documented deployment targets include Node.js, Cloudflare Workers, GitHub Actions, GitLab CI/CD, and Render; Daytona appears as a sandbox option rather than a deployment target. [@claim:clm_16f2f5b82b5dd0c8ab65d06e539aa52ec5ea23410909087dbe525fb665cf459e]
- Agents can connect to authenticated tools and services through MCP servers, and telemetry can be exported via OpenTelemetry and Braintrust. [@claim:clm_2233b28f31493d43a446a1e3d3f441fd4bb6ce6be439a17d0f365e8bdf855917]
- The framework supports subagents: specialized roles can be defined for different tasks, and the agent can delegate work to the appropriate expert. [@claim:clm_22ba5b0dab1a2e4cfe42b86a03446c8b1391c2b0866153642af31951c89754b6]
- Agents keep context across conversations and events, and preserve progress through failures and restarts via durable recovery for accepted work. [@claim:clm_4d8456a7bdea1e471b1eca58cea45863d16ee1800d51f7ab710dad780818adba]
- Flue positions itself as a framework for autonomous agents that receive a task rather than pre-defined steps, contrasting with agents built from raw LLM API calls. [@claim:clm_74a2d79d27f90e8ae497a0c9b7b46bddf0a6411c3d1c794edb77d5c2f6605623]
- Agents are exported TypeScript functions marked with a 'use agent' directive; hooks like useModel, useSandbox, useSkill, and useTool compose capabilities, and the function's returned string is its instruction. [@claim:clm_8f4dd52f2e57e4405b71f542ad1c7ff7f0d2f534a5c10f105819d6700621cec8]
- The built-in TypeScript harness gives models sessions, tools, skills, instructions, filesystem access, and a secure sandbox; agents run locally via CLI or deploy to a hosted runtime. [@claim:clm_cb4ba6a79e752df37187c870718302fc4d1e612ded6898a23aae7c647ca70db2]
<!-- rcw:end owner=source:src_4c80b1181148552895c35aa40d72a657 block=evidence -->

## Researcher notes

