# atmosphere/atmosphere

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 468f0ea79d57 @ 0d4003c8c705d782

## Summary (orientation draft, not independently verified)

The snapshot is README plus contributor docs for Atmosphere, a JVM real-time framework for AI agents with streaming transports, runtime adapters, governance, and durable sessions. Evidence supports product claims from the README and development-practice claims from AGENTS.md. Evidence coverage: 115 of 164 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 14 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The atmosphere-ai module ships an AgentRuntime SPI with a built-in OpenAI-compatible adapter; eleven more adapters live in separate modules, two of which (Anthropic, Cohere) are native HTTP+SSE clients. -- evidence: [README.md#L158-L158](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L158-L158)
  - [observation/documented] Governance controls include GovernancePolicy/PolicyRing with allow/deny lists and rate limits, @AgentScope purpose enforcement, tool approval policies, and a plan-and-verify verifier module. -- evidence: [README.md#L185-L197](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L185-L197)
- design-choices (1 claim(s)):
  - [observation/documented] Runtime adapter capabilities are pinned by AbstractAgentRuntimeContractTest.expectedCapabilities(), so a runtime cannot drift from its declared feature set without breaking tests. -- evidence: [README.md#L162-L162](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L162-L162)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: the project uses Maven with the wrapper; contributors run ./mvnw install/test, per-module builds, checkstyle and PMD checks, and must run a full compile with zero warnings before committing. -- evidence: [AGENTS.md#L6-L15](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/AGENTS.md#L6-L15), [AGENTS.md#L150-L155](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/AGENTS.md#L150-L155), [AGENTS.md#L3-L3](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/AGENTS.md#L3-L3)
  - [observation/documented] Repository development practice: git hooks must be enabled via core.hooksPath .githooks each session; they enforce copyright headers, no unused imports, commit format, and no AI-generated commit trailers, and --no-verify is forbidden. -- evidence: [AGENTS.md#L60-L65](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/AGENTS.md#L60-L65), [AGENTS.md#L33-L37](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/AGENTS.md#L33-L37), [AGENTS.md#L39-L44](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/AGENTS.md#L39-L44)
- skills-patterns (1 claim(s)):
  - [observation/documented] The CLI can import agent skill files, e.g. atmosphere import of an Anthropic SKILL.md URL, and a companion atmosphere-skills repository offers curated skill files. -- evidence: [README.md#L329-L332](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L329-L332), [README.md#L87-L91](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L87-L91)
- interfaces (3 claim(s)):
  - [observation/documented] A single @Agent annotation declares an agent, with @Prompt for streaming messages, @Command for slash commands (including confirmation prompts), and @AiTool for tool methods. -- evidence: [README.md#L111-L115](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L111-L115), [README.md#L101-L104](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L101-L104), [README.md#L95-L95](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L95-L95), [README.md#L117-L122](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L117-L122), [README.md#L106-L109](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L106-L109), [README.md#L97-L99](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L97-L99)
  - [observation/documented] Classpath modules register endpoints: browser endpoint at /atmosphere/agent/my-agent, MCP at .../mcp, A2A at .../a2a, AG-UI at .../agui, plus an admin dashboard and console UI. -- evidence: [README.md#L124-L132](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L124-L132)
- memory-state (1 claim(s)):
  - [observation/documented] Memory is provided as AiConversationMemory per-conversation history and LongTermMemory per-user facts, in-memory or durable via SQLite/Redis modules, with a SemanticRecallInterceptor for vector recall. -- evidence: [README.md#L40-L49](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L40-L49)
- orchestration (1 claim(s)):
  - [observation/documented] Multi-agent orchestration uses @Coordinator and AgentFleet with handoffs, conditional routing, an event-sourced coordination journal, and durable hibernating Workflow<S> over a CheckpointStore (optionally Temporal-backed). -- evidence: [README.md#L40-L49](https://github.com/Atmosphere/atmosphere/blob/468f0ea79d57a4fafbef1bddc09ba03d0eb65096/README.md#L40-L49)
More evidence: [full detail](atmosphere.detail.md)

Metadata and full claim list: [full detail](atmosphere.detail.md)
Human notes ([notes](atmosphere.notes.md), never overwritten by build)

[Back to map index](../../index.md)
