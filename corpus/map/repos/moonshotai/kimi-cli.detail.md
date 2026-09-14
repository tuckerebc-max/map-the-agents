# moonshotai/kimi-cli -- full detail

[Back to orientation](kimi-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/moonshotai/kimi-cli/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/4eced92fc40afd7a.json](../../../wiki/dossiers/moonshotai/kimi-cli/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/4eced92fc40afd7a.json)

## specifications (1 claim(s))

- [observation/documented] The README describes Kimi CLI as a terminal AI agent that helps complete software development tasks and terminal operations: it reads and edits code, executes shell commands, searches and fetches web pages, and autonomously plans and adjusts actions during execution. -- evidence: [README.md#L14-L14](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/README.md#L14-L14) (`clm_a45d0534e9a3a87cacd4f8350c8c928574e53c726cce9382b176a911c376334a`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] Documentation states a detected newer version shows a blocking update prompt before the shell loads, letting the user upgrade immediately, skip once, or skip and suppress future reminders for that version; this whole update check can be disabled with an environment variable. -- evidence: [docs/en/faq.md#L146-L148](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/docs/en/faq.md#L146-L148), [docs/en/faq.md#L144-L144](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/docs/en/faq.md#L144-L144), [docs/en/faq.md#L158-L158](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/docs/en/faq.md#L158-L158), [docs/en/faq.md#L152-L152](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/docs/en/faq.md#L152-L152) (`clm_f069076df183e2ab68d9b97fc2917f08965a96a0352ad530fd72183259b7e4b8`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: Documented development commands include make format, make check for linting and type checking, make test, and separate make test-kimi-cli, make test-kosong, and make test-pykaos targets for each component. -- evidence: [README.md#L165-L175](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/README.md#L165-L175) (`clm_b999aa78f8a734d066282e275a78dd73cd1a5960e0cf889701d9932128f564e6`)

## skills-patterns (2 claim(s))

- [observation/documented] Documentation distinguishes two Kimi Code CLI extension mechanisms: skills give knowledge-based guidance the AI reads via SKILL.md, while plugins declare executable tools through plugin.json that the AI can invoke directly. -- evidence: [docs/en/customization/skills.md#L15-L16](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/docs/en/customization/skills.md#L15-L16) (`clm_abb71dd2bc5e119b629bacd09d899b3a160826f47ab1c7d5f40a154f31e05a2d`)
- [observation/documented] Documented skill discovery scans a brand group (kimi, then claude, then codex directories) and a generic group independently and merges the results, with same-named brand-group skills resolved kimi-over-claude-over-codex under a setting that defaults to merging every available brand directory. -- evidence: [docs/en/customization/skills.md#L44-L44](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/docs/en/customization/skills.md#L44-L44), [docs/en/customization/skills.md#L34-L40](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/docs/en/customization/skills.md#L34-L40) (`clm_0fe113e8fbc89317cb2770c437488b2a914be30db59a2e9a009bdeb8447bde6b`)

## interfaces (2 claim(s))

- [observation/documented] Documentation describes a shell command mode toggled with Ctrl-X that runs shell commands without leaving Kimi CLI, noting built-in shell commands like cd are not yet supported in that mode. -- evidence: [README.md#L28-L29](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/README.md#L28-L29), [README.md#L24-L24](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/README.md#L24-L24) (`clm_87f753f389ecfe88ecf9f94ee590917c1f1e7c69f42ba36a84c8595eb39f5d62`)
- [observation/documented] Documentation states Kimi CLI supports the Agent Client Protocol out of the box, so it can run as an ACP agent server for ACP-compatible editors such as Zed or JetBrains after completing login in the terminal first. -- evidence: [README.md#L39-L39](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/README.md#L39-L39), [README.md#L43-L43](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/README.md#L43-L43) (`clm_7b7d9a373b763ae37df9b95f3b6e05a53c9b51887025ab28b1cd617f6215b663`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Documentation states that if the working directory becomes inaccessible mid-session, Kimi Code CLI detects this, shows a crash report with the session ID and path, exits cleanly, and lets the session be resumed from the correct directory. -- evidence: [docs/en/faq.md#L47-L47](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/docs/en/faq.md#L47-L47) (`clm_69af78d568cd66eb1f537fb2a366e29418d664e650884e8f65a376f75006dd9e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The README gives kimi mcp add examples for HTTP, HTTP with OAuth, and stdio servers, and documents ad-hoc connections through the --mcp-config-file option. -- evidence: [README.md#L96-L96](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/README.md#L96-L96), [README.md#L102-L102](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/README.md#L102-L102), [README.md#L99-L99](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/README.md#L99-L99), [README.md#L137-L137](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/README.md#L137-L137) (`clm_0da987b323ed937fe2f0670d9e5ee6a841894784362689ee0aadc515ef4cfb5f`)

## limitations (2 claim(s))

- [observation/documented] A prominent README notice states Kimi CLI is evolving into Kimi Code CLI from the same team, that installing Kimi Code CLI automatically migrates existing configuration and sessions, and that this project will be gradually wound down while its docs and existing installs remain available. -- evidence: [README.md#L11-L12](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/README.md#L11-L12) (`clm_2de7cbb8e74f3dfc5559ed151ee9a01149bc2bf99c6e6455bf0f64cb702afa66`)
- [observation/documented] Documentation states running cd in shell command mode does not change Kimi Code CLI's own working directory, because each shell command runs in an independent subprocess whose directory changes do not persist. -- evidence: [docs/en/faq.md#L28-L28](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/docs/en/faq.md#L28-L28) (`clm_f8648b5e8f4a3a2d7049619d0cfd930f059906763b7b456e9f51caf753cab9ac`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

