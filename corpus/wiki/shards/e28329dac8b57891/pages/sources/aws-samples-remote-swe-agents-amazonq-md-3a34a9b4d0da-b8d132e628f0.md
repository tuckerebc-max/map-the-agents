---
access: public
aliases: []
claim_ids:
- clm_05169d21606bea3932ce1d8b11cf57e2da45a796dad3b0d84848d6ef8768b0fb
- clm_059a883de673835b4c954621f5e5b33618215d2cfcb75ee46ef518fe64ab7c1e
- clm_dd4be6fd6c0a5cb88bf97a6edd6cfdbd3588505cc70fef926ad6bb25e23c801d
maturity: draft
page_id: pg_5195bdc946475196a9b6b8d132e628f0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_587abd3e0a195643a6772252f3cf2216
title: aws-samples/remote-swe-agents/AmazonQ.md @ 3a34a9b4d0da
updated_at: '2026-09-14T01:36:38Z'
---

# aws-samples/remote-swe-agents/AmazonQ.md @ 3a34a9b4d0da

<!-- rcw:begin owner=source:src_587abd3e0a195643a6772252f3cf2216 block=evidence -->
- Repository development practice: AmazonQ.md prescribes contributor conventions including TypeScript, Prettier formatting, avoiding comments unless necessary, using Next.js server actions with Zod schemas and authActionClient, and building agent-core before other packages. [@claim:clm_05169d21606bea3932ce1d8b11cf57e2da45a796dad3b0d84848d6ef8768b0fb]
- Repository development practice: the documented development flow is to create a branch, implement and test, run format and type checks, open a PR with an English title and description, and request review once CI passes. [@claim:clm_059a883de673835b4c954621f5e5b33618215d2cfcb75ee46ef518fe64ab7c1e]
- The repository is organized into five main parts: a CDK infrastructure directory, an agent-core shared module, a Slack Bolt app, a worker package containing the AI agent implementation and tool suite, and a Next.js webapp. [@claim:clm_dd4be6fd6c0a5cb88bf97a6edd6cfdbd3588505cc70fef926ad6bb25e23c801d]
<!-- rcw:end owner=source:src_587abd3e0a195643a6772252f3cf2216 block=evidence -->

## Researcher notes

