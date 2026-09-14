# tiann/hapi

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit de6c9dee2032 @ 73f1d2d4ce7cd239

## Summary (orientation draft, not independently verified)

HAPI is a local-first remote-control platform for coding agents (Claude Code, Codex, etc.) with a CLI/hub architecture, native mobile and web clients, and an E2E-encrypted relay. Evidence covers product features and CLI usage plus contributor workflows; no evaluation or runtime permission evidence is present.

## Source coverage

Source coverage (partial): 3 of 29 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The repository includes SwiftUI/UIKit and Kotlin Compose native clients offering chat, approvals, session creation, files, dictation, and push notifications, with a documented client protocol contract. -- evidence: [README.md#L53-L53](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L53-L53)
  - [observation/documented] A workspace browser feature is opt-in via one or more `hapi runner start --workspace-root <path>` flags, allowing scoped file-tree browsing and session starts in allowed subdirectories. -- evidence: [README.md#L9-L16](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L9-L16)
- design-choices (2 claim(s)):
  - [observation/documented] HAPI positions itself as a local-first alternative to Happy, wrapping the user's existing AI agent rather than replacing it, keeping the same terminal experience. -- evidence: [README.md#L5-L5](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L5-L5), [README.md#L9-L16](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L9-L16)
  - [observation/documented] The relay uses WireGuard plus TLS for end-to-end encryption, with data encrypted from the user's device to their machine; self-hosted options like Cloudflare Tunnel and Tailscale are documented. -- evidence: [README.md#L37-L37](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L37-L37), [README.md#L39-L39](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L39-L39)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors use Bun workspaces (cli, shared, hub, web, website, docs, relay) with TypeScript strict typing, and root scripts `bun typecheck` and `bun run test` cover CLI/Web Vitest and Hub/Shared/Relay Bun tests. -- evidence: [AGENTS.md#L31-L34](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/AGENTS.md#L31-L34), [AGENTS.md#L53-L56](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/AGENTS.md#L53-L56), [CONTRIBUTING.md#L68-L71](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/CONTRIBUTING.md#L68-L71)
  - [observation/documented] Repository development practice: PRs must stay focused on a single concern, oversized 'mega PRs' are rejected, significant features require an issue discussion first, and AI-generated code must disclose the model used in the PR description. -- evidence: [CONTRIBUTING.md#L14-L14](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/CONTRIBUTING.md#L14-L14), [CONTRIBUTING.md#L30-L34](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/CONTRIBUTING.md#L30-L34), [CONTRIBUTING.md#L26-L26](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/CONTRIBUTING.md#L26-L26), [CONTRIBUTING.md#L20-L20](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/CONTRIBUTING.md#L20-L20)
- skills-patterns (1 claim(s)):
  - [observation/documented] Shared Codex sessions let users work with Codex from terminal and phone simultaneously, requiring Codex 0.154.0 or newer. -- evidence: [README.md#L9-L16](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L9-L16)
- interfaces (4 claim(s)):
  - [observation/documented] HAPI lets users run sessions of agents such as Claude Code, Codex, Cursor Agent, Grok Build, OpenCode, Kimi, Copilot, Antigravity, Pi, and DeepSeek Harness, controlled remotely via iOS/Android apps, Web/PWA, or a Telegram Mini App. -- evidence: [README.md#L3-L3](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L3-L3)
  - [observation/documented] The CLI supports starting an agent directly with `hapi <agent> [options]` (e.g. `hapi claude`), and scripts must specify the agent explicitly; `hapi --help` lists commands and supported agents. -- evidence: [README.md#L31-L33](https://github.com/tiann/hapi/blob/de6c9dee2032059b11fa3a4e23f5a805b28667b4/README.md#L31-L33)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](hapi.detail.md)

Metadata and full claim list: [full detail](hapi.detail.md)
Human notes ([notes](hapi.notes.md), never overwritten by build)

[Back to map index](../../index.md)
