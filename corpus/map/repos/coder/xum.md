# coder/xum

Status: distilled - Freshness: current
Catalog classes: agent
Origins: github-rename-resolution, alltheagents.org-backing, github-verified-rename - Projects: navy-yard, Observatory
Formerly: coder/mux (github id 1058825816).
Latest snapshot: commit fbbea2b16403 @ 519b231f1435b189

## Summary (orientation draft, not independently verified)

Evidence covers Xum (formerly Mux), an open-source AGPL-3.0 coding-agent multiplexer with isolated workspaces, multi-model support, tool hooks, and CLI/desktop distribution, plus documentation-development guidance. Most claims are documentation-based; no source code is included in the slices. Evidence coverage: 174 of 333 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 59 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] Xum is a coding-agent multiplexer that runs parallel agents, each in its own isolated workspace, with a central view of git divergence; runtimes include local directories, git worktrees, and SSH remote execution. -- evidence: [docs/index.mdx#L31-L31](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/index.mdx#L31-L31), [docs/index.mdx#L5-L5](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/index.mdx#L5-L5), [README.md#L25-L34](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/README.md#L25-L34), [docs/index.mdx#L33-L36](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/index.mdx#L33-L36)
  - [observation/documented] The product supports multiple model families (sonnet-4-*, grok-*, gpt-5-*, opus-4-*), with Ollama for local LLMs and OpenRouter for a long tail of providers. -- evidence: [README.md#L25-L34](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/README.md#L25-L34), [docs/index.mdx#L33-L36](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/index.mdx#L33-L36)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: docs are built with Mintlify, served locally via `make docs-server`, auto-deployed on push to main, and CI runs `mintlify broken-links` on every PR to validate internal links. -- evidence: [docs/README.md#L16-L18](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/README.md#L16-L18), [docs/README.md#L11-L12](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/README.md#L11-L12), [docs/README.md#L52-L53](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/README.md#L52-L53)
  - [observation/documented] Repository development practice: a documentation style guide (STYLE.md) instructs writers to skip obvious or expected behavior, document deviations and complex workflows, and follow conventions for mermaid diagrams; new pages need frontmatter and docs.json navigation entries. -- evidence: [docs/README.md#L48-L48](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/README.md#L48-L48), [docs/STYLE.md#L7-L11](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/STYLE.md#L7-L11), [docs/STYLE.md#L3-L3](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/STYLE.md#L3-L3), [docs/README.md#L32-L35](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/README.md#L32-L35), [docs/STYLE.md#L42-L45](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/STYLE.md#L42-L45)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] A CLI is available via npm: `npx @coder/xum run "..."` runs agent tasks and `npx @coder/xum server --port 3000` starts a server for remote/mobile access; the legacy `mux` package forwards to Xum during the rename transition. -- evidence: [docs/install.mdx#L103-L103](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/install.mdx#L103-L103), [docs/install.mdx#L87-L87](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/install.mdx#L87-L87), [docs/install.mdx#L94-L95](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/install.mdx#L94-L95), [docs/install.mdx#L91-L91](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/install.mdx#L91-L91)
  - [observation/documented] Release distribution includes signed/notarized macOS DMGs (separate Intel and Apple Silicon builds), a Linux AppImage, and a Windows installer exe; only main-branch builds are signed, so PR builds need Gatekeeper bypass on macOS. -- evidence: [docs/install.mdx#L75-L78](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/install.mdx#L75-L78), [docs/install.mdx#L22-L26](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/install.mdx#L22-L26), [docs/install.mdx#L14-L16](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/install.mdx#L14-L16)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (3 claim(s)):
More evidence: [full detail](xum.detail.md)

Metadata and full claim list: [full detail](xum.detail.md)
Human notes ([notes](xum.notes.md), never overwritten by build)

[Back to map index](../../index.md)
