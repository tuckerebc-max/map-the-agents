# rcarmo/piclaw -- full detail

[Back to orientation](piclaw.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/rcarmo/piclaw/ced7c11253c31cfda51c0803dfc244332266dc9a/be372c19d583039d.json](../../../wiki/dossiers/rcarmo/piclaw/ced7c11253c31cfda51c0803dfc244332266dc9a/be372c19d583039d.json)

## specifications (1 claim(s))

- [observation/documented] PiClaw is a self-hosted, single-user-by-default AI workspace built on the Pi Coding Agent, letting users chat with an agent, edit files, and run commands in one browser window. -- evidence: [README.md#L7-L7](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L7-L7) (`clm_f0a7cc3e86fbac9884abe3a994002947b60be7eae74b1fbe05842a4576589645`)

## components (1 claim(s))

- [observation/documented] The runtime core comprises a router, a lane-aware AgentQueue, an AgentPool of Pi SDK AgentSessions, built-in and packaged extensions, and background workers for IPC, scheduling, and Dream memory consolidation. -- evidence: [docs/architecture.md#L34-L38](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L34-L38), [docs/architecture.md#L84-L89](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L84-L89), [docs/architecture.md#L21-L26](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L21-L26) (`clm_7fbcf5485c9cf90aed1ce709d3df7d04140a5f60641155f61f906461704a9d98`)

## design-choices (1 claim(s))

- [observation/documented] Configuration resolves in a documented precedence chain: CLI flags, then process.env, workspace .env, .piclaw/config.json, and built-in defaults. -- evidence: [docs/configuration.md#L35-L39](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/configuration.md#L35-L39) (`clm_68f56f2508ad223909bcc3801346fe66d933adeedd951e4d78e1c0da2c3dd6ef`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: code changes should follow docs/development.md and the repository workflow in AGENTS.md, and be submitted via pull request; issues use dedicated templates. -- evidence: [README.md#L84-L86](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L84-L86), [README.md#L88-L88](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L88-L88) (`clm_dd393718da3970cb5f37864fae731ff97ee8a53cd2c7558a8da6bb17dcd41fea`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The web UI supports English, Simplified Chinese and Japanese with desktop and mobile layouts, and model requests go to the configured provider including local OpenAI-compatible servers. -- evidence: [README.md#L7-L7](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L7-L7), [README.md#L9-L9](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L9-L9) (`clm_4804ca20917a57b36b3868d5c2b9a502d97ad5cc560ad63b87b744f6888a69d8`)
- [observation/documented] Chat commands include /login for provider setup, /model for model selection, /dream for memory consolidation, /tasks and /scheduled for scheduled tasks, and /theme and /tint for UI theming. -- evidence: [docs/architecture.md#L164-L185](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L164-L185), [README.md#L45-L48](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L45-L48) (`clm_fa3e7d1dde6d50ddf70860dd3b2b54d7d695c2c7625b99fb18ef15c53972b5b7`)

## memory-state (3 claim(s))

- [observation/documented] Durable state lives in SQLite (messages, chats, tasks, configs, token usage), session trees, and a workspace holding notes, skills and files. -- evidence: [docs/architecture.md#L84-L89](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L84-L89), [docs/architecture.md#L40-L44](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L40-L44) (`clm_5c189280901a1fd0cd1d43e4bf18c2b610a9130e95a86cfb5a497d42b1bcfb1c`)
- [observation/documented] Dream/AutoDream memory consolidation runs as out-of-band model turns on a temporary dream: channel and a dedicated dream:<chatJid> queue lane, so long consolidations do not block interactive chat. -- evidence: [docs/architecture.md#L210-L219](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L210-L219) (`clm_36f444dbdfd4e8cd2f1f0464101e4a1c22e9ba4f0d0de1d141d8f82bb7a8d0da`)
- [observation/documented] Single-user memory uses a compact notes/memory/MEMORY.md startup index (line-capped, under ~25KB) plus typed files for user, feedback, project and reference detail. -- evidence: [docs/architecture.md#L210-L219](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L210-L219) (`clm_a384c5b7be6921687456c3a518688d235c6ce453a656fb8687c0ff554dc6627a`)

## orchestration (1 claim(s))

- [observation/documented] Per-chat turns use a cursor with inflight and failed markers: transient failures recover automatically, while persistent failures roll the cursor back and hold the chat for explicit retry or skip. -- evidence: [docs/architecture.md#L336-L339](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L336-L339), [docs/architecture.md#L318-L334](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L318-L334) (`clm_5e8378a6bd2fab34103934df4eaec20290c91397d58ce5f2ff3e8d5084ef6247`)

## tools-permissions (1 claim(s))

- [observation/documented] The agent runs with its process user's permissions; native installs can access that user's files and commands, and containers expose mounted files and configured network access. -- evidence: [README.md#L68-L71](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L68-L71) (`clm_88e25c6a1efc253bfb4517b444d4cca2462dcc618a1d8c2e204abf135a6502aa`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] PiClaw is built on the Pi Coding Agent core (earendil-works/pi) and is not directly affiliated with pi.dev; Docker deployment bundles Bun and command-line tools. -- evidence: [README.md#L99-L100](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L99-L100), [README.md#L15-L20](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L15-L20), [README.md#L7-L7](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L7-L7) (`clm_6dc90be39abbbece5ef9a8f07b1f75731eeeb60cbaa514eb6a6676a0f929f720`)

## limitations (2 claim(s))

- [observation/documented] A fresh instance has no web login gate, so the Docker quick start publishes the port on localhost only until browser authentication is configured. -- evidence: [README.md#L28-L29](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L28-L29) (`clm_3826b62a98cbd3ef0e11e9d2e8676f4d5284ca58bfc630fd9a0478cf8922b74b`)
- [observation/documented] Multi-user family mode is experimental: family-shared deployments share one workspace and process without filesystem isolation, isolated-container mode is unavailable, and no family-mode release gate has passed. -- evidence: [docs/architecture.md#L103-L103](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/docs/architecture.md#L103-L103), [README.md#L68-L71](https://github.com/rcarmo/piclaw/blob/ced7c11253c31cfda51c0803dfc244332266dc9a/README.md#L68-L71) (`clm_99795eb62a4baa9dfbf7b3ce1daf70030f4001df8cce3935375bb78940928d98`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

