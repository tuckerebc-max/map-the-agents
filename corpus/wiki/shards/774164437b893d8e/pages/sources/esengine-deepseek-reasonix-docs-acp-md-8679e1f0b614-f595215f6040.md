---
access: public
aliases: []
claim_ids:
- clm_21363203e0d16a36e77c20e30ff62c28629db51f56eb9331d3e79c5f67dcc4fe
- clm_30aba16090a5c19f0648f37a29def9e3550668490d5b538de0f1c2ff6eceeebb
- clm_44183ae25a0abfc887cd7e2b66eebd2e869c60d133b5a891384bd60e3b845b15
- clm_914cecc3c84bfac1020fca791a18c6320ef4fae15a9104da1016f89375c9057a
- clm_a7426a9beb75edf6263e23d284cbb6a84a1c91ed6488ce8ff01da51d48897d62
- clm_b3568155dda85e633753e0ea9b6c02fdc0302fbd51a590cd9a9e40269d7d4be1
- clm_da8966472920f310d6957f187da3ab5271b2f032c0595a1bd6d17c7cfceae7c6
maturity: draft
page_id: pg_b6241eeceeae577680fef595215f6040
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_294a47589e8a579e94ec3d5329cac65d
title: esengine/DeepSeek-Reasonix/docs/ACP.md @ 8679e1f0b614
updated_at: '2026-09-14T02:00:56Z'
---

# esengine/DeepSeek-Reasonix/docs/ACP.md @ 8679e1f0b614

<!-- rcw:begin owner=source:src_294a47589e8a579e94ec3d5329cac65d block=evidence -->
- Reasonix implements Agent Client Protocol v1 as an NDJSON JSON-RPC 2.0 agent over stdin/stdout, launched via `reasonix acp`, with diagnostics sent to stderr. [@claim:clm_21363203e0d16a36e77c20e30ff62c28629db51f56eb9331d3e79c5f67dcc4fe]
- ACP exposes session lifecycle methods including session/new, load, resume, prompt, cancel, list, close, and delete, each session owning an isolated controller, workspace root, model, and transcript. [@claim:clm_30aba16090a5c19f0648f37a29def9e3550668490d5b538de0f1c2ff6eceeebb]
- Permission presets are read-only, workspace-write, and danger-full-access; tool-approval changes update the gate in place without rebuilding the session controller. [@claim:clm_44183ae25a0abfc887cd7e2b66eebd2e869c60d133b5a891384bd60e3b845b15]
- A durable session inbox extension supports enqueue, list, get, update, delete, move, setPaused, retry, and refresh operations on persisted follow-up work. [@claim:clm_914cecc3c84bfac1020fca791a18c6320ef4fae15a9104da1016f89375c9057a]
- When the ACP client advertises fs.readTextFile, fs.writeTextFile, or terminal capabilities, eligible file operations route through editor unsaved buffers and foreground commands through a client-owned terminal; non-UTF-8 files stay on the local path. [@claim:clm_a7426a9beb75edf6263e23d284cbb6a84a1c91ed6488ce8ff01da51d48897d62]
- A vendor extension `_reasonix.io/session/steer` provides mid-turn guidance, returning steer_accepted or queued_followup after durably committing the guidance. [@claim:clm_b3568155dda85e633753e0ea9b6c02fdc0302fbd51a590cd9a9e40269d7d4be1]
- Session controls are split into independent axes: collaboration mode (normal/plan/goal), model, reasoning effort, and permission preset (read-only, workspace-write, danger-full-access), set via session/set_config_option. [@claim:clm_da8966472920f310d6957f187da3ab5271b2f032c0595a1bd6d17c7cfceae7c6]
<!-- rcw:end owner=source:src_294a47589e8a579e94ec3d5329cac65d block=evidence -->

## Researcher notes

