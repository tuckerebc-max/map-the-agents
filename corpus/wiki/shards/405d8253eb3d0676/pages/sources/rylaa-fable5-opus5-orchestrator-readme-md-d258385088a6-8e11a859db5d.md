---
access: public
aliases: []
claim_ids:
- clm_221141e91323ad3f5b8d977e19da2261483cca88a733979c39a6ca6050ffc5cc
- clm_31280e69718f5df695fe5f14463047bbca3f0c8d5b23dd326a5d2a1a48b99ac2
- clm_459044351bca2811a0f1dfeb503c5caa0e0326265ee2e55c37ab52d69aed1308
- clm_97747af4959536a2c1c823f2d435c265e86719947054d374d2222a38276fbaf4
- clm_9955ecbac2a8f4ebeaa9c17c3b54dc2ac955e614b2931da40be50086c2e95c8d
- clm_a5212a76b171883a4c28297660c2ab2ea8a5fae446d25a14c654af0cf19a3621
- clm_ba06ecc7b65c9a364f9f0774f58a48032389467a8c6a003b2058060e7603f031
- clm_c791faff4a0967f3417cc22b62fdcb2e412d9073f2a123d1212a2293e6065760
- clm_d0fcf10d2c3aa7937cd2ba83e241e5bd856c9eff75beeb3ff3d8f2b47d066e9b
- clm_d29c7fd00cf1f945a8873a01f38024bba530442e3921b71ef287ec0234d98cd2
- clm_d4f95ba1c01c5d2cb4e33f8f385b8bd985dd6104b5bf3714e3deb18be4929184
- clm_f58a7e45025e484b597c5e8d42d7b40d7ada39be61c782d88064b2acbdc2af13
maturity: draft
page_id: pg_88a53e5fd1b455d0a1d58e11a859db5d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b095d662063659d48d7654c5740e83f9
title: Rylaa/fable5-opus5-orchestrator/README.md @ d258385088a6
updated_at: '2026-09-14T02:37:43Z'
---

# Rylaa/fable5-opus5-orchestrator/README.md @ d258385088a6

<!-- rcw:begin owner=source:src_b095d662063659d48d7654c5740e83f9 block=evidence -->
- The hook validates the `## Clarified` record by four rules: every question has an `->` answer, no `Assumption:` line, at least one answered question, and a `Branch:` line; only plain bullets count, not fenced templates or HTML comments. [@claim:clm_221141e91323ad3f5b8d977e19da2261483cca88a733979c39a6ca6050ffc5cc]
- Repository development practice: tests run with `python3 -m pytest tests/ -q`; the hook tests execute the stdin/stdout JSON filters end to end as subprocesses, plus a second layer pinning the core text and the skill. [@claim:clm_31280e69718f5df695fe5f14463047bbca3f0c8d5b23dd326a5d2a1a48b99ac2]
- Finished teammates are reaped automatically at session end and on a rate-limited idle sweep (default 1-hour idle threshold); metrics go to ~/.claude/fable-orch/metrics.jsonl, summarized by `python3 scripts/stats.py`. [@claim:clm_459044351bca2811a0f1dfeb503c5caa0e0326265ee2e55c37ab52d69aed1308]
- Behavior is configurable via env vars under `"env"` in ~/.claude/settings.json: a 1500-char spawn threshold, per-gate disable flags, stop-gate frequency, metrics logging, and teammate reaping settings. [@claim:clm_97747af4959536a2c1c823f2d435c265e86719947054d374d2222a38276fbaf4]
- The hooks check record shape, not question fidelity, and enforcement depends on the host's hook pipeline, so users should verify behavior on their own setup. [@claim:clm_9955ecbac2a8f4ebeaa9c17c3b54dc2ac955e614b2931da40be50086c2e95c8d]
- Four hooks enforce the workflow: a PreToolUse clarify gate, a PreToolUse spawn gate, a task-list gate on the third ledgerless tracker task, and a Stop gate when a turn ends with open ledger items. [@claim:clm_a5212a76b171883a4c28297660c2ab2ea8a5fae446d25a14c654af0cf19a3621]
- The product is a Claude Code plugin installed via the marketplace commands `/plugin marketplace add Rylaa/fable5-opus5-orchestrator` and `/plugin install orchestrator@fable-orchestrator`. [@claim:clm_ba06ecc7b65c9a364f9f0774f58a48032389467a8c6a003b2058060e7603f031]
- Short spawns, forks, and teammates are never gated; a fully closed ledger from an earlier session does not disarm gates, and ledgers are retired by renaming to `LEDGER-<topic>-archive.md`. [@claim:clm_c791faff4a0967f3417cc22b62fdcb2e412d9073f2a123d1212a2293e6065760]
- The plugin needs `python3` on PATH, supports macOS and Linux only, and Claude Code must be restarted after installation. [@claim:clm_d0fcf10d2c3aa7937cd2ba83e241e5bd856c9eff75beeb3ff3d8f2b47d066e9b]
- The clarify protocol in skills/clarify/SKILL.md scans seven axes (scope edge, acceptance, constraints, decision ownership, priority conflicts, existing-code contact, failure behavior) and always asks whether work lands on the current branch or a new one. [@claim:clm_d29c7fd00cf1f945a8873a01f38024bba530442e3921b71ef287ec0234d98cd2]
- Sessions run as: chair reads the repo, asks all questions in rounds before planning, writes a ledger, then works directly or through workers; workers cannot ask the user anything. [@claim:clm_d4f95ba1c01c5d2cb4e33f8f385b8bd985dd6104b5bf3714e3deb18be4929184]
- Requirements are recorded as checkbox lines in `./.workflow/LEDGER.md` with open, done, and deferred-with-approval states; phases cite item numbers and discoveries are appended. [@claim:clm_f58a7e45025e484b597c5e8d42d7b40d7ada39be61c782d88064b2acbdc2af13]
<!-- rcw:end owner=source:src_b095d662063659d48d7654c5740e83f9 block=evidence -->

## Researcher notes

