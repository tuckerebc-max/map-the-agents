---
access: public
aliases: []
claim_ids:
- clm_0fa108caa900742341b04ccb4580e7a452cfa5660e137fc235ae9f71966f3943
- clm_216c859cc158079d8c730e03a1d0d0d173946fb3509052258955304cf524b348
- clm_509700169736615b2f314d3025837f8e38210ea583917ad88ff8b5c9ef068414
- clm_6933f3720f210b8a6857ae4e11e2a83bc70dc19497de91927f86a7a6fa7baf10
- clm_761d356669adf9a507d1eda599c92ff49f7ce5bb34c1565d329bebda5a05963b
- clm_902ef62c1703f863b0a8dddd1b789fdbd0162d71bd4ce77e3588973f70f59b4b
- clm_c10bb93fe6e4ecbcb1249b68d42a7377fd448532265faea577d25dc073a84aff
- clm_ed0c78d742e2cb47f9906201e0935ca093c7c812fdf5ebce513bc1e413bcd6af
- clm_fdf737ac4f634f099d284d68a77bb026bc35d6e5f714d1f7ce7e886bfe79bbf7
maturity: draft
page_id: pg_08462c2d05885a7bb37458237612e841
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_70ef8de10b695a6283ae3d4dbd18d470
title: almogdepaz/wolfpack/README.md @ 0c7ee60e7163
updated_at: '2026-09-14T01:32:37Z'
---

# almogdepaz/wolfpack/README.md @ 0c7ee60e7163

<!-- rcw:begin owner=source:src_70ef8de10b695a6283ae3d4dbd18d470 block=evidence -->
- Remote access is designed to go directly over a private Tailscale network with no Wolfpack-hosted relay or account, and the phone client is a PWA with touch-friendly controls and optional notifications. [@claim:clm_0fa108caa900742341b04ccb4580e7a452cfa5660e137fc235ae9f71966f3943]
- The product supports built-in coding-agent providers Claude Code, Codex, Gemini CLI, Cursor, and Pi, with shell as an always-available fallback and custom PATH commands configurable in Settings → Agents. [@claim:clm_216c859cc158079d8c730e03a1d0d0d173946fb3509052258955304cf524b348]
- The tool grants browser users shell-level control over configured projects; session control follows the global API auth policy and has no inter-session authorization layer, so it should be kept on a trusted Tailnet with ACLs or JWT. [@claim:clm_509700169736615b2f314d3025837f8e38210ea583917ad88ff8b5c9ef068414]
- Wolfpack is a self-hosted control room for running coding agents remotely, letting users monitor and control persistent agent terminals from a desktop or phone. [@claim:clm_6933f3720f210b8a6857ae4e11e2a83bc70dc19497de91927f86a7a6fa7baf10]
- A CLI exposes JSON session control, e.g. wolfpack --machine <peer> list --json, session status, session create with --harness and --plan, and agent spawn with --notify-parent. [@claim:clm_761d356669adf9a507d1eda599c92ff49f7ce5bb34c1565d329bebda5a05963b]
- Sessions run in a Rust PTY broker separate from the web server, so closing the browser or restarting only the web server does not end sessions; a broker restart or login-service reinstall can terminate them. [@claim:clm_902ef62c1703f863b0a8dddd1b789fdbd0162d71bd4ce77e3588973f70f59b4b]
- Remote access depends on a Tailscale network; machine targeting uses configured tailscaleHostname suffixes, and the CLI sends JWT authorization on a bounded GET /api/machine handshake, failing closed on invalid or unreachable targets. [@claim:clm_c10bb93fe6e4ecbcb1249b68d42a7377fd448532265faea577d25dc073a84aff]
- Wolfpack ships agent skills: wolfpack-tailnet-control for session control across Agent Skills-compatible harnesses, and wolfpack-pi-task-delegation teaching Pi durable task routing via agent_task_* commands. [@claim:clm_ed0c78d742e2cb47f9906201e0935ca093c7c812fdf5ebce513bc1e413bcd6af]
- Session persistence has boundaries: a broker restart or login-service reinstallation can terminate sessions, per the README's lifecycle description. [@claim:clm_fdf737ac4f634f099d284d68a77bb026bc35d6e5f714d1f7ce7e886bfe79bbf7]
<!-- rcw:end owner=source:src_70ef8de10b695a6283ae3d4dbd18d470 block=evidence -->

## Researcher notes

