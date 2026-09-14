---
access: public
aliases: []
claim_ids:
- clm_013a36dbe9fd8f2c84bcf87e95975daa11a994d83c7d0102e8caa22ed0bac309
- clm_05c8cc81de4879fcc1f6df75a57005dbd6942278a2a7fa10d61c3177adb4fdf3
- clm_3f635834af19b65b5eaadf1046cf9df56e3c8749476d5b853e6ffd85acf98195
- clm_4744c115b07d63f708e42752d86cf58a17c9e3d02fe7791eacd2156b2728097e
- clm_7cdbe55d1ac966914171516d14b699b1e8932f21cf72a72d198431d10e6edfb8
- clm_85ba173b72b3e1aeebebed01537054c397dab540a366d809f8301dfc08af863d
- clm_91f9abca059948acdee6f00ba63503a79de03360dfda391c76c9656a0aa8b12d
- clm_9a36544b8c582d4ea382568cd8ef649be1264e01f362cf5b15642c3449b33f18
- clm_a59d28db92b902eacfc1bed2e8eb07a6d2a0170ca78b5538f1edb5ff9a38a86b
- clm_bdc8b859495abc0bba5cf243335f5e270e5b03b85da6cb009d095f2bf7ebb954
- clm_ed7ea7cd91c6f6cbdde6e56392485b9be8a95b4771581305fdd92abfdc23dc85
maturity: draft
page_id: pg_22ef4202d02e5b1aa02cf743024858f7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_acaa2f1f71745dbdada5ad4f7a1757ab
title: MarsZ42/Awel/README.md @ 3687fea3fa73
updated_at: '2026-09-14T02:16:19Z'
---

# MarsZ42/Awel/README.md @ 3687fea3fa73

<!-- rcw:begin owner=source:src_acaa2f1f71745dbdada5ad4f7a1757ab block=evidence -->
- The CLI exposes two commands: `awel create` to scaffold a new Next.js project in creation mode, and `awel dev` with options `-p/--port` (default 3000), `-v/--verbose` for LLM stream events on stderr, and `--no-open`. [@claim:clm_013a36dbe9fd8f2c84bcf87e95975daa11a994d83c7d0102e8caa22ed0bac309]
- Model switching appears to be supported at runtime via a dropdown in the dashboard header, with at least one configured provider required for Awel to function. [@claim:clm_05c8cc81de4879fcc1f6df75a57005dbd6942278a2a7fa10d61c3177adb4fdf3]
- The dashboard offers an element inspector for attaching selected DOM elements as prompt context, a screenshot annotator, image attachments, plan approval, per-session undo of agent file changes, and diff review before accepting changes. [@claim:clm_3f635834af19b65b5eaadf1046cf9df56e3c8749476d5b853e6ffd85acf98195]
- The agent has tools for file read/write/edit, shell commands, code search, web search/fetch, plan proposal, user questions, dev-server restart, todo tracking, and persistent memory, with file edits and shell commands subject to optional user confirmation. [@claim:clm_4744c115b07d63f708e42752d86cf58a17c9e3d02fe7791eacd2156b2728097e]
- Awel is built on the Vercel AI SDK and supports multiple providers configured via environment variables, including Anthropic, OpenAI, Google AI, MiniMax, Zhipu, Vercel Gateway, OpenRouter, and a Claude CLI in PATH. [@claim:clm_7cdbe55d1ac966914171516d14b699b1e8932f21cf72a72d198431d10e6edfb8]
- Awel targets Next.js developers, letting them converse with an AI agent that can read, write, and edit project files from an embedded dashboard during development. [@claim:clm_85ba173b72b3e1aeebebed01537054c397dab540a366d809f8301dfc08af863d]
- HMR/WebSocket traffic is proxied through transparently and paused while the agent edits files, to prevent hot-reload interference. [@claim:clm_91f9abca059948acdee6f00ba63503a79de03360dfda391c76c9656a0aa8b12d]
- The agent includes a Memory tool to store and retrieve persistent project knowledge, and the product advertises saving and recalling project-specific knowledge across sessions. [@claim:clm_9a36544b8c582d4ea382568cd8ef649be1264e01f362cf5b15642c3449b33f18]
- Awel runs a proxy on port 3001 in front of the Next.js dev server on port 3000, intercepts HTML responses to inject a script, and opens a full-screen chat dashboard in an iframe from a floating Shadow DOM button. [@claim:clm_a59d28db92b902eacfc1bed2e8eb07a6d2a0170ca78b5538f1edb5ff9a38a86b]
- Claude Code models run in 'YOLO mode', automatically approving all file edits and shell commands without confirmation; a warning is displayed when such a model is selected. [@claim:clm_bdc8b859495abc0bba5cf243335f5e270e5b03b85da6cb009d095f2bf7ebb954]
- Repository development practice: the README's Development section lists npm scripts for building everything, CLI watch mode, running tests, and test watch mode; contributor notes specify Vitest for tests and separate build pipelines (tsc for CLI, Vite for dashboard, esbuild for host). [@claim:clm_ed7ea7cd91c6f6cbdde6e56392485b9be8a95b4771581305fdd92abfdc23dc85]
<!-- rcw:end owner=source:src_acaa2f1f71745dbdada5ad4f7a1757ab block=evidence -->

## Researcher notes

