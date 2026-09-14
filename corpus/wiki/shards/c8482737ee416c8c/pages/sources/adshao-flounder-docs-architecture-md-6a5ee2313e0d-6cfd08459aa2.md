---
access: public
aliases: []
claim_ids:
- clm_3dfb7167b74b95d3a06e253d2b9dd2dba6705134f181672214d0b221ef575e40
- clm_78e1d538ff4347db8e484a073c0e57ee0addbbf7b3a7ce206996f7dc21433806
maturity: draft
page_id: pg_ad5242590c0a5ec39e826cfd08459aa2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_57c7248325f15442a1f02a4c54eff8f9
title: adshao/flounder/docs/ARCHITECTURE.md @ 6a5ee2313e0d
updated_at: '2026-09-14T03:31:01Z'
---

# adshao/flounder/docs/ARCHITECTURE.md @ 6a5ee2313e0d

<!-- rcw:begin owner=source:src_57c7248325f15442a1f02a4c54eff8f9 block=evidence -->
- The framework is deliberately stack-agnostic: it encodes no Solidity, ZK, Rust, Go, or crypto-specific audit strategy; the model decides strategy while Flounder supplies sandbox, command policy, durable state, and reporting. [@claim:clm_3dfb7167b74b95d3a06e253d2b9dd2dba6705134f181672214d0b221ef575e40]
- The product includes an Evaluations control plane for durable audit, benchmark, regression, and verification run groups, with lifecycle and evidence axes kept separate so a build failure cannot count as a safe control pass. [@claim:clm_78e1d538ff4347db8e484a073c0e57ee0addbbf7b3a7ce206996f7dc21433806]
<!-- rcw:end owner=source:src_57c7248325f15442a1f02a4c54eff8f9 block=evidence -->

## Researcher notes

