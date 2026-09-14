---
access: public
aliases: []
claim_ids:
- clm_494c70ec6cd111ec4f34658a589406b38c1615c25c95e4edb72ecb4c6d4cddde
- clm_4eca9297b4b9fab0023d83f8c1b9ff016e5101a51dcf69d6e741c686d2425da3
- clm_53ee003035769becae444bfa5519e811aba7b091d1cb010c9cb260b07ad4c143
- clm_7f77b4ba6f55435a98353f7f92b16c625d66e5a1b96a4f68d5469c809ba1f4b6
- clm_8f22d190a21712bfee9dab2b91c6ae37b946eae95a9fea5eb3076cdb9b144a3a
- clm_c1582cb515a437647d1fab8673ea9be25f53143aa8270d2b2cf6b62e3b1a0abf
- clm_c9ec2b2a9cb6dacd4d75c13afa2a92fe23fa0296b70f49b76ccb8b52fbe9ffdf
- clm_fd486503f8e9dac41768d24e4d42376482f6ec56dba0f1aec016de8f683cbf35
maturity: draft
page_id: pg_3b303d0d86fd562ca1911896a04d57a0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ad3aac3bd2255dcaa87a203b0730cdd2
title: danshapiro/freshell/README.md @ e68ae40a2b3e
updated_at: '2026-09-14T03:06:36Z'
---

# danshapiro/freshell/README.md @ e68ae40a2b3e

<!-- rcw:begin owner=source:src_ad3aac3bd2255dcaa87a203b0730cdd2 block=evidence -->
- Stream Deck integration requires Chrome or Edge via WebHID and is not supported inside the freshell desktop app. [@claim:clm_494c70ec6cd111ec4f34658a589406b38c1615c25c95e4edb72ecb4c6d4cddde]
- For OpenCode sessions, freshell does not set OPENCODE_PERMISSION or pass --dangerously-skip-permissions; OpenCode's own config and OS filesystem permissions govern access. [@claim:clm_4eca9297b4b9fab0023d83f8c1b9ff016e5101a51dcf69d6e741c686d2425da3]
- The stack includes React 18, Redux Toolkit, xterm.js, Monaco, Express, node-pty, WebSocket, Vite, TypeScript, and Vitest-based testing tools. [@claim:clm_53ee003035769becae444bfa5519e811aba7b091d1cb010c9cb260b07ad4c143]
- The host pressure dashboard pane is limited to Linux, WSL, and macOS and is not shown on Windows. [@claim:clm_7f77b4ba6f55435a98353f7f92b16c625d66e5a1b96a4f68d5469c809ba1f4b6]
- Desktop profiles let multiple independent clients run on one machine, each with its own settings, storage dir, and single-instance lock, configured via ~/.freshell/profiles.json. [@claim:clm_8f22d190a21712bfee9dab2b91c6ae37b946eae95a9fea5eb3076cdb9b144a3a]
- An extension system supports three pane-type categories: client (static HTML/JS), server (freshell-managed HTTP server with auto port allocation), and CLI (terminal tool wrapped as a pane), installed via a freshell.json manifest in ~/.freshell/extensions/. [@claim:clm_c1582cb515a437647d1fab8673ea9be25f53143aa8270d2b2cf6b62e3b1a0abf]
- The app requires Node.js 18+ (20+ recommended) plus platform build tools for native modules, and runs on Windows, macOS, and Linux. [@claim:clm_c9ec2b2a9cb6dacd4d75c13afa2a92fe23fa0296b70f49b76ccb8b52fbe9ffdf]
- Freshell indexes local session history for Claude Code, Codex, OpenCode, and Amplifier, and can launch terminals for those plus Gemini and Kimi; OpenCode sessions are read directly from its local session database. [@claim:clm_fd486503f8e9dac41768d24e4d42376482f6ec56dba0f1aec016de8f683cbf35]
<!-- rcw:end owner=source:src_ad3aac3bd2255dcaa87a203b0730cdd2 block=evidence -->

## Researcher notes

