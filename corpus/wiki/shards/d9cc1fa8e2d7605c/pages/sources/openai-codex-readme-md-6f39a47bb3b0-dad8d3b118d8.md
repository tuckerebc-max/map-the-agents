---
access: public
aliases: []
claim_ids:
- clm_04115f1de140056c833e22ab498342411f9de61ca60aa63e2968b59a4ade8bd1
- clm_1a4f339e0210a86bc4e23b93d223caaca7ad2520bcded444a04237244e5f46a5
- clm_7a850c1df144fadce442e2744c5c922febb1dc34891c4f7f157a06cf82e766c2
- clm_8dd0b86d8f1e4d8a4df8ee6f1e48a4dbc79b588753a1de38e54b0f0aa69ff945
- clm_b81ae7fa3f3152a9d6025f167edc84cdfad7f682e8498cea7be248faf9102608
- clm_c0d9169e44929b3b0cf7c5e748c6caef777c8e51f27820ae3172a39da74730a2
maturity: draft
page_id: pg_028f779f0ebf52ff99f2dad8d3b118d8
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_806a6b761aaa59af916db2c7c2826a7c
title: openai/codex/README.md @ 6f39a47bb3b0
updated_at: '2026-09-14T02:25:53Z'
---

# openai/codex/README.md @ 6f39a47bb3b0

<!-- rcw:begin owner=source:src_806a6b761aaa59af916db2c7c2826a7c block=evidence -->
- On Mac/Linux the CLI installs via a curl-piped shell script, and on Windows via a PowerShell one-liner fetching install.ps1. [@claim:clm_04115f1de140056c833e22ab498342411f9de61ca60aa63e2968b59a4ade8bd1]
- Codex CLI can also be installed through npm (@openai/codex) and Homebrew (brew install --cask codex), or by downloading platform binaries from GitHub Releases. [@claim:clm_1a4f339e0210a86bc4e23b93d223caaca7ad2520bcded444a04237244e5f46a5]
- Standalone installers default to downloads from releases.openai.com/codex and fall back to GitHub Releases; setting CODEX_INSTALLER_USE_RELEASES_OPENAI_COM=false forces GitHub Releases. [@claim:clm_7a850c1df144fadce442e2744c5c922febb1dc34891c4f7f157a06cf82e766c2]
- Authentication supports signing in with a ChatGPT account (recommended for Plus/Pro/Business/Edu/Enterprise plans) or, with extra setup, an API key. [@claim:clm_8dd0b86d8f1e4d8a4df8ee6f1e48a4dbc79b588753a1de38e54b0f0aa69ff945]
- The repository is Apache-2.0 licensed and links to external docs for configuration, sandboxing/approvals, execution policy, skills, and AGENTS.md. [@claim:clm_b81ae7fa3f3152a9d6025f167edc84cdfad7f682e8498cea7be248faf9102608]
- Codex CLI is a local coding agent from OpenAI, started by running the `codex` command; a desktop app experience is available via `codex app`. [@claim:clm_c0d9169e44929b3b0cf7c5e748c6caef777c8e51f27820ae3172a39da74730a2]
<!-- rcw:end owner=source:src_806a6b761aaa59af916db2c7c2826a7c block=evidence -->

## Researcher notes

