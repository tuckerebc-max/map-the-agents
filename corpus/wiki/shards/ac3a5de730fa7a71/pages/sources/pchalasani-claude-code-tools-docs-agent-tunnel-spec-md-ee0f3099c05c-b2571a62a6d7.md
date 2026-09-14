---
access: public
aliases: []
claim_ids:
- clm_1298c9ef91d5d6a6528a1bc0dba091a7b5c8f7585a7cf7bc864dd19b9e9c3a0a
- clm_26415cee010dbd178c9aed47a3f9bdf242cbc1dc0c83f79206572dc9adfd382f
- clm_27202477a165f912b1e66bb9379a7f51e62d22ab118c365c9e88e760be7c5f7a
- clm_40dfded60246ce70ea24eed84e923f6c75228ab9106bb42aca29977378d07c20
- clm_53b690b8c997afefeb80c402807cd315948bf5e822d89fdbc86be2c518184484
- clm_56f7787c1dcb25553bcdf1dbe3b58d0caaebd513078f45089da8ab348e1e9fda
- clm_672792543a29b3a6dc03c2bac185826b610c4c791a586907f87e34a8ca5eb465
- clm_6734c7ab7fedbd3bc28dc4b08fed6159d4e47ecb4b0c4cca5438973325155295
- clm_680c1219b2532e636a8881cbd2bc6fa99fdc7d8f3979fdab7f549f4eadcb6028
- clm_72d4a6321fc48c7c7b9efdf8c179b674385bf8e53d666b1887fd9ad4b44dacb8
- clm_8e547980325ffe280d0dbc15b900bee6c6c1a316fe50316f3e5eeef9fc5e50e2
- clm_adc7f9e1fbae4d3131568fe08021103e58bf45cd72c7ee4b5bdb90cd9e9a1f14
- clm_d61005b097b552348cadf1a37cd77e02c5481b6b7472afb4fa44fbfacee8ab1c
- clm_de6afbb8995390a98cd9d4a17336cfa38dfb53e55f7edaf03fc074e6095cfb08
- clm_f451ca94e7446318f904cc67fdc9875255560ea910e631fde566a473d91c2b0d
maturity: draft
page_id: pg_531ed8529c5c57129ee1b2571a62a6d7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_dd8ddf3436a95724b46da45b063794b3
title: pchalasani/claude-code-tools/docs/agent-tunnel-spec.md @ ee0f3099c05c
updated_at: '2026-09-14T04:15:23Z'
---

# pchalasani/claude-code-tools/docs/agent-tunnel-spec.md @ ee0f3099c05c

<!-- rcw:begin owner=source:src_dd8ddf3436a95724b46da45b063794b3 block=evidence -->
- The >share hook (hooks/share_hook.py) is a standalone stdlib UserPromptSubmit hook that reads session_id/cwd/transcript_path from stdin, writes an fcntl-locked atomic registry, and blocks the prompt to print the handle. [@claim:clm_1298c9ef91d5d6a6528a1bc0dba091a7b5c8f7585a7cf7bc864dd19b9e9c3a0a]
- In a watched channel, '<handle> [question]' opens a Discord thread bound to that session with follow-ups staying in the thread; !list/!handles list active handles; !done/!close/!end tear down the fork immediately. [@claim:clm_26415cee010dbd178c9aed47a3f9bdf242cbc1dc0c83f79206572dc9adfd382f]
- agent-tunnel exposes long-lived local Claude Code sessions ('experts') to teammates over Discord; a session is published at runtime with >share and addressed by a short handle, with each conversation answered against a read-only fork. [@claim:clm_27202477a165f912b1e66bb9379a7f51e62d22ab118c365c9e88e760be7c5f7a]
- The spec notes a ToS gray area: consumer plans prohibit making your account available to others, and headless with an API key is described as the unambiguous path. [@claim:clm_40dfded60246ce70ea24eed84e923f6c75228ab9106bb42aca29977378d07c20]
- agent-tunnel supports two backends: headless (default) runs claude -p per question with clean JSON I/O, while tmux runs an interactive claude per thread in a private tmux server window, watchable via agent-tunnel watch. [@claim:clm_53b690b8c997afefeb80c402807cd315948bf5e822d89fdbc86be2c518184484]
- Security model: read-only tools are hard-enforced by the CLI permission layer by default; access is Discord channel membership plus optional user/role allowlists, and the persona's discouragement of leaking secrets is described as a soft layer only. [@claim:clm_56f7787c1dcb25553bcdf1dbe3b58d0caaebd513078f45089da8ab348e1e9fda]
- Write/bash forks save deliverables to .agent-tunnel-out/<thread>/; the bot snapshots and diffs that dir to post new or modified files as Discord attachments, and a wildcard .gitignore keeps deliverables out of git status. [@claim:clm_672792543a29b3a6dc03c2bac185826b610c4c791a586907f87e34a8ca5eb465]
- agent-tunnel uses no inbound tunnel: it connects via the Discord Gateway's outbound websocket, so nothing on the machine is internet-reachable. [@claim:clm_6734c7ab7fedbd3bc28dc4b08fed6159d4e47ecb4b0c4cca5438973325155295]
- Per-handle access levels: --write adds Write/Edit/NotebookEdit (never Bash); --dangerously-allow-bash adds command execution; --dangerously-skip-permissions lets the fork use any tool or MCP server the session has. [@claim:clm_680c1219b2532e636a8881cbd2bc6fa99fdc7d8f3979fdab7f549f4eadcb6028]
- Repository development practice: the agent-tunnel spec reports unit tests using real files without mocks, covering the registry, hook, store, session discovery, flag building, config, and attachment handling. [@claim:clm_72d4a6321fc48c7c7b9efdf8c179b674385bf8e53d666b1887fd9ad4b44dacb8]
- Binary Office attachments are best-effort converted using whatever converter is on PATH (LibreOffice→PDF preferred, else pandoc→Markdown, else macOS textutil); no converter is a hard dependency, and PDF/images/text work unaided. [@claim:clm_8e547980325ffe280d0dbc15b900bee6c6c1a316fe50316f3e5eeef9fc5e50e2]
- Inbound attachments are downloaded to a per-thread uploads dir outside any repo and exposed to the fork via --add-dir, with per-file size and count caps; oversized or excess files are skipped with a notice. [@claim:clm_adc7f9e1fbae4d3131568fe08021103e58bf45cd72c7ee4b5bdb90cd9e9a1f14]
- The config dir is propagated end to end: the hook derives it from transcript_path and records it in the registry, and the daemon pins each fork via CLAUDE_CONFIG_DIR so work and personal sessions fork under their own config/account. [@claim:clm_d61005b097b552348cadf1a37cd77e02c5481b6b7472afb4fa44fbfacee8ab1c]
- The spec reports live end-to-end validation of agent-tunnel in both headless mode and tmux-over-Discord, confirming forked sessions inherit context and follow-ups continue the same fork. [@claim:clm_de6afbb8995390a98cd9d4a17336cfa38dfb53e55f7edaf03fc074e6095cfb08]
- Threads answer via --resume with --fork-session so the original session is untouched; remote turns run with --allowedTools Read,Grep,Glob, an explicit deny list, and --permission-mode dontAsk. [@claim:clm_f451ca94e7446318f904cc67fdc9875255560ea910e631fde566a473d91c2b0d]
<!-- rcw:end owner=source:src_dd8ddf3436a95724b46da45b063794b3 block=evidence -->

## Researcher notes

