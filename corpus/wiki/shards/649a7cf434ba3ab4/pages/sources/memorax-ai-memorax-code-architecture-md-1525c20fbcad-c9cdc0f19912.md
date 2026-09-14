---
access: public
aliases: []
claim_ids:
- clm_2799c9f6f086415b6b0a5f59ed65bdede1342f137fd7f8f58fdd0c7e1af1c0ae
- clm_33c49998aa682dd0b060d2ac0b03789410322cce02f10502e48299c9b766fc10
- clm_4db40c8d6b9342e787b37f5653b3f25f3dd0ce716d22e502bac1edf1c8baf3a6
- clm_66c97585ac8a651a827302d786cec72fe60923a46c914bfe5b1e9d16e5d90c54
- clm_74376d914b1cfd1da92279991a398dc08c40b9d10f10db9e750b238ffd11797c
- clm_dedbb3ef52a30450ea7d4107a30759a1d7326e42ad2b0a8731b9af85351d99f2
- clm_eaebe6aacefec997e47210a9018d2960f8b36aaeb3825a557027bbd36a4e9512
maturity: draft
page_id: pg_81943465ead8543e8082c9cdc0f19912
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4075b6c35e0f503fac600b7ee3dc8a2f
title: memorax-ai/memorax-code/ARCHITECTURE.md @ 1525c20fbcad
updated_at: '2026-09-14T04:09:28Z'
---

# memorax-ai/memorax-code/ARCHITECTURE.md @ 1525c20fbcad

<!-- rcw:begin owner=source:src_4075b6c35e0f503fac600b7ee3dc8a2f block=evidence -->
- Automatic Search on turn-start Hooks is disabled by default; the usual retrieval path is the client invoking memorax-cli through the shared Skill, while Hooks still provide identity, scope, and writeback coordination. [@claim:clm_2799c9f6f086415b6b0a5f59ed65bdede1342f137fd7f8f58fdd0c7e1af1c0ae]
- Adapter Hooks and plugins communicate with the Backend via versioned, client-qualified local HTTP commands carrying JSON and token headers, with a request deadline and optional cancellation; the transport does not retry or start the Backend. [@claim:clm_33c49998aa682dd0b060d2ac0b03789410322cce02f10502e48299c9b766fc10]
- After setup, the managed Backend schedules a detached updater that locks, resolves a channel target, installs an exact published version via the package-replacement path, and reuses non-interactive setup reconciliation. [@claim:clm_4db40c8d6b9342e787b37f5653b3f25f3dd0ce716d22e502bac1edf1c8baf3a6]
- The system integrates seven coding clients with one local Backend, a capability-oriented modular monolith, surrounded by six client deployment adapters, a shared runtime source layer, and an npm assembly/CLI layer. [@claim:clm_66c97585ac8a651a827302d786cec72fe60923a46c914bfe5b1e9d16e5d90c54]
- The Backend owns the local memory service, repository scope, trace, lifecycle, and update scheduling, but must not own model execution, provider credentials, or native transcript creation. [@claim:clm_74376d914b1cfd1da92279991a398dc08c40b9d10f10db9e750b238ffd11797c]
- Repository development practice: contributors are directed to read CONTRIBUTING.md before making changes, and AGENTS.md defines working rules for coding agents, runtime/data invariants, and Git handoff requirements. [@claim:clm_dedbb3ef52a30450ea7d4107a30759a1d7326e42ad2b0a8731b9af85351d99f2]
- adapter-common is a shared source layer consumed by the Backend and all six adapters, providing connection primitives, credential storage, locks, and Hook transport; it is not an independently deployed service. [@claim:clm_eaebe6aacefec997e47210a9018d2960f8b36aaeb3825a557027bbd36a4e9512]
<!-- rcw:end owner=source:src_4075b6c35e0f503fac600b7ee3dc8a2f block=evidence -->

## Researcher notes

