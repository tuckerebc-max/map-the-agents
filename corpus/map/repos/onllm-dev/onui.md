# onllm-dev/onui

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d1a2d29677a4 @ 1686a01f7710bd7b

## Summary (orientation draft, not independently verified)

onUI is a browser extension (Chrome, Edge, Firefox) with a local MCP bridge for annotation-first UI feedback; evidence covers its capture modes, annotation schema, export levels, MCP tools, and local release/build workflows.

## Source coverage

Source coverage (partial): 6 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repository has three packages: core (shared annotation/report types and formatters), extension (background/content/popup runtime), and mcp-server (local MCP server plus native bridge setup/doctor tooling). -- evidence: [README.md#L242-L247](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L242-L247)
- design-choices (5 claim(s)):
  - [observation/documented] The extension offers two capture flows: Annotate mode for element-level targeting (with Shift multi-select) and Draw mode for rectangle/ellipse region annotations. -- evidence: [docs/mcp-setup.md#L16-L18](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/mcp-setup.md#L16-L18), [docs/release.md#L5-L10](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/release.md#L5-L10), [README.md#L28-L36](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L28-L36)
  - [observation/documented] Each annotation supports a comment, an intent (fix, change, question, approve), and a severity (blocking, important, suggestion). -- evidence: [docs/usage.md#L25-L28](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/usage.md#L25-L28)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors run pnpm install, pnpm check, and pnpm test:coverage; docs/development.md also documents pnpm test:all and loading unpacked builds from packages/extension/dist. -- evidence: [docs/development.md#L27-L29](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/development.md#L27-L29), [README.md#L234-L238](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L234-L238), [docs/development.md#L45-L49](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/development.md#L45-L49)
  - [observation/documented] Repository development practice: releases run locally via app.sh with no CI/CD dependency; --release gates on a clean tree, main branch, and gh auth, then bumps, tags, and publishes a GitHub release. -- evidence: [README.md#L219-L222](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L219-L222), [README.md#L224-L230](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L224-L230), [README.md#L215-L217](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L215-L217), [README.md#L188-L188](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L188-L188)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] onUI ships as a lightweight browser extension for Chrome, Edge, and Firefox plus a local MCP bridge for annotation-first UI pair programming. -- evidence: [README.md#L4-L4](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L4-L4)
  - [observation/documented] The local MCP server exposes eight tools: onui_list_pages, onui_get_annotations, onui_get_report, onui_search_annotations, onui_update_annotation_metadata, onui_bulk_update_annotation_metadata, onui_delete_annotation, and onui_clear_page_annotations. -- evidence: [docs/mcp-setup.md#L158-L166](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/mcp-setup.md#L158-L166)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Installer-based MCP setup uses a prebuilt release bundle and requires Node 20+; development prerequisites include Node.js 20+, pnpm 8+, and Chrome, Edge, or Firefox. -- evidence: [README.md#L123-L123](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L123-L123), [docs/development.md#L5-L7](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/development.md#L5-L7)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(4 additional claim(s) omitted for length; see [full detail](onui.detail.md) for every claim.)

Metadata and full claim list: [full detail](onui.detail.md)
Human notes ([notes](onui.notes.md), never overwritten by build)

[Back to map index](../../index.md)
