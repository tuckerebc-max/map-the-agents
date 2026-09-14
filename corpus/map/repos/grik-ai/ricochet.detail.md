# grik-ai/ricochet -- full detail

[Back to orientation](ricochet.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/grik-ai/ricochet/706fceac6a3e558c40dba66a4795f357f4689fe0/b279f561c72e01dd.json](../../../wiki/dossiers/grik-ai/ricochet/706fceac6a3e558c40dba66a4795f357f4689fe0/b279f561c72e01dd.json)

## specifications (1 claim(s))

- [observation/documented] Ricochet is described as an open-source AI coding agent for VS Code-compatible editors and the terminal, letting users plan changes, inspect code, run tools, and review edits. -- evidence: [README.md#L7-L10](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L7-L10) (`clm_078330f28e7410f6908500c87f755d26de4d59827296345a2c3008b8e4a351c0`)

## components (1 claim(s))

- [observation/documented] A native Go core handles planning, tool execution, provider routing, sessions, and terminal/TUI workflows, while the editor UI focuses on conversation, timeline, approvals, and checkpoints. -- evidence: [README.md#L30-L30](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L30-L30) (`clm_347199340dc2c43582aee47fbd0294ce425b754c1da3cbc74691653ff4da9614`)

## design-choices (1 claim(s))

- [observation/documented] AI-generated file changes are surfaced for review before being applied, and task-level workspace checkpoints can be restored or compared. -- evidence: [README.md#L36-L45](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L36-L45) (`clm_3a8048a848e542bdc34ac71e4c50cea43705d615271cc7df34d67fcfff6130a7`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: contributors build with ./scripts/build-all.sh and run focused checks including go test ./... in core, npm test/build in webview and extension-vscode, and scripts/check-public-hygiene.sh. -- evidence: [CONTRIBUTING.md#L23-L26](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/CONTRIBUTING.md#L23-L26), [CONTRIBUTING.md#L19-L21](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/CONTRIBUTING.md#L19-L21), [CONTRIBUTING.md#L30-L32](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/CONTRIBUTING.md#L30-L32), [README.md#L110-L112](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L110-L112), [CONTRIBUTING.md#L9-L11](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/CONTRIBUTING.md#L9-L11), [README.md#L116-L121](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L116-L121), [CONTRIBUTING.md#L15-L17](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/CONTRIBUTING.md#L15-L17) (`clm_834814f022f9026f4e6f06c8659ed538a4420bab2a98b0b4ab10f69dd639d181`)
- [observation/documented] Repository development practice: PRs should stay focused, include tests for behavior changes, avoid committing generated outputs or local secrets, and keep public docs user-facing. -- evidence: [CONTRIBUTING.md#L36-L39](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/CONTRIBUTING.md#L36-L39) (`clm_dfb76da436a298f9c29c0eed34438352c4623c526651cf381ca496d58e3588a1`)
- [observation/documented] Repository development practice: a Chat Dev Lab supports webview UI iteration via Vite hot reload (npm run dev:chat-lab) with a fake VS Code API and fixture-driven dev panel, plus a ricochet.webview.devServerUrl setting for sidebar hot reload. -- evidence: [docs/chat-dev-lab.md#L16-L20](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/docs/chat-dev-lab.md#L16-L20), [docs/chat-dev-lab.md#L7-L10](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/docs/chat-dev-lab.md#L7-L10), [docs/chat-dev-lab.md#L14-L14](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/docs/chat-dev-lab.md#L14-L14), [docs/chat-dev-lab.md#L39-L39](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/docs/chat-dev-lab.md#L39-L39), [docs/chat-dev-lab.md#L33-L37](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/docs/chat-dev-lab.md#L33-L37) (`clm_327649bd972f0e9d665cf86991a8879b8b15bb45e28d7dfe2fd3a782f73a9a2b`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product ships as a VS Code Marketplace extension (grik.ricochet) and also offers a CLI/TUI mode for terminal use. -- evidence: [README.md#L36-L45](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L36-L45), [README.md#L51-L53](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L51-L53), [README.md#L12-L18](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L12-L18) (`clm_48f291abf0729656f8504180be7892a3990f756be176a0954151e4f63b5700e8`)
- [observation/documented] External tools can be connected via MCP, project-specific instructions can be added as skills, and an optional Live Mode provides Telegram or Discord control for updates and responses away from the IDE. -- evidence: [README.md#L36-L45](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L36-L45) (`clm_0b0ae4b3c99535b8976d2839ba92e14829853e7af45375eb4a9637cc651ae8e8`)
- [observation/documented] The public provider catalog lives at core/config/providers.yaml and contains model metadata and environment-variable placeholders such as key: "${OPENROUTER_API_KEY}". -- evidence: [README.md#L91-L91](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L91-L91), [docs/providers.md#L17-L19](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/docs/providers.md#L17-L19) (`clm_ead285506ba680e3171df101134a24d06cb3c80fcf8a9a477ef343ae7682f146`)

## memory-state (1 claim(s))

- [observation/documented] BYOK provider keys are stored locally (user settings, OS secret store, or environment variables), and the Go core resolves catalog placeholders from the user's environment or local configuration at runtime. -- evidence: [docs/providers.md#L21-L21](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/docs/providers.md#L21-L21), [docs/providers.md#L13-L13](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/docs/providers.md#L13-L13) (`clm_ae259f0f6629bb262002a103b911fce02ebdd158956a6207286d5e8d18681726`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The agent can read files, propose edits, and run commands in the workspace; permissions, approvals, checkpoints, and pending-change review are described as safety controls but explicitly not a complete sandbox. -- evidence: [README.md#L97-L97](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L97-L97), [SECURITY.md#L7-L11](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/SECURITY.md#L7-L11) (`clm_6e6093a7e4607f3112db51914fce343730c6de76e3481b7287ef80b388d44e37`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Model access supports Grik hosted subscription models or BYOK providers including OpenRouter, OpenAI-compatible APIs, Anthropic, OpenAI, Mistral, DeepSeek, Z.AI, xAI, and MiniMax. -- evidence: [README.md#L36-L45](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L36-L45), [README.md#L88-L89](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L88-L89) (`clm_413cfbde2f47ca6ea5380a5f5161e8fdd308a91f52df3bf080aaa31c3151468f`)

## limitations (1 claim(s))

- [observation/documented] SECURITY.md's 'Not A Security Boundary' section lists model output text, markdown rendering alone, checkpoint existence, UI permission labels, and local config files holding secrets. -- evidence: [SECURITY.md#L46-L50](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/SECURITY.md#L46-L50) (`clm_515482ce6a93ea180337fa684440ba60602dadf797d1ddf47dd3c4ddb3de00f5`)

## relevance (1 claim(s))

- [observation/documented] The project is maintained by Igor Pryimak with decisions made via community consensus on GitHub Issues, and is licensed under Apache 2.0. -- evidence: [GOVERNANCE.md#L3-L3](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/GOVERNANCE.md#L3-L3), [README.md#L131-L131](https://github.com/Grik-ai/ricochet/blob/706fceac6a3e558c40dba66a4795f357f4689fe0/README.md#L131-L131) (`clm_8de9d65171db9bfad9fa1d6ecef71a173ebba0d20645aba5c8757c9311f4487b`)

