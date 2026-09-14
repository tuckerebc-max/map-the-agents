---
access: public
aliases: []
claim_ids:
- clm_0121697644bf3855c02ab40a15d01c565b26f7def740dba8c5afbf739366b089
- clm_16d43335a7bcd44660f219cba308ffe4536c5339080eb465f626b5022a30707c
- clm_5c22cc44217616e2d5d904e69206b0f7eb528f2deef6a42c5fe78b70315bbb12
- clm_728277689f0f0bdd63bc54d7630decaee69658e9775f2ae2ecda039be7b47c8a
- clm_c1032f0da4048c2d00d8e56ec33f93fb4488855e37ab4e527038043f5362a6d8
maturity: draft
page_id: pg_9aa16d85fd0a59e190c4e6896b63667f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7e76bd9a478b5249be9ef3af3bcfd83a
title: rizwan3d/StemCode/README.md @ dfe4dd789988
updated_at: '2026-09-14T02:36:28Z'
---

# rizwan3d/StemCode/README.md @ dfe4dd789988

<!-- rcw:begin owner=source:src_7e76bd9a478b5249be9ef3af3bcfd83a block=evidence -->
- Reusable commands live in `.stemcode/commands` and long-lived project knowledge in `.stemcode/memory`, stored as versionable files users can review and commit. [@claim:clm_0121697644bf3855c02ab40a15d01c565b26f7def740dba8c5afbf739366b089]
- The CLI binary is documented as self-contained and AOT-compiled, and all installers expose the same `stemcode` command from the same release assets. [@claim:clm_16d43335a7bcd44660f219cba308ffe4536c5339080eb465f626b5022a30707c]
- The product uses approval prompts, permissions, and profiles to keep actions under human control; `--sandbox-mode` overrides sandbox policy per run with read-only, workspace-write, or danger-full-access values. [@claim:clm_5c22cc44217616e2d5d904e69206b0f7eb528f2deef6a42c5fe78b70315bbb12]
- Release assets publish SHA256SUMS and GitHub artifact attestations; the release pipeline verifies each checksum before publishing, and `gh attestation verify` is documented for provenance checks. [@claim:clm_728277689f0f0bdd63bc54d7630decaee69658e9775f2ae2ecda039be7b47c8a]
- Subagents run delegated tasks with independent contexts to keep the main conversation focused, and interactive user questions support clarification, multiple-choice, multi-select, and free-form input. [@claim:clm_c1032f0da4048c2d00d8e56ec33f93fb4488855e37ab4e527038043f5362a6d8]
<!-- rcw:end owner=source:src_7e76bd9a478b5249be9ef3af3bcfd83a block=evidence -->

## Researcher notes

