---
access: public
aliases: []
claim_ids:
- clm_c8d0f5f6a73515c224d721bbe63f46ce55a2321f93b2c133dfb9351409ff6eeb
- clm_e7a1f02613658b4b09660e4f7825bbe680b467f2f60ac2799de83209f9102405
- clm_f0d0733e9b8c00fb2d8bf10f3ae31b2d54383ecabb1dcbcd95b8cc4deb2beeec
maturity: draft
page_id: pg_91d83107bffd5a7ebecec03c2c85204e
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7e9db388747f5b08887b9c6924f10ef1
title: 2389-research/binary-re/docs/arch-adapters.md @ 42aee9063f3f
updated_at: '2026-09-14T03:28:43Z'
---

# 2389-research/binary-re/docs/arch-adapters.md @ 42aee9063f3f

<!-- rcw:begin owner=source:src_7e9db388747f5b08887b9c6924f10ef1 block=evidence -->
- The repo includes reference documentation covering per-architecture tooling considerations (ARM, ARM64, x86_64, MIPS), Ghidra headless decompilation usage, and Python bytecode reverse engineering. [@claim:clm_c8d0f5f6a73515c224d721bbe63f46ce55a2321f93b2c133dfb9351409ff6eeb]
- The emulation compatibility matrix suggests MIPS 64 emulation is limited and less tested, and ARM 64 user-mode emulation requires a newer QEMU version. [@claim:clm_e7a1f02613658b4b09660e4f7825bbe680b467f2f60ac2799de83209f9102405]
- The architecture guide lists fallbacks when QEMU user-mode emulation fails: Qiling Framework, Unicorn CPU-only emulation, full-system QEMU, or running on actual hardware. [@claim:clm_f0d0733e9b8c00fb2d8bf10f3ae31b2d54383ecabb1dcbcd95b8cc4deb2beeec]
<!-- rcw:end owner=source:src_7e9db388747f5b08887b9c6924f10ef1 block=evidence -->

## Researcher notes

