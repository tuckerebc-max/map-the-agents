---
access: public
aliases: []
claim_ids:
- clm_4eeed67f2b747bac91d8ab0a57bb28e67e2edfd15908980909e8616f9f87b322
- clm_63470019199fb459e94688778d2d5cf473a165a29b46244bd1c6483577bf18ab
- clm_80ba83c198dd12aa94258ead07f7ab11e1776146ccdf5106a1007bd3327c6a49
- clm_978e141d0d07d924837d6d0a5c2b86cf3fa1ab82d255df2f1798a70065814dd7
- clm_a58e8eaee8334719b99217a3f63915e68acb3b095d8746994191b068438f4ff4
- clm_b4a00f426526a8ad4e7518f64e7bcd209f3c74ae5849c63fb03653c32557253d
- clm_e346a1d4a0395511577bc30bac2c041e19115129e06445354f0e46abfd4b2992
- clm_e46f7d6556cc28f2fb3c5fb8ffa73055e5e8b853e388f56dd02376d78ba6fdbf
maturity: draft
page_id: pg_f7fac61cfb59583192b043a931e9dab3
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c1959eb23df459bbaef76a633b424a65
title: alex-reysa/singular-lite/README.md @ 0f92cba1fb1f
updated_at: '2026-09-14T02:48:44Z'
---

# alex-reysa/singular-lite/README.md @ 0f92cba1fb1f

<!-- rcw:begin owner=source:src_c1959eb23df459bbaef76a633b424a65 block=evidence -->
- An agent-tiers table documents three roles: an L0 origin scheduler that runs the reconcile cycle, L1 area planners that stage batches of tasks per DAG node, and L2 workers that execute one task per isolated git worktree and produce a state packet for review. [@claim:clm_4eeed67f2b747bac91d8ab0a57bb28e67e2edfd15908980909e8616f9f87b322]
- After each worker run, a configured gate command's result feeds an auditor model, and a decider maps the failure class and remaining retries to a recovery action - retry, amend-scope, escalate, or park - via a deterministic table before any model round-trip. [@claim:clm_63470019199fb459e94688778d2d5cf473a165a29b46244bd1c6483577bf18ab]
- Documentation states that gates and audit checks stay identical across every session-routing strategy, and that any outcome improvement from session continuity is measured rather than assumed, via per-strategy results recorded in an attempts index and a metrics command. [@claim:clm_80ba83c198dd12aa94258ead07f7ab11e1776146ccdf5106a1007bd3327c6a49]
- The docs state an independence pin that always runs final-audit, paired-audit, re-critique, and critic-recheck fresh, regardless of session-routing settings, so no configuration lets an auditor grade work from a session that already formed an opinion on it. [@claim:clm_978e141d0d07d924837d6d0a5c2b86cf3fa1ab82d255df2f1798a70065814dd7]
- The README describes singular as a bash and Python orchestration engine that runs autonomous AI coding agents in parallel across a repository, using a three-tier scheduling model of an origin loop, area planners, and worker agents with git-worktree isolation. [@claim:clm_a58e8eaee8334719b99217a3f63915e68acb3b095d8746994191b068438f4ff4]
- Each reconcile cycle is documented as five ordered steps: importing staged task proposals, recovering stale leases, integrating completed worker branches, dispatching new tasks, and writing a state snapshot. [@claim:clm_b4a00f426526a8ad4e7518f64e7bcd209f3c74ae5849c63fb03653c32557253d]
- With detached dispatch on by default, reconcile pre-leases frontier tasks and spawns each worker in its own session, returning quickly; a separate reaper process later attributes completions, failures, and crashes from dispatch records and worker exit files. [@claim:clm_e346a1d4a0395511577bc30bac2c041e19115129e06445354f0e46abfd4b2992]
- Documented install prerequisites are Bash 4+, Python 3, Git, and one supported runner CLI on PATH; the shipped runner adapters listed are for codex, claude, gemini, opencode, cursor, openrouter, and grok. [@claim:clm_e46f7d6556cc28f2fb3c5fb8ffa73055e5e8b853e388f56dd02376d78ba6fdbf]
<!-- rcw:end owner=source:src_c1959eb23df459bbaef76a633b424a65 block=evidence -->

## Researcher notes

