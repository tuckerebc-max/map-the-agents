# lidangzzz/ai-coding-style-guides

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 16f2f9c646d2 @ 64afa9d674f12c13

## Summary (orientation draft, not independently verified)

The repository is a documentation project: an AI coding style guide (English and Chinese READMEs) plus a TOML file of prompts intended to instruct LLMs to compress source code for vibe-coding/SWE-agent workflows. Evidence covers the guide's motivation, rules, compression levels, worked examples, and usage instructions; no runtime code or agent implementation is evidenced. Evidence coverage: 140 of 250 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (4 claim(s)):
  - [observation/documented] The project ships a set of coding style guides, including general guides for common languages and guides tailored to specific languages and scenarios, aimed at maximizing code compression. -- evidence: [README.md#L30-L30](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L30-L30)
  - [observation/documented] Basic rules include minimizing whitespace, keeping full names for top-level entities while shortening local variables, brief comments only at top level, and co-locating related code in single files. -- evidence: [README.md#L54-L54](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L54-L54), [README.md#L58-L58](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L58-L58), [README.md#L52-L52](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L52-L52), [README.md#L56-L56](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L56-L56)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (3 claim(s)):
  - [observation/documented] The stated goal is to maximize code compression across languages while keeping reasonable human readability, balancing compactness against context-window savings. -- evidence: [README.md#L32-L32](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L32-L32)
  - [observation/documented] The guide's rationale cites three trends: growing LLM capability, perpetually insufficient context windows, and reduced importance of human readability when agents do most programming. -- evidence: [README.md#L42-L42](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L42-L42), [README.md#L40-L40](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L40-L40), [README.md#L38-L38](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L38-L38)
- workflows (2 claim(s)):
  - [observation/documented] Usage instructions tell readers to open AI_Coding_Style_Guide_prompts.toml, copy its prompts into their own prompt management system, and optionally modify them for their needs. -- evidence: [README.md#L9-L9](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L9-L9), [README.md#L11-L11](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L11-L11)
  - [observation/documented] A Python snippet using the toml library is provided to load prompts from the TOML file into a user's prompt management system. -- evidence: [README.md#L15-L22](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L15-L22)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (3 claim(s)):
  - [observation/documented] The README demonstrates compression on a 1216-character TypeScript KMP implementation, showing staged reductions to 795, 715, 443, and finally 283 characters (~23.3% of original). -- evidence: [README.md#L198-L198](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L198-L198), [README.md#L89-L89](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L89-L89), [README.md#L209-L209](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L209-L209), [README.md#L218-L218](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L218-L218), [README.md#L147-L147](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L147-L147)
  - [observation/documented] The guide benchmarks against conventional tools: JSCompress output was 348 characters (~28.6%) for the compiled JavaScript, and jsonminify.com produced 2144 characters (~79.2%) for the C++ example. -- evidence: [README.md#L433-L433](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L433-L433), [README.md#L226-L226](https://github.com/lidangzzz/AI-Coding-Style-Guides/blob/16f2f9c646d240929567f76ac07643d4426679aa/README.md#L226-L226)
- dependencies: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](ai-coding-style-guides.detail.md)

Metadata and full claim list: [full detail](ai-coding-style-guides.detail.md)
Human notes ([notes](ai-coding-style-guides.notes.md), never overwritten by build)

[Back to map index](../../index.md)
