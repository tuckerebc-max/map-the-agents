# fission-ai/openspec

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9d4e5974e5c0 @ 01249e4603bb0f5e

## Summary (orientation draft, not independently verified)

OpenSpec is a spec-driven development CLI (@fission-ai/openspec) that gives AI coding assistants a shared, reviewable plan via slash commands and an openspec/ directory of specs and changes. Evidence covers its interfaces, artifact design, Node requirement, tool integrations, telemetry, and a documented parallel-merge data-loss limitation; contributor guidance is recorded only under workflows. Evidence coverage: 137 of 347 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 36 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] Specs are plain Markdown with requirements and concrete scenarios and no special syntax to learn; each change gets its own folder containing proposal, specs, design, and tasks artifacts. -- evidence: [README.md#L82-L82](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L82-L82), [README.md#L58-L64](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L58-L64), [README.md#L190-L193](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L190-L193)
  - [observation/documented] The stated philosophy favors fluid, iterative workflows over rigid phase gates, targeting brownfield projects and scaling from personal projects to enterprises. -- evidence: [README.md#L28-L34](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L28-L34), [README.md#L197-L197](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L197-L197), [README.md#L190-L193](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L190-L193)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors should open a discussion or issue before a PR and link it; new features, significant refactors, and architectural changes require an OpenSpec change proposal first, with details in CONTRIBUTING.md. -- evidence: [README.md#L227-L227](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L227-L227), [README.md#L229-L229](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L229-L229)
  - [observation/documented] Repository development practice: install.md is an agent-facing setup prompt directing the installing agent to verify Node, install the CLI globally with user confirmation, run openspec init --tools, and report what init actually created. -- evidence: [install.md#L64-L64](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/install.md#L64-L64), [install.md#L5-L5](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/install.md#L5-L5), [install.md#L17-L21](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/install.md#L17-L21)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] OpenSpec is driven from AI coding tools via slash commands such as /opsx:explore, /opsx:propose, /opsx:apply, and /opsx:archive, with tool-specific spellings like /opsx-propose (Cursor, Copilot), @opsx-propose (Amazon Q), or $openspec-propose (Codex). -- evidence: [README.md#L66-L72](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L66-L72), [install.md#L66-L66](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/install.md#L66-L66), [README.md#L74-L77](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L74-L77), [README.md#L58-L64](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L58-L64), [README.md#L149-L149](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L149-L149), [README.md#L49-L56](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L49-L56)
  - [observation/documented] The product ships a CLI installed globally via npm, pnpm, yarn, or bun (with a Nix option), with commands including openspec init, openspec update, and openspec config profile. -- evidence: [install.md#L33-L38](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/install.md#L33-L38), [README.md#L135-L138](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L135-L138), [README.md#L129-L131](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L129-L131), [README.md#L215-L217](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L215-L217), [README.md#L147-L147](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L147-L147), [README.md#L207-L209](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L207-L209)
- memory-state (1 claim(s)):
  - [observation/documented] The product maintains an openspec/ directory separating openspec/specs/ (current truth) from openspec/changes/ (proposed updates), and archiving merges approved updates back into the specs. -- evidence: [README_OLD.md#L82-L86](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README_OLD.md#L82-L86), [README.md#L74-L77](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README.md#L74-L77), [README_OLD.md#L49-L52](https://github.com/Fission-AI/OpenSpec/blob/9d4e5974e5c0d9a09b9c6c1e1eb0975e80ec4461/README_OLD.md#L49-L52)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](openspec.detail.md)

Metadata and full claim list: [full detail](openspec.detail.md)
Human notes ([notes](openspec.notes.md), never overwritten by build)

[Back to map index](../../index.md)
