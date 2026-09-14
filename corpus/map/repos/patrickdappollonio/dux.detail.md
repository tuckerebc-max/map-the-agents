# patrickdappollonio/dux -- full detail

[Back to orientation](dux.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/patrickdappollonio/dux/14e044d616d205a5ef1d030978c55337a812fa04/9cf959f4d95c8dad.json](../../../wiki/dossiers/patrickdappollonio/dux/14e044d616d205a5ef1d030978c55337a812fa04/9cf959f4d95c8dad.json)

## specifications (1 claim(s))

- [observation/documented] dux is a terminal UI that runs multiple AI coding agents side by side, each in its own git worktree, with companion terminals, macros, commit generation, and a command palette. -- evidence: [README.md#L7-L7](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L7-L7) (`clm_df90e48dec2785e69ad94e41d095d61cdc775973453854792fae20c2fd5d66ec`)

## components (2 claim(s))

- [observation/documented] The interface has three panes: projects and agent sessions on the left, the agent's live terminal output or diff in the center, and changed files, staging, and diffs on the right. -- evidence: [README.md#L81-L83](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L81-L83) (`clm_ff104f5610089b2d526b76c26b365dd298cdceffa6c8e9027d34ce441cfb190d`)
- [observation/documented] Each agent gets companion terminal shells in the same worktree, and multiple companion terminals per agent are supported. -- evidence: [README.md#L179-L179](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L179-L179) (`clm_336b6f28a274f3688e71bd905515ed23c7d92fbde45a6b450024141b4e88f535`)

## design-choices (1 claim(s))

- [observation/documented] Agents run through a PTY like a normal shell, so CLIs such as Claude, Codex, or OpenCode behave as they would in a regular terminal, including MCP servers, hooks, and permission dialogs. -- evidence: [README.md#L19-L19](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L19-L19) (`clm_f90c6ce639f60c5dd3541de2e4ee89d90a6a0a0ee12c1c17ab004db824b8c024`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors verify changes with cargo fmt, cargo clippy --all-targets --all-features -- -D warnings (a CI gate on every PR), and cargo test, and every change should include unit tests. -- evidence: [CLAUDE.md#L155-L155](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/CLAUDE.md#L155-L155), [CLAUDE.md#L48-L49](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/CLAUDE.md#L48-L49), [CLAUDE.md#L149-L153](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/CLAUDE.md#L149-L153) (`clm_19c20ba1c908846385fa0b12122781533e156a23300f497c9bb8a046300a45bf`)
- [observation/documented] Repository development practice: the src/app/ TUI is split into focused submodules (mod.rs, input.rs, render.rs, sessions.rs, workers.rs), and changes should stay scoped to the relevant submodule. -- evidence: [CLAUDE.md#L78-L78](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/CLAUDE.md#L78-L78), [CLAUDE.md#L80-L84](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/CLAUDE.md#L80-L84), [CLAUDE.md#L86-L86](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/CLAUDE.md#L86-L86), [CLAUDE.md#L136-L143](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/CLAUDE.md#L136-L143) (`clm_566f79842b0096c0e360c3a6e5a49fc17ac9911db93c1d27b585f4916483cb45`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] Any terminal command can be a provider via a TOML config entry with command, args, and optional resume_args; built-in defaults include Claude, Codex, and OpenCode, and adding a provider is config-only. -- evidence: [README.md#L91-L96](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L91-L96), [README.md#L89-L89](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L89-L89) (`clm_a22d9d059994befb9bce672d8aab79cd9c3d58b8102df4511c9842432f8d5b94`)
- [observation/documented] Palette commands include change-agent-provider, change-default-provider, and change-project-default-provider for switching providers per worktree, globally, or per project, with resume_args reused when available. -- evidence: [README.md#L102-L102](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L102-L102), [README.md#L104-L106](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L104-L106) (`clm_8903dc642be7c1c55d384f35fbb379ec12ab08b4c5a489043a6c6d57eac34944`)
- [observation/documented] Projects support a startup command run in the new worktree before the provider launches, with env expansion, DUX_* environment variables, and log/rerun palette commands; failure does not block agent creation. -- evidence: [README.md#L152-L152](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L152-L152), [README.md#L114-L114](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L114-L114), [README.md#L154-L154](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L154-L154) (`clm_47c97e0b1ae495ff5fae8d6fddbe51100710e2bb64f6f148d2c16c25253a876b`)
- [observation/documented] The right pane provides git staging: stage/unstage files, view syntax-highlighted diffs, write commit messages, push, and pull; AI commit-message drafting uses the provider in oneshot mode with a customizable prompt. -- evidence: [README.md#L173-L173](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L173-L173), [README.md#L171-L171](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L171-L171) (`clm_6af25d1b0d573d5832195e4efa762443efcd4a1ab5def7154d4b4ce7cb011643`)
- [observation/documented] Themes use the Opaline TOML format; custom themes live next to the config file, resolution prefers user themes then bundled dux_dark then built-in Opaline themes, falling back to dux_dark with a logged warning. -- evidence: [README.md#L224-L224](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L224-L224), [README.md#L210-L213](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L210-L213), [README.md#L222-L222](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L222-L222) (`clm_b4f5c8f8286acf5097cd8a57f0be616fb4772c5b20bdd7f7fcac386485332d4b`)

## memory-state (1 claim(s))

- [observation/documented] Session state persists in sessions.sqlite3 alongside the config, and logs go to dux.log in the config directory with a configurable level and path. -- evidence: [CLAUDE.md#L57-L63](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/CLAUDE.md#L57-L63), [README.md#L283-L283](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L283-L283), [README.md#L285-L289](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L285-L289) (`clm_7375a5afe5e3c460771b3fd74b0e571b033b13bcffc2a523fb5097cd4ac5d9db`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] git is required on PATH; the gh CLI is optional and enables PR status tracking shown as status pills in the interface. -- evidence: [README.md#L70-L71](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L70-L71), [README.md#L175-L175](https://github.com/patrickdappollonio/dux/blob/14e044d616d205a5ef1d030978c55337a812fa04/README.md#L175-L175) (`clm_fa614dff30db6eb0c77c1e534ebd5c1ff3e47f09dfcf21dccfbcbe2f8f1fd41e`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

