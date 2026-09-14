# pablopunk/pi.nvim -- full detail

[Back to orientation](pi.nvim.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/pablopunk/pi.nvim/fab2a7932a5478e522d609a9fd39a7aac6c0440d/91394a9b37fe7fe2.json](../../../wiki/dossiers/pablopunk/pi.nvim/fab2a7932a5478e522d609a9fd39a7aac6c0440d/91394a9b37fe7fe2.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The plugin wraps the external pi CLI binary (default "pi", configurable to a custom path or wrapper command array) rather than implementing the agent itself. -- evidence: [README.md#L56-L80](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L56-L80), [README.md#L82-L96](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L82-L96) (`clm_6618eb0df2f2fd1ff23c07c8c861a578638e68cc71e2fc064fed57c622218136`)

## design-choices (3 claim(s))

- [observation/documented] Configuration options include binary path, provider, model, thinking level (off through xhigh), tools list, system prompts, and context sizing knobs like max_bytes and surrounding_lines. -- evidence: [README.md#L56-L80](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L56-L80), [README.md#L82-L96](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L82-L96) (`clm_d77bfa6588d952a8cbbe61cce0cd8d11581593368eb685a00d10818ad53f2ddc`)
- [observation/documented] The tools option lets users restrict pi's tools; read, edit, and write are always enabled, and an empty list disables bash. -- evidence: [README.md#L82-L96](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L82-L96) (`clm_62ad7e0089384df6254c03da4eb470dacf1fc945e1bed692886c4dcb1aed1a3f`)
- [observation/documented] Oversized context is trimmed (default max 24000 bytes) for speed rather than always sending the full file. -- evidence: [README.md#L147-L152](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L147-L152), [README.md#L82-L96](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L82-L96) (`clm_bb1cd15dba29e82634dbb26b02229ed71cc9bab73fa7bb46298fd724c3a57c5d`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The plugin exposes four user commands: :PiAsk (normal mode, prompts and sends buffer context), :PiAskSelection (visual), :PiCancel, and :PiLog which opens a session log split. -- evidence: [README.md#L138-L143](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L138-L143) (`clm_a4fe14f010e1d0b7237efcdaac5abdd9fc6c503e8d1d25323645ee0c79e65e94`)
- [observation/documented] No default keymaps are set; users configure their own, with example mappings for :PiAsk and :PiAskSelection provided. -- evidence: [README.md#L130-L132](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L130-L132), [README.md#L124-L124](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L124-L124), [README.md#L126-L128](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L126-L128) (`clm_e3d7c9a0bafda0c239d62511456a473786c1c82887005c5f7070fe56e0d8780a`)
- [observation/documented] A Lua setup API is documented via require("pi").setup with all options optional, plus programmatic get_cmd() and run() functions. -- evidence: [README.md#L157-L157](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L157-L157), [README.md#L50-L52](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L50-L52), [README.md#L48-L48](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L48-L48) (`clm_a7db40426f031c7e0e8272dc339cf8e356cfd0a106f3e1396a92f06ee7fb8f4a`)

## memory-state (1 claim(s))

- [observation/documented] Context sent to pi includes the current buffer, cwd, selection, and optionally LSP/linter diagnostics via vim.diagnostic, with unsaved buffer content treated as the source of truth over disk. -- evidence: [README.md#L15-L18](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L15-L18), [README.md#L147-L152](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L147-L152) (`clm_eabac3ec142aeca91f8738484861ea3c1896c9a0de38ff28044478d7cbad3ca9`)

## orchestration (1 claim(s))

- [observation/documented] Requests run asynchronously so editing stays nonblocking, and changed loaded buffers are reloaded after successful pi edits. -- evidence: [README.md#L147-L152](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L147-L152) (`clm_69a750720892e130c64a1c2becf3f1138e584f8770b09cf3532caa2634c0953e`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Requires Neovim 0.10+ and a globally installed pi binary, installed via a curl script; models must be available in pi. -- evidence: [README.md#L22-L24](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L22-L24) (`clm_28a390ed4616a085c05558bea2c20495b5f70a3aa95d208eb196e26f2b162aa0`)
- [observation/documented] Status updates use nvim-notify or mini.notify when available, falling back to a floating status window otherwise. -- evidence: [README.md#L147-L152](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L147-L152) (`clm_5b36b0ea4a337697cb3b8da3f5f2956ba55038e9f6355dc951a6aabf620967bd`)

## limitations (1 claim(s))

- [observation/documented] Setting a custom system_prompt overrides pi's generated baseline instructions, which the README flags as something to use with care. -- evidence: [README.md#L82-L96](https://github.com/pablopunk/pi.nvim/blob/fab2a7932a5478e522d609a9fd39a7aac6c0440d/README.md#L82-L96) (`clm_51a9c1b91ad342590ec9159e66c0fad19de7bc4aa6eb16e11e3a7710982eb3e6`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

