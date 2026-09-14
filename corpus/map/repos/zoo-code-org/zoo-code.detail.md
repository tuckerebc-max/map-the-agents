# zoo-code-org/zoo-code -- full detail

[Back to orientation](zoo-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/zoo-code-org/zoo-code/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/2a1006e3c37b084d.json](../../../wiki/dossiers/zoo-code-org/zoo-code/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/2a1006e3c37b084d.json)

## specifications (2 claim(s))

- [observation/documented] The product is described as an AI-powered dev team inside the editor that can generate and refactor code, write documentation, answer codebase questions, automate tasks, and use MCP servers. -- evidence: [README.md#L83-L89](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L83-L89), [README.md#L14-L14](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L14-L14) (`clm_f0bc719b51a6cc4d8cf651e6d7eff4be25db7c6744f706fb35dac3bd80e84735`)
- [observation/documented] Zoo Code continues development of Roo Code after the Roo team wound down, with a core team of former Roo contributors planning model updates, bug fixes, and features. -- evidence: [README.md#L18-L30](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L18-L30) (`clm_f4fff1acc6c3d05064011205cbb518bb9045cfe810580aeb275958d2f4ca817b`)

## components (1 claim(s))

- [observation/documented] Additions over Roo Code include Semble semantic code search, stronger orchestrator delegation with parent/child task recovery, and a Destructive Command Guard that blocks dangerous commands during autonomous runs. -- evidence: [README.md#L41-L47](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L41-L47) (`clm_ea1b08c665096b9a098a507087758e8f3dc252f275a0ba4905fce4f3ac5d7b47`)

## design-choices (3 claim(s))

- [observation/documented] The assistant operates through modes: Code, Architect, Ask, Debug, and user-defined Custom Modes for specialized team workflows. -- evidence: [README.md#L95-L99](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L95-L99), [README.md#L83-L89](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L83-L89) (`clm_fd85ed7b6b3d99205c1a0f16c04e6a985ab953ba883efdc8a909df7d1d550203`)
- [observation/documented] Per the privacy policy, telemetry is enabled by default but can be opted out via settings, and users can run models locally to avoid sending data to third parties. -- evidence: [PRIVACY.md#L62-L65](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/PRIVACY.md#L62-L65) (`clm_a3a9f3c88d772abd158c512f923556f9f9a32649349928e3129f44e476843c09`)
- [observation/documented] In Zoo Code Cloud proxy mode, code and prompts transit Zoo Code servers only for forwarding to the upstream provider and are not stored; otherwise data goes directly to the chosen AI provider. -- evidence: [PRIVACY.md#L11-L52](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/PRIVACY.md#L11-L52) (`clm_830cd6e3f84c14e325d1986c8042ea17ec12ffa4249969b18bfbe7f60b1737dc`)

## workflows (6 claim(s))

- [observation/documented] Repository development practice: local setup uses pnpm install, the extension runs via VS Code F5 debugging with hot reload, and VSIX builds install through pnpm install:vsix or manual code --install-extension. -- evidence: [README.md#L144-L145](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L144-L145), [README.md#L141-L142](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L141-L142), [README.md#L129-L131](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L129-L131), [README.md#L174-L183](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L174-L183), [README.md#L151-L153](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L151-L153) (`clm_f0b4eaff9bfd61dfadafa779c03cc1c0b52b1c552efc8a99f4004fc631b0648e`)
- [observation/documented] Repository development practice: a bounded TypeScript model-check suite (pnpm lifecycle:model-check) runs six submodels covering task delegation, shared-store concurrency, provider handoff, cleanup, parser scoping, and completion persistence, and is the model-check entry point in the compile CI job. -- evidence: [docs/architecture/task-lifecycle-model.md#L3-L3](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/docs/architecture/task-lifecycle-model.md#L3-L3), [docs/architecture/task-lifecycle-model.md#L18-L18](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/docs/architecture/task-lifecycle-model.md#L18-L18), [docs/architecture/task-lifecycle-model.md#L11-L16](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/docs/architecture/task-lifecycle-model.md#L11-L16) (`clm_a8982545176872a3499638959b0012781a1268aadcceaea7be2a5b5acd031cc4`)
- [observation/documented] Repository development practice: the shared-store model tracks two known-unsafe witnesses as issue-keyed ratchets (#1469 stale completion after handoff, #1021 stale live-task save after abandonment), and CI fails if witnesses or landmarks change. -- evidence: [docs/architecture/task-lifecycle-model.md#L70-L71](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/docs/architecture/task-lifecycle-model.md#L70-L71), [docs/architecture/task-lifecycle-model.md#L73-L73](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/docs/architecture/task-lifecycle-model.md#L73-L73), [docs/architecture/task-lifecycle-model.md#L68-L68](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/docs/architecture/task-lifecycle-model.md#L68-L68) (`clm_ee205600f0cee36ceb43bb435d30b7b7ab404feb16bcb0f81a5796df5306be30`)
- [observation/documented] Repository development practice: progress notes record cherry-picking Roo PRs in batches, deferring AI-SDK-entangled PRs, and validation with 5224 backend and 1267 UI tests passing plus clean type checks. -- evidence: [progress.txt#L27-L29](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/progress.txt#L27-L29), [progress.txt#L49-L52](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/progress.txt#L49-L52), [progress.txt#L7-L8](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/progress.txt#L7-L8) (`clm_14b2406e52ec55d8d0f3b0d6e0454dce5a554b8ec04e77050cca54f3f5c666d2`)
- [observation/documented] Repository development practice: versioning and publishing use changesets, with release notes in CHANGELOG.md. -- evidence: [README.md#L187-L188](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L187-L188) (`clm_8272559b96bd282f4815794baeaf08123f373f5b2718f05b1f4dd0eaf88072c4`)
- [observation/documented] Repository development practice: contributions are welcomed via CONTRIBUTING.md, and the project is licensed Apache 2.0. -- evidence: [README.md#L209-L210](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L209-L210), [README.md#L216-L216](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L216-L216) (`clm_2c8457b16ee28fa59f5b6aaae4738aac0d894c579030d0ac44ab5cd71ddc5bc7`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Zoo Code is distributed as a VS Code extension (a VS Code Marketplace badge and VSIX installation instructions appear in the README). -- evidence: [README.md#L1-L10](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L1-L10), [README.md#L174-L183](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L174-L183), [README.md#L149-L149](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L149-L149) (`clm_04840c07d9cfa1eecca629a280f5f98b562667278372bb5f8f40ec69e7de273d`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The README lists supported model families (Claude, GPT, Gemini, Kimi, GLM, Grok, MiniMax, and others) and providers including Zoo Gateway, Moonshot, Kimi Code, Kenari, Friendli, and OpenCode Go. -- evidence: [README.md#L41-L47](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L41-L47), [README.md#L51-L53](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L51-L53) (`clm_68d8c4ca74d8fbd7b7b3989ec690521379ec21ce61598ed9eda4edac72f2685c`)

## limitations (1 claim(s))

- [observation/documented] The README disclaimer states Zoo Code provides no warranties for its tools, models, or outputs, which are offered AS IS, and users assume all risks of use. -- evidence: [README.md#L194-L203](https://github.com/Zoo-Code-Org/Zoo-Code/blob/ba46d1f34a5be3eb7754e4a35bd638ab27287a9e/README.md#L194-L203) (`clm_723b955f8b99fd97ca4e420cd72e83fb35178aeb8641e91280ebc65061a1f74f`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

