---
access: public
aliases: []
claim_ids:
- clm_02ebf76a05bd8cb850c17aa49a63d0f4f07f9da47fa51796d2542c48213fc273
- clm_901e94172194af794762b741fb1af4ede0b419ea88fd915ad4147016079f3684
maturity: draft
page_id: pg_e1e685d2d9885915bf44867f6fe6d069
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ca8490582aac55b2babb18e9f9f1c89a
title: SquareWaveSystems/squarebox/docs/adr/0001-fail-closed-artifact-installation.md
  @ 8c1f97fcfb57
updated_at: '2026-09-14T04:23:14Z'
---

# SquareWaveSystems/squarebox/docs/adr/0001-fail-closed-artifact-installation.md @ 8c1f97fcfb57

<!-- rcw:begin owner=source:src_ca8490582aac55b2babb18e9f9f1c89a block=evidence -->
- The ADR notes its rollback guarantee is not crash atomicity—power loss during a multi-path commit can leave staged files needing inspection—and dpkg package operations fall outside the rollback guarantee. [@claim:clm_02ebf76a05bd8cb850c17aa49a63d0f4f07f9da47fa51796d2542c48213fc273]
- Artifact installation is fail-closed: GitHub-hosted optional tools require an exact release tag, one exactly named asset, and a matching SHA-256 digest, failing before download or extraction on missing or malformed metadata. [@claim:clm_901e94172194af794762b741fb1af4ede0b419ea88fd915ad4147016079f3684]
<!-- rcw:end owner=source:src_ca8490582aac55b2babb18e9f9f1c89a block=evidence -->

## Researcher notes

