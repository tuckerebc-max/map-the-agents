# kilo-org/kilocode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c36e22634860 @ 9a09d74283c90a85

## Summary (orientation draft, not independently verified)

Selected evidence records: Kilo Code is an AI coding agent available for VS Code, JetBrains IDEs, and as a CLI, installable via npm, curl, pnpm, bun, Homebrew, and AUR. The CLI ships as platform binaries for Windows, macOS (Intel and Apple Silicon), and Linux x64/ARM, including a musl build for Alpine and a non-AVX baseline build for older CPUs.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Kilo ships specialized agents: Code (default, implements code), Plan (architecture and plans), Ask (answers without touching files), Debug, and Review, and users can build custom agents. -- evidence: [README.md#L125-L129](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L125-L129), [README.md#L123-L123](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L123-L123)
  - [observation/documented] Documented capabilities include multi-file code generation, inline ghost-text autocomplete, self-checking, terminal and browser control, an MCP marketplace, and 500+ models with mid-task switching. -- evidence: [README.md#L135-L140](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L135-L140)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: releases run through an automated GitHub Actions publish workflow whose four sequential jobs are version, build-cli, build-vscode, and publish, gated to the Kilo-Org/kilocode repo and requiring write access. -- evidence: [RELEASING.md#L44-L48](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/RELEASING.md#L44-L48), [RELEASING.md#L25-L29](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/RELEASING.md#L25-L29), [RELEASING.md#L3-L3](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/RELEASING.md#L3-L3), [RELEASING.md#L21-L21](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/RELEASING.md#L21-L21), [RELEASING.md#L33-L40](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/RELEASING.md#L33-L40), [RELEASING.md#L52-L52](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/RELEASING.md#L52-L52), [RELEASING.md#L90-L91](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/RELEASING.md#L90-L91)
  - [observation/documented] Repository development practice: an automated reviewer bot is guided by REVIEW.md to catch bugs, design issues, and fork-merge hygiene beyond what CI reports, minimizing diff against the upstream opencode fork. -- evidence: [REVIEW.md#L3-L3](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/REVIEW.md#L3-L3), [REVIEW.md#L57-L57](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/REVIEW.md#L57-L57), [REVIEW.md#L5-L5](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/REVIEW.md#L5-L5)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Kilo Code is an AI coding agent available for VS Code, JetBrains IDEs, and as a CLI, installable via npm, curl, pnpm, bun, Homebrew, and AUR. -- evidence: [README.md#L49-L49](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L49-L49), [README.md#L24-L24](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L24-L24), [README.md#L46-L46](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L46-L46), [README.md#L58-L58](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L58-L58), [README.md#L9-L9](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L9-L9), [README.md#L55-L55](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L55-L55), [README.md#L61-L62](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L61-L62), [README.md#L52-L52](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L52-L52)
  - [observation/documented] The CLI ships as platform binaries for Windows, macOS (Intel and Apple Silicon), and Linux x64/ARM, including a musl build for Alpine and a non-AVX baseline build for older CPUs. -- evidence: [README.md#L117-L117](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L117-L117), [README.md#L109-L115](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/README.md#L109-L115)
- memory-state (3 claim(s)):
  - [observation/documented] The runtime defines a session context model: a System Context assembled from typed Context Sources, Session History projected per provider turn, and a Context Snapshot tracking each source's last-admitted value. -- evidence: [CONTEXT.md#L7-L9](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L7-L9), [CONTEXT.md#L15-L17](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L15-L17), [CONTEXT.md#L33-L34](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L33-L34), [CONTEXT.md#L3-L3](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L3-L3), [CONTEXT.md#L11-L13](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L11-L13)
  - [observation/documented] Context changes are admitted lazily at a Safe Provider-Turn Boundary rather than pushed asynchronously, and changes from multiple sources at one boundary combine into a single Mid-Conversation System Message. -- evidence: [CONTEXT.md#L22-L24](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L22-L24), [CONTEXT.md#L90-L199](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L90-L199), [CONTEXT.md#L39-L40](https://github.com/Kilo-Org/kilocode/blob/c36e22634860e06e0aa63234fae37bbd83d3b182/CONTEXT.md#L39-L40)
- orchestration: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](kilocode.detail.md)

Metadata and full claim list: [full detail](kilocode.detail.md)
Human notes ([notes](kilocode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
