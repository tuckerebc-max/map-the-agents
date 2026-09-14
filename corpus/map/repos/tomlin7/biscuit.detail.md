# tomlin7/biscuit -- full detail

[Back to orientation](biscuit.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tomlin7/biscuit/85c5beb0c624c1885d994c63bb1a24ce19599467/912a5b85f4128f0b.json](../../../wiki/dossiers/tomlin7/biscuit/85c5beb0c624c1885d994c63bb1a24ce19599467/912a5b85f4128f0b.json)

## specifications (2 claim(s))

- [observation/documented] Biscuit is described as a fast, extensible native code editor with agents, under 20 MB in size, installable in seconds. -- evidence: [README.md#L15-L15](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L15-L15), [docs/index.mdx#L6-L8](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/index.mdx#L6-L8) (`clm_a48fad887d5b6a96a1e3c123e1944612268a4ee01a7a69e669d2c725824cff28`)
- [observation/documented] The editor is built with Python and Tkinter, runs natively on Windows, Linux, and macOS, and is not an Electron app. -- evidence: [docs/index.mdx#L1-L4](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/index.mdx#L1-L4), [docs/index.mdx#L6-L8](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/index.mdx#L6-L8), [docs/index.mdx#L10-L20](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/index.mdx#L10-L20) (`clm_93ac0411ece4dc1826b3f4ce74f01d0551eb292266c692bb2d9df88452bd00b9`)

## components (6 claim(s))

- [observation/documented] The built-in planning agent ships with eleven tools, including ReadFile, EditFile, DeleteFile, ListDir, GlobFileSearch, Grep, CodebaseSearch, RunTerminalCmd, TodoWrite, GetWorkspaceInfo, and GetActiveEditor. -- evidence: [docs/index.mdx#L36-L42](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/index.mdx#L36-L42), [README.md#L49-L67](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L49-L67) (`clm_d1a3d8738564346186256a7d96adeab5c270a71c80fa7795ca0218e3684e0f42`)
- [observation/documented] The agent supports Gemini and Anthropic APIs (claude-4-5-opus/sonnet/haiku, gemini-2-5-flash/pro), file attachment for chat context, and additional LLM providers via extensions. -- evidence: [README.md#L49-L67](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L49-L67) (`clm_aa3163a8490f476852ff672986d4e6275bc7987e82977a700d6ae98f1e9a808d`)
- [observation/documented] Code intelligence features tree-sitter parsing/highlights, completions, hover docs, symbol outline, symbol search, peek-to-definition, and references, with more language servers added via extensions. -- evidence: [README.md#L71-L78](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L71-L78), [README.md#L80-L80](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L80-L80) (`clm_c9061fde8880895b165c7a61361b6ed8fa8119479150eb2af5c3420985095494`)
- [observation/documented] Source control features include a split diff viewer, git operations (push, pull, commit, stage, unstage, branch switching), and repository cloning; GitHub issues/PR viewing is currently disabled pending conversion to an extension. -- evidence: [README.md#L86-L89](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L86-L89) (`clm_7878b95867aa8d35473f1c4398098296e09bf68f091a9a5123981356e6206d2e`)
- [observation/documented] Search is ripgrep-based with regex and case-sensitivity support, individual or bulk replace, and a floating find-replace widget in open editors. -- evidence: [README.md#L93-L96](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L93-L96) (`clm_f7fd5e4d88aba0ae25efcf4fa2f6fb07f088c8d9be136f5659657ffa211bbc8e`)
- [observation/documented] Debugging includes breakpoints, runtime variable inspection and modification, call stack visualization, and a built-in Python debugger; additional debuggers can be registered via extensions. -- evidence: [README.md#L102-L108](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L102-L108) (`clm_ed00676f8acf685710ec605ca6658485b7af8ab3572b2f6c2593b90fd4496e14`)

## design-choices (1 claim(s))

- [observation/documented] The extension system is Python-based, covering language servers, formatters, AI providers, and UI views, contrasting with JS/TS plugin systems of traditional editors. -- evidence: [docs/index.mdx#L36-L42](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/index.mdx#L36-L42), [docs/index.mdx#L24-L32](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/index.mdx#L24-L32), [docs/index.mdx#L10-L20](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/index.mdx#L10-L20) (`clm_40c83cdcf21f3b201c2da4a4efdf01b0570e41b13bf076e72b0308a6d7ef03df`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors are directed to a contributing guide and docs for project structure and environment setup, and the project supports both Poetry and uv for dependency management. -- evidence: [README.md#L42-L43](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L42-L43), [README.md#L38-L40](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L38-L40) (`clm_476218364a80222ce97f6907ae611b1ed01afc6d29028c4b04679d8b7e7bbbbb`)
- [observation/documented] Repository development practice: source installation uses `poetry install` or `uv sync`, then runs via `poetry run biscuit` or `uv run biscuit`; Python 3.10+ is required (3.11+ recommended for development). -- evidence: [docs/installation.mdx#L49-L49](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L49-L49), [docs/installation.mdx#L59-L63](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L59-L63), [docs/installation.mdx#L70-L71](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L70-L71), [docs/installation.mdx#L51-L55](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L51-L55), [docs/installation.mdx#L67-L68](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L67-L68), [docs/installation.mdx#L57-L57](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L57-L57), [docs/installation.mdx#L8-L8](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L8-L8) (`clm_21408efd9f3ff9cd2d3be42b08ad74659ed1b0dc4777452ff209256eb276a8da`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI accepts `biscuit [OPTIONS] [PATH]`, with subcommands including open, goto (line:column), clone, diff, and doc. -- evidence: [docs/cli-reference.mdx#L8-L10](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/cli-reference.mdx#L8-L10), [docs/cli-reference.mdx#L48-L50](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/cli-reference.mdx#L48-L50), [docs/cli-reference.mdx#L16-L20](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/cli-reference.mdx#L16-L20), [docs/cli-reference.mdx#L24-L26](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/cli-reference.mdx#L24-L26), [docs/cli-reference.mdx#L30-L32](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/cli-reference.mdx#L30-L32), [docs/cli-reference.mdx#L42-L44](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/cli-reference.mdx#L42-L44), [docs/cli-reference.mdx#L36-L38](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/cli-reference.mdx#L36-L38) (`clm_98a44489363c5d90b422858fbd14b14a50b8b81803e855fcab84c59beaef1de3`)
- [observation/documented] CLI options include --version, --dev (development mode launch), and --help. -- evidence: [docs/cli-reference.mdx#L91-L95](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/cli-reference.mdx#L91-L95) (`clm_32c6238a233292b67da41ffe243ac40ab6edf64ab17dd5f27ab64405034c9b56`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Linux installation may require system packages such as fontconfig, a C++ compiler, and CMake, plus pip-installed scikit-build on Debian-based distributions. -- evidence: [docs/installation.mdx#L82-L84](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L82-L84), [docs/installation.mdx#L77-L80](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/docs/installation.mdx#L77-L80) (`clm_99da2986b0907c2f008e8b9f604761a09266c1342dc5ebff0a5eaba9faba87b2`)

## limitations (1 claim(s))

- [observation/documented] Per the README checklist, full DAP client integration, vim mode support, LLM provider extension examples, and an ollama extension rewrite remain incomplete; the old ollama and several formatter extensions are deprecated. -- evidence: [README.md#L122-L129](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L122-L129), [README.md#L49-L67](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L49-L67), [README.md#L102-L108](https://github.com/tomlin7/biscuit/blob/85c5beb0c624c1885d994c63bb1a24ce19599467/README.md#L102-L108) (`clm_60d844d9217015d89201914f2b57f8425aed37dc19e3ae40d2dac2bdb840784f`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

