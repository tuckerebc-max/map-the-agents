# entropy-research/devon

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8f68f1d74671 @ 48b598ca7c27ac23

## Summary (orientation draft, not independently verified)

Devon is an open-source AI pair programmer distributed as a pipx backend (devon_agent) plus npm UIs (devon-ui, devon-tui), supporting multiple model providers including local Ollama. Evidence is mostly README documentation plus contributor docs describing the agent's component architecture.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Architecture comprises Environments (LocalShell, User), Tools, Agents (TaskAgent, ConversationalAgent), a Session orchestrator, and a config object, each with base classes in devon_agent modules. -- evidence: [contributor.md#L5-L10](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/contributor.md#L5-L10)
- design-choices (1 claim(s)):
  - [observation/documented] The agent is documented to only access files and folders in the directory it was started from, and users can correct it mid-action. -- evidence: [README.md#L111-L112](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L111-L112)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors fork, branch, commit descriptively, and open pull requests; PRs should include a descriptive title, rationale, test steps, and screenshots, and a maintainer reviews before merging. -- evidence: [CONTRIBUTING.md#L63-L66](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/CONTRIBUTING.md#L63-L66), [CONTRIBUTING.md#L68-L68](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/CONTRIBUTING.md#L68-L68), [CONTRIBUTING.md#L15-L20](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/CONTRIBUTING.md#L15-L20)
  - [observation/documented] Repository development practice: coding conventions require 4-space indentation, PEP 8 style, docstrings for public code, and descriptive names; local setup runs build.sh with DEVON_TELEMETRY_DISABLED=true. -- evidence: [CONTRIBUTING.md#L32-L33](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/CONTRIBUTING.md#L32-L33), [CONTRIBUTING.md#L28-L30](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/CONTRIBUTING.md#L28-L30), [CONTRIBUTING.md#L54-L57](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/CONTRIBUTING.md#L54-L57)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product ships as a backend installed via pipx (devon_agent) with a main UI run through npx devon-ui. -- evidence: [README.md#L45-L45](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L45-L45), [README.md#L60-L63](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L60-L63), [README.md#L48-L49](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L48-L49)
  - [observation/documented] A terminal interface exists, installed globally via npm as devon-tui and launched with the devon-tui command. -- evidence: [README.md#L73-L76](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L73-L76), [README.md#L78-L85](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L78-L85), [README.md#L104-L107](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L104-L107)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Communication between agents, tools, and environments happens via an event handler/emitter system whose handlers are declared in the Session; registering tools and environments requires no handler changes. -- evidence: [contributor.md#L13-L15](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/contributor.md#L13-L15)
- tools-permissions (1 claim(s)):
  - [observation/documented] The product collects basic event-type and failure telemetry, which users can disable by setting DEVON_TELEMETRY_DISABLED=true. -- evidence: [README.md#L249-L249](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L249-L249), [README.md#L251-L254](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L251-L254)
- evaluation (1 claim(s)):
  - [inference/documented] The project appears to track agent performance via SWE-bench Lite, citing a past milestone of beating AutoCodeRover and a goal to set SOTA there. -- evidence: [README.md#L177-L185](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L177-L185), [README.md#L198-L207](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L198-L207)
- dependencies (2 claim(s)):
  - [observation/documented] Running Devon requires node.js/npm, pipx, and at least one API key from Anthropic or OpenAI. -- evidence: [README.md#L28-L32](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L28-L32)
  - [observation/documented] Supported models include Claude 3.5 Sonnet, GPT4-o, Groq llama3-70b, and Ollama deepseek-coder:6.7b, with Gemini 1.5 Pro planned but unchecked. -- evidence: [README.md#L177-L185](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L177-L185), [README.md#L138-L144](https://github.com/entropy-research/Devon/blob/8f68f1d7467161562d64138aefee7d26c7e68130/README.md#L138-L144)
- limitations (2 claim(s)):
More evidence: [full detail](devon.detail.md)

Metadata and full claim list: [full detail](devon.detail.md)
Human notes ([notes](devon.notes.md), never overwritten by build)

[Back to map index](../../index.md)
