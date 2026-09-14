# onllm-dev/onui -- full detail

[Back to orientation](onui.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/onllm-dev/onui/d1a2d29677a412353e64b15a14300dc13b84dc3c/1686a01f7710bd7b.json](../../../wiki/dossiers/onllm-dev/onui/d1a2d29677a412353e64b15a14300dc13b84dc3c/1686a01f7710bd7b.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repository has three packages: core (shared annotation/report types and formatters), extension (background/content/popup runtime), and mcp-server (local MCP server plus native bridge setup/doctor tooling). -- evidence: [README.md#L242-L247](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L242-L247) (`clm_d73add54cd0a6bd30cc47dd6a09c250cbc0a73ecfd8719c5027999e90e5cb955`)

## design-choices (5 claim(s))

- [observation/documented] The extension offers two capture flows: Annotate mode for element-level targeting (with Shift multi-select) and Draw mode for rectangle/ellipse region annotations. -- evidence: [docs/mcp-setup.md#L16-L18](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/mcp-setup.md#L16-L18), [docs/release.md#L5-L10](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/release.md#L5-L10), [README.md#L28-L36](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L28-L36) (`clm_0a6cdbcd4247e87899182199c11af1f69428675c9f61a12bcd6317259577f95a`)
- [observation/documented] Each annotation supports a comment, an intent (fix, change, question, approve), and a severity (blocking, important, suggestion). -- evidence: [docs/usage.md#L25-L28](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/usage.md#L25-L28) (`clm_41d153f34f7591ceaf331e220166e1da97b0bb3885eeb85f391f160e6373031c`)
- [observation/documented] Exports come in four output levels (compact, standard, detailed, forensic); region annotations include shape and geometry fields in report output at detailed and forensic levels. -- evidence: [docs/mcp-setup.md#L217-L217](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/mcp-setup.md#L217-L217), [docs/usage.md#L85-L93](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/usage.md#L85-L93), [README.md#L28-L36](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L28-L36) (`clm_7417f873c6180d1cb2ed9b5b5e9a0c9146fb0d0338b442f30a70cef61ab41dd6`)
- [observation/documented] The extension uses Shadow DOM isolation for stable styling and per-tab ON/OFF control that is off by default; new tabs start with onUI off. -- evidence: [docs/usage.md#L113-L115](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/usage.md#L113-L115), [README.md#L28-L36](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L28-L36) (`clm_ddb7a23072693e7461594b65c4ba343c9e070098f80ed9b0cb8e1e3c51eb9b32`)
- [observation/documented] In annotate mode the page freezes: scrolling is disabled and page interactions are blocked so element positions stay stable; draw mode does not freeze the page. -- evidence: [docs/usage.md#L97-L97](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/usage.md#L97-L97), [docs/usage.md#L109-L109](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/usage.md#L109-L109), [docs/usage.md#L99-L101](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/usage.md#L99-L101) (`clm_edd5867200ff4a0a80e1b74c866f7fe819ca3ba95fdd7a25cc7b8fbfa9253eab`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors run pnpm install, pnpm check, and pnpm test:coverage; docs/development.md also documents pnpm test:all and loading unpacked builds from packages/extension/dist. -- evidence: [docs/development.md#L27-L29](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/development.md#L27-L29), [README.md#L234-L238](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L234-L238), [docs/development.md#L45-L49](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/development.md#L45-L49) (`clm_815c1dc9ce9d65ec20562d19fa0acd65d53716dd8e58d41595efe81cf6f97c2c`)
- [observation/documented] Repository development practice: releases run locally via app.sh with no CI/CD dependency; --release gates on a clean tree, main branch, and gh auth, then bumps, tags, and publishes a GitHub release. -- evidence: [README.md#L219-L222](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L219-L222), [README.md#L224-L230](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L224-L230), [README.md#L215-L217](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L215-L217), [README.md#L188-L188](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L188-L188) (`clm_f7663ba5f01ce5b5896cdbd11c320dbee34d4dfc5d4db951277488eefbede05a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] onUI ships as a lightweight browser extension for Chrome, Edge, and Firefox plus a local MCP bridge for annotation-first UI pair programming. -- evidence: [README.md#L4-L4](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L4-L4) (`clm_59e67ac1078bfe3977e33549522ae908ba9cc9f48ac24f4303a6ad9ea8dbe296`)
- [observation/documented] The local MCP server exposes eight tools: onui_list_pages, onui_get_annotations, onui_get_report, onui_search_annotations, onui_update_annotation_metadata, onui_bulk_update_annotation_metadata, onui_delete_annotation, and onui_clear_page_annotations. -- evidence: [docs/mcp-setup.md#L158-L166](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/mcp-setup.md#L158-L166) (`clm_225e4bbd78c8649ca64eed9b8a3d919b76d49cd7fc23ad50541212e38c6c4baf`)
- [observation/documented] The MCP server is registered as 'onui-local' and runs via node on the onui-cli.js entrypoint; setup auto-registers it for Claude Code and Codex when those CLIs are installed. -- evidence: [README.md#L137-L149](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L137-L149), [README.md#L177-L179](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L177-L179), [docs/mcp-setup.md#L43-L48](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/mcp-setup.md#L43-L48) (`clm_b078dcab1d17214f58df8e8bf2fd5b882b441175fa19dabb4f67a830194f54a2`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Installer-based MCP setup uses a prebuilt release bundle and requires Node 20+; development prerequisites include Node.js 20+, pnpm 8+, and Chrome, Edge, or Firefox. -- evidence: [README.md#L123-L123](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/README.md#L123-L123), [docs/development.md#L5-L7](https://github.com/onllm-dev/onUI/blob/d1a2d29677a412353e64b15a14300dc13b84dc3c/docs/development.md#L5-L7) (`clm_3a547781567d5e5f8d33025c008f8a3f69e59de5abae6b6398fc7c1c9d93d0f6`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

