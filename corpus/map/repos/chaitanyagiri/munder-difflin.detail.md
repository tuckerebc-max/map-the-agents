# chaitanyagiri/munder-difflin -- full detail

[Back to orientation](munder-difflin.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/chaitanyagiri/munder-difflin/417d8decf08c4e4da484a5c3c35aa6e8925e5989/ba331b94f28a7410.json](../../../wiki/dossiers/chaitanyagiri/munder-difflin/417d8decf08c4e4da484a5c3c35aa6e8925e5989/ba331b94f28a7410.json)

## specifications (1 claim(s))

- [observation/documented] The product is a desktop app that wraps real terminal-agent CLIs as agents, wires them into a hive mind, and puts a clone agent (Michael) in charge of coordination. -- evidence: [README.md#L107-L110](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L107-L110) (`clm_e7384455ef5657337aee8f18de3759367f7cdbe54b5f004d55836bbb51d187c4`)

## components (1 claim(s))

- [observation/documented] The app is built with Electron, React, TypeScript, Pixi.js, xterm.js, and node-pty; each agent session runs as a real process in a pseudo-terminal rendered with xterm.js. -- evidence: [README.md#L112-L119](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L112-L119), [README.md#L27-L29](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L27-L29) (`clm_fed551d34d91f84d971dd2a7474833e2a48bc6a5fa7203a9e8cd9a5daed43c3e`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: every pull request must include before/after evidence under the PR template's '### Before' and '### After' headings, enforced by an automated 'PR evidence' check; PRs failing it do not merge, with only a maintainer-applied no-visual-change label as exemption. -- evidence: [CONTRIBUTING.md#L95-L98](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/CONTRIBUTING.md#L95-L98), [README.md#L392-L397](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L392-L397), [CONTRIBUTING.md#L74-L77](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/CONTRIBUTING.md#L74-L77) (`clm_14571f2290ebc55febcdc46a4bb40def3470ac79f66868295bcfdf15fabd0cea`)
- [observation/documented] Repository development practice: contributors run npm install && npm run dev, keep npm run typecheck green, run npm run test:focused, confirm npm run build works, derive new UI from DESIGN.md tokens, and keep changes scoped to one improvement per PR. -- evidence: [CONTRIBUTING.md#L102-L121](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/CONTRIBUTING.md#L102-L121), [README.md#L387-L390](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L387-L390), [CONTRIBUTING.md#L17-L33](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/CONTRIBUTING.md#L17-L33) (`clm_65cf00780d4f07718226eae1a26da217219985d373045518e0de39091763f1bf`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Supported agent CLIs include Claude Code, Codex, Grok, Kimi, Gemini CLI, Antigravity, Qwen, OpenCode, Crush, pi.dev, Copilot CLI, and Cursor, plus custom commands and local models via Ollama, LM Studio, or vLLM. -- evidence: [README.md#L103-L103](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L103-L103), [README.md#L21-L25](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L21-L25), [README.md#L87-L101](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L87-L101) (`clm_48f3414a230ea43a10887f6e6861efe1e4ff8fdc5440503271c72e6c675b624e`)
- [observation/documented] The architecture has two data planes — a terminal plane owning PTYs, filesystem and git, and an event plane running the hive, hook server, and router — with the renderer accessing both only through a typed bridge. -- evidence: [README.md#L352-L354](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L352-L354) (`clm_d1d0bd3ef3c5bea3aa82d4ec6a60e604b755d58608782991a4227bf843176e33`)
- [observation/documented] The UI includes a Command Center with kanban tasks, scheduled missions, live fleet monitoring, memory search, a Skills catalog of 227 installable skills, and a built-in Monaco IDE with git rails; all fs/git access is brokered through main. -- evidence: [README.md#L254-L257](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L254-L257) (`clm_acb94360ef1f441b69bdbf73cde7c4ebbf6115edd3baa81bf45f616540ba7c18`)

## memory-state (2 claim(s))

- [observation/documented] The hive is a local git repo of plain files: agents write to their own outbox, a router delivers to recipients' inboxes, and only the harness touches git (single-committer design to avoid index.lock corruption). -- evidence: [README.md#L140-L149](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L140-L149) (`clm_c006d9232cba52d1aab4fd8e674d1604ad01321cb285cdcd3dc55e167d210632`)
- [observation/documented] Each agent keeps markdown memory mined into a shared searchable memory palace with a semantic recall index, persisting across sessions; the semantic index is optional and markdown memory works without it. -- evidence: [README.md#L112-L119](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L112-L119), [README.md#L312-L325](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L312-L325), [README.md#L189-L190](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L189-L190) (`clm_d4f2c143576f72c17b29e346fd4affe3de9c10d38f31e299eb333f8a0697fd79`)

## orchestration (1 claim(s))

- [observation/documented] A GOD agent acts as orchestrator: it reads requests, resolves routine ones autonomously, routes messages between agent inboxes, and escalates critical items (spend, destructive ops, scope changes) to a human approvals queue. -- evidence: [README.md#L112-L119](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L112-L119), [README.md#L140-L149](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L140-L149) (`clm_94e66f6e6fbbcc586ddf284bd30d34f4d63364bfb126e87fff2ad7c1969488bb`)

## tools-permissions (1 claim(s))

- [observation/documented] Per-agent autonomy settings control how far agents act alone; spend, scope, and destructive operations escalate to the user, and a circuit breaker steers, constrains, then stops looping or runaway agents. -- evidence: [README.md#L249-L252](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L249-L252), [README.md#L202-L203](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L202-L203) (`clm_d0ff5ac873f6207e95b546debce6147a2628a3f10d622477772e2d4c2f22ce7f`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Running from source requires Node.js 18+, npm, a C/C++ toolchain for node-pty's native addon, and at least one supported agent CLI on PATH; missing CLIs can self-heal via an in-terminal installer. -- evidence: [README.md#L312-L325](https://github.com/chaitanyagiri/munder-difflin/blob/417d8decf08c4e4da484a5c3c35aa6e8925e5989/README.md#L312-L325) (`clm_68821c5d4852b33fa4210e587093a776a5c9101453878e18dd635fc0b9b51fe2`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

