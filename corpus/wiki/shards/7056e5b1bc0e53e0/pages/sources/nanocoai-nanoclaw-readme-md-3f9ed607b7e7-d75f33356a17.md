---
access: public
aliases: []
claim_ids:
- clm_03711d486d1699152d9c7c0c9caf5820a30a3f0bcca9ea4f7e460650be1b4408
- clm_0c69316f38b290f83bf63f84a1148423f8cd56b9cc4947362696e3ad1dac316c
- clm_28579e58674e33a6e8f89efc1cc0252bfa4cfd45fdc96b1a136e1d1e17113835
- clm_7fe1e3da4664ce173ee2ee745448164f9e13daaf3af7559af2ed9735b99e7484
- clm_b0512fa8f2a4e24a724468625dae4e1396e9841d5f0c833e633d2e64e78ee19b
- clm_c3b585fce0a4bdfafe1446200faa88091e102ee59c7b5329d22b494bb9ea2f39
- clm_d2866fc2a317926ad5a529b800892795ec60cba25fe09f6ac154b8290e0332ca
maturity: draft
page_id: pg_f86a8cfb120b5c7e8824d75f33356a17
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_871248f08f6b5106ac2bd85028dd5d76
title: nanocoai/nanoclaw/README.md @ 3f9ed607b7e7
updated_at: '2026-09-14T02:22:07Z'
---

# nanocoai/nanoclaw/README.md @ 3f9ed607b7e7

<!-- rcw:begin owner=source:src_871248f08f6b5106ac2bd85028dd5d76 block=evidence -->
- Agents never hold raw API keys; outbound requests route through OneCLI's Agent Vault, which injects credentials at request time and enforces per-agent policies and rate limits. [@claim:clm_03711d486d1699152d9c7c0c9caf5820a30a3f0bcca9ea4f7e460650be1b4408]
- Requirements are macOS or Linux (Windows via WSL2), Node.js 22+, pnpm 10+, Docker, and Claude Code for /customize, /debug, setup error recovery, and /add-<channel> skills; the installer installs Node and pnpm if missing. [@claim:clm_0c69316f38b290f83bf63f84a1148423f8cd56b9cc4947362696e3ad1dac316c]
- The project deliberately avoids configuration files; customization is done by asking Claude Code to modify the small codebase, or via a guided /customize command. [@claim:clm_28579e58674e33a6e8f89efc1cc0252bfa4cfd45fdc96b1a136e1d1e17113835]
- Trunk ships only the registry and infrastructure; channel adapters and alternative providers live on long-lived channels/providers branches and are installed into a user's fork via /add-<name> skills that copy modules, wire registration, and pin dependencies. [@claim:clm_7fe1e3da4664ce173ee2ee745448164f9e13daaf3af7559af2ed9735b99e7484]
- A single Node host process routes messages through an entity model (user → messaging group → agent group → session), writes to the session's inbound.db, and wakes the container; the agent-runner inside polls inbound.db and writes responses to outbound.db. [@claim:clm_b0512fa8f2a4e24a724468625dae4e1396e9841d5f0c833e633d2e64e78ee19b]
- Repository development practice: contributions to the base are limited to security fixes, bug fixes, and clear improvements; new capabilities must be contributed as skills on the channels/providers branches or as self-contained skills, per CONTRIBUTING.md. [@claim:clm_c3b585fce0a4bdfafe1446200faa88091e102ee59c7b5329d22b494bb9ea2f39]
- Agents run in their own Linux/Docker containers with filesystem isolation, so bash commands execute inside the container rather than on the host, and only explicitly mounted directories are visible. [@claim:clm_d2866fc2a317926ad5a529b800892795ec60cba25fe09f6ac154b8290e0332ca]
<!-- rcw:end owner=source:src_871248f08f6b5106ac2bd85028dd5d76 block=evidence -->

## Researcher notes

