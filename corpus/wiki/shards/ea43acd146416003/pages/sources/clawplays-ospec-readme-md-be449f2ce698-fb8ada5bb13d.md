---
access: public
aliases: []
claim_ids:
- clm_187a580e443fed83d8ec8d04543aa3c66af299e604742089d6cab1ecbfe60924
- clm_352968681cfa2367e1ff24d59f076e7548c600326245c2f2d57ba4a8573ecbe6
- clm_421f937769a97c599bc85b33a51831b0c120f1843776a7faa2669d71c13edd98
- clm_535d81ac10dd42283939d67bbe8a3802c52f58a5ffef8942983908e0594184b4
- clm_690d78b56edd195ea23e6842d51eb6a79d71ee900b654e926d7d9ef97ec8efca
- clm_7eb22274a8eba5983d1a7aaeba23bb697b6e7b22659e0f1f69afc962f7283da8
- clm_818b2e2423704a6aa8bc647b2f92a136fed3b61fec1f2ded9796a5e8a5d51545
- clm_a796981ee60e84ca41e06fe59ad0621945c0365da6c8af536304782ca498ffc2
- clm_b52fcbb7b99b1bc58515ceead6317cd0a3060f04f6e44ed9472e6648124d892b
- clm_d48f189365599463aed619dfbad38049d7431897bc643ff0d2a2b073cbdfa4c3
- clm_f9c3ec2ef15297ea60f536a96ccbcaa0923de8508eaabfd7453d8a58cb313cc2
- clm_faf06daf426b8ad16b358bb8f5f4c1a9a59324e34f8ccb9a977d40bb97a83865
maturity: draft
page_id: pg_e628c4a69deb5fc686f1fb8ada5bb13d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6a6d0f85439757af8b29f8420861244e
title: clawplays/ospec/README.md @ be449f2ce698
updated_at: '2026-09-14T03:40:58Z'
---

# clawplays/ospec/README.md @ be449f2ce698

<!-- rcw:begin owner=source:src_6a6d0f85439757af8b29f8420861244e block=evidence -->
- For Claude Code, `ospec session hook --target claude --apply` installs a hook bundle under .ospec/hooks/claude merged into .claude/settings.json that announces dispatches, hard-blocks subagent dispatch while a required decision is pending, and is Claude-only and opt-in. [@claim:clm_187a580e443fed83d8ec8d04543aa3c66af299e604742089d6cab1ecbfe60924]
- New projects initialized by `ospec init` default to a nested layout: root .skillrc and README.md with OSpec-managed files under .ospec/, while CLI shorthand like changes/active/<name> still resolves to .ospec/ paths. [@claim:clm_352968681cfa2367e1ff24d59f076e7548c600326245c2f2d57ba4a8573ecbe6]
- OSpec never launches agent CLIs as a fallback; if the harness lacks native subagents, executable dispatch blocks until a supported harness reports capability, and IDE controller dispatch fails clearly. [@claim:clm_421f937769a97c599bc85b33a51831b0c120f1843776a7faa2669d71c13edd98]
- Installation docs require Node.js >= 18 and npm >= 8, installed globally via npm install -g @clawplays/ospec-cli, verified with ospec --version / --help. [@claim:clm_535d81ac10dd42283939d67bbe8a3802c52f58a5ffef8942983908e0594184b4]
- Archiving writes an SKILL.index.json.archived_changes entry, refreshes docs/project/feature-catalog.md rows, and idempotently replaces ospec:last-change traceability comments — described as the engine's only write into human-owned documents, with comment failures warning rather than blocking. [@claim:clm_690d78b56edd195ea23e6842d51eb6a79d71ee900b654e926d7d9ef97ec8efca]
- `ospec init` accepts flags such as --summary, --tech-stack, --architecture, and --document-language (en-US, zh-CN, ja-JP, or ar) to shape generated project docs. [@claim:clm_7eb22274a8eba5983d1a7aaeba23bb697b6e7b22659e0f1f69afc962f7283da8]
- The goal controller dispatches native subagents per harness (Codex spawn_agent with bounded waits, Claude Code background Task polling, Gemini @generalist, OpenCode @mention), with 60-second poll boundaries, heartbeats, and immediate persistence of completed children. [@claim:clm_818b2e2423704a6aa8bc647b2f92a136fed3b61fec1f2ded9796a5e8a5d51545]
- Loop commands manage concurrency and recovery: `ospec loop tick` issues task/final reviews bound to the real reviewer executor, `loop configure` sets concurrency/budgets/limits, and `loop recover --force` expires only unfinished items after confirmed session or child loss. [@claim:clm_a796981ee60e84ca41e06fe59ad0621945c0365da6c8af536304782ca498ffc2]
- The chosen document language is persisted in .skillrc and reused for for-ai guidance, `ospec change`, and `ospec update`; CLI language resolution falls back through explicit flag, persisted settings, existing docs, then en-US. [@claim:clm_b52fcbb7b99b1bc58515ceead6317cd0a3060f04f6e44ed9472e6648124d892b]
- The official npm package is @clawplays/ospec-cli and the command is `ospec`; documented subcommands include init, change, goal, verify, finalize, session, execute, loop, docs, update, and layout migrate. [@claim:clm_d48f189365599463aed619dfbad38049d7431897bc643ff0d2a2b073cbdfa4c3]
- A user-selected Change stays a Change regardless of complexity or risk; the full goal workflow is entered via `ospec goal` or explicit opt-in, and the classic change flow has no controller layer or subagents. [@claim:clm_f9c3ec2ef15297ea60f536a96ccbcaa0923de8508eaabfd7453d8a58cb313cc2]
- Workflow state lives in repository artifacts: active changes hold proposal.md, tasks.md, state.json, verification.md, and review.md; goals add design.md, implementation-plan.md, task-graph.json, worker/reviewer/evidence artifacts, so later sessions can resume without replaying chat. [@claim:clm_faf06daf426b8ad16b358bb8f5f4c1a9a59324e34f8ccb9a977d40bb97a83865]
<!-- rcw:end owner=source:src_6a6d0f85439757af8b29f8420861244e block=evidence -->

## Researcher notes

