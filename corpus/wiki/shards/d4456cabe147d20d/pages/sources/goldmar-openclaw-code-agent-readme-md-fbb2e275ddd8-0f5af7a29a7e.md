---
access: public
aliases: []
claim_ids:
- clm_076812dad80c676c4061bd0b37a784c4afce3288bac86641fe0bb937c3ec9d0e
- clm_1a4668950ffccd5ba8d3895bfa727a60779e4f3d2de1971414f9a8c0d342849f
- clm_3ea19d83e1f4e9684e68afc52466da5a036ae52f5a70674ae9c16b7c24c9e666
- clm_4c94713ee92c8136d450b91464e20604f58f074cf17fe570558c1e563d878e75
- clm_5ed56ee38a49e4e3cd9e2e0763d090cf877fcd6059ddc66fb074216bf58c042a
- clm_62e0ed3b889173d87f8bfdb0aceaf76fa9814c65682980afe911bfafe1934df4
- clm_6e85d0003df39d59cda50aa7941792018dc69370dd7df5e7ce9e27480950efa2
- clm_d00f24ec244834ea79e23d45cb68ea3cfd971fd032e9804aafa83a0b3509c2bb
- clm_d27fa21adc99ef7c9ccafc95857166e1b92cec0bfcfb9a05add7b9c866fc9754
- clm_eb9982da87028c0050a2e9421f8434d02a159c1dd1beb12da2c08db7fb45945d
- clm_ef1082d228791e2d303f5560357f30046ec54340b1de0b9314bbd27c9349f21d
- clm_ff1926c3b87746d10ff10c1cf06282f20fe1d54516e43f1c33c4c4b2ccfcda41
maturity: draft
page_id: pg_da6d8610374f534191f00f5af7a29a7e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c9dc013b1aca53ffbf01c9854b262ebd
title: goldmar/openclaw-code-agent/README.md @ fbb2e275ddd8
updated_at: '2026-09-14T01:52:24Z'
---

# goldmar/openclaw-code-agent/README.md @ fbb2e275ddd8

<!-- rcw:begin owner=source:src_c9dc013b1aca53ffbf01c9854b262ebd block=evidence -->
- The package is built and validated against OpenClaw 2026.9.4 and requires Node >=24.16.0 <25 or >=26.1.0, with a verified 2026.8.1 compatibility floor for plugin API, Gateway, and peer dependency contracts. [@claim:clm_076812dad80c676c4061bd0b37a784c4afce3288bac86641fe0bb937c3ec9d0e]
- Chat commands mirror common workflows: /agent, /agent_sessions, /agent_output, /agent_respond, /agent_kill, /agent_stats, /agent_policy, /agent_goal, /agent_goal_status, /agent_goal_edit, and /agent_goal_stop. [@claim:clm_1a4668950ffccd5ba8d3895bfa727a60779e4f3d2de1971414f9a8c0d342849f]
- Goal tasks are explicit autonomous loops, available as verifier-driven or Ralph-style loops; the iteration counter advances only when the goal controller starts another agent turn after a missing completion promise or failed verifier. [@claim:clm_3ea19d83e1f4e9684e68afc52466da5a036ae52f5a70674ae9c16b7c24c9e666]
- The package runs Claude Code, Codex, and experimental OpenCode as managed background coding sessions from OpenClaw chat, adding plan approval, session lifecycle, wake routing, worktree isolation, and merge/PR follow-through. [@claim:clm_4c94713ee92c8136d450b91464e20604f58f074cf17fe570558c1e563d878e75]
- The plugin is positioned for starting coding work from Telegram, Discord, or other OpenClaw channels and keeping the job observable after the first message, distinct from OpenClaw's bundled acpx and codex plugins. [@claim:clm_5ed56ee38a49e4e3cd9e2e0763d090cf877fcd6059ddc66fb074216bf58c042a]
- In ask-mode worktree decisions, buttons adapt to state: new branches offer Merge/Open PR/Later/Discard, existing-PR branches add View PR and Sync PR, and PR options are omitted when the GitHub CLI is unavailable. [@claim:clm_62e0ed3b889173d87f8bfdb0aceaf76fa9814c65682980afe911bfafe1934df4]
- The plugin exposes agent-facing tools including agent_launch, agent_respond, agent_output, agent_sessions, agent_kill, agent_stats, agent_merge, agent_pr, agent_worktree_status, agent_worktree_cleanup, and four agent_goal_* tools. [@claim:clm_6e85d0003df39d59cda50aa7941792018dc69370dd7df5e7ce9e27480950efa2]
- Worktree-backed sessions move through lifecycle states including active, pending decision, pr_open, merged, released, dismissed, and no_change, with agent_worktree_status and a preview_safe cleanup mode. [@claim:clm_d00f24ec244834ea79e23d45cb68ea3cfd971fd032e9804aafa83a0b3509c2bb]
- The default policy is review-first: permissionMode is 'plan', planApproval defaults to 'delegate', and defaultWorktreeStrategy defaults to 'delegate', so the orchestrator reviews plans before approving or escalating to the user. [@claim:clm_d27fa21adc99ef7c9ccafc95857166e1b92cec0bfcfb9a05add7b9c866fc9754]
- Merge, PR, terminal, and no-change outcomes use a two-step completion contract: the plugin sends a terse canonical status, then wakes the orchestrator with route metadata so it sends at most one short factual summary to the origin thread. [@claim:clm_eb9982da87028c0050a2e9421f8434d02a159c1dd1beb12da2c08db7fb45945d]
- Sessions support suspend, resume, fork, interrupt, and recovery across restarts with persisted metadata and output; persisted records stay resumable even after runtime sessions are garbage-collected at sessionGcAgeMinutes. [@claim:clm_ef1082d228791e2d303f5560357f30046ec54340b1de0b9314bbd27c9349f21d]
- The OpenCode harness is explicitly experimental: it runs a per-session local 'opencode serve' process, uses classic session lifecycle routes because v2 session wait is unavailable, and does not forward the reasoning-effort option. [@claim:clm_ff1926c3b87746d10ff10c1cf06282f20fe1d54516e43f1c33c4c4b2ccfcda41]
<!-- rcw:end owner=source:src_c9dc013b1aca53ffbf01c9854b262ebd block=evidence -->

## Researcher notes

