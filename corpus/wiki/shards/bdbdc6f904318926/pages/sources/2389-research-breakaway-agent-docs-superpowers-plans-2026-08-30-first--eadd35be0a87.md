---
access: public
aliases: []
claim_ids:
- clm_1c8c7de48fd125368cd9eb1d20e7d8bb28a1094fc3e217e006d9487a1efc8cf4
- clm_cd29cd1d6a68a4dfdc276cb6a7ec06cc2f9a19a40599417d5974e2509b806e31
- clm_def100601a9493d34fb9b469aae6b38d92d41ab5fea815d780066a84f748203d
- clm_e067d5adb55ab124b76bb7a40a282b8115fe72135021c5ba8a824b36a6bbe04f
maturity: draft
page_id: pg_275087378f4b55248041eadd35be0a87
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d239a3e42d285207a0238fa49a08690e
title: 2389-research/breakaway-agent/docs/superpowers/plans/2026-08-30-first-class-binary.md
  @ a426c399d50f
updated_at: '2026-09-14T01:25:59Z'
---

# 2389-research/breakaway-agent/docs/superpowers/plans/2026-08-30-first-class-binary.md @ a426c399d50f

<!-- rcw:begin owner=source:src_d239a3e42d285207a0238fa49a08690e block=evidence -->
- The plan's architecture detects compiled-binary mode via import.meta.dir starting with /$bunfs/, redirecting system prompt, transcripts, and spawn commands to writable paths while leaving source mode untouched. [@claim:clm_1c8c7de48fd125368cd9eb1d20e7d8bb28a1094fc3e217e006d9487a1efc8cf4]
- The project targets Bun (bun install, bun src/index.ts, bun build --compile producing a ~61 MB self-contained binary); the plan lists Bun 1.3.14 and TypeScript as the tech stack. [@claim:clm_cd29cd1d6a68a4dfdc276cb6a7ec06cc2f9a19a40599417d5974e2509b806e31]
- Repository development practice: the implementation plan mandates TDD (write failing test, verify failure, implement, verify pass), conventional commits with a Claude-Session trailer, bun test staying green (80+ tests), no mocks of own code, stdout purity, and .env never committed or printed. [@claim:clm_def100601a9493d34fb9b469aae6b38d92d41ab5fea815d780066a84f748203d]
- Repository development practice: the plan document instructs agentic workers to use superpowers:subagent-driven-development or superpowers:executing-plans to implement tasks with checkbox tracking. [@claim:clm_e067d5adb55ab124b76bb7a40a282b8115fe72135021c5ba8a824b36a6bbe04f]
<!-- rcw:end owner=source:src_d239a3e42d285207a0238fa49a08690e block=evidence -->

## Researcher notes

