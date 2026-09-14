# phodal/auto-dev -- full detail

[Back to orientation](auto-dev.md)

## Origins

- alltheagents.org-backing
- github-rename-resolution
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/phodal/auto-dev/23777fe2d3f1526694f3dd324d82595f651f28bc/2b23abe5f306fa8f.json](../../../wiki/dossiers/phodal/auto-dev/23777fe2d3f1526694f3dd324d82595f651f28bc/2b23abe5f306fa8f.json)

## specifications (1 claim(s))

- [observation/documented] AutoDev Xiuper is described as an AI-native, multi-agent development platform built on Kotlin Multiplatform, focused on document research, coding, code review, data query, artifact generation, and web interaction workflows. -- evidence: [README.md#L6-L8](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L6-L8) (`clm_47673e63cd180e4c3d686a33122e7fc67349517b5163551288398ec433249ed1`)

## components (3 claim(s))

- [observation/documented] The default Gradle build includes mpp-core (shared agent engine with tools, MCP integration, and AGENTS.md loading), mpp-ui, mpp-server (a Ktor-based remote coding agent server), viewer modules, and xiuper support modules, with mpp-idea as a composite build. -- evidence: [README.md#L33-L43](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L33-L43), [README.md#L47-L49](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L47-L49) (`clm_1ea351d1a102fcb7b1fab5ff9715ef59d8dec562e8c9684882c00aae361a2aef`)
- [observation/documented] mpp-vscode, mpp-ios, and mpp-web are maintained in the repository but are not part of the current root settings.gradle.kts default build graph. -- evidence: [README.md#L47-L49](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L47-L49) (`clm_b0e0f8995a4636dc7b22ae95513ead2998077a42476f3c1221de30c3a71b97ad`)
- [observation/documented] Five top-level agents are listed as code-backed: DocumentAgent, CodingAgent, CodeReviewAgent, ChatDBAgent, and ArtifactAgent; a web agent/WebEdit flow exists but is marked experimental. -- evidence: [README.md#L70-L77](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L70-L77) (`clm_fc1bd74cd54fb90cae02f4330e7c0a29c7eb93ff18cb6b0cb90219b840f60895`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: AGENTS.md instructs contributors to run builds and tests before completing tasks, use per-module clean instead of global clean, place temporary scripts under docs/test-scripts, and check ~/.autodev/logs/autodev-app.log for debugging. -- evidence: [AGENTS.md#L3-L9](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/AGENTS.md#L3-L9) (`clm_b05896e30b2e5cce2148e5b821ac5c3365f51d18f4cd5748336e5d86a041789c`)
- [observation/documented] Repository development practice: contributors must update all CodingAgentRenderer implementations (Kotlin, TypeScript, VSCode, and JVM CLI variants) when modifying it, and follow expect/actual and @JsExport conventions for KMP code. -- evidence: [AGENTS.md#L13-L16](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/AGENTS.md#L13-L16), [AGENTS.md#L20-L24](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/AGENTS.md#L20-L24) (`clm_e1d6dee448e2bcc545acac8ba89ccfc30530b058a49dd9e97c09ddd4a5216918`)
- [observation/documented] Repository development practice: documented commands cover CLI testing via Gradle and npm, IDEA plugin compilation, targeted renderer tests, and buildPlugin. -- evidence: [AGENTS.md#L43-L47](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/AGENTS.md#L43-L47), [AGENTS.md#L35-L39](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/AGENTS.md#L35-L39) (`clm_3960302a3d592a9f90123e3a622e7264c7c7e01dbef82e44f53eecc96fc81747`)

## skills-patterns (1 claim(s))

- [observation/documented] Agent ecosystem support includes MCP, A2A agent commands, Claude Skill loading, and SpecKit command integration. -- evidence: [README.md#L55-L64](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L55-L64) (`clm_98369a6ab8b56dc081bcdca9b827c7bacd03aacf923c6054dd625aa90463fcee`)

## interfaces (1 claim(s))

- [observation/documented] The platform targets IntelliJ IDEA, VS Code, CLI, Desktop JVM, Android, iOS, JS/WASM web, and server runtimes, with distribution via JetBrains Marketplace, VS Code Marketplace, npm, a web app, and GitHub Releases (iOS built from source). -- evidence: [README.md#L20-L25](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L20-L25), [README.md#L6-L8](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L6-L8) (`clm_1e364b01be454eaac80c73b2538f3edf6ba0c1bfad49dbd5c3f0bb0f07316427`)

## memory-state (1 claim(s))

- [observation/documented] The runtime performs automatic AGENTS.md discovery across the project hierarchy and injects project rules into prompts. -- evidence: [README.md#L55-L64](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L55-L64) (`clm_2c83ec2aa2605352a473e6a79491ceaa2a0d6b057e6395bd3524b0fbe08650ba`)

## orchestration (1 claim(s))

- [observation/documented] SubAgents follow an 'agent as tool' pattern in which the main Coding Agent invokes specialized micro-agents (NanoDSL, PlotDSL, Chart, Analysis, Codebase Investigator, and others) for focused sub-tasks. -- evidence: [README.md#L97-L97](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L97-L97), [README.md#L83-L83](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L83-L83), [README.md#L85-L95](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L85-L95) (`clm_56036429237f95dc05f57bfb9028c076f02d222e61fc4e21cc57deba999fc2a4`)

## tools-permissions (1 claim(s))

- [observation/documented] The coding agent is tool-driven, with built-in file system, grep/glob, shell, web fetch, and MCP tools plus renderer integration, per the README feature list. -- evidence: [README.md#L55-L64](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L55-L64) (`clm_c9d097556cf84596f715d49c21c55715bd856024522985399487458e080ec428`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Multi-LLM support is claimed for OpenAI, Anthropic, Google, DeepSeek, Ollama, and more, and code intelligence uses tree-sitter parsing for Java, Kotlin, Python, JS/TS, Go, Rust, and C#. -- evidence: [README.md#L55-L64](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L55-L64) (`clm_31034b51274a60f57d411864de01161f9827ea5c7d0f13af67cc8689ab1ad415`)

## limitations (1 claim(s))

- [observation/documented] Testing capability exists mainly through xiuper-e2e and E2E-oriented agent/tooling work and is not yet represented as a clearly separated top-level agent in the current code layout. -- evidence: [README.md#L79-L79](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L79-L79) (`clm_a681f694e95fb34de3ab5e6aca29c34fcbc3f66a75bdf3be4e3fedcb401f6d08`)

## relevance (1 claim(s))

- [observation/documented] The code is distributed under the MPL 2.0 license, and AutoDev 2.0 remains available on a separate branch and as a stable plugin. -- evidence: [README.md#L101-L101](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L101-L101), [README.md#L29-L29](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L29-L29) (`clm_78d56693a8edcaa4b0e8183e02009fd0107e63f4c53bd0c46a125ddb10aa2230`)

