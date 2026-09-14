---
access: public
aliases: []
claim_ids:
- clm_28a390ed4616a085c05558bea2c20495b5f70a3aa95d208eb196e26f2b162aa0
- clm_51a9c1b91ad342590ec9159e66c0fad19de7bc4aa6eb16e11e3a7710982eb3e6
- clm_5b36b0ea4a337697cb3b8da3f5f2956ba55038e9f6355dc951a6aabf620967bd
- clm_62ad7e0089384df6254c03da4eb470dacf1fc945e1bed692886c4dcb1aed1a3f
- clm_6618eb0df2f2fd1ff23c07c8c861a578638e68cc71e2fc064fed57c622218136
- clm_69a750720892e130c64a1c2becf3f1138e584f8770b09cf3532caa2634c0953e
- clm_a4fe14f010e1d0b7237efcdaac5abdd9fc6c503e8d1d25323645ee0c79e65e94
- clm_a7db40426f031c7e0e8272dc339cf8e356cfd0a106f3e1396a92f06ee7fb8f4a
- clm_bb1cd15dba29e82634dbb26b02229ed71cc9bab73fa7bb46298fd724c3a57c5d
- clm_d77bfa6588d952a8cbbe61cce0cd8d11581593368eb685a00d10818ad53f2ddc
- clm_e3d7c9a0bafda0c239d62511456a473786c1c82887005c5f7070fe56e0d8780a
- clm_eabac3ec142aeca91f8738484861ea3c1896c9a0de38ff28044478d7cbad3ca9
maturity: draft
page_id: pg_8ed8cb16aa8a5bb1aa46c5c1497681a0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d5f093c182785dbcb8b593ed8c1bf86f
title: pablopunk/pi.nvim/README.md @ fab2a7932a54
updated_at: '2026-09-14T04:15:03Z'
---

# pablopunk/pi.nvim/README.md @ fab2a7932a54

<!-- rcw:begin owner=source:src_d5f093c182785dbcb8b593ed8c1bf86f block=evidence -->
- Requires Neovim 0.10+ and a globally installed pi binary, installed via a curl script; models must be available in pi. [@claim:clm_28a390ed4616a085c05558bea2c20495b5f70a3aa95d208eb196e26f2b162aa0]
- Setting a custom system_prompt overrides pi's generated baseline instructions, which the README flags as something to use with care. [@claim:clm_51a9c1b91ad342590ec9159e66c0fad19de7bc4aa6eb16e11e3a7710982eb3e6]
- Status updates use nvim-notify or mini.notify when available, falling back to a floating status window otherwise. [@claim:clm_5b36b0ea4a337697cb3b8da3f5f2956ba55038e9f6355dc951a6aabf620967bd]
- The tools option lets users restrict pi's tools; read, edit, and write are always enabled, and an empty list disables bash. [@claim:clm_62ad7e0089384df6254c03da4eb470dacf1fc945e1bed692886c4dcb1aed1a3f]
- The plugin wraps the external pi CLI binary (default "pi", configurable to a custom path or wrapper command array) rather than implementing the agent itself. [@claim:clm_6618eb0df2f2fd1ff23c07c8c861a578638e68cc71e2fc064fed57c622218136]
- Requests run asynchronously so editing stays nonblocking, and changed loaded buffers are reloaded after successful pi edits. [@claim:clm_69a750720892e130c64a1c2becf3f1138e584f8770b09cf3532caa2634c0953e]
- The plugin exposes four user commands: :PiAsk (normal mode, prompts and sends buffer context), :PiAskSelection (visual), :PiCancel, and :PiLog which opens a session log split. [@claim:clm_a4fe14f010e1d0b7237efcdaac5abdd9fc6c503e8d1d25323645ee0c79e65e94]
- A Lua setup API is documented via require("pi").setup with all options optional, plus programmatic get_cmd() and run() functions. [@claim:clm_a7db40426f031c7e0e8272dc339cf8e356cfd0a106f3e1396a92f06ee7fb8f4a]
- Oversized context is trimmed (default max 24000 bytes) for speed rather than always sending the full file. [@claim:clm_bb1cd15dba29e82634dbb26b02229ed71cc9bab73fa7bb46298fd724c3a57c5d]
- Configuration options include binary path, provider, model, thinking level (off through xhigh), tools list, system prompts, and context sizing knobs like max_bytes and surrounding_lines. [@claim:clm_d77bfa6588d952a8cbbe61cce0cd8d11581593368eb685a00d10818ad53f2ddc]
- No default keymaps are set; users configure their own, with example mappings for :PiAsk and :PiAskSelection provided. [@claim:clm_e3d7c9a0bafda0c239d62511456a473786c1c82887005c5f7070fe56e0d8780a]
- Context sent to pi includes the current buffer, cwd, selection, and optionally LSP/linter diagnostics via vim.diagnostic, with unsaved buffer content treated as the source of truth over disk. [@claim:clm_eabac3ec142aeca91f8738484861ea3c1896c9a0de38ff28044478d7cbad3ca9]
<!-- rcw:end owner=source:src_d5f093c182785dbcb8b593ed8c1bf86f block=evidence -->

## Researcher notes

