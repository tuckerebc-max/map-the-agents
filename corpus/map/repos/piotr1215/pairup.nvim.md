# piotr1215/pairup.nvim

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a4841094a58b @ 4fa12d5ec32839c7

## Summary (orientation draft, not independently verified)

pairup.nvim is a Neovim plugin (v4) providing inline AI pair programming with Claude Code via cc:/uu: markers, operators, plan-review conflict views, a peripheral Claude worktree mode, and statusline progress tracking. Evidence is documentation-only (README and vimdoc). Evidence coverage: 152 of 271 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] A peripheral Claude feature runs a second autonomous Claude instance in a sibling git worktree that receives diffs of spec files and implements changes independently. -- evidence: [README.md#L68-L68](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L68-L68), [README.md#L70-L70](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L70-L70), [README.md#L72-L77](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L72-L77)
  - [observation/documented] Todo progress is tracked via a Claude Code PostToolUse hook script that the user must copy into ~/.claude/scripts and register in settings.json. -- evidence: [README.md#L309-L320](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L309-L320), [README.md#L302-L305](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L302-L305), [README.md#L300-L300](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L300-L300)
- design-choices (1 claim(s)):
  - [observation/documented] v4.0 removed the overlay system, sessions, RPC, and marker-based suggestions to focus on simple inline editing, citing less complexity and more reliability; legacy features remain on the legacy-v3 branch. -- evidence: [README.md#L5-L14](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L5-L14), [doc/pairup.txt#L29-L36](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/doc/pairup.txt#L29-L36)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (7 claim(s)):
  - [observation/documented] Users write cc:, cc!:, or ccp: markers in code and save; Claude then edits the file directly, per the README's how-it-works section. -- evidence: [README.md#L18-L18](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L18-L18), [doc/pairup.txt#L40-L41](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/doc/pairup.txt#L40-L41)
  - [observation/documented] ccp: (plan) makes Claude wrap changes in CURRENT/PROPOSED conflict markers so the user reviews and accepts or rejects before anything changes. -- evidence: [doc/pairup.txt#L53-L56](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/doc/pairup.txt#L53-L56), [README.md#L20-L25](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L20-L25)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The default provider command includes Claude's --permission-mode acceptEdits flag so Claude edits files without per-change confirmation, which the docs say the inline workflow requires. -- evidence: [README.md#L343-L343](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L343-L343), [README.md#L347-L395](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L347-L395)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Requirements are Neovim 0.11+ and the Claude Code CLI. -- evidence: [README.md#L434-L435](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L434-L435)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(5 additional claim(s) omitted for length; see [full detail](pairup.nvim.detail.md) for every claim.)

Metadata and full claim list: [full detail](pairup.nvim.detail.md)
Human notes ([notes](pairup.nvim.notes.md), never overwritten by build)

[Back to map index](../../index.md)
