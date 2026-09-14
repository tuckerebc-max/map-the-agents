---
access: public
aliases: []
claim_ids:
- clm_081ef3c5eb9b1353da916b373f3648a5b174b903adc88474ae04ad6062cb7ae6
- clm_12aab05b3b2550f770c5cc2bdf91244b629d5986ddf2e8eee126c5f57285f87f
- clm_1d9ede3bdb71359c304722ebf12833eae9e6e08d7667dd74c7186cd2c28a4d1a
- clm_336d49c8f2fd8b9e537bf891e30a061b30c4c13ca93ab6cdca2694fefc169a62
- clm_5db5de085a051b95c994193a9d557fcface3741461a1bc2cf93b02cf985067b5
- clm_80d97e2f431a312847f8eea4efa9a659b7c2964a4ad53fba526284b96386bba7
- clm_8d654b0e9ae9a8452f2c1abbb956a698063c87c2fc677fbebb6d073683e9cbb4
- clm_a34ca7be637b13d909aef57592040cf966f4027b92dd1861863a36839dae0ef0
- clm_bf1dea5425fa0402ae0d898bce0423797394e7b2d18b8d4d6f92998194082f44
- clm_c737d3f8bdb7d62887074d3cb1e00d4b1dcc0f4dc9fa838db7c0bf05257a3815
- clm_c823a96cae53118e686fd8a8e57cab5c4377e9707e5e7788223aee602bc2da8c
maturity: draft
page_id: pg_d0528f51be5d5f94b0717abd7fe4c9a5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7a72052a02cd5032b888579c9b517a59
title: nicepkg/auto-company/README.md @ 125292073565
updated_at: '2026-09-14T04:11:44Z'
---

# nicepkg/auto-company/README.md @ 125292073565

<!-- rcw:begin owner=source:src_7a72052a02cd5032b888579c9b517a59 block=evidence -->
- The runtime charter grants agents all terminal tools (gh, wrangler, git, node/npm, uv/python, curl/jq listed as available) with hard safety red lines: no repo deletion, no wrangler delete, no deleting system files, no credential leaks, no force-push to main/master, and new projects must live under projects/. [@claim:clm_081ef3c5eb9b1353da916b373f3648a5b174b903adc88474ae04ad6062cb7ae6]
- Six standard collaboration chains are defined (new product evaluation, feature development, launch, pricing, weekly review, opportunity discovery), and convergence rules force concrete output: cycle 1 brainstorm, cycle 2 GO/NO-GO pre-mortem, and from cycle 3 onward pure discussion is forbidden. [@claim:clm_12aab05b3b2550f770c5cc2bdf91244b629d5986ddf2e8eee126c5f57285f87f]
- Users control the loop through make targets: start, start-awake, stop, status, monitor, last, cycles, awake, install/uninstall (launchd daemon), pause, and resume. [@claim:clm_1d9ede3bdb71359c304722ebf12833eae9e6e08d7667dd74c7186cd2c28a4d1a]
- The product is described as a fully autonomous AI company of 14 agents that conceives products, makes decisions, writes code, deploys, and markets with no human involvement, driven by Claude Code Agent Teams. [@claim:clm_336d49c8f2fd8b9e537bf891e30a061b30c4c13ca93ab6cdca2694fefc169a62]
- A launchd-managed auto-loop.sh runs an endless cycle: read PROMPT.md and consensus.md, drive one work period via `claude -p`, then handle failures (rate-limit waits, circuit breaker, consensus rollback) and sleep before the next round. [@claim:clm_5db5de085a051b95c994193a9d557fcface3741461a1bc2cf93b02cf985067b5]
- The repo ships 14 agent persona definitions under .claude/agents (e.g. ceo-bezos, cto-vogels, critic-munger, fullstack-dhh, qa-bach, devops-hightower, cfo-campbell, research-thompson) plus 30+ skills under .claude/skills. [@claim:clm_80d97e2f431a312847f8eea4efa9a659b7c2964a4ad53fba526284b96386bba7]
- The project is flagged experimental: macOS-only, running but not guaranteed stable, consumes Claude API quota each cycle, acts fully autonomously without asking humans, and carries no warranty that the AI won't build unexpected things. [@claim:clm_8d654b0e9ae9a8452f2c1abbb956a698063c87c2fc677fbebb6d073683e9cbb4]
- Requirements are macOS (launchd-based daemon; Linux/systemd listed as future), an installed and logged-in Claude Code CLI, and a Claude subscription (Max or Pro recommended); jq, gh, and wrangler are optional. [@claim:clm_a34ca7be637b13d909aef57592040cf966f4027b92dd1861863a36839dae0ef0]
- Human steering appears to be intentionally limited to editing the 'Next Action' in memories/consensus.md (plus pause/resume), since the charter says humans guide direction only through that file while everything else stays autonomous. [@claim:clm_bf1dea5425fa0402ae0d898bce0423797394e7b2d18b8d4d6f92998194082f44]
- Each cycle is an independent `claude -p` call, and memories/consensus.md is stated to be the only cross-cycle state, like a relay baton; the prompt requires updating it before each cycle ends with fields such as Current Phase, Key Decisions, Active Projects, Next Action, and Company State. [@claim:clm_c737d3f8bdb7d62887074d3cb1e00d4b1dcc0f4dc9fa838db7c0bf05257a3815]
- Agents are prompted as real-world luminaries (e.g. 'you are DHH' rather than 'you are a developer') to activate the LLM's deep domain knowledge, and the charter sets decision principles like Ship > Plan > Discuss and monolith-first boring technology. [@claim:clm_c823a96cae53118e686fd8a8e57cab5c4377e9707e5e7788223aee602bc2da8c]
<!-- rcw:end owner=source:src_7a72052a02cd5032b888579c9b517a59 block=evidence -->

## Researcher notes

