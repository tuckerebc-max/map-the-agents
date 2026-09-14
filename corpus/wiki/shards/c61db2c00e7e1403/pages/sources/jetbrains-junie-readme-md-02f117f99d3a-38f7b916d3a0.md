---
access: public
aliases: []
claim_ids:
- clm_13cfac17055b22d6ff1c860e7624c3b6bdb4c4d60a4a4ab49f5c20be4979b52f
- clm_3e0822cebadf25f51cde902f568108db7998413710f5aa480a1f65ca6dcb9540
- clm_6c8399a15eb7d1571d8ff6709a9f6ebf62958413ef5eff547876b0dafd2b860d
- clm_9accc951c04c6475220f49fd35f46f81dd2671e3a4627fab8387fcf17602d850
- clm_b810501065a13dc04264ee8942757e0a962be89957b0c9aca0675b6e05563757
- clm_c746fbc9ca43bda4a0f26118284ac50daee2ae54dbb8b52b65cea0e28fc86ccf
- clm_e47d15145e5dba730a31448a5612cc3bfb93c904fb9a4ebbb07cd47c2a8cb9a1
- clm_eebaaef744dd83b8bb93e73e66222d0924e672284bbc0eb3d430cb4ce6d720d2
maturity: draft
page_id: pg_c5f533553ec657c9829a38f7b916d3a0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_0508f900ca445a84959d8d0d77a43579
title: JetBrains/junie/README.md @ 02f117f99d3a
updated_at: '2026-09-14T02:06:52Z'
---

# JetBrains/junie/README.md @ 02f117f99d3a

<!-- rcw:begin owner=source:src_0508f900ca445a84959d8d0d77a43579 block=evidence -->
- The agent exposes in-session commands including /install-github-action to set up a GitHub Action responding to issues, PRs, and CI failures, and /feedback for reporting bugs. [@claim:clm_13cfac17055b22d6ff1c860e7624c3b6bdb4c4d60a4a4ab49f5c20be4979b52f]
- Installation is documented for macOS/Linux via a curl-piped shell script, Windows via a PowerShell one-liner, plus Homebrew (jetbrains-junie/junie tap) and npm (@jetbrains/junie) alternatives. [@claim:clm_3e0822cebadf25f51cde902f568108db7998413710f5aa480a1f65ca6dcb9540]
- The evidence consists solely of README and LICENSE content, so runtime internals such as architecture, memory, or tool-permission behavior cannot be verified from this snapshot. [@claim:clm_6c8399a15eb7d1571d8ff6709a9f6ebf62958413ef5eff547876b0dafd2b860d]
- The repository is the public home of JetBrains' Junie CLI, with links to official docs, a Discord community, and a GitHub issue tracker for bug reports; use is governed by the JetBrains AI Service Terms of Service. [@claim:clm_9accc951c04c6475220f49fd35f46f81dd2671e3a4627fab8387fcf17602d850]
- A specific build of a channel can be pinned with --use-version (e.g. junie --eap --use-version=122.1), and a plain junie invocation afterwards still launches and auto-updates the default channel. [@claim:clm_b810501065a13dc04264ee8942757e0a962be89957b0c9aca0675b6e05563757]
- Authentication options include JetBrains Account OAuth, a Junie API key, or bring-your-own-key with model providers Anthropic, OpenAI, Google, xAI, OpenRouter, or Copilot. [@claim:clm_c746fbc9ca43bda4a0f26118284ac50daee2ae54dbb8b52b65cea0e28fc86ccf]
- Junie is described as an LLM-agnostic coding agent by JetBrains that runs in the terminal, integrates with IDEs and CI/CD pipelines, and takes natural-language tasks such as fixing bugs, implementing features, or reviewing PRs. [@claim:clm_e47d15145e5dba730a31448a5612cc3bfb93c904fb9a4ebbb07cd47c2a8cb9a1]
- The CLI supports launching a different update channel for a single run via flags like --eap, --nightly, --experimental, --release, or the explicit --channel form, without changing the installed default. [@claim:clm_eebaaef744dd83b8bb93e73e66222d0924e672284bbc0eb3d430cb4ce6d720d2]
<!-- rcw:end owner=source:src_0508f900ca445a84959d8d0d77a43579 block=evidence -->

## Researcher notes

