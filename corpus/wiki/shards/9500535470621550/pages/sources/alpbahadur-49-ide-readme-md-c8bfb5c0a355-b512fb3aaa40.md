---
access: public
aliases: []
claim_ids:
- clm_12589f1cdcf149c44a218ecc39d1017f52618bd386ce02c3d1ac06839f672028
- clm_15cbb01876bc042379bc22299e72ca3b8d527372054afe0e4ef400db21cdbdd5
- clm_1d42606b8ffd4f0b0c0b23c4ae7703992276ae63d6d521c278a6156347ca14dd
- clm_679c79dabf272228f6ba85837afe8147c227eef3d4b115a0fdec715766d6b1f0
- clm_a6a5efcc5808fe6a36c25c6229123d0476708f62ab97bbaed7456427b64c46ee
- clm_adce38f8c4c45e63c70ee2600e9c4efad06013da4f50f15a251e4f9b2e36679e
- clm_d62ea3cac180e8b555e0a3d2954944c69ab0bb192504144cffba0684d5fa340d
- clm_e316b82e2913f340a8fc17fec64f75097672defc524870fe4a685b1214e04050
- clm_e7460fadefa1a461847867265734c0c775383e41c9c47b15c4d00e09a0c33413
maturity: draft
page_id: pg_3abc9d98d04e524fb6abb512fb3aaa40
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2e45875e77a850e489e0cbcca69f9127
title: alpbahadur/49-IDE/README.md @ c8bfb5c0a355
updated_at: '2026-09-14T03:34:09Z'
---

# alpbahadur/49-IDE/README.md @ c8bfb5c0a355

<!-- rcw:begin owner=source:src_2e45875e77a850e489e0cbcca69f9127 block=evidence -->
- A HUD overlay shows live CPU, RAM, and Claude API usage across all connected machines, and agents from any machine join one canvas without SSH. [@claim:clm_12589f1cdcf149c44a218ecc39d1017f52618bd386ce02c3d1ac06839f672028]
- The product is described as a 2D agentic IDE whose workspace is an infinite zoomable canvas of draggable, resizable panes with persistent layout, replacing terminal tabs. [@claim:clm_15cbb01876bc042379bc22299e72ca3b8d527372054afe0e4ef400db21cdbdd5]
- Terminals are real tmux sessions served via ttyd with ANSI color, scrollback, and the user's shell config, plus broadcast input to multiple terminals at once. [@claim:clm_1d42606b8ffd4f0b0c0b23c4ae7703992276ae63d6d521c278a6156347ca14dd]
- The macOS app is not notarized, so macOS blocks it on first launch until the user runs 'xattr -cr' on the app bundle. [@claim:clm_679c79dabf272228f6ba85837afe8147c227eef3d4b115a0fdec715766d6b1f0]
- The product integrates Beads (steveyegge/beads) for interactive issue tables on the canvas; the agent runs via node agent/bin/49-agent.js and the cloud server via node cloud/src/index.js. [@claim:clm_a6a5efcc5808fe6a36c25c6229123d0476708f62ab97bbaed7456427b64c46ee]
- A macOS desktop app is distributed as a .dmg on GitHub Releases, runs as a tray icon, is not notarized (requiring an xattr workaround), and offers in-app update checks. [@claim:clm_adce38f8c4c45e63c70ee2600e9c4efad06013da4f50f15a251e4f9b2e36679e]
- The relay stores no terminal data server-side; terminal I/O is relayed, never persisted, and self-hosting keeps terminals and files on the user's machine. [@claim:clm_d62ea3cac180e8b555e0a3d2954944c69ab0bb192504144cffba0684d5fa340d]
- Architecture: 49-agent processes on machines connect over WSS to a relay (self-hosted or 49agents.com), which browsers on phones, laptops, and tablets also connect to; each agent connects independently via WebSocket. [@claim:clm_e316b82e2913f340a8fc17fec64f75097672defc524870fe4a685b1214e04050]
- Setup uses a 49ctl CLI: './49ctl setup' for one-time interactive setup and './49ctl start' to launch the cloud server and agent, then the UI is served at localhost:1071 with no account or login. [@claim:clm_e7460fadefa1a461847867265734c0c775383e41c9c47b15c4d00e09a0c33413]
<!-- rcw:end owner=source:src_2e45875e77a850e489e0cbcca69f9127 block=evidence -->

## Researcher notes

