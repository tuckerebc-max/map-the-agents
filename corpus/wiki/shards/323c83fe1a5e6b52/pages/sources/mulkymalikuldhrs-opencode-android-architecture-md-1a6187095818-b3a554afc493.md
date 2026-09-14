---
access: public
aliases: []
claim_ids:
- clm_06b73ef2e169bc74cc2449be74467790642436374b82494973419253dfdc50e0
- clm_1a302757549887bb2be1a7e096be004c28f5913dd521427e6f69a6c1e7f9fc5d
- clm_2300c952f365aae8c47c31b67948fd703cb149658e6eddc2ab92b536e8813d8d
- clm_35ffb6c285e1acd8c72a531b01c3bdcec719899648a8e4cc4380abace37f9e51
- clm_39d0b98d3dd9dda9e4f9b0ba2e016407aa721bf8374bf06a1edcb7af3ada43d7
- clm_65bbbb870160779148f4342d46b550acc60a692df498c33445d95a753c70621b
- clm_6ed6e37bf4f83150533190d86433525a25571b3167868bbfefc909aaa9447ebb
- clm_8b795014839e08d1f7e7c0910b3b6b192a7187fd9b178f6b5f814a92f03ca156
- clm_95a5fb2e98f1eb12ccf26f0165993e9d7a4a48a72334eef016a89807861cf437
- clm_ac45c502b5455375c57935f27315b01541cb76c939e2d175b11d8d1e183e656a
- clm_bda2774173097270afa60f1e9297c0182df02be3a4509184d8fc8b4ce8e651da
- clm_e7ffc10be066676ba76f6955a7fdaa867a4de34527d6d86821e824b1d74290f4
maturity: draft
page_id: pg_9449ef9969be5b07be9bb3a554afc493
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e6400a023e4657958bf1eb0ac5a4ed48
title: mulkymalikuldhrs/opencode-android/ARCHITECTURE.md @ 1a6187095818
updated_at: '2026-09-14T04:10:38Z'
---

# mulkymalikuldhrs/opencode-android/ARCHITECTURE.md @ 1a6187095818

<!-- rcw:begin owner=source:src_e6400a023e4657958bf1eb0ac5a4ed48 block=evidence -->
- The OpenCodeClient implements 50+ API endpoints spanning sessions, messages, files, providers, commands, LSP, MCP, auth, and TUI control categories. [@claim:clm_06b73ef2e169bc74cc2449be74467790642436374b82494973419253dfdc50e0]
- The project intentionally keeps dependencies minimal, using OkHttp for HTTP/SSE, AndroidX for UI, Kotlin coroutines and Flow for async work, and org.json for parsing. [@claim:clm_1a302757549887bb2be1a7e096be004c28f5913dd521427e6f69a6c1e7f9fc5d]
- The app requests INTERNET, ACCESS_NETWORK_STATE, legacy external storage, FOREGROUND_SERVICE, POST_NOTIFICATIONS (SDK 33+), and WAKE_LOCK permissions. [@claim:clm_2300c952f365aae8c47c31b67948fd703cb149658e6eddc2ab92b536e8813d8d]
- SessionManager is the central state coordinator tracking current session, session list, SSE event stream, message state, and connection state, exposed via StateFlow/SharedFlow. [@claim:clm_35ffb6c285e1acd8c72a531b01c3bdcec719899648a8e4cc4380abace37f9e51]
- The UI uses Material Design 3 with a dark theme as primary identity, bottom-tab navigation with four sections, and dynamic color support on Android 12+. [@claim:clm_39d0b98d3dd9dda9e4f9b0ba2e016407aa721bf8374bf06a1edcb7af3ada43d7]
- Main UI components include ConnectionActivity (connection wizard with health check), MainActivity with bottom navigation, and Chat, Terminal, FileManager, and CodeEditor fragments. [@claim:clm_65bbbb870160779148f4342d46b550acc60a692df498c33445d95a753c70621b]
- Connection settings (server URL, username, password, auto-connect) are persisted in SharedPreferences, using EncryptedSharedPreferences when available on newer Android versions. [@claim:clm_6ed6e37bf4f83150533190d86433525a25571b3167868bbfefc909aaa9447ebb]
- The app communicates with the server over HTTP with SSE for real-time streaming, WebSocket for the terminal shell, and TLS (HTTPS/WSS) as the transport security layer. [@claim:clm_8b795014839e08d1f7e7c0910b3b6b192a7187fd9b178f6b5f814a92f03ca156]
- The app uses HTTP Basic Authentication included in the Authorization header of every request; cleartext traffic is disabled by default except for localhost in development. [@claim:clm_95a5fb2e98f1eb12ccf26f0165993e9d7a4a48a72334eef016a89807861cf437]
- OpenCodeService is a foreground service (dataSync type) that keeps the SSE connection alive in the background and shows a persistent notification. [@claim:clm_ac45c502b5455375c57935f27315b01541cb76c939e2d175b11d8d1e183e656a]
- The architecture follows a thin client-server model: AI processing, file operations, and command execution happen on the server, while the app handles only UI presentation and interaction. [@claim:clm_bda2774173097270afa60f1e9297c0182df02be3a4509184d8fc8b4ce8e651da]
- The app targets Android 7.0 (API 24) minimum and SDK 34, is written in Kotlin, uses package ai.opencode.mobile, and is version 2.0.0 (versionCode 2). [@claim:clm_e7ffc10be066676ba76f6955a7fdaa867a4de34527d6d86821e824b1d74290f4]
<!-- rcw:end owner=source:src_e6400a023e4657958bf1eb0ac5a4ed48 block=evidence -->

## Researcher notes

