---
access: public
aliases: []
claim_ids:
- clm_09d7b48b2c01a0ef2e3b11cc39a9f9512bcbab4e757179e2fc64210528c9a519
- clm_6818878674cdb7981e0b6b0d1dc21b436eecb27c306161c6448b4c93e55cb09e
- clm_814b17e26d0e35ca4d7c41029c87f04f4e9f0754d75c68d61551b1ecb28d470e
- clm_bc2992af2dd306609af118971956e4ac9ffc32f9531edee8beca8ea0b72d0ac7
- clm_d8e73c1c1a9f59525009408ae781e7da160376e5a67f1eacb55ac5e7b637e8fb
maturity: draft
page_id: pg_6a113e6815565ba28061cf7f7ab278d9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7b489ba2180251d18998735aa7044d69
title: HarnessRouter/harnessrouter/CONTRIBUTING.md @ 5637717816b5
updated_at: '2026-09-14T02:03:14Z'
---

# HarnessRouter/harnessrouter/CONTRIBUTING.md @ 5637717816b5

<!-- rcw:begin owner=source:src_7b489ba2180251d18998735aa7044d69 block=evidence -->
- Repository development practice: protocol changes follow a UEP process (issue labelled 'uep' with Problem, Proposal, Compatibility, Alternatives; maintainer response within 10 working days; accepted UEPs land as one PR updating spec, schema, implementation, conformance test, and changelog). [@claim:clm_09d7b48b2c01a0ef2e3b11cc39a9f9512bcbab4e757179e2fc64210528c9a519]
- Repository development practice: substantial changes require an issue describing problem, proposal, and impact before implementation; small obvious fixes may go straight to a pull request. [@claim:clm_6818878674cdb7981e0b6b0d1dc21b436eecb27c306161c6448b4c93e55cb09e]
- Repository development practice: harness-support changes must be measured against five scenarios per harness and model plus a custom harness with its own skill and tool policy, judged by code-enforced rules per docs/harness-verification.md. [@claim:clm_814b17e26d0e35ca4d7c41029c87f04f4e9f0754d75c68d61551b1ecb28d470e]
- Repository development practice: main accepts PRs only with one approval and all checks green, no self-approval; agent-driven PRs are opened via an 'open-pr' workflow as github-actions[bot]. [@claim:clm_bc2992af2dd306609af118971956e4ac9ffc32f9531edee8beca8ea0b72d0ac7]
- Repository development practice: contributor checks include npm type-check/test/build for the console, pytest for the gateway, and building the image plus walking the self-hosted flow for container changes. [@claim:clm_d8e73c1c1a9f59525009408ae781e7da160376e5a67f1eacb55ac5e7b637e8fb]
<!-- rcw:end owner=source:src_7b489ba2180251d18998735aa7044d69 block=evidence -->

## Researcher notes

