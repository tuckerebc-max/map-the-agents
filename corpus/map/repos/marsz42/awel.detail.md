# marsz42/awel -- full detail

[Back to orientation](awel.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/marsz42/awel/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/4b213dd8f93324f0.json](../../../wiki/dossiers/marsz42/awel/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/4b213dd8f93324f0.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] HMR/WebSocket traffic is proxied through transparently and paused while the agent edits files, to prevent hot-reload interference. -- evidence: [README.md#L60-L60](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L60-L60) (`clm_91f9abca059948acdee6f00ba63503a79de03360dfda391c76c9656a0aa8b12d`)
- [observation/documented] The dashboard offers an element inspector for attaching selected DOM elements as prompt context, a screenshot annotator, image attachments, plan approval, per-session undo of agent file changes, and diff review before accepting changes. -- evidence: [README.md#L104-L104](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L104-L104), [README.md#L112-L120](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L112-L120), [README.md#L108-L108](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L108-L108) (`clm_3f635834af19b65b5eaadf1046cf9df56e3c8749476d5b853e6ffd85acf98195`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the README's Development section lists npm scripts for building everything, CLI watch mode, running tests, and test watch mode; contributor notes specify Vitest for tests and separate build pipelines (tsc for CLI, Vite for dashboard, esbuild for host). -- evidence: [CLAUDE.md#L292-L297](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/CLAUDE.md#L292-L297), [CLAUDE.md#L31-L38](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/CLAUDE.md#L31-L38), [README.md#L133-L137](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L133-L137), [README.md#L124-L129](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L124-L129) (`clm_ed7ea7cd91c6f6cbdde6e56392485b9be8a95b4771581305fdd92abfdc23dc85`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Awel runs a proxy on port 3001 in front of the Next.js dev server on port 3000, intercepts HTML responses to inject a script, and opens a full-screen chat dashboard in an iframe from a floating Shadow DOM button. -- evidence: [README.md#L55-L58](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L55-L58), [README.md#L34-L34](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L34-L34), [README.md#L51-L53](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L51-L53), [README.md#L5-L5](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L5-L5) (`clm_a59d28db92b902eacfc1bed2e8eb07a6d2a0170ca78b5538f1edb5ff9a38a86b`)
- [observation/documented] The CLI exposes two commands: `awel create` to scaffold a new Next.js project in creation mode, and `awel dev` with options `-p/--port` (default 3000), `-v/--verbose` for LLM stream events on stderr, and `--no-open`. -- evidence: [README.md#L23-L23](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L23-L23), [README.md#L42-L45](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L42-L45), [README.md#L38-L40](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L38-L40) (`clm_013a36dbe9fd8f2c84bcf87e95975daa11a994d83c7d0102e8caa22ed0bac309`)
- [inference/documented] Model switching appears to be supported at runtime via a dropdown in the dashboard header, with at least one configured provider required for Awel to function. -- evidence: [README.md#L32-L32](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L32-L32), [README.md#L77-L77](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L77-L77) (`clm_05c8cc81de4879fcc1f6df75a57005dbd6942278a2a7fa10d61c3177adb4fdf3`)

## memory-state (1 claim(s))

- [observation/documented] The agent includes a Memory tool to store and retrieve persistent project knowledge, and the product advertises saving and recalling project-specific knowledge across sessions. -- evidence: [README.md#L92-L100](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L92-L100), [README.md#L112-L120](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L112-L120) (`clm_9a36544b8c582d4ea382568cd8ef649be1264e01f362cf5b15642c3449b33f18`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] The agent has tools for file read/write/edit, shell commands, code search, web search/fetch, plan proposal, user questions, dev-server restart, todo tracking, and persistent memory, with file edits and shell commands subject to optional user confirmation. -- evidence: [README.md#L92-L100](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L92-L100) (`clm_4744c115b07d63f708e42752d86cf58a17c9e3d02fe7791eacd2156b2728097e`)
- [observation/documented] Claude Code models run in 'YOLO mode', automatically approving all file edits and shell commands without confirmation; a warning is displayed when such a model is selected. -- evidence: [README.md#L79-L79](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L79-L79) (`clm_bdc8b859495abc0bba5cf243335f5e270e5b03b85da6cb009d095f2bf7ebb954`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Awel is built on the Vercel AI SDK and supports multiple providers configured via environment variables, including Anthropic, OpenAI, Google AI, MiniMax, Zhipu, Vercel Gateway, OpenRouter, and a Claude CLI in PATH. -- evidence: [README.md#L64-L64](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L64-L64), [README.md#L66-L75](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L66-L75) (`clm_7cdbe55d1ac966914171516d14b699b1e8932f21cf72a72d198431d10e6edfb8`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] Awel targets Next.js developers, letting them converse with an AI agent that can read, write, and edit project files from an embedded dashboard during development. -- evidence: [README.md#L5-L5](https://github.com/MarsZ42/Awel/blob/3687fea3fa73c172ff91f6f6dc8ea89953c8da06/README.md#L5-L5) (`clm_85ba173b72b3e1aeebebed01537054c397dab540a366d809f8301dfc08af863d`)

