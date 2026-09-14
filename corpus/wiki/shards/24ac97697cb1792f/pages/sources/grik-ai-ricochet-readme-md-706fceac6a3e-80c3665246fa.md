---
access: public
aliases: []
claim_ids:
- clm_078330f28e7410f6908500c87f755d26de4d59827296345a2c3008b8e4a351c0
- clm_0b0ae4b3c99535b8976d2839ba92e14829853e7af45375eb4a9637cc651ae8e8
- clm_347199340dc2c43582aee47fbd0294ce425b754c1da3cbc74691653ff4da9614
- clm_3a8048a848e542bdc34ac71e4c50cea43705d615271cc7df34d67fcfff6130a7
- clm_413cfbde2f47ca6ea5380a5f5161e8fdd308a91f52df3bf080aaa31c3151468f
- clm_48f291abf0729656f8504180be7892a3990f756be176a0954151e4f63b5700e8
- clm_6e6093a7e4607f3112db51914fce343730c6de76e3481b7287ef80b388d44e37
- clm_834814f022f9026f4e6f06c8659ed538a4420bab2a98b0b4ab10f69dd639d181
- clm_8de9d65171db9bfad9fa1d6ecef71a173ebba0d20645aba5c8757c9311f4487b
- clm_ead285506ba680e3171df101134a24d06cb3c80fcf8a9a477ef343ae7682f146
maturity: draft
page_id: pg_488dec05892859c08bbc80c3665246fa
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_053f820cadf3554c817e7e97bbc05ab2
title: Grik-ai/ricochet/README.md @ 706fceac6a3e
updated_at: '2026-09-14T01:52:28Z'
---

# Grik-ai/ricochet/README.md @ 706fceac6a3e

<!-- rcw:begin owner=source:src_053f820cadf3554c817e7e97bbc05ab2 block=evidence -->
- Ricochet is described as an open-source AI coding agent for VS Code-compatible editors and the terminal, letting users plan changes, inspect code, run tools, and review edits. [@claim:clm_078330f28e7410f6908500c87f755d26de4d59827296345a2c3008b8e4a351c0]
- External tools can be connected via MCP, project-specific instructions can be added as skills, and an optional Live Mode provides Telegram or Discord control for updates and responses away from the IDE. [@claim:clm_0b0ae4b3c99535b8976d2839ba92e14829853e7af45375eb4a9637cc651ae8e8]
- A native Go core handles planning, tool execution, provider routing, sessions, and terminal/TUI workflows, while the editor UI focuses on conversation, timeline, approvals, and checkpoints. [@claim:clm_347199340dc2c43582aee47fbd0294ce425b754c1da3cbc74691653ff4da9614]
- AI-generated file changes are surfaced for review before being applied, and task-level workspace checkpoints can be restored or compared. [@claim:clm_3a8048a848e542bdc34ac71e4c50cea43705d615271cc7df34d67fcfff6130a7]
- Model access supports Grik hosted subscription models or BYOK providers including OpenRouter, OpenAI-compatible APIs, Anthropic, OpenAI, Mistral, DeepSeek, Z.AI, xAI, and MiniMax. [@claim:clm_413cfbde2f47ca6ea5380a5f5161e8fdd308a91f52df3bf080aaa31c3151468f]
- The product ships as a VS Code Marketplace extension (grik.ricochet) and also offers a CLI/TUI mode for terminal use. [@claim:clm_48f291abf0729656f8504180be7892a3990f756be176a0954151e4f63b5700e8]
- The agent can read files, propose edits, and run commands in the workspace; permissions, approvals, checkpoints, and pending-change review are described as safety controls but explicitly not a complete sandbox. [@claim:clm_6e6093a7e4607f3112db51914fce343730c6de76e3481b7287ef80b388d44e37]
- Repository development practice: contributors build with ./scripts/build-all.sh and run focused checks including go test ./... in core, npm test/build in webview and extension-vscode, and scripts/check-public-hygiene.sh. [@claim:clm_834814f022f9026f4e6f06c8659ed538a4420bab2a98b0b4ab10f69dd639d181]
- The project is maintained by Igor Pryimak with decisions made via community consensus on GitHub Issues, and is licensed under Apache 2.0. [@claim:clm_8de9d65171db9bfad9fa1d6ecef71a173ebba0d20645aba5c8757c9311f4487b]
- The public provider catalog lives at core/config/providers.yaml and contains model metadata and environment-variable placeholders such as key: "${OPENROUTER_API_KEY}". [@claim:clm_ead285506ba680e3171df101134a24d06cb3c80fcf8a9a477ef343ae7682f146]
<!-- rcw:end owner=source:src_053f820cadf3554c817e7e97bbc05ab2 block=evidence -->

## Researcher notes

