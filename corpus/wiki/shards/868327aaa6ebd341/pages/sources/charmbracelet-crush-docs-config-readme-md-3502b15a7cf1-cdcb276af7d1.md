---
access: public
aliases: []
claim_ids:
- clm_15dc8b6f02a8bbe45f775c10c8190e9d4c465620574234c554158001b89cf75b
- clm_445ecab51d2efcdc492926e8559a07e0d850ff7096daf102bd67a06b8ef3e8f3
- clm_f3043de202908b1ecb3cb571977985b01ee93842474564bbb111ccf994af977c
maturity: draft
page_id: pg_8392695707705c049129cdcb276af7d1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_39b6560a38195270be8345b55a445f20
title: charmbracelet/crush/docs/config/README.md @ 3502b15a7cf1
updated_at: '2026-09-14T01:40:40Z'
---

# charmbracelet/crush/docs/config/README.md @ 3502b15a7cf1

<!-- rcw:begin owner=source:src_39b6560a38195270be8345b55a445f20 block=evidence -->
- Config is discovered from project-level .crushrc/crushrc and XDG config paths with project settings overriding global ones; crushrc overrides JSON in the same directory, and hook command paths resolve relative to the current working directory. [@claim:clm_15dc8b6f02a8bbe45f775c10c8190e9d4c465620574234c554158001b89cf75b]
- Configuration is Bash-based via builtin commands (provider, model, mcp, lsp, hook, permissions, option) in a crushrc file that runs at startup; legacy JSON config is still supported but deprecated and receives no new features. [@claim:clm_445ecab51d2efcdc492926e8559a07e0d850ff7096daf102bd67a06b8ef3e8f3]
- Crush ships a builtin crush-hook skill so the agent can write, edit, and configure hooks on itself, and a builtin config skill for natural-language configuration. [@claim:clm_f3043de202908b1ecb3cb571977985b01ee93842474564bbb111ccf994af977c]
<!-- rcw:end owner=source:src_39b6560a38195270be8345b55a445f20 block=evidence -->

## Researcher notes

