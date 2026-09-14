# opencode-android (`opencode-android`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: mulkymalikuldhrs
- License: MIT
- Language: Kotlin
- Interface: platforms=IDE; install=Download APK from GitHub Releases, or build from source via Gradle (./gradlew assembleDebug / installDebug)
- Model providers: none on-device — 75+ providers configured on the OpenCode server; the app only displays/switches server-exposed providers
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [mulkymalikuldhrs/opencode-android](../../repos/mulkymalikuldhrs/opencode-android.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Native Android client for the OpenCode AI coding agent — combines SSE streaming AI chat, remote terminal (WebSocket), code editor with syntax highlighting, and file manager in a Material Design 3 dark theme. Thin-client architecture where all heavy lifting runs on the OpenCode server.

(captured site page body (agents/opencode-android.md), not a verified repo-code finding)
The OpenCode agent lives in a desktop terminal, which leaves its sessions unreachable from a phone. This Kotlin app (Jetpack Compose, Material Design 3, MVVM) connects to a running OpenCode server and mirrors it on Android: SSE-streaming AI chat, a WebSocket terminal that executes on the server machine, a code editor with syntax highlighting, and a file manager, all in a dark Material 3 interface. The README is explicit about the architecture's limits — nothing works offline, the phone manages no API keys, terminal commands execute on the server host, and security hardening (certificate pinning, encrypted preferences) is only partially implemented. APKs ship via GitHub Releases for Android 7.0+, and a Termux guide documents running the server on-device. It is a small early-stage project (27 stars, 70 commits) marked for education and research use. Developers running OpenCode who want to monitor and steer sessions from Android are the audience.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/opencode-android.md)
