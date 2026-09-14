# ovh/shai

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f076f6128a82 @ 77abcd8c07c0bab2

## Summary (orientation draft, not independently verified)

SHAI is a Rust terminal coding agent with interactive, headless, HTTP-server, and shell-assistant modes, MCP-based custom agents, SHAI.md project context, and multiple LLM providers (OVHcloud default). Contributor guidance covers style, testing, DCO sign-off, Apache 2.0 licensing, and a release process.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The workspace is split into shai-cli (CLI entry point), shai-core (agent, state machine, protocol), and shai-llm (LLM provider wrappers), plus docs, examples, and tests directories. -- evidence: [SHAI.md#L15-L23](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/SHAI.md#L15-L23)
- design-choices (1 claim(s)):
  - [observation/documented] Project context is loaded from a `SHAI.md` file at the project root, which the agent automatically reads as additional context. -- evidence: [README.md#L132-L132](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L132-L132), [README.md#L9-L15](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L9-L15)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributions must follow coding style rules, be unit-tested and documented, be DCO signed-off, and be submitted via GitHub pull requests under Apache 2.0. -- evidence: [CONTRIBUTING.md#L35-L36](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/CONTRIBUTING.md#L35-L36), [CONTRIBUTING.md#L30-L31](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/CONTRIBUTING.md#L30-L31), [CONTRIBUTING.md#L6-L10](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/CONTRIBUTING.md#L6-L10)
  - [observation/documented] Repository development practice: releases require bumping versions in four crate Cargo.toml files, running `cargo check`, then tagging and pushing to trigger the release workflow. -- evidence: [CONTRIBUTING.md#L16-L19](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/CONTRIBUTING.md#L16-L19), [CONTRIBUTING.md#L23-L26](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/CONTRIBUTING.md#L23-L26)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Running `shai` starts an interactive terminal coding agent for chatting, writing code, fixing bugs, and answering questions. -- evidence: [README.md#L59-L59](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L59-L59), [README.md#L9-L15](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L9-L15)
  - [observation/documented] Headless mode accepts a piped prompt and streams events to stderr; shai can be told to return the whole conversation as a trace, which enables chaining shai calls. -- evidence: [README.md#L63-L63](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L63-L63), [README.md#L79-L81](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L79-L81), [README.md#L77-L77](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L77-L77), [README.md#L71-L71](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L71-L71)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Custom agents can be defined in separate config files placed under ~/.config/shai/agents/, listed with `shai agent list`, and run via `shai agent <name>`; MCP and OAuth are supported. -- evidence: [README.md#L136-L136](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L136-L136), [README.md#L142-L145](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L142-L145), [README.md#L140-L140](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L140-L140), [README.md#L147-L147](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L147-L147), [README.md#L149-L151](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L149-L151), [README.md#L9-L15](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L9-L15)
- tools-permissions (1 claim(s)):
  - [observation/documented] A shell-assistant mode hooks the terminal via `shai on`/`shai off`, sending the last command, output, and error code to the LLM provider to suggest fixes for failed commands. -- evidence: [README.md#L110-L110](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L110-L110), [README.md#L124-L126](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L124-L126), [README.md#L114-L116](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L114-L116)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Shai works with multiple LLM providers including OVHcloud (default, anonymous with rate limits), OpenAI, and other compatible endpoints; `shai auth` configures sign-in or provider selection. -- evidence: [README.md#L41-L43](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L41-L43), [README.md#L39-L39](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L39-L39), [README.md#L9-L15](https://github.com/ovh/shai/blob/f076f6128a826a96a28e47d0d674284b1552905e/README.md#L9-L15)
More evidence: [full detail](shai.detail.md)

Metadata and full claim list: [full detail](shai.detail.md)
Human notes ([notes](shai.notes.md), never overwritten by build)

[Back to map index](../../index.md)
