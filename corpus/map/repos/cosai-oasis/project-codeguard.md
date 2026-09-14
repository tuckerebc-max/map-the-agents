# cosai-oasis/project-codeguard

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit d6a04cc5bfee @ 343681b93c681609

## Summary (orientation draft, not independently verified)

Project CodeGuard is a CoSAI/OASIS open-source framework of security skills and rules for AI coding agents, shipped as markdown rule sources, converted agent/IDE bundles, a Claude Code plugin, a Codex plugin, a SARIF-emitting reviewer subagent, and an MCP server. All prior claims were verified against cited slices; the summary now cites the model-agnostic and CoSAI/OASIS descriptors directly. Evidence coverage: 159 of 177 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 18 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 20 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

20 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (4 claim(s)):
  - [observation/documented] CodeGuard ships 23 security rule files: 3 always-apply rules (hardcoded credentials, crypto algorithms, digital certificates) and 20 context-specific rules selected by language, framework, or feature. -- evidence: [docs/claude-code-skill-plugin.md#L45-L45](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L45-L45), [docs/claude-code-skill-plugin.md#L84-L85](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L84-L85), [docs/claude-code-skill-plugin.md#L166-L166](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L166-L166), [docs/claude-code-skill-plugin.md#L79-L82](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L79-L82)
  - [observation/documented] Rules are authored in a unified markdown format under sources/ and converted into formats for popular coding agents, with release automation packaging them into downloadable ZIP files. -- evidence: [docs/claude-code-skill-plugin.md#L310-L313](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L310-L313), [README.md#L67-L71](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/README.md#L67-L71)
- components (3 claim(s)):
  - [observation/documented] The repository includes an MCP server exposing all CodeGuard security rules as tools over streamable HTTP, intended for centrally managed organizational deployment. -- evidence: [README.md#L62-L62](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/README.md#L62-L62)
  - [observation/documented] A CodeGuard Reviewer subagent performs full-repository security scans against all CodeGuard rules and emits findings as a SARIF 2.1.0 file, writing only that output file. -- evidence: [docs/codeguard-reviewer.md#L130-L137](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/codeguard-reviewer.md#L130-L137), [docs/codeguard-reviewer.md#L3-L3](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/codeguard-reviewer.md#L3-L3)
- design-choices (2 claim(s)):
  - [observation/documented] The reviewer treats repository content as untrusted data, ignores embedded instructions, never executes discovered code, and redacts suspected credential values from SARIF and summary output. -- evidence: [docs/codeguard-reviewer.md#L130-L137](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/codeguard-reviewer.md#L130-L137)
  - [observation/documented] The Codex plugin intentionally packages only ./skills/, excluding sources/skills/, the reviewer agent, hooks, and the MCP server, which are available via other install routes. -- evidence: [docs/codex-skill-plugin.md#L8-L11](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/codex-skill-plugin.md#L8-L11)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors regenerate the plugin with 'uv run python src/convert_to_ide_formats.py', which converts sources/ rules into skills/ (core rules only) and dist/ formats. -- evidence: [docs/claude-code-skill-plugin.md#L310-L313](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L310-L313), [docs/claude-code-skill-plugin.md#L307-L308](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L307-L308)
  - [observation/documented] Repository development practice: local plugin testing is done via 'claude --plugin-dir .' after regeneration, with /reload-plugins to pick up regenerated files in a running session. -- evidence: [docs/claude-code-skill-plugin.md#L326-L326](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L326-L326), [docs/claude-code-skill-plugin.md#L321-L324](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L321-L324)
- skills-patterns (2 claim(s)):
  - [observation/documented] The Claude Code skill activates automatically when writing or reviewing code, implementing security-sensitive features, handling user input or credentials, or configuring cloud infrastructure. -- evidence: [docs/claude-code-skill-plugin.md#L49-L55](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L49-L55)
  - [observation/documented] The skill follows a 3-step workflow: initial security check to identify applicable rules, code generation with secure-by-default patterns, and a security review against rule checklists. -- evidence: [docs/claude-code-skill-plugin.md#L70-L75](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L70-L75), [docs/claude-code-skill-plugin.md#L66-L68](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L66-L68), [docs/claude-code-skill-plugin.md#L61-L64](https://github.com/cosai-oasis/project-codeguard/blob/d6a04cc5bfee65fc400a931fcaff5926d2d9bfe8/docs/claude-code-skill-plugin.md#L61-L64)
More evidence: [full detail](project-codeguard.detail.md)

Metadata and full claim list: [full detail](project-codeguard.detail.md)
Human notes ([notes](project-codeguard.notes.md), never overwritten by build)

[Back to map index](../../index.md)
