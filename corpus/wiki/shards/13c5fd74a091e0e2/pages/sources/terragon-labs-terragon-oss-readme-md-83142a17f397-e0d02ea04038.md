---
access: public
aliases: []
claim_ids:
- clm_09fa607ceb81ccc4a8b44c385ab92d5aee194654d77ba59c3e37f36a4fe8cf67
- clm_5d77f26f953f0469f28f0fdeb51fa9c2fc8dcac4185ab3bcec0691f6cc67e85a
- clm_80b5f11c0dcbfbf96324b30e75167c52f71866eb3f1095fd8c3d9a7c1cfb33be
- clm_a15105b67f635d6a2bf09b8b3d7a9f77367c3c5fbd7989c10208842137ea3794
- clm_a86c9e5a572778cabeeff1d8b431befc950957eb5541254c3e18b6294a47f1a2
- clm_ad6b837c7f991284a6be97ae872399956885b2d86bc86dba20e236ddf592f329
- clm_bfe2ae56a802f0a7298b7b4fbc9b5c1ce9430ebdd46d88432d6f1f691b4135de
- clm_c1c5a01a90d43b81498751c2f48461ded03005c665bca22a3dd20602ce3b5e79
maturity: draft
page_id: pg_ff3f6b9511c955daaff6e0d02ea04038
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b98c6b59adab5e4291b96d27db2ace43
title: terragon-labs/terragon-oss/README.md @ 83142a17f397
updated_at: '2026-09-14T03:18:49Z'
---

# terragon-labs/terragon-oss/README.md @ 83142a17f397

<!-- rcw:begin owner=source:src_b98c6b59adab5e4291b96d27db2ace43 block=evidence -->
- Repository development practice: local development requires Node.js 20+, pnpm 10.14.0+, Docker for PostgreSQL/Redis containers, and Stripe CLI for webhook forwarding; dependencies install via 'pnpm install'. [@claim:clm_09fa607ceb81ccc4a8b44c385ab92d5aee194654d77ba59c3e37f36a4fe8cf67]
- Terragon supports multiple coding agents—Claude Code, OpenAI Codex, Amp, and Gemini—and is designed so support for additional agents can be added. [@claim:clm_5d77f26f953f0469f28f0fdeb51fa9c2fc8dcac4185ab3bcec0691f6cc67e85a]
- Each agent runs in an isolated sandbox container with its own repository copy, letting it read files, edit, and run tests without affecting concurrent tasks or the local environment. [@claim:clm_80b5f11c0dcbfbf96324b30e75167c52f71866eb3f1095fd8c3d9a7c1cfb33be]
- The product ships a 'terry' CLI for local task takeover and continuation, plus an MCP server so MCP-compatible clients like Cursor and Claude Code can create and manage tasks. [@claim:clm_a15105b67f635d6a2bf09b8b3d7a9f77367c3c5fbd7989c10208842137ea3794]
- The product offers automations: recurring tasks or event-triggered workflows, such as triggers on new issues or pull requests, to automate repetitive development work. [@claim:clm_a86c9e5a572778cabeeff1d8b431befc950957eb5541254c3e18b6294a47f1a2]
- The repository is an as-is snapshot taken at Terragon's shutdown, with no guarantees of maintenance, support, or completeness. [@claim:clm_ad6b837c7f991284a6be97ae872399956885b2d86bc86dba20e236ddf592f329]
- Repository development practice: after schema changes, contributors push the Drizzle schema to the dev database with 'pnpm -C packages/shared drizzle-kit-push-dev', and 'pnpm dev' starts all development services. [@claim:clm_bfe2ae56a802f0a7298b7b4fbc9b5c1ce9430ebdd46d88432d6f1f691b4135de]
- Tasks get unique branches, and agent work is checkpointed to GitHub with AI-generated commits and pull requests; this git workflow can be disabled for flexibility. [@claim:clm_c1c5a01a90d43b81498751c2f48461ded03005c665bca22a3dd20602ce3b5e79]
<!-- rcw:end owner=source:src_b98c6b59adab5e4291b96d27db2ace43 block=evidence -->

## Researcher notes

