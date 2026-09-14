---
access: public
aliases: []
claim_ids:
- clm_051cec14ccece35ef6350f75ce306d45318454673f25fff81892aaaffc5f826e
- clm_1c3264a9521ee05a19794c8720d33d0b922f367227c8d23b32ff4278801aaec4
- clm_2045e793386b6176a11f9d19192adbd27c21a6664bb09d3e38a62f7d552aee02
- clm_297525ac9f6ade7ffc529d0c3dd0d79be550ed5cab988d32f832d11931c51791
- clm_31703e8ca5e04516827fca5c580b69c69a34044f453b809b7e0ee7126899c15c
- clm_57688bc17e9a2285ae48cbd01b0513dc15411d790e9e8358f04b8790a4018307
- clm_6af3927edae6cb790f8fe9db5b1a7228f6bfe9e6b66fe1a88e7fb8592dab50c5
- clm_78764217335934e0dbe38206add05ac6de101c513b10e0d0b9501404b607900d
- clm_79110435ae7f91076ed1ca9597288a44875217409c4d11931c0c8db81e604c68
- clm_7f6fea46fd2cf493faaf0396fb5bf18ec57683ce6ba615818884afd1b240a76b
- clm_ba01eb5d0198874e8049c4e438fad606ae630ee47b3f4e5518d66abc58e11566
- clm_bffb27743f05870a311ed29716fc2fc3b613cb725c3fcbaec16c8061a3a24c94
maturity: draft
page_id: pg_c76f36f87ca25b1dabb7de499c70c22c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_09f8fc8f2f7a5ad38a40c65437afe543
title: bbarit/terminal/README.md @ b219ba8199da
updated_at: '2026-09-14T01:37:40Z'
---

# bbarit/terminal/README.md @ b219ba8199da

<!-- rcw:begin owner=source:src_09f8fc8f2f7a5ad38a40c65437afe543 block=evidence -->
- The built-in BBARIT Agent is documented to enforce a verify loop (tests/build must pass by exit code), block edits to files changed on disk without a prior read, snapshot every change for rollback, and block catastrophic commands like rm -rf /, mkfs, and raw disk writes. [@claim:clm_051cec14ccece35ef6350f75ce306d45318454673f25fff81892aaaffc5f826e]
- BBARIT Agent is documented to support 37 providers and 1,000+ models including OpenAI, Anthropic, Google, Mistral, AWS Bedrock, and Azure, with subscription login, API keys, or fully local Ollama. [@claim:clm_1c3264a9521ee05a19794c8720d33d0b922f367227c8d23b32ff4278801aaec4]
- The product supports multiple AI CLIs (Claude Code, Codex, Gemini, Kimi, Qwen, Cursor, OpenCode, Ollama, Pi, Reasonix), each run in its own PTY session with per-project model, flags, and autonomy modes (normal, auto-accept, full-auto, yolo). [@claim:clm_2045e793386b6176a11f9d19192adbd27c21a6664bb09d3e38a62f7d552aee02]
- The backend stack is documented as Rust with tokio, axum, and portable-pty; the frontend uses React 19, TypeScript, and Vite 7, with xterm.js plus a WebGL addon for the terminal. [@claim:clm_297525ac9f6ade7ffc529d0c3dd0d79be550ed5cab988d32f832d11931c51791]
- BBARIT Terminal is a free desktop AI coding IDE combining terminal, IDE, and coding agent, built with Tauri v2, Rust, and React 19, distributed for macOS (Apple Silicon) and Windows 10/11. [@claim:clm_31703e8ca5e04516827fca5c580b69c69a34044f453b809b7e0ee7126899c15c]
- The app embeds a Monaco code editor and Tiptap/CodeMirror markdown editors, plus viewers for PDF, Word, PowerPoint, Excel, EPUB, SQLite, JSON, images, video, and audio. [@claim:clm_57688bc17e9a2285ae48cbd01b0513dc15411d790e9e8358f04b8790a4018307]
- Developer tooling includes a git panel with worktrees, hybrid BM25 + semantic code search with a code graph, Kanban/Todo/Gantt task views, MCP server connections with a browser MCP bridge and 100+ presets, and MySQL/PostgreSQL database browsing. [@claim:clm_6af3927edae6cb790f8fe9db5b1a7228f6bfe9e6b66fe1a88e7fb8592dab50c5]
- A two-tier (project + global) 'Karpathy Wiki' knowledge base is documented, which agents read and write back to, alongside a notes vault with wikilinks, backlinks, tags, and a graph view. [@claim:clm_78764217335934e0dbe38206add05ac6de101c513b10e0d0b9501404b607900d]
- A Broker Agent feature opens a Developer and Reviewer terminal pair mediated by a deterministic, non-LLM broker that judges diffs via git growth, code-graph impact, and sensitivity patterns, then auto-merges on approval. [@claim:clm_79110435ae7f91076ed1ca9597288a44875217409c4d11931c0c8db81e604c68]
- Broker harnesses run in isolated git worktrees under .octo-tmp/broker-wt-…, never touching the user's working tree, and support parallel multi-harness management, model hot-swapping, and session auto-restore. [@claim:clm_7f6fea46fd2cf493faaf0396fb5bf18ec57683ce6ba615818884afd1b240a76b]
- Per the requirements table, macOS requires Apple Silicon (M1 or later) and Windows requires 10/11 64-bit; users must separately install the AI CLIs they want the app to drive. [@claim:clm_ba01eb5d0198874e8049c4e438fad606ae630ee47b3f4e5518d66abc58e11566]
- Remote access is documented via a browser-based Web Terminal over a Cloudflare tunnel, Telegram/Discord/Slack terminal mirroring, and SSH projects that behave like local ones. [@claim:clm_bffb27743f05870a311ed29716fc2fc3b613cb725c3fcbaec16c8061a3a24c94]
<!-- rcw:end owner=source:src_09f8fc8f2f7a5ad38a40c65437afe543 block=evidence -->

## Researcher notes

