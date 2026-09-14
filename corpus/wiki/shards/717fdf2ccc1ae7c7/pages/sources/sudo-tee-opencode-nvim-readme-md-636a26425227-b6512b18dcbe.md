---
access: public
aliases: []
claim_ids:
- clm_09b4d6767cebabeb82e24c87f463cba1493e545dde58a8c22913a5642e0944e6
- clm_0b6999515845995de780c194625a6db8ab91f843f97de0b91f941d198394b896
- clm_158e498610f93c3c97771a523d44ae78febef2ee186892d371e9bb64011be9ce
- clm_3dc2f3604b3ce498691173863074b58ea065bc4d92f8ab88a493b8a3bea0fba0
- clm_3effa5b394bd24207d07e90b610c7217b5e339ebd163a1216fad1507b3ebcefc
- clm_401bcd08fe6b427b6b44c8bc8619e9739adeb82b5de8cd12a97e768952ed0b27
- clm_43efeec5a5fa4211c5bd210c008c47016dede64629a6ad312a7ca01b0a0d77aa
- clm_49ca772a38e6eff8ef8ae591fa0ce3d07c2bbbbc0c1d79b39fe631c0b77879b7
- clm_53236c67f284ba1a6764c1985b9b940aaca713a266162841b775a27d8c60e1df
- clm_731b3fd7396788213ab1336c8e49f67a9e2133d389da17aaac53912c914a6f8f
- clm_8b0c50c736686a6886ae1de5a5cb4907fb7ff23cc047fecab1617b8c06ec74eb
- clm_8f8a01e5f8290537cb72641aee6f97caf91a4521a0d43f7c73e98c246df5bab6
- clm_8fe2647361b7676fdf1eab07e073f1c931dc290c5f4773295045f7a0faf0f656
- clm_9dfbb7ff2f78e3f6ff3295ed494798bf0e0d7727197d55f2a9432624c6574eba
- clm_d5621af849e40a0dd4d13787851b4189f0188804f6085142a3652b2004c20a61
maturity: draft
page_id: pg_ee990a78265a521ea79eb6512b18dcbe
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a2bbf80420c95f7ca096a720cb368939
title: sudo-tee/opencode.nvim/README.md @ 636a26425227
updated_at: '2026-09-14T04:24:22Z'
---

# sudo-tee/opencode.nvim/README.md @ 636a26425227

<!-- rcw:begin owner=source:src_a2bbf80420c95f7ca096a720cb368939 block=evidence -->
- The README cautions that the plugin is in early development, may have bugs and breaking changes, and is not recommended for production use yet. [@claim:clm_09b4d6767cebabeb82e24c87f463cba1493e545dde58a8c22913a5642e0944e6]
- The plugin requires the Opencode CLI v0.6.3 or newer to be installed and available. [@claim:clm_0b6999515845995de780c194625a6db8ab91f843f97de0b91f941d198394b896]
- With ui.persist_state true (default), toggle hides/restores the UI keeping buffers in memory for fast restore; false fully tears down and recreates buffers, and close() always fully closes. [@claim:clm_158e498610f93c3c97771a523d44ae78febef2ee186892d371e9bb64011be9ce]
- Permission requests can be answered via a dialog (j/k plus <CR> or number keys), commands like :Opencode permission accept/accept_all/deny, or API functions mapping to once/always/reject responses. [@claim:clm_3dc2f3604b3ce498691173863074b58ea065bc4d92f8ab88a493b8a3bea0fba0]
- Favorite models, toggled with <C-f> in the model picker, show a star icon, sort to the top, and persist across Neovim sessions; the plugin respects the OpenCode CLI storage format. [@claim:clm_3effa5b394bd24207d07e90b610c7217b5e339ebd163a1216fad1507b3ebcefc]
- An experimental quick buffer chat feature (<leader>o/) chats using the current buffer context, capturing visual selections or the current line, and the AI's quick edits are applied by the plugin. [@claim:clm_401bcd08fe6b427b6b44c8bc8619e9739adeb82b5de8cd12a97e768952ed0b27]
- Opencode issues permission requests for potentially destructive operations (file edits, reverts, shell commands, persistent tool access); requests appear inline and must be answered before the action proceeds. [@claim:clm_43efeec5a5fa4211c5bd210c008c47016dede64629a6ad312a7ca01b0a0d77aa]
- A dedicated chat panel window inside Neovim shows previous messages and responses and uses workspace/editor state as context for iterating on code. [@claim:clm_49ca772a38e6eff8ef8ae591fa0ce3d07c2bbbbc0c1d79b39fe631c0b77879b7]
- Recommended lazy.nvim setup lists render-markdown.nvim as a dependency, with optional blink.cmp or nvim-cmp for completion and snacks.nvim, telescope, fzf-lua, or mini.nvim as optional pickers. [@claim:clm_53236c67f284ba1a6764c1985b9b940aaca713a266162841b775a27d8c60e1df]
- Prompts can be run with options overriding the agent, model, or per-prompt context types (current_file, selection, diagnostics, cursor_data), e.g. agent=plan context.current_file.enabled=false. [@claim:clm_731b3fd7396788213ab1336c8e49f67a9e2133d389da17aaac53912c914a6f8f]
- The model picker sorts favorites first (by favoriting order), then recently used models, then others alphabetically; variant selection per model is remembered for future use. [@claim:clm_8b0c50c736686a6886ae1de5a5cb4907fb7ff23cc047fecab1617b8c06ec74eb]
- The server configuration supports custom/external opencode servers with url, port, timeout, spawn_command, auto_kill, path_map, and Basic-auth username/password with env-var fallbacks. [@claim:clm_8f8a01e5f8290537cb72641aee6f97caf91a4521a0d43f7c73e98c246df5bab6]
- Editor context is automatically captured for conversations, including current file, visual selection, mentioned files, diagnostics, and cursor position/line content. [@claim:clm_8fe2647361b7676fdf1eab07e073f1c931dc290c5f4773295045f7a0faf0f656]
- The plugin bridges Neovim and the opencode AI agent, providing a chat interface that captures editor context such as the current file and selections, with persistent sessions tied to the workspace. [@claim:clm_9dfbb7ff2f78e3f6ff3295ed494798bf0e0d7727197d55f2a9432624c6574eba]
- Actions are reachable via default keymaps (e.g. <leader>og toggle), user commands (e.g. :Opencode open input), and Lua API functions such as require('opencode.api').toggle(). [@claim:clm_d5621af849e40a0dd4d13787851b4189f0188804f6085142a3652b2004c20a61]
<!-- rcw:end owner=source:src_a2bbf80420c95f7ca096a720cb368939 block=evidence -->

## Researcher notes

