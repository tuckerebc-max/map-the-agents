# sumitsingh4411/repo-agent -- full detail

[Back to orientation](repo-agent.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sumitsingh4411/repo-agent/703c1afdf6f3f6d291e828852af9db361bcb3cc9/ff5baa40eebdbcd5.json](../../../wiki/dossiers/sumitsingh4411/repo-agent/703c1afdf6f3f6d291e828852af9db361bcb3cc9/ff5baa40eebdbcd5.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (4 claim(s))

- [observation/documented] An autonomous agent mode reads files, edits across many files with inline Keep/Undo review, and runs terminal commands with user approval, tracked by a live checklist that can be stopped. -- evidence: [README.md#L190-L194](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L190-L194), [README.md#L98-L98](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L98-L98) (`clm_dfbd746dd540f31f691fad9599af24ef14c939ce8c98f83fc97835c678e84005`)
- [observation/documented] After editing, the agent reportedly runs the project's typecheck/build, reads errors, and fixes them before declaring a task done (self-verification). -- evidence: [README.md#L190-L194](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L190-L194), [README.md#L106-L106](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L106-L106), [README.md#L404-L408](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L404-L408) (`clm_5f9ce1327f24b7f9591307ecbe9bc2c11354400c959f36a98a49c74e1db70cfe`)
- [observation/documented] Plugins are MCP servers addable from a built-in catalog of ~20 servers, from npm/GitHub packages (run via npx), custom stdio commands, or remote URLs over Streamable HTTP with optional bearer tokens. -- evidence: [docs/PLUGINS.md#L28-L28](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/docs/PLUGINS.md#L28-L28), [README.md#L293-L293](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L293-L293), [docs/PLUGINS.md#L54-L58](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/docs/PLUGINS.md#L54-L58), [docs/PLUGINS.md#L37-L40](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/docs/PLUGINS.md#L37-L40), [docs/PLUGINS.md#L11-L12](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/docs/PLUGINS.md#L11-L12), [docs/PLUGINS.md#L45-L49](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/docs/PLUGINS.md#L45-L49) (`clm_8a920caed05636898c6195b2cd4c34d6a221c07314b7da9740885be904f8350c`)
- [observation/documented] A code-review feature reviews staged changes, files, or branches, runs a second audit pass (review.deepAudit default true), reports Critical/Quality/Architecture/Testing findings, and can enforce user rules from a system-design.md guidelines file. -- evidence: [README.md#L317-L317](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L317-L317), [README.md#L126-L126](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L126-L126), [README.md#L357-L370](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L357-L370) (`clm_32903c6fdc7fb3cb06e556856eb61b0ac824ee7b287516b6f0b139169959f8a0`)

## design-choices (1 claim(s))

- [observation/documented] API keys and plugin tokens are stored in VS Code SecretStorage rather than settings or repo files; the CLI keeps its own key store (~/.repo-agent.json, chmod 600, opt-in) since it cannot read VS Code SecretStorage. -- evidence: [docs/PLUGINS.md#L89-L90](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/docs/PLUGINS.md#L89-L90), [README.md#L376-L385](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L376-L385), [README.md#L235-L237](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L235-L237) (`clm_f2c947a9f19b1d784c2b0d0e6cd2b452be5122ca16e1475def0aba4e9f4ff19c`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product ships as a VS Code extension ('free-repo-agent' on the Marketplace) with a chat panel opened via Cmd/Ctrl+Shift+A or a docked icon, plus 'Agent:' commands in the command palette. -- evidence: [README.md#L339-L350](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L339-L350), [README.md#L180-L180](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L180-L180), [README.md#L22-L26](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L22-L26), [README.md#L337-L337](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L337-L337), [README.md#L9-L9](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L9-L9) (`clm_794d79b4b52db184fa61c88bf9d639501fb4218950c3db78e5682a94f78c1926`)
- [observation/documented] A terminal CLI ships inside the extension (v0.10.0+), runnable via an alias to dist/cli.js, with flags like --model, --effort, --cwd, --base-url, --yes, and in-session commands such as /model, /effort, /login. -- evidence: [README.md#L229-L233](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L229-L233), [README.md#L215-L215](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L215-L215), [README.md#L219-L220](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L219-L220) (`clm_9997d548a71a51c0ccdd288b03cb4867702b5325eb0de48effdc3d16b335b35a`)

## memory-state (2 claim(s))

- [observation/documented] The agent indexes the repository (symbols, structure, optional AI per-file summaries) into a local .agent-cache/ cache and injects the most relevant files (default 8 via repoAgent.retrieval.maxFiles) into each prompt. -- evidence: [README.md#L333-L333](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L333-L333), [README.md#L357-L370](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L357-L370) (`clm_b5fad5ae2600cade3b829bb71365a8d5530839beeb2315d312647ed8c9baf659`)
- [observation/documented] A 'Learn this codebase' command writes a knowledge brief to .repo-agent/knowledge.md injected into every prompt, and a memory.md (or .agent.md/.claude.md) at the repo root supplies always-on user rules. -- evidence: [README.md#L254-L254](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L254-L254), [README.md#L311-L311](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L311-L311), [README.md#L297-L297](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L297-L297) (`clm_1c7a412d04c6cdc6984942f9a3252677087daf41a45c099cdb49b295a9337fd8`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Plugin tools run without a confirmation prompt by default (repoAgent.plugins.autoRun = true); turning it off yields a Run/Reject prompt per external tool call. File edits are blocked from absolute paths and '..' traversal per the README. -- evidence: [README.md#L376-L385](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L376-L385), [docs/PLUGINS.md#L74-L75](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/docs/PLUGINS.md#L74-L75), [README.md#L357-L370](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L357-L370) (`clm_dbb3b4a94ff7321d3e0373b92966d5495d7ff303e99f7bc3d503d5c446e30109`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The extension uses a bring-your-own-key DeepSeek API by default (deepseek-flash default model), and speaks an OpenAI-compatible API so baseUrl can point at OpenAI, OpenRouter, Gemini, or other providers. -- evidence: [README.md#L249-L250](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L249-L250), [README.md#L176-L176](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L176-L176), [README.md#L357-L370](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/README.md#L357-L370) (`clm_0df47d975cdc23dc08387538cf4bb018ab4562951821beca44eadcfd2fd0eba9`)

## limitations (1 claim(s))

- [observation/documented] Per the docs, remote MCP support covers Streamable HTTP with no-auth or bearer token only; legacy SSE-only servers and servers requiring OAuth login are not supported in this build. -- evidence: [docs/PLUGINS.md#L103-L106](https://github.com/sumitsingh4411/repo-agent/blob/703c1afdf6f3f6d291e828852af9db361bcb3cc9/docs/PLUGINS.md#L103-L106) (`clm_6f1a3903af13faf53d0ee0aacc49fd405506897471a85c165496422c082af0aa`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

