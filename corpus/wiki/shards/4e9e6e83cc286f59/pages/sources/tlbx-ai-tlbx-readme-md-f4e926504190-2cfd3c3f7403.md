---
access: public
aliases: []
claim_ids:
- clm_196dec3902e59da9df7a6975b5b13de182fbbe9ddf316f9b7450781f549e3766
- clm_35aee09d8a10481c4da6ce834dfc37f911c682ab0d5dced9b198df5a13d6bbf8
- clm_4c4c95c59e05b81682e111a4549b2a56ae361d1983e23653ceeec285cf36b34e
- clm_50eae6673982c6e0184c32e1ae8d5aaa79174ed233e8f0dc56243092615d6fe2
- clm_61595994a539a0c0d6e5873f9b7fcbee5e5c7cb785cfc78f571f4086aa524a30
- clm_6eb01da92ed8c289eb8aa243478eb72d1531a033664ede5bcc3fb17e0e3ca38e
- clm_7efce07b686bdfdbeee3cb8cbd2d58ec5753c1377284e43d7ddfe34b5fe6befd
- clm_8af2698e15b91569f069a37393bbeb558b390cc5f4ee7724903b8cbf70f37939
- clm_9252486372b375db29ce38ff427a1fe9c5ccc1a044d0f5485154b8d1c2e29bfa
- clm_a8448f753ab7c7b10680b49135ea52f4c32ebf804a613ee3b31d567a8cf54c83
- clm_dee109a0d33b13718bd2e46ab30aea055c835a17715cda2ee17f7a39dfef8384
maturity: draft
page_id: pg_f79478d68c625eae909e2cfd3c3f7403
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a5ee5229cf6f5e658541fe4670e30c64
title: tlbx-ai/tlbx/README.md @ f4e926504190
updated_at: '2026-09-14T03:19:50Z'
---

# tlbx-ai/tlbx/README.md @ f4e926504190

<!-- rcw:begin owner=source:src_a5ee5229cf6f5e658541fe4670e30c64 block=evidence -->
- Agent Controller has built-in launch options for Codex, Grok Build, OpenCode, Gemini CLI and GitHub Copilot CLI, and compatible ACP agents can be added via acp-agents.json; Claude Code runs in a normal terminal session. [@claim:clm_196dec3902e59da9df7a6975b5b13de182fbbe9ddf316f9b7450781f549e3766]
- A quick local trial is available by running npx @tlbx-ai/midterm, which downloads the stable native binary and opens a browser; the npm launcher may lag behind native releases. [@claim:clm_35aee09d8a10481c4da6ce834dfc37f911c682ab0d5dced9b198df5a13d6bbf8]
- The mt helpers let agents send prompts, read terminal output, and inspect or control the app preview within the workspace. [@claim:clm_4c4c95c59e05b81682e111a4549b2a56ae361d1983e23653ceeec285cf36b34e]
- Sessions persist when the browser disconnects or the user switches devices, as long as the host stays awake and online; shutting down the host stops its processes. [@claim:clm_50eae6673982c6e0184c32e1ae8d5aaa79174ed233e8f0dc56243092615d6fe2]
- Users can paste images with Ctrl+V/Cmd+V so the terminal receives the file path, use multiline prompts with saved drafts, attachments and scheduled follow-ups, and resend prior input via an Alt+H history view. [@claim:clm_61595994a539a0c0d6e5873f9b7fcbee5e5c7cb785cfc78f571f4086aa524a30]
- tlbx is built with .NET 10 Native AOT, TypeScript and xterm.js. [@claim:clm_6eb01da92ed8c289eb8aa243478eb72d1531a033664ede5bcc3fb17e0e3ca38e]
- tlbx offers two session types: a Terminal Session rendering the user's terminal with output retained on the host, and an Agent Controller Session rendering a conversation view with tool calls, code changes, questions and approval buttons. [@claim:clm_7efce07b686bdfdbeee3cb8cbd2d58ec5753c1377284e43d7ddfe34b5fe6befd]
- Installation is via a curl/piped bash script on macOS/Linux or an irm/iex PowerShell command on Windows, with the installer setting up password-protected HTTPS and updates. [@claim:clm_8af2698e15b91569f069a37393bbeb558b390cc5f4ee7724903b8cbf70f37939]
- The architecture splits roles: the host runs tlbx and the user's tools, mthost runs terminals, mtagenthost runs Agent Controller sessions, and a browser client connects over HTTPS/WebSocket. [@claim:clm_9252486372b375db29ce38ff427a1fe9c5ccc1a044d0f5485154b8d1c2e29bfa]
- The product supports PowerShell, bash and zsh plus full-screen terminal apps like btop, vim, lazygit and database shells, with sessions splittable into panes. [@claim:clm_a8448f753ab7c7b10680b49135ea52f4c32ebf804a613ee3b31d567a8cf54c83]
- The README notes that repositories, credentials and processes stay on the host, but coding agents may send data to their model provider according to their own configuration and terms. [@claim:clm_dee109a0d33b13718bd2e46ab30aea055c835a17715cda2ee17f7a39dfef8384]
<!-- rcw:end owner=source:src_a5ee5229cf6f5e658541fe4670e30c64 block=evidence -->

## Researcher notes

