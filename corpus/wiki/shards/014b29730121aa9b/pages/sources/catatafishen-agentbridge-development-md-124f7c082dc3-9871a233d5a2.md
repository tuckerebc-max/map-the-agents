---
access: public
aliases: []
claim_ids:
- clm_19242d54bb7e1cdfdaef9042ca269d2d7c1ed5697ce38e39aab5664405572981
- clm_2afd9d890f85af613bd60ce8a308e9b5930ea14e3d8641feeee40df233aa7d98
- clm_5b755d2d5c4dfc5642a3599e739e4b79e063d95f4e0e5639d93e6ff5937931eb
- clm_8a0096434ea9902cf184244dc53bbf0f4ca0357bb2109aee4f0ea8295c34a1e6
- clm_9ae6b247be1606d74b118c3c7b06de7a63f3fbb1e482cb2f4141326f43baafd3
- clm_b76aa0aae8156d0a5b9ddf1a202b2192834f734a633e1001149ec94f2d921dfe
- clm_f0cffae3b4741825d2b7ae4b0ab69b235baf9102e1c5a22e4a31b1983a24692e
maturity: draft
page_id: pg_6821cc66651652509b419871a233d5a2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_2c1a93c3237959a99d58abdbf4a9cf2c
title: catatafishen/agentbridge/DEVELOPMENT.md @ 124f7c082dc3
updated_at: '2026-09-14T03:40:39Z'
---

# catatafishen/agentbridge/DEVELOPMENT.md @ 124f7c082dc3

<!-- rcw:begin owner=source:src_2c1a93c3237959a99d58abdbf4a9cf2c block=evidence -->
- Repository development practice: tests run via Gradle (./gradlew test, :plugin-core:test, :mcp-server:test, with -Dinclude.integration=true for integration tests), and the project builds two plugin ZIPs (plugin-core and plugin-experimental) via buildPlugin tasks. [@claim:clm_19242d54bb7e1cdfdaef9042ca269d2d7c1ed5697ce38e39aab5664405572981]
- GitHub Copilot surfaces ACP resource references only as tagged-file metadata without content, so the plugin appends referenced file content as plain text after the user's message as a workaround. [@claim:clm_2afd9d890f85af613bd60ce8a308e9b5930ea14e3d8641feeee40df233aa7d98]
- The bridge port is shared via a file at ~/.copilot/psi-bridge.json, which the MCP server reads to reach the in-IDE HTTP service. [@claim:clm_5b755d2d5c4dfc5642a3599e739e4b79e063d95f4e0e5639d93e6ff5937931eb]
- A prolonged EDT freeze (30+ seconds) can permanently stall the JCEF off-screen renderer; defenses include an EdtFreezeRecovery heartbeat monitor and a 2-second cooldown on file-open navigations to prevent cascading VCS git log/blame operations. [@claim:clm_8a0096434ea9902cf184244dc53bbf0f4ca0357bb2109aee4f0ea8295c34a1e6]
- Development requires JDK 21 (Gradle JVM pinned via gradle.properties) and an installed, authenticated GitHub Copilot CLI; the Gradle wrapper JAR is not checked into the repository. [@claim:clm_9ae6b247be1606d74b118c3c7b06de7a63f3fbb1e482cb2f4141326f43baafd3]
- For Copilot, built-in file operations are denied so all writes route through IntelliJ's Document API; denied permission kinds include edit, create, read, execute, and runInTerminal, with an auto-retry prompting the agent to use write_file instead. [@claim:clm_b76aa0aae8156d0a5b9ddf1a202b2192834f734a633e1001149ec94f2d921dfe]
- Every file write via write_file triggers document commit, import optimization, and reformatting inside a single undoable command group on the EDT. [@claim:clm_f0cffae3b4741825d2b7ae4b0ab69b235baf9102e1c5a22e4a31b1983a24692e]
<!-- rcw:end owner=source:src_2c1a93c3237959a99d58abdbf4a9cf2c block=evidence -->

## Researcher notes

