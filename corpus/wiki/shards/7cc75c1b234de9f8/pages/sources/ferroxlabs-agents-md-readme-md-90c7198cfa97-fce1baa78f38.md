---
access: public
aliases: []
claim_ids:
- clm_0bee21d4c1a943d8e5fbcc5658fdd0212ac01c21488daaef1438c899e02730bd
- clm_32434882651e7d69c01f8d46d31da00678ebb686836f8314bd5d788eff5fc964
- clm_4243351e15a8bc1abd623b66bd802be5cd708309686b2b476efb2b4504546421
- clm_9a0eae13936832cddff66283d9eb1e742adbfb8671bed378fe71c1b61969250c
- clm_b03094605754634cbd5a9c8f3d31c24f479d59399aa00d693440ca7806571e80
- clm_f52edcde04ee5121417c3e2b8676f5ee687af8d4e7cc712a7cf27605aa14b57f
maturity: draft
page_id: pg_02eb439cbb5951369e13fce1baa78f38
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_80241cbfc07a593fa532454065334e35
title: FerroxLabs/agents-md/README.md @ 90c7198cfa97
updated_at: '2026-09-14T03:50:05Z'
---

# FerroxLabs/agents-md/README.md @ 90c7198cfa97

<!-- rcw:begin owner=source:src_80241cbfc07a593fa532454065334e35 block=evidence -->
- The file is deliberately kept tight (about 200 lines per the README, with under 300 suggested as a ceiling) so rules stay loaded, and sections 0-9 are meant to be left untouched by users. [@claim:clm_0bee21d4c1a943d8e5fbcc5658fdd0212ac01c21488daaef1438c899e02730bd]
- The file targets the AGENTS.md open standard: tools like Codex, Cursor, Aider, Windsurf, Copilot, and Devin read it natively, while Claude Code and Gemini CLI require CLAUDE.md and GEMINI.md symlinks (or copies) pointing to it. [@claim:clm_32434882651e7d69c01f8d46d31da00678ebb686836f8314bd5d788eff5fc964]
- The template synthesizes Karpathy's four principles on LLM coding failure modes, Boris Cherny's Claude Code workflow with reactive pruning, Anthropic's Claude Code best practices, community anti-sycophancy patterns, and the AGENTS.md standard. [@claim:clm_4243351e15a8bc1abd623b66bd802be5cd708309686b2b476efb2b4504546421]
- For large codebases the README suggests sharding via Claude Code @-imports or .claude/rules with path frontmatter, or Cursor .cursor/rules with path scoping, while keeping a single AGENTS.md for other tools. [@claim:clm_9a0eae13936832cddff66283d9eb1e742adbfb8671bed378fe71c1b61969250c]
- Installation is documented two ways: an agent-driven prompt that fetches the raw file, symlinks CLAUDE.md/GEMINI.md, and fills section 10 from the codebase, or a manual curl download of AGENTS.md. [@claim:clm_b03094605754634cbd5a9c8f3d31c24f479d59399aa00d693440ca7806571e80]
- The repository's product is a single drop-in AGENTS.md file of operating instructions intended to be placed at any project's root and read by coding agents, released under the MIT license. [@claim:clm_f52edcde04ee5121417c3e2b8676f5ee687af8d4e7cc712a7cf27605aa14b57f]
<!-- rcw:end owner=source:src_80241cbfc07a593fa532454065334e35 block=evidence -->

## Researcher notes

