# h0x91b/dev-3.0 -- full detail

[Back to orientation](dev-3.0.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/h0x91b/dev-3.0/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/8a06927f2fafd0f5.json](../../../wiki/dossiers/h0x91b/dev-3.0/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/8a06927f2fafd0f5.json)

## specifications (1 claim(s))

- [observation/documented] dev-3.0 is described as a Kanban board where each card is a live AI coding agent, with each task getting its own git worktree, terminal, and agent so many tasks run concurrently without file conflicts. -- evidence: [README.md#L33-L35](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L33-L35), [README.md#L7-L11](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L7-L11) (`clm_d9d4bc56738749f5c02ee91a30f0759164bf29fb6de10db9b323c24e7ec3cbc0`)

## components (1 claim(s))

- [observation/documented] Per-task sandboxes include a fresh git worktree off the base branch, a tmux session inside it, a per-project setup script, and optionally reserved free ports for the task's dev server. -- evidence: [README.md#L56-L59](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L56-L59) (`clm_e2e56770adc3e5ca02a7bf49017d47b68f53d00443216d63067b4c7c8aa6f38c`)

## design-choices (1 claim(s))

- [observation/documented] Heavy directories like node_modules or .venv are copy-on-write cloned into task sandboxes, so sandboxes cost near-zero disk and appear instantly. -- evidence: [README.md#L56-L59](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L56-L59) (`clm_407f8a210c0d22558fdc78b7995515c043fc0065574672423902eff7e119f894`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors must run bun run lint and bun run test:full before opening a PR, rebase on main first (PRs are squash-merged), add a dated changelog entry under change-logs/YYYY/MM/DD, and write decision records for non-obvious choices. -- evidence: [CONTRIBUTING.md#L21-L30](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/CONTRIBUTING.md#L21-L30) (`clm_83f8e5152dab12eadf39a695ad8ee30adde0f7861fff5935d90500dfa4a20e17`)
- [observation/documented] Repository development practice: setup requires Bun, git, and tmux 3.6 or newer, with bun run dev as the local dev loop and bun run test as a fast subset excluding slow e2e suites that CI runs. -- evidence: [CONTRIBUTING.md#L9-L15](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/CONTRIBUTING.md#L9-L15), [CONTRIBUTING.md#L7-L7](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/CONTRIBUTING.md#L7-L7) (`clm_033f31174edcaea335254aea90cf775fe0ee269fad8e7e27612ae88c34c30ca4`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The dev3 CLI lets agents communicate with the board: setting task overviews, leaving notes, raising attention badges, showing images or HTML artifacts, starting peer tasks, and read-only peeking at other tasks' terminals. -- evidence: [README.md#L191-L197](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L191-L197), [README.md#L201-L203](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L201-L203), [README.md#L186-L189](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L186-L189) (`clm_e3021b11835e76709db59e70fd9d12877f61b719f74342decc73192e5d3d93b3`)
- [observation/documented] A built-in review panel shows the branch diff with syntax highlighting, per-file read state, and inline comments on line ranges; the review can be copied back into the agent's terminal as a prompt. -- evidence: [README.md#L92-L94](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L92-L94) (`clm_1a75e600a8d174b01e8417d29beed2efb89abedebe93efb8439bcdf7f527790a`)
- [observation/documented] The app supports remote access via 'dev3 remote', serving the full UI to browsers over a Cloudflare tunnel, LAN, or SSH forward, with a QR code that keeps a phone connected for 8 hours. -- evidence: [README.md#L168-L170](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L168-L170), [README.md#L164-L166](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L164-L166) (`clm_8c64c03e98d5b5183fa224728e91ee6bf6bd02bd86728fb96649305d103da5c8`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The product can launch read-only 'bug hunter' agents that comb a branch diff in parallel and report only provable findings, indicating a read-only agent mode. -- evidence: [README.md#L109-L111](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L109-L111) (`clm_db011e3800e8c5a9c575578b7779a5fd37c86c26b947da69397f9c9a865232e5`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The app is built on Electrobun (native webview, no Chromium) and Bun, with React 19 and Tailwind on the front end, ghostty-web for GPU-accelerated terminals, and tmux underneath. -- evidence: [README.md#L410-L412](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L410-L412) (`clm_757103e44fff75f031ae78ceb942626a8112e2fa0a7f992eebcd2c954cefe9a7`)
- [observation/documented] Supported agents include Claude Code, Codex, Gemini CLI, Cursor Agent, opencode, and any CLI tool the user configures; Claude Code and Codex report status via hooks while others use the installed dev3 skill. -- evidence: [README.md#L319-L323](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L319-L323), [README.md#L325-L328](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L325-L328) (`clm_dcdd6f98434b9798fcafeaa482e41c7d3b87adb3e4eaa28cb42d900937244a7a`)

## limitations (1 claim(s))

- [observation/documented] Windows support is described as brand new and possibly rough, and the Windows build is unsigned, so first launch requires clicking past a SmartScreen warning. -- evidence: [README.md#L319-L323](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L319-L323), [README.md#L304-L309](https://github.com/h0x91b/dev-3.0/blob/e781c4265b7dbf2203fe0c2a3a5ae4dce6a88bef/README.md#L304-L309) (`clm_2b49520b96d09c3fe167983b7424a0043603d7e82756bb84ada6553a2d41dade`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

