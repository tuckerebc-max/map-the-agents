# harnessworks/harness-starter-kit

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 62437bec264b @ 08418ac572a3a2e1

## Summary (orientation draft, not independently verified)

Selected evidence records: Harness Starter Kit is described as a prompt-first starter kit that converts repeated coding-agent mistakes into durable repository instructions, checks, memory, and evaluation. Adoption is agent-driven rather than an automatic installer: the agent inspects the target repo first and applies only the smallest useful set of harness artifacts, following documented workflow and prompt files.

## Source coverage

Source coverage (partial): 6 of 67 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Harness Starter Kit is described as a prompt-first starter kit that converts repeated coding-agent mistakes into durable repository instructions, checks, memory, and evaluation. -- evidence: [README.md#L43-L44](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L43-L44)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Adoption is agent-driven rather than an automatic installer: the agent inspects the target repo first and applies only the smallest useful set of harness artifacts, following documented workflow and prompt files. -- evidence: [README.md#L267-L272](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L267-L272)
- workflows (2 claim(s)):
  - [observation/documented] The adoption prompt instructs the agent to treat the working directory as the target repo, treat the cloned kit as read-only reference, inspect before editing, preserve existing architecture and conventions, and add only minimal harness pieces. -- evidence: [README.md#L80-L111](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L80-L111)
  - [observation/documented] The expected adoption outcome includes a project-specific AGENTS.md, a knowledge store if none exists, lightweight drift checks from the repo's real rules, local verification commands, and an adoption report covering changes, checks, assumptions, failure memory, and gate placement. -- evidence: [README.md#L113-L122](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L113-L122)
- skills-patterns (1 claim(s)):
  - [observation/documented] Besides prompt-first workflows, the same workflows are published as runtime-native skills for Codex and Claude Code, with the source package in agent-skills/ and packaging details in docs/agent-skills-package.md. -- evidence: [README.md#L258-L260](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L258-L260), [README.md#L193-L194](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L193-L194)
- interfaces (2 claim(s)):
  - [observation/documented] The /harness command names are prompt conventions typed into the coding agent chat by default, not built-in editor commands; they appear in editor command palettes only if matching custom slash commands are added separately. -- evidence: [README.md#L160-L163](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L160-L163)
  - [observation/documented] The kit exposes five stage-based commands: doctor (inspect without modifying), adopt (apply minimal harness pieces), review (challenge the diff pre-commit/PR), update (bring in a newer kit reference), and refresh (clean stale or duplicated guidance). -- evidence: [README.md#L178-L182](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L178-L182), [README.md#L167-L174](https://github.com/harnessworks/harness-starter-kit/blob/62437bec264b2deed83353e8209660d645e86828/README.md#L167-L174)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
More evidence: [full detail](harness-starter-kit.detail.md)

Metadata and full claim list: [full detail](harness-starter-kit.detail.md)
Human notes ([notes](harness-starter-kit.notes.md), never overwritten by build)

[Back to map index](../../index.md)
