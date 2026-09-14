# mulkymalikuldhrs/opencode-android

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 1a6187095818 @ 910c35b32f3924ae

## Summary (orientation draft, not independently verified)

Opencode Android is a documented thin-client Android app for the OpenCode AI coding agent, connecting over HTTP/SSE/WebSocket to a required server that performs all AI, shell, and file operations. Claims are drawn from README and ARCHITECTURE.md product documentation; the previously flagged Basic Auth claim was revised to remove an uncited implementation detail. Evidence coverage: 135 of 368 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Opencode Android is a native Android client for the OpenCode AI coding agent; it requires a running OpenCode server and is not a standalone AI tool. -- evidence: [README.md#L28-L28](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L28-L28), [README.md#L26-L26](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L26-L26)
  - [observation/documented] The app targets Android 7.0 (API 24) minimum and SDK 34, is written in Kotlin, uses package ai.opencode.mobile, and is version 2.0.0 (versionCode 2). -- evidence: [ARCHITECTURE.md#L398-L405](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L398-L405), [ARCHITECTURE.md#L32-L37](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L32-L37)
- components (3 claim(s)):
  - [observation/documented] Main UI components include ConnectionActivity (connection wizard with health check), MainActivity with bottom navigation, and Chat, Terminal, FileManager, and CodeEditor fragments. -- evidence: [ARCHITECTURE.md#L313-L316](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L313-L316), [ARCHITECTURE.md#L114-L119](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L114-L119), [ARCHITECTURE.md#L107-L110](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L107-L110)
  - [observation/documented] SessionManager is the central state coordinator tracking current session, session list, SSE event stream, message state, and connection state, exposed via StateFlow/SharedFlow. -- evidence: [ARCHITECTURE.md#L285-L285](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L285-L285), [ARCHITECTURE.md#L287-L291](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L287-L291), [ARCHITECTURE.md#L137-L139](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L137-L139), [ARCHITECTURE.md#L293-L293](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L293-L293)
- design-choices (2 claim(s)):
  - [observation/documented] The architecture follows a thin client-server model: AI processing, file operations, and command execution happen on the server, while the app handles only UI presentation and interaction. -- evidence: [README.md#L28-L28](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L28-L28), [ARCHITECTURE.md#L43-L43](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L43-L43)
  - [observation/documented] The UI uses Material Design 3 with a dark theme as primary identity, bottom-tab navigation with four sections, and dynamic color support on Android 12+. -- evidence: [README.md#L47-L47](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L47-L47), [ARCHITECTURE.md#L49-L49](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L49-L49)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors should follow existing Kotlin style, write unit tests, ensure ./gradlew test passes, keep PRs focused, and follow a fork-branch-PR workflow. -- evidence: [README.md#L373-L377](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L373-L377), [README.md#L381-L385](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L381-L385)
  - [observation/documented] Repository development practice: building requires Android Studio Hedgehog+, JDK 17+, Android SDK API 34, and the included Gradle 8.x wrapper; debug/release builds and unit and instrumented tests run via Gradle tasks. -- evidence: [README.md#L353-L353](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L353-L353), [README.md#L350-L350](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L350-L350), [README.md#L271-L271](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L271-L271), [README.md#L331-L334](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L331-L334), [README.md#L277-L278](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L277-L278)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The app communicates with the server over HTTP with SSE for real-time streaming, WebSocket for the terminal shell, and TLS (HTTPS/WSS) as the transport security layer. -- evidence: [ARCHITECTURE.md#L30-L30](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L30-L30), [README.md#L101-L113](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L101-L113), [README.md#L86-L91](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L86-L91)
More evidence: [full detail](opencode-android.detail.md)

Metadata and full claim list: [full detail](opencode-android.detail.md)
Human notes ([notes](opencode-android.notes.md), never overwritten by build)

[Back to map index](../../index.md)
