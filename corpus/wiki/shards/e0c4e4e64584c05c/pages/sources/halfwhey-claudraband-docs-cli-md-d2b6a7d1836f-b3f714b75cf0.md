---
access: public
aliases: []
claim_ids:
- clm_1994a38214d3ac14c93e344c135617c9cd90e713ee0c3db67fa8eddaa4e301b4
- clm_25625fcc2fee98b48d6ce5c43514c0b1adae142e47bd124fe765b4e4adf498b3
- clm_2d4690e8a4fb811178d51adfe17e5d2a0053ec2459e03cdc5304b7a4408b62ad
- clm_58f61386aa9b2856f068b87dc4cef410fecf5f78dbed43e20b5c8cf5f8e8c015
- clm_87b62e767427d1031de95864644fb992ad7f3d919ec509c36e0ea92afaf119c0
- clm_cd6613998a07343aedc784d43582ad4524a9058a26287cb7fa7955b368ce15df
maturity: draft
page_id: pg_05332dc8f10151f39a51b3f714b75cf0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4aaf7a35bb9d5b6e80ba4c2a7d77bc8d
title: halfwhey/claudraband/docs/cli.md @ d2b6a7d1836f
updated_at: '2026-09-14T01:53:26Z'
---

# halfwhey/claudraband/docs/cli.md @ d2b6a7d1836f

<!-- rcw:begin owner=source:src_4aaf7a35bb9d5b6e80ba4c2a7d77bc8d block=evidence -->
- Live sessions are tracked in ~/.claudraband/; the sessions command lists only live entries, while prompt or send with --session auto-resume saved sessions even when no longer live. [@claim:clm_1994a38214d3ac14c93e344c135617c9cd90e713ee0c3db67fa8eddaa4e301b4]
- The --select flag answers pending AskUserQuestion or permission prompts using Claude's raw option numbers (the bypass-permissions warning is option 2); prompt --select waits for the following turn while send --select is fire-and-forget. [@claim:clm_25625fcc2fee98b48d6ce5c43514c0b1adae142e47bd124fe765b4e4adf498b3]
- Sessions run inside tmux by default both locally and in the daemon; an experimental, slower headless xterm backend exists as a fallback, and the auto backend prefers tmux then xterm. [@claim:clm_2d4690e8a4fb811178d51adfe17e5d2a0053ec2459e03cdc5304b7a4408b62ad]
- The project is explicitly experimental and geared toward personal, ad-hoc usage rather than replacing the Claude SDK; attach only works on live sessions and does not restart dead ones. [@claim:clm_58f61386aa9b2856f068b87dc4cef410fecf5f78dbed43e20b5c8cf5f8e8c015]
- The package bundles Claude Code @anthropic-ai/claude-code@2.1.96, and the CLAUDRABAND_CLAUDE_PATH environment variable can override the binary path. [@claim:clm_87b62e767427d1031de95864644fb992ad7f3d919ec509c36e0ea92afaf119c0]
- The CLI offers prompt, send, watch, interrupt, status, last, attach, sessions (with close), serve, and acp commands, with flags such as --session, --select, --model, --permission-mode, --backend, and --connect. [@claim:clm_cd6613998a07343aedc784d43582ad4524a9058a26287cb7fa7955b368ce15df]
<!-- rcw:end owner=source:src_4aaf7a35bb9d5b6e80ba4c2a7d77bc8d block=evidence -->

## Researcher notes

