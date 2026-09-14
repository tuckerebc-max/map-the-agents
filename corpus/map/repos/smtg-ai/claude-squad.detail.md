# smtg-ai/claude-squad -- full detail

[Back to orientation](claude-squad.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/smtg-ai/claude-squad/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/930f92076f14d5f0.json](../../../wiki/dossiers/smtg-ai/claude-squad/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/930f92076f14d5f0.json)

## specifications (1 claim(s))

- [observation/documented] Claude Squad is a terminal application that manages multiple local AI coding agents such as Claude Code, Codex, Gemini, and Aider in separate workspaces for parallel tasks. -- evidence: [README.md#L3-L3](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L3-L3) (`clm_711115868d893aa61ac071c5bf63b3a281fd1da0050acbcd8dd73c87aab2c3df`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (3 claim(s))

- [observation/documented] The app uses tmux for isolated per-agent terminal sessions and git worktrees so each session works on its own branch, with a TUI for navigation. -- evidence: [README.md#L152-L154](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L152-L154) (`clm_87fa88b518a1a8d3f6b426cf0bb27a06902e993999f3aee5cbd238108a4f72e1`)
- [observation/documented] Profiles allow named program configurations selectable at session creation; a `profiles` array with name/program fields and `default_program` is set in the config file. -- evidence: [README.md#L119-L119](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L119-L119), [README.md#L136-L139](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L136-L139), [README.md#L123-L132](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L123-L132), [README.md#L121-L121](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L121-L121) (`clm_a05a6ed103a32d9e76cb1cc9d13c11420b416513972d622c55262b5bbc62428c`)
- [observation/documented] When no profiles are defined, the app uses `default_program` directly as the launch command, defaulting to `claude`. -- evidence: [README.md#L74-L77](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L74-L77), [README.md#L141-L141](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L141-L141) (`clm_5c82fe4ca46b5ab66e1f81c45f62240767ab8507bb10bfa4c82aea8e29f36f76`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors fork and clone the repo, add upstream, run `go mod download`, lint with `gofmt -w .`, and should include tests for new features or fixes. -- evidence: [CONTRIBUTING.md#L18-L20](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/CONTRIBUTING.md#L18-L20), [CONTRIBUTING.md#L24-L24](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/CONTRIBUTING.md#L24-L24), [CONTRIBUTING.md#L7-L10](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/CONTRIBUTING.md#L7-L10) (`clm_352ccb9ba0b662ed239955b7c0a63b6973eb7575ffcfd10321b2d471ec37c622`)
- [observation/documented] Repository development practice: contributors accept a CLA via the CLA assistant bot on their first pull request, granting copyright, patent, and relicensing rights to maintainers. -- evidence: [CLA.md#L43-L43](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/CLA.md#L43-L43), [CLA.md#L19-L19](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/CLA.md#L19-L19), [CLA.md#L35-L35](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/CLA.md#L35-L35), [CLA.md#L17-L17](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/CLA.md#L17-L17) (`clm_3e42b0a0f69ea04047b0f745732a5d4b22c772ca9fb0c97ee06a247e403191bd`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI is invoked as `cs` with subcommands including completion, debug, help, reset, and version, plus flags like --autoyes and --program. -- evidence: [README.md#L22-L22](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L22-L22), [README.md#L54-L57](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L54-L57), [README.md#L59-L64](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L59-L64), [README.md#L66-L70](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L66-L70) (`clm_092df2b58322bc5b0db1807afeea6943b7cfdcb411ddb0f68adab51406f7b4b7`)
- [observation/documented] Keybindings support session creation (`n`, `N`), deletion (`D`), attach/detach (`↵/o`, ctrl-q), commit-push (`s`), checkout (`c`), resume (`r`), and diff-view navigation. -- evidence: [README.md#L109-L111](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L109-L111), [README.md#L101-L106](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L101-L106), [README.md#L95-L98](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L95-L98) (`clm_ec68ea97733d3e9f6bf9e6118d1fcc6e9c3f74de0dc4656a8e5937bea7e7874c`)
- [observation/documented] The `-p/--program` flag lets users launch a chosen agent command in new instances, e.g. `cs -p "codex"` or an aider command with a specific model. -- evidence: [README.md#L81-L87](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L81-L87), [README.md#L66-L70](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L66-L70) (`clm_a7a576cc5d4dbd0b750ed866770788ffc74a0c575e71acfdd3dbdfa63dc8a725`)

## memory-state (1 claim(s))

- [observation/documented] Configuration is stored in `~/.claude-squad/config.json`, and the exact path can be found via `cs debug`. -- evidence: [README.md#L115-L115](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L115-L115) (`clm_8ce9e1559ffd1d59cfae0f909159c1c503f6688c82e50994060f220ae5a4f55f`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] An experimental `-y/--autoyes` flag makes all instances automatically accept prompts for Claude Code and Aider; the README also mentions background yolo/auto-accept mode. -- evidence: [README.md#L9-L12](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L9-L12), [README.md#L66-L70](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L66-L70) (`clm_b7dad2ea275be19f97b0732252b4ea4997f0fcf395afcb4b914787055811e1c1`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The product requires tmux and the GitHub CLI (gh) as prerequisites. -- evidence: [README.md#L49-L50](https://github.com/smtg-ai/claude-squad/blob/ce1ffb4392b01f38e2c4599c7c84d2a93973b138/README.md#L49-L50) (`clm_4fc6e84aa2b46ee403a7ecbf24736f6bfca79214ba07886e912ea130eaca3f2a`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

