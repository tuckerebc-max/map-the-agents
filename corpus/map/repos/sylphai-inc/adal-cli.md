# sylphai-inc/adal-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f278cb8ab54b @ 80a34de43a933b55

## Summary (orientation draft, not independently verified)

AdaL is described as an AI coding agent that runs in the terminal, created by SylphAI and named after Ada Lovelace. The product claims to work with Claude, GPT, Gemini, GLM, Kimi, DeepSeek, MiniMax, and local models.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] AdaL is described as an AI coding agent that runs in the terminal, created by SylphAI and named after Ada Lovelace. -- evidence: [README.md#L29-L29](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L29-L29)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] The product claims to work with Claude, GPT, Gemini, GLM, Kimi, DeepSeek, MiniMax, and local models. -- evidence: [README.md#L29-L29](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L29-L29)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributing a skill involves forking SylphAI-Inc/skills, creating skills/<name>/SKILL.md with frontmatter (name, description, author, version), registering it in .claude-plugin/marketplace.json, and opening a pull request. -- evidence: [README.md#L151-L157](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L151-L157), [README.md#L146-L149](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L146-L149)
  - [observation/documented] Repository development practice: issue reports should include expected vs actual behavior, reproduction steps, the CLI version from `adal -v`, OS, and terminal. -- evidence: [README.md#L189-L189](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L189-L189), [README.md#L191-L195](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L191-L195)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are markdown files that teach the agent a repeatable workflow without touching CLI internals, stored in the SylphAI-Inc/skills repository and installable via /plugin marketplace add and /plugin install commands. -- evidence: [README.md#L134-L134](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L134-L134), [README.md#L136-L136](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L136-L136), [README.md#L138-L142](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L138-L142)
- interfaces (5 claim(s)):
  - [observation/documented] The CLI exposes slash commands including /model for model choice, /ide to open the session in an IDE, /resume to restore prior context, and /stats for session health and usage. -- evidence: [README.md#L82-L87](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L82-L87)
  - [observation/documented] Running the `adal` command starts the CLI, and the first run opens the browser for authentication. -- evidence: [README.md#L67-L69](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L67-L69), [README.md#L71-L71](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L71-L71)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Native install is recommended and is said to manage AdaL's runtime and updates across platforms; install scripts are fetched from adal.sylph.ai for macOS/Linux/WSL and Windows. -- evidence: [README.md#L43-L43](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L43-L43), [README.md#L47-L49](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L47-L49), [README.md#L53-L55](https://github.com/SylphAI-Inc/adal-cli/blob/f278cb8ab54bae3e49a6be1f1004686cf8615f1c/README.md#L53-L55)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](adal-cli.detail.md) for every claim.)

Metadata and full claim list: [full detail](adal-cli.detail.md)
Human notes ([notes](adal-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
