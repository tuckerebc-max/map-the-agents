# openbmb/pilotdeck

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 97633a08a73e @ 2d0f9ca69f85ae00

## Summary (orientation draft, not independently verified)

Selected evidence records: PilotDeck is an open-source agent operating system organized around a 'WorkSpace' concept, jointly developed by THUNLP, ModelBest, OpenBMB, and AI9Stars, targeting general-purpose multi-task scenarios. The WorkSpace is the fundamental isolation unit: each project gets its own file system, memory store, and skill set, so parallel work does not interfere and retrieval stays scoped.

## Source coverage

Source coverage (partial): 6 of 24 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] PilotDeck is an open-source agent operating system organized around a 'WorkSpace' concept, jointly developed by THUNLP, ModelBest, OpenBMB, and AI9Stars, targeting general-purpose multi-task scenarios. -- evidence: [README.md#L42-L42](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L42-L42)
- components (1 claim(s)):
  - [observation/documented] An open plugin architecture separates the open-source core from plugin customization, supporting MCP servers, custom tools and skills, lifecycle hooks such as PreToolUse and UserPromptSubmit, and pluggable memory store providers. -- evidence: [README.md#L479-L479](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L479-L479), [README.md#L481-L484](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L481-L484)
- design-choices (1 claim(s)):
  - [observation/documented] The WorkSpace is the fundamental isolation unit: each project gets its own file system, memory store, and skill set, so parallel work does not interfere and retrieval stays scoped. -- evidence: [README.md#L63-L63](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L63-L63), [README.md#L53-L53](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L53-L53)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributions follow a fork, feature branch, and pull-request workflow, and bugs or feature requests go through GitHub Issues. -- evidence: [README.md#L492-L492](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L492-L492), [README.md#L498-L499](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L498-L499)
  - [observation/documented] Repository development practice: source installs use corepack pnpm with a committed pnpm-lock.yaml and workspace filters, and Git LFS demo media is skipped by default for a lightweight clone. -- evidence: [README.md#L388-L388](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L388-L388), [README.md#L399-L399](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L399-L399), [README.md#L394-L397](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L394-L397)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The system natively supports the Model Context Protocol (MCP) and is described as behaving consistently across Web, CLI, and IM front-ends. -- evidence: [README.md#L53-L53](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L53-L53)
  - [observation/documented] PilotDeck ships a Web UI with WorkSpace management, white-box memory editing, and visualization of multi-agent collaboration; the 'pilotdeck' command starts the server at http://localhost:3001. -- evidence: [README.md#L221-L221](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L221-L221), [README.md#L315-L318](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L315-L318)
- memory-state (1 claim(s)):
  - [observation/documented] Memory is white-box and traceable: generation, extraction, storage, and retrieval are visible, entries can be edited or deleted, and a Dream Mode consolidates memory in idle windows with one-click rollback. -- evidence: [README.md#L180-L215](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L180-L215), [README.md#L74-L74](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L74-L74)
- orchestration (2 claim(s)):
  - [observation/documented] Smart Routing auto-detects task difficulty and sends complex calls to flagship models while simple tasks go to lighter sub-agent models, aiming to reduce token cost. -- evidence: [README.md#L87-L87](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L87-L87)
More evidence: [full detail](pilotdeck.detail.md)

Metadata and full claim list: [full detail](pilotdeck.detail.md)
Human notes ([notes](pilotdeck.notes.md), never overwritten by build)

[Back to map index](../../index.md)
