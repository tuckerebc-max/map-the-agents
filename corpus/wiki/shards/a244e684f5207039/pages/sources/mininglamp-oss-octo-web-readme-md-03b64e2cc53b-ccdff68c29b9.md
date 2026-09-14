---
access: public
aliases: []
claim_ids:
- clm_06ac04a20d191b2643cec1d3105cf59fd4c93b0f93ac305d66dc3a4747478b5f
- clm_093c4f407480827a2441f70b02b22315356aed11eea9310237d0dd7ee2b12132
- clm_0d20650047d91a77b346ebcd94f87f7ff1a5b3a6f922e37706cd6829271e040f
- clm_563666c1db14778b2324b9af50140a2acbd6344b892630441de5e430ac7e06db
- clm_6d8dcf0fffa51a55c83dca8c94ec91aba69f050ddd03015af9de60aa95d59a9d
- clm_7114e9ab302d865e3d3fc593d3cb0dc52b3770f51f2755dc827798921162e77d
- clm_b608a62d7b8f4005a0c4ad085dfd42eed12afa73e2e5b71b78befd618d2d4ab0
- clm_ec08e473455bfef0440bdf4ed256e442fab74e2e2dfc445123ae4f610c1bdcb8
maturity: draft
page_id: pg_0a8dbc0e2b4759d9b702ccdff68c29b9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8462aa04b91950bea8d81cce2d0697ea
title: Mininglamp-OSS/octo-web/README.md @ 03b64e2cc53b
updated_at: '2026-09-14T02:19:13Z'
---

# Mininglamp-OSS/octo-web/README.md @ 03b64e2cc53b

<!-- rcw:begin owner=source:src_8462aa04b91950bea8d81cce2d0697ea block=evidence -->
- The repository layout includes route-level pages (chat, channels, org, settings), a shared UI kit, client state, a REST/WebSocket API client, i18n resources, and an Electron bootstrap directory. [@claim:clm_06ac04a20d191b2643cec1d3105cf59fd4c93b0f93ac305d66dc3a4747478b5f]
- The client is part of an ecosystem where octo-web, Android, iOS, and admin clients connect to octo-server, which in turn links to task, AI-summary, and adapter services built on a shared Go library. [@claim:clm_093c4f407480827a2441f70b02b22315356aed11eea9310237d0dd7ee2b12132]
- The project's original scaffolding derives from TangSengDaoDaoWeb, and octo-server is described as driving a WuKongIM real-time messaging core behind this client. [@claim:clm_0d20650047d91a77b346ebcd94f87f7ff1a5b3a6f922e37706cd6829271e040f]
- The project is licensed under Apache License 2.0, with third-party attributions listed in a NOTICE file. [@claim:clm_563666c1db14778b2324b9af50140a2acbd6344b892630441de5e430ac7e06db]
- The Electron PC shell is intentionally thin: it hosts the same React app and forwards IPC for native capabilities such as tray, notifications, file drop, and auto-update, while the browser build runs without any Electron dependency. [@claim:clm_6d8dcf0fffa51a55c83dca8c94ec91aba69f050ddd03015af9de60aa95d59a9d]
- octo-web is a TypeScript/React front-end that communicates with octo-server over REST and WebSocket, and ships as both a browser build and an Electron-packaged desktop client. [@claim:clm_7114e9ab302d865e3d3fc593d3cb0dc52b3770f51f2755dc827798921162e77d]
- By default the web build expects an octo-server instance at http://localhost:8080, configurable via VITE_API_* values in a .env.local file copied from .env.example. [@claim:clm_b608a62d7b8f4005a0c4ad085dfd42eed12afa73e2e5b71b78befd618d2d4ab0]
- The UI provides first-class surfaces for AI agent conversations, including streaming replies, typing indicators, inline tool-call previews, read receipts, and agent-vs-human identity chips. [@claim:clm_ec08e473455bfef0440bdf4ed256e442fab74e2e2dfc445123ae4f610c1bdcb8]
<!-- rcw:end owner=source:src_8462aa04b91950bea8d81cce2d0697ea block=evidence -->

## Researcher notes

