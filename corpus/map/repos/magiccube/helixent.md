# magiccube/helixent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5cc1fb3faf29 @ 1f960ac622028c5c

## Summary (orientation draft, not independently verified)

Helixent is a TypeScript/Bun coding-agent product comprising a ReAct-style agent loop with middleware, a coding agent layer with developer tools and skills, and a TUI CLI, published as the npm package 'helixent'. Evidence is documentation-based (README and docs/), with no code-inspected slices supplied. Evidence coverage: 160 of 217 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Helixent is described as a coding agent comprising an agent loop, a coding-focused agent layer, and a CLI, distributed as the npm package 'helixent'. -- evidence: [README.md#L79-L79](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L79-L79), [README.md#L14-L14](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L14-L14)
- components (3 claim(s)):
  - [observation/documented] The codebase is organized into three layers plus a community area: src/foundation (core primitives), src/agent (agent loop), src/coding (coding agent), and src/community (third-party integrations such as OpenAI). -- evidence: [README.md#L193-L193](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L193-L193), [README.md#L195-L201](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L195-L201)
  - [observation/documented] The foundation layer provides three core primitives: a Model abstraction over LLM providers, a single Message transcript type, and Tool definitions with execution plumbing. -- evidence: [README.md#L207-L209](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L207-L209), [docs/foundation.md#L3-L3](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/foundation.md#L3-L3)
- design-choices (2 claim(s)):
  - [observation/documented] Bun was chosen over Node for its native async/await concurrency, faster HTTP/filesystem/cold-start performance, single-file compiled executables via 'bun build --compile', and bundled test runner, bundler, and TypeScript support. -- evidence: [README.md#L296-L296](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L296-L296), [README.md#L300-L303](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L300-L303)
  - [observation/documented] The OpenAI provider defaults to temperature 0 and top_p 0, merges caller options last, and works with any OpenAI-compatible endpoint; thinking content is dropped when converting messages to OpenAI wire format. -- evidence: [README.md#L230-L230](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L230-L230), [docs/foundation.md#L81-L84](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/foundation.md#L81-L84), [docs/foundation.md#L77-L77](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/foundation.md#L77-L77), [docs/code-convention.md#L69-L70](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/code-convention.md#L69-L70)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: all pushes and pull requests run 'bun run check' in GitHub Actions, local commits are gated by a pre-commit hook running the same check, and contributors build with bun install / bun run dev / bun run build:bin producing dist/bin/helixent. -- evidence: [README.md#L152-L154](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L152-L154), [README.md#L172-L172](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L172-L172), [README.md#L178-L180](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L178-L180), [README.md#L156-L156](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L156-L156), [README.md#L160-L162](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L160-L162), [README.md#L166-L168](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L166-L168)
  - [observation/documented] Repository development practice: docs/bun.md instructs contributors to default to Bun (bun test, bun install, Bun.file, Bun.serve) and avoid Node/dotenv/express equivalents; docs/code-convention.md mandates kebab-case files, named exports only, _-prefixed private members, and layered dependency direction (agent stays generic; adapters live in community/). -- evidence: [docs/code-convention.md#L10-L11](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/code-convention.md#L10-L11), [docs/code-convention.md#L14-L18](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/code-convention.md#L14-L18), [docs/code-convention.md#L40-L44](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/code-convention.md#L40-L44), [docs/bun.md#L9-L15](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/bun.md#L9-L15), [docs/bun.md#L7-L7](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/docs/bun.md#L7-L7)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills in the standard agentskills.io format are discovered from ~/.agents/skills, ~/.helixent/skills, and the project's .agents/skills and .helixent/skills directories; duplicate skill names across folders are allowed. -- evidence: [README.md#L54-L69](https://github.com/MagicCube/helixent/blob/5cc1fb3faf29b8db8dce614e925c89030ae2558b/README.md#L54-L69)
- interfaces (3 claim(s)):
More evidence: [full detail](helixent.detail.md)

Metadata and full claim list: [full detail](helixent.detail.md)
Human notes ([notes](helixent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
