# sylphai-inc/adal-cli -- full detail

[Back to orientation](adal-cli.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sylphai-inc/adal-cli/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/80a34de43a933b55.json](../../../wiki/dossiers/sylphai-inc/adal-cli/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/80a34de43a933b55.json)

## specifications (1 claim(s))

- [observation/documented] AdaL is described as an AI coding agent that runs in the terminal, created by SylphAI and named after Ada Lovelace. -- evidence: [README.md#L29-L29](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L29-L29) (`clm_8e51ee806a3525e85811682abecf35488bea205c979d1d32f97b9a621f248a12`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The product claims to work with Claude, GPT, Gemini, GLM, Kimi, DeepSeek, MiniMax, and local models. -- evidence: [README.md#L29-L29](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L29-L29) (`clm_1e1fcb7891b3f3663901f0fc084712e086fee96dca92b206f018936b5b269410`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributing a skill involves forking SylphAI-Inc/skills, creating skills/<name>/SKILL.md with frontmatter (name, description, author, version), registering it in .claude-plugin/marketplace.json, and opening a pull request. -- evidence: [README.md#L151-L157](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L151-L157), [README.md#L146-L149](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L146-L149) (`clm_26ed6a72d58732b5aca84b214ae1975bf4f7134c46eadde8b7dca50e5fe96b53`)
- [observation/documented] Repository development practice: issue reports should include expected vs actual behavior, reproduction steps, the CLI version from `adal -v`, OS, and terminal. -- evidence: [README.md#L189-L189](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L189-L189), [README.md#L191-L195](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L191-L195) (`clm_d9a14fe47b596c9d295992924dcf21c6e9950551b293bb0a9fe82dfc5006ebf8`)

## skills-patterns (1 claim(s))

- [observation/documented] Skills are markdown files that teach the agent a repeatable workflow without touching CLI internals, stored in the SylphAI-Inc/skills repository and installable via /plugin marketplace add and /plugin install commands. -- evidence: [README.md#L134-L134](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L134-L134), [README.md#L136-L136](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L136-L136), [README.md#L138-L142](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L138-L142) (`clm_6f1e8eaa727ae8418f8f8845e84321a82542b68cf3a4bf233ba772c3c13f4786`)

## interfaces (5 claim(s))

- [observation/documented] The CLI exposes slash commands including /model for model choice, /ide to open the session in an IDE, /resume to restore prior context, and /stats for session health and usage. -- evidence: [README.md#L82-L87](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L82-L87) (`clm_c5407aae2cf27f5af7bfe3863285182fdb950c5cc12a1576d56cf62e8b6c24a0`)
- [observation/documented] Running the `adal` command starts the CLI, and the first run opens the browser for authentication. -- evidence: [README.md#L67-L69](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L67-L69), [README.md#L71-L71](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L71-L71) (`clm_dc6e088defa02c278a24c58de49b0eadff42dca0b327b40d04bc88beb1e7cba1`)
- [observation/documented] The CLI advertises review-first behavior: tool calls, file edits, diffs, and plans stay visible before sign-off, plus a command palette for switching models. -- evidence: [README.md#L77-L80](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L77-L80) (`clm_8b6555cb0f50383509f9d63583306c8c531c856dcd5e23e53e84932baac59a07`)
- [observation/documented] Documented feature areas include MCP server support, deep research, web search, browser use, image generation and analysis, headless mode, cron-scheduled prompts, local models, and bring-your-own API key. -- evidence: [README.md#L106-L116](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L106-L116) (`clm_d0f4b1aac6b74f505909b37059a66fc02fe0016591dd956252fb52bcbf1d9f36`)
- [inference/documented] The CLI appears to support CLI-to-IDE handoff, allowing the same session to be opened in AdaL's agentic IDE via the /ide command. -- evidence: [README.md#L82-L87](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L82-L87), [README.md#L77-L80](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L77-L80) (`clm_608b8f9dbd536ce1e371eed49e127fae4e691f6c44602eacde1dfa2a02d7e8f6`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Native install is recommended and is said to manage AdaL's runtime and updates across platforms; install scripts are fetched from adal.sylph.ai for macOS/Linux/WSL and Windows. -- evidence: [README.md#L43-L43](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L43-L43), [README.md#L47-L49](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L47-L49), [README.md#L53-L55](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L53-L55) (`clm_7b7e508c1960b4aa3cd0bdc0e940c25b4add1f6b5f2d5b92019bf15175b7c250`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

