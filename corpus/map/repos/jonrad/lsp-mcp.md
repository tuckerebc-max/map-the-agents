# jonrad/lsp-mcp

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b48c04c52731 @ a955f65a50821306

## Summary (orientation draft, not independently verified)

Selected evidence records: The project is an MCP server that gives LLMs and AI agents access to language server protocol (LSP) capabilities, providing language-aware context from a codebase. The README states the project is in a POC (proof-of-concept) state.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project is an MCP server that gives LLMs and AI agents access to language server protocol (LSP) capabilities, providing language-aware context from a codebase. -- evidence: [README.md#L2-L2](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L2-L2)
- components (1 claim(s)):
  - [observation/documented] The features list says the server supports multiple LSPs (multiple programming languages) at the same time, referencing a sample config file. -- evidence: [README.md#L73-L74](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L73-L74)
- design-choices (2 claim(s)):
  - [observation/documented] Supported LSP methods are dynamically generated from an LSP JSON Schema stored at src/resources/generated.protocol.schema.json. -- evidence: [README.md#L73-L74](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L73-L74)
  - [observation/documented] Recorded design decisions include switching from Python to Node (vscode's LSP library over multilspy), using the low-level MCP SDK rather than FastMCP, and using zod for config validation. -- evidence: [README.md#L135-L142](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L135-L142)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: development commands include 'yarn', 'yarn mcp-cli' (an interactive MCP tool for development help), and 'yarn dev --help' for CLI help. -- evidence: [README.md#L128-L132](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L128-L132)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The server is configured as an MCP server via mcpServers JSON config using a command (docker or npx) plus an --lsp argument specifying the language server command to launch. -- evidence: [README.md#L98-L107](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L98-L107), [README.md#L109-L109](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L109-L109), [README.md#L81-L91](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L81-L91)
  - [observation/documented] The language server can be changed by switching the --lsp argument and then restarting the client (e.g. Claude Desktop). -- evidence: [README.md#L109-L109](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L109-L109)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The example npx setup launches typescript-language-server 4.3.3 with typescript 5.7.3 via npx, communicating over stdio. -- evidence: [README.md#L98-L107](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L98-L107)
  - [observation/documented] The project is MIT licensed, permitting use, copying, modification, and redistribution with the copyright notice retained, and is provided as-is without warranty. -- evidence: [LICENSE.txt#L1-L1](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/LICENSE.txt#L1-L1), [LICENSE.txt#L3-L6](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/LICENSE.txt#L3-L6), [LICENSE.txt#L10-L13](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/LICENSE.txt#L10-L13), [LICENSE.txt#L8-L8](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/LICENSE.txt#L8-L8)
- limitations (2 claim(s)):
  - [observation/documented] The README states the project is in a POC (proof-of-concept) state. -- evidence: [README.md#L70-L70](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L70-L70)
  - [observation/documented] The README notes that running multiple LSPs at the same time is not yet supported, in the section following the npx example. -- evidence: [README.md#L111-L111](https://github.com/jonrad/lsp-mcp/blob/b48c04c52731e3e499352fc644992dcce6202db2/README.md#L111-L111)
More evidence: [full detail](lsp-mcp.detail.md)

Metadata and full claim list: [full detail](lsp-mcp.detail.md)
Human notes ([notes](lsp-mcp.notes.md), never overwritten by build)

[Back to map index](../../index.md)
