# aws/amazon-q-developer-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 15cc8f3cd18c @ 1a8a017dfd018fb0

## Summary (orientation draft, not independently verified)

Selected evidence records: The README states this open-source project is no longer actively maintained and will only receive critical security fixes; Amazon Q Developer CLI continues as the closed-source Kiro CLI. The main component is the chat_cli crate, the `q` CLI for interfacing with Amazon Q Developer from the command line; the repo also contains crates, scripts, and docs directories.

## Source coverage

Source coverage (partial): 6 of 18 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The main component is the chat_cli crate, the `q` CLI for interfacing with Amazon Q Developer from the command line; the repo also contains crates, scripts, and docs directories. -- evidence: [README.md#L54-L58](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/README.md#L54-L58)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors need macOS with Xcode 13+ and Brew, install the Rust toolchain via rustup (stable plus nightly) and typos-cli, then build with cargo run --bin chat_cli, test with cargo test, lint with cargo clippy, and format with cargo +nightly fmt. -- evidence: [README.md#L45-L50](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/README.md#L45-L50), [README.md#L36-L41](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/README.md#L36-L41), [README.md#L24-L26](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/README.md#L24-L26)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Agent configurations are JSON files whose filename (minus .json) becomes the agent name; sections include name, description, prompt, mcpServers, tools, toolAliases, allowedTools, toolsSettings, resources, hooks, useLegacyMcpJson, and model. -- evidence: [docs/agent-format.md#L3-L3](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-format.md#L3-L3), [docs/agent-format.md#L10-L21](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-format.md#L10-L21)
  - [observation/documented] The prompt field accepts inline text or file:// URIs; relative paths resolve against the agent config file's directory and absolute paths are used as-is. -- evidence: [docs/agent-format.md#L45-L45](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-format.md#L45-L45), [docs/agent-format.md#L67-L71](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-format.md#L67-L71)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] Agent selection follows a fallback hierarchy: the --agent flag first, then the chat.defaultAgent setting, then a built-in default agent (all tools, fs_read pre-approved, legacy MCP enabled); a q_cli_default agent file can override the built-in default. -- evidence: [docs/default-agent-behavior.md#L32-L45](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/default-agent-behavior.md#L32-L45), [docs/default-agent-behavior.md#L98-L100](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/default-agent-behavior.md#L98-L100), [docs/default-agent-behavior.md#L30-L30](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/default-agent-behavior.md#L30-L30), [docs/default-agent-behavior.md#L21-L23](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/default-agent-behavior.md#L21-L23), [docs/default-agent-behavior.md#L102-L102](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/default-agent-behavior.md#L102-L102), [docs/default-agent-behavior.md#L10-L10](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/default-agent-behavior.md#L10-L10), [docs/default-agent-behavior.md#L55-L56](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/default-agent-behavior.md#L55-L56), [docs/default-agent-behavior.md#L65-L65](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/default-agent-behavior.md#L65-L65)
  - [observation/documented] Agent files resolve local-first: .amazonq/cli-agents/ in the working directory takes precedence over ~/.aws/amazonq/cli-agents/, with a warning on name conflicts; the global directory is auto-created while the local one must be created manually. -- evidence: [docs/agent-file-locations.md#L55-L55](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-file-locations.md#L55-L55), [docs/agent-file-locations.md#L110-L110](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-file-locations.md#L110-L110), [docs/agent-file-locations.md#L50-L51](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-file-locations.md#L50-L51), [docs/agent-file-locations.md#L61-L61](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-file-locations.md#L61-L61)
- tools-permissions (1 claim(s)):
  - [observation/documented] By default fs_read and report_issue are trusted, while execute_bash, fs_write, and use_aws prompt for permission; toolsSettings can pre-allow specific commands, paths, or AWS services, with deny rules evaluated before allow rules. -- evidence: [docs/built-in-tools.md#L154-L158](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/built-in-tools.md#L154-L158), [docs/built-in-tools.md#L195-L197](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/built-in-tools.md#L195-L197), [docs/built-in-tools.md#L35-L40](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/built-in-tools.md#L35-L40), [docs/built-in-tools.md#L63-L66](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/built-in-tools.md#L63-L66)
- evaluation: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](amazon-q-developer-cli.detail.md)

Metadata and full claim list: [full detail](amazon-q-developer-cli.detail.md)
Human notes ([notes](amazon-q-developer-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
