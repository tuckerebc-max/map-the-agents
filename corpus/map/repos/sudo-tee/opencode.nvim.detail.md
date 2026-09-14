# sudo-tee/opencode.nvim -- full detail

[Back to orientation](opencode.nvim.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sudo-tee/opencode.nvim/636a26425227bb35c622653a65ccab5690927539/166e3c2d123d18b6.json](../../../wiki/dossiers/sudo-tee/opencode.nvim/636a26425227bb35c622653a65ccab5690927539/166e3c2d123d18b6.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The plugin bridges Neovim and the opencode AI agent, providing a chat interface that captures editor context such as the current file and selections, with persistent sessions tied to the workspace. -- evidence: [README.md#L21-L21](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L21-L21) (`clm_9dfbb7ff2f78e3f6ff3295ed494798bf0e0d7727197d55f2a9432624c6574eba`)
- [observation/documented] A dedicated chat panel window inside Neovim shows previous messages and responses and uses workspace/editor state as context for iterating on code. -- evidence: [README.md#L27-L27](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L27-L27) (`clm_49ca772a38e6eff8ef8ae591fa0ce3d07c2bbbbc0c1d79b39fe631c0b77879b7`)
- [observation/documented] An experimental quick buffer chat feature (<leader>o/) chats using the current buffer context, capturing visual selections or the current line, and the AI's quick edits are applied by the plugin. -- evidence: [README.md#L35-L35](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L35-L35) (`clm_401bcd08fe6b427b6b44c8bc8619e9739adeb82b5de8cd12a97e768952ed0b27`)

## design-choices (2 claim(s))

- [observation/documented] Editor context is automatically captured for conversations, including current file, visual selection, mentioned files, diagnostics, and cursor position/line content. -- evidence: [README.md#L788-L794](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L788-L794), [README.md#L786-L786](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L786-L786) (`clm_8fe2647361b7676fdf1eab07e073f1c931dc290c5f4773295045f7a0faf0f656`)
- [observation/documented] The model picker sorts favorites first (by favoriting order), then recently used models, then others alphabetically; variant selection per model is remembered for future use. -- evidence: [README.md#L411-L413](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L411-L413), [README.md#L435-L435](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L435-L435) (`clm_8b0c50c736686a6886ae1de5a5cb4907fb7ff23cc047fecab1617b8c06ec74eb`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: recipe contributions should use the provided template, start from the problem being solved, include a GIF demo, give step-by-step setup instructions, cross-reference related recipes, and be self-contained. -- evidence: [docs/README.md#L17-L20](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/docs/README.md#L17-L20), [docs/README.md#L22-L22](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/docs/README.md#L22-L22), [docs/README.md#L15-L15](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/docs/README.md#L15-L15) (`clm_99fb369f209c07d12b7b1ee9e4962c6f4328c5fd2be596fe0055f682510ba296`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Actions are reachable via default keymaps (e.g. <leader>og toggle), user commands (e.g. :Opencode open input), and Lua API functions such as require('opencode.api').toggle(). -- evidence: [README.md#L656-L718](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L656-L718), [README.md#L654-L654](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L654-L654) (`clm_d5621af849e40a0dd4d13787851b4189f0188804f6085142a3652b2004c20a61`)
- [observation/documented] The plugin exposes a diff view of modified files since the last prompt via :Opencode diff_open, :Opencode diff open, pressing D on a 'Created Snapshot' output, or the default <leader>od keymap. -- evidence: [docs/recipes/change-by-change-review/README.md#L10-L12](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/docs/recipes/change-by-change-review/README.md#L10-L12) (`clm_c20d380087d31052ea4c799747cad3915c374858eac35b41fb2316bc65e94a42`)
- [observation/documented] Prompts can be run with options overriding the agent, model, or per-prompt context types (current_file, selection, diagnostics, cursor_data), e.g. agent=plan context.current_file.enabled=false. -- evidence: [README.md#L761-L764](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L761-L764), [README.md#L747-L755](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L747-L755) (`clm_731b3fd7396788213ab1336c8e49f67a9e2133d389da17aaac53912c914a6f8f`)

## memory-state (2 claim(s))

- [observation/documented] Favorite models, toggled with <C-f> in the model picker, show a star icon, sort to the top, and persist across Neovim sessions; the plugin respects the OpenCode CLI storage format. -- evidence: [README.md#L417-L417](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L417-L417), [README.md#L419-L421](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L419-L421), [README.md#L423-L423](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L423-L423) (`clm_3effa5b394bd24207d07e90b610c7217b5e339ebd163a1216fad1507b3ebcefc`)
- [observation/documented] With ui.persist_state true (default), toggle hides/restores the UI keeping buffers in memory for fast restore; false fully tears down and recreates buffers, and close() always fully closes. -- evidence: [README.md#L537-L539](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L537-L539), [README.md#L530-L530](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L530-L530), [README.md#L532-L533](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L532-L533) (`clm_158e498610f93c3c97771a523d44ae78febef2ee186892d371e9bb64011be9ce`)

## orchestration (2 claim(s))

- [observation/documented] The server configuration supports custom/external opencode servers with url, port, timeout, spawn_command, auto_kill, path_map, and Basic-auth username/password with env-var fallbacks. -- evidence: [README.md#L127-L137](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L127-L137) (`clm_8f8a01e5f8290537cb72641aee6f97caf91a4521a0d43f7c73e98c246df5bab6`)
- [observation/documented] A bidirectional-sync recipe shares one HTTP server (default port 4096) between the opencode TUI and the nvim plugin so session state persists across switches; the TUI attaches via 'opencode attach' and the server stays alive until manually killed. -- evidence: [docs/recipes/bidirectional-sync/README.md#L21-L23](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/docs/recipes/bidirectional-sync/README.md#L21-L23), [docs/recipes/bidirectional-sync/README.md#L79-L82](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/docs/recipes/bidirectional-sync/README.md#L79-L82), [docs/recipes/bidirectional-sync/README.md#L19-L19](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/docs/recipes/bidirectional-sync/README.md#L19-L19) (`clm_a82290514b057ff325c8033eb9f424dff77f5beeb654cfe8cc9aabefb63f2d42`)

## tools-permissions (2 claim(s))

- [observation/documented] Opencode issues permission requests for potentially destructive operations (file edits, reverts, shell commands, persistent tool access); requests appear inline and must be answered before the action proceeds. -- evidence: [README.md#L768-L768](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L768-L768) (`clm_43efeec5a5fa4211c5bd210c008c47016dede64629a6ad312a7ca01b0a0d77aa`)
- [observation/documented] Permission requests can be answered via a dialog (j/k plus <CR> or number keys), commands like :Opencode permission accept/accept_all/deny, or API functions mapping to once/always/reject responses. -- evidence: [README.md#L777-L780](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L777-L780) (`clm_3dc2f3604b3ce498691173863074b58ea065bc4d92f8ab88a493b8a3bea0fba0`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The plugin requires the Opencode CLI v0.6.3 or newer to be installed and available. -- evidence: [README.md#L71-L71](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L71-L71), [README.md#L77-L77](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L77-L77) (`clm_0b6999515845995de780c194625a6db8ab91f843f97de0b91f941d198394b896`)
- [observation/documented] Recommended lazy.nvim setup lists render-markdown.nvim as a dependency, with optional blink.cmp or nvim-cmp for completion and snacks.nvim, telescope, fzf-lua, or mini.nvim as optional pickers. -- evidence: [README.md#L85-L102](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L85-L102), [README.md#L104-L111](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L104-L111) (`clm_53236c67f284ba1a6764c1985b9b940aaca713a266162841b775a27d8c60e1df`)

## limitations (1 claim(s))

- [observation/documented] The README cautions that the plugin is in early development, may have bugs and breaking changes, and is not recommended for production use yet. -- evidence: [README.md#L69-L69](https://github.com/sudo-tee/opencode.nvim/blob/636a26425227bb35c622653a65ccab5690927539/README.md#L69-L69) (`clm_09b4d6767cebabeb82e24c87f463cba1493e545dde58a8c22913a5642e0944e6`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

