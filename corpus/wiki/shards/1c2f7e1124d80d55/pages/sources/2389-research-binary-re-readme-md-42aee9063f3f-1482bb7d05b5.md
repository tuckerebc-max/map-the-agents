---
access: public
aliases: []
claim_ids:
- clm_36d3adddb1c1512f5da3cd83283c196217521694e3075cc544a3bc78429f0993
- clm_5fc43892852603f17cd786b50be6fff722d04b80118e640a1d1863e552eded77
- clm_9c886225fbed3bab1747bdb8ad8417e4a35fca5eb14b483119b64816ccff7cb1
- clm_9d44c3cf6906aad16366cfc5e077b1295f4e0242f31e3bea36d3be2f73a5c5be
- clm_db1dc933e9900f1bd3d50f0946ee0369a125a3731bcbd64642929293e9648ce0
- clm_e7295b2093cdf142c0d288f5b9d22d7ff5129dd115d4a4f6ef6559afb4f0c6dc
- clm_f5ec2725684eae24f606cc5f01f3ba2624d8f1baf909c7af4ed5d1dc79d90437
maturity: draft
page_id: pg_f89d58d6477a5c908b081482bb7d05b5
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_da3c62d57db655ed8a4b5d3fc51e7811
title: 2389-research/binary-re/README.md @ 42aee9063f3f
updated_at: '2026-09-14T03:28:43Z'
---

# 2389-research/binary-re/README.md @ 42aee9063f3f

<!-- rcw:begin owner=source:src_da3c62d57db655ed8a4b5d3fc51e7811 block=evidence -->
- Installation is via Claude Code plugin marketplace commands: '/plugin marketplace add 2389-research/claude-plugins' followed by '/plugin install binary-re@2389-research'. [@claim:clm_36d3adddb1c1512f5da3cd83283c196217521694e3075cc544a3bc78429f0993]
- The stated philosophy is that the LLM drives analysis while the human provides context: the user supplies platform, hardware, theories, and constraints, and Claude runs tools, forms hypotheses, and designs experiments. [@claim:clm_5fc43892852603f17cd786b50be6fff722d04b80118e640a1d1863e552eded77]
- Required external tools include radare2, qemu-user, and gdb-multiarch installed via apt, plus frida-tools via pip and ARM hard-float/arm64 cross sysroot packages (libc6-armhf-cross, libc6-arm64-cross). [@claim:clm_9c886225fbed3bab1747bdb8ad8417e4a35fca5eb14b483119b64816ccff7cb1]
- The example interaction shows the skill recording facts, stating a hypothesis with a confidence score of 0.7, then asking the user whether to proceed with static analysis or dynamic analysis under QEMU. [@claim:clm_9d44c3cf6906aad16366cfc5e077b1295f4e0242f31e3bea36d3be2f73a5c5be]
- The plugin ships a 'binary-re' skill described as a structured RE workflow with hypothesis-driven analysis, driven by hypothesis-testing rather than blind exploration. [@claim:clm_db1dc933e9900f1bd3d50f0946ee0369a125a3731bcbd64642929293e9648ce0]
- Stated use cases include firmware analysis, protocol reverse engineering, security research on embedded systems, and hardware hacking of robot/IoT device internals. [@claim:clm_e7295b2093cdf142c0d288f5b9d22d7ff5129dd115d4a4f6ef6559afb4f0c6dc]
- The skill asks for confirmation before executing binaries (even sandboxed), network-capable dynamic analysis, operations requiring device access, and major changes in analysis direction. [@claim:clm_f5ec2725684eae24f606cc5f01f3ba2624d8f1baf909c7af4ed5d1dc79d90437]
<!-- rcw:end owner=source:src_da3c62d57db655ed8a4b5d3fc51e7811 block=evidence -->

## Researcher notes

