# tlbx-ai/tlbx -- full detail

[Back to orientation](tlbx.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/tlbx-ai/tlbx/f4e92650419094d42b7c9d8f8f516213ef415fbc/85ca0d4d0e4cf7cf.json](../../../wiki/dossiers/tlbx-ai/tlbx/f4e92650419094d42b7c9d8f8f516213ef415fbc/85ca0d4d0e4cf7cf.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The architecture splits roles: the host runs tlbx and the user's tools, mthost runs terminals, mtagenthost runs Agent Controller sessions, and a browser client connects over HTTPS/WebSocket. -- evidence: [README.md#L123-L129](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L123-L129), [README.md#L145-L149](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L145-L149) (`clm_9252486372b375db29ce38ff427a1fe9c5ccc1a044d0f5485154b8d1c2e29bfa`)

## design-choices (1 claim(s))

- [observation/documented] Sessions persist when the browser disconnects or the user switches devices, as long as the host stays awake and online; shutting down the host stops its processes. -- evidence: [README.md#L131-L131](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L131-L131), [README.md#L29-L29](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L29-L29) (`clm_50eae6673982c6e0184c32e1ae8d5aaa79174ed233e8f0dc56243092615d6fe2`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: AGENTS.md and CLAUDE.md instruct contributors that development happens on the dev branch, with main reserved for stable integration, and that release scripts (release-dev.ps1, promote.ps1, release.ps1) may only be run for the explicitly requested release path. -- evidence: [AGENTS.md#L19-L19](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/AGENTS.md#L19-L19), [AGENTS.md#L30-L43](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/AGENTS.md#L30-L43) (`clm_eff3b16b10d6ca0d9429af5368981f80b23ed47d4dbb275e241e339cd48e4a9e`)
- [observation/documented] Repository development practice: every release invocation must explicitly pass -TestCategories from a fixed set (assets, frontend, server, runtime, installers, dependencies, build, or all), and stable releases require all. -- evidence: [AGENTS.md#L8-L15](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/AGENTS.md#L8-L15) (`clm_4a040a0d43c9e8b0ae23ab2a35ce15d44df1c8742f22fd40fb3879c1724256c4`)
- [observation/documented] Repository development practice: contributors are told to keep major data-processing, protocol and business logic in C# while keeping the TypeScript frontend lean, to remove superseded dead code in the same change, and to use domReconcile.ts for keyed UI lists so content-only updates preserve DOM node identity. -- evidence: [AGENTS.md#L21-L26](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/AGENTS.md#L21-L26) (`clm_32719d1269b5bf2ecbc28fd410d5461f0438046c0ff1d7b24976ffc53870ab12`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] tlbx offers two session types: a Terminal Session rendering the user's terminal with output retained on the host, and an Agent Controller Session rendering a conversation view with tool calls, code changes, questions and approval buttons. -- evidence: [README.md#L57-L60](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L57-L60) (`clm_7efce07b686bdfdbeee3cb8cbd2d58ec5753c1377284e43d7ddfe34b5fe6befd`)
- [observation/documented] Agent Controller has built-in launch options for Codex, Grok Build, OpenCode, Gemini CLI and GitHub Copilot CLI, and compatible ACP agents can be added via acp-agents.json; Claude Code runs in a normal terminal session. -- evidence: [README.md#L84-L84](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L84-L84) (`clm_196dec3902e59da9df7a6975b5b13de182fbbe9ddf316f9b7450781f549e3766`)
- [observation/documented] The product supports PowerShell, bash and zsh plus full-screen terminal apps like btop, vim, lazygit and database shells, with sessions splittable into panes. -- evidence: [README.md#L66-L66](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L66-L66) (`clm_a8448f753ab7c7b10680b49135ea52f4c32ebf804a613ee3b31d567a8cf54c83`)
- [observation/documented] Users can paste images with Ctrl+V/Cmd+V so the terminal receives the file path, use multiline prompts with saved drafts, attachments and scheduled follow-ups, and resend prior input via an Alt+H history view. -- evidence: [README.md#L76-L82](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L76-L82) (`clm_61595994a539a0c0d6e5873f9b7fcbee5e5c7cb785cfc78f571f4086aa524a30`)
- [observation/documented] A quick local trial is available by running npx @tlbx-ai/midterm, which downloads the stable native binary and opens a browser; the npm launcher may lag behind native releases. -- evidence: [README.md#L141-L141](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L141-L141), [README.md#L137-L139](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L137-L139) (`clm_35aee09d8a10481c4da6ce834dfc37f911c682ab0d5dced9b198df5a13d6bbf8`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The mt helpers let agents send prompts, read terminal output, and inspect or control the app preview within the workspace. -- evidence: [README.md#L76-L82](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L76-L82) (`clm_4c4c95c59e05b81682e111a4549b2a56ae361d1983e23653ceeec285cf36b34e`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] tlbx is built with .NET 10 Native AOT, TypeScript and xterm.js. -- evidence: [README.md#L151-L151](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L151-L151) (`clm_6eb01da92ed8c289eb8aa243478eb72d1531a033664ede5bcc3fb17e0e3ca38e`)
- [observation/documented] Installation is via a curl/piped bash script on macOS/Linux or an irm/iex PowerShell command on Windows, with the installer setting up password-protected HTTPS and updates. -- evidence: [README.md#L102-L104](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L102-L104), [README.md#L96-L98](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L96-L98), [README.md#L92-L92](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L92-L92) (`clm_8af2698e15b91569f069a37393bbeb558b390cc5f4ee7724903b8cbf70f37939`)

## limitations (1 claim(s))

- [observation/documented] The README notes that repositories, credentials and processes stay on the host, but coding agents may send data to their model provider according to their own configuration and terms. -- evidence: [README.md#L118-L119](https://github.com/tlbx-ai/tlbx/blob/f4e92650419094d42b7c9d8f8f516213ef415fbc/README.md#L118-L119) (`clm_dee109a0d33b13718bd2e46ab30aea055c835a17715cda2ee17f7a39dfef8384`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

