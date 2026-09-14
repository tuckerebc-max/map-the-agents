---
access: public
aliases: []
claim_ids:
- clm_002cf7947be38670f1434eb7440d1a7bc1b1304333f3f20bb5f5a483172f911d
- clm_133e70c679f59c54b8ac659997e5b8e03128cfb16065b2f8c1eaaff4ce12c78b
- clm_195b44f5fa73a7a3340245e42ff229d065c713e83dee93bda2dee1a0f49e6709
- clm_27d5a60e43b207a685868421aac1af684470a84d097282e043f1bb79cdf78980
- clm_2d7ced6b7f349171358d615d676aa22c6c6ab2bf71192fc74d87def6377db0af
- clm_2e01678dd72e9bc366ad28851e51f3bb465b5645608857fd265f787f34b9a2c6
- clm_43450c85f57135b8ae245b7263c8f75740bc9f822d8037f88535c10a40610de2
- clm_76d59394a7f8bd34d614d0d9f48ff311ba7a9075783d3b18db938879d2c8c21a
- clm_7b7f209c83b18616329a752c5115c70f2b96f3bc7b6e9f2294b592fa97331b48
- clm_965166d942a5105687c49903a0d04b85535d9fecd4f155a10c993aebf394a50f
- clm_98fdaa60decedd2ee4d6a4b1e6133d4ed6b386825a8e23972a1c7844f73544d2
- clm_ab72d6b5b17ea95eacab811c0fc8e81b3db675a8cf5a00ac800d680213dcb061
- clm_e516c802c2946b3c6d2f6844e2ad5ce6bf3275d45d111e684adc8cfc4a279320
- clm_e5e55063a220dae21408caea327daa642d79b2aa64815b81692659941f6753a8
- clm_f4256438dd509e1a63cb9c40b67f1108e6d1545285e79003e0bcc0629b204292
maturity: draft
page_id: pg_9b18e394047a5bf58e20cf2b22234fec
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_a61e9a9d75855d7f8d9c5a778aed2fbc
title: omnigent-ai/omnigent/README.md @ 270eca52b1e0
updated_at: '2026-09-14T02:24:55Z'
---

# omnigent-ai/omnigent/README.md @ 270eca52b1e0

<!-- rcw:begin owner=source:src_a61e9a9d75855d7f8d9c5a778aed2fbc block=evidence -->
- Agents are defined in YAML files declaring a prompt, an executor harness (e.g. claude-sdk, codex, cursor, pi, openai-agents), tools including local Python functions, MCP servers, and delegatable sub-agents. [@claim:clm_002cf7947be38670f1434eb7440d1a7bc1b1304333f3f20bb5f5a483172f911d]
- Sessions can run in disposable cloud sandboxes on providers including Modal, Daytona, E2B, Kubernetes, CoreWeave, and Databricks, launched from the CLI or provisioned per session by the server as managed hosts. [@claim:clm_133e70c679f59c54b8ac659997e5b8e03128cfb16065b2f8c1eaaff4ce12c78b]
- Omnigent is described as an open-source meta-harness providing a common orchestration layer over Claude Code, Codex, Cursor, OpenCode, Hermes, Pi, and self-written agents, allowing harness swapping without rewrites. [@claim:clm_195b44f5fa73a7a3340245e42ff229d065c713e83dee93bda2dee1a0f49e6709]
- Repository development practice: PRs adding or changing harness support should run the harness test bench to check the capability matrix against observed behavior. [@claim:clm_27d5a60e43b207a685868421aac1af684470a84d097282e043f1bb79cdf78980]
- The CLI exposes per-harness launchers such as omnigent claude, codex, cursor, agy, opencode, hermes, and pi, plus an interchangeable short alias 'omni' installed alongside the main command. [@claim:clm_2d7ced6b7f349171358d615d676aa22c6c6ab2bf71192fc74d87def6377db0af]
- Sessions follow the user across devices: started in a terminal, they continue in the browser or on a phone, with messages, sub-agents, terminals, and files staying in sync. [@claim:clm_2e01678dd72e9bc366ad28851e51f3bb465b5645608857fd265f787f34b9a2c6]
- YAML-defined agents are launched with 'omnigent run path/to/agent.yaml', and examples such as polly, debby, and deep-research can be run the same way, optionally with a --harness override. [@claim:clm_43450c85f57135b8ae245b7263c8f75740bc9f822d8037f88535c10a40610de2]
- The Polly example is a multi-agent orchestrator that delegates coding to sub-agents (Claude Code, Codex, or Pi) in parallel git worktrees and routes each diff to a reviewer from a different vendor. [@claim:clm_76d59394a7f8bd34d614d0d9f48ff311ba7a9075783d3b18db938879d2c8c21a]
- Multi-user accounts are enabled via OMNIGENT_AUTH_ENABLED=1; signup is invite-only through single-use invite links, and OIDC providers (Google, GitHub, Okta, Microsoft) can be configured on a deployed server. [@claim:clm_7b7f209c83b18616329a752c5115c70f2b96f3bc7b6e9f2294b592fa97331b48]
- Native harness terminal wrappers require tmux, the coding-harness CLIs installed by omnigent run need Node.js 22 LTS or newer with npm, and pnpm is needed for the web UI. [@claim:clm_965166d942a5105687c49903a0d04b85535d9fecd4f155a10c993aebf394a50f]
- On Linux, native harness terminal wrappers and the pi harness sandbox each agent terminal with bubblewrap, and that isolation is mandatory; macOS uses the built-in seatbelt sandbox instead. [@claim:clm_98fdaa60decedd2ee4d6a4b1e6133d4ed6b386825a8e23972a1c7844f73544d2]
- On Windows the product runs in a degraded mode: tmux/PTY terminal wrappers and bwrap/seatbelt filesystem and network sandboxing are unavailable; the Windows Job Object backend contains the process tree but does not isolate filesystem or network. [@claim:clm_ab72d6b5b17ea95eacab811c0fc8e81b3db675a8cf5a00ac800d680213dcb061]
- Policies check every agent action and allow, block, or pause for approval; builtins can cap tool calls and spend, and policies stack at server-wide, per-agent, and per-session levels with stricter session rules checked first. [@claim:clm_e516c802c2946b3c6d2f6844e2ad5ce6bf3275d45d111e684adc8cfc4a279320]
- Running omnigent starts a terminal session and a local web UI at http://localhost:6767 showing the same session; a macOS desktop app wraps that UI with OS notifications and a dock badge. [@claim:clm_e5e55063a220dae21408caea327daa642d79b2aa64815b81692659941f6753a8]
- Omnigent requires Python 3.12+ and is installable via a curl installer script, uv/pip, or Homebrew; optional extras cover model providers (databricks, bedrock, vertex), sandbox providers, SDK harnesses, and storage/memory backends. [@claim:clm_f4256438dd509e1a63cb9c40b67f1108e6d1545285e79003e0bcc0629b204292]
<!-- rcw:end owner=source:src_a61e9a9d75855d7f8d9c5a778aed2fbc block=evidence -->

## Researcher notes

