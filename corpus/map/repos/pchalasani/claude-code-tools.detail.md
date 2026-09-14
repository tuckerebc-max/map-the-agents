# pchalasani/claude-code-tools -- full detail

[Back to orientation](claude-code-tools.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/pchalasani/claude-code-tools/ee0f3099c05c50141feff2559193c0af1fb81ec7/97d770c6b369880b.json](../../../wiki/dossiers/pchalasani/claude-code-tools/ee0f3099c05c50141feff2559193c0af1fb81ec7/97d770c6b369880b.json)

## specifications (1 claim(s))

- [observation/documented] The project provides CLI tools, skills, agents, hooks, and plugins intended to enhance productivity with Claude Code and other coding agents. -- evidence: [README.md#L8-L8](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/README.md#L8-L8) (`clm_0c13d24be1a1a669b6e20657aa86faea8e9ae9c7747d1d8aeff481a48c785435`)

## components (4 claim(s))

- [observation/documented] The >share hook (hooks/share_hook.py) is a standalone stdlib UserPromptSubmit hook that reads session_id/cwd/transcript_path from stdin, writes an fcntl-locked atomic registry, and blocks the prompt to print the handle. -- evidence: [docs/agent-tunnel-spec.md#L64-L69](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L64-L69) (`clm_1298c9ef91d5d6a6528a1bc0dba091a7b5c8f7585a7cf7bc864dd19b9e9c3a0a`)
- [observation/documented] Inbound attachments are downloaded to a per-thread uploads dir outside any repo and exposed to the fork via --add-dir, with per-file size and count caps; oversized or excess files are skipped with a notice. -- evidence: [docs/agent-tunnel-spec.md#L188-L196](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L188-L196) (`clm_adc7f9e1fbae4d3131568fe08021103e58bf45cd72c7ee4b5bdb90cd9e9a1f14`)
- [observation/documented] Write/bash forks save deliverables to .agent-tunnel-out/<thread>/; the bot snapshots and diffs that dir to post new or modified files as Discord attachments, and a wildcard .gitignore keeps deliverables out of git status. -- evidence: [docs/agent-tunnel-spec.md#L207-L215](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L207-L215) (`clm_672792543a29b3a6dc03c2bac185826b610c4c791a586907f87e34a8ca5eb465`)
- [observation/documented] find-claude-session maps a project directory to ~/.claude/projects/<path with slashes replaced by dashes>, streams JSONL line by line, requires all keywords case-insensitively, sorts by modification time, and shows the top 10 matches. -- evidence: [docs/find-claude-session.md#L43-L46](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/find-claude-session.md#L43-L46), [docs/find-claude-session.md#L48-L52](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/find-claude-session.md#L48-L52), [docs/find-claude-session.md#L54-L58](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/find-claude-session.md#L54-L58) (`clm_098c74ed0d2c35d80eb08d50034835ecbde6526d89b5d276b8f2e3af7ca7e7e7`)

## design-choices (2 claim(s))

- [observation/documented] Threads answer via --resume with --fork-session so the original session is untouched; remote turns run with --allowedTools Read,Grep,Glob, an explicit deny list, and --permission-mode dontAsk. -- evidence: [docs/agent-tunnel-spec.md#L19-L40](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L19-L40) (`clm_f451ca94e7446318f904cc67fdc9875255560ea910e631fde566a473d91c2b0d`)
- [observation/documented] agent-tunnel uses no inbound tunnel: it connects via the Discord Gateway's outbound websocket, so nothing on the machine is internet-reachable. -- evidence: [docs/agent-tunnel-spec.md#L19-L40](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L19-L40) (`clm_6734c7ab7fedbd3bc28dc4b08fed6159d4e47ecb4b0c4cca5438973325155295`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the agent-tunnel spec reports unit tests using real files without mocks, covering the registry, hook, store, session discovery, flag building, config, and attachment handling. -- evidence: [docs/agent-tunnel-spec.md#L281-L294](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L281-L294) (`clm_72d4a6321fc48c7c7b9efdf8c179b674385bf8e53d666b1887fd9ad4b44dacb8`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] agent-tunnel exposes long-lived local Claude Code sessions ('experts') to teammates over Discord; a session is published at runtime with >share and addressed by a short handle, with each conversation answered against a read-only fork. -- evidence: [docs/agent-tunnel-spec.md#L3-L7](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L3-L7) (`clm_27202477a165f912b1e66bb9379a7f51e62d22ab118c365c9e88e760be7c5f7a`)
- [observation/documented] In a watched channel, '<handle> [question]' opens a Discord thread bound to that session with follow-ups staying in the thread; !list/!handles list active handles; !done/!close/!end tear down the fork immediately. -- evidence: [docs/agent-tunnel-spec.md#L168-L181](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L168-L181) (`clm_26415cee010dbd178c9aed47a3f9bdf242cbc1dc0c83f79206572dc9adfd382f`)
- [observation/documented] find-claude-session is a CLI that keyword-searches Claude Code session files with an interactive selection UI and automatic resumption via claude -r; a -g/--global flag searches across all projects. -- evidence: [docs/find-claude-session.md#L9-L13](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/find-claude-session.md#L9-L13), [docs/find-claude-session.md#L5-L5](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/find-claude-session.md#L5-L5), [docs/find-claude-session.md#L26-L29](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/find-claude-session.md#L26-L29) (`clm_81db7311c1cca63c59ee9d4fc09f6bd5a58ff79ca078086b811c0c0ea82a40e1`)

## memory-state (1 claim(s))

- [observation/documented] The config dir is propagated end to end: the hook derives it from transcript_path and records it in the registry, and the daemon pins each fork via CLAUDE_CONFIG_DIR so work and personal sessions fork under their own config/account. -- evidence: [docs/agent-tunnel-spec.md#L226-L231](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L226-L231), [docs/agent-tunnel-spec.md#L221-L224](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L221-L224) (`clm_d61005b097b552348cadf1a37cd77e02c5481b6b7472afb4fa44fbfacee8ab1c`)

## orchestration (1 claim(s))

- [observation/documented] agent-tunnel supports two backends: headless (default) runs claude -p per question with clean JSON I/O, while tmux runs an interactive claude per thread in a private tmux server window, watchable via agent-tunnel watch. -- evidence: [docs/agent-tunnel-spec.md#L243-L259](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L243-L259) (`clm_53b690b8c997afefeb80c402807cd315948bf5e822d89fdbc86be2c518184484`)

## tools-permissions (2 claim(s))

- [observation/documented] Per-handle access levels: --write adds Write/Edit/NotebookEdit (never Bash); --dangerously-allow-bash adds command execution; --dangerously-skip-permissions lets the fork use any tool or MCP server the session has. -- evidence: [docs/agent-tunnel-spec.md#L137-L164](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L137-L164) (`clm_680c1219b2532e636a8881cbd2bc6fa99fdc7d8f3979fdab7f549f4eadcb6028`)
- [observation/documented] Security model: read-only tools are hard-enforced by the CLI permission layer by default; access is Discord channel membership plus optional user/role allowlists, and the persona's discouragement of leaking secrets is described as a soft layer only. -- evidence: [docs/agent-tunnel-spec.md#L263-L277](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L263-L277) (`clm_56f7787c1dcb25553bcdf1dbe3b58d0caaebd513078f45089da8ab348e1e9fda`)

## evaluation (1 claim(s))

- [observation/documented] The spec reports live end-to-end validation of agent-tunnel in both headless mode and tmux-over-Discord, confirming forked sessions inherit context and follow-ups continue the same fork. -- evidence: [docs/agent-tunnel-spec.md#L281-L294](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L281-L294) (`clm_de6afbb8995390a98cd9d4a17336cfa38dfb53e55f7edaf03fc074e6095cfb08`)

## dependencies (3 claim(s))

- [observation/documented] README badges link the package to PyPI as claude-code-tools and to a Rust crate named aichat-search on crates.io. -- evidence: [README.md#L10-L14](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/README.md#L10-L14) (`clm_b802df94b0c4cefbe1da936282e938a2d1622ddd86d66c18a32d62a722e46786`)
- [observation/documented] Binary Office attachments are best-effort converted using whatever converter is on PATH (LibreOffice→PDF preferred, else pandoc→Markdown, else macOS textutil); no converter is a hard dependency, and PDF/images/text work unaided. -- evidence: [docs/agent-tunnel-spec.md#L198-L205](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L198-L205) (`clm_8e547980325ffe280d0dbc15b900bee6c6c1a316fe50316f3e5eeef9fc5e50e2`)
- [observation/documented] find-claude-session requires Python 3.11+ and click, with rich as an optional dependency for the interactive UI. -- evidence: [docs/find-claude-session.md#L83-L85](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/find-claude-session.md#L83-L85) (`clm_b7423a1778e84c83b35ead9ca8b2b9e18d8ce3a69fdd10e9aefbb219b2779611`)

## limitations (1 claim(s))

- [observation/documented] The spec notes a ToS gray area: consumer plans prohibit making your account available to others, and headless with an API key is described as the unambiguous path. -- evidence: [docs/agent-tunnel-spec.md#L263-L277](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/agent-tunnel-spec.md#L263-L277) (`clm_40dfded60246ce70ea24eed84e923f6c75228ab9106bb42aca29977378d07c20`)

## relevance (1 claim(s))

- [observation/documented] The docs include a Zsh shell setup guide covering Oh My Zsh with autosuggestions and syntax-highlighting plugins, the Starship prompt, eza aliases, and Atuin or HSTR history tools. -- evidence: [docs/dot-zshrc.md#L169-L169](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/dot-zshrc.md#L169-L169), [docs/dot-zshrc.md#L70-L70](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/dot-zshrc.md#L70-L70), [docs/dot-zshrc.md#L187-L189](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/dot-zshrc.md#L187-L189), [docs/dot-zshrc.md#L115-L119](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/dot-zshrc.md#L115-L119), [docs/dot-zshrc.md#L55-L59](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/dot-zshrc.md#L55-L59), [docs/dot-zshrc.md#L3-L4](https://github.com/pchalasani/claude-code-tools/blob/ee0f3099c05c50141feff2559193c0af1fb81ec7/docs/dot-zshrc.md#L3-L4) (`clm_53eba45573368c50f49eef0606112dcd6cb0b83bffe7d168b1edd34e591bd6e8`)

