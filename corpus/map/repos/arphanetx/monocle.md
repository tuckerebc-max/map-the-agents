# arphanetx/monocle

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6a865d767a96 @ 82058386115fbb7c

## Summary (orientation draft, not independently verified)

Monocle is an LLM-backed binary analysis search tool that decompiles binaries via Ghidra headless and uses Mistral-7B-Instruct-v0.2 to score functions against natural-language search criteria. Evidence covers its purpose, CLI, dependencies, output format, and contribution guidelines.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Monocle performs natural language searches against compiled binaries: given a binary and search criteria, it decompiles the binary and uses an in-built LLM to identify and score matching code areas. -- evidence: [README.md#L17-L20](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L17-L20)
- components (1 claim(s)):
  - [observation/documented] Monocle uses Ghidra headless to enable decompilation of compiled binaries. -- evidence: [README.md#L17-L20](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L17-L20)
- design-choices (1 claim(s)):
  - [observation/documented] Queries are written in plain text because the tool is backed by an LLM, allowing open-ended natural language questions about a binary without prior knowledge. -- evidence: [README.md#L17-L20](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L17-L20)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors should fork the repo, create a descriptively named branch, test changes, submit a pull request with a detailed description, and address maintainer feedback before merge. -- evidence: [README.md#L106-L111](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L106-L111), [README.md#L103-L104](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L103-L104)
  - [observation/documented] Repository development practice: the project follows the Contributor Covenant Code of Conduct, and bugs or feature requests should be reported via GitHub issues with reproduction details. -- evidence: [README.md#L114-L114](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L114-L114), [README.md#L117-L117](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L117-L117)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI takes a binary path and a search target, e.g. monocle --binary <path-to-binary> --find <component-to-find> on Unix, with a monocle.exe variant on Windows. -- evidence: [README.md#L56-L63](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L56-L63)
  - [observation/documented] While processing, Monocle shows a live table sorted by score, listing each analyzed function with a 0-10 relevance score and an explanation; zero-scored functions get no explanation. -- evidence: [README.md#L65-L65](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L65-L65)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (3 claim(s)):
  - [observation/documented] The runtime model is Mistral-7B-Instruct-v0.2, an instruct fine-tuned Mistral-7B-v0.2 with 7.24B parameters, BF16 tensors, and a 32k context window. -- evidence: [README.md#L95-L100](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L95-L100), [README.md#L25-L25](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L25-L25)
  - [observation/documented] Monocle requires Nvidia CUDA for improved LLM performance, plus Ghidra installed with analyzeHeadless available in the environment. -- evidence: [README.md#L35-L35](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L35-L35), [README.md#L30-L33](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L30-L33)
- limitations (2 claim(s)):
  - [observation/documented] At least 16GB RAM and a dedicated Nvidia GPU with 4GB+ memory are recommended; lower-spec machines can run it but significantly slower. -- evidence: [README.md#L25-L25](https://github.com/arphanetx/Monocle/blob/6a865d767a9623af4e72cd1c2b9e39e62db45105/README.md#L25-L25)
More evidence: [full detail](monocle.detail.md)

Metadata and full claim list: [full detail](monocle.detail.md)
Human notes ([notes](monocle.notes.md), never overwritten by build)

[Back to map index](../../index.md)
