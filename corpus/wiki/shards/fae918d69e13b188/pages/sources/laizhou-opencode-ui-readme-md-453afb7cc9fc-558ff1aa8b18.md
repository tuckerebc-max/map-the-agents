---
access: public
aliases: []
claim_ids:
- clm_20a009df664e61bfc1fab5883ffdaf18122e1848d14ec0abaa395fba87551768
- clm_3075399ab082c7bf0b56a04e51bdb7292c2d46f40005f688c06628dc6a181232
- clm_3f8a08c6c2bf80b33696ce9d6ee8f5cc936cc76ee8c3a6c7911200cdbee7d649
- clm_4c659e5453f2d3bbf804db99fc5e3cc597b2d7d75d3579033a43e1191c39c1c2
- clm_62693995a7cda1947e2628d6322e9d29d62a2fd097dd264e7f5aa536d05048d4
- clm_7037ef48717412d06df0a7a43f0a6103b330152c719e5d2a8550456da26ab406
- clm_7e25e208166cb5dc1c1319bb78f939e0b82e4298ecd02a0c2f57ad46d0ee3b04
- clm_8b77dd19e5dbbd1cc3e1e0c6058b9ece3d09ceaa9a63f1c8425b1d560dd292b8
- clm_ade1e4a868f9f75f1ffa85e288b4c11297093fd1c566e3535decb2adb7786985
- clm_ca7bf6032a54297a3670afef99f389a443ce764586ea39df64827f3bd98b5513
- clm_f3ad5b1ba6459ba94d125443ccb4d2e6f9c6cba715b54d2978591cc01da43113
maturity: draft
page_id: pg_392774e8c48d5c70bc90558ff1aa8b18
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e297e91ed3895d8cbe6dff2be9caee33
title: LaiZhou/OpenCode_UI/README.md @ 453afb7cc9fc
updated_at: '2026-09-14T04:04:37Z'
---

# LaiZhou/OpenCode_UI/README.md @ 453afb7cc9fc

<!-- rcw:begin owner=source:src_e297e91ed3895d8cbe6dff2be9caee33 block=evidence -->
- Compared with Claude Code, the plugin lacks diagnostic sharing and instead uses the IDE's built-in LSP, per the feature comparison table. [@claim:clm_20a009df664e61bfc1fab5883ffdaf18122e1848d14ec0abaa395fba87551768]
- Keyboard shortcuts are customizable through the IDE's Settings > Keymap by searching for 'OpenCode'. [@claim:clm_3075399ab082c7bf0b56a04e51bdb7292c2d46f40005f688c06628dc6a181232]
- An 'Add to Terminal' shortcut (Opt+Cmd+K / Ctrl+Alt+K) sends the current file or selection to OpenCode as @path references, with line ranges like @file.kt#L10-25 when text is selected, and opens/focuses the terminal if needed. [@claim:clm_3f8a08c6c2bf80b33696ce9d6ee8f5cc936cc76ee8c3a6c7911200cdbee7d649]
- The plugin sends a system notification when OpenCode transitions from Busy to Idle, and supports auto-resume of the last session, clickable file-path links in terminal output, and remembered connection settings. [@claim:clm_4c659e5453f2d3bbf804db99fc5e3cc597b2d7d75d3579033a43e1191c39c1c2]
- Quick Launch opens a connection dialog via Cmd+Esc (Mac) or Ctrl+\ (Win/Linux), letting users connect to an existing OpenCode server by host:port with optional password, or create a new local terminal session on default port 127.0.0.1:4096. [@claim:clm_62693995a7cda1947e2628d6322e9d29d62a2fd097dd264e7f5aa536d05048d4]
- Terminal management uses a single persistent terminal tab per project named OpenCode({port}); closing it causes a new one to be created on next launch. [@claim:clm_7037ef48717412d06df0a7a43f0a6103b330152c719e5d2a8550456da26ab406]
- The product is a JetBrains IDE plugin integrating the OpenCode open-source AI coding agent into the development workflow. [@claim:clm_7e25e208166cb5dc1c1319bb78f939e0b82e4298ecd02a0c2f57ad46d0ee3b04]
- Context can also be added via right-click menus: 'OpenCode: Add Context' in the editor and 'OpenCode: Add File(s)' in Project View. [@claim:clm_8b77dd19e5dbbd1cc3e1e0c6058b9ece3d09ceaa9a63f1c8425b1d560dd292b8]
- The plugin appears to detect server authentication automatically when connecting to a running OpenCode server, and supports an optional password for the server. [@claim:clm_ade1e4a868f9f75f1ffa85e288b4c11297093fd1c566e3535decb2adb7786985]
- The plugin requires a JetBrains IDE (2025.2+ per README) and the OpenCode CLI, installable via npm or from opencode.ai/download. [@claim:clm_ca7bf6032a54297a3670afef99f389a443ce764586ea39df64827f3bd98b5513]
- When OpenCode edits files, the plugin opens a native IDE diff viewer showing changes chronologically with navigation, progress count, and accept (write to disk and git add) or reject (restore pre-edit state) actions. [@claim:clm_f3ad5b1ba6459ba94d125443ccb4d2e6f9c6cba715b54d2978591cc01da43113]
<!-- rcw:end owner=source:src_e297e91ed3895d8cbe6dff2be9caee33 block=evidence -->

## Researcher notes

