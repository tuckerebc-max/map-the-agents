---
access: public
aliases: []
claim_ids:
- clm_21735609f7c09dfc9e6248cfd20a40acde943779b9e55ce09338c54a7bd52b6a
- clm_51f068d7ff7e96dfac712ab7556441697e9100da1fc38e99119e81ffd7aa08b7
- clm_57fccd7aa1f39faf94b4d2a0343c00eb5c377f5e8608898593e9efce818a2afa
- clm_683238a7e6f7bd6a2f8d665581adb9bd6667c8d0f1be4e5c0f29d56bb57c233b
- clm_6df7c027fbc627cdd89d350643de5f59c319f85be95331bc0126b5bd99f26f12
- clm_7f1ca87a67f8f38107fe4dc17f40552a69c818cf9d5c19cdbeb50b45842b929e
- clm_858ee248c94c03ff299f784e6055eecbe63e31232a5601d22a135b89f5192f09
- clm_a38a80c8d755af0b21b6994f25d266411d4b0ccf1c36cad1deb28eff798fbcd2
- clm_b6b3ffc886dbf4153a1c33c16b39888d05542927fd418cd9e39ed7283894562c
- clm_b92dd9cb97c61d2f931ca91890f57e2c674f7669593ccb09238f54715ea292de
- clm_c430cce67ac5dfb5d3d8fe15af8c438cf6ed71b41416a81b3407163f4ecf20d9
- clm_cc5acf0bca626beae7a3848c6b0011114324cf0b2c625bd74662f59503c64ed4
- clm_ee9c34132fb7cd3faaab7213c9bd19ebd165621de536e281d07e8a6d38dfd274
maturity: draft
page_id: pg_d4b2f18028b6577090970984de2611e5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e367bbd10c0f5ad88d1763a2835bed74
title: OpenSource03/harnss/README.md @ dc1dfd8a33ca
updated_at: '2026-09-14T02:27:28Z'
---

# OpenSource03/harnss/README.md @ dc1dfd8a33ca

<!-- rcw:begin owner=source:src_e367bbd10c0f5ad88d1763a2835bed74 block=evidence -->
- Voice input is supported via native macOS dictation or an on-device Whisper model requiring no API key, alongside configurable OS notifications for approvals, permission prompts, and session events. [@claim:clm_21735609f7c09dfc9e6248cfd20a40acde943779b9e55ce09338c54a7bd52b6a]
- Running Claude Code requires a Claude account (subscription or API key); Codex requires the Codex CLI in PATH plus an OpenAI API key or ChatGPT account; ACP agents have agent-specific requirements. [@claim:clm_51f068d7ff7e96dfac712ab7556441697e9100da1fc38e99119e81ffd7aa08b7]
- Repository development practice: contributors should fork the repo, create a feature branch, follow conventions in CLAUDE.md, test with pnpm dev, and open a pull request; local development uses pnpm install and pnpm dev. [@claim:clm_57fccd7aa1f39faf94b4d2a0343c00eb5c377f5e8608898593e9efce818a2afa]
- Pre-built release binaries are currently unsigned, requiring macOS users to bypass Gatekeeper via right-click Open and Windows users to click through Defender warnings. [@claim:clm_683238a7e6f7bd6a2f8d665581adb9bd6667c8d0f1be4e5c0f29d56bb57c233b]
- Built-in panels include a multi-tab PTY terminal backed by native shell processes, an embedded browser, git staging/commit/push with worktree support, and AI-generated commit messages from the staged diff. [@claim:clm_6df7c027fbc627cdd89d350643de5f59c319f85be95331bc0126b5bd99f26f12]
- Sessions, history, and panel settings are scoped per project; projects map to disk folders and can be grouped into named Spaces with custom icons and colors. [@claim:clm_7f1ca87a67f8f38107fe4dc17f40552a69c818cf9d5c19cdbeb50b45842b929e]
- Harnss is a cross-platform desktop app providing a single interface to run, manage, and switch between AI coding agents including Claude Code, Codex, and ACP-compatible agents. [@claim:clm_858ee248c94c03ff299f784e6055eecbe63e31232a5601d22a135b89f5192f09]
- MCP servers can be connected per project over stdio, SSE, or HTTP transports, with in-app OAuth handling and token persistence across sessions. [@claim:clm_a38a80c8d755af0b21b6994f25d266411d4b0ccf1c36cad1deb28eff798fbcd2]
- The README states Harnss is in early development with issues to be expected, and a large rewrite toward a more production-ready app is pending. [@claim:clm_b6b3ffc886dbf4153a1c33c16b39888d05542927fd418cd9e39ed7283894562c]
- The product offers three permission levels (Ask First, Accept Edits, Allow All) plus a plan mode where the agent drafts a plan before changes; modes can be switched mid-session without losing context. [@claim:clm_b92dd9cb97c61d2f931ca91890f57e2c674f7669593ccb09238f54715ea292de]
- An Agent Store lets users browse and install agents from the ACP community registry, or define custom agents with command, arguments, environment variables, and icon via Settings. [@claim:clm_c430cce67ac5dfb5d3d8fe15af8c438cf6ed71b41416a81b3407163f4ecf20d9]
- The app supports three execution engines: Claude Code via the Anthropic Agent SDK, Codex via a JSON-RPC app-server, and ACP agents via the Agent Client Protocol. [@claim:clm_cc5acf0bca626beae7a3848c6b0011114324cf0b2c625bd74662f59503c64ed4]
- Tool calls render as interactive cards with word-level diffs, syntax highlighting, inline bash output, nested subagent progress tracking, and a per-turn Changes panel. [@claim:clm_ee9c34132fb7cd3faaab7213c9bd19ebd165621de536e281d07e8a6d38dfd274]
<!-- rcw:end owner=source:src_e367bbd10c0f5ad88d1763a2835bed74 block=evidence -->

## Researcher notes

