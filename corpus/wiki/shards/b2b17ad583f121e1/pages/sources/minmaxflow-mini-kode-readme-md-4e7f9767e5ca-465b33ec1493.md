---
access: public
aliases: []
claim_ids:
- clm_3aaaea4b807d6829794feefd46d3307d895f33cc04947fcab1c8980a585b4c59
- clm_467610794cd570914ad7fa3d29a8b0b9a7858bbf3e12a63e16003682ebe666d1
- clm_6bebbfd61415de1e5ffd3c2b8c85679817ce5c32aa9a46770d4ed7966a45bcf7
- clm_6d075132f9e58ed6762d8b91f0ac3e3ed32c316667dd24b1ebb803328d36e951
- clm_a197315229be7f96ae0ed94d5d88c1fcb4a9fec023d54b3288d0dcc9b2d90f40
- clm_c3649298ba9da2533f28f9ede6f9978cea6b396827167b5ebe57d8d496e91b0a
- clm_c61821c4f771d452eace373afe4c8cd1a79f36c8cea2dbbeba779dc514c41634
- clm_d696de5cdfec1c7f0ba4c5e8e7aee777e5371c59338095e8c10424bcdcb100fb
maturity: draft
page_id: pg_b1abd69b96295f9bb979465b33ec1493
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4a8ec1d2c7085a37bf89c1ad5a1143f2
title: minmaxflow/mini-kode/README.md @ 4e7f9767e5ca
updated_at: '2026-09-14T02:19:14Z'
---

# minmaxflow/mini-kode/README.md @ 4e7f9767e5ca

<!-- rcw:begin owner=source:src_4a8ec1d2c7085a37bf89c1ad5a1143f2 block=evidence -->
- The source tree is organized into modules for tools, Ink-based UI, LLM client, permissions, config, CLI, agent logic, sessions, and shared utilities. [@claim:clm_3aaaea4b807d6829794feefd46d3307d895f33cc04947fcab1c8980a585b4c59]
- LLM access is configured via environment variables including DEEPSEEK_API_KEY, GLM_API_KEY, OPENAI_API_KEY, and generic MINIKODE_API_KEY/BASE_URL/MODEL variables; DeepSeek and GLM are noted as tested and verified. [@claim:clm_467610794cd570914ad7fa3d29a8b0b9a7858bbf3e12a63e16003682ebe666d1]
- The system reads an AGENTS.md file from the project root and includes it in system prompts, providing persistent project context across sessions that users can edit. [@claim:clm_6bebbfd61415de1e5ffd3c2b8c85679817ce5c32aa9a46770d4ed7966a45bcf7]
- The documented tech stack includes TypeScript, pnpm, Ink for the terminal UI, OpenAI SDK for LLM integration, Vitest for testing, Zod for runtime validation, and Commander for the CLI. [@claim:clm_6d075132f9e58ed6762d8b91f0ac3e3ed32c316667dd24b1ebb803328d36e951]
- Mini-Kode is an educational project to help developers understand modern coding-agent architecture, described as a complete yet manageable implementation of about 14K lines of production code. [@claim:clm_a197315229be7f96ae0ed94d5d88c1fcb4a9fec023d54b3288d0dcc9b2d90f40]
- No agent-performance evaluation or benchmark harness appears in the provided evidence; the only test-related material is the repository's own Vitest test command, so evaluation capability remains unknown. [@claim:clm_c3649298ba9da2533f28f9ede6f9978cea6b396827167b5ebe57d8d496e91b0a]
- The product is invoked as the mini-kode command; it supports an interactive mode (bare command) and a non-interactive mode that executes a task supplied as a quoted argument. [@claim:clm_c61821c4f771d452eace373afe4c8cd1a79f36c8cea2dbbeba779dc514c41634]
- Repository development practice: contributors need Bun and pnpm, install with pnpm install, and use pnpm run dev, pnpm run build, and pnpm run test for development, building, and testing. [@claim:clm_d696de5cdfec1c7f0ba4c5e8e7aee777e5371c59338095e8c10424bcdcb100fb]
<!-- rcw:end owner=source:src_4a8ec1d2c7085a37bf89c1ad5a1143f2 block=evidence -->

## Researcher notes

