# angleschina/angles-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: github-verified-rename, alltheagents.org-backing - Projects: Observatory
Formerly: zsj305/angles-cli (github id 1306494403).
Latest snapshot: commit 53cf51b702e4 @ 8818c2194b628043

## Summary (orientation draft, not independently verified)

Angles Code CLI is a terminal-native agentic coding assistant shipped as a single ~1.6 MB static Rust binary with zero runtime dependencies, 30+ built-in angles-* tools, 11 model providers, a TUI setup wizard, a local HTTP gateway, and a handlebars-style system-prompt template. Evidence is documentation-based (README, gateway-flow.md, instructions.txt); no runtime code is inspected in these slices. Evidence coverage: 161 of 249 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The codebase is organized into Rust modules including main.rs (entry/routing), cli.rs, config.rs, provider.rs, gateway.rs, instructions.rs, api.rs, search.rs, server.rs, and tools.rs, plus instructions.txt, providers.toml, and docs/. -- evidence: [README.md#L67-L89](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L67-L89)
  - [observation/documented] The conversation loop lives in api.rs, an OpenAI/Anthropic/Gemini client with streaming and a tool-calling loop that resolves angles-* commands to implementations in tools.rs. -- evidence: [README.md#L91-L91](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L91-L91)
- design-choices (2 claim(s)):
  - [observation/documented] The tool ships as a single static ~1.6 MB Rust binary with zero runtime dependencies (no Node, Python, or dynamic libc), aimed at constrained environments like ARM64 SBCs, rootless containers, and iSH. -- evidence: [README.md#L37-L37](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L37-L37), [README.md#L54-L54](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L54-L54), [README.md#L56-L61](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L56-L61)
  - [observation/documented] All agent capabilities are exposed as curated angles-* commands rather than free-form shell improvisation, binding the model to a deterministic tool set. -- evidence: [README.md#L99-L99](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L99-L99)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: building from source uses cargo build --release with Makefile targets for Linux ARM64/x64 and macOS ARM64 cross-compilation, and GitHub Actions produces prebuilt binaries for all 5 platforms on every tag push. -- evidence: [README.md#L256-L258](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L256-L258), [README.md#L266-L270](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L266-L270), [README.md#L272-L272](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L272-L272)
  - [observation/documented] Repository development practice: the repo includes a release workflow (.github/workflows/release.yml), a Cross.toml for cross-compilation, and a docs/ directory published as a GitHub Pages site. -- evidence: [README.md#L67-L89](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L67-L89)
- skills-patterns (1 claim(s)):
  - [observation/documented] The 13 KB instructions.txt system-prompt template uses handlebars-style {{variable}} injection for config values, persona, and architecture, and directs the agent to emit operation plans with fixed verbs before non-trivial tasks. -- evidence: [README.md#L67-L89](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L67-L89), [instructions.txt#L99-L105](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/instructions.txt#L99-L105), [instructions.txt#L96-L97](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/instructions.txt#L96-L97), [instructions.txt#L21-L28](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/instructions.txt#L21-L28)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI offers subcommands including an interactive default session (angles), angles exec for one-shot runs, angles plan, angles serve, angles gateway, angles config, angles doctor, and angles help. -- evidence: [README.md#L218-L218](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L218-L218), [README.md#L221-L221](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L221-L221), [README.md#L215-L215](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L215-L215), [README.md#L212-L212](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L212-L212), [README.md#L209-L209](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L209-L209), [README.md#L224-L227](https://github.com/angleschina/angles-cli/blob/53cf51b702e45dd0621b8453d0cc3d301b98cef1/README.md#L224-L227)
More evidence: [full detail](angles-cli.detail.md)

Metadata and full claim list: [full detail](angles-cli.detail.md)
Human notes ([notes](angles-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
