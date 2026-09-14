---
access: public
aliases: []
claim_ids:
- clm_2497cb3e3c24a6c42b4703774043b26d17a6b3ffa14d90290dabd285faf69196
- clm_49cecca808c9b69673572d73ea82b182f6e3a8e3c3be5d181df0dacadcff8d49
- clm_6db76b511b4e0757606e6e78946f762eea12f230874571947b7f8e5cf7eb718e
- clm_86b1491f8552eb44bc3212aaebcbd24ef94d8229cb18d0c44eeddaf1d11405e9
- clm_af975098dfe5e6c90cec3cae92ed1a0547cd6f25c6568b6208cd03c8b5487095
- clm_c91721ef053953c0cf728c2c5a45f19c6b2ee4630c8f8ce774bcb08a8bc23505
- clm_cf859cfb002088c1cde2700bca96d733a8a447f98c2847a294417de7fb108001
- clm_dfedc3d12440d425f2ce8f6881281c57b133753d9b037201982221e7b52afa56
maturity: draft
page_id: pg_820c0ab7ef7854cabfac225b425d3e8f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ec12f1e3f976584ca6d63a033ec07e79
title: whut09/opencode-plusplus/README.md @ 598767170bb7
updated_at: '2026-09-14T04:31:25Z'
---

# whut09/opencode-plusplus/README.md @ 598767170bb7

<!-- rcw:begin owner=source:src_ec12f1e3f976584ca6d63a033ec07e79 block=evidence -->
- Runtime artifacts are local per repository: traces, runs, loops, sidecar latest.md and visualization.json, plus cache, context-registry usage/feedback, annotations, and interventions directories under .agent-context/. [@claim:clm_2497cb3e3c24a6c42b4703774043b26d17a6b3ffa14d90290dabd285faf69196]
- By default the plugin works offline: it does not fetch remote Context sources or call a second model; remote sources or feedback transports must be explicitly enabled. [@claim:clm_49cecca808c9b69673572d73ea82b182f6e3a8e3c3be5d181df0dacadcff8d49]
- The plugin explicitly is not an operating-system sandbox; it cannot stop another application from editing a file or prove business semantics from an exit code. [@claim:clm_6db76b511b4e0757606e6e78946f762eea12f230874571947b7f8e5cf7eb718e]
- The Windows installer adds a selectable OpenCode primary mode named OpenCode++ chosen from the mode picker, with no Slash Commands to remember. [@claim:clm_86b1491f8552eb44bc3212aaebcbd24ef94d8229cb18d0c44eeddaf1d11405e9]
- Repository development practice: contributors fork, read AGENTS.md, add deterministic tests before behavior changes, keep runtime artifacts out of commits, and run npm run check, lint, format:check, docs:bilingual:check, and npm test. [@claim:clm_af975098dfe5e6c90cec3cae92ed1a0547cd6f25c6568b6208cd03c8b5487095]
- The plugin runs in-process inside OpenCode Desktop, does not start a second model or CLI process, and does not expose hidden model chain-of-thought. [@claim:clm_c91721ef053953c0cf728c2c5a45f19c6b2ee4630c8f8ce774bcb08a8bc23505]
- Desktop results default to a compact Verified, Repair required, or Human review status, with structured JSON containing an actionSummary of observed, prevented, requested, repaired, verified, and unresolved items. [@claim:clm_cf859cfb002088c1cde2700bca96d733a8a447f98c2847a294417de7fb108001]
- A passing command alone is evidence, not a correctness proof; verified fixes require fresh command or CI evidence matched to the current working tree, and blocking results require repair or human review. [@claim:clm_dfedc3d12440d425f2ce8f6881281c57b133753d9b037201982221e7b52afa56]
<!-- rcw:end owner=source:src_ec12f1e3f976584ca6d63a033ec07e79 block=evidence -->

## Researcher notes

