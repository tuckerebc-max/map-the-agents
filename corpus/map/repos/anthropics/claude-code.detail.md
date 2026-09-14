# anthropics/claude-code -- full detail

[Back to orientation](claude-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/anthropics/claude-code/b5932767f3acbd07da25367064827e5cb81f43de/1c81b4db7b0df1f2.json](../../../wiki/dossiers/anthropics/claude-code/b5932767f3acbd07da25367064827e5cb81f43de/1c81b4db7b0df1f2.json)

## specifications (1 claim(s))

- [observation/documented] Claude Code is described as an agentic coding tool that runs in the terminal, understands the codebase, executes routine tasks, explains code, and handles git workflows via natural language commands. -- evidence: [README.md#L7-L7](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L7-L7) (`clm_b7a63ab175c58093635fdb7b8e86b4f938bd8c061713497cf2dec5ce4788b160`)

## components (1 claim(s))

- [observation/documented] The repository includes Claude Code plugins that extend functionality with custom commands and agents, documented in a plugins directory. -- evidence: [README.md#L50-L50](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L50-L50) (`clm_0924ad49db39570d530ed487cad3586c095be3646022e3d7b76cb4b91bf29007`)

## design-choices (1 claim(s))

- [observation/documented] The README states feedback collection includes usage data such as code acceptance or rejections, conversation data, and /bug submissions, with safeguards like limited retention and no use of feedback for model training. -- evidence: [README.md#L70-L70](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L70-L70), [README.md#L62-L62](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L62-L62) (`clm_db663f37d57a56f09ca9a98aca9843d7af3b1a3efc55bada68b730e1fd0471a4`)

## workflows (3 claim(s))

- [observation/documented] Recommended installation is via a curl install script on macOS/Linux and a PowerShell script on Windows; Homebrew and WinGet are also offered, while npm installation is deprecated. -- evidence: [README.md#L41-L44](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L41-L44), [README.md#L26-L29](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L26-L29), [README.md#L21-L24](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L21-L24), [README.md#L36-L39](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L36-L39), [README.md#L31-L34](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L31-L34), [README.md#L14-L15](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L14-L15) (`clm_289496b4929f75d631d1857d5a8faa1bb796480c897eaf904aa31a4326d55bb0`)
- [observation/documented] After installing, users navigate to their project directory and run the `claude` command to start. -- evidence: [README.md#L46-L46](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L46-L46) (`clm_afd09e89874a80ff8c59cd03a44b39356c1a24f793ce29f83de7a5e8261cb38d`)
- [observation/documented] Security vulnerabilities are to be reported through Anthropic's HackerOne bug bounty program rather than public channels. -- evidence: [SECURITY.md#L8-L8](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/SECURITY.md#L8-L8), [SECURITY.md#L12-L12](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/SECURITY.md#L12-L12) (`clm_d8143fff5f1b166fc16181a268196f67d3aad10832d1e6e35cf50c30cbabe026`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The tool can be used in a terminal, in an IDE, or by tagging @claude on GitHub, per the README. -- evidence: [README.md#L7-L7](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L7-L7) (`clm_c17e1083455ef35b0d88248f355d5b0d7cf46951d7b355146c09ea1b830ad673`)
- [observation/documented] A `/bug` command exists inside Claude Code for reporting issues directly, and GitHub issues are an alternative feedback channel. -- evidence: [README.md#L54-L54](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L54-L54) (`clm_128a56451a5937fd7b9d42924185330da225df6169438ac72fbc78f9acd797b5`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] A Node.js 18+ badge appears in the README, and the npm package is @anthropic-ai/claude-code. -- evidence: [README.md#L3-L3](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L3-L3), [README.md#L5-L5](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L5-L5) (`clm_c5e6df0a33c047e10dd5ec0f7834df8bd6082e082e83576dfd6fa06e050b46f2`)
- [observation/documented] The license file states use is subject to Anthropic's Commercial Terms of Service, © Anthropic PBC. -- evidence: [LICENSE.md#L1-L1](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/LICENSE.md#L1-L1) (`clm_9dd81f5ba8a32c738c01b920c82ded67be725f2d8d8f300db71b5bab9bc4656b`)

## limitations (1 claim(s))

- [observation/documented] npm-based installation is explicitly marked deprecated in favor of other recommended methods. -- evidence: [README.md#L41-L44](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L41-L44), [README.md#L14-L15](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L14-L15) (`clm_7106b8908e7930f6129779c2c4be9098452a9ade5c8d6b8206bd6c532ecb905c`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

