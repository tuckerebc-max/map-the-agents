# mastra-ai/mastra

Status: distilled - Freshness: current
Catalog classes: agent-sdk
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f04f724c6c58 @ 4a191eb4e779b79d

## Summary (orientation draft, not independently verified)

Evidence covers the Mastra README (product description, features, licensing, security contact), a code of conduct, and contributor-facing guides (DEVELOPMENT.md, CONTRIBUTING.md, AGENTS.md). No runtime source code is included in the snapshot, so product claims rest on documentation only.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree truncated (partial listing). Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Mastra is documented as a TypeScript framework for building AI-powered applications and agents, integrating with React, Next.js, and Node or deployable as a standalone server. -- evidence: [README.md#L11-L11](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L11-L11), [README.md#L13-L13](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L13-L13)
- components (1 claim(s)):
  - [observation/documented] Documented capabilities include model routing to 40+ providers, autonomous agents, a graph-based workflow engine, human-in-the-loop suspend/resume, memory and RAG context management, MCP server authoring, and built-in evals and observability. -- evidence: [README.md#L23-L23](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L23-L23), [README.md#L21-L21](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L21-L21), [README.md#L35-L35](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L35-L35), [README.md#L33-L33](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L33-L33), [README.md#L27-L27](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L27-L27), [README.md#L29-L29](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L29-L29), [README.md#L25-L25](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L25-L25)
- design-choices (1 claim(s)):
  - [observation/documented] The repository uses dual licensing: Apache-2.0 for most code, while any directory named ee/ (e.g., packages/core/src/auth/ee/) falls under the Mastra Enterprise License, free for development/testing but requiring a license for production use. -- evidence: [README.md#L100-L101](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L100-L101), [README.md#L98-L98](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L98-L98)
- workflows (6 claim(s)):
  - [observation/documented] Repository development practice: contributors need Node.js v22.13.0+, pnpm v10.18.0+ (enabled via corepack), and optionally Docker for a subset of tests; setup uses pnpm run setup to install dependencies and build the CLI package. -- evidence: [DEVELOPMENT.md#L7-L9](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L7-L9), [DEVELOPMENT.md#L22-L22](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L22-L22), [DEVELOPMENT.md#L30-L32](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L30-L32), [DEVELOPMENT.md#L34-L34](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L34-L34)
  - [observation/documented] Repository development practice: testing uses Vitest with pnpm test and per-package scripts; some tests require environment variables such as OPENAI_API_KEY and a local PostgreSQL DB_URL, with services started via pnpm run dev:services:up. -- evidence: [DEVELOPMENT.md#L130-L130](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L130-L130), [DEVELOPMENT.md#L132-L149](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L132-L149), [DEVELOPMENT.md#L155-L162](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L155-L162), [DEVELOPMENT.md#L151-L151](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L151-L151), [DEVELOPMENT.md#L166-L168](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/DEVELOPMENT.md#L166-L168)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The workflow engine's documented control-flow syntax includes methods such as .then(), .branch(), and .parallel() for orchestrating multi-step processes. -- evidence: [README.md#L25-L25](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L25-L25)
  - [observation/documented] Mastra Studio is presented as a web interface at http://localhost:4111 for building, testing, and managing agents, workflows, and tools after starting the dev server. -- evidence: [README.md#L65-L65](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L65-L65), [README.md#L67-L67](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L67-L67)
- memory-state (1 claim(s)):
  - [observation/documented] Suspended agents or workflows use storage to remember execution state, allowing indefinite pausing and later resumption where execution left off. -- evidence: [README.md#L27-L27](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L27-L27)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The model router is documented to connect to 40+ providers through one standard interface, naming OpenAI, Anthropic, and Gemini among supported model sources. -- evidence: [README.md#L21-L21](https://github.com/mastra-ai/mastra/blob/f04f724c6c587463424232e777266fdcc316f3f6/README.md#L21-L21)
More evidence: [full detail](mastra.detail.md)

Metadata and full claim list: [full detail](mastra.detail.md)
Human notes ([notes](mastra.notes.md), never overwritten by build)

[Back to map index](../../index.md)
