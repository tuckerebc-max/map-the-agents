---
access: public
aliases: []
claim_ids:
- clm_565f1f6b30a56a95b108c0d90ba45bfa03bc0058668e6c298ba88e5e6ac64f17
- clm_6e150bab3f132cd8b409bce5ecfe7c57b5095e48415595db98c8570f40b6aaad
- clm_c442d7274061534187febb62c8bcc2de7ab3f4016a616cb8b9b02a4722b231a8
maturity: draft
page_id: pg_7159ddafc40a54dfb1ddf6973129b838
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c92c8c521109535b81a3df13e694aa11
title: openchamber/openchamber/AGENTS.md @ 1636fd2bf8e4
updated_at: '2026-09-14T03:11:17Z'
---

# openchamber/openchamber/AGENTS.md @ 1636fd2bf8e4

<!-- rcw:begin owner=source:src_c92c8c521109535b81a3df13e694aa11 block=evidence -->
- Repository development practice: AGENTS.md mandates loading every matching project skill and nearest DOCUMENTATION.md before editing, treats skill loading as required rather than optional, and requires stopping to resolve conflicts between guidance sources. [@claim:clm_565f1f6b30a56a95b108c0d90ba45bfa03bc0058668e6c298ba88e5e6ac64f17]
- OpenChamber uses OpenCode to run coding agents, calling official OpenCode APIs through @opencode-ai/sdk/v2; the CLI/Web and VS Code surfaces use the user's installed OpenCode CLI. [@claim:clm_6e150bab3f132cd8b409bce5ecfe7c57b5095e48415595db98c8570f40b6aaad]
- Repository development practice: contributors validate changes with package.json scripts, run 'bun run dead-code' after file/export changes, and run 'bunx oxlint' with a vendored anti-slop plugin on new or substantially rewritten TypeScript files. [@claim:clm_c442d7274061534187febb62c8bcc2de7ab3f4016a616cb8b9b02a4722b231a8]
<!-- rcw:end owner=source:src_c92c8c521109535b81a3df13e694aa11 block=evidence -->

## Researcher notes

