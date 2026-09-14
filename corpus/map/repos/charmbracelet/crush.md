# charmbracelet/crush

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3502b15a7cf1 @ 7bb77b7deb239b31

## Summary (orientation draft, not independently verified)

The snapshot contains only documentation (hooks and config READMEs) for Crush, an agent runtime with a hook system and Bash-based configuration. Claims below describe the documented product behavior; no code or development-practice evidence is present. Evidence coverage: 165 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Crush ships a builtin crush-hook skill so the agent can write, edit, and configure hooks on itself, and a builtin config skill for natural-language configuration. -- evidence: [docs/config/README.md#L6-L13](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/config/README.md#L6-L13), [docs/hooks/README.md#L15-L23](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L15-L23)
- design-choices (3 claim(s)):
  - [observation/documented] Hooks run in parallel but their results compose deterministically in config order; deny beats allow, updated_input patches shallow-merge sequentially, and identical commands are deduplicated. -- evidence: [docs/hooks/README.md#L383-L385](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L383-L385), [docs/hooks/README.md#L174-L175](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L174-L175), [docs/hooks/README.md#L15-L23](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L15-L23), [docs/hooks/README.md#L389-L398](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L389-L398), [docs/hooks/README.md#L726-L733](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L726-L733), [docs/hooks/README.md#L207-L219](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L207-L219)
  - [observation/documented] Hooks execute through Crush's embedded POSIX shell (mvdan.cc/sh), the same interpreter as the bash tool; shebang'd scripts dispatch to the named interpreter via os/exec, identically across macOS, Linux, and Windows. -- evidence: [docs/hooks/README.md#L95-L99](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L95-L99)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (6 claim(s)):
  - [observation/documented] Hooks are user-defined shell commands configured under a 'hooks' object in crush.json, keyed by event name, with optional name, matcher regex, required command, and timeout (default 30s). -- evidence: [docs/hooks/README.md#L608-L609](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L608-L609), [docs/hooks/README.md#L137-L150](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L137-L150), [docs/hooks/README.md#L614-L617](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L614-L617), [docs/hooks/README.md#L611-L612](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L611-L612), [docs/hooks/README.md#L602-L606](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L602-L606), [docs/hooks/README.md#L200-L201](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L200-L201), [docs/hooks/README.md#L6-L8](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L6-L8)
  - [observation/documented] Currently only one hook event, PreToolUse, is supported; it fires before every top-level agent tool call and matches against the tool name, with sub-agent tool calls not intercepted. -- evidence: [docs/hooks/README.md#L183-L185](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L183-L185), [docs/hooks/README.md#L187-L188](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L187-L188), [docs/hooks/README.md#L194-L198](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L194-L198), [docs/hooks/README.md#L15-L23](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L15-L23)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Hook results apply before permission checks: an aggregated 'deny' blocks the call without a prompt, 'allow' pre-approves and skips the prompt, and no decision falls through to the normal permission flow. -- evidence: [docs/hooks/README.md#L339-L344](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L339-L344), [docs/hooks/README.md#L726-L733](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L726-L733), [docs/hooks/README.md#L686-L690](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L686-L690), [docs/hooks/README.md#L207-L219](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L207-L219)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (2 claim(s)):
  - [observation/documented] PowerShell .ps1 scripts are not auto-dispatched by extension and must be invoked explicitly via powershell -File or pwsh -File. -- evidence: [docs/hooks/README.md#L103-L130](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L103-L130)
More evidence: [full detail](crush.detail.md)

Metadata and full claim list: [full detail](crush.detail.md)
Human notes ([notes](crush.notes.md), never overwritten by build)

[Back to map index](../../index.md)
