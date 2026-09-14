---
access: public
aliases: []
claim_ids:
- clm_9a76a549662b2421f785e6ccdb42c4f38db9fe766c43ed4b58f73a2b59a93389
- clm_ae6737a936e8bc68260bf5dd36c5888da7c61e3071fb7c20dbde768e804bcf57
maturity: draft
page_id: pg_49bc2e95db7d51fca09a872b75292692
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bd14f38d5319510aaa5289cafd1e81ba
title: boringcomputers/nehemiah/docs/architecture.md @ fea6f0a52991
updated_at: '2026-09-14T03:39:33Z'
---

# boringcomputers/nehemiah/docs/architecture.md @ fea6f0a52991

<!-- rcw:begin owner=source:src_bd14f38d5319510aaa5289cafd1e81ba block=evidence -->
- In local mode the guest shell runs over serial: the kernel boots with console=ttyS0 and nehemiahd pumps the Firecracker child's stdin/stdout as the terminal, working identically for cold-boot and snapshot-restored VMs. [@claim:clm_9a76a549662b2421f785e6ccdb42c4f38db9fe766c43ed4b58f73a2b59a93389]
- The local daemon exposes a REST API on port 8080 (machine create/list/get/delete, branch, and a /tty WebSocket with binary frames) plus an open /healthz endpoint. [@claim:clm_ae6737a936e8bc68260bf5dd36c5888da7c61e3071fb7c20dbde768e804bcf57]
<!-- rcw:end owner=source:src_bd14f38d5319510aaa5289cafd1e81ba block=evidence -->

## Researcher notes

