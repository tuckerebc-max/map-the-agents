# goldmar/openclaw-code-agent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fbb2e275ddd8 @ 1d896bcda1b0e71c

## Summary (orientation draft, not independently verified)

The repository is an OpenClaw plugin that orchestrates Claude Code, Codex, and experimental OpenCode coding sessions from chat, with plan review, worktree follow-through, and goal loops. Claims are drawn from README and docs slices; the previously unsupported goal-loop characterization is corrected with proper citations. Evidence coverage: 133 of 244 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 5 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The package runs Claude Code, Codex, and experimental OpenCode as managed background coding sessions from OpenClaw chat, adding plan approval, session lifecycle, wake routing, worktree isolation, and merge/PR follow-through. -- evidence: [README.md#L7-L7](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L7-L7)
- components (1 claim(s)):
  - [observation/documented] src/session-manager.ts is the control plane: it enforces maxSessions, spawns and tracks sessions, resolves resume/fork requests, persists runtime metadata and output, and composes notification, interaction, and worktree-controller services. -- evidence: [docs/ARCHITECTURE.md#L70-L75](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/docs/ARCHITECTURE.md#L70-L75), [docs/ARCHITECTURE.md#L68-L68](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/docs/ARCHITECTURE.md#L68-L68)
- design-choices (1 claim(s)):
  - [observation/documented] The default policy is review-first: permissionMode is 'plan', planApproval defaults to 'delegate', and defaultWorktreeStrategy defaults to 'delegate', so the orchestrator reviews plans before approving or escalating to the user. -- evidence: [README.md#L13-L22](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L13-L22), [README.md#L123-L125](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L123-L125)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The plugin exposes agent-facing tools including agent_launch, agent_respond, agent_output, agent_sessions, agent_kill, agent_stats, agent_merge, agent_pr, agent_worktree_status, agent_worktree_cleanup, and four agent_goal_* tools. -- evidence: [README.md#L218-L235](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L218-L235)
  - [observation/documented] Chat commands mirror common workflows: /agent, /agent_sessions, /agent_output, /agent_respond, /agent_kill, /agent_stats, /agent_policy, /agent_goal, /agent_goal_status, /agent_goal_edit, and /agent_goal_stop. -- evidence: [README.md#L237-L237](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L237-L237)
- memory-state (2 claim(s)):
  - [observation/documented] Sessions support suspend, resume, fork, interrupt, and recovery across restarts with persisted metadata and output; persisted records stay resumable even after runtime sessions are garbage-collected at sessionGcAgeMinutes. -- evidence: [docs/ARCHITECTURE.md#L79-L85](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/docs/ARCHITECTURE.md#L79-L85), [README.md#L13-L22](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L13-L22)
  - [observation/documented] Worktree-backed sessions move through lifecycle states including active, pending decision, pr_open, merged, released, dismissed, and no_change, with agent_worktree_status and a preview_safe cleanup mode. -- evidence: [README.md#L63-L69](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L63-L69), [README.md#L71-L71](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L71-L71)
- orchestration (2 claim(s)):
  - [observation/documented] Merge, PR, terminal, and no-change outcomes use a two-step completion contract: the plugin sends a terse canonical status, then wakes the orchestrator with route metadata so it sends at most one short factual summary to the origin thread. -- evidence: [README.md#L193-L193](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L193-L193)
  - [observation/documented] Goal tasks are explicit autonomous loops, available as verifier-driven or Ralph-style loops; the iteration counter advances only when the goal controller starts another agent turn after a missing completion promise or failed verifier. -- evidence: [README.md#L13-L22](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L13-L22), [README.md#L204-L210](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L204-L210), [README.md#L200-L200](https://github.com/goldmar/openclaw-code-agent/blob/fbb2e275ddd8d0734bb63775abf5f05860f7be7a/README.md#L200-L200)
More evidence: [full detail](openclaw-code-agent.detail.md)

Metadata and full claim list: [full detail](openclaw-code-agent.detail.md)
Human notes ([notes](openclaw-code-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
