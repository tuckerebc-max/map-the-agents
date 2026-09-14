# limecloud/lime

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 580022b574cb @ abaebea4bce76cc8

## Summary (orientation draft, not independently verified)

Evidence describes Lime, an open-source GPLv3 Electron desktop AI agent with a Rust App Server (JSON-RPC), React/TypeScript frontend, Thread/Turn/Item task model, MCP/Skills, multi-agent orchestration, and user-granted permissions; macOS and Windows builds only. Claims are drawn from product READMEs and the FEATURE-MAP architecture/ownership documentation. Evidence coverage: 149 of 178 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 25 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Lime is described as an open-source full-stack desktop AI agent for coding, files, terminals, tools, research, content, multimodal work, and multi-agent workflows. -- evidence: [README.md#L9-L9](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L9-L9), [README.md#L11-L11](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L11-L11), [README.md#L49-L49](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L49-L49)
- components (2 claim(s)):
  - [observation/documented] The stack comprises an Electron desktop shell, a Rust App Server speaking JSON-RPC, a React/TypeScript/Vite frontend, and local capabilities including filesystem, processes, workspaces, artifacts, and persisted state. -- evidence: [README.md#L173-L178](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L173-L178), [README.en.md#L175-L180](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.en.md#L175-L180)
  - [observation/documented] FEATURE-MAP assigns ownership across crates: agent-runtime/agent for turn lifecycle and orchestration, model-provider for catalog/routing/retry, and tool-runtime for tool definitions, permissions, sandbox, dispatch, processes and MCP; the main-chain diagram lists thread-store/repository for persistence and projection. -- evidence: [FEATURE-MAP.md#L76-L84](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/FEATURE-MAP.md#L76-L84), [FEATURE-MAP.md#L24-L33](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/FEATURE-MAP.md#L24-L33)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: minimal documentation checks are `npm run docs:boundary`, relative-link validation, and `git diff --check`, with `npm run governance:legacy-report` added when governance categories change. -- evidence: [FEATURE-MAP.md#L101-L106](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/FEATURE-MAP.md#L101-L106)
  - [observation/documented] Repository development practice: FEATURE-MAP maintenance rules require updating code and the architecture doc first, then syncing the map after owner confirmation, and readiness is judged by code, protocol, and corresponding evidence levels rather than roadmap claims or single test results. -- evidence: [FEATURE-MAP.md#L101-L106](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/FEATURE-MAP.md#L101-L106), [FEATURE-MAP.md#L17-L20](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/FEATURE-MAP.md#L17-L20)
- skills-patterns (1 claim(s)):
  - [observation/documented] Recurring procedures can be encoded as Skills that the agent discovers and runs through MCP or controlled capabilities instead of repeating instructions in every prompt. -- evidence: [README.md#L95-L95](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L95-L95)
- interfaces (1 claim(s)):
  - [observation/documented] Desktop GUI business capabilities enter the Rust runtime only through App Server JSON-RPC; Electron IPC is limited to windows, file selection, system permissions, notifications, updates, native views, and sidecar lifecycle. -- evidence: [FEATURE-MAP.md#L46-L46](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/FEATURE-MAP.md#L46-L46)
- memory-state (1 claim(s)):
  - [observation/documented] Work is projected as Thread, Turn, Item, and reusable artifacts so tasks can be paused, reviewed, restored, and continued; project materials, conversation history, and configuration are kept locally by default. -- evidence: [README.md#L194-L194](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L194-L194), [README.md#L55-L58](https://github.com/limecloud/lime/blob/580022b574cb23acc3c44614566ed05ffb4f6180/README.md#L55-L58)
- orchestration (1 claim(s)):
More evidence: [full detail](lime.detail.md)

Metadata and full claim list: [full detail](lime.detail.md)
Human notes ([notes](lime.notes.md), never overwritten by build)

[Back to map index](../../index.md)
