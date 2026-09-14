# juliusbrussee/caveman-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 3a21be115c32 @ 5d4b7561aa9d2419

## Summary (orientation draft, not independently verified)

README and docs describe Caveman Code, a frozen (August 2026) MIT-licensed terminal coding agent forked from pi-code, whose core value is four-layer token compression plus plan mode, goal loop, subagents, MCP, and cavemem-backed memory. Evidence is documentation-only; no source code slices are present. Evidence coverage: 156 of 192 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 30 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 23 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

23 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The project is marked frozen as of August 2026: it still installs and works but receives no new features or fixes, and its lesson moved into the separate 'caveman' project. -- evidence: [README.md#L1-L6](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/README.md#L1-L6)
  - [observation/documented] Caveman Code is MIT-licensed and described as a heavy fork of Mario Zechner's pi-code, with upstream tracked and fixes contributed back where generally useful. -- evidence: [README.md#L355-L355](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/README.md#L355-L355), [README.md#L341-L341](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/README.md#L341-L341)
- components (1 claim(s)):
  - [observation/documented] The repository is described as a TypeScript monorepo of 9 packages, with the coding-agent package exporting full TypeScript types and hosting the daemon's OpenAPI 3.1 spec. -- evidence: [docs/api.md#L34-L34](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/docs/api.md#L34-L34), [docs/api.md#L121-L121](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/docs/api.md#L121-L121), [docs/api.md#L128-L128](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/docs/api.md#L128-L128), [README.md#L335-L335](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/README.md#L335-L335)
- design-choices (2 claim(s)):
  - [observation/documented] The core design is four always-on compression layers targeting two token sinks: model replies (Caveman Mode with lite/full/ultra levels) and tool output (tool budgets, read dedup, optional RTK). -- evidence: [README.md#L132-L132](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/README.md#L132-L132), [README.md#L134-L139](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/README.md#L134-L139)
  - [observation/documented] Tool-output compression applies per-tool line caps (bash 80, read 300, grep 120), strips ANSI, collapses blank lines, and does semantic JSON/XML extraction, with claimed cuts of 67–94%. -- evidence: [README.md#L134-L139](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/README.md#L134-L139)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are markdown files auto-loaded on description match (unlike explicit slash commands), stored at project (.cave/skills/<name>/SKILL.md), user (~/.cave/skills/...), or plugin scope, using a frontmatter superset of Claude Code's format. -- evidence: [docs/reference/skills.md#L8-L8](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/docs/reference/skills.md#L8-L8), [docs/reference/skills.md#L14-L18](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/docs/reference/skills.md#L14-L18)
- interfaces (5 claim(s)):
  - [observation/documented] The CLI installs two binaries, 'caveman' (primary) and 'caveman-code' (alias), and supports TUI, one-shot prompt, print mode (-p), stdin piping, session continue/resume (-c/-r), and 'goal start' for an autonomous loop. -- evidence: [README.md#L84-L90](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/README.md#L84-L90), [README.md#L82-L82](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/README.md#L82-L82), [README.md#L115-L124](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/README.md#L115-L124)
  - [observation/documented] Four programmatic surfaces are documented: a Node SDK (createAgentSession), a daemon SDK (@juliusbrussee/caveman-sdk over HTTP/WS), JSON-RPC over stdin/stdout via --mode rpc, and print/JSON output modes including --output-schema validation for CI. -- evidence: [docs/api.md#L68-L70](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/docs/api.md#L68-L70), [docs/api.md#L105-L105](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/docs/api.md#L105-L105), [docs/api.md#L8-L8](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/docs/api.md#L8-L8), [docs/api.md#L38-L40](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/docs/api.md#L38-L40), [docs/api.md#L99-L103](https://github.com/JuliusBrussee/caveman-code/blob/3a21be115c32aa27288c8ed6d860d9aa1b65d2c5/docs/api.md#L99-L103)
- memory-state (3 claim(s)):
More evidence: [full detail](caveman-code.detail.md)

Metadata and full claim list: [full detail](caveman-code.detail.md)
Human notes ([notes](caveman-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
