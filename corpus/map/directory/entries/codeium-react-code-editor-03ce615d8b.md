# codeium-react-code-editor (`codeium-react-code-editor`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Exafunction
- License: MIT
- Language: TypeScript
- Interface: platforms=IDE; install=npm install @codeium/react-code-editor
- Model providers: Codeium
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: unknown (unknown)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [exafunction/codeium-react-code-editor](../../repos/exafunction/codeium-react-code-editor.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Free, open-source code editor React component wrapping Monaco editor with unlimited AI autocomplete powered by Codeium. No account required. Supports multi-document context for smarter autocompletion (up to 10 documents).

(captured site page body (agents/codeium-react-code-editor.md), not a verified repo-code finding)
This package exists for developers who need to embed a working code editor with AI completion into a web application without building the integration themselves. It wraps monaco-react — the React Monaco wrapper behind VS Code's editor — and adds Codeium's autocomplete service on top, requiring no user account and carrying no usage charge. Completions can reference up to ten additional documents through the otherDocuments prop, giving suggestions context beyond the visible file. The package exposes the underlying Monaco editor instance for direct API access and ships ESM and CommonJS builds, published as @codeium/react-code-editor on npm. It is a side utility from Exafunction, whose main product lines are the Windsurf plugin and editor, and its update cadence has been slow since 2024.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/codeium-react-code-editor.md)
