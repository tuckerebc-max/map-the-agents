# kirodotdev/kiro

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit bfe7ff30d9b2 @ 0f0f944d18d31554

## Summary (orientation draft, not independently verified)

This repository is Kiro's public issue/feedback tracker plus GitHub issue-triage automation, not the Kiro product source. Evidence documents a daily stale-issue-closing workflow and describes the Kiro product's surfaces and features via README links. Evidence coverage: 160 of 177 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Kiro's Specs feature structures requirements, design decisions, and implementation tasks, with a Requirements Analysis step to find contradictions and gaps before coding. -- evidence: [README.md#L41-L47](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/README.md#L41-L47)
- components (1 claim(s)):
  - [observation/documented] The Crew surface is described as a persistent open-source development workspace with memory, scheduling, and multi-channel access. -- evidence: [README.md#L31-L37](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/README.md#L31-L37)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] The repository hosts automation for triaging and managing its own GitHub issues, while the Kiro product source code is not hosted here. -- evidence: [README.md#L19-L19](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/README.md#L19-L19)
  - [observation/documented] Maintainers are advised to apply the pending-response label consistently, monitor workflow logs, and adjust the 7-day threshold if their community needs more time. -- evidence: [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L460-L462](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L460-L462), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L464-L466](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L464-L466), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L452-L454](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L452-L454)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Kiro is described as an agentic AI development platform spanning IDE, CLI, Web, Mobile, and Crew surfaces, powered by a unified agent harness. -- evidence: [README.md#L29-L29](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/README.md#L29-L29), [README.md#L7-L9](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/README.md#L7-L9)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (4 claim(s)):
  - [observation/documented] The stale-issue workflow runs daily at midnight UTC via cron and can also be triggered manually with gh workflow run close-stale.yml. -- evidence: [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L23-L25](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L23-L25), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L10-L13](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L10-L13), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L27-L30](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L27-L30)
  - [observation/documented] The workflow targets open issues labeled 'pending-response', closes those inactive for 7 or more days, and posts a closing comment explaining the closure and how to reopen. -- evidence: [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L5-L5](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L5-L5), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L283-L290](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L283-L290), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L251-L253](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L251-L253), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L292-L292](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L292-L292)
- tools-permissions (2 claim(s)):
  - [observation/documented] The product includes a permissions feature for setting agent access boundaries, plus Hooks, Powers, and MCP for tools and external integrations. -- evidence: [README.md#L41-L47](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/README.md#L41-L47)
  - [observation/documented] The stale-issue workflow requires GitHub permissions of issues:write (close issues, post comments) and contents:read (access scripts). -- evidence: [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L515-L519](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L515-L519), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L521-L523](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L521-L523)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [inference/documented] The automation appears to be TypeScript scripts using the Octokit GitHub client, built with npm, based on code examples and build instructions in the docs. -- evidence: [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L341-L345](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L341-L345), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L104-L116](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L104-L116), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L336-L339](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L336-L339), [docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L59-L67](https://github.com/kirodotdev/Kiro/blob/bfe7ff30d9b21e583566c844d75e3dd2b572e2c7/docs/STALE_ISSUE_CLOSING_EXPLAINED.md#L59-L67)
More evidence: [full detail](kiro.detail.md)

Metadata and full claim list: [full detail](kiro.detail.md)
Human notes ([notes](kiro.notes.md), never overwritten by build)

[Back to map index](../../index.md)
