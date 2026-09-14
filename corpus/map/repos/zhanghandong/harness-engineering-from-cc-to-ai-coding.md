# zhanghandong/harness-engineering-from-cc-to-ai-coding

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit e40e0feec02b @ 62d8f458f85dc19c

## Summary (orientation draft, not independently verified)

Selected evidence records: The repository publishes a Chinese technical book on Harness Engineering, analyzed from the publicly released Claude Code v2.1.88 package and its source-map reconstruction rather than official docs. The book targets engineers building AI coding products, agent frameworks, and tool-calling platforms who want to understand Claude Code's implementation details.

## Source coverage

Source coverage (partial): 6 of 11 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications (4 claim(s)):
  - [observation/documented] The book is organized into seven main parts (architecture, prompt engineering, context management, prompt caching, security/permissions, advanced subsystems, lessons) plus four appendices. -- evidence: [README.md#L29-L29](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.md#L29-L29), [README.md#L31-L37](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.md#L31-L37)
  - [observation/documented] The analysis is stated to be based on reverse-engineering 1,902 TypeScript source files of Claude Code v2.1.88. -- evidence: [docs/book-outline.md#L5-L5](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/docs/book-outline.md#L5-L5)
- components (1 claim(s)):
  - [observation/documented] The reverse-engineering guide documents helper scripts: scripts/extract-signals.sh for string-constant mining and scripts/cc-version-diff.sh for structured version-to-version diff reports. -- evidence: [docs/reverse-engineering-guide.md#L178-L185](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/docs/reverse-engineering-guide.md#L178-L185), [docs/reverse-engineering-guide.md#L169-L169](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/docs/reverse-engineering-guide.md#L169-L169), [docs/reverse-engineering-guide.md#L101-L101](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/docs/reverse-engineering-guide.md#L101-L101), [docs/reverse-engineering-guide.md#L165-L165](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/docs/reverse-engineering-guide.md#L165-L165), [docs/reverse-engineering-guide.md#L97-L97](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/docs/reverse-engineering-guide.md#L97-L97)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Local preview is done with 'mdbook build book' and 'mdbook serve book', serving by default at http://localhost:3000. -- evidence: [README.en.md#L35-L38](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.en.md#L35-L38), [README.md#L54-L54](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.md#L54-L54), [README.en.md#L42-L42](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.en.md#L42-L42), [README.md#L47-L50](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.md#L47-L50)
  - [observation/documented] The repository intentionally tracks only files needed to publish the book to GitHub Pages; the English edition is a scaffolded preview while the Chinese edition is canonical. -- evidence: [README.md#L58-L61](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.md#L58-L61), [README.en.md#L46-L48](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.en.md#L46-L48), [README.en.md#L11-L11](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.en.md#L11-L11)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (2 claim(s)):
  - [observation/documented] A dedicated chapter documents Claude Code's shortcomings as analyzed by the book, including cache fragility, compaction information loss, text-only Grep limits, silent truncation, and flag complexity. -- evidence: [docs/book-outline.md#L280-L285](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/docs/book-outline.md#L280-L285)
  - [inference/documented] The book explicitly disclaims official status: it is reverse-engineering-based research and does not represent Anthropic's official documentation or positions. -- evidence: [README.md#L58-L61](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.md#L58-L61), [README.en.md#L46-L48](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.en.md#L46-L48)
- relevance (2 claim(s)):
  - [observation/documented] The repository publishes a Chinese technical book on Harness Engineering, analyzed from the publicly released Claude Code v2.1.88 package and its source-map reconstruction rather than official docs. -- evidence: [README.en.md#L9-L9](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.en.md#L9-L9), [README.md#L11-L11](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.md#L11-L11)
  - [observation/documented] The book targets engineers building AI coding products, agent frameworks, and tool-calling platforms who want to understand Claude Code's implementation details. -- evidence: [README.md#L41-L43](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.md#L41-L43), [README.en.md#L29-L31](https://github.com/ZhangHanDong/harness-engineering-from-cc-to-ai-coding/blob/e40e0feec02b90e308ccbfc7a8911d64118ccca0/README.en.md#L29-L31)
More evidence: [full detail](harness-engineering-from-cc-to-ai-coding.detail.md)

Metadata and full claim list: [full detail](harness-engineering-from-cc-to-ai-coding.detail.md)
Human notes ([notes](harness-engineering-from-cc-to-ai-coding.notes.md), never overwritten by build)

[Back to map index](../../index.md)
