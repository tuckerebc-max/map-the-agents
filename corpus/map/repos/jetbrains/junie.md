# jetbrains/junie

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 02f117f99d3a @ 67e12109739a8d65

## Summary (orientation draft, not independently verified)

The snapshot contains only README and LICENSE files for Junie, a JetBrains LLM-agnostic terminal/IDE/CI coding agent, documenting installation, update channels, authentication, and GitHub integration. No source code or development-practice files are present in the evidence.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 8 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

8 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Junie is described as an LLM-agnostic coding agent by JetBrains that runs in the terminal, integrates with IDEs and CI/CD pipelines, and takes natural-language tasks such as fixing bugs, implementing features, or reviewing PRs. -- evidence: [README.md#L2-L2](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L2-L2), [README.md#L4-L4](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L4-L4)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (1 claim(s)):
  - [observation/documented] Installation is documented for macOS/Linux via a curl-piped shell script, Windows via a PowerShell one-liner, plus Homebrew (jetbrains-junie/junie tap) and npm (@jetbrains/junie) alternatives. -- evidence: [README.md#L40-L42](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L40-L42), [README.md#L33-L36](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L33-L36), [README.md#L18-L20](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L18-L20), [README.md#L24-L26](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L24-L26)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The CLI supports launching a different update channel for a single run via flags like --eap, --nightly, --experimental, --release, or the explicit --channel form, without changing the installed default. -- evidence: [README.md#L48-L50](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L48-L50), [README.md#L52-L58](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L52-L58)
  - [observation/documented] A specific build of a channel can be pinned with --use-version (e.g. junie --eap --use-version=122.1), and a plain junie invocation afterwards still launches and auto-updates the default channel. -- evidence: [README.md#L60-L60](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L60-L60), [README.md#L67-L68](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L67-L68), [README.md#L62-L65](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L62-L65)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Authentication options include JetBrains Account OAuth, a Junie API key, or bring-your-own-key with model providers Anthropic, OpenAI, Google, xAI, OpenRouter, or Copilot. -- evidence: [README.md#L74-L76](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L74-L76)
- limitations (1 claim(s)):
  - [inference/documented] The evidence consists solely of README and LICENSE content, so runtime internals such as architecture, memory, or tool-permission behavior cannot be verified from this snapshot. -- evidence: [README.md#L2-L2](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L2-L2), [LICENSE.md#L1-L1](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/LICENSE.md#L1-L1)
- relevance (1 claim(s)):
  - [observation/documented] The repository is the public home of JetBrains' Junie CLI, with links to official docs, a Discord community, and a GitHub issue tracker for bug reports; use is governed by the JetBrains AI Service Terms of Service. -- evidence: [README.md#L101-L101](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L101-L101), [README.md#L125-L125](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L125-L125), [README.md#L119-L119](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L119-L119), [README.md#L115-L115](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L115-L115)

(1 additional claim(s) omitted for length; see [full detail](junie.detail.md) for every claim.)

Metadata and full claim list: [full detail](junie.detail.md)
Human notes ([notes](junie.notes.md), never overwritten by build)

[Back to map index](../../index.md)
