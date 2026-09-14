# oi-overide/oi

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit dc4904403f50 @ e9bfe679c94f5f47

## Summary (orientation draft, not independently verified)

Selected evidence records: Users place prompts between `//>` and `<//` markers in source files; generated code is shown with an accept-changes (y/n) prompt. Code generation uses the OpenAI API; a changelog entry states all other platform support was removed, leaving OpenAI as the sole provider.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] A live file-monitoring component continuously watches project files for code-generation prompts and is started with `overide start`. -- evidence: [README.md#L25-L28](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L25-L28), [README.md#L64-L66](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L64-L66)
- design-choices (1 claim(s)):
  - [observation/documented] The tool is designed to be IDE-agnostic, working with any IDE or text editor rather than integrating with a specific one. -- evidence: [README.md#L25-L28](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L25-L28)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: contributors branch from `dev`, merge PRs through `staging` to `main`, and create a changeset (patch/minor/major) before submitting a feature-branch PR. -- evidence: [README.md#L101-L107](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L101-L107), [README.md#L117-L117](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L117-L117), [README.md#L127-L129](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L127-L129)
  - [observation/documented] Repository development practice: a GitHub Actions pipeline runs on PRs and pushes to `main` (pnpm install, lint, build, release PRs), and a publish workflow publishes to npm and syncs back to `staging`. -- evidence: [README.md#L214-L214](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L214-L214), [README.md#L231-L233](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L231-L233), [README.md#L218-L222](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L218-L222)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Users place prompts between `//>` and `<//` markers in source files; generated code is shown with an accept-changes (y/n) prompt. -- evidence: [README.md#L72-L74](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L72-L74), [README.md#L78-L84](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L78-L84)
  - [observation/documented] Projects are configured via an `oi-config.json` file holding a project name and an ignore list such as `node_modules` and `*.test.js`. -- evidence: [README.md#L90-L95](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L90-L95), [README.md#L88-L88](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L88-L88)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Code generation uses the OpenAI API; a changelog entry states all other platform support was removed, leaving OpenAI as the sole provider. -- evidence: [README.md#L25-L28](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L25-L28), [CHANGELOG.md#L7-L7](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/CHANGELOG.md#L7-L7)
  - [observation/documented] The project is licensed under GNU GPL-2.0 and uses changesets for version management and npm publishing. -- evidence: [README.md#L133-L135](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L133-L135), [README.md#L115-L115](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L115-L115), [README.md#L248-L248](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L248-L248)
- limitations (1 claim(s)):
  - [inference/documented] Features listed under 'Future Plans (v2.0)' — local-parser context management, unified-diff insertion, multi-file edits, and script execution — appear not yet shipped in this version. -- evidence: [README.md#L237-L240](https://github.com/oi-overide/oi/blob/dc4904403f5013e31d436b03a5ea5f6d31201ef8/README.md#L237-L240)
- relevance: unknown (no source-linked claim submitted for this facet)

(2 additional claim(s) omitted for length; see [full detail](oi.detail.md) for every claim.)

Metadata and full claim list: [full detail](oi.detail.md)
Human notes ([notes](oi.notes.md), never overwritten by build)

[Back to map index](../../index.md)
