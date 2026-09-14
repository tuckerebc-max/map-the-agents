---
access: public
aliases: []
claim_ids:
- clm_1a6749db0581f421d4787ce29ab192635df42fcb68d2d0d582f2274f0075072a
- clm_212bd080fbc62bc3b785f35d5e97905a6f69ddd6a4a7653cc55e219cfae559de
- clm_2676378cc7e03582cdae0c5f020d09cf4c83a85a3be246d134217e3bca93b898
- clm_40c914724c4bf780f0fcd63e00b4e037ff5f33902350ea7a31aeb8f05dd137d2
- clm_59af9cd3cecf2693aff698db0088b64986e4c6b9f26915b68ac863c0cf0e2463
- clm_7b80926cc27e77495d454099cf1d7d29ea782c9feb2c5952542f0cc9d9213ffa
- clm_7d899e87a142e781f732b7f26b82c1906cf2104826e33347f74edc2bf452d1ca
- clm_ef23240f603528346092a158f01701f68925cd9728ad36cbe889cb804e3c7bbd
maturity: draft
page_id: pg_d3386abd911451c7ba74a575d1874b6f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b843e5fe65c653e68282c2f305c6e317
title: gastownhall/gastown/README.md @ 649b832b7672
updated_at: '2026-09-14T03:52:52Z'
---

# gastownhall/gastown/README.md @ 649b832b7672

<!-- rcw:begin owner=source:src_b843e5fe65c653e68282c2f305c6e317 block=evidence -->
- Agent work state persists in git worktree-based 'Hooks' storage that survives crashes and restarts, and work items are stored in the Beads ledger, a git-backed issue tracking system. [@claim:clm_1a6749db0581f421d4787ce29ab192635df42fcb68d2d0d582f2274f0075072a]
- Native installs require Git 2.20+, Go 1.26.2+ (per go.mod), Beads (bd) 0.57.0+, sqlite3, ICU4C dev headers for source builds, tmux 3.0+ for tmux-backed roles, and a Claude Code CLI as the default runtime; Docker installs only need Docker Compose. [@claim:clm_212bd080fbc62bc3b785f35d5e97905a6f69ddd6a4a7653cc55e219cfae559de]
- Bead/issue IDs use a prefix plus 5-character alphanumeric format (e.g. gt-abc12), where the prefix indicates the item's origin or rig; commands like gt sling and gt convoy accept these IDs. [@claim:clm_2676378cc7e03582cdae0c5f020d09cf4c83a85a3be246d134217e3bca93b898]
- The Refinery is a per-rig Bors-style merge queue: polecats run 'gt done' to create MR beads, the Refinery batches them, runs verification gates, and bisects failing batches; polecats never push directly to main. [@claim:clm_40c914724c4bf780f0fcd63e00b4e037ff5f33902350ea7a31aeb8f05dd137d2]
- The architecture includes a Mayor AI coordinator, a Town workspace directory (e.g. ~/gt/), per-project Rigs wrapping git repositories, and Polecats (worker agents with persistent identity but ephemeral sessions). [@claim:clm_59af9cd3cecf2693aff698db0088b64986e4c6b9f26915b68ac863c0cf0e2463]
- A three-tier watchdog system keeps agents healthy: per-rig Witnesses monitor polecats and trigger recovery, the Deacon runs continuous patrol cycles across rigs, and Dogs are dispatched for maintenance tasks like triage. [@claim:clm_7b80926cc27e77495d454099cf1d7d29ea782c9feb2c5952542f0cc9d9213ffa]
- Runtime configuration is per-rig via settings/config.json with provider, command, args, and prompt_mode fields; built-in agent presets include claude, gemini, codex, kiro, cursor, auggie, amp, opencode, copilot, pi, and omp. [@claim:clm_7d899e87a142e781f732b7f26b82c1906cf2104826e33347f74edc2bf452d1ca]
- The Wasteland federated coordination network links Gas Towns through DoltHub, and Dolt is a prerequisite on the Linux and Windows install paths. [@claim:clm_ef23240f603528346092a158f01701f68925cd9728ad36cbe889cb804e3c7bbd]
<!-- rcw:end owner=source:src_b843e5fe65c653e68282c2f305c6e317 block=evidence -->

## Researcher notes

