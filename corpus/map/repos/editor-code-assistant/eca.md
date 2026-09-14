# editor-code-assistant/eca

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e30026331ad6 @ 6543b15215023cac

## Summary (orientation draft, not independently verified)

ECA is a Clojure, editor-agnostic AI coding-assistant server speaking JSON-RPC over stdin/stdout, with configurable tools, MCP servers, skills, and agents, storing data locally per its privacy doc. Development docs describe Babashka-based build/test workflows for contributors. Evidence coverage: 148 of 239 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 33 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 22 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

22 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The server is written in Clojure with a layered layout: handlers.clj receives all JSON-RPC requests, db.clj holds in-memory state, llm_api.clj is the LLM facade, and llm_providers/ holds vendor adapters. -- evidence: [README.md#L43-L43](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/README.md#L43-L43), [docs/development.md#L18-L56](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L18-L56)
  - [observation/documented] The documented request flow is: client/editor → stdin JSON-RPC → handlers → features → llm_api → llm_provider, with results streamed back via messenger. -- evidence: [docs/development.md#L60-L60](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L60-L60)
- design-choices (2 claim(s)):
  - [observation/documented] ECA places a server between editors and LLMs to centralize tool-call management, multi-LLM interaction, telemetry, and a single configuration shared across editors. -- evidence: [README.md#L45-L50](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/README.md#L45-L50)
  - [observation/documented] Configuration is centralized and resolved from multiple sources: global config, local config, environment variables, and initializationOptions. -- evidence: [docs/development.md#L18-L56](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L18-L56)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors run unit tests with `bb test` (CI runs the same task), single namespaces via kaocha focus, and integration tests with `bb integration-test`, which spawns the server over JSON-RPC with mocked LLM and MCP servers. -- evidence: [docs/development.md#L74-L76](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L74-L76), [docs/development.md#L70-L70](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L70-L70), [docs/development.md#L80-L80](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L80-L80), [docs/development.md#L72-L72](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L72-L72)
  - [observation/documented] Repository development practice: a local debug binary is built with `bb debug-cli` (requires babashka), and contributors can attach to the nREPL port printed on stderr to modify the running ECA process. -- evidence: [docs/development.md#L92-L95](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L92-L95), [docs/development.md#L9-L10](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/development.md#L9-L10)
- skills-patterns (2 claim(s)):
  - [observation/documented] Skills are SKILL.md folders following the agentskills standard, searched in ~/.config/eca/skills, .eca/skills, and .agents/skills; only name and description are sent to the LLM, which loads a skill via the `eca__skill` tool. -- evidence: [docs/config/skills.md#L9-L10](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/skills.md#L9-L10), [docs/config/skills.md#L12-L12](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/skills.md#L12-L12)
  - [observation/documented] Skills can be parameterized as slash commands using $ARGS, $ARGUMENTS, and positional variables; when arguments are given, ECA substitutes them into the skill body instead of using the eca__skill tool. -- evidence: [docs/config/skills.md#L110-L110](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/skills.md#L110-L110), [docs/config/skills.md#L92-L92](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/skills.md#L92-L92), [docs/config/skills.md#L90-L90](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/docs/config/skills.md#L90-L90)
- interfaces (3 claim(s)):
  - [observation/documented] Editors spawn the server via `eca server` and communicate over stdin/stdout using a JSON-RPC protocol inspired by LSP, so any editor can integrate. -- evidence: [README.md#L43-L43](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/README.md#L43-L43), [README.md#L54-L54](https://github.com/editor-code-assistant/eca/blob/e30026331ad698d0748d52dc403e4a7d481d241e/README.md#L54-L54)
More evidence: [full detail](eca.detail.md)

Metadata and full claim list: [full detail](eca.detail.md)
Human notes ([notes](eca.notes.md), never overwritten by build)

[Back to map index](../../index.md)
