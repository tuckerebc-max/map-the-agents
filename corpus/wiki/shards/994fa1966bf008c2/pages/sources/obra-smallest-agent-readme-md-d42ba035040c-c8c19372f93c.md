---
access: public
aliases: []
claim_ids:
- clm_32cacb367813ac018f73ecada1db5787dbd18d73a1c3d66d50ecc3c2773f3348
- clm_5c8ced439292e206a5d4bc3a24fcf3c612716946f4bfa107415556d8a7b3f9d8
- clm_7e070eab8a8d6517221599c568af19e2aea4e96f6d520edf236f9dc23ff58e84
- clm_b661f11ccd969db6d6a601c6d310bcd3825b710999ae1e32833f2fb3a4e3dc1a
- clm_ef08e8d1e57d097f5ade2f91867460b7bd0ec93e53dea87e4edf51b1f19b86fd
maturity: draft
page_id: pg_2e4f8b7282b253a293efc8c19372f93c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_38e37995dad7598c9af7d7156549b585
title: obra/smallest-agent/README.md @ d42ba035040c
updated_at: '2026-09-14T03:10:37Z'
---

# obra/smallest-agent/README.md @ d42ba035040c

<!-- rcw:begin owner=source:src_38e37995dad7598c9af7d7156549b585 block=evidence -->
- The README warns the agent has unrestricted bash access and can do anything, including destructive actions. [@claim:clm_32cacb367813ac018f73ecada1db5787dbd18d73a1c3d66d50ecc3c2773f3348]
- Repository development practice: npm test runs a repeatable smoke test against the live API covering 'hi', uuidgen, and a failing shell command. [@claim:clm_5c8ced439292e206a5d4bc3a24fcf3c612716946f4bfa107415556d8a7b3f9d8]
- The project originated as an experiment in how small a functional coding agent could be; an earlier draft was then set to golf itself down over about 20 minutes. [@claim:clm_7e070eab8a8d6517221599c568af19e2aea4e96f6d520edf236f9dc23ff58e84]
- The minified agent source src/smallest-agent.js is stated to be 493 bytes, with a separately commented, more readable variant of the same code. [@claim:clm_b661f11ccd969db6d6a601c6d310bcd3825b710999ae1e32833f2fb3a4e3dc1a]
- Repository development practice: the final minification step is done with terser -c -m --module on the commented source, per the README. [@claim:clm_ef08e8d1e57d097f5ade2f91867460b7bd0ec93e53dea87e4edf51b1f19b86fd]
<!-- rcw:end owner=source:src_38e37995dad7598c9af7d7156549b585 block=evidence -->

## Researcher notes

