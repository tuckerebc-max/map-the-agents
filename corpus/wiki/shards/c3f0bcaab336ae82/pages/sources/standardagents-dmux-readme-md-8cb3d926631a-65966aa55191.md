---
access: public
aliases: []
claim_ids:
- clm_0ca2535e9cd3aefa16624b70b766816eb9d102ca625e13b0048fdbce44f7a110
- clm_1fd614cc3c0aa6da097b4ddff74c6cdfdf6c90e08d40e958ebd47715400d9b9a
- clm_25f1318024e3c5f39e490b50c2837f71d733d0fc13fae68b439dfd79956b8413
- clm_30ebe052a252f4f3d418e66abc46856e4df763a60814ec8cd706a230d16b190c
- clm_31fa6019a9afaeb2a140f3728cfda459cc486dbe77acef77d1f279fe087c33fe
- clm_ad52f889b36563b378c4d8e21d39598c8fbd65f030586f6ad710404c5dedba7f
- clm_de5e65aff50500448b78c8245d5fd64dad7ecafc4096a7681d7e636491bca986
maturity: draft
page_id: pg_cdbeaea1fc265036814f65966aa55191
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d5e3df68bbb354df8d87abe1d11141f1
title: standardagents/dmux/README.md @ 8cb3d926631a
updated_at: '2026-09-14T03:13:03Z'
---

# standardagents/dmux/README.md @ 8cb3d926631a

<!-- rcw:begin owner=source:src_d5e3df68bbb354df8d87abe1d11141f1 block=evidence -->
- First-run setup can configure a primary inference provider and optional backup, discovering models from the provider and supporting API keys, custom OpenAI-compatible endpoints, or Codex/Grok Build logins; reopened via the settings key. [@claim:clm_0ca2535e9cd3aefa16624b70b766816eb9d102ca625e13b0048fdbce44f7a110]
- dmux manages multiple AI coding agents in parallel, giving each task a tmux pane backed by its own isolated git worktree and branch, with merge or GitHub PR actions to bring work back. [@claim:clm_1fd614cc3c0aa6da097b4ddff74c6cdfdf6c90e08d40e958ebd47715400d9b9a]
- dmux supports launching many agent CLIs, including Claude Code, Codex, OpenCode, Cline, Gemini, Qwen, Amp, pi, Cursor, Copilot, and Crush, with multi-select of several agents per prompt. [@claim:clm_25f1318024e3c5f39e490b50c2837f71d733d0fc13fae68b439dfd79956b8413]
- Each pane is a full working copy in its own worktree so agents do not conflict; merging auto-commits, merges, and cleans up in one step. [@claim:clm_30ebe052a252f4f3d418e66abc46856e4df763a60814ec8cd706a230d16b190c]
- The TUI exposes single-key shortcuts: n for a new worktree pane, t for a terminal pane, m for the pane menu, f for file browsing, s for settings, and q to quit, among others. [@claim:clm_31fa6019a9afaeb2a140f3728cfda459cc486dbe77acef77d1f279fe087c33fe]
- Branch handling defaults to automatic worktree/branch naming, but users can optionally pick a different base branch per pane or supply an explicit name, with agent-specific suffixes for multi-agent launches. [@claim:clm_ad52f889b36563b378c4d8e21d39598c8fbd65f030586f6ad710404c5dedba7f]
- Runtime requirements are tmux 3.0+, Node.js 18+, Git 2.20+, at least one supported agent CLI, and optionally an inference provider key or Codex/Grok Build login for AI naming and analysis. [@claim:clm_de5e65aff50500448b78c8245d5fd64dad7ecafc4096a7681d7e636491bca986]
<!-- rcw:end owner=source:src_d5e3df68bbb354df8d87abe1d11141f1 block=evidence -->

## Researcher notes

