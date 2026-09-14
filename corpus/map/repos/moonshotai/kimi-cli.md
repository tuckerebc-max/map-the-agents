# moonshotai/kimi-cli

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 86f136422a0a @ 4eced92fc40afd7a

## Summary (orientation draft, not independently verified)

Kimi CLI is documented as a terminal AI agent for software development and shell operations, with a shell command mode, ACP-based IDE integration, MCP tool support, and a layered, cross-tool skills system. A prominent notice states the project is evolving into Kimi Code CLI and will be gradually wound down.

## Source coverage

Source coverage (partial): 6 of 69 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The README describes Kimi CLI as a terminal AI agent that helps complete software development tasks and terminal operations: it reads and edits code, executes shell commands, searches and fetches web pages, and autonomously plans and adjusts actions during execution. -- evidence: [README.md#L14-L14](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/README.md#L14-L14)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Documentation states a detected newer version shows a blocking update prompt before the shell loads, letting the user upgrade immediately, skip once, or skip and suppress future reminders for that version; this whole update check can be disabled with an environment variable. -- evidence: [docs/en/faq.md#L146-L148](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/docs/en/faq.md#L146-L148), [docs/en/faq.md#L144-L144](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/docs/en/faq.md#L144-L144), [docs/en/faq.md#L158-L158](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/docs/en/faq.md#L158-L158), [docs/en/faq.md#L152-L152](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/docs/en/faq.md#L152-L152)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: Documented development commands include make format, make check for linting and type checking, make test, and separate make test-kimi-cli, make test-kosong, and make test-pykaos targets for each component. -- evidence: [README.md#L165-L175](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/README.md#L165-L175)
- skills-patterns (2 claim(s)):
  - [observation/documented] Documentation distinguishes two Kimi Code CLI extension mechanisms: skills give knowledge-based guidance the AI reads via SKILL.md, while plugins declare executable tools through plugin.json that the AI can invoke directly. -- evidence: [docs/en/customization/skills.md#L15-L16](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/docs/en/customization/skills.md#L15-L16)
  - [observation/documented] Documented skill discovery scans a brand group (kimi, then claude, then codex directories) and a generic group independently and merges the results, with same-named brand-group skills resolved kimi-over-claude-over-codex under a setting that defaults to merging every available brand directory. -- evidence: [docs/en/customization/skills.md#L44-L44](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/docs/en/customization/skills.md#L44-L44), [docs/en/customization/skills.md#L34-L40](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/docs/en/customization/skills.md#L34-L40)
- interfaces (2 claim(s)):
  - [observation/documented] Documentation describes a shell command mode toggled with Ctrl-X that runs shell commands without leaving Kimi CLI, noting built-in shell commands like cd are not yet supported in that mode. -- evidence: [README.md#L28-L29](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/README.md#L28-L29), [README.md#L24-L24](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/README.md#L24-L24)
  - [observation/documented] Documentation states Kimi CLI supports the Agent Client Protocol out of the box, so it can run as an ACP agent server for ACP-compatible editors such as Zed or JetBrains after completing login in the terminal first. -- evidence: [README.md#L39-L39](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/README.md#L39-L39), [README.md#L43-L43](https://github.com/MoonshotAI/kimi-cli/blob/86f136422a0aae6b217ea49e7ea1d2e8a1defcd2/README.md#L43-L43)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
More evidence: [full detail](kimi-cli.detail.md)

Metadata and full claim list: [full detail](kimi-cli.detail.md)
Human notes ([notes](kimi-cli.notes.md), never overwritten by build)

[Back to map index](../../index.md)
