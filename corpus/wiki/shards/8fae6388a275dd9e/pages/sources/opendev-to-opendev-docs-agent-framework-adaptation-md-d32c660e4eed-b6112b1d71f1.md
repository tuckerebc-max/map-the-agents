---
access: public
aliases: []
claim_ids:
- clm_2d92d54e1bfa222b4c19531557432f09070ab955ecaea84b3cded9bc16061d1e
- clm_4a036e3fd12f5f820c20bda1de179af88b26e18466b98ba789a5d1ca8f6622c2
- clm_4be6dda976e36c638f39a11f9cbb51907212a6cd5dbe269efe3e4f4de1989042
- clm_5311f4defdac0b9aa5585ce7580bda67b36fcaf7da683781a35d43a68074b1a6
- clm_5ef3258e920f6d4f26c73241dd365762485d0daf361f457820279bbaa4b492f8
- clm_69a59e544af4ec3feac0eff2c0f1723abb9883b424d2764fbce30d77686750c1
maturity: draft
page_id: pg_a7d8169f351a54239021b6112b1d71f1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e62a0f140c195ff18f1a3c740c59bbb3
title: opendev-to/opendev/docs/agent-framework-adaptation.md @ d32c660e4eed
updated_at: '2026-09-14T02:27:10Z'
---

# opendev-to/opendev/docs/agent-framework-adaptation.md @ d32c660e4eed

<!-- rcw:begin owner=source:src_e62a0f140c195ff18f1a3c740c59bbb3 block=evidence -->
- The adaptation document indicates that before this work OpenDev lacked background agents, inter-agent communication, teams, and worktree isolation, suggesting these multi-agent capabilities are recent additions whose shipped status should be verified against code. [@claim:clm_2d92d54e1bfa222b4c19531557432f09070ab955ecaea84b3cded9bc16061d1e]
- Per-agent sidechain transcripts are stored as append-only JSONL at `~/.opendev/sessions/{session_id}/agents/{agent_id}.jsonl`, with readers that filter malformed lines and orphaned tool calls for resume. [@claim:clm_4a036e3fd12f5f820c20bda1de179af88b26e18466b98ba789a5d1ca8f6622c2]
- A WorktreeManager creates git worktrees per agent (branch `opendev/agent-{short_id}`), detects changes, and removes clean worktrees while preserving dirty ones for review. [@claim:clm_4be6dda976e36c638f39a11f9cbb51907212a6cd5dbe269efe3e4f4de1989042]
- The design doc specifies a TaskManager in opendev-runtime: a UI-agnostic task lifecycle state machine with idempotent transitions, a notified flag, 5-second eviction grace, and retain-to-block-eviction. [@claim:clm_5311f4defdac0b9aa5585ce7580bda67b36fcaf7da683781a35d43a68074b1a6]
- A file-based mailbox system gives each agent an inbox with fd-lock protocol, corruption recovery via rename, a 1000-entry cap, and message types including Text, ShutdownRequest, ShutdownResponse, and Idle. [@claim:clm_5ef3258e920f6d4f26c73241dd365762485d0daf361f457820279bbaa4b492f8]
- A `run_in_background` parameter on `spawn_subagent` returns a task_id immediately, runs the agent in a detached tokio task, and injects results into the parent via a sentinel mechanism when idle. [@claim:clm_69a59e544af4ec3feac0eff2c0f1723abb9883b424d2764fbce30d77686750c1]
<!-- rcw:end owner=source:src_e62a0f140c195ff18f1a3c740c59bbb3 block=evidence -->

## Researcher notes

