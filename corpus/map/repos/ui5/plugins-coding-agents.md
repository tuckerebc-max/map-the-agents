# ui5/plugins-coding-agents

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4c3754ae5b66 @ 72a0a0048c55923a

## Summary (orientation draft, not independently verified)

The repository provides Claude Code plugins for UI5 development: a general 'ui5' plugin (a wrapper around the UI5 MCP server), a modernization plugin, and a TypeScript conversion plugin, each installable via Claude plugin commands. Contributor-facing docs cover issue reporting, DCO/CLA, and commit conventions.

## Source coverage

Source coverage (complete): 6 of 6 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repository ships three plugins: 'ui5' (project creation, API lookup, linter integration, best-practice skills), 'ui5-modernization', and 'ui5-typescript-conversion'. -- evidence: [README.md#L28-L32](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/README.md#L28-L32)
- design-choices (1 claim(s)):
  - [observation/documented] The TypeScript conversion plugin provides a step-by-step playbook addressing UI5-specific migration challenges like the class system, sap.ui.define loader, and runtime-generated getters/setters. -- evidence: [CHANGELOG.md#L107-L107](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L107-L107)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: contributors must run 'npm run prettier' to format .mcp.json and .claude-plugin/plugin.json before committing. -- evidence: [docs/Guidelines.md#L5-L5](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/docs/Guidelines.md#L5-L5)
  - [observation/documented] Repository development practice: the project uses Conventional Commits with a required lowercase type, optional scope, and Sentence Case description, and asks for rebase instead of merge commits. -- evidence: [docs/Guidelines.md#L15-L15](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/docs/Guidelines.md#L15-L15), [docs/Guidelines.md#L11-L11](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/docs/Guidelines.md#L11-L11), [docs/Guidelines.md#L29-L31](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/docs/Guidelines.md#L29-L31), [docs/Guidelines.md#L25-L27](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/docs/Guidelines.md#L25-L27)
- skills-patterns (2 claim(s)):
  - [observation/documented] The ui5-modernization plugin includes skills such as fix-cyclic-deps, fix-js-globals, fix-xml-globals, modernize-flp-sandbox, modernize-test-starter, and modernize-ui5-app. -- evidence: [CHANGELOG.md#L8-L19](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L8-L19)
  - [observation/documented] The changelog records added skills for the ui5 plugin covering accessibility, QUnit, Smart & MDC controls, tables, OPA5 guidelines, UI Integration Cards, and general UI5 guidelines. -- evidence: [CHANGELOG.md#L50-L50](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L50-L50), [CHANGELOG.md#L26-L28](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L26-L28), [CHANGELOG.md#L77-L78](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L77-L78), [CHANGELOG.md#L42-L43](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L42-L43)
- interfaces (2 claim(s)):
  - [observation/documented] The ui5 plugin can be installed via 'claude plugin install ui5@claude-plugins-official' or the in-app '/plugin install ui5@claude-plugins-official' command. -- evidence: [CHANGELOG.md#L95-L97](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L95-L97), [CHANGELOG.md#L101-L103](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L101-L103)
  - [observation/documented] The ui5-typescript-conversion plugin is installed with 'claude plugin install ui5-typescript-conversion@claude-plugins-official'. -- evidence: [CHANGELOG.md#L111-L113](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L111-L113)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The ui5 plugin is described as a wrapper around the UI5 MCP server, with possible future additions such as more skills. -- evidence: [CHANGELOG.md#L91-L91](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L91-L91)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
  - [observation/documented] The project targets developers using coding agents on UI5 projects, aiming to help create UI5 projects, detect and fix UI5-specific errors, and supply UI5-specific information. -- evidence: [README.md#L5-L5](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/README.md#L5-L5), [README.md#L22-L24](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/README.md#L22-L24)

(2 additional claim(s) omitted for length; see [full detail](plugins-coding-agents.detail.md) for every claim.)

Metadata and full claim list: [full detail](plugins-coding-agents.detail.md)
Human notes ([notes](plugins-coding-agents.notes.md), never overwritten by build)

[Back to map index](../../index.md)
