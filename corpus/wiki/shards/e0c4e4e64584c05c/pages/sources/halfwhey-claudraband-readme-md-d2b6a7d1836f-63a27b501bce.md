---
access: public
aliases: []
claim_ids:
- clm_1994a38214d3ac14c93e344c135617c9cd90e713ee0c3db67fa8eddaa4e301b4
- clm_2d4690e8a4fb811178d51adfe17e5d2a0053ec2459e03cdc5304b7a4408b62ad
- clm_55afbbcbf562191b1161845d4c711601b71ea07acf2250a10ce06bb87f23a909
- clm_58f61386aa9b2856f068b87dc4cef410fecf5f78dbed43e20b5c8cf5f8e8c015
- clm_6248154111f65c677675a3ddc13a16e7e6b48fde8fad797e12892503c1ff0bd8
- clm_63b640d92add1000117cdb2530236ce74657f5c002214bc4993b8cfc68705c73
- clm_87b62e767427d1031de95864644fb992ad7f3d919ec509c36e0ea92afaf119c0
- clm_cd6613998a07343aedc784d43582ad4524a9058a26287cb7fa7955b368ce15df
- clm_ee9d8bd75283c9a5b79f7174b9e3a64fdbcb7158f8f948ce0a1c6e885e46d27c
maturity: draft
page_id: pg_9b2eef9c05da5959959f63a27b501bce
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_cd8f2d1b608f5409945f74809316fa30
title: halfwhey/claudraband/README.md @ d2b6a7d1836f
updated_at: '2026-09-14T01:53:26Z'
---

# halfwhey/claudraband/README.md @ d2b6a7d1836f

<!-- rcw:begin owner=source:src_cd8f2d1b608f5409945f74809316fa30 block=evidence -->
- Live sessions are tracked in ~/.claudraband/; the sessions command lists only live entries, while prompt or send with --session auto-resume saved sessions even when no longer live. [@claim:clm_1994a38214d3ac14c93e344c135617c9cd90e713ee0c3db67fa8eddaa4e301b4]
- Sessions run inside tmux by default both locally and in the daemon; an experimental, slower headless xterm backend exists as a fallback, and the auto backend prefers tmux then xterm. [@claim:clm_2d4690e8a4fb811178d51adfe17e5d2a0053ec2459e03cdc5304b7a4408b62ad]
- Runtime requirements are Node.js or Bun, an already-authenticated Claude Code, and tmux for the first-class local and daemon-backed workflow. [@claim:clm_55afbbcbf562191b1161845d4c711601b71ea07acf2250a10ce06bb87f23a909]
- The project is explicitly experimental and geared toward personal, ad-hoc usage rather than replacing the Claude SDK; attach only works on live sessions and does not restart dead ones. [@claim:clm_58f61386aa9b2856f068b87dc4cef410fecf5f78dbed43e20b5c8cf5f8e8c015]
- The project provides resumable non-interactive workflows, an HTTP daemon for remote or headless session control, an ACP server for editor integration, and a TypeScript library for building custom tools. [@claim:clm_6248154111f65c677675a3ddc13a16e7e6b48fde8fad797e12892503c1ff0bd8]
- The tool wraps the official Claude Code TUI in a controlled terminal rather than replacing it; it does not touch OAuth, and every interaction runs through a real Claude Code session with authentication via Claude Code. [@claim:clm_63b640d92add1000117cdb2530236ce74657f5c002214bc4993b8cfc68705c73]
- The package bundles Claude Code @anthropic-ai/claude-code@2.1.96, and the CLAUDRABAND_CLAUDE_PATH environment variable can override the binary path. [@claim:clm_87b62e767427d1031de95864644fb992ad7f3d919ec509c36e0ea92afaf119c0]
- The CLI offers prompt, send, watch, interrupt, status, last, attach, sessions (with close), serve, and acp commands, with flags such as --session, --select, --model, --permission-mode, --backend, and --connect. [@claim:clm_cd6613998a07343aedc784d43582ad4524a9058a26287cb7fa7955b368ce15df]
- ACP support lets external frontends such as Toad and Zed drive Claude Code through claudraband, with session follow and resume supported while a real Claude Code pane remains underneath. [@claim:clm_ee9d8bd75283c9a5b79f7174b9e3a64fdbcb7158f8f948ce0a1c6e885e46d27c]
<!-- rcw:end owner=source:src_cd8f2d1b608f5409945f74809316fa30 block=evidence -->

## Researcher notes

