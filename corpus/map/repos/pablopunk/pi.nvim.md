# pablopunk/pi.nvim

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fab2a7932a54 @ 91394a9b37fe7fe2

## Summary (orientation draft, not independently verified)

pi.nvim is a Neovim plugin integrating the pi CLI agent, sending buffer/selection context and exposing commands like :PiAsk. Evidence is README-only documentation of configuration, commands, and behavior.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The plugin wraps the external pi CLI binary (default "pi", configurable to a custom path or wrapper command array) rather than implementing the agent itself. -- evidence: [README.md#L56-L80](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L56-L80), [README.md#L82-L96](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L82-L96)
- design-choices (3 claim(s)):
  - [observation/documented] Configuration options include binary path, provider, model, thinking level (off through xhigh), tools list, system prompts, and context sizing knobs like max_bytes and surrounding_lines. -- evidence: [README.md#L56-L80](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L56-L80), [README.md#L82-L96](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L82-L96)
  - [observation/documented] The tools option lets users restrict pi's tools; read, edit, and write are always enabled, and an empty list disables bash. -- evidence: [README.md#L82-L96](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L82-L96)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The plugin exposes four user commands: :PiAsk (normal mode, prompts and sends buffer context), :PiAskSelection (visual), :PiCancel, and :PiLog which opens a session log split. -- evidence: [README.md#L138-L143](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L138-L143)
  - [observation/documented] No default keymaps are set; users configure their own, with example mappings for :PiAsk and :PiAskSelection provided. -- evidence: [README.md#L130-L132](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L130-L132), [README.md#L124-L124](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L124-L124), [README.md#L126-L128](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L126-L128)
- memory-state (1 claim(s)):
  - [observation/documented] Context sent to pi includes the current buffer, cwd, selection, and optionally LSP/linter diagnostics via vim.diagnostic, with unsaved buffer content treated as the source of truth over disk. -- evidence: [README.md#L15-L18](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L15-L18), [README.md#L147-L152](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L147-L152)
- orchestration (1 claim(s)):
  - [observation/documented] Requests run asynchronously so editing stays nonblocking, and changed loaded buffers are reloaded after successful pi edits. -- evidence: [README.md#L147-L152](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L147-L152)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Requires Neovim 0.10+ and a globally installed pi binary, installed via a curl script; models must be available in pi. -- evidence: [README.md#L22-L24](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L22-L24)
  - [observation/documented] Status updates use nvim-notify or mini.notify when available, falling back to a floating status window otherwise. -- evidence: [README.md#L147-L152](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L147-L152)
- limitations (1 claim(s)):
  - [observation/documented] Setting a custom system_prompt overrides pi's generated baseline instructions, which the README flags as something to use with care. -- evidence: [README.md#L82-L96](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L82-L96)
- relevance: unknown (no source-linked claim submitted for this facet)

(2 additional claim(s) omitted for length; see [full detail](pi.nvim.detail.md) for every claim.)

Metadata and full claim list: [full detail](pi.nvim.detail.md)
Human notes ([notes](pi.nvim.notes.md), never overwritten by build)

[Back to map index](../../index.md)
