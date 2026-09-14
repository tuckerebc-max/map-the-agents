---
access: public
aliases: []
claim_ids:
- clm_1141b7548e7f9db256ffb86fa792cdd5912354488ad4e62ecb970af808f1c72c
- clm_3392f10cd9c30fc485ecf2e49d0b7856743def29b38fdc85d0d2d1d4441cc4a9
- clm_4296e2a763e85f3aba1fef7e0bc28b46d17424ee44e1277d59e2cb35704b5de6
- clm_6b8542cefdc23e81ff1418141701345d9aaa846fc817f996ddcc9dde4c05260d
- clm_729bbadb3cf070715c7a3d280eba3dca3c2c0894ba072596ecbb13c6a500e971
- clm_95a8d26c94dc255601eb1098325ad2677ce1fc81bcc5aace8a3eff7438ba9b89
- clm_a44fb2a56ef973a1ca42ddf652a19303b597796a2392663489e648f3d0981fd4
- clm_ced2ba0d1b7ac9a5411f13caf20f3de9955a52be0658da7fea85f98e0df1a470
maturity: draft
page_id: pg_44cfda8d37ee579dbcffc37e8ec8018f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d97e7f59455556e9bd83ffc9eceaf0e5
title: electric-sql/electric/AGENTS_DESKTOP_PLAN.md @ bb397424db0e
updated_at: '2026-09-14T03:49:21Z'
---

# electric-sql/electric/AGENTS_DESKTOP_PLAN.md @ bb397424db0e

<!-- rcw:begin owner=source:src_d97e7f59455556e9bd83ffc9eceaf0e5 block=evidence -->
- The plan specifies that closing the last window should not stop the local runtime, while explicitly quitting the app should; the tray should indicate runtime states of starting, running, error, or stopped. [@claim:clm_1141b7548e7f9db256ffb86fa792cdd5912354488ad4e62ecb970af808f1c72c]
- A planned preload API extends window.electronAPI with methods such as getServers, saveServers, getDesktopState, setActiveServer, restartRuntime, stopRuntime, and onDesktopStateChanged, exposing a DesktopState with runtimeStatus, runtimeUrl, activeServer, workingDirectory, and error fields. [@claim:clm_3392f10cd9c30fc485ecf2e49d0b7856743def29b38fdc85d0d2d1d4441cc4a9]
- The planned desktop v1 would not bundle an Agents server, Postgres, or Electric; it would run the local builtin agents runtime from @electric-ax/agents while connecting to an external Agents server. [@claim:clm_4296e2a763e85f3aba1fef7e0bc28b46d17424ee44e1277d59e2cb35704b5de6]
- The proposed package structure includes Electron main.ts and preload.ts, a Vite config, and tray icon assets, with dependencies on @electric-ax/agents-server-ui, @electric-ax/agents, and electron. [@claim:clm_6b8542cefdc23e81ff1418141701345d9aaa846fc817f996ddcc9dde4c05260d]
- The desktop plan explicitly marks remote callback tunnelling, bundling the Agents server, Postgres, Electric, and auto-update/signing polish as out of scope for v1. [@claim:clm_729bbadb3cf070715c7a3d280eba3dca3c2c0894ba072596ecbb13c6a500e971]
- The plan proposes starting BuiltinAgentsServer with host 127.0.0.1 and port 0 so the OS picks a free port, restarting the runtime when the active Agents server changes, and noting that remote servers cannot reach the local callback URL without a later tunnel/relay design. [@claim:clm_95a8d26c94dc255601eb1098325ad2677ce1fc81bcc5aace8a3eff7438ba9b89]
- The planned desktop app is both a windowed Agents UI and a background runtime indicator/controller, with a macOS menu bar icon and tray/status icons on Windows and Linux. [@claim:clm_a44fb2a56ef973a1ca42ddf652a19303b597796a2392663489e648f3d0981fd4]
- A plan proposes a desktop app package at packages/agents-desktop that reuses the existing agents-server-ui React app and adds local desktop functionality. [@claim:clm_ced2ba0d1b7ac9a5411f13caf20f3de9955a52be0658da7fea85f98e0df1a470]
<!-- rcw:end owner=source:src_d97e7f59455556e9bd83ffc9eceaf0e5 block=evidence -->

## Researcher notes

