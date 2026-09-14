# rustykuntz/clideck

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 2c381835565b @ eb88fdf2ee936171

## Summary (orientation draft, not independently verified)

CliDeck is a local browser workspace for running multiple CLI agent sessions (Claude Code, Codex, Gemini CLI, OpenCode, Pi, shell) grouped into projects, with preview tabs, plugins, and cross-session agent messaging; the snapshot documents the CLI, plugin SDK, and contributor workflow.

## Source coverage

Source coverage (partial): 3 of 5 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Built-in plugins include Git Changes, Supertonic Voice, Emoji, and Smart Dictation, and additional plugins can be built with a plugin SDK. -- evidence: [README.md#L73-L73](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L73-L73), [README.md#L68-L71](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L68-L71)
- design-choices (1 claim(s)):
  - [observation/documented] CliDeck binds to localhost, and agent CLIs use their own network connections rather than going through CliDeck. -- evidence: [README.md#L101-L102](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L101-L102)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors use Node.js 22.12+, run npm ci and npm test, start the app with npm start using a separate dev data-dir, run UI checks with node --test, and test interface changes in both light and dark themes. -- evidence: [CONTRIBUTING.md#L5-L9](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/CONTRIBUTING.md#L5-L9), [CONTRIBUTING.md#L11-L12](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/CONTRIBUTING.md#L11-L12)
  - [observation/documented] Repository development practice: keep changes simple and focused, open an issue before large changes, and include the problem, resulting behavior, and relevant checks in pull requests. -- evidence: [CONTRIBUTING.md#L3-L3](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/CONTRIBUTING.md#L3-L3), [CONTRIBUTING.md#L11-L12](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/CONTRIBUTING.md#L11-L12)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] CliDeck runs Claude Code, Codex, Gemini CLI, OpenCode, Pi, and shell sessions in one browser window, grouped into projects, where each session is the agent's actual terminal with its own tools, configuration, and account. -- evidence: [README.md#L5-L9](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L5-L9)
  - [observation/documented] After starting, the web UI is opened at http://127.0.0.1:4000; the tool can also be run via npx. -- evidence: [README.md#L24-L25](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L24-L25)
- memory-state (1 claim(s)):
  - [observation/documented] Sessions can be reopened and earlier conversations read, stopped sessions show last-used times, and session backups can be exported for recovery. -- evidence: [README.md#L32-L41](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L32-L41)
- orchestration (1 claim(s)):
  - [observation/documented] CliDeck Ask lets agents send requests to other sessions and receive replies, including across providers; users type '@@' to find sessions, and agents discover teammates with 'clideck agents' and contact them with 'clideck ask'. -- evidence: [README.md#L77-L78](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L77-L78), [README.md#L88-L89](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/README.md#L88-L89)
- tools-permissions (2 claim(s)):
  - [observation/documented] Plugin backends run as arbitrary local code with the user's filesystem and network authority; worker isolation protects against accidental crashes but is explicitly not a malicious-code sandbox. -- evidence: [PLUGIN-SDK.md#L223-L225](https://github.com/rustykuntz/clideck/blob/2c381835565bf58fcfd50bb5645f13c5429245ee/PLUGIN-SDK.md#L223-L225)
More evidence: [full detail](clideck.detail.md)

Metadata and full claim list: [full detail](clideck.detail.md)
Human notes ([notes](clideck.notes.md), never overwritten by build)

[Back to map index](../../index.md)
