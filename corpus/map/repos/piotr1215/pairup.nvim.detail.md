# piotr1215/pairup.nvim -- full detail

[Back to orientation](pairup.nvim.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/piotr1215/pairup.nvim/a4841094a58bb9d42591f3c7085411b1ea87a66a/4fa12d5ec32839c7.json](../../../wiki/dossiers/piotr1215/pairup.nvim/a4841094a58bb9d42591f3c7085411b1ea87a66a/4fa12d5ec32839c7.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] A peripheral Claude feature runs a second autonomous Claude instance in a sibling git worktree that receives diffs of spec files and implements changes independently. -- evidence: [README.md#L68-L68](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L68-L68), [README.md#L70-L70](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L70-L70), [README.md#L72-L77](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L72-L77) (`clm_60960c24b6ca95fceb55ce8f5363c1a5d0b246ab3d32b92282057805bc4544ef`)
- [observation/documented] Todo progress is tracked via a Claude Code PostToolUse hook script that the user must copy into ~/.claude/scripts and register in settings.json. -- evidence: [README.md#L309-L320](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L309-L320), [README.md#L302-L305](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L302-L305), [README.md#L300-L300](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L300-L300) (`clm_a19f9d1e0f8877e2b2b09093a6b3658886f964ca086b0ef1add158d713dedfbb`)

## design-choices (1 claim(s))

- [observation/documented] v4.0 removed the overlay system, sessions, RPC, and marker-based suggestions to focus on simple inline editing, citing less complexity and more reliability; legacy features remain on the legacy-v3 branch. -- evidence: [README.md#L5-L14](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L5-L14), [doc/pairup.txt#L29-L36](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/doc/pairup.txt#L29-L36) (`clm_6832875b98dc3c7f7f56ee631750232b967d5c37b96ff8a9d8124b70548a6afc`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (7 claim(s))

- [observation/documented] Users write cc:, cc!:, or ccp: markers in code and save; Claude then edits the file directly, per the README's how-it-works section. -- evidence: [README.md#L18-L18](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L18-L18), [doc/pairup.txt#L40-L41](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/doc/pairup.txt#L40-L41) (`clm_94a436377e36420e43635f534ad3acaf4bf3b00a09a1adfcbe17a72c5dd64a86`)
- [observation/documented] ccp: (plan) makes Claude wrap changes in CURRENT/PROPOSED conflict markers so the user reviews and accepts or rejects before anything changes. -- evidence: [doc/pairup.txt#L53-L56](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/doc/pairup.txt#L53-L56), [README.md#L20-L25](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L20-L25) (`clm_71ec5053dd23050507e718d1c26dacf251aed7c7b425238b301936167a162d3d`)
- [observation/documented] cc!: (constitution) executes the instruction and additionally extracts the underlying rule into the project's CLAUDE.md for future work. -- evidence: [doc/pairup.txt#L49-L51](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/doc/pairup.txt#L49-L51), [README.md#L20-L25](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L20-L25) (`clm_e9622db9799ced98da710a8fbecb7914d1a52a287723dfad1feff114b7b2ff2f`)
- [observation/documented] uu: is Claude's reply marker for clarification questions; the user answers by appending a cc: line below it. -- evidence: [doc/pairup.txt#L58-L64](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/doc/pairup.txt#L58-L64), [README.md#L20-L25](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L20-L25) (`clm_bb6f79e4d9c91f8289f2a9648c2d5116fad29b48756e508ff1de25d2ba470cc9`)
- [observation/documented] The plugin exposes :Pairup subcommands including start, stop, toggle, say, markers, inline, diff, lsp, suspend, accept, and peripheral variants. -- evidence: [doc/pairup.txt#L310-L331](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/doc/pairup.txt#L310-L331), [README.md#L254-L275](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L254-L275) (`clm_485f8162b1d4bbf33922f75f040d078a009aa660a28d3e27b7bb233ca1f5d25d`)
- [observation/documented] Operators gC{motion}, g!{motion}, and g?{motion} insert cc:, cc!:, and ccp: markers respectively, working with motions and text-objects; keybindings are active only when the plugin is loaded. -- evidence: [README.md#L98-L100](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L98-L100), [README.md#L102-L106](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L102-L106), [README.md#L96-L96](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L96-L96) (`clm_7115563d46b64ac1443a5a285560fdb533c7a7bfdb7bb44c8d70f57bb3b684ac`)
- [observation/documented] Statusline indicators are auto-injected into lualine or the native statusline, showing states like [CL:pending], [CL:2/5], [CL:ready], and peripheral [CP] states. -- evidence: [README.md#L288-L292](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L288-L292), [README.md#L281-L286](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L281-L286), [README.md#L279-L279](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L279-L279) (`clm_90a57af4dd3d91a9c6d4a47333443478ed58a9e4f0f6d924aa8427562b10b9c5`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The default provider command includes Claude's --permission-mode acceptEdits flag so Claude edits files without per-change confirmation, which the docs say the inline workflow requires. -- evidence: [README.md#L343-L343](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L343-L343), [README.md#L347-L395](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L347-L395) (`clm_c820833c60e3d0c0850000850886d1892e002915456c0d27c551ec5ff3e2aaef`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Requirements are Neovim 0.11+ and the Claude Code CLI. -- evidence: [README.md#L434-L435](https://github.com/Piotr1215/pairup.nvim/blob/a4841094a58bb9d42591f3c7085411b1ea87a66a/README.md#L434-L435) (`clm_da34287dd0cbc9f238109efd5f0493a44f6b577f0422070364c92302a3f888f8`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

