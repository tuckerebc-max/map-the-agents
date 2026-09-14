# bbarit/terminal

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b219ba8199da @ afd231008ab1b632

## Summary (orientation draft, not independently verified)

The snapshot contains only README content describing BBARIT Terminal, a Rust/Tauri desktop AI coding IDE with a built-in agent, broker dev/review pairs, multi-AI terminals, and bundled editors/tools. All claims below are documentation-based; no code, tests, or contributor workflows are evidenced.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] BBARIT Terminal is a free desktop AI coding IDE combining terminal, IDE, and coding agent, built with Tauri v2, Rust, and React 19, distributed for macOS (Apple Silicon) and Windows 10/11. -- evidence: [README.md#L9-L9](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L9-L9), [README.md#L314-L322](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L314-L322), [README.md#L17-L20](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L17-L20), [README.md#L13-L13](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L13-L13)
- components (3 claim(s)):
  - [observation/documented] The backend stack is documented as Rust with tokio, axum, and portable-pty; the frontend uses React 19, TypeScript, and Vite 7, with xterm.js plus a WebGL addon for the terminal. -- evidence: [README.md#L314-L322](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L314-L322)
  - [observation/documented] The app embeds a Monaco code editor and Tiptap/CodeMirror markdown editors, plus viewers for PDF, Word, PowerPoint, Excel, EPUB, SQLite, JSON, images, video, and audio. -- evidence: [README.md#L275-L280](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L275-L280), [README.md#L206-L215](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L206-L215)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product supports multiple AI CLIs (Claude Code, Codex, Gemini, Kimi, Qwen, Cursor, OpenCode, Ollama, Pi, Reasonix), each run in its own PTY session with per-project model, flags, and autonomy modes (normal, auto-accept, full-auto, yolo). -- evidence: [README.md#L173-L173](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L173-L173), [README.md#L175-L184](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L175-L184), [README.md#L186-L189](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L186-L189), [README.md#L268-L273](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L268-L273)
  - [observation/documented] Remote access is documented via a browser-based Web Terminal over a Cloudflare tunnel, Telegram/Discord/Slack terminal mirroring, and SSH projects that behave like local ones. -- evidence: [README.md#L297-L301](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L297-L301), [README.md#L243-L246](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L243-L246)
- memory-state (1 claim(s)):
  - [observation/documented] A two-tier (project + global) 'Karpathy Wiki' knowledge base is documented, which agents read and write back to, alongside a notes vault with wikilinks, backlinks, tags, and a graph view. -- evidence: [README.md#L290-L295](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L290-L295), [README.md#L221-L225](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L221-L225)
- orchestration (2 claim(s)):
  - [observation/documented] A Broker Agent feature opens a Developer and Reviewer terminal pair mediated by a deterministic, non-LLM broker that judges diffs via git growth, code-graph impact, and sensitivity patterns, then auto-merges on approval. -- evidence: [README.md#L143-L143](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L143-L143), [README.md#L156-L165](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L156-L165), [README.md#L147-L152](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L147-L152)
  - [observation/documented] Broker harnesses run in isolated git worktrees under .octo-tmp/broker-wt-…, never touching the user's working tree, and support parallel multi-harness management, model hot-swapping, and session auto-restore. -- evidence: [README.md#L156-L165](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L156-L165), [README.md#L361-L370](https://github.com/bbarit/terminal/blob/b219ba8199da880a6ae717e9b8eac00cbeb1b3bc/README.md#L361-L370)
- tools-permissions (1 claim(s)):
More evidence: [full detail](terminal.detail.md)

Metadata and full claim list: [full detail](terminal.detail.md)
Human notes ([notes](terminal.notes.md), never overwritten by build)

[Back to map index](../../index.md)
