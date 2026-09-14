---
access: public
aliases: []
claim_ids:
- clm_25d17b3503f0f70a56d4c6627e8e455ba961183096a27edd4b96b0a7361731a3
- clm_53c7a67690d76c01c06a1994da160317c73ed56295e32cbc8ee35fc2e846556c
- clm_9ce46fb776e9339fbb0576259ef05fc3efef440dbd82dcc66070411e0a766c92
- clm_bedebd5f20a476ed8e607765efbcc4ffa41a4d6c557954a596018a4ea025cc53
- clm_ced6f1915ba54d65581d75d1bd0c5333d53c3c99bba7ccf99a612c6771c8e287
- clm_d95058f42c060916e81dce858bdd24eadd56aabbc760929ae5b5fa8602e8be3d
- clm_ead391c3adca1bf46277370b6d0b44511af3fdf2de7ee3913ef7af28e5cbb4aa
- clm_fe72318bffa3df25e245e6cd0345d61b63ef13d9ef81083d1c302e3cc7c5b49b
maturity: draft
page_id: pg_222b77b9339b563191df597f2e859e70
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_586e9430154a57f295c69294ad57ee5c
title: nimbalyst/nimbalyst/README.md @ d6e1d008d9ee
updated_at: '2026-09-14T03:10:36Z'
---

# nimbalyst/nimbalyst/README.md @ d6e1d008d9ee

<!-- rcw:begin owner=source:src_586e9430154a57f295c69294ad57ee5c block=evidence -->
- The repository is a TypeScript/Electron npm-workspaces monorepo with packages for the Electron desktop app, a native SwiftUI iOS app, cross-platform runtime services (AI, sync, Lexical editor), a collab-protocol wire-format package, an extension SDK, and built-in extensions. [@claim:clm_25d17b3503f0f70a56d4c6627e8e455ba961183096a27edd4b96b0a7361731a3]
- The app sends anonymous usage analytics to PostHog, states it collects no PII, file contents/paths, API keys, or document/session/chat content, uses a random anonymous install ID, and offers an opt-out in Settings. [@claim:clm_53c7a67690d76c01c06a1994da160317c73ed56295e32cbc8ee35fc2e846556c]
- Desktop builds are distributed as macOS .dmg (Apple Silicon and Intel), Windows .exe, Linux .deb, and AppImage, with stated OS requirements such as macOS 12+ and Windows 10+; fresh installs default to the stable release channel with an opt-in alpha channel. [@claim:clm_9ce46fb776e9339fbb0576259ef05fc3efef440dbd82dcc66070411e0a766c92]
- Acknowledged building blocks include Electron, Meta's Lexical, React, Monaco Editor, and Excalidraw; the collaboration sync server is a separate Cloudflare Worker project reached at wss://sync.nimbalyst.com via the collab-protocol wire format. [@claim:clm_bedebd5f20a476ed8e607765efbcc4ffa41a4d6c557954a596018a4ea025cc53]
- Every editor, built-in or custom, goes through the same EditorHost contract, making pluggable editors for arbitrary file types first-class; existing extensions include an Astro website editor, visual git log, mindmap, slides, and a 3D object editor. [@claim:clm_ced6f1915ba54d65581d75d1bd0c5333d53c3c99bba7ccf99a612c6771c8e287]
- Content and status are stored as plain markdown files and workflows as slash commands inside the user's git repo, with no proprietary store, and parallel agent sessions are each isolated in their own git worktree. [@claim:clm_d95058f42c060916e81dce858bdd24eadd56aabbc760929ae5b5fa8602e8be3d]
- The app acts as an MCP client that can connect any MCP server and renders tool results as visual widgets rather than raw JSON. [@claim:clm_ead391c3adca1bf46277370b6d0b44511af3fdf2de7ee3913ef7af28e5cbb4aa]
- Nimbalyst is described as an open-source, MIT-licensed visual workspace for building with coding agents such as Codex, Claude Code, and OpenCode, shipped as a desktop app for macOS, Windows, and Linux with an iOS companion app. [@claim:clm_fe72318bffa3df25e245e6cd0345d61b63ef13d9ef81083d1c302e3cc7c5b49b]
<!-- rcw:end owner=source:src_586e9430154a57f295c69294ad57ee5c block=evidence -->

## Researcher notes

