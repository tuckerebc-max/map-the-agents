# aws/amazon-q-developer-cli -- full detail

[Back to orientation](amazon-q-developer-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/aws/amazon-q-developer-cli/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/1a8a017dfd018fb0.json](../../../wiki/dossiers/aws/amazon-q-developer-cli/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/1a8a017dfd018fb0.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The main component is the chat_cli crate, the `q` CLI for interfacing with Amazon Q Developer from the command line; the repo also contains crates, scripts, and docs directories. -- evidence: [README.md#L54-L58](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/README.md#L54-L58) (`clm_0347fc06cd25320cbcfff0e1a47b120b65f0d1a7e260f64fb9b4fcf72826693d`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors need macOS with Xcode 13+ and Brew, install the Rust toolchain via rustup (stable plus nightly) and typos-cli, then build with cargo run --bin chat_cli, test with cargo test, lint with cargo clippy, and format with cargo +nightly fmt. -- evidence: [README.md#L45-L50](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/README.md#L45-L50), [README.md#L36-L41](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/README.md#L36-L41), [README.md#L24-L26](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/README.md#L24-L26) (`clm_3e682aabc706c0737272b81f88722d17e5bd166111b55b7246566d6e4cca40fc`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Agent configurations are JSON files whose filename (minus .json) becomes the agent name; sections include name, description, prompt, mcpServers, tools, toolAliases, allowedTools, toolsSettings, resources, hooks, useLegacyMcpJson, and model. -- evidence: [docs/agent-format.md#L3-L3](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-format.md#L3-L3), [docs/agent-format.md#L10-L21](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-format.md#L10-L21) (`clm_38051fa623c098bb314426402b8dabfb3b1c0c20d449a21a2eb35b7d131dd7b0`)
- [observation/documented] The prompt field accepts inline text or file:// URIs; relative paths resolve against the agent config file's directory and absolute paths are used as-is. -- evidence: [docs/agent-format.md#L45-L45](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-format.md#L45-L45), [docs/agent-format.md#L67-L71](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-format.md#L67-L71) (`clm_b400a4c7ebbb5a9d4ec926f0792c8c0de9874fbd1a0c8c6bb60e5425a4fdd314`)
- [observation/documented] Each MCP server is configured with a required command plus optional args, env variables, and a per-request timeout in milliseconds defaulting to 120000. -- evidence: [docs/agent-format.md#L110-L114](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-format.md#L110-L114) (`clm_11c8952ee4dd045db2b1fbf14af4701ddfc82f9c64f2da36143ddb7ad079735a`)
- [observation/documented] Hooks run commands at lifecycle trigger points: agentSpawn, userPromptSubmit, preToolUse (which can block tool use), postToolUse, and stop; each hook has a required command and an optional tool-name matcher. -- evidence: [docs/agent-format.md#L337-L342](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-format.md#L337-L342), [docs/agent-format.md#L333-L335](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-format.md#L333-L335) (`clm_e73a9f1cec7ee8e60e3c1afbf841c371d725b5d8b6390a1ca2ef22aba960911b`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] Agent selection follows a fallback hierarchy: the --agent flag first, then the chat.defaultAgent setting, then a built-in default agent (all tools, fs_read pre-approved, legacy MCP enabled); a q_cli_default agent file can override the built-in default. -- evidence: [docs/default-agent-behavior.md#L32-L45](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/default-agent-behavior.md#L32-L45), [docs/default-agent-behavior.md#L98-L100](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/default-agent-behavior.md#L98-L100), [docs/default-agent-behavior.md#L30-L30](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/default-agent-behavior.md#L30-L30), [docs/default-agent-behavior.md#L21-L23](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/default-agent-behavior.md#L21-L23), [docs/default-agent-behavior.md#L102-L102](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/default-agent-behavior.md#L102-L102), [docs/default-agent-behavior.md#L10-L10](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/default-agent-behavior.md#L10-L10), [docs/default-agent-behavior.md#L55-L56](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/default-agent-behavior.md#L55-L56), [docs/default-agent-behavior.md#L65-L65](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/default-agent-behavior.md#L65-L65) (`clm_9f9dbec13c96aa90485a5264c296454d5fe870c6d999f4073489024bb72706d0`)
- [observation/documented] Agent files resolve local-first: .amazonq/cli-agents/ in the working directory takes precedence over ~/.aws/amazonq/cli-agents/, with a warning on name conflicts; the global directory is auto-created while the local one must be created manually. -- evidence: [docs/agent-file-locations.md#L55-L55](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-file-locations.md#L55-L55), [docs/agent-file-locations.md#L110-L110](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-file-locations.md#L110-L110), [docs/agent-file-locations.md#L50-L51](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-file-locations.md#L50-L51), [docs/agent-file-locations.md#L61-L61](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/agent-file-locations.md#L61-L61) (`clm_9a049dcd95f0f40120b9ef413d96e2b257fb9044fb65bcf28f5ed458e3edb1ec`)

## tools-permissions (1 claim(s))

- [observation/documented] By default fs_read and report_issue are trusted, while execute_bash, fs_write, and use_aws prompt for permission; toolsSettings can pre-allow specific commands, paths, or AWS services, with deny rules evaluated before allow rules. -- evidence: [docs/built-in-tools.md#L154-L158](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/built-in-tools.md#L154-L158), [docs/built-in-tools.md#L195-L197](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/built-in-tools.md#L195-L197), [docs/built-in-tools.md#L35-L40](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/built-in-tools.md#L35-L40), [docs/built-in-tools.md#L63-L66](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/docs/built-in-tools.md#L63-L66) (`clm_9588730130eae209277eb1411013cf5ee0f6c00f94cf86f230e03afe80245f6a`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project is written in Rust; contributor setup instructions require installing the Rust toolchain via rustup with stable as default plus the nightly toolchain. -- evidence: [README.md#L36-L41](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/README.md#L36-L41) (`clm_7451d006a5619d5533b960dffee79cf6d97616c0c27a6a6636d9e3ebe58f24ab`)

## limitations (1 claim(s))

- [observation/documented] The README states this open-source project is no longer actively maintained and will only receive critical security fixes; Amazon Q Developer CLI continues as the closed-source Kiro CLI. -- evidence: [README.md#L3-L4](https://github.com/aws/amazon-q-developer-cli/blob/15cc8f3cd18c4272925ce1c7053268eedff1ea0a/README.md#L3-L4) (`clm_2983288e6f8844552e4040f302925ec47a6bce3b5b90f6dbaf1b4984126eee0c`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

