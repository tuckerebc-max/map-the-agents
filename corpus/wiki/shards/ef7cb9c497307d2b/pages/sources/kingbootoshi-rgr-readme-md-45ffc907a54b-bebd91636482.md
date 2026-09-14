---
access: public
aliases: []
claim_ids:
- clm_41f7efe1058853cd503512261dc36bb04e738500a18948ce51c8de77d7bd92c7
- clm_4812ceee52e841b721437d7eca50668dc25ec8882b0fff47abc972b1dced1ede
- clm_725688658c0766c43e2e7d9aa797385dcd83c7b2c82a014ca5966ae1277699a5
- clm_83cc8a355c6e7f664c9654fb2eefe1423a1bb18b787130102f44b202daf01e85
- clm_97b577b99e2bb8835a5a8995c6b359c688078e46abc77cc1812284ddc3da761e
- clm_9ef1c58777b257877c2dc78e4c15b46fdc9430f6dfe0373fd4e4456f4fdc7cd5
- clm_a3013de4a7d0fb3024bd1409eaf0ad792e71886313a4c78780bbaceb97627f58
maturity: draft
page_id: pg_8ccb89e973f05cc9b1f7bebd91636482
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_d50b118cb4605c69b519bdd47bd0cf4b
title: kingbootoshi/rgr/README.md @ 45ffc907a54b
updated_at: '2026-09-14T04:03:28Z'
---

# kingbootoshi/rgr/README.md @ 45ffc907a54b

<!-- rcw:begin owner=source:src_d50b118cb4605c69b519bdd47bd0cf4b block=evidence -->
- Enforcement rules include: Red must fail, Red defaults to test-surface changes only, protected Red files are hashed with SHA-256 and snapshotted, Green runs the exact Red command, and strict Red protects imported helpers, fixtures, snapshots, test config, and lockfiles. [@claim:clm_41f7efe1058853cd503512261dc36bb04e738500a18948ce51c8de77d7bd92c7]
- Every command proof uses the argv after the -- separator, and per the enforcement list this is currently direct `bun test` only. [@claim:clm_4812ceee52e841b721437d7eca50668dc25ec8882b0fff47abc972b1dced1ede]
- Every rgr run writes .rgr/manifest.json, .rgr/events.jsonl, snapshots, diffs, and command output logs as an audit trail. [@claim:clm_725688658c0766c43e2e7d9aa797385dcd83c7b2c82a014ca5966ae1277699a5]
- The threat model states that an agent with unrestricted write access to the same repo can still delete .rgr or bypass the CLI, so local use is a discipline gate and authoritative results require running verify inside CI, sandboxes, or agent harnesses. [@claim:clm_83cc8a355c6e7f664c9654fb2eefe1423a1bb18b787130102f44b202daf01e85]
- rgr is described as a no-dependency Red-Green-Refactor gate for coding agents that records the failing test first, freezes it with hashes and snapshots, and refuses Green or Refactor if the Red test was edited. [@claim:clm_97b577b99e2bb8835a5a8995c6b359c688078e46abc77cc1812284ddc3da761e]
- RGR ships two skills as Claude Code and Codex plugins: the rgr skill and intent-contract, which compiles a signed Locked Intent Boundary into an IntentLock that `rgr verify --intent-lock` enforces. [@claim:clm_9ef1c58777b257877c2dc78e4c15b46fdc9430f6dfe0373fd4e4456f4fdc7cd5]
- The CLI exposes subcommands including init, red, green, refactor, verify, revise-test, status, doctor, inspect-test, prompt, and lock-intent, invoked via Bun with flags like --goal-id, --test, --protect, --ci, --replay. [@claim:clm_a3013de4a7d0fb3024bd1409eaf0ad792e71886313a4c78780bbaceb97627f58]
<!-- rcw:end owner=source:src_d50b118cb4605c69b519bdd47bd0cf4b block=evidence -->

## Researcher notes

