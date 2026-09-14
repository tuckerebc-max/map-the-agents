---
access: public
aliases: []
claim_ids:
- clm_0ef2ad0503639ad8290439eccf3a615bd96755095aea1c23006068110375617c
- clm_17cc819bca8d21cf6c9d191bbaab9e041a0d2fd832e754877e069354c13d7d63
- clm_592fb050a727d5071ae34f4e91f9412fc86a82b9c36e922f7b65adde2bec7f08
- clm_ed5316e179b683c0c7a1374fa17d3b85ba7afd4eeb98f04d28844d6f36a7138f
maturity: draft
page_id: pg_b1f0d5ef4e915fee936a1542acc15e41
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b96fcaef359854e28c6f4b1a5f3420bb
title: andyrewlee/amux/ARCHITECTURE.md @ f94362f6c25f
updated_at: '2026-09-14T01:33:26Z'
---

# andyrewlee/amux/ARCHITECTURE.md @ f94362f6c25f

<!-- rcw:begin owner=source:src_b96fcaef359854e28c6f4b1a5f3420bb block=evidence -->
- Two binaries share internal packages: cmd/amux (interactive app) and cmd/amux-harness (headless renderer for deterministic perf and render testing), with internal layers for app, ui, tmux, pty, git, data, and vterm. [@claim:clm_0ef2ad0503639ad8290439eccf3a615bd96755095aea1c23006068110375617c]
- The amux-harness binary appears to support deterministic perf and render testing of the UI itself (headless frame dumps), suggesting an internal render/perf evaluation path rather than agent-task benchmarking. [@claim:clm_17cc819bca8d21cf6c9d191bbaab9e041a0d2fd832e754877e069354c13d7d63]
- amux is a terminal UI (Bubble Tea v2) for running multiple coding agents in parallel, using a workspace-first model that can import git worktrees. [@claim:clm_592fb050a727d5071ae34f4e91f9412fc86a82b9c36e922f7b65adde2bec7f08]
- internal/ui/compositor imports charmbracelet/ultraviolet directly on the render path; ultraviolet has no semver releases and its pin must stay in lockstep with bubbletea/v2 to avoid rendering breakage. [@claim:clm_ed5316e179b683c0c7a1374fa17d3b85ba7afd4eeb98f04d28844d6f36a7138f]
<!-- rcw:end owner=source:src_b96fcaef359854e28c6f4b1a5f3420bb block=evidence -->

## Researcher notes

