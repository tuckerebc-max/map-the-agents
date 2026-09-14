---
access: public
aliases: []
claim_ids:
- clm_299b02a28a04a22a8d1899315b7f5e269d999b5c95cc6b8c92d917f41d7291f7
- clm_934e9e18c7bd22d1559d3aefd58ec9588af109b3e7c571cc3989b1aaf2913b59
- clm_d785aa05f215d45edd20d83d152e0f7684e0a30720182dd5450024b76f8ca9cc
maturity: draft
page_id: pg_48c93b476758500087cad57d4621eff5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_42ecbf7ebe8651c3a22a37c96b76109d
title: MagicCube/helixent/docs/code-convention.md @ 5cc1fb3faf29
updated_at: '2026-09-14T02:15:19Z'
---

# MagicCube/helixent/docs/code-convention.md @ 5cc1fb3faf29

<!-- rcw:begin owner=source:src_42ecbf7ebe8651c3a22a37c96b76109d block=evidence -->
- The OpenAI provider defaults to temperature 0 and top_p 0, merges caller options last, and works with any OpenAI-compatible endpoint; thinking content is dropped when converting messages to OpenAI wire format. [@claim:clm_299b02a28a04a22a8d1899315b7f5e269d999b5c95cc6b8c92d917f41d7291f7]
- The stack uses TypeScript strict/ESM on the Bun runtime, Zod for schemas, the OpenAI SDK, Ink with React 19 for the TUI, Commander for the CLI, and gray-matter plus yaml for skills parsing. [@claim:clm_934e9e18c7bd22d1559d3aefd58ec9588af109b3e7c571cc3989b1aaf2913b59]
- Repository development practice: docs/bun.md instructs contributors to default to Bun (bun test, bun install, Bun.file, Bun.serve) and avoid Node/dotenv/express equivalents; docs/code-convention.md mandates kebab-case files, named exports only, _-prefixed private members, and layered dependency direction (agent stays generic; adapters live in community/). [@claim:clm_d785aa05f215d45edd20d83d152e0f7684e0a30720182dd5450024b76f8ca9cc]
<!-- rcw:end owner=source:src_42ecbf7ebe8651c3a22a37c96b76109d block=evidence -->

## Researcher notes

