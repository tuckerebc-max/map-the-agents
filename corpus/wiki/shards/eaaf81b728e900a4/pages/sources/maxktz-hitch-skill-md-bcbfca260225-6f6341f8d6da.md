---
access: public
aliases: []
claim_ids:
- clm_0ba161c12660d344be2c3507f0fdfb5068a0c68ced87cce3310cd76e0ff56d3e
- clm_2b50d452eefc34b43471e6de22d31a722a804fe8e38b6eeb3fdda4c1b6459d56
- clm_2bf1f55bf4047ff84256f81224f2612b07336f861e47aaf8fd03feebf89ffe86
- clm_52783d4ddb5d9029927b667fcfe7cef5edec8bd8404c7e2aacde3e259f84430a
- clm_6dc0f5014bf85f06a57fd01d44d3497ffac6a9cbf647cb8cbf2e9c6c278947af
- clm_cb46d937cfce6256437e956c6d4eb4e6b5f2af0137f98e5a865edb6ddfc6b331
maturity: draft
page_id: pg_effe83cd54de55f78e196f6341f8d6da
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_549d3fc0112e5f72992f5f86e5f05550
title: maxktz/hitch/SKILL.md @ bcbfca260225
updated_at: '2026-09-14T04:09:11Z'
---

# maxktz/hitch/SKILL.md @ bcbfca260225

<!-- rcw:begin owner=source:src_549d3fc0112e5f72992f5f86e5f05550 block=evidence -->
- The skill instructs agents to prefer `hitch context` first, avoid --all by default, use --wait instead of sleep polling, and only use hitch for collaboration rather than short tool calls. [@claim:clm_0ba161c12660d344be2c3507f0fdfb5068a0c68ced87cce3310cd76e0ff56d3e]
- `hitch send-keys -t <terminal>` sends input to a terminal, supports keys like Enter, Tab, C-c, and options including --wait finish/quiet/time/output, --timeout (default 30s), --tail, and --force. [@claim:clm_2b50d452eefc34b43471e6de22d31a722a804fe8e38b6eeb3fdda4c1b6459d56]
- A SKILL.md (version 3) describes when agents should use hitch, e.g. before starting a dev server, watcher, tunnel, REPL, build, or log tail that may already be running. [@claim:clm_2bf1f55bf4047ff84256f81224f2612b07336f861e47aaf8fd03feebf89ffe86]
- `hitch capture` mirrors tmux capture-pane behavior with tmux-compatible options (-p, -S, -E, -e) and accepts no-op compatibility flags such as -C, -J, -N, -T, -a, -q. [@claim:clm_52783d4ddb5d9029927b667fcfe7cef5edec8bd8404c7e2aacde3e259f84430a]
- The `hitch context` command shows compact terminal state and recent output, with forms for all project terminals, a specific terminal, or `--all` including terminals outside the project. [@claim:clm_6dc0f5014bf85f06a57fd01d44d3497ffac6a9cbf647cb8cbf2e9c6c278947af]
- Hitch refuses by default sending shell commands into terminals with running processes, printing terminal context instead; `--force` overrides this, and a sequence starting with C-c is allowed. [@claim:clm_cb46d937cfce6256437e956c6d4eb4e6b5f2af0137f98e5a865edb6ddfc6b331]
<!-- rcw:end owner=source:src_549d3fc0112e5f72992f5f86e5f05550 block=evidence -->

## Researcher notes

