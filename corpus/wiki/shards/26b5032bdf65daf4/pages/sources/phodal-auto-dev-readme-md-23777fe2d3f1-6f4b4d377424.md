---
access: public
aliases: []
claim_ids:
- clm_1e364b01be454eaac80c73b2538f3edf6ba0c1bfad49dbd5c3f0bb0f07316427
- clm_1ea351d1a102fcb7b1fab5ff9715ef59d8dec562e8c9684882c00aae361a2aef
- clm_2c83ec2aa2605352a473e6a79491ceaa2a0d6b057e6395bd3524b0fbe08650ba
- clm_31034b51274a60f57d411864de01161f9827ea5c7d0f13af67cc8689ab1ad415
- clm_47673e63cd180e4c3d686a33122e7fc67349517b5163551288398ec433249ed1
- clm_56036429237f95dc05f57bfb9028c076f02d222e61fc4e21cc57deba999fc2a4
- clm_78d56693a8edcaa4b0e8183e02009fd0107e63f4c53bd0c46a125ddb10aa2230
- clm_98369a6ab8b56dc081bcdca9b827c7bacd03aacf923c6054dd625aa90463fcee
- clm_a681f694e95fb34de3ab5e6aca29c34fcbc3f66a75bdf3be4e3fedcb401f6d08
- clm_b0e0f8995a4636dc7b22ae95513ead2998077a42476f3c1221de30c3a71b97ad
- clm_c9d097556cf84596f715d49c21c55715bd856024522985399487458e080ec428
- clm_fc1bd74cd54fb90cae02f4330e7c0a29c7eb93ff18cb6b0cb90219b840f60895
maturity: draft
page_id: pg_39a77f55ee5c50b190976f4b4d377424
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bd0ea77e4c375982b31ad69786a73052
title: phodal/auto-dev/README.md @ 23777fe2d3f1
updated_at: '2026-09-14T02:31:23Z'
---

# phodal/auto-dev/README.md @ 23777fe2d3f1

<!-- rcw:begin owner=source:src_bd0ea77e4c375982b31ad69786a73052 block=evidence -->
- The platform targets IntelliJ IDEA, VS Code, CLI, Desktop JVM, Android, iOS, JS/WASM web, and server runtimes, with distribution via JetBrains Marketplace, VS Code Marketplace, npm, a web app, and GitHub Releases (iOS built from source). [@claim:clm_1e364b01be454eaac80c73b2538f3edf6ba0c1bfad49dbd5c3f0bb0f07316427]
- The default Gradle build includes mpp-core (shared agent engine with tools, MCP integration, and AGENTS.md loading), mpp-ui, mpp-server (a Ktor-based remote coding agent server), viewer modules, and xiuper support modules, with mpp-idea as a composite build. [@claim:clm_1ea351d1a102fcb7b1fab5ff9715ef59d8dec562e8c9684882c00aae361a2aef]
- The runtime performs automatic AGENTS.md discovery across the project hierarchy and injects project rules into prompts. [@claim:clm_2c83ec2aa2605352a473e6a79491ceaa2a0d6b057e6395bd3524b0fbe08650ba]
- Multi-LLM support is claimed for OpenAI, Anthropic, Google, DeepSeek, Ollama, and more, and code intelligence uses tree-sitter parsing for Java, Kotlin, Python, JS/TS, Go, Rust, and C#. [@claim:clm_31034b51274a60f57d411864de01161f9827ea5c7d0f13af67cc8689ab1ad415]
- AutoDev Xiuper is described as an AI-native, multi-agent development platform built on Kotlin Multiplatform, focused on document research, coding, code review, data query, artifact generation, and web interaction workflows. [@claim:clm_47673e63cd180e4c3d686a33122e7fc67349517b5163551288398ec433249ed1]
- SubAgents follow an 'agent as tool' pattern in which the main Coding Agent invokes specialized micro-agents (NanoDSL, PlotDSL, Chart, Analysis, Codebase Investigator, and others) for focused sub-tasks. [@claim:clm_56036429237f95dc05f57bfb9028c076f02d222e61fc4e21cc57deba999fc2a4]
- The code is distributed under the MPL 2.0 license, and AutoDev 2.0 remains available on a separate branch and as a stable plugin. [@claim:clm_78d56693a8edcaa4b0e8183e02009fd0107e63f4c53bd0c46a125ddb10aa2230]
- Agent ecosystem support includes MCP, A2A agent commands, Claude Skill loading, and SpecKit command integration. [@claim:clm_98369a6ab8b56dc081bcdca9b827c7bacd03aacf923c6054dd625aa90463fcee]
- Testing capability exists mainly through xiuper-e2e and E2E-oriented agent/tooling work and is not yet represented as a clearly separated top-level agent in the current code layout. [@claim:clm_a681f694e95fb34de3ab5e6aca29c34fcbc3f66a75bdf3be4e3fedcb401f6d08]
- mpp-vscode, mpp-ios, and mpp-web are maintained in the repository but are not part of the current root settings.gradle.kts default build graph. [@claim:clm_b0e0f8995a4636dc7b22ae95513ead2998077a42476f3c1221de30c3a71b97ad]
- The coding agent is tool-driven, with built-in file system, grep/glob, shell, web fetch, and MCP tools plus renderer integration, per the README feature list. [@claim:clm_c9d097556cf84596f715d49c21c55715bd856024522985399487458e080ec428]
- Five top-level agents are listed as code-backed: DocumentAgent, CodingAgent, CodeReviewAgent, ChatDBAgent, and ArtifactAgent; a web agent/WebEdit flow exists but is marked experimental. [@claim:clm_fc1bd74cd54fb90cae02f4330e7c0a29c7eb93ff18cb6b0cb90219b840f60895]
<!-- rcw:end owner=source:src_bd0ea77e4c375982b31ad69786a73052 block=evidence -->

## Researcher notes

