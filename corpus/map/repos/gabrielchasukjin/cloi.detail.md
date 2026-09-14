# gabrielchasukjin/cloi -- full detail

[Back to orientation](cloi.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/gabrielchasukjin/cloi/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/797f9eefb3e6fe1a.json](../../../wiki/dossiers/gabrielchasukjin/cloi/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/797f9eefb3e6fe1a.json)

## specifications (1 claim(s))

- [observation/documented] Cloi is described as a local-first terminal coding agent that reads, searches, writes and edits files and runs commands in the workspace, with everything running locally and no API key. -- evidence: [README.md#L3-L3](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L3-L3), [README.md#L5-L7](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L5-L7) (`clm_e49387aa311048d2d0f7b76d4a60e8fcdab907387d16a7468931483193f5433f`)

## components (2 claim(s))

- [observation/documented] The architecture includes src/agent modules (loop, prompt, permission, verify, judge), tools (fs-tools, shell, todo, workspace, registry), a SQLite session store, an Ollama provider, and setup/hardware/recommendation utilities. -- evidence: [docs/internals.md#L8-L32](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L8-L32) (`clm_f3cd146bf441665f38fcf692c6376905d90341475533aa1ea1d58a53c49c7676`)
- [observation/documented] A session-long Python interpreter exposes stored results as variables and tools as callable functions; variables, imports and helpers persist across sessions, and the namespace is saved per variable between runs. -- evidence: [docs/internals.md#L356-L362](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L356-L362), [README.md#L99-L101](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L99-L101), [README.md#L90-L91](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L90-L91), [docs/internals.md#L349-L350](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L349-L350) (`clm_04405ea117b0360bc196b082552e13688623560cb5c9242ab6aeed91a1801b91`)

## design-choices (3 claim(s))

- [observation/documented] Setup reads VRAM, RAM and core count and proposes two models: a primary that must fit in VRAM and a fallback that only needs to fit in RAM, stepping down the primary if the prediction was wrong. -- evidence: [README.md#L47-L51](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L47-L51), [docs/models.md#L15-L20](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/models.md#L15-L20), [docs/models.md#L12-L13](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/models.md#L12-L13) (`clm_16c16421cb2fc7e7814a764289f41260d13dcd1f91b27b95b7fe93eecf222178`)
- [observation/documented] Answers are verified before display: filesystem-settled claims are checked without a model call (line citations, quotes, absence claims), and a model-based judge review runs only after an escalation. -- evidence: [docs/internals.md#L118-L122](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L118-L122), [README.md#L66-L69](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L66-L69), [README.md#L71-L72](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L71-L72), [docs/internals.md#L113-L116](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L113-L116) (`clm_ecf9a3f84f8f03a973cd30e513c6fe220f0580aa477d9c4fdb0870004f311931`)
- [observation/documented] Safety rails include Levenshtein tool-name repair, doom-loop detection, strike budgets, a hard iteration ceiling, and tool-output truncation at 2000 lines / 50 KB with overflow spilled to a readable temp file. -- evidence: [docs/internals.md#L55-L65](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L55-L65) (`clm_4b338359fc82b5fea5b1e263ffa51e18e4d947d9dcc61ce7deb90710b63250fe`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: tests are run with npm test; the suite covers 126 tests including tool-name repair, permission gating, credential containment, and regression tests for false positives found in live runs. -- evidence: [docs/internals.md#L472-L474](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L472-L474), [docs/internals.md#L476-L481](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L476-L481) (`clm_f428c48d7d504178ec3c6a10fac58529d2d3bcf24b672821af5a3dda9722cc00`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI supports interactive sessions, one-shot requests, --continue to resume a session, and cloi setup to re-pick models; in-session slash commands include /model, /tools, /plan, /usage, /sessions, /help. -- evidence: [README.md#L131-L136](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L131-L136), [README.md#L138-L139](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L138-L139) (`clm_c0d6581da761cf70cb22e969b11c3128ea7ede387b7a1f85c964a3f5560f8478`)
- [observation/documented] Configuration lives in ~/.cloi/config.json (overridable via CLOI_DATA_DIR) with settings for model, host, maxIterations, escalationModel, verifyAnswers, compaction, temperature, and autoApprove. -- evidence: [docs/configuration.md#L7-L7](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/configuration.md#L7-L7), [docs/configuration.md#L27-L35](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/configuration.md#L27-L35), [docs/configuration.md#L9-L12](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/configuration.md#L9-L12), [docs/configuration.md#L19-L20](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/configuration.md#L19-L20), [docs/configuration.md#L22-L25](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/configuration.md#L22-L25), [docs/configuration.md#L14-L17](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/configuration.md#L14-L17) (`clm_25bb18540847a9b8cd5d7f45499f424ff8a26e4d8690fd11a60c1c3060cd1bee`)

## memory-state (3 claim(s))

- [observation/documented] Conversation state is persisted in SQLite and rebuilt from the database on every loop iteration, so interrupted turns leave a coherent, resumable session. -- evidence: [docs/internals.md#L8-L32](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L8-L32), [docs/internals.md#L46-L49](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L46-L49) (`clm_a0cf10ba086c1db606807cc798a634e10beb11ddb0627ffcf84a46caf75fb363`)
- [observation/documented] When the prompt nears the context window, the older half of history is replaced by a summary; nothing is deleted and the on-disk transcript stays whole. -- evidence: [README.md#L114-L117](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L114-L117), [docs/internals.md#L210-L215](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L210-L215), [README.md#L119-L120](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L119-L120) (`clm_bfcba7695cf5b7d090fa5c557ab0b5529f458a5d035c4d07dd8cdcab54956be5`)
- [observation/documented] Substantial tool results are stored in full under argument-derived handles (e.g. stats_js, npm_test) and can be recalled whole, sliced, or searched; results over 256 KB are not stored. -- evidence: [README.md#L84-L86](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L84-L86), [docs/internals.md#L265-L266](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L265-L266), [README.md#L76-L77](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L76-L77), [docs/internals.md#L252-L255](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L252-L255) (`clm_1273b03afdd4bc7ec1b57ac956a9d539f1825be0b3fd199af9148e7b9bcb3cc8`)

## orchestration (1 claim(s))

- [observation/documented] Escalation to a stronger model is triggered by six observed-failure signals (e.g. repeated identical calls, consecutive tool failures, disproved claims), and the escalated model inherits the full conversation plus a handoff note. -- evidence: [docs/internals.md#L143-L145](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L143-L145), [README.md#L58-L60](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L58-L60), [docs/internals.md#L153-L160](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L153-L160) (`clm_6bfc78956d372a0a800ac32527e41f7d3c2d0c4959eefd9d44668c8a858bad8d`)

## tools-permissions (3 claim(s))

- [observation/documented] Writes, edits and shell commands ask permission first with three answers (once, always-for-this-tool, no); 'always' is scoped to the running process, and autoApprove config grants durable approval. -- evidence: [README.md#L124-L127](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L124-L127), [docs/internals.md#L396-L400](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L396-L400) (`clm_773c74c32026905dd6ff4250ec877444d5cfe980f7b85bb51d3ff48cda75e2a1`)
- [observation/documented] Subprocesses run with a sanitised environment stripping credential-shaped variables, and live secret values are redacted from tool output; the docs note this is defence in depth, not a guarantee. -- evidence: [docs/internals.md#L391-L392](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L391-L392), [README.md#L124-L127](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L124-L127), [docs/internals.md#L377-L385](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L377-L385) (`clm_7367ecce71a775df3bb55397a2e52ba8b460f05b43b584f4255c482c4e436df1`)
- [observation/documented] Tools called from the Python scratchpad still ask permission, so approving a cell does not approve everything it can reach; the python tool also runs with the sanitised environment. -- evidence: [README.md#L99-L101](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L99-L101), [docs/internals.md#L302-L305](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L302-L305), [docs/internals.md#L337-L342](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L337-L342) (`clm_5bc9a9e5d6c98c8ae885a9e7c188502d62d4fd9e794f0e26f450f25f1a8b641a`)

## evaluation (1 claim(s))

- [observation/documented] The repo includes benchmark scripts (bench/compare.js, bench/python-tool.js) that drive the real agent against real tools; a python-tool benchmark showed accuracy moving from 0/8 to 3/8 with worked examples in the tool description. -- evidence: [docs/internals.md#L318-L321](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L318-L321), [README.md#L106-L110](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L106-L110), [README.md#L149-L152](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L149-L152), [README.md#L154-L155](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L154-L155) (`clm_fa80952c07bd32bb66e0f0564131bbb99a2480d4c6c0af4c7842d03a177e4c97`)

## dependencies (1 claim(s))

- [observation/documented] Running Cloi requires Ollama, Node 22.5+, and a tool-capable model; it is installed via npm as @cloi-ai/cloi. -- evidence: [README.md#L9-L12](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L9-L12), [README.md#L14-L16](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L14-L16) (`clm_388c2c0247634f8219ee7dcacd582dedac6ea9d8f336ef1c5a1ec8394fb47127`)

## limitations (1 claim(s))

- [observation/documented] Documented gaps: only Ollama is wired up, no sub-agents, no MCP, no web access, and hard cross-file debugging scored 0/12 in the benchmark for models fitting 8 GB. -- evidence: [README.md#L159-L161](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L159-L161) (`clm_6a22bb37ede2132577d01c54ec088bd43af0c4a84f7911a2d21c169a979531ea`)

## relevance (1 claim(s))

- [observation/documented] Licensed under MIT; relevant as a reference for local-model agent loop design, escalation, verification, and small-model failure guardrails. -- evidence: [README.md#L165-L165](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/README.md#L165-L165), [docs/internals.md#L3-L4](https://github.com/gabrielchasukjin/cloi/blob/1da62db7aa3aed8b1e65f1e3fb69a89cf00707b9/docs/internals.md#L3-L4) (`clm_32e14c06adb7276e6915091da5e9bf544336b1f595d1171d68e818aca174645d`)

