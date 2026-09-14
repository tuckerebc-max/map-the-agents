# cpoile/claudemacs -- full detail

[Back to orientation](claudemacs.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/cpoile/claudemacs/1f2fe7bbc718ca1b08eee316340d188be9f1564b/21761bc18dec649d.json](../../../wiki/dossiers/cpoile/claudemacs/1f2fe7bbc718ca1b08eee316340d188be9f1564b/21761bc18dec649d.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (3 claim(s))

- [observation/documented] The package supports multiple terminal backends: Ghostel is selected automatically when available, otherwise it falls back to Eat; the backend can be forced via claudemacs-terminal-backend. -- evidence: [README.md#L154-L155](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L154-L155), [README.md#L150-L152](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L150-L152), [README.md#L13-L31](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L13-L31), [README.md#L145-L148](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L145-L148) (`clm_b077a3d34ec28fa2eefdee7350430a793c916292561ef60df558e34894ac0733`)
- [observation/documented] A configurable tool registry defines which AI CLI tools are available, with defaults Claude, Codex, and Gemini, each with program, switches, and model-types entries; users can add tools like aider. -- evidence: [README.md#L478-L478](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L478-L478), [README.md#L491-L499](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L491-L499), [README.md#L480-L489](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L480-L489) (`clm_476905049b6a57a6236546ea54f59ae288eb7f728f565a11f16cd31222c7455c`)
- [observation/documented] System notifications fire (with sound) when the AI tool awaits input or finishes, with per-OS configuration for macOS sounds, Linux notify-send auto-dismiss and canberra sounds, and Windows toast timeouts. -- evidence: [README.md#L197-L197](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L197-L197), [README.md#L236-L236](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L236-L236), [README.md#L616-L619](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L616-L619), [README.md#L624-L627](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L624-L627), [README.md#L13-L31](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L13-L31), [README.md#L218-L220](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L218-L220), [README.md#L209-L209](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L209-L209) (`clm_bccf8c3837cb10d79465eaf2b07d0c3a7b7c5e64796e1f26ddb3198d52bcb882`)

## design-choices (5 claim(s))

- [observation/documented] The project's stated design philosophy is simplicity: let the LLM CLI run in the terminal without agents, MCP, or IDE integration, which the README says would consume context. -- evidence: [README.md#L8-L9](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L8-L9) (`clm_01711f2fdead377bf7f04a760325929316bac472befa423baa88aeb7f32cdd55`)
- [observation/documented] Sessions are workspace-aware: the session is keyed to the Doom/Perspective workspace and the tool's cwd defaults to the project's git root, enabling separate sessions per workspace in a monorepo. -- evidence: [README.md#L363-L367](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L363-L367) (`clm_29bf2d6f0a45f0496ae3846729452abbd53f7c85d24ad6462aa6ea8c105b09bb`)
- [observation/documented] The backend selector is checked only at session start and affects new sessions; an invalid or unloadable selection raises an error rather than silently falling back to another backend. -- evidence: [README.md#L165-L168](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L165-L168) (`clm_e72675cece2ecb11d243fd2ed1a4cbb4664b7bb10ec6060362858f3bf8e4fca0`)
- [observation/documented] Claudemacs presents the same session and action commands regardless of which terminal backend is in use. -- evidence: [README.md#L145-L148](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L145-L148) (`clm_6f3aa1b01844e56b2fd31d8c038278c02b27a5a7e84044fbe2df1af11a8a6de9`)
- [observation/documented] When claudemacs-prefer-projectile-root is set, the tool's cwd uses the projectile root instead of the git root, letting Claude Code read and edit files across sibling repos in a monorepo layout. -- evidence: [README.md#L392-L392](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L392-L392), [README.md#L373-L375](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L373-L375), [README.md#L371-L371](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L371-L371) (`clm_15693131a7e4d2c461a0dfc2e15659b09d4156fc9b7600418f116d630900337e`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (6 claim(s))

- [observation/documented] Claudemacs exposes a transient menu (default binding C-c C-e) with core commands for starting, switching, resuming, listing, and killing sessions, plus action commands like fix-error-at-point and implement-comment. -- evidence: [README.md#L420-L427](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L420-L427), [README.md#L443-L450](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L443-L450), [README.md#L418-L418](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L418-L418) (`clm_07e61166e02e006eadadc263d7c6305e22ece1bf8f8f7fdcdfe5b5e829e6a2ae`)
- [observation/documented] Action commands accept a C-u prefix to broadcast the action to all active sessions. -- evidence: [README.md#L13-L31](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L13-L31), [README.md#L443-L450](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L443-L450) (`clm_8e3ac48445948cd819795c05d0f63d7662b5d5602bf1cf47b5a94826ad9aba5d`)
- [observation/documented] Session buffers are named *claudemacs:TOOL(-N):SESSION-ID*, where SESSION-ID is the workspace name or project path and -N distinguishes multiple instances of the same tool. -- evidence: [README.md#L646-L649](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L646-L649), [README.md#L651-L654](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L651-L654) (`clm_e19688f777d6dcb8a13aa289229d3674bbcf2a28a236d43ffd9b94d87e383b43`)
- [observation/documented] M-x claudemacs-session-list shows a table of live sessions with workspace, tool instance, and project directory columns; exited sessions disappear on refresh and no CLI history is shown. -- evidence: [README.md#L467-L467](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L467-L467), [README.md#L469-L469](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L469-L469) (`clm_e46cda62bc9fc3e8dbc223ebc9b69aed69a968af80ac943e6990bc5d75c6f534`)
- [observation/documented] In semi-char mode, C-q acts as a quoted-input escape hatch to send literal control characters (e.g., C-q C-g sends Ctrl-g to Claude Code), while C-g itself is mapped to send ESC. -- evidence: [README.md#L702-L702](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L702-L702), [README.md#L706-L708](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L706-L708) (`clm_c7669d6f1cfa1f10a66db4ad5dbdc2fc1f2d37bd46c85894f2b3e73dfd50efa1`)
- [observation/documented] The terminal buffer has two interaction modes: a semi-char mode for typing directly to the AI tool and an Emacs mode (C-c C-e) for editing terminal contents, with C-c C-j returning to semi-char mode. -- evidence: [README.md#L662-L664](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L662-L664), [README.md#L671-L672](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L671-L672) (`clm_c68efe2d806c40f6837680faeb8cbfba647e1d3092e788004f840a1a392dab44`)

## memory-state (1 claim(s))

- [observation/documented] Sessions can be resumed using tool-specific resume flags, and the resume submenu supports resuming a Codex session by UUID. -- evidence: [README.md#L437-L441](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L437-L441), [README.md#L13-L31](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L13-L31) (`clm_e2f206886c7ab0b249b1bf934a69282191c031b65cf83a25a5b3ed78edf013ed`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] The start-session submenu offers a -d switch to skip permissions (--dangerously-skip-permissions or equivalent) when launching a tool. -- evidence: [README.md#L437-L441](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L437-L441) (`clm_9f62331c5650a82ea4704e5594a77d33578039f522966b513d945630bfd83a13`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Requirements are Emacs 28.1+, the Eat package or Ghostel with its native module, transient (built-in since Emacs 28), and a supported AI CLI such as Claude Code. -- evidence: [README.md#L734-L737](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L734-L737) (`clm_d5bd91cc7b9707dc6b81263e37d3caf092541479f4f2996098b8a0b300d45509`)
- [observation/documented] Only the selected terminal backend is loaded; both Eat and Ghostel need not be installed, but the chosen backend must be installed and loadable before starting a session. -- evidence: [README.md#L69-L71](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L69-L71) (`clm_ba5988dffa1f8669b535e1764a480b9ae58a9b2e912cec2170f99cff33eb0765`)

## limitations (2 claim(s))

- [observation/documented] On macOS, clicking a system notification does not bring focus to Emacs; the README notes this limitation and solicits ideas. -- evidence: [README.md#L205-L205](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L205-L205) (`clm_080b1f5f453171e29b63660d69c9c2b98eac18068d0d64efb1997af9fc23a615`)
- [observation/documented] Terminal-emulator interactions with Claude Code can cause scroll-popping, a stuck input box, or border-drawing issues after window resize; a 'u' unstick command resets the buffer for both backends. -- evidence: [README.md#L722-L724](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L722-L724), [README.md#L712-L717](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L712-L717), [README.md#L719-L720](https://github.com/cpoile/claudemacs/blob/1f2fe7bbc718ca1b08eee316340d188be9f1564b/README.md#L719-L720) (`clm_d5cdf680c0f5c61034e77464009389fae85eb98155a022f0ae08fb1fb328728f`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

