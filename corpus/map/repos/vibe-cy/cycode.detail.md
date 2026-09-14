# vibe-cy/cycode -- full detail

[Back to orientation](cycode.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/vibe-cy/cycode/fbdb97f7432894e1a04e1f6f883464c31ba48255/09e32013832fa0a0.json](../../../wiki/dossiers/vibe-cy/cycode/fbdb97f7432894e1a04e1f6f883464c31ba48255/09e32013832fa0a0.json)

## specifications (1 claim(s))

- [observation/documented] CyCode is described as a lightweight AI coding agent that runs in the terminal and uses an OpenAI-compatible Chat Completions API. -- evidence: [README.md#L3-L3](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L3-L3) (`clm_ba087d78cc5182e37128d4112ca3e9d9a78c4131ad03d74f3f0b906dceb5329e`)

## components (1 claim(s))

- [observation/documented] The project structure includes modules for the agent loop, CLI entry, config, context compression, LLM client, REPL, sessions, tool registry, built-in tools, and an Ink TUI. -- evidence: [README.md#L151-L168](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L151-L168) (`clm_5b86cc351bf778568327d9f5238ada442b2eeebd013801b1e20ab3ab06e57e48`)

## design-choices (2 claim(s))

- [observation/documented] edit_file relies on exact text matching; if the target fragment is not unique, the edit is rejected and more context is required. -- evidence: [README.md#L224-L227](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L224-L227) (`clm_96ed01a0a946fbf0d6bbe9bec683bdfafd2f2733d6187e24cc4c0260972dfc49`)
- [observation/documented] One-shot mode preserves plain stdout for scripting, while interactive mode prefers an Ink TUI with a text REPL fallback when TTY rendering is unavailable. -- evidence: [README.md#L9-L15](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L9-L15), [README.md#L224-L227](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L224-L227) (`clm_4361db9bd4f5eaa47d1851bfc9646acda0788923e7e3ab209dd2d253bb0b877d`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: npm scripts include build (TypeScript to dist/), start, dev, and test, where test builds then runs tests/*.test.mjs. -- evidence: [README.md#L180-L185](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L180-L185), [README.md#L172-L176](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L172-L176) (`clm_c1e145b8b844b788feb973589ebf2af464ee5af4a708c572a5b8d9416b9a493e`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI supports one-shot flags (-m/--message, -p/--prompt), session resume, working directory, model, base URL, API key, version, and help options. -- evidence: [README.md#L83-L93](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L83-L93) (`clm_70126a05722a403f570a97d24a0037b32a28525525822748b8cbce8739809be7`)
- [observation/documented] Interactive mode provides slash commands including /reset, /model, /tokens, /compact, /diff, /save, and /sessions, plus quit/exit. -- evidence: [README.md#L97-L108](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L97-L108) (`clm_af5a2d5d2b17bf8f7e8f140fbe23659e873b8f824b2275c8c115cf4fda53d494`)

## memory-state (1 claim(s))

- [observation/documented] Sessions can be saved, listed, and resumed, stored by default under ~/.cycode/sessions, with the root configurable via CYCODE_HOME. -- evidence: [README.md#L114-L129](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L114-L129), [README.md#L218-L220](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L218-L220), [README.md#L204-L204](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L204-L204), [README.md#L206-L208](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L206-L208) (`clm_b9352161465262d87738ae84743edaea0f154323349ef8e594b5ddbd91acedc2`)

## orchestration (1 claim(s))

- [observation/documented] MAX_TURNS defaults to 50, capping tool-use turns per task, and CYCODE_MAX_TOKENS defaults to 4096 output tokens per call. -- evidence: [README.md#L114-L129](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L114-L129) (`clm_00d48a2b98038cf8b1f4bfc32f9a704844dc13122c43b2dcfd38c5edea4c3e37`)

## tools-permissions (2 claim(s))

- [observation/documented] Built-in tools exposed to the model include read_file, edit_file, write_file, bash, grep, glob, and an agent tool for spawning sub-agents. -- evidence: [README.md#L137-L145](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L137-L145) (`clm_7c812efe1a91322aa3e91b93b51908ed586045d3b2fec1938efc1ff56d47a31d`)
- [observation/documented] The bash tool blocks some high-risk command patterns like forced recursive deletion and piping scripts into a shell, but the README states this is not a complete sandbox. -- evidence: [README.md#L147-L147](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L147-L147) (`clm_01a66d1324c3c56b6e8d3bd5e0998e17bffd621623a7112299c215401c484d93`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Requirements are Node.js 18 or later, npm, and an OpenAI-compatible API key. -- evidence: [README.md#L19-L21](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L19-L21) (`clm_2acc2aa40a460e7e40fbfaadb567f2b34941ee79b65a2308ae170c33994d0bbb`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

