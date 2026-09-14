# sudo-tee/opencode.nvim

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 636a26425227 @ 166e3c2d123d18b6

## Summary (orientation draft, not independently verified)

Evidence covers the opencode.nvim Neovim frontend plugin: its chat UI, commands/keymaps/API, context capture, permission handling, server configuration, and community recipes (change-by-change review, bidirectional TUI/nvim sync). Most claims are documentation-based; no source code is included in the slices. Evidence coverage: 147 of 262 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 18 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

18 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (3 claim(s)):
  - [observation/documented] The plugin bridges Neovim and the opencode AI agent, providing a chat interface that captures editor context such as the current file and selections, with persistent sessions tied to the workspace. -- evidence: [README.md#L21-L21](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L21-L21)
  - [observation/documented] A dedicated chat panel window inside Neovim shows previous messages and responses and uses workspace/editor state as context for iterating on code. -- evidence: [README.md#L27-L27](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L27-L27)
- design-choices (2 claim(s)):
  - [observation/documented] Editor context is automatically captured for conversations, including current file, visual selection, mentioned files, diagnostics, and cursor position/line content. -- evidence: [README.md#L788-L794](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L788-L794), [README.md#L786-L786](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L786-L786)
  - [observation/documented] The model picker sorts favorites first (by favoriting order), then recently used models, then others alphabetically; variant selection per model is remembered for future use. -- evidence: [README.md#L411-L413](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L411-L413), [README.md#L435-L435](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L435-L435)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: recipe contributions should use the provided template, start from the problem being solved, include a GIF demo, give step-by-step setup instructions, cross-reference related recipes, and be self-contained. -- evidence: [docs/README.md#L17-L20](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/docs/README.md#L17-L20), [docs/README.md#L22-L22](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/docs/README.md#L22-L22), [docs/README.md#L15-L15](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/docs/README.md#L15-L15)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Actions are reachable via default keymaps (e.g. <leader>og toggle), user commands (e.g. :Opencode open input), and Lua API functions such as require('opencode.api').toggle(). -- evidence: [README.md#L656-L718](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L656-L718), [README.md#L654-L654](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L654-L654)
  - [observation/documented] The plugin exposes a diff view of modified files since the last prompt via :Opencode diff_open, :Opencode diff open, pressing D on a 'Created Snapshot' output, or the default <leader>od keymap. -- evidence: [docs/recipes/change-by-change-review/README.md#L10-L12](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/docs/recipes/change-by-change-review/README.md#L10-L12)
- memory-state (2 claim(s)):
  - [observation/documented] Favorite models, toggled with <C-f> in the model picker, show a star icon, sort to the top, and persist across Neovim sessions; the plugin respects the OpenCode CLI storage format. -- evidence: [README.md#L417-L417](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L417-L417), [README.md#L419-L421](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L419-L421), [README.md#L423-L423](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L423-L423)
  - [observation/documented] With ui.persist_state true (default), toggle hides/restores the UI keeping buffers in memory for fast restore; false fully tears down and recreates buffers, and close() always fully closes. -- evidence: [README.md#L537-L539](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L537-L539), [README.md#L530-L530](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L530-L530), [README.md#L532-L533](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L532-L533)
- orchestration (2 claim(s)):
More evidence: [full detail](opencode.nvim.detail.md)

Metadata and full claim list: [full detail](opencode.nvim.detail.md)
Human notes ([notes](opencode.nvim.notes.md), never overwritten by build)

[Back to map index](../../index.md)
