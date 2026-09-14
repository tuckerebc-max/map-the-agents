# yeachan-heo/oh-my-claudecode -- full detail

[Back to orientation](oh-my-claudecode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/yeachan-heo/oh-my-claudecode/5281b19e0d64f8e6dc6767f2130299a88af2dc71/1fded3a5854f6853.json](../../../wiki/dossiers/yeachan-heo/oh-my-claudecode/5281b19e0d64f8e6dc6767f2130299a88af2dc71/1fded3a5854f6853.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: CONTRIBUTING.md is the developer guide covering forking, local checkout setup, linking as the active plugin, running tests, and submitting PRs. -- evidence: [README.md#L338-L338](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L338-L338) (`clm_3cb4573ad335aabe827764be1312b3881737bf8dda63fab96975e80008b5514b`)

## skills-patterns (1 claim(s))

- [observation/documented] Custom skills are stored at `.omc/skills/` (project, higher priority) or `~/.omc/skills/` (user fallback), with frontmatter triggers, and matching skills auto-inject into context; `/skillify` extracts patterns with quality gates. -- evidence: [README.md#L352-L359](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L352-L359), [README.md#L361-L363](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L361-L363), [README.md#L344-L348](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L344-L348) (`clm_a7d0a0341cadb84f57656a38bf5d58105a8f7c34a6c58cbb7ff6a7143b50642e`)

## interfaces (3 claim(s))

- [observation/documented] OMC exposes two surfaces: terminal CLI commands (`omc ...`) run from a shell, and in-session slash skills (`/...`) run inside a Claude Code session after plugin setup. -- evidence: [README.md#L141-L142](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L141-L142) (`clm_09003e45565102f98d3168c4bb3fe7f22f9a0d48b0aee2646e48fc301ba631ef`)
- [observation/documented] The npm package installs both `oh-my-claudecode` and a short `omc` command alias, while the repo/plugin branding is oh-my-claudecode. -- evidence: [README.md#L245-L245](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L245-L245), [README.md#L255-L255](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L255-L255) (`clm_4358309eff6d658bbc338075d2a66c0963d352053e411dd02b0d54a4b8a7799e`)
- [observation/documented] The npm package exports TypeScript helpers such as `createOmcSession()` and prompt-expansion utilities built on `@anthropic-ai/claude-agent-sdk` as a library surface for Node.js programs. -- evidence: [README.md#L155-L157](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L155-L157) (`clm_f3dc0583e6eef2779645a908216986786a68db4a043bce2c6633c5ce8c23885d`)

## memory-state (2 claim(s))

- [observation/documented] OMC writes runtime state, session data, plans, logs, and artifacts under `.omc/` by default; gitignore keeps it local except `.omc/skills/**` which stays committable, and `OMC_STATE_DIR` or a `.omc-workspace` marker can relocate or share state. -- evidence: [README.md#L371-L371](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L371-L371), [README.md#L369-L369](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L369-L369), [README.md#L379-L379](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L379-L379) (`clm_0e5763ee6372f991b1537f41f90b736a539a313d970833937dd88a6370b319b8`)
- [observation/documented] Outside a git repository OMC uses a canonical state root at `~/.omc/` (or `$OMC_STATE_DIR/non-git`) and avoids creating per-cwd state roots or writing into sensitive directories like `~/.ssh` or `~/Downloads`. -- evidence: [README.md#L373-L373](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L373-L373) (`clm_ce98890160ea249edd83407136fc2437fa2835f79abf463fd2aa295817dc6488`)

## orchestration (3 claim(s))

- [observation/documented] Team is the canonical orchestration surface as of v4.1.7, running a staged pipeline: team-plan, team-prd, team-exec, team-verify, and team-fix (loop); the legacy `swarm` alias was removed. -- evidence: [README.md#L181-L181](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L181-L181), [README.md#L171-L171](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L171-L171), [README.md#L412-L414](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L412-L414) (`clm_ded61db43c3f57585ad0f728664933c5ebff742717264563189c8cfed72f52a1`)
- [observation/documented] `omc team N:<provider>` spawns on-demand tmux worker panes for claude, codex, gemini, antigravity, grok, or cursor CLIs; workers die when their task completes, and the selected CLI plus tmux must be installed and authenticated. -- evidence: [README.md#L199-L207](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L199-L207), [README.md#L216-L224](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L216-L224), [README.md#L226-L226](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L226-L226) (`clm_0f495dbf894e1c3a06937302fa937b83c64e8813de20f0cd16694b5e9aa86f95`)
- [observation/documented] Named autopilot stage profiles (v1) are selected via `/autopilot --workflow <name>`, configured under `autopilot.workflows` in project or user config, and admit only four fixed stage sequences such as [ralplan, execution, qa]. -- evidence: [README.md#L107-L107](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L107-L107), [README.md#L128-L128](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L128-L128), [README.md#L113-L113](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L113-L113) (`clm_948fe740e11c0833a4b8d13853e7743fb370f3b502fa9fdf45e31ae2cc3c83a7`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The CLI depends on better-sqlite3, whose upstream prebuild-install@7.1.3 dependency triggers a deprecation warning during npm install; the warning is tracked in issue #2913 and does not indicate install failure. -- evidence: [README.md#L76-L81](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L76-L81) (`clm_66942730338b47cba0334580b256f77caf3dc4e8f745e67075825e069cc49d99`)
- [observation/documented] Requirements include the Claude Code CLI plus a Claude Max/Pro subscription or Anthropic API key, and tmux is required for features like `omc team` and rate-limit detection. -- evidence: [README.md#L471-L471](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L471-L471), [README.md#L599-L599](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L599-L599), [README.md#L594-L595](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L594-L595) (`clm_884722d1299b559920bc9207466615de89915d8bf62a82f4f9d3f1d7cf139093`)

## limitations (2 claim(s))

- [observation/documented] Named autopilot profiles currently require Linux with `flock`; unsupported environments reject explicit `--workflow` invocation before changing autopilot state, while legacy autopilot remains available. -- evidence: [README.md#L130-L130](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L130-L130) (`clm_c4fd0e5e0c1c5147a32fc79116d88def0cc58fe9362ce92d6b69563e14ccdad3`)
- [observation/documented] OMC does not ship a VS Code extension or document extension-specific install flows; interactive slash commands like /autopilot and /team require an active Claude Code session and should not be relied on in CI. -- evidence: [README.md#L155-L157](https://github.com/Yeachan-Heo/oh-my-claudecode/blob/5281b19e0d64f8e6dc6767f2130299a88af2dc71/README.md#L155-L157) (`clm_44277a6e0b722de587bb276fb95dff6a87c08632da073940cc992a9045fd806e`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

