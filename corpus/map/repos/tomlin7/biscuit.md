# tomlin7/biscuit

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 85c5beb0c624 @ 912a5b85f4128f0b

## Summary (orientation draft, not independently verified)

Biscuit is described as a fast, extensible native code editor with agents, under 20 MB in size, installable in seconds. The editor is built with Python and Tkinter, runs natively on Windows, Linux, and macOS, and is not an Electron app.

## Source coverage

Source coverage (partial): 6 of 46 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] Biscuit is described as a fast, extensible native code editor with agents, under 20 MB in size, installable in seconds. -- evidence: [README.md#L15-L15](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L15-L15), [docs/index.mdx#L6-L8](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/index.mdx#L6-L8)
  - [observation/documented] The editor is built with Python and Tkinter, runs natively on Windows, Linux, and macOS, and is not an Electron app. -- evidence: [docs/index.mdx#L1-L4](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/index.mdx#L1-L4), [docs/index.mdx#L6-L8](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/index.mdx#L6-L8), [docs/index.mdx#L10-L20](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/index.mdx#L10-L20)
- components (6 claim(s)):
  - [observation/documented] The built-in planning agent ships with eleven tools, including ReadFile, EditFile, DeleteFile, ListDir, GlobFileSearch, Grep, CodebaseSearch, RunTerminalCmd, TodoWrite, GetWorkspaceInfo, and GetActiveEditor. -- evidence: [docs/index.mdx#L36-L42](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/index.mdx#L36-L42), [README.md#L49-L67](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L49-L67)
  - [observation/documented] The agent supports Gemini and Anthropic APIs (claude-4-5-opus/sonnet/haiku, gemini-2-5-flash/pro), file attachment for chat context, and additional LLM providers via extensions. -- evidence: [README.md#L49-L67](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L49-L67)
- design-choices (1 claim(s)):
  - [observation/documented] The extension system is Python-based, covering language servers, formatters, AI providers, and UI views, contrasting with JS/TS plugin systems of traditional editors. -- evidence: [docs/index.mdx#L36-L42](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/index.mdx#L36-L42), [docs/index.mdx#L24-L32](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/index.mdx#L24-L32), [docs/index.mdx#L10-L20](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/index.mdx#L10-L20)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors are directed to a contributing guide and docs for project structure and environment setup, and the project supports both Poetry and uv for dependency management. -- evidence: [README.md#L42-L43](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L42-L43), [README.md#L38-L40](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L38-L40)
  - [observation/documented] Repository development practice: source installation uses `poetry install` or `uv sync`, then runs via `poetry run biscuit` or `uv run biscuit`; Python 3.10+ is required (3.11+ recommended for development). -- evidence: [docs/installation.mdx#L49-L49](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L49-L49), [docs/installation.mdx#L59-L63](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L59-L63), [docs/installation.mdx#L70-L71](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L70-L71), [docs/installation.mdx#L51-L55](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L51-L55), [docs/installation.mdx#L67-L68](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L67-L68), [docs/installation.mdx#L57-L57](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L57-L57), [docs/installation.mdx#L8-L8](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L8-L8)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI accepts `biscuit [OPTIONS] [PATH]`, with subcommands including open, goto (line:column), clone, diff, and doc. -- evidence: [docs/cli-reference.mdx#L8-L10](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/cli-reference.mdx#L8-L10), [docs/cli-reference.mdx#L48-L50](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/cli-reference.mdx#L48-L50), [docs/cli-reference.mdx#L16-L20](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/cli-reference.mdx#L16-L20), [docs/cli-reference.mdx#L24-L26](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/cli-reference.mdx#L24-L26), [docs/cli-reference.mdx#L30-L32](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/cli-reference.mdx#L30-L32), [docs/cli-reference.mdx#L42-L44](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/cli-reference.mdx#L42-L44), [docs/cli-reference.mdx#L36-L38](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/cli-reference.mdx#L36-L38)
  - [observation/documented] CLI options include --version, --dev (development mode launch), and --help. -- evidence: [docs/cli-reference.mdx#L91-L95](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/cli-reference.mdx#L91-L95)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Linux installation may require system packages such as fontconfig, a C++ compiler, and CMake, plus pip-installed scikit-build on Debian-based distributions. -- evidence: [docs/installation.mdx#L82-L84](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L82-L84), [docs/installation.mdx#L77-L80](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L77-L80)
- limitations (1 claim(s)):
More evidence: [full detail](biscuit.detail.md)

Metadata and full claim list: [full detail](biscuit.detail.md)
Human notes ([notes](biscuit.notes.md), never overwritten by build)

[Back to map index](../../index.md)
