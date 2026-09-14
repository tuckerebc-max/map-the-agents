---
access: public
aliases: []
claim_ids:
- clm_0c3d655cc8da39df988898bf2762492a5a7366ac063243388f8af8622853351c
- clm_46020c87fe9e583359f2f757c200b53ff09d372ed450381b9b2d70410d2123e4
- clm_6d5dbae82c73711ab5230e04e374ac3d97233304aff66398d5f5a2867f2f7d5a
- clm_8f04bee140652d5709f0620afb3e0aa6e6dd82eed9715c3ab9084056ad4746ef
- clm_9ac30038584937f8777a79e6bdfbf103fcd8c526b53aa592e586896916ed5d3e
- clm_9d40d4d6f8200614834eb2f1e31aefeb44a2cfa513adc2151e211443db498edc
- clm_abd15c7722d159cbbdb92933104dd0a95eea5618208fcabd6db94924474f1f65
- clm_af1c9de4d49fbf9c5348cf643f93d97bc44563485a9aed5a90cb827ff5bf346a
- clm_c959748cf46bb5ab3531ea2a4dcb6b933f5bc57f113433b0f7e3fb67950407be
- clm_fc13f5b7ffcb9ed5fb15c552d81feb0bf2f192f6df1dc5d41b6039f454f3de71
maturity: draft
page_id: pg_4753b9e158e35f6683c5aaf46db6448c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_894a3453ecb25793b2490f76a7f4712a
title: Larens94/codedna/README.md @ b3fe577b47c9
updated_at: '2026-09-14T04:05:04Z'
---

# Larens94/codedna/README.md @ b3fe577b47c9

<!-- rcw:begin owner=source:src_894a3453ecb25793b2490f76a7f4712a block=evidence -->
- Header comment syntax adapts to the language: PHP/TS/Go use //, Python uses docstrings, Ruby uses #, and Blade uses {{-- --}}. [@claim:clm_0c3d655cc8da39df988898bf2762492a5a7366ac063243388f8af8622853351c]
- The docs state these are historical results whose raw run artifacts are not included in the checkout, so CI does not claim to reproduce the numerical advantage; versioned traces and a reproduction command are required first. [@claim:clm_46020c87fe9e583359f2f757c200b53ff09d372ed450381b9b2d70410d2123e4]
- codedna install creates a .codedna directory, installs a Git pre-commit gate, and adds the selected agent's instruction file while preserving existing instruction files and hooks. [@claim:clm_6d5dbae82c73711ab5230e04e374ac3d97233304aff66398d5f5a2867f2f7d5a]
- The CLI is installed via pipx and requires Python 3.11+; non-Python language adapters rely on tree-sitter, while Swift and VB.NET use structural parsers. [@claim:clm_8f04bee140652d5709f0620afb3e0aa6e6dd82eed9715c3ab9084056ad4746ef]
- Python is described as the most tested language; non-Python adapters have seen less real-world usage, and users are asked to report wrong exports or header format issues. [@claim:clm_9ac30038584937f8777a79e6bdfbf103fcd8c526b53aa592e586896916ed5d3e]
- The protocol embeds structured header fields in source files: exports, used_by (importers, with [cascade] markers), related (semantic links without imports), rules, wiki pointers, and agent messages with model and date. [@claim:clm_9d40d4d6f8200614834eb2f1e31aefeb44a2cfa513adc2151e211443db498edc]
- The product exposes a CLI with commands including init, update, refresh, check, verify, impact, doctor, manifest, mode, install, and wiki bootstrap/sync, all of which auto-detect languages. [@claim:clm_abd15c7722d159cbbdb92933104dd0a95eea5618208fcabd6db94924474f1f65]
- An optional post-commit wiki-sync hook regenerates docs/codedna-wiki.md after each commit; it is non-blocking (failures silenced) and never overwrites an existing hook, looking for a CodeDNA marker instead. [@claim:clm_af1c9de4d49fbf9c5348cf643f93d97bc44563485a9aed5a90cb827ff5bf346a]
- A Claude Code plugin exposes slash commands (/codedna:init, /codedna:check, /codedna:manifest, /codedna:impact) as an alternative to the CLI for Claude Code users. [@claim:clm_c959748cf46bb5ab3531ea2a4dcb6b933f5bc57f113433b0f7e3fb67950407be]
- codedna install supports a --tools flag selecting integrations for agents such as claude, codex, opencode, aider, cursor, copilot, cline, windsurf, roo, and agents, writing the corresponding instruction files and hooks. [@claim:clm_fc13f5b7ffcb9ed5fb15c552d81feb0bf2f192f6df1dc5d41b6039f454f3de71]
<!-- rcw:end owner=source:src_894a3453ecb25793b2490f76a7f4712a block=evidence -->

## Researcher notes

