# anthropics/claude-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b5932767f3ac @ 1c81b4db7b0df1f2

## Summary (orientation draft, not independently verified)

The snapshot is mostly README/security/license documentation for Claude Code, an agentic terminal coding tool, with install instructions, plugin mention, data-collection notes, and a HackerOne bug bounty. No source code or runtime internals are present in the evidence.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Claude Code is described as an agentic coding tool that runs in the terminal, understands the codebase, executes routine tasks, explains code, and handles git workflows via natural language commands. -- evidence: [README.md#L7-L7](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L7-L7)
- components (1 claim(s)):
  - [observation/documented] The repository includes Claude Code plugins that extend functionality with custom commands and agents, documented in a plugins directory. -- evidence: [README.md#L50-L50](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L50-L50)
- design-choices (1 claim(s)):
  - [observation/documented] The README states feedback collection includes usage data such as code acceptance or rejections, conversation data, and /bug submissions, with safeguards like limited retention and no use of feedback for model training. -- evidence: [README.md#L70-L70](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L70-L70), [README.md#L62-L62](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L62-L62)
- workflows (3 claim(s)):
  - [observation/documented] Recommended installation is via a curl install script on macOS/Linux and a PowerShell script on Windows; Homebrew and WinGet are also offered, while npm installation is deprecated. -- evidence: [README.md#L41-L44](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L41-L44), [README.md#L26-L29](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L26-L29), [README.md#L21-L24](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L21-L24), [README.md#L36-L39](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L36-L39), [README.md#L31-L34](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L31-L34), [README.md#L14-L15](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L14-L15)
  - [observation/documented] After installing, users navigate to their project directory and run the `claude` command to start. -- evidence: [README.md#L46-L46](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L46-L46)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The tool can be used in a terminal, in an IDE, or by tagging @claude on GitHub, per the README. -- evidence: [README.md#L7-L7](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L7-L7)
  - [observation/documented] A `/bug` command exists inside Claude Code for reporting issues directly, and GitHub issues are an alternative feedback channel. -- evidence: [README.md#L54-L54](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L54-L54)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] A Node.js 18+ badge appears in the README, and the npm package is @anthropic-ai/claude-code. -- evidence: [README.md#L3-L3](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L3-L3), [README.md#L5-L5](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L5-L5)
  - [observation/documented] The license file states use is subject to Anthropic's Commercial Terms of Service, © Anthropic PBC. -- evidence: [LICENSE.md#L1-L1](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/LICENSE.md#L1-L1)
- limitations (1 claim(s)):
  - [observation/documented] npm-based installation is explicitly marked deprecated in favor of other recommended methods. -- evidence: [README.md#L41-L44](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L41-L44), [README.md#L14-L15](https://github.com/anthropics/claude-code/blob/b5932767f3acbd07da25367064827e5cb81f43de/README.md#L14-L15)
- relevance: unknown (no source-linked claim submitted for this facet)

(1 additional claim(s) omitted for length; see [full detail](claude-code.detail.md) for every claim.)

Metadata and full claim list: [full detail](claude-code.detail.md)
Human notes ([notes](claude-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
