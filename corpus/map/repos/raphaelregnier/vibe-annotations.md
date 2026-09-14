# raphaelregnier/vibe-annotations

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 97c324e1f96b @ 8ecb8626410ca4a9

## Summary (orientation draft, not independently verified)

The product is a visual feedback tool for web development: users annotate page elements, make design tweaks, and share the results with AI coding agents or teammates. AI coding agents such as Claude Code, Cursor, Windsurf, Codex, and VS Code connect via Model Context Protocol (MCP) to read annotations and implement fixes; the MCP route is the recommended option, with clipboard copy as an alternative.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The product is a visual feedback tool for web development: users annotate page elements, make design tweaks, and share the results with AI coding agents or teammates. -- evidence: [README.md#L5-L5](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L5-L5)
  - [observation/documented] The README badge indicates the Chrome extension has 6K+ users on the Chrome Web Store, and the server is distributed as the npm package vibe-annotations-server. -- evidence: [README.md#L3-L3](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L3-L3)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (4 claim(s)):
  - [observation/documented] Getting started involves installing the Chrome extension, running 'npx vibe-annotations-server init' (an interactive command that installs the global server, starts it in the background, and configures the AI coding agent), then annotating a localhost page. -- evidence: [README.md#L17-L19](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L17-L19), [README.md#L21-L21](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L21-L21), [README.md#L13-L13](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L13-L13), [README.md#L23-L23](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L23-L23)
  - [observation/documented] Repository development practice: contributors work in a pnpm workspace with packages for extension, server, and website; the extension is built with WXT (pnpm dev gives live reload, load unpacked from .output/chrome-mv3), and the server runs via node lib/server.js or bin/cli.js start against 127.0.0.1:3846. -- evidence: [CLAUDE.md#L14-L14](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/CLAUDE.md#L14-L14), [CONTRIBUTING.md#L78-L80](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/CONTRIBUTING.md#L78-L80), [CONTRIBUTING.md#L67-L67](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/CONTRIBUTING.md#L67-L67), [CONTRIBUTING.md#L69-L74](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/CONTRIBUTING.md#L69-L74), [CONTRIBUTING.md#L54-L61](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/CONTRIBUTING.md#L54-L61)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] AI coding agents such as Claude Code, Cursor, Windsurf, Codex, and VS Code connect via Model Context Protocol (MCP) to read annotations and implement fixes; the MCP route is the recommended option, with clipboard copy as an alternative. -- evidence: [README.md#L27-L27](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L27-L27), [README.md#L25-L25](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L25-L25), [README.md#L21-L21](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/README.md#L21-L21), [CLAUDE.md#L28-L31](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/CLAUDE.md#L28-L31)
  - [observation/documented] The extension communicates only with a local server on port 3846, which the terms describe as the sole network endpoint for the product besides an optional NPM registry version check. -- evidence: [TERMS.md#L29-L31](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/TERMS.md#L29-L31)
- memory-state (1 claim(s)):
  - [observation/documented] Annotation data is stored locally on the user's machine under ~/.vibe-annotations/, with the Chrome extension using the Chrome Storage API for persistence; no data is sent to external servers. -- evidence: [TERMS.md#L24-L26](https://github.com/RaphaelRegnier/vibe-annotations/blob/97c324e1f96b7bd818106554041060f321a25025/TERMS.md#L24-L26)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
More evidence: [full detail](vibe-annotations.detail.md)

Metadata and full claim list: [full detail](vibe-annotations.detail.md)
Human notes ([notes](vibe-annotations.notes.md), never overwritten by build)

[Back to map index](../../index.md)
