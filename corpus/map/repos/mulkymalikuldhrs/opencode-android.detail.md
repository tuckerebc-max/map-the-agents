# mulkymalikuldhrs/opencode-android -- full detail

[Back to orientation](opencode-android.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/mulkymalikuldhrs/opencode-android/1a61870958185217232dd7056e73f3dde067710b/910c35b32f3924ae.json](../../../wiki/dossiers/mulkymalikuldhrs/opencode-android/1a61870958185217232dd7056e73f3dde067710b/910c35b32f3924ae.json)

## specifications (2 claim(s))

- [observation/documented] Opencode Android is a native Android client for the OpenCode AI coding agent; it requires a running OpenCode server and is not a standalone AI tool. -- evidence: [README.md#L28-L28](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L28-L28), [README.md#L26-L26](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L26-L26) (`clm_36b5129967135d141a9cef627a65ce7e9a87f32592a6893c8085f0b48b160f6c`)
- [observation/documented] The app targets Android 7.0 (API 24) minimum and SDK 34, is written in Kotlin, uses package ai.opencode.mobile, and is version 2.0.0 (versionCode 2). -- evidence: [ARCHITECTURE.md#L398-L405](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L398-L405), [ARCHITECTURE.md#L32-L37](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L32-L37) (`clm_e7ffc10be066676ba76f6955a7fdaa867a4de34527d6d86821e824b1d74290f4`)

## components (3 claim(s))

- [observation/documented] Main UI components include ConnectionActivity (connection wizard with health check), MainActivity with bottom navigation, and Chat, Terminal, FileManager, and CodeEditor fragments. -- evidence: [ARCHITECTURE.md#L313-L316](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L313-L316), [ARCHITECTURE.md#L114-L119](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L114-L119), [ARCHITECTURE.md#L107-L110](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L107-L110) (`clm_65bbbb870160779148f4342d46b550acc60a692df498c33445d95a753c70621b`)
- [observation/documented] SessionManager is the central state coordinator tracking current session, session list, SSE event stream, message state, and connection state, exposed via StateFlow/SharedFlow. -- evidence: [ARCHITECTURE.md#L285-L285](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L285-L285), [ARCHITECTURE.md#L287-L291](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L287-L291), [ARCHITECTURE.md#L137-L139](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L137-L139), [ARCHITECTURE.md#L293-L293](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L293-L293) (`clm_35ffb6c285e1acd8c72a531b01c3bdcec719899648a8e4cc4380abace37f9e51`)
- [observation/documented] OpenCodeService is a foreground service (dataSync type) that keeps the SSE connection alive in the background and shows a persistent notification. -- evidence: [ARCHITECTURE.md#L143-L145](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L143-L145), [ARCHITECTURE.md#L348-L348](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L348-L348), [ARCHITECTURE.md#L354-L354](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L354-L354) (`clm_ac45c502b5455375c57935f27315b01541cb76c939e2d175b11d8d1e183e656a`)

## design-choices (2 claim(s))

- [observation/documented] The architecture follows a thin client-server model: AI processing, file operations, and command execution happen on the server, while the app handles only UI presentation and interaction. -- evidence: [README.md#L28-L28](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L28-L28), [ARCHITECTURE.md#L43-L43](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L43-L43) (`clm_bda2774173097270afa60f1e9297c0182df02be3a4509184d8fc8b4ce8e651da`)
- [observation/documented] The UI uses Material Design 3 with a dark theme as primary identity, bottom-tab navigation with four sections, and dynamic color support on Android 12+. -- evidence: [README.md#L47-L47](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L47-L47), [ARCHITECTURE.md#L49-L49](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L49-L49) (`clm_39d0b98d3dd9dda9e4f9b0ba2e016407aa721bf8374bf06a1edcb7af3ada43d7`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors should follow existing Kotlin style, write unit tests, ensure ./gradlew test passes, keep PRs focused, and follow a fork-branch-PR workflow. -- evidence: [README.md#L373-L377](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L373-L377), [README.md#L381-L385](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L381-L385) (`clm_59109a9d66c6174c5c016da985069bbdab3296a7ec6926f6c0526312c0865105`)
- [observation/documented] Repository development practice: building requires Android Studio Hedgehog+, JDK 17+, Android SDK API 34, and the included Gradle 8.x wrapper; debug/release builds and unit and instrumented tests run via Gradle tasks. -- evidence: [README.md#L353-L353](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L353-L353), [README.md#L350-L350](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L350-L350), [README.md#L271-L271](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L271-L271), [README.md#L331-L334](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L331-L334), [README.md#L277-L278](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L277-L278) (`clm_67c0276a0c8ac364e7efe91a790646585c199771f0a3a21db615d237745e1f19`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The app communicates with the server over HTTP with SSE for real-time streaming, WebSocket for the terminal shell, and TLS (HTTPS/WSS) as the transport security layer. -- evidence: [ARCHITECTURE.md#L30-L30](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L30-L30), [README.md#L101-L113](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L101-L113), [README.md#L86-L91](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L86-L91) (`clm_8b795014839e08d1f7e7c0910b3b6b192a7187fd9b178f6b5f814a92f03ca156`)
- [observation/documented] The OpenCodeClient implements 50+ API endpoints spanning sessions, messages, files, providers, commands, LSP, MCP, auth, and TUI control categories. -- evidence: [ARCHITECTURE.md#L30-L30](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L30-L30), [ARCHITECTURE.md#L249-L261](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L249-L261) (`clm_06b73ef2e169bc74cc2449be74467790642436374b82494973419253dfdc50e0`)
- [observation/documented] The app uses HTTP Basic Authentication included in the Authorization header of every request; cleartext traffic is disabled by default except for localhost in development. -- evidence: [ARCHITECTURE.md#L362-L362](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L362-L362), [ARCHITECTURE.md#L376-L378](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L376-L378), [ARCHITECTURE.md#L368-L368](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L368-L368) (`clm_95a5fb2e98f1eb12ccf26f0165993e9d7a4a48a72334eef016a89807861cf437`)

## memory-state (1 claim(s))

- [observation/documented] Connection settings (server URL, username, password, auto-connect) are persisted in SharedPreferences, using EncryptedSharedPreferences when available on newer Android versions. -- evidence: [ARCHITECTURE.md#L372-L372](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L372-L372), [ARCHITECTURE.md#L297-L301](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L297-L301) (`clm_6ed6e37bf4f83150533190d86433525a25571b3167868bbfefc909aaa9447ebb`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The app requests INTERNET, ACCESS_NETWORK_STATE, legacy external storage, FOREGROUND_SERVICE, POST_NOTIFICATIONS (SDK 33+), and WAKE_LOCK permissions. -- evidence: [ARCHITECTURE.md#L382-L388](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L382-L388) (`clm_2300c952f365aae8c47c31b67948fd703cb149658e6eddc2ab92b536e8813d8d`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project intentionally keeps dependencies minimal, using OkHttp for HTTP/SSE, AndroidX for UI, Kotlin coroutines and Flow for async work, and org.json for parsing. -- evidence: [ARCHITECTURE.md#L47-L47](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L47-L47), [ARCHITECTURE.md#L45-L45](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L45-L45), [ARCHITECTURE.md#L53-L53](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/ARCHITECTURE.md#L53-L53) (`clm_1a302757549887bb2be1a7e096be004c28f5913dd521427e6f69a6c1e7f9fc5d`)

## limitations (2 claim(s))

- [observation/documented] Documented limitations: no AI runs on the device, terminal commands execute on the server machine, file operations target the server filesystem, and there is no offline functionality. -- evidence: [README.md#L62-L70](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L62-L70) (`clm_4b056b000b1b94550ad130857738f8304a667a6c3188efe28c76450437a6c0f5`)
- [observation/documented] A maturity note states the code editor and file manager support only basic operations, and security hardening such as certificate pinning and encrypted preferences is only partially implemented. -- evidence: [README.md#L235-L235](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L235-L235) (`clm_6b47efb18c8ebf2ffa815b4409fe0355f34f377c673f389911c346f4218a119f`)

## relevance (1 claim(s))

- [observation/documented] The project is explicitly provided for educational and research purposes only, with authors disclaiming liability for its use. -- evidence: [README.md#L389-L389](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L389-L389), [README.md#L391-L391](https://github.com/mulkymalikuldhrs/opencode-android/blob/1a61870958185217232dd7056e73f3dde067710b/README.md#L391-L391) (`clm_d7838936fa626d94250d46eafb08c80c9d3441c6a2a469cfb6c0b45600043de6`)

