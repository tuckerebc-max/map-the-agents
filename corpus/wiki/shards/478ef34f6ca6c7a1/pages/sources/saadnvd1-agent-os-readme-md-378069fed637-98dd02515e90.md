---
access: public
aliases: []
claim_ids:
- clm_0681f31da857a9ea39263893c58884c5b5b9af300b99cc88151302ebf467c8f1
- clm_074570f800ca37c59c3f1e8a8ab70e4fcfbe28c8183387b6153498784be5d686
- clm_62384540f6289a02c1bec3e6a5436e0875b2c830881171ab86a7c03aa6bdaa91
- clm_70c342477c833db2d49398738f29b174ce96b05f90821cdabcfa15e9bc613b44
- clm_7b5be1e0093745d7dcb68c6863a32a715a845a87365238a6518cda2317efafd9
- clm_90947ede32d15d9ab14a01ed7cef23e74920ec5253019f68262c20a599d66753
- clm_ad1633ee8999b0878559b6a2fc317ca654ec9ffcb0dd3fab5079d69915f44dea
- clm_c5b666dde13d0e6138365d56e1d94d625cbed07df5a1bc4d67f2ec7d7dd0e3cb
- clm_d1d6de197adcf6e068e5cc7cf5379d55ef1789a29c2a7dbbf3a376ceed156bd8
- clm_dd4ea2fd77268a36a7a0f0e5f30f9dceab52199fadf3224b668a594df35502f6
maturity: draft
page_id: pg_a4dec91e82b0532b8e4c98dd02515e90
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c5dd7cd174a456149c757fb0f53ed435
title: saadnvd1/agent-os/README.md @ 378069fed637
updated_at: '2026-09-14T02:37:46Z'
---

# saadnvd1/agent-os/README.md @ 378069fed637

<!-- rcw:begin owner=source:src_c5dd7cd174a456149c757fb0f53ed435 block=evidence -->
- The product supports multiple AI coding agents with a capability matrix: only Claude Code and Kilo Code support resume and fork, and each agent has a distinct auto-approve mechanism (flags or config files). [@claim:clm_0681f31da857a9ea39263893c58884c5b5b9af300b99cc88151302ebf467c8f1]
- AgentOS provides a mobile-first web UI for managing AI coding sessions, served on port 3011 in the manual dev setup. [@claim:clm_074570f800ca37c59c3f1e8a8ab70e4fcfbe28c8183387b6153498784be5d686]
- The CLI offers run, start, stop, status, logs, and update commands for controlling the server. [@claim:clm_62384540f6289a02c1bec3e6a5436e0875b2c830881171ab86a7c03aa6bdaa91]
- Native desktop builds are distributed via GitHub Releases as macOS Apple Silicon .dmg and Linux .deb or .AppImage packages. [@claim:clm_70c342477c833db2d49398738f29b174ce96b05f90821cdabcfa15e9bc613b44]
- The project is MIT licensed and free and open source. [@claim:clm_7b5be1e0093745d7dcb68c6863a32a715a845a87365238a6518cda2317efafd9]
- Prerequisites are Node.js 20+, tmux, and ripgrep (auto-installed by the installer script per the README), plus at least one supported AI CLI such as Claude Code, Codex, Gemini CLI, Aider, or Cursor CLI. [@claim:clm_90947ede32d15d9ab14a01ed7cef23e74920ec5253019f68262c20a599d66753]
- Installation paths: global npm install followed by 'agent-os install' and 'agent-os start' (recommended when Node.js 20+ exists), a curl-piped install script for fresh machines without Node.js, or manual git clone with npm install and npm run dev. [@claim:clm_ad1633ee8999b0878559b6a2fc317ca654ec9ffcb0dd3fab5079d69915f44dea]
- Documented features include voice-to-text prompting, up to four side-by-side session panes, code search, file picker with mobile upload, GitHub cloning, git integration, git worktrees, dev server control, and conductor/worker session orchestration via MCP. [@claim:clm_c5b666dde13d0e6138365d56e1d94d625cbed07df5a1bc4d67f2ec7d7dd0e3cb]
- The desktop app is a native wrapper around the web UI; the backend server must still be installed and run separately, with the wrapper only providing a native window instead of a browser. [@claim:clm_d1d6de197adcf6e068e5cc7cf5379d55ef1789a29c2a7dbbf3a376ceed156bd8]
- Mobile access is documented via Tailscale: install on machine and phone, sign in with the same account, then reach the server at its 100.x.x.x address on port 3011. [@claim:clm_dd4ea2fd77268a36a7a0f0e5f30f9dceab52199fadf3224b668a594df35502f6]
<!-- rcw:end owner=source:src_c5dd7cd174a456149c757fb0f53ed435 block=evidence -->

## Researcher notes

