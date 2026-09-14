---
access: public
aliases: []
claim_ids:
- clm_22f74dcbf6c53684e87c026d3ee5be369afb17982095e825a3530efc059c8f3f
- clm_415590fe5241a12f44dee3661d9681e4d982609227caca07656ee5a808d39353
- clm_42a3e602e587717a2f8aaa307c91c844ba18eebfa2bd91b880961d701cb2dbd8
- clm_53ae285956b82072ca1fe3b506900271a7257e9aa73b65ca5a7dfa5d32f8e013
- clm_5eab302eac6346d2a2bd883541f3f3306c46194eb927da63bdc2d3bdf02f1d22
- clm_f300bb4f3514101b80124c4876dabc1cc6bbf57cbb6bf4929dd17a5db7e43c56
maturity: draft
page_id: pg_cb0fda11117e5b8084eedc6e09215d0e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4b4663e8cbda56bbb67b80938891d624
title: johannesjo/parallel-code/PRIVACY.md @ dcc4df2592cc
updated_at: '2026-09-14T02:08:03Z'
---

# johannesjo/parallel-code/PRIVACY.md @ dcc4df2592cc

<!-- rcw:begin owner=source:src_4b4663e8cbda56bbb67b80938891d624 block=evidence -->
- A Remote Access feature lets users monitor agents from a phone over Wi-Fi or Tailscale, with a QR code and a bearer-token URL. [@claim:clm_22f74dcbf6c53684e87c026d3ee5be369afb17982095e825a3530efc059c8f3f]
- For coordinator sub-tasks, the app injects a system-prompt preamble telling the sub-agent to call the signal_done MCP tool, via .claude/settings.local.json for Claude Code. [@claim:clm_415590fe5241a12f44dee3661d9681e4d982609227caca07656ee5a808d39353]
- State is stored locally: state.json with a rolling backup, keybindings, themes, arena files, and a .updaterId UUID in per-OS app data directories. [@claim:clm_42a3e602e587717a2f8aaa307c91c844ba18eebfa2bd91b880961d701cb2dbd8]
- The app drives third-party AI coding CLIs the user installs, including Claude Code, Codex CLI, Gemini CLI, Copilot CLI, OpenCode, and Antigravity CLI. [@claim:clm_53ae285956b82072ca1fe3b506900271a7257e9aa73b65ca5a7dfa5d32f8e013]
- Packaged macOS and Linux builds check GitHub Releases for updates via electron-updater, sending a stable per-install x-user-staging-id UUID to GitHub. [@claim:clm_5eab302eac6346d2a2bd883541f3f3306c46194eb927da63bdc2d3bdf02f1d22]
- Docker sandboxing is supported via a project-specific Dockerfile placed at .parallel-code/Dockerfile, in which tasks then run. [@claim:clm_f300bb4f3514101b80124c4876dabc1cc6bbf57cbb6bf4929dd17a5db7e43c56]
<!-- rcw:end owner=source:src_4b4663e8cbda56bbb67b80938891d624 block=evidence -->

## Researcher notes

