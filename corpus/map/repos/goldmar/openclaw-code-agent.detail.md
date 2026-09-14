# goldmar/openclaw-code-agent -- full detail

[Back to orientation](openclaw-code-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/goldmar/openclaw-code-agent/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/1d896bcda1b0e71c.json](../../../wiki/dossiers/goldmar/openclaw-code-agent/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/1d896bcda1b0e71c.json)

## specifications (1 claim(s))

- [observation/documented] The package runs Claude Code, Codex, and experimental OpenCode as managed background coding sessions from OpenClaw chat, adding plan approval, session lifecycle, wake routing, worktree isolation, and merge/PR follow-through. -- evidence: [README.md#L7-L7](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L7-L7) (`clm_4c94713ee92c8136d450b91464e20604f58f074cf17fe570558c1e563d878e75`)

## components (1 claim(s))

- [observation/documented] src/session-manager.ts is the control plane: it enforces maxSessions, spawns and tracks sessions, resolves resume/fork requests, persists runtime metadata and output, and composes notification, interaction, and worktree-controller services. -- evidence: [docs/ARCHITECTURE.md#L70-L75](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/docs/ARCHITECTURE.md#L70-L75), [docs/ARCHITECTURE.md#L68-L68](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/docs/ARCHITECTURE.md#L68-L68) (`clm_1a572e56a112ad70cbab6e87a17eb229b4c9c7c44937361e63adc28f6c9d57af`)

## design-choices (1 claim(s))

- [observation/documented] The default policy is review-first: permissionMode is 'plan', planApproval defaults to 'delegate', and defaultWorktreeStrategy defaults to 'delegate', so the orchestrator reviews plans before approving or escalating to the user. -- evidence: [README.md#L13-L22](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L13-L22), [README.md#L123-L125](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L123-L125) (`clm_d27fa21adc99ef7c9ccafc95857166e1b92cec0bfcfb9a05add7b9c866fc9754`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The plugin exposes agent-facing tools including agent_launch, agent_respond, agent_output, agent_sessions, agent_kill, agent_stats, agent_merge, agent_pr, agent_worktree_status, agent_worktree_cleanup, and four agent_goal_* tools. -- evidence: [README.md#L218-L235](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L218-L235) (`clm_6e85d0003df39d59cda50aa7941792018dc69370dd7df5e7ce9e27480950efa2`)
- [observation/documented] Chat commands mirror common workflows: /agent, /agent_sessions, /agent_output, /agent_respond, /agent_kill, /agent_stats, /agent_policy, /agent_goal, /agent_goal_status, /agent_goal_edit, and /agent_goal_stop. -- evidence: [README.md#L237-L237](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L237-L237) (`clm_1a4668950ffccd5ba8d3895bfa727a60779e4f3d2de1971414f9a8c0d342849f`)
- [observation/documented] In ask-mode worktree decisions, buttons adapt to state: new branches offer Merge/Open PR/Later/Discard, existing-PR branches add View PR and Sync PR, and PR options are omitted when the GitHub CLI is unavailable. -- evidence: [README.md#L185-L189](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L185-L189) (`clm_62e0ed3b889173d87f8bfdb0aceaf76fa9814c65682980afe911bfafe1934df4`)

## memory-state (2 claim(s))

- [observation/documented] Sessions support suspend, resume, fork, interrupt, and recovery across restarts with persisted metadata and output; persisted records stay resumable even after runtime sessions are garbage-collected at sessionGcAgeMinutes. -- evidence: [docs/ARCHITECTURE.md#L79-L85](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/docs/ARCHITECTURE.md#L79-L85), [README.md#L13-L22](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L13-L22) (`clm_ef1082d228791e2d303f5560357f30046ec54340b1de0b9314bbd27c9349f21d`)
- [observation/documented] Worktree-backed sessions move through lifecycle states including active, pending decision, pr_open, merged, released, dismissed, and no_change, with agent_worktree_status and a preview_safe cleanup mode. -- evidence: [README.md#L63-L69](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L63-L69), [README.md#L71-L71](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L71-L71) (`clm_d00f24ec244834ea79e23d45cb68ea3cfd971fd032e9804aafa83a0b3509c2bb`)

## orchestration (2 claim(s))

- [observation/documented] Merge, PR, terminal, and no-change outcomes use a two-step completion contract: the plugin sends a terse canonical status, then wakes the orchestrator with route metadata so it sends at most one short factual summary to the origin thread. -- evidence: [README.md#L193-L193](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L193-L193) (`clm_eb9982da87028c0050a2e9421f8434d02a159c1dd1beb12da2c08db7fb45945d`)
- [observation/documented] Goal tasks are explicit autonomous loops, available as verifier-driven or Ralph-style loops; the iteration counter advances only when the goal controller starts another agent turn after a missing completion promise or failed verifier. -- evidence: [README.md#L13-L22](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L13-L22), [README.md#L204-L210](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L204-L210), [README.md#L200-L200](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L200-L200) (`clm_3ea19d83e1f4e9684e68afc52466da5a036ae52f5a70674ae9c16b7c24c9e666`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The package is built and validated against OpenClaw 2026.9.4 and requires Node >=24.16.0 <25 or >=26.1.0, with a verified 2026.8.1 compatibility floor for plugin API, Gateway, and peer dependency contracts. -- evidence: [README.md#L131-L131](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L131-L131) (`clm_076812dad80c676c4061bd0b37a784c4afce3288bac86641fe0bb937c3ec9d0e`)

## limitations (1 claim(s))

- [observation/documented] The OpenCode harness is explicitly experimental: it runs a per-session local 'opencode serve' process, uses classic session lifecycle routes because v2 session wait is unavailable, and does not forward the reasoning-effort option. -- evidence: [README.md#L141-L141](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L141-L141), [README.md#L197-L198](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L197-L198), [docs/ARCHITECTURE.md#L111-L113](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/docs/ARCHITECTURE.md#L111-L113) (`clm_ff1926c3b87746d10ff10c1cf06282f20fe1d54516e43f1c33c4c4b2ccfcda41`)

## relevance (1 claim(s))

- [observation/documented] The plugin is positioned for starting coding work from Telegram, Discord, or other OpenClaw channels and keeping the job observable after the first message, distinct from OpenClaw's bundled acpx and codex plugins. -- evidence: [README.md#L9-L9](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L9-L9), [README.md#L24-L24](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L24-L24) (`clm_5ed56ee38a49e4e3cd9e2e0763d090cf877fcd6059ddc66fb074216bf58c042a`)

