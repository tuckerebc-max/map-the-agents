# 777genius/agent-teams-ai -- full detail

[Back to orientation](agent-teams-ai.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/777genius/agent-teams-ai/43764e1df31fccb3a8ba793e7d8637af15aa10ea/771d7e3404fa9a61.json](../../../wiki/dossiers/777genius/agent-teams-ai/43764e1df31fccb3a8ba793e7d8637af15aa10ea/771d7e3404fa9a61.json)

## specifications (1 claim(s))

- [observation/documented] The product is described as an orchestration layer for AI agent teams spanning Claude Code, Codex, OpenCode, Cursor, SuperGrok, GitHub Copilot, Z.AI, MiniMax, and Kiro. -- evidence: [README.md#L203-L203](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L203-L203) (`clm_2c1e08104efef08e123dc6fc8b1a5de6a51dc0b7e82378a74c2eeaf7ccdb9be7`)

## components (3 claim(s))

- [observation/documented] The app is an Electron desktop application distributed as macOS dmg (Apple Silicon and Intel), Windows exe, Linux AppImage and deb builds via GitHub releases. -- evidence: [README.md#L142-L178](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L142-L178) (`clm_3da0cf710bdde2e717099a99528eba652e255eacd4160b45906f28b446c9a425`)
- [observation/documented] Token analytics track input, output, cache, and reasoning usage across teams, agents, tasks, projects, models, runtimes, sessions, and runs, with monthly token or cost budgets and alerts at 80% and 100%. -- evidence: [README.md#L205-L218](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L205-L218) (`clm_131cd95d9d134e1b1e97d6bd9c8aeb2c830ab0e47a0cc3ccc559898bd4d7b640`)
- [observation/documented] An announcements/news feature is documented as implemented locally but not yet released: the desktop app fetches a static feed from agentteams.live, with auto-show rules (30-minute usage delay, newest-only, deduplication by ID) and no backend or user-data server storage. -- evidence: [docs/announcements-implementation-plan.md#L11-L22](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/docs/announcements-implementation-plan.md#L11-L22), [docs/announcements-implementation-plan.md#L3-L3](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/docs/announcements-implementation-plan.md#L3-L3), [docs/announcements-implementation-plan.md#L7-L7](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/docs/announcements-implementation-plan.md#L7-L7) (`clm_38b1fc8337eab2f2bfec44cb215ea6dd76b7456ab0387b0e28a214a2078ca13b`)

## design-choices (3 claim(s))

- [observation/documented] The app works through locally installed Claude/Codex/OpenCode CLIs rather than app-level API keys, and the FAQ states it does not upload project code to Agent Teams servers; there is no cloud backend for code storage. -- evidence: [docs/articles/agent-teams-opus-4-8.en.md#L42-L42](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/docs/articles/agent-teams-opus-4-8.en.md#L42-L42), [README.md#L320-L324](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L320-L324) (`clm_7a21a5b8c0ef86590ecf95b955ac66edf2bb090350e831aad85c9c7b07972d6c`)
- [observation/documented] Onboarding starts with a free model requiring no auth (no signup, API key, or card), with paid or account providers connected later; the app is free and open source. -- evidence: [README.md#L332-L336](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L332-L336), [README.md#L14-L16](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L14-L16), [README.md#L239-L239](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L239-L239) (`clm_d9c1ffe5730cfb319cc817276f49b7d99868ce5c39606346564fd9a0cebd46ff`)
- [observation/documented] At team launch, each teammate can run on the main checkout or in its own git worktree to avoid conflicts when running multiple teams, with branch rules configurable via the provisioning prompt. -- evidence: [README.md#L245-L245](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L245-L245), [README.md#L350-L354](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L350-L354) (`clm_248591bf787bab6dc15a69b9a85af9424882dd2be7082d8373294f63c82b64ac`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributor guardrails require pnpm (not npm/yarn), desktop Electron dev via pnpm dev, production files capped at 800 lines enforced by a source-file-size ratchet script, and testing only in sandbox/test projects rather than real user projects. -- evidence: [AGENT_CRITICAL_GUARDRAILS.md#L5-L18](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/AGENT_CRITICAL_GUARDRAILS.md#L5-L18) (`clm_f7d74c3ac48396dc63e810b191352dbcf0f4efee941bda0021d684da5a9f5c67`)
- [observation/documented] Repository development practice: an announcements e2e checklist defines a sandboxed fixture harness with isolated user-data roots, a loopback fixture server, CDP-based verification, and rules that evaluation is restricted to DOM inspection and sandbox setup. -- evidence: [docs/announcements-e2e-checklist.md#L7-L11](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/docs/announcements-e2e-checklist.md#L7-L11), [docs/announcements-e2e-checklist.md#L3-L3](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/docs/announcements-e2e-checklist.md#L3-L3), [docs/announcements-e2e-checklist.md#L13-L13](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/docs/announcements-e2e-checklist.md#L13-L13) (`clm_5410154359b6989398ee4402907c9eeb074e9843bcd1bd74e0003f882a34a84b`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The desktop app is the main product; a web version exists but is described as still in active development. -- evidence: [README.md#L314-L314](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L314-L314) (`clm_491df4c10f126c1cfa3360c0be04c5abfc858402352dba55c6d063f4074662c7`)
- [observation/documented] Tasks with detected code changes offer a diff view where users can accept, reject, or comment on individual code hunks, similar to Cursor's review flow. -- evidence: [README.md#L338-L342](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L338-L342) (`clm_628f9618cdb35d65b3cc14477071e4c6685a51e7d5698b0b1d3f4f5f9b00d1e2`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] Agents in a team message each other, create and manage shared tasks on a kanban board, review each other's work, and can communicate across different teams; multiple teams can run simultaneously and coordinate. -- evidence: [docs/articles/agent-teams-opus-4-8.en.md#L21-L21](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/docs/articles/agent-teams-opus-4-8.en.md#L21-L21), [README.md#L205-L218](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L205-L218), [README.md#L326-L330](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L326-L330) (`clm_8d3cd70a1aeb1242fb4a2e6c075ee6e75e2360abb434dfd3ab8290d05fdeda0b`)
- [observation/documented] A guarded, rate-limited nudge system sends short control messages to wake stalled agents, e.g. after a known rate-limit cooldown or when a teammate has not synced with its task or review. -- evidence: [README.md#L344-L348](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L344-L348) (`clm_e95694869f32c094078cc21b9091527e30a0c87e51c7772c1949a4f8ccdcffa0`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README's comparison scores for live collaboration are explicitly labeled qualitative editorial assessments of documented capabilities, not benchmark results. -- evidence: [README.md#L287-L287](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L287-L287), [README.md#L294-L294](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L294-L294) (`clm_5bbc5740814bf82a6a60cd5e79c898b5a8688e0d8a167d28833434d668ad2a08`)

## dependencies (1 claim(s))

- [observation/documented] No prerequisites are required: the app can detect installed Claude Code, Codex, and OpenCode runtimes, and other providers like Cursor, SuperGrok, GitHub Copilot, Z.AI, MiniMax, and Kiro can be connected from the UI. -- evidence: [README.md#L140-L140](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L140-L140) (`clm_6994c231848fbb2172c80b1b97675faa5b4744d94f07b9c6a18d837b373e2c4d`)

## limitations (1 claim(s))

- [observation/documented] Some RDP sessions expose virtual GPU drivers that can break Electron rendering; the documented workaround is launching with AGENT_TEAMS_DISABLE_GPU=1 to disable hardware acceleration. -- evidence: [README.md#L356-L360](https://github.com/777genius/agent-teams-ai/blob/43764e1df31fccb3a8ba793e7d8637af15aa10ea/README.md#L356-L360) (`clm_f19010cac70964705307ec512e8aab62db38517b8fab2015ec4a6f3d6cd311f3`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

