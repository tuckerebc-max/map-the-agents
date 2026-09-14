---
access: public
aliases: []
claim_ids:
- clm_018442b9651ada44c2ed6dbbe81441788b2e84ec42c2362bef69b7aa4e2c0dea
- clm_18d10fd31b97f44d1b2a2edcf4470129f985dfbc558758818bd48a6b15d03600
- clm_3c1c188a716f1da30c780e6a064266f8a8a121f01f683af7df62cb0de0dc3e4a
- clm_55bf3fc0cd120da9bdc12600958a081255941f84501907bfb198571ed8ff4b77
maturity: draft
page_id: pg_f1e5d771766057c38750231a56abcaf7
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bf99d52ce8d355e4850829127bf12730
title: manaflow-ai/cmux/PR-10599-AUDIT.md @ 419cf0a00cc3
updated_at: '2026-09-14T02:14:59Z'
---

# manaflow-ai/cmux/PR-10599-AUDIT.md @ 419cf0a00cc3

<!-- rcw:begin owner=source:src_bf99d52ce8d355e4850829127bf12730 block=evidence -->
- Repository development practice: contributors must sign a CLA (v2.2), which can be signed electronically by posting an exact phrase as a PR comment; the PR audit notes the contributor's unsigned CLA as an external blocker. [@claim:clm_018442b9651ada44c2ed6dbbe81441788b2e84ec42c2362bef69b7aa4e2c0dea]
- Repository development practice: the PR audit documents review-tooling gates (Cursor Bugbot, CodeRabbit, Vercel preview authorization) and notes all 58 inline review threads resolved at the audited head. [@claim:clm_18d10fd31b97f44d1b2a2edcf4470129f985dfbc558758818bd48a6b15d03600]
- Repository development practice: the PR #10599 audit records focused Swift package test runs (e.g., 11 tests in CmuxFilePreviewCore, 24 in CmuxSyntaxHighlighting) plus project lint/check scripts such as check-pbxproj.sh and lint-pbxproj-test-wiring.sh. [@claim:clm_3c1c188a716f1da30c780e6a064266f8a8a121f01f683af7df62cb0de0dc3e4a]
- The PR audit states Highlightr is pinned exactly and that the audited change introduced no shell execution, network/eval, path traversal, authentication, or secret-handling paths. [@claim:clm_55bf3fc0cd120da9bdc12600958a081255941f84501907bfb198571ed8ff4b77]
<!-- rcw:end owner=source:src_bf99d52ce8d355e4850829127bf12730 block=evidence -->

## Researcher notes

