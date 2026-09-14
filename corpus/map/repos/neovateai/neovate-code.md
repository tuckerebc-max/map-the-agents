# neovateai/neovate-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 0a24b363ecbe @ d399a326a058e2ba

## Summary (orientation draft, not independently verified)

Selected evidence records: A design doc dated 2025-01-26 addresses terminal focus escape sequences ([I]/[O]) appearing as literal text in the chat input when modals are shown, because Ink strips the escape prefix. The chosen fix is a global always-active useInput hook in ChatInput.tsx to intercept focus events, with a simplified skip-handler kept in TextInput as a safety net.

## Source coverage

Source coverage (partial): 6 of 149 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (4 claim(s)):
  - [observation/documented] The focus handler updates window focus state via useAppStore.getState().setWindowFocused, setting true for '[I' (focus gained) and false for '[O' (focus lost). -- evidence: [docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L50-L62](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L50-L62)
  - [observation/documented] The planned BackgroundTaskManager stores tasks in a Map with fields id, command, pid, optional pgid, status (running/completed/killed/failed), createdAt, output, and exitCode, generating ids prefixed 'task_'. -- evidence: [docs/designs/2025-01-27-bash-background-execution.md#L101-L102](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L101-L102), [docs/designs/2025-01-27-bash-background-execution.md#L104-L118](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L104-L118), [docs/designs/2025-01-27-bash-background-execution.md#L84-L93](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L84-L93)
- design-choices (3 claim(s)):
  - [observation/documented] A design doc dated 2025-01-26 addresses terminal focus escape sequences ([I]/[O]) appearing as literal text in the chat input when modals are shown, because Ink strips the escape prefix. -- evidence: [docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L7-L7](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L7-L7), [docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L9-L9](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L9-L9)
  - [observation/documented] The chosen fix is a global always-active useInput hook in ChatInput.tsx to intercept focus events, with a simplified skip-handler kept in TextInput as a safety net. -- evidence: [docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L46-L46](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L46-L46), [docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L42-L42](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-26-global-terminal-focus-event-handler.md#L42-L42)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The plan adds a run_in_background boolean parameter to the bash tool and documents that dev-pattern commands auto-move to background after 2 seconds if producing output, returning a task_id for bash_output and kill_bash. -- evidence: [docs/designs/2025-01-27-bash-background-execution.md#L456-L472](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L456-L472), [docs/designs/2025-01-27-bash-background-execution.md#L481-L485](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L481-L485)
  - [observation/documented] The planned bash_output tool takes a task_id and returns the task's command, status, PID, creation time, accumulated output, and exit code when set. -- evidence: [docs/designs/2025-01-27-bash-background-execution.md#L802-L810](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L802-L810), [docs/designs/2025-01-27-bash-background-execution.md#L812-L814](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L812-L814), [docs/designs/2025-01-27-bash-background-execution.md#L778-L800](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L778-L800)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] In the planned design, bash_output requires no approval (category 'read', needsApproval returns false), while kill_bash refuses to terminate tasks whose status is not 'running'. -- evidence: [docs/designs/2025-01-27-bash-background-execution.md#L892-L897](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L892-L897), [docs/designs/2025-01-27-bash-background-execution.md#L816-L826](https://github.com/neovateai/neovate-code/blob/0a24b363ecbe24eb87a0190a88fcb78c80593b4b/docs/designs/2025-01-27-bash-background-execution.md#L816-L826)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
More evidence: [full detail](neovate-code.detail.md)

Metadata and full claim list: [full detail](neovate-code.detail.md)
Human notes ([notes](neovate-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
