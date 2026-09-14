# neovateai/neovate-code -- full detail

[Back to orientation](neovate-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/neovateai/neovate-code/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/d399a326a058e2ba.json](../../../wiki/dossiers/neovateai/neovate-code/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/d399a326a058e2ba.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (4 claim(s))

- [observation/documented] The focus handler updates window focus state via useAppStore.getState().setWindowFocused, setting true for '[I' (focus gained) and false for '[O' (focus lost). -- evidence: [docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L50-L62](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L50-L62) (`clm_fddc79e3507044a1182c9e093186a43a59186cc79f8ece553c42bc7f8f03b83c`)
- [observation/documented] The planned BackgroundTaskManager stores tasks in a Map with fields id, command, pid, optional pgid, status (running/completed/killed/failed), createdAt, output, and exitCode, generating ids prefixed 'task_'. -- evidence: [docs/designs/2025-01-27-bash-background-execution.md#L101-L102](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L101-L102), [docs/designs/2025-01-27-bash-background-execution.md#L104-L118](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L104-L118), [docs/designs/2025-01-27-bash-background-execution.md#L84-L93](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L84-L93) (`clm_0ce59c42ae9eb4d649d02ef1a15400170ec5236e0c4612d006d3b1da880fb160`)
- [observation/documented] The planned killTask uses taskkill on Windows; otherwise it signals the process group with SIGTERM, then SIGKILL after 200ms if still running, falling back to killing the pid directly. -- evidence: [docs/designs/2025-01-27-bash-background-execution.md#L206-L220](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L206-L220), [docs/designs/2025-01-27-bash-background-execution.md#L204-L204](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L204-L204) (`clm_fc2956f870a29f84b57798055cc5fa63e7450eb920f6e4f6548956a723ea6134`)
- [observation/documented] Background detection runs a command in background if user-requested, or if elapsed time exceeds a 2000ms threshold with output and the command root matches a dev-command list (npm, pnpm, yarn, node, python, go, cargo, docker, vite, jest, pytest, and others). -- evidence: [docs/designs/2025-01-27-bash-background-execution.md#L367-L383](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L367-L383), [docs/designs/2025-01-27-bash-background-execution.md#L396-L404](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L396-L404), [docs/designs/2025-01-27-bash-background-execution.md#L415-L417](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L415-L417), [docs/designs/2025-01-27-bash-background-execution.md#L406-L408](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L406-L408), [docs/designs/2025-01-27-bash-background-execution.md#L385-L385](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L385-L385) (`clm_ae7cc88cc46ec8df800819b1cbc2174a01476345df240f1722a1aeb88cb60b23`)

## design-choices (3 claim(s))

- [observation/documented] A design doc dated 2025-01-26 addresses terminal focus escape sequences ([I]/[O]) appearing as literal text in the chat input when modals are shown, because Ink strips the escape prefix. -- evidence: [docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L7-L7](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L7-L7), [docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L9-L9](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L9-L9) (`clm_c00023d751c7808ad2a8828b7712b7ae498a1f0ef28dae622d6a9fecbbcb21da`)
- [observation/documented] The chosen fix is a global always-active useInput hook in ChatInput.tsx to intercept focus events, with a simplified skip-handler kept in TextInput as a safety net. -- evidence: [docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L46-L46](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L46-L46), [docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L42-L42](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L42-L42) (`clm_0d97a3f036e85b5246bf559cb00efabd330d74375f7b294d7d77a2af2e601030`)
- [observation/documented] A 2025-01-27 plan proposes background bash execution so the LLM can monitor and control long-running development tasks, extending the bash tool with a BackgroundTaskManager plus bash_output and kill_bash tools. -- evidence: [docs/designs/2025-01-27-bash-background-execution.md#L5-L5](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L5-L5), [docs/designs/2025-01-27-bash-background-execution.md#L3-L3](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L3-L3) (`clm_b6ef33a419da9b6a4754696182b48949da68678461ff6d67210f042d8e355858`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The plan adds a run_in_background boolean parameter to the bash tool and documents that dev-pattern commands auto-move to background after 2 seconds if producing output, returning a task_id for bash_output and kill_bash. -- evidence: [docs/designs/2025-01-27-bash-background-execution.md#L456-L472](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L456-L472), [docs/designs/2025-01-27-bash-background-execution.md#L481-L485](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L481-L485) (`clm_cbf9163feda76f637f22834f0145cccd52552d5ab51967614e85160c15d985a1`)
- [observation/documented] The planned bash_output tool takes a task_id and returns the task's command, status, PID, creation time, accumulated output, and exit code when set. -- evidence: [docs/designs/2025-01-27-bash-background-execution.md#L802-L810](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L802-L810), [docs/designs/2025-01-27-bash-background-execution.md#L812-L814](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L812-L814), [docs/designs/2025-01-27-bash-background-execution.md#L778-L800](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L778-L800) (`clm_7daba09d4c9d196c92e3a6214a8fbb587eeba46a6dd793b3e26ef45728990dd1`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] In the planned design, bash_output requires no approval (category 'read', needsApproval returns false), while kill_bash refuses to terminate tasks whose status is not 'running'. -- evidence: [docs/designs/2025-01-27-bash-background-execution.md#L892-L897](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L892-L897), [docs/designs/2025-01-27-bash-background-execution.md#L816-L826](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L816-L826) (`clm_dde1f11e32a47a9519330fb4b72cd4f5db5114039e8d2fce8f5d25c6f58519c2`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [inference/documented] Because the bash background execution material is a step-by-step implementation plan with TDD instructions, the described tools and behavior appear to be proposed rather than verified as already shipped in this snapshot. -- evidence: [docs/designs/2025-01-27-bash-background-execution.md#L17-L17](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L17-L17), [docs/designs/2025-01-27-bash-background-execution.md#L428-L431](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L428-L431), [docs/designs/2025-01-27-bash-background-execution.md#L13-L15](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L13-L15) (`clm_34f54d8b9a5ebf57910ac32e7949fcbf7840411d305551770e9e13772a8201f5`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

