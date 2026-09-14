# jetbrains/junie -- full detail

[Back to orientation](junie.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jetbrains/junie/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/67e12109739a8d65.json](../../../wiki/dossiers/jetbrains/junie/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/67e12109739a8d65.json)

## specifications (1 claim(s))

- [observation/documented] Junie is described as an LLM-agnostic coding agent by JetBrains that runs in the terminal, integrates with IDEs and CI/CD pipelines, and takes natural-language tasks such as fixing bugs, implementing features, or reviewing PRs. -- evidence: [README.md#L2-L2](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L2-L2), [README.md#L4-L4](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L4-L4) (`clm_e47d15145e5dba730a31448a5612cc3bfb93c904fb9a4ebbb07cd47c2a8cb9a1`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (1 claim(s))

- [observation/documented] Installation is documented for macOS/Linux via a curl-piped shell script, Windows via a PowerShell one-liner, plus Homebrew (jetbrains-junie/junie tap) and npm (@jetbrains/junie) alternatives. -- evidence: [README.md#L40-L42](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L40-L42), [README.md#L33-L36](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L33-L36), [README.md#L18-L20](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L18-L20), [README.md#L24-L26](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L24-L26) (`clm_3e0822cebadf25f51cde902f568108db7998413710f5aa480a1f65ca6dcb9540`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI supports launching a different update channel for a single run via flags like --eap, --nightly, --experimental, --release, or the explicit --channel form, without changing the installed default. -- evidence: [README.md#L48-L50](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L48-L50), [README.md#L52-L58](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L52-L58) (`clm_eebaaef744dd83b8bb93e73e66222d0924e672284bbc0eb3d430cb4ce6d720d2`)
- [observation/documented] A specific build of a channel can be pinned with --use-version (e.g. junie --eap --use-version=122.1), and a plain junie invocation afterwards still launches and auto-updates the default channel. -- evidence: [README.md#L60-L60](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L60-L60), [README.md#L67-L68](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L67-L68), [README.md#L62-L65](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L62-L65) (`clm_b810501065a13dc04264ee8942757e0a962be89957b0c9aca0675b6e05563757`)
- [observation/documented] The agent exposes in-session commands including /install-github-action to set up a GitHub Action responding to issues, PRs, and CI failures, and /feedback for reporting bugs. -- evidence: [README.md#L105-L105](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L105-L105), [README.md#L107-L109](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L107-L109), [README.md#L115-L115](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L115-L115) (`clm_13cfac17055b22d6ff1c860e7624c3b6bdb4c4d60a4a4ab49f5c20be4979b52f`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Authentication options include JetBrains Account OAuth, a Junie API key, or bring-your-own-key with model providers Anthropic, OpenAI, Google, xAI, OpenRouter, or Copilot. -- evidence: [README.md#L74-L76](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L74-L76) (`clm_c746fbc9ca43bda4a0f26118284ac50daee2ae54dbb8b52b65cea0e28fc86ccf`)

## limitations (1 claim(s))

- [inference/documented] The evidence consists solely of README and LICENSE content, so runtime internals such as architecture, memory, or tool-permission behavior cannot be verified from this snapshot. -- evidence: [README.md#L2-L2](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L2-L2), [LICENSE.md#L1-L1](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/LICENSE.md#L1-L1) (`clm_6c8399a15eb7d1571d8ff6709a9f6ebf62958413ef5eff547876b0dafd2b860d`)

## relevance (1 claim(s))

- [observation/documented] The repository is the public home of JetBrains' Junie CLI, with links to official docs, a Discord community, and a GitHub issue tracker for bug reports; use is governed by the JetBrains AI Service Terms of Service. -- evidence: [README.md#L101-L101](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L101-L101), [README.md#L125-L125](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L125-L125), [README.md#L119-L119](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L119-L119), [README.md#L115-L115](https://github.com/JetBrains/junie/blob/02f117f99d3ac94879dbe1d643b031a12c8ef8c9/README.md#L115-L115) (`clm_9accc951c04c6475220f49fd35f46f81dd2671e3a4627fab8387fcf17602d850`)

