# amix/dunk -- full detail

[Back to orientation](dunk.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/amix/dunk/c824593566882378255d0017c4c6bff79d547027/39f303c315706246.json](../../../wiki/dossiers/amix/dunk/c824593566882378255d0017c4c6bff79d547027/39f303c315706246.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] dunk exports a DunkDiffView component from dunkdiff/opentui so the diff renderer can be embedded in other OpenTUI applications. -- evidence: [README.md#L179-L179](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L179-L179) (`clm_16e079f5acfe6bb64bd02f41e52fe79b9d0113d22d02742b48fd679678db01b4`)

## design-choices (3 claim(s))

- [observation/documented] Comments are hunk-scoped rather than line-scoped: the user picks a hunk with J/K and presses 'a' to comment, and drifted comments surface at the top of the diff (clearable with d/D) instead of getting lost. -- evidence: [README.md#L95-L95](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L95-L95), [README.md#L109-L109](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L109-L109), [README.md#L9-L14](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L9-L14), [README.md#L93-L93](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L93-L93) (`clm_b8399ffe6af39d20a9818d54b9ff307f3fed6597de2ab583009ff85382ce9a56`)
- [observation/documented] dunk is a hard fork of hunk that keeps the OpenTUI/Pierre diff-viewer foundation while removing the daemon, MCP, and session-broker layers; agent integration flows through the on-disk comments file. -- evidence: [README.md#L7-L7](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L7-L7), [CHANGELOG.md#L85-L88](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/CHANGELOG.md#L85-L88) (`clm_8664445b26972b0ec469f10cc5ae017773e322c5504d1f6f10ebd61952619f15`)
- [observation/documented] Branch-review base resolution follows an explicit order: the --branch=<ref> flag, then [branch_review] base in .dunk/config.toml, then origin/HEAD, then main/master/trunk fallbacks, with the resolved base shown in the status bar. -- evidence: [README.md#L148-L148](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L148-L148), [CHANGELOG.md#L45-L45](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/CHANGELOG.md#L45-L45) (`clm_41b168109285f4ce36c520ef4a2f804bc6990ae5b9ce98dbe9ebf79a685b5a07`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors use Bun commands (bun install, bun test, bun run typecheck/lint/format/test:integration/test:tty-smoke), colocate unit tests with source, keep tests in test/cli, test/pty, and test/smoke, follow Conventional Commits, and maintain CHANGELOG.md as the release-notes source of truth. -- evidence: [AGENTS.md#L106-L117](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/AGENTS.md#L106-L117), [AGENTS.md#L70-L76](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/AGENTS.md#L70-L76), [AGENTS.md#L158-L158](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/AGENTS.md#L158-L158), [AGENTS.md#L139-L149](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/AGENTS.md#L139-L149), [AGENTS.md#L127-L130](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/AGENTS.md#L127-L130) (`clm_631fd3355e18989d5de54925b12b32c57df75ab32b7e7c9412722830f1a008f0`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The agent-facing comments CLI supports listing pending comments, showing one with 10 lines of post-image context (configurable via --context), and an atomic resolve that refuses partial success; --json returns a stable shape with drift state. -- evidence: [CHANGELOG.md#L65-L71](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/CHANGELOG.md#L65-L71) (`clm_2afbe2b1533dd434c447dca90c4445759bd3d25cf06e02820392bbdf6c6b4d34`)
- [observation/documented] Configuration is read from ~/.config/dunk/config.toml or .dunk/config.toml, with keys for theme, layout mode, watch, exclude_untracked, line_numbers, wrap_lines, and selection_auto_copy; a CLI --watch flag overrides the config watch value. -- evidence: [README.md#L175-L175](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L175-L175), [README.md#L160-L161](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L160-L161), [README.md#L165-L173](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L165-L173) (`clm_a4e2bd97a5beb2a2c38461cf865b1eaa531deb9d7787c6c34e20fc84ee47bdde`)

## memory-state (1 claim(s))

- [observation/documented] Review comments are stored in .dunk/comments.json with the file path, hunk anchor line, body, and a context hash so comments survive small nearby edits; the file is meant to stay local and gitignored, and is deleted once the last comment is resolved. -- evidence: [README.md#L95-L95](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L95-L95), [CHANGELOG.md#L15-L15](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/CHANGELOG.md#L15-L15), [README.md#L97-L97](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L97-L97) (`clm_9f3064bee04729bf4c796e1e78a648cce9ce2c3deebf958eee41190820959691`)

## orchestration (1 claim(s))

- [observation/documented] The intended workflow pairs a human reviewer running dunk diff --watch with a coding agent in another terminal: the agent reads comments, fixes code, resolves entries, and the watched diff reloads in place as code and comments change. -- evidence: [README.md#L5-L5](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L5-L5), [README.md#L79-L79](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L79-L79), [README.md#L105-L105](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L105-L105), [README.md#L101-L101](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L101-L101) (`clm_2c095273fbfb88b4109d2437695fdc23559f7163bd0008987f4a9c09ac43c2f3`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The product builds on the OpenTUI and Pierre (@pierre/diffs) diff-viewer foundation, requires Node.js 18+ and Git, and ships via npm (dunkdiff) with prebuilt macOS and Linux binaries. -- evidence: [README.md#L20-L22](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L20-L22), [README.md#L24-L24](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L24-L24), [README.md#L7-L7](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L7-L7), [README.md#L18-L18](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/README.md#L18-L18) (`clm_c9081a390d5a93146fc361fe53be3cf4fe312949944ae4d430eed9c8c740fe9d`)

## limitations (1 claim(s))

- [observation/documented] Ctrl-Z suspension of dunk is a no-op on Windows, per the changelog; Jujutsu (jj) support was also removed, so dunk now targets Git only. -- evidence: [CHANGELOG.md#L34-L34](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/CHANGELOG.md#L34-L34), [CHANGELOG.md#L27-L30](https://github.com/amix/dunk/blob/c824593566882378255d0017c4c6bff79d547027/CHANGELOG.md#L27-L30) (`clm_fa9ff5d7bd3ed30d8dbd53b6d86946ea6df2bce15ee4324886370c036ac65cf2`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

