# bbarit/terminal -- full detail

[Back to orientation](terminal.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/bbarit/terminal/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/afd231008ab1b632.json](../../../wiki/dossiers/bbarit/terminal/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/afd231008ab1b632.json)

## specifications (1 claim(s))

- [observation/documented] BBARIT Terminal is a free desktop AI coding IDE combining terminal, IDE, and coding agent, built with Tauri v2, Rust, and React 19, distributed for macOS (Apple Silicon) and Windows 10/11. -- evidence: [README.md#L9-L9](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L9-L9), [README.md#L314-L322](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L314-L322), [README.md#L17-L20](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L17-L20), [README.md#L13-L13](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L13-L13) (`clm_31703e8ca5e04516827fca5c580b69c69a34044f453b809b7e0ee7126899c15c`)

## components (3 claim(s))

- [observation/documented] The backend stack is documented as Rust with tokio, axum, and portable-pty; the frontend uses React 19, TypeScript, and Vite 7, with xterm.js plus a WebGL addon for the terminal. -- evidence: [README.md#L314-L322](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L314-L322) (`clm_297525ac9f6ade7ffc529d0c3dd0d79be550ed5cab988d32f832d11931c51791`)
- [observation/documented] The app embeds a Monaco code editor and Tiptap/CodeMirror markdown editors, plus viewers for PDF, Word, PowerPoint, Excel, EPUB, SQLite, JSON, images, video, and audio. -- evidence: [README.md#L275-L280](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L275-L280), [README.md#L206-L215](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L206-L215) (`clm_57688bc17e9a2285ae48cbd01b0513dc15411d790e9e8358f04b8790a4018307`)
- [observation/documented] Developer tooling includes a git panel with worktrees, hybrid BM25 + semantic code search with a code graph, Kanban/Todo/Gantt task views, MCP server connections with a browser MCP bridge and 100+ presets, and MySQL/PostgreSQL database browsing. -- evidence: [README.md#L231-L237](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L231-L237), [README.md#L282-L288](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L282-L288) (`clm_6af3927edae6cb790f8fe9db5b1a7228f6bfe9e6b66fe1a88e7fb8592dab50c5`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The product supports multiple AI CLIs (Claude Code, Codex, Gemini, Kimi, Qwen, Cursor, OpenCode, Ollama, Pi, Reasonix), each run in its own PTY session with per-project model, flags, and autonomy modes (normal, auto-accept, full-auto, yolo). -- evidence: [README.md#L173-L173](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L173-L173), [README.md#L175-L184](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L175-L184), [README.md#L186-L189](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L186-L189), [README.md#L268-L273](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L268-L273) (`clm_2045e793386b6176a11f9d19192adbd27c21a6664bb09d3e38a62f7d552aee02`)
- [observation/documented] Remote access is documented via a browser-based Web Terminal over a Cloudflare tunnel, Telegram/Discord/Slack terminal mirroring, and SSH projects that behave like local ones. -- evidence: [README.md#L297-L301](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L297-L301), [README.md#L243-L246](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L243-L246) (`clm_bffb27743f05870a311ed29716fc2fc3b613cb725c3fcbaec16c8061a3a24c94`)

## memory-state (1 claim(s))

- [observation/documented] A two-tier (project + global) 'Karpathy Wiki' knowledge base is documented, which agents read and write back to, alongside a notes vault with wikilinks, backlinks, tags, and a graph view. -- evidence: [README.md#L290-L295](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L290-L295), [README.md#L221-L225](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L221-L225) (`clm_78764217335934e0dbe38206add05ac6de101c513b10e0d0b9501404b607900d`)

## orchestration (2 claim(s))

- [observation/documented] A Broker Agent feature opens a Developer and Reviewer terminal pair mediated by a deterministic, non-LLM broker that judges diffs via git growth, code-graph impact, and sensitivity patterns, then auto-merges on approval. -- evidence: [README.md#L143-L143](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L143-L143), [README.md#L156-L165](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L156-L165), [README.md#L147-L152](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L147-L152) (`clm_79110435ae7f91076ed1ca9597288a44875217409c4d11931c0c8db81e604c68`)
- [observation/documented] Broker harnesses run in isolated git worktrees under .octo-tmp/broker-wt-…, never touching the user's working tree, and support parallel multi-harness management, model hot-swapping, and session auto-restore. -- evidence: [README.md#L156-L165](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L156-L165), [README.md#L361-L370](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L361-L370) (`clm_7f6fea46fd2cf493faaf0396fb5bf18ec57683ce6ba615818884afd1b240a76b`)

## tools-permissions (1 claim(s))

- [observation/documented] The built-in BBARIT Agent is documented to enforce a verify loop (tests/build must pass by exit code), block edits to files changed on disk without a prior read, snapshot every change for rollback, and block catastrophic commands like rm -rf /, mkfs, and raw disk writes. -- evidence: [README.md#L130-L135](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L130-L135), [README.md#L268-L273](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L268-L273) (`clm_051cec14ccece35ef6350f75ce306d45318454673f25fff81892aaaffc5f826e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] BBARIT Agent is documented to support 37 providers and 1,000+ models including OpenAI, Anthropic, Google, Mistral, AWS Bedrock, and Azure, with subscription login, API keys, or fully local Ollama. -- evidence: [README.md#L130-L135](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L130-L135), [README.md#L361-L370](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L361-L370) (`clm_1c3264a9521ee05a19794c8720d33d0b922f367227c8d23b32ff4278801aaec4`)

## limitations (1 claim(s))

- [observation/documented] Per the requirements table, macOS requires Apple Silicon (M1 or later) and Windows requires 10/11 64-bit; users must separately install the AI CLIs they want the app to drive. -- evidence: [README.md#L341-L346](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L341-L346) (`clm_ba01eb5d0198874e8049c4e438fad606ae630ee47b3f4e5518d66abc58e11566`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

