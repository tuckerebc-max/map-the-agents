---
access: public
aliases: []
claim_ids:
- clm_0f66fce9ca8aa3aaf49c04ffdb4faf67fee473b700000068f054a789347731ea
- clm_14bc4b6623b50c593bc851763570f455b28534bb5cb15d1fc676e9075e1b9869
- clm_169b44fc7dbb7f45478526becf90046d58ab90685c1a9abe27eac80e16f1390b
- clm_5a35f847e31f8410e3d1bfd8c5973ce175872b7443703bc7d40f8427ac434a60
- clm_8a42e354eaf7eb9184fee6e07ede8381e4ec1028b71b9864664090430b74aab2
maturity: draft
page_id: pg_f8dabca7c2a35ec2b9546fff0b71a53e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_67694cea036e5b7881d048ecae056646
title: winfunc/opcode/web_server.design.md @ 70c16d8a4910
updated_at: '2026-09-14T03:24:03Z'
---

# winfunc/opcode/web_server.design.md @ 70c16d8a4910

<!-- rcw:begin owner=source:src_67694cea036e5b7881d048ecae056646 block=evidence -->
- Web server mode exposes a REST API and WebSocket interface mirroring the desktop app, with request fields for command type (execute/continue/resume), project path, prompt, model, and session id. [@claim:clm_0f66fce9ca8aa3aaf49c04ffdb4faf67fee473b700000068f054a789347731ea]
- The web server provides cancel and output endpoints at /api/sessions/{sessionId}/cancel and /api/sessions/{sessionId}/output, added because the frontend expected them. [@claim:clm_14bc4b6623b50c593bc851763570f455b28534bb5cb15d1fc676e9075e1b9869]
- The web server mode has documented critical issues: sessions interfere via generic events, the cancel endpoint is a stub that does not terminate processes, stderr is not captured, and claude-cancelled events are missing. [@claim:clm_169b44fc7dbb7f45478526becf90046d58ab90685c1a9abe27eac80e16f1390b]
- In web mode the frontend falls back from Tauri event listening to browser DOM events, handling both string payloads (Tauri) and object payloads (web) for compatibility. [@claim:clm_5a35f847e31f8410e3d1bfd8c5973ce175872b7443703bc7d40f8427ac434a60]
- Web server mode is described as functional for single-session use but not production-suitable, and web mode runs Claude with the --dangerously-skip-permissions flag with CORS allowing all origins. [@claim:clm_8a42e354eaf7eb9184fee6e07ede8381e4ec1028b71b9864664090430b74aab2]
<!-- rcw:end owner=source:src_67694cea036e5b7881d048ecae056646 block=evidence -->

## Researcher notes

