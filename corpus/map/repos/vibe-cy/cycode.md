# vibe-cy/cycode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fbdb97f74328 @ 09e32013832fa0a0

## Summary (orientation draft, not independently verified)

CyCode is a terminal-based AI coding agent using OpenAI-compatible Chat Completions APIs, with built-in local tools, session management, context compression, and a documented CLI/programmatic interface. Evidence is limited to the README of one commit.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] CyCode is described as a lightweight AI coding agent that runs in the terminal and uses an OpenAI-compatible Chat Completions API. -- evidence: [README.md#L3-L3](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L3-L3)
- components (1 claim(s)):
  - [observation/documented] The project structure includes modules for the agent loop, CLI entry, config, context compression, LLM client, REPL, sessions, tool registry, built-in tools, and an Ink TUI. -- evidence: [README.md#L151-L168](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L151-L168)
- design-choices (2 claim(s)):
  - [observation/documented] edit_file relies on exact text matching; if the target fragment is not unique, the edit is rejected and more context is required. -- evidence: [README.md#L224-L227](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L224-L227)
  - [observation/documented] One-shot mode preserves plain stdout for scripting, while interactive mode prefers an Ink TUI with a text REPL fallback when TTY rendering is unavailable. -- evidence: [README.md#L9-L15](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L9-L15), [README.md#L224-L227](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L224-L227)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: npm scripts include build (TypeScript to dist/), start, dev, and test, where test builds then runs tests/*.test.mjs. -- evidence: [README.md#L180-L185](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L180-L185), [README.md#L172-L176](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L172-L176)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI supports one-shot flags (-m/--message, -p/--prompt), session resume, working directory, model, base URL, API key, version, and help options. -- evidence: [README.md#L83-L93](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L83-L93)
  - [observation/documented] Interactive mode provides slash commands including /reset, /model, /tokens, /compact, /diff, /save, and /sessions, plus quit/exit. -- evidence: [README.md#L97-L108](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L97-L108)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions can be saved, listed, and resumed, stored by default under ~/.cycode/sessions, with the root configurable via CYCODE_HOME. -- evidence: [README.md#L114-L129](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L114-L129), [README.md#L218-L220](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L218-L220), [README.md#L204-L204](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L204-L204), [README.md#L206-L208](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L206-L208)
- orchestration (1 claim(s)):
  - [observation/documented] MAX_TURNS defaults to 50, capping tool-use turns per task, and CYCODE_MAX_TOKENS defaults to 4096 output tokens per call. -- evidence: [README.md#L114-L129](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L114-L129)
- tools-permissions (2 claim(s)):
  - [observation/documented] Built-in tools exposed to the model include read_file, edit_file, write_file, bash, grep, glob, and an agent tool for spawning sub-agents. -- evidence: [README.md#L137-L145](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L137-L145)
  - [observation/documented] The bash tool blocks some high-risk command patterns like forced recursive deletion and piping scripts into a shell, but the README states this is not a complete sandbox. -- evidence: [README.md#L147-L147](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L147-L147)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Requirements are Node.js 18 or later, npm, and an OpenAI-compatible API key. -- evidence: [README.md#L19-L21](https://github.com/vibe-cy/CyCode/blob/fbdb97f7432894e1a04e1f6f883464c31ba48255/README.md#L19-L21)
More evidence: [full detail](cycode.detail.md)

Metadata and full claim list: [full detail](cycode.detail.md)
Human notes ([notes](cycode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
