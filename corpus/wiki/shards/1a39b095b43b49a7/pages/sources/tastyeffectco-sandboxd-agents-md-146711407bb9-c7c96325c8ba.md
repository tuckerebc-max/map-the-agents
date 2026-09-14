---
access: public
aliases: []
claim_ids:
- clm_8cbd2e7199062aab13b507b0bf4591f3c4747abd761fb8f1efbf2bba847c7ed5
- clm_e00752f04b3c9ba228ac94d7b44c043cd359127834ca14226a42ee9322f09d6e
maturity: draft
page_id: pg_92c2611c562252d98fcec7c96325c8ba
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ecc21651c8ef5e77ad2a66e5a420d273
title: tastyeffectco/sandboxd/AGENTS.md @ 146711407bb9
updated_at: '2026-09-14T03:18:13Z'
---

# tastyeffectco/sandboxd/AGENTS.md @ 146711407bb9

<!-- rcw:begin owner=source:src_ecc21651c8ef5e77ad2a66e5a420d273 block=evidence -->
- Agent credentials never enter a sandbox: a control-plane-side auth proxy holds the real keys and injects Authorization/X-Api-Key on the wire, giving the sandbox only a base URL and a dummy key; credential-shaped env vars are scrubbed from agent processes. [@claim:clm_8cbd2e7199062aab13b507b0bf4591f3c4747abd761fb8f1efbf2bba847c7ed5]
- Repository development practice: AGENTS.md is a copy-pasteable runbook for an AI agent or human to install (./install.sh), operate, drive the API, run the console profile, and uninstall (./uninstall.sh with --images/--data flags) sandboxd. [@claim:clm_e00752f04b3c9ba228ac94d7b44c043cd359127834ca14226a42ee9322f09d6e]
<!-- rcw:end owner=source:src_ecc21651c8ef5e77ad2a66e5a420d273 block=evidence -->

## Researcher notes

