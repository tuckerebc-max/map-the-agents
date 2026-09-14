# phodal/auto-dev

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing, github-rename-resolution, github-verified-rename - Projects: navy-yard, Observatory
Formerly: unit-mesh/auto-dev (github id 627920448).
Latest snapshot: commit 23777fe2d3f1 @ 2b23abe5f306fa8f

## Summary (orientation draft, not independently verified)

AutoDev Xiuper is documented as an AI-native, multi-agent development platform built on Kotlin Multiplatform, with code-backed agents, sub-agent orchestration, multi-LLM and MCP support, and distribution across IDE, CLI, web, desktop, and mobile targets. Repository development guidance in AGENTS.md covers contributor build, test, and coding conventions.

## Source coverage

Source coverage (partial): 2 of 3 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] AutoDev Xiuper is described as an AI-native, multi-agent development platform built on Kotlin Multiplatform, focused on document research, coding, code review, data query, artifact generation, and web interaction workflows. -- evidence: [README.md#L6-L8](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L6-L8)
- components (3 claim(s)):
  - [observation/documented] The default Gradle build includes mpp-core (shared agent engine with tools, MCP integration, and AGENTS.md loading), mpp-ui, mpp-server (a Ktor-based remote coding agent server), viewer modules, and xiuper support modules, with mpp-idea as a composite build. -- evidence: [README.md#L33-L43](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L33-L43), [README.md#L47-L49](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L47-L49)
  - [observation/documented] mpp-vscode, mpp-ios, and mpp-web are maintained in the repository but are not part of the current root settings.gradle.kts default build graph. -- evidence: [README.md#L47-L49](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L47-L49)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs contributors to run builds and tests before completing tasks, use per-module clean instead of global clean, place temporary scripts under docs/test-scripts, and check ~/.autodev/logs/autodev-app.log for debugging. -- evidence: [AGENTS.md#L3-L9](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/AGENTS.md#L3-L9)
  - [observation/documented] Repository development practice: contributors must update all CodingAgentRenderer implementations (Kotlin, TypeScript, VSCode, and JVM CLI variants) when modifying it, and follow expect/actual and @JsExport conventions for KMP code. -- evidence: [AGENTS.md#L13-L16](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/AGENTS.md#L13-L16), [AGENTS.md#L20-L24](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/AGENTS.md#L20-L24)
- skills-patterns (1 claim(s)):
  - [observation/documented] Agent ecosystem support includes MCP, A2A agent commands, Claude Skill loading, and SpecKit command integration. -- evidence: [README.md#L55-L64](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L55-L64)
- interfaces (1 claim(s)):
  - [observation/documented] The platform targets IntelliJ IDEA, VS Code, CLI, Desktop JVM, Android, iOS, JS/WASM web, and server runtimes, with distribution via JetBrains Marketplace, VS Code Marketplace, npm, a web app, and GitHub Releases (iOS built from source). -- evidence: [README.md#L20-L25](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L20-L25), [README.md#L6-L8](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L6-L8)
- memory-state (1 claim(s)):
  - [observation/documented] The runtime performs automatic AGENTS.md discovery across the project hierarchy and injects project rules into prompts. -- evidence: [README.md#L55-L64](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L55-L64)
- orchestration (1 claim(s)):
  - [observation/documented] SubAgents follow an 'agent as tool' pattern in which the main Coding Agent invokes specialized micro-agents (NanoDSL, PlotDSL, Chart, Analysis, Codebase Investigator, and others) for focused sub-tasks. -- evidence: [README.md#L97-L97](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L97-L97), [README.md#L83-L83](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L83-L83), [README.md#L85-L95](https://github.com/phodal/auto-dev/blob/23777fe2d3f1526694f3dd324d82595f651f28bc/README.md#L85-L95)
- tools-permissions (1 claim(s)):
More evidence: [full detail](auto-dev.detail.md)

Metadata and full claim list: [full detail](auto-dev.detail.md)
Human notes ([notes](auto-dev.notes.md), never overwritten by build)

[Back to map index](../../index.md)
