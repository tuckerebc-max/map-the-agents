# dazuiba/handoff -- full detail

[Back to orientation](handoff.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/dazuiba/handoff/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/7e70da208eba64cc.json](../../../wiki/dossiers/dazuiba/handoff/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/7e70da208eba64cc.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] Backends are configured in ~/.handoff/config.yaml; any Anthropic-compatible endpoint can be added, env keys are exported before the CLI launches, {model} substitutes the resolved model, and ${ENV_VAR} expands from the shell. -- evidence: [README.md#L187-L187](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L187-L187), [README.md#L200-L200](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L200-L200), [README.md#L189-L198](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L189-L198) (`clm_43c26cca1e3c4426e52dcaec0d27b6133dceac93bdef69fd2c0fa57c0e3713a2`)
- [observation/documented] The opus and codex backends reuse existing Claude Code / Codex logins with zero configuration; only DeepSeek requires a token. -- evidence: [README.md#L54-L54](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L54-L54) (`clm_adad25f7d3f8016dce392f75c19c42a563af7837d5c8b8b226f52c9f905275ea`)
- [observation/documented] The changelog states the Codex backend by default bypasses approval and sandbox so background tasks are not interrupted by interactive confirmations. -- evidence: [CHANGELOG.md#L25-L45](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/CHANGELOG.md#L25-L45) (`clm_1059fa884d894e3e2e2e91ae4c240920249a13bfe8aaca170613f0fe9e2a7a7e`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: releases are made by bumping the version in pyproject.toml, committing, tagging vX.Y.Z, and pushing; a v* tag triggers a workflow that builds with uv build and publishes to PyPI. -- evidence: [CLAUDE.md#L48-L48](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/CLAUDE.md#L48-L48), [CLAUDE.md#L43-L46](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/CLAUDE.md#L43-L46) (`clm_b2172dee153cf5264e5a3d605f07cb9cf2220701514c1611f774b563ae6a37e8`)
- [observation/documented] Repository development practice: CLAUDE.md provides guidance to Claude Code when working with code in this repository, including a file map of the cli/ package and release steps. -- evidence: [CLAUDE.md#L3-L3](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/CLAUDE.md#L3-L3), [CLAUDE.md#L43-L46](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/CLAUDE.md#L43-L46), [CLAUDE.md#L11-L39](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/CLAUDE.md#L11-L39) (`clm_8047ed3e8fc4752d42b18ec7d0cf6aeccda90403ba3a1a219ed7d520e1ccb6fe`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The CLI exposes run, resume, list/ls, tail, env, init, and new commands; list and tail provide interactive TUI views of task history and live output streams. -- evidence: [README.md#L124-L124](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L124-L124), [README.md#L113-L113](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L113-L113), [README.md#L219-L221](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L219-L221), [CLAUDE.md#L11-L39](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/CLAUDE.md#L11-L39), [README.md#L119-L119](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L119-L119) (`clm_284ee53b233a5bd7c32a72700fcc6a4d9e4965a94b412fb5beefda8e0a3637ef`)
- [observation/documented] Dispatched tasks return exactly one line, RESULT=<path-to-result-file>, to the calling session; that path serves as a stable handle so every follow-up resumes the same session. -- evidence: [README.md#L209-L213](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L209-L213) (`clm_83351cb1f7e6ebd6b9f398b4f165d5ed26c95cda1002d5da80d809a817591f92`)
- [observation/documented] In Claude Code the tool is invoked via slash skills like /handoff-ds and /handoff-codex; Codex has no slash commands, so users mention custom agents such as handoff-ds by name. -- evidence: [README.md#L100-L100](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L100-L100), [README.md#L92-L98](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L92-L98) (`clm_1249423a4b3c6a3aff241e09241e3ab21a6ee5aecb1d244c7bc4e1e1153181ac`)
- [observation/documented] Per the changelog, handoff open and handoff resume accept --backend, --session-id, and --cwd to attach native sessions not recorded in handoff.db. -- evidence: [CHANGELOG.md#L25-L45](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/CHANGELOG.md#L25-L45) (`clm_18fa3f7a93c7d69ee7804da0d618408321b05c532915da8447d844f161c07490`)

## memory-state (1 claim(s))

- [observation/documented] State persists under ~/.handoff, including config.yaml, a SQLite runs database (handoff.db), and tui_state.json storing the user's TUI theme choice. -- evidence: [CLAUDE.md#L11-L39](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/CLAUDE.md#L11-L39), [README.md#L56-L56](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L56-L56), [README.md#L151-L151](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L151-L151) (`clm_28df0c67b0b8449675e230afee62f7d2a96ad031d0fa61fab0eaa418df445c98`)

## orchestration (1 claim(s))

- [observation/documented] Tasks run in the background so the main session never blocks; handoff launches the backend CLI (claude -p or codex exec) in an isolated context and streams output to disk, and several tasks can be dispatched in one message. -- evidence: [README.md#L209-L213](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L209-L213), [README.md#L160-L160](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L160-L160) (`clm_eedc583ae6b2c59659f750aeb4a97ea03aa145a3f39ab6f7aaee20908af2dbfe`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The tool is distributed as handoff-cli, installable via uv tool install, pipx, or pip, and requires Claude Code or Codex to be installed and logged in. -- evidence: [README.md#L46-L50](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L46-L50), [README.md#L42-L42](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L42-L42), [README.md#L172-L172](https://github.com/dazuiba/handoff/blob/717ac79e1885dca50cc7387c0e3cd4dc12e1233a/README.md#L172-L172) (`clm_05e5caed0636562102fb164961c9d12697681a7d9cfb974ff3f4f9e9a7bf8d48`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

