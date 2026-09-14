---
access: public
aliases: []
claim_ids:
- clm_308942903fd7f609a53ce97e769f5c6d0f4e5f9994ea5876403db915cd756216
- clm_72ec5a38ad78b754541f1918afeae0ce3353e1c2f73dae817cca9e70248b941b
- clm_761f9deeee81908f0ec6f7fdf178d4bd8daedaa8f19c8e542e1eba3b9e5a6c66
- clm_c797267ff84e977963f684ad537fbf8a3b9a0d6a495cfec039f3491ce57f49ef
maturity: draft
page_id: pg_51f8edb5ccbe548f84fd5d4ff3c92e80
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_872821a22f605331bc831be51c1c70db
title: guanyilun/agent-sh/README.md @ 8038ae7730eb
updated_at: '2026-09-14T01:52:03Z'
---

# guanyilun/agent-sh/README.md @ 8038ae7730eb

<!-- rcw:begin owner=source:src_872821a22f605331bc831be51c1c70db block=evidence -->
- The bundled frontend is a shell on top of node-pty, and the grep tool searches file contents via ripgrep; ash works with any OpenAI-compatible API including built-in providers openrouter, openai, deepseek, ollama, zai-coding-plan, and opencode. [@claim:clm_308942903fd7f609a53ce97e769f5c6d0f4e5f9994ea5876403db915cd756216]
- agent-sh is published as an npm package (`agent-sh`) with a license badge, installable globally via `npm install -g agent-sh`. [@claim:clm_72ec5a38ad78b754541f1918afeae0ce3353e1c2f73dae817cca9e70248b941b]
- Native Windows (cmd.exe/PowerShell) is not supported as the host shell; the README recommends running inside WSL for the full interactive experience, while headless/library/ACP-bridge usage may work. [@claim:clm_761f9deeee81908f0ec6f7fdf178d4bd8daedaa8f19c8e542e1eba3b9e5a6c66]
- The runtime requires Node.js 18+ and supports bash, zsh, and fish as host shells; other shells such as nushell are not yet wired up. [@claim:clm_c797267ff84e977963f684ad537fbf8a3b9a0d6a495cfec039f3491ce57f49ef]
<!-- rcw:end owner=source:src_872821a22f605331bc831be51c1c70db block=evidence -->

## Researcher notes

