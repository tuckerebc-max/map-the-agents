# 2389-research/binary-re

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit 42aee9063f3f @ fa6ea75b7b34d0e2

## Summary (orientation draft, not independently verified)

The repository is a Claude Code plugin ('binary-re') providing a hypothesis-driven binary reverse-engineering skill, supported by per-architecture tooling docs, Ghidra headless guidance, Python bytecode RE notes, and a dated LZSS bug case study. Prior claim about Ghidra download source and soft-float sysroots was unsupported and has been removed. Evidence coverage: 192 of 242 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The repo includes reference documentation covering per-architecture tooling considerations (ARM, ARM64, x86_64, MIPS), Ghidra headless decompilation usage, and Python bytecode reverse engineering. -- evidence: [docs/python-bytecode-re.md#L5-L5](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/python-bytecode-re.md#L5-L5), [docs/arch-adapters.md#L5-L5](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/arch-adapters.md#L5-L5), [docs/ghidra-headless.md#L5-L5](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/ghidra-headless.md#L5-L5)
  - [observation/documented] A dated case-study document analyzes an LZSS compressor binary, identifying a window-position wrap bug in decompression and a 9-byte instruction-reorder patch verified by MD5 comparison of outputs. -- evidence: [docs/bad-compression-analysis-2026-01-06.md#L112-L116](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/bad-compression-analysis-2026-01-06.md#L112-L116), [docs/bad-compression-analysis-2026-01-06.md#L106-L108](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/bad-compression-analysis-2026-01-06.md#L106-L108), [docs/bad-compression-analysis-2026-01-06.md#L5-L7](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/bad-compression-analysis-2026-01-06.md#L5-L7), [docs/bad-compression-analysis-2026-01-06.md#L77-L77](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/bad-compression-analysis-2026-01-06.md#L77-L77)
- design-choices (2 claim(s)):
  - [observation/documented] The stated philosophy is that the LLM drives analysis while the human provides context: the user supplies platform, hardware, theories, and constraints, and Claude runs tools, forms hypotheses, and designs experiments. -- evidence: [README.md#L80-L80](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L80-L80), [README.md#L84-L84](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L84-L84), [README.md#L82-L82](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L82-L82)
  - [observation/documented] The example interaction shows the skill recording facts, stating a hypothesis with a confidence score of 0.7, then asking the user whether to proceed with static analysis or dynamic analysis under QEMU. -- evidence: [README.md#L49-L51](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L49-L51), [README.md#L44-L47](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L44-L47), [README.md#L53-L55](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L53-L55)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns (2 claim(s)):
  - [observation/documented] The plugin ships a 'binary-re' skill described as a structured RE workflow with hypothesis-driven analysis, driven by hypothesis-testing rather than blind exploration. -- evidence: [README.md#L16-L16](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L16-L16), [README.md#L3-L3](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L3-L3)
  - [observation/documented] The case study records lessons for the skill: compare known inputs/outputs first, trace circular-buffer wrap-around carefully, and watch for divergent code paths implementing the same operation. -- evidence: [docs/bad-compression-analysis-2026-01-06.md#L124-L124](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/bad-compression-analysis-2026-01-06.md#L124-L124), [docs/bad-compression-analysis-2026-01-06.md#L122-L122](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/bad-compression-analysis-2026-01-06.md#L122-L122), [docs/bad-compression-analysis-2026-01-06.md#L126-L126](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/docs/bad-compression-analysis-2026-01-06.md#L126-L126)
- interfaces (1 claim(s)):
  - [observation/documented] Installation is via Claude Code plugin marketplace commands: '/plugin marketplace add 2389-research/claude-plugins' followed by '/plugin install binary-re@2389-research'. -- evidence: [README.md#L7-L10](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L7-L10)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] The skill asks for confirmation before executing binaries (even sandboxed), network-capable dynamic analysis, operations requiring device access, and major changes in analysis direction. -- evidence: [README.md#L88-L92](https://github.com/2389-research/binary-re/blob/42aee9063f3f3d52616700df3aa16df82b848604/README.md#L88-L92)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
More evidence: [full detail](binary-re.detail.md)

Metadata and full claim list: [full detail](binary-re.detail.md)
Human notes ([notes](binary-re.notes.md), never overwritten by build)

[Back to map index](../../index.md)
