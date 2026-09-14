---
access: public
aliases: []
claim_ids:
- clm_36b5129967135d141a9cef627a65ce7e9a87f32592a6893c8085f0b48b160f6c
- clm_39d0b98d3dd9dda9e4f9b0ba2e016407aa721bf8374bf06a1edcb7af3ada43d7
- clm_4b056b000b1b94550ad130857738f8304a667a6c3188efe28c76450437a6c0f5
- clm_59109a9d66c6174c5c016da985069bbdab3296a7ec6926f6c0526312c0865105
- clm_67c0276a0c8ac364e7efe91a790646585c199771f0a3a21db615d237745e1f19
- clm_6b47efb18c8ebf2ffa815b4409fe0355f34f377c673f389911c346f4218a119f
- clm_8b795014839e08d1f7e7c0910b3b6b192a7187fd9b178f6b5f814a92f03ca156
- clm_bda2774173097270afa60f1e9297c0182df02be3a4509184d8fc8b4ce8e651da
- clm_d7838936fa626d94250d46eafb08c80c9d3441c6a2a469cfb6c0b45600043de6
maturity: draft
page_id: pg_313eeebeac8052aab949dd11efedf29d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3db9ebfff63a57209e2341ced72f04eb
title: mulkymalikuldhrs/opencode-android/README.md @ 1a6187095818
updated_at: '2026-09-14T04:10:38Z'
---

# mulkymalikuldhrs/opencode-android/README.md @ 1a6187095818

<!-- rcw:begin owner=source:src_3db9ebfff63a57209e2341ced72f04eb block=evidence -->
- Opencode Android is a native Android client for the OpenCode AI coding agent; it requires a running OpenCode server and is not a standalone AI tool. [@claim:clm_36b5129967135d141a9cef627a65ce7e9a87f32592a6893c8085f0b48b160f6c]
- The UI uses Material Design 3 with a dark theme as primary identity, bottom-tab navigation with four sections, and dynamic color support on Android 12+. [@claim:clm_39d0b98d3dd9dda9e4f9b0ba2e016407aa721bf8374bf06a1edcb7af3ada43d7]
- Documented limitations: no AI runs on the device, terminal commands execute on the server machine, file operations target the server filesystem, and there is no offline functionality. [@claim:clm_4b056b000b1b94550ad130857738f8304a667a6c3188efe28c76450437a6c0f5]
- Repository development practice: contributors should follow existing Kotlin style, write unit tests, ensure ./gradlew test passes, keep PRs focused, and follow a fork-branch-PR workflow. [@claim:clm_59109a9d66c6174c5c016da985069bbdab3296a7ec6926f6c0526312c0865105]
- Repository development practice: building requires Android Studio Hedgehog+, JDK 17+, Android SDK API 34, and the included Gradle 8.x wrapper; debug/release builds and unit and instrumented tests run via Gradle tasks. [@claim:clm_67c0276a0c8ac364e7efe91a790646585c199771f0a3a21db615d237745e1f19]
- A maturity note states the code editor and file manager support only basic operations, and security hardening such as certificate pinning and encrypted preferences is only partially implemented. [@claim:clm_6b47efb18c8ebf2ffa815b4409fe0355f34f377c673f389911c346f4218a119f]
- The app communicates with the server over HTTP with SSE for real-time streaming, WebSocket for the terminal shell, and TLS (HTTPS/WSS) as the transport security layer. [@claim:clm_8b795014839e08d1f7e7c0910b3b6b192a7187fd9b178f6b5f814a92f03ca156]
- The architecture follows a thin client-server model: AI processing, file operations, and command execution happen on the server, while the app handles only UI presentation and interaction. [@claim:clm_bda2774173097270afa60f1e9297c0182df02be3a4509184d8fc8b4ce8e651da]
- The project is explicitly provided for educational and research purposes only, with authors disclaiming liability for its use. [@claim:clm_d7838936fa626d94250d46eafb08c80c9d3441c6a2a469cfb6c0b45600043de6]
<!-- rcw:end owner=source:src_3db9ebfff63a57209e2341ced72f04eb block=evidence -->

## Researcher notes

