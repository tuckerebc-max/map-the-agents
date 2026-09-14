---
access: public
aliases: []
claim_ids:
- clm_145c33522168cc284258373d32434168b837495710c485a2d0ecd8b95afdd875
- clm_205b0e1a8111b89503e077dfbb8d7b762402da47160c69f2177fa607c9d85fd3
- clm_2816fd116f916e5b4adf0a8556f7e60ac4c7b86726782e79afb1ea15b0bc14e6
- clm_29f46a03d925b4567f47fc4931dd2c636a63ea9f128f94181ad41691c6f50993
- clm_2d6dd0ab5e611300c1a92caa6e9b6525f3d86e81ba2bffa96fba69324d4bba49
- clm_9060f631018ed27b9ac2225de8a1cccd5c0d58175a87eb11a7cb5f1e24d030ee
- clm_ac9550387728feff74be59e29008398aca2aeacbc2bd2c0a69a426744737d847
- clm_b99f1129c3802c5c3b40c8c65f3807c3c9bbbcfd63a5286de4544b2f5a3088b7
maturity: draft
page_id: pg_db4f06964b5b5c47b9c73ac97ff0c3d6
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_eae8f519e4065db1ab478c4d06e3dd07
title: CodebuffAI/freebuff/README.md @ 654a906e6758
updated_at: '2026-09-14T03:40:43Z'
---

# CodebuffAI/freebuff/README.md @ 654a906e6758

<!-- rcw:begin owner=source:src_eae8f519e4065db1ab478c4d06e3dd07 block=evidence -->
- Freebuff ships five products: Desktop (parallel local agents), CLI, Web (full-stack app building), Cloud (agents on GitHub repos), and Chat. [@claim:clm_145c33522168cc284258373d32434168b837495710c485a2d0ecd8b95afdd875]
- Freebuff uses specialized agents rather than one model and prompt; agents gather context, plan, edit, research, run tools, and review results. [@claim:clm_205b0e1a8111b89503e077dfbb8d7b762402da47160c69f2177fa607c9d85fd3]
- The Muse Spark 1.2 model is rate limited and shared by all users, so it queues when busy and answers on DeepSeek V4 Flash instead of making users wait. [@claim:clm_2816fd116f916e5b4adf0a8556f7e60ac4c7b86726782e79afb1ea15b0bc14e6]
- The CLI is installed globally via npm and run with the 'freebuff' command inside a project directory. [@claim:clm_29f46a03d925b4567f47fc4931dd2c636a63ea9f128f94181ad41691c6f50993]
- Users outside supported regions and VPN users get limited access, restricted to GLM 5.3 Flash, DeepSeek V4.1 Flash, MiMo 2.5, and Solar Pro 4. [@claim:clm_2d6dd0ab5e611300c1a92caa6e9b6525f3d86e81ba2bffa96fba69324d4bba49]
- The repository is a TypeScript monorepo built with Bun, and local development requires Docker and a configured .env.local. [@claim:clm_9060f631018ed27b9ac2225de8a1cccd5c0d58175a87eb11a7cb5f1e24d030ee]
- Repository development practice: contributors clone, run 'bun install' and 'bun up', start the CLI with 'bun start-cli', and consult the contributing, development, and testing guides before opening a PR. [@claim:clm_ac9550387728feff74be59e29008398aca2aeacbc2bd2c0a69a426744737d847]
- Freebuff is built on the Codebuff open multi-agent framework, which powers its orchestration, tools, and SDK; custom agents can use @codebuff/sdk. [@claim:clm_b99f1129c3802c5c3b40c8c65f3807c3c9bbbcfd63a5286de4544b2f5a3088b7]
<!-- rcw:end owner=source:src_eae8f519e4065db1ab478c4d06e3dd07 block=evidence -->

## Researcher notes

