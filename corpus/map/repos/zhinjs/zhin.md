# zhinjs/zhin

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 494dd81f1ac5 @ 5af28cbf7a2c96f7

## Summary (orientation draft, not independently verified)

Zhin.js is a TypeScript multi-platform chat-bot framework (pnpm monorepo) with an optional AI/agent layer, Remote Console, and a layered package architecture enforced in CI. Evidence is mostly README and architecture/adapter docs; no code inspection. Evidence coverage: 137 of 139 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 166 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repo is a pnpm workspace monorepo whose packages include @zhin.js/core (IM layer), @zhin.js/ai, @zhin.js/agent, @zhin.js/cli (composition root), and the zhin.js facade package. -- evidence: [docs/concepts/architecture.md#L3-L3](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/concepts/architecture.md#L3-L3), [docs/concepts/architecture.md#L62-L75](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/concepts/architecture.md#L62-L75), [README.md#L205-L211](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L205-L211)
- design-choices (2 claim(s)):
  - [observation/documented] Package dependency direction is unidirectional downward: upper layers may depend on lower ones, and lower layers never reference upper layers; @zhin.js/cli is the sole exception allowed to import across all layers. -- evidence: [docs/en/concepts/architecture.md#L3-L3](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/en/concepts/architecture.md#L3-L3), [docs/en/concepts/architecture.md#L76-L76](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/en/concepts/architecture.md#L76-L76), [docs/concepts/architecture.md#L79-L79](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/concepts/architecture.md#L79-L79), [docs/concepts/architecture.md#L3-L3](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/concepts/architecture.md#L3-L3)
  - [observation/documented] Plugin hot reload is described as a Generation transaction: the next plugin tree is prepared and validated off-path, then published atomically, so a failed candidate leaves the active Generation serving traffic. -- evidence: [README.md#L125-L129](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L125-L129)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: `pnpm check:architecture` runs in CI to block lower-layer packages importing upper-layer packages, and the layering rule is enforced by harness checks rather than convention. -- evidence: [docs/en/concepts/architecture.md#L3-L3](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/en/concepts/architecture.md#L3-L3), [docs/concepts/architecture.md#L3-L3](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/concepts/architecture.md#L3-L3)
  - [observation/documented] Repository development practice: adapter doc pages are auto-generated from in-package READMEs; contributors edit the package README and run `pnpm sync:adapter-docs`. -- evidence: [docs/adapters/sandbox.md#L7-L9](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/adapters/sandbox.md#L7-L9), [docs/en/adapters/sandbox.md#L7-L9](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/en/adapters/sandbox.md#L7-L9)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI exposes commands including `zhin runtime start`, `zhin setup`, `zhin doctor`, `zhin new my-plugin`, and `zhin search <kw>`. -- evidence: [README.md#L228-L234](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L228-L234), [README.md#L81-L81](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L81-L81), [docs/concepts/architecture.md#L81-L81](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/concepts/architecture.md#L81-L81)
  - [observation/documented] The Sandbox adapter is a WebSocket-based local testing adapter exposing a `/sandbox` WebSocket endpoint plus a browser chat UI, requiring no third-party platform account. -- evidence: [docs/en/adapters/sandbox.md#L15-L15](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/en/adapters/sandbox.md#L15-L15), [docs/en/adapters/sandbox.md#L19-L23](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/en/adapters/sandbox.md#L19-L23), [docs/adapters/sandbox.md#L19-L23](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/adapters/sandbox.md#L19-L23), [docs/adapters/sandbox.md#L15-L15](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/adapters/sandbox.md#L15-L15)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Agent execution security is configurable via zhin.config.yml, e.g. execSecurity: allowlist and execApprovalMode: ask; the stability table lists a baseline security tier with bash allowlist, file policy, and approval. -- evidence: [README.md#L173-L186](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L173-L186), [README.md#L134-L141](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L134-L141)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](zhin.detail.md)

Metadata and full claim list: [full detail](zhin.detail.md)
Human notes ([notes](zhin.notes.md), never overwritten by build)

[Back to map index](../../index.md)
