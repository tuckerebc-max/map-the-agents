# cosai-oasis/project-codeguard -- full detail

[Back to orientation](project-codeguard.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/cosai-oasis/project-codeguard/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/343681b93c681609.json](../../../wiki/dossiers/cosai-oasis/project-codeguard/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/343681b93c681609.json)

## specifications (4 claim(s))

- [observation/documented] CodeGuard ships 23 security rule files: 3 always-apply rules (hardcoded credentials, crypto algorithms, digital certificates) and 20 context-specific rules selected by language, framework, or feature. -- evidence: [docs/claude-code-skill-plugin.md#L45-L45](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L45-L45), [docs/claude-code-skill-plugin.md#L84-L85](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L84-L85), [docs/claude-code-skill-plugin.md#L166-L166](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L166-L166), [docs/claude-code-skill-plugin.md#L79-L82](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L79-L82) (`clm_30c717e7b61016c2b6eaa07eb77151d38f5bfe984572972ab9a7a96873ac2987`)
- [observation/documented] Rules are authored in a unified markdown format under sources/ and converted into formats for popular coding agents, with release automation packaging them into downloadable ZIP files. -- evidence: [docs/claude-code-skill-plugin.md#L310-L313](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L310-L313), [README.md#L67-L71](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/README.md#L67-L71) (`clm_4cd559c4d37f7b31d55bc60a124f4be607ba8d2d61d3660365123c91cf0b72ff`)
- [observation/documented] Security coverage spans cryptography (including post-quantum), input validation, authentication, authorization, supply chain, cloud, platform, and data protection domains. -- evidence: [README.md#L40-L47](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/README.md#L40-L47) (`clm_75764dceece35120dbf9c508f04fa6134fa903b83569597367b3b36ecd785ca7`)
- [observation/documented] Project CodeGuard is described as an AI model-agnostic security coding agent skills framework embedding secure-by-default practices into AI coding workflows, part of the CoSAI coalition's work as an OASIS Open Project. -- evidence: [README.md#L6-L6](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/README.md#L6-L6), [README.md#L12-L12](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/README.md#L12-L12) (`clm_fc705a39fb7accdf4412b6178f7df9972644e53ab59822bb342c00fa8d0b46e6`)

## components (3 claim(s))

- [observation/documented] The repository includes an MCP server exposing all CodeGuard security rules as tools over streamable HTTP, intended for centrally managed organizational deployment. -- evidence: [README.md#L62-L62](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/README.md#L62-L62) (`clm_694d417a16147dac3ac8862a927bde8dc17ce142db50b4f7251776010f0f37be`)
- [observation/documented] A CodeGuard Reviewer subagent performs full-repository security scans against all CodeGuard rules and emits findings as a SARIF 2.1.0 file, writing only that output file. -- evidence: [docs/codeguard-reviewer.md#L130-L137](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/codeguard-reviewer.md#L130-L137), [docs/codeguard-reviewer.md#L3-L3](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/codeguard-reviewer.md#L3-L3) (`clm_e06599c6414020a13ab2ec67eda6ebc502b08b9f99a0c51ec8637e367dc05765`)
- [observation/documented] Two authored skills ship in sources/skills/: security-review (full codebase review producing a structured markdown report) and memory-safe-migration (guided C/C++ migration to a memory-safe language). -- evidence: [docs/skills.md#L5-L8](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/skills.md#L5-L8), [docs/skills.md#L3-L3](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/skills.md#L3-L3) (`clm_7a71a86e32d0ac7f56fbd36f57b6302de1830f9439bede52d16049723e6d7009`)

## design-choices (2 claim(s))

- [observation/documented] The reviewer treats repository content as untrusted data, ignores embedded instructions, never executes discovered code, and redacts suspected credential values from SARIF and summary output. -- evidence: [docs/codeguard-reviewer.md#L130-L137](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/codeguard-reviewer.md#L130-L137) (`clm_bdfa070413e1c4c0946c7b098f942851d8983384d5360707d9c764b0c0bf1a81`)
- [observation/documented] The Codex plugin intentionally packages only ./skills/, excluding sources/skills/, the reviewer agent, hooks, and the MCP server, which are available via other install routes. -- evidence: [docs/codex-skill-plugin.md#L8-L11](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/codex-skill-plugin.md#L8-L11) (`clm_0ac5bb0279d411f56f19f4c8753eee832f9385e3ecab59be1b2cbb7317e67ded`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors regenerate the plugin with 'uv run python src/convert_to_ide_formats.py', which converts sources/ rules into skills/ (core rules only) and dist/ formats. -- evidence: [docs/claude-code-skill-plugin.md#L310-L313](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L310-L313), [docs/claude-code-skill-plugin.md#L307-L308](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L307-L308) (`clm_10dc9805950b6b976da0fc3073627c06e84f07733e027a97ede1df3cea651541`)
- [observation/documented] Repository development practice: local plugin testing is done via 'claude --plugin-dir .' after regeneration, with /reload-plugins to pick up regenerated files in a running session. -- evidence: [docs/claude-code-skill-plugin.md#L326-L326](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L326-L326), [docs/claude-code-skill-plugin.md#L321-L324](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L321-L324) (`clm_f23a1d16b1d66a36951885b38e2adb4ae72d8d149ac22c9feefece6d9fabc6e9`)

## skills-patterns (2 claim(s))

- [observation/documented] The Claude Code skill activates automatically when writing or reviewing code, implementing security-sensitive features, handling user input or credentials, or configuring cloud infrastructure. -- evidence: [docs/claude-code-skill-plugin.md#L49-L55](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L49-L55) (`clm_d6cd8e0597c3d2854cc1d0ae62042830afb1ddbc9c5047b4c9757796e3eb3622`)
- [observation/documented] The skill follows a 3-step workflow: initial security check to identify applicable rules, code generation with secure-by-default patterns, and a security review against rule checklists. -- evidence: [docs/claude-code-skill-plugin.md#L70-L75](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L70-L75), [docs/claude-code-skill-plugin.md#L66-L68](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L66-L68), [docs/claude-code-skill-plugin.md#L61-L64](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L61-L64) (`clm_159bc845ff0e7b1800ed47f647043e4874ff29f6202a0e0b80ab97140f75a83e`)

## interfaces (3 claim(s))

- [observation/documented] The reviewer emits SARIF 2.1.0 with tool.driver.name 'CodeGuard Security Reviewer', results only for confirmed or needs-human findings, and levels error/warning/note by rule class. -- evidence: [docs/codeguard-reviewer.md#L120-L126](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/codeguard-reviewer.md#L120-L126), [docs/codeguard-reviewer.md#L113-L116](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/codeguard-reviewer.md#L113-L116) (`clm_36553331b809a8cfe81c88d6ab9a19f9074d60272b6b1c75c48498fb368e43ba`)
- [observation/documented] The reviewer classifies candidates as confirmed, needs-human, or false-positive; false positives are excluded from SARIF with a one-line justification in the summary. -- evidence: [docs/codeguard-reviewer.md#L104-L107](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/codeguard-reviewer.md#L104-L107), [docs/codeguard-reviewer.md#L92-L96](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/codeguard-reviewer.md#L92-L96) (`clm_901b85e56a13136c81532b0aaaf29a859c412a6c3ec3ad3809dd58891965f497`)
- [observation/documented] The reviewer subagent is emitted for Claude Code, Cursor, OpenCode, GitHub Copilot/VS Code, and OpenAI Codex, each with a host-specific agent file location. -- evidence: [docs/codeguard-reviewer.md#L12-L18](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/codeguard-reviewer.md#L12-L18) (`clm_8a55c901cda20b01b387509e0a7e1c2597ebadfa19ff5dd2391105469ed9967d`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The Codex plugin route requires Codex CLI 0.142.0 or newer, the version that added marketplace plugin support with repository-root source, the layout this repository uses. -- evidence: [docs/codex-skill-plugin.md#L17-L19](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/codex-skill-plugin.md#L17-L19) (`clm_f046c7b617822bc55d705aacb4ea52f9cbc71ea8b75f23c302f9aa933421d757`)
- [observation/documented] Licensing is split: rules are CC BY 4.0 and tools are Apache License 2.0. -- evidence: [docs/claude-code-skill-plugin.md#L442-L443](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L442-L443) (`clm_d125e13a79a4a6a65cc83d3a8653f051bcce74966508293abae3f563a98204cf`)

## limitations (1 claim(s))

- [observation/documented] The CodeGuard Reviewer is designed for on-demand security scans only and does not activate for general code writing or editing. -- evidence: [docs/codeguard-reviewer.md#L5-L6](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/codeguard-reviewer.md#L5-L6) (`clm_d4367bed3d54835f86da39fe312e5d9f78c93bd3e12d3fbd3a17241e88a952ec`)

## relevance (1 claim(s))

- [observation/documented] CodeGuard targets AI coding agents (Cursor, GitHub Copilot, Codex, Windsurf, Claude Code) across the lifecycle: planning, generation, and post-generation review. -- evidence: [README.md#L30-L33](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/README.md#L30-L33) (`clm_a877599d9782f092e4eec24664d71dd408106ac3c0a6eca7cb12254f9cda6e10`)

