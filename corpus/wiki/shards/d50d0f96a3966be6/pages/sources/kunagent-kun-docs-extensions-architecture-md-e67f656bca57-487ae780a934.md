---
access: public
aliases: []
claim_ids:
- clm_1079f0f1c270f7ffb2fd232ea071d9e8042de8b457a1407e4280626b596223b6
- clm_52ea4a9340407fe75eaa81afd541104c98d277673f14c5f1ce1dc4840ec7321a
- clm_ab761180148e462781f85e3e894b9001c2d26683ceb7597c452a5ada6deec468
- clm_feacdc7b0bdb590ea341c1be5d53a973d8b08b144a4ee04cff384c31bcd1fb65
maturity: draft
page_id: pg_fc485162eb415a629f91487ae780a934
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_79c0144adcb45042a240b2cc8f595683
title: KunAgent/Kun/docs/extensions/architecture.md @ e67f656bca57
updated_at: '2026-09-14T02:10:53Z'
---

# KunAgent/Kun/docs/extensions/architecture.md @ e67f656bca57

<!-- rcw:begin owner=source:src_79c0144adcb45042a240b2cc8f595683 block=evidence -->
- The extension platform is documented as not creating a second agent runtime; extensions reach agent, tool, approval, and provider capabilities only through a public Host Context and Broker. [@claim:clm_1079f0f1c270f7ffb2fd232ea071d9e8042de8b457a1407e4280626b596223b6]
- Each Broker operation re-checks extension enablement, workspace trust and permission grants, resource ownership, request schema/rate limits, and whether protected user confirmation via an ApprovalGate is required. [@claim:clm_52ea4a9340407fe75eaa81afd541104c98d277673f14c5f1ce1dc4840ec7321a]
- ExtensionManager runs one Node child process per active Node extension over versioned private JSON IPC, lazily starts hosts on activation, merges concurrent activations, and enforces bounded time, concurrency, rate, and memory limits. [@claim:clm_ab761180148e462781f85e3e894b9001c2d26683ceb7597c452a5ada6deec468]
- Node extensions run with the current user's OS permissions, and the docs state that process isolation is not a security sandbox; Node can bypass the Broker to call OS file, network, and process APIs directly. [@claim:clm_feacdc7b0bdb590ea341c1be5d53a973d8b08b144a4ee04cff384c31bcd1fb65]
<!-- rcw:end owner=source:src_79c0144adcb45042a240b2cc8f595683 block=evidence -->

## Researcher notes

