---
access: public
aliases: []
claim_ids:
- clm_10647f653b6300ff706196fbd3a23ed9165972c91357df4a8cab220d3266fec8
- clm_243aa14ba3aeb9977d8b6ba699823383a98149e041d49e2141a2ef596cc125d1
- clm_3f2df59fc645581ded2c2128d8c93ee38cf9f7a4c7d2e1adfda2fe317295a197
- clm_41d7703f37ca8a016627434b5e5c55d21e212122608a2ef858798b2d32665705
- clm_7259c6ab8a3722472e3a87a10cb277cf5ad25f57ff70c740efd099a304da0610
- clm_82f86f56c02c3003ff186abb3e7472b3e50f675c6341557a234cb632efe71f7a
- clm_8ef14b8cc2eafe8960fcf64a9e7afbd34dbdbc97dd5f41cbc6986231ee38563b
- clm_9d5d31dad10242132779c21a7fa2ab2e41e14f71cf39cefec8226e32de5ce3bb
- clm_9e42627bab5d304617b92e771633d76c768790ea1c302285a4cbbc30a35a3a61
- clm_b272bb8d2c1c1b21e492b4063262f53d0f979c80b75389f4297cb76f744fa599
- clm_f18cc7263a3c3dc889cb827a8d92cce538e463b2cb49d51bad7cd7fb9ec72a9a
maturity: draft
page_id: pg_9b44838b54695183ac2f31f294537758
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2d3b5df742f85b52a755cebda2860fe1
title: shrijayan/itwillsync/README.md @ f12b57bf7385
updated_at: '2026-09-14T02:39:54Z'
---

# shrijayan/itwillsync/README.md @ f12b57bf7385

<!-- rcw:begin owner=source:src_2d3b5df742f85b52a755cebda2860fe1 block=evidence -->
- Documented CLI flags include --port (default 7964), --localhost, --tailscale, --local, --no-qr, a setup subcommand, and -h/-v. [@claim:clm_10647f653b6300ff706196fbd3a23ed9165972c91357df4a8cab220d3266fec8]
- The architecture pairs a node-pty-backed agent process and HTTP/WebSocket server on the laptop with a browser terminal client on the phone, connected via WebSocket with token auth. [@claim:clm_243aa14ba3aeb9977d8b6ba699823383a98149e041d49e2141a2ef596cc125d1]
- Connections run over the local network (or Tailscale) with no cloud component, no accounts, and no telemetry; three connection modes are local WiFi (default), Tailscale, and localhost-only. [@claim:clm_3f2df59fc645581ded2c2128d8c93ee38cf9f7a4c7d2e1adfda2fe317295a197]
- A hub daemon provides a multi-session dashboard showing each agent's name, working directory, status, and uptime, with real-time WebSocket updates and tap-to-open full terminal. [@claim:clm_41d7703f37ca8a016627434b5e5c55d21e212122608a2ef858798b2d32665705]
- On startup the tool prints a QR code in the terminal; scanning it opens a browser-based terminal (xterm.js) on the phone with a touch keyboard and extra keys bar. [@claim:clm_7259c6ab8a3722472e3a87a10cb277cf5ad25f57ff70c740efd099a304da0610]
- The monorepo contains packages for the CLI (main npm package), a web-client browser terminal, a hub dashboard daemon, a landing page, and VitePress docs. [@claim:clm_82f86f56c02c3003ff186abb3e7472b3e50f675c6341557a234cb632efe71f7a]
- The product is agent-agnostic: it works with any terminal-based tool, citing Claude Code, Aider, Codex, Goose, Cline, and Copilot CLI, without vendor lock-in. [@claim:clm_8ef14b8cc2eafe8960fcf64a9e7afbd34dbdbc97dd5f41cbc6986231ee38563b]
- A first-run setup wizard detects the network and saves the connection preference; per-session overrides via --tailscale/--local and a re-run via 'npx itwillsync setup' are supported. [@claim:clm_9d5d31dad10242132779c21a7fa2ab2e41e14f71cf39cefec8226e32de5ce3bb]
- The CLI is invoked as npx itwillsync followed by an agent command (e.g. claude, aider, or any terminal command), with no install required but Node.js 20+ needed. [@claim:clm_9e42627bab5d304617b92e771633d76c768790ea1c302285a4cbbc30a35a3a61]
- The client auto-reconnects with scrollback buffer sync after connection drops, renders via WebGL on desktop with canvas fallback on mobile, and plays audio notifications when agents need attention. [@claim:clm_b272bb8d2c1c1b21e492b4063262f53d0f979c80b75389f4297cb76f744fa599]
- Security model: WebSocket messages are encrypted with NaCl secretbox (XSalsa20-Poly1305), each session gets a random 64-character token embedded in the QR URL, auth uses constant-time comparison, and 5 failed attempts lock out an IP for 60 seconds. [@claim:clm_f18cc7263a3c3dc889cb827a8d92cce538e463b2cb49d51bad7cd7fb9ec72a9a]
<!-- rcw:end owner=source:src_2d3b5df742f85b52a755cebda2860fe1 block=evidence -->

## Researcher notes

