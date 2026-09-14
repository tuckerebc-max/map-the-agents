# aduermael/herm

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4bcb16ba05da @ de79735aea23feee

## Summary (orientation draft, not independently verified)

Herm is a model-agnostic, general-purpose AI agent CLI (Go) that runs by default inside Docker containers with self-building environments, plus native sandbox modes and an iOS/macOS app. Evidence is mostly README and architecture documentation; no source code slices are included. Evidence coverage: 167 of 385 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 13 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The CLI is a terminal TUI with an event loop selecting on stdin, agent events, and async results; agent events include Thinking, ToolCall, Approval, and Done, and sub-agent events continue to be drained after the main agent stops. -- evidence: [ARCHITECTURE.md#L381-L383](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/ARCHITECTURE.md#L381-L383), [ARCHITECTURE.md#L98-L124](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/ARCHITECTURE.md#L98-L124), [ARCHITECTURE.md#L276-L281](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/ARCHITECTURE.md#L276-L281)
  - [observation/documented] The repository also contains a SwiftUI iOS/macOS app that uses an in-process Unix-like sandbox and a Luau-scriptable runtime for on-device tasks; it is not usable as a coding agent in that context and is not yet on the App Store. -- evidence: [README.md#L55-L55](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L55-L55), [README.md#L53-L53](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L53-L53)
- design-choices (2 claim(s)):
  - [observation/documented] Herm is described as a model-agnostic, general-purpose AI agent built for safe, flexible execution, natively supporting multiple isolation methods including containers, in-process Unix-like sandboxes, and host sandboxes such as sandbox_exec on macOS or bubblewrap on Linux. -- evidence: [README.md#L7-L7](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L7-L7)
  - [observation/documented] Herm extends container environments by writing Dockerfiles dynamically, with environments scoped per project (the current working directory). -- evidence: [README.md#L21-L21](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L21-L21)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README points contributors to CONTRIBUTING.md for setup, tests, CI checks, coding standards, and pull request expectations, and CI badges cover test, prompt-length, and ci-checks GitHub Actions workflows. -- evidence: [README.md#L92-L92](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L92-L92), [README.md#L3-L5](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L3-L5)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI supports multiple providers (Anthropic, OpenAI, Gemini, Grok, OpenRouter, Ollama, Azure OpenAI, Vertex AI, Bedrock) and models can be mixed, e.g. a different model for the main agent, exploration, or vision. -- evidence: [README.md#L19-L19](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/README.md#L19-L19)
  - [observation/documented] Documented CLI flags include --version, --debug, --prompt for headless mode, --cpsl to run with a CPSL local sandbox library, and --naked to run without Docker or CPSL. -- evidence: [CLI_QUICK_START.md#L12-L14](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/CLI_QUICK_START.md#L12-L14), [CLI_QUICK_START.md#L45-L52](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/CLI_QUICK_START.md#L45-L52), [CLI_DOCS_INDEX.md#L382-L382](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/CLI_DOCS_INDEX.md#L382-L382), [CLI_DOCS_INDEX.md#L81-L98](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/CLI_DOCS_INDEX.md#L81-L98)
- memory-state (1 claim(s)):
  - [observation/documented] Configuration merges a global config (~/.herm/config.json, holding API keys, model, exploration, tool config, UI preferences) with a project-level .herm/config.json that can override model and tools. -- evidence: [ARCHITECTURE.md#L311-L314](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/ARCHITECTURE.md#L311-L314), [ARCHITECTURE.md#L229-L232](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/ARCHITECTURE.md#L229-L232), [ARCHITECTURE.md#L219-L225](https://github.com/aduermael/herm/blob/4bcb16ba05da6bdfc9b963c8c1fa14a51e743819/ARCHITECTURE.md#L219-L225)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](herm.detail.md)

Metadata and full claim list: [full detail](herm.detail.md)
Human notes ([notes](herm.notes.md), never overwritten by build)

[Back to map index](../../index.md)
