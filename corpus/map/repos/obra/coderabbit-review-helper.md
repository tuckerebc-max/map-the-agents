# obra/coderabbit-review-helper

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit de5963701c37 @ 4505dbfc98add824

## Summary (orientation draft, not independently verified)

Selected evidence records: The tool converts CodeRabbit GitHub PR reviews into clean, LLM-friendly text intended for AI-assisted code improvement workflows. The CLI accepts a PR as a full GitHub URL or short owner/repo/123 format, and supports --all-reviews, --since-commit (listed as coming soon), --debug, and --help flags.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The tool converts CodeRabbit GitHub PR reviews into clean, LLM-friendly text intended for AI-assisted code improvement workflows. -- evidence: [README.md#L3-L3](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L3-L3)
- components (1 claim(s)):
  - [observation/documented] Output groups feedback by file, sorts AI-actionable (robot-marked) items first within each file, and reports totals such as files with feedback and comment counts. -- evidence: [README.md#L86-L87](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L86-L87), [README.md#L71-L73](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L71-L73)
- design-choices (2 claim(s)):
  - [observation/documented] The output prioritizes detailed AI prompts over diffs, never shows both prompt and diff for the same suggestion, and strips GitHub web-interface HTML artifacts. -- evidence: [README.md#L76-L79](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L76-L79), [README.md#L215-L223](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L215-L223)
  - [observation/documented] The tool organizes three feedback categories: AI-actionable items with implementation prompts, nitpick comments with simple diffs, and outside-diff-range comments with broader context. -- evidence: [README.md#L178-L178](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L178-L178), [README.md#L187-L189](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L187-L189), [README.md#L181-L184](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L181-L184), [README.md#L192-L194](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L192-L194)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI accepts a PR as a full GitHub URL or short owner/repo/123 format, and supports --all-reviews, --since-commit (listed as coming soon), --debug, and --help flags. -- evidence: [README.md#L116-L118](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L116-L118), [README.md#L22-L22](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L22-L22), [README.md#L19-L19](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L19-L19), [README.md#L124-L125](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L124-L125), [README.md#L121-L121](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L121-L121), [README.md#L25-L26](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L25-L26)
  - [observation/documented] By default the tool extracts only the latest review to avoid overwhelming output on PRs with many reviews; --all-reviews extracts every CodeRabbit review instead. -- evidence: [README.md#L116-L118](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L116-L118), [README.md#L133-L133](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L133-L133), [README.md#L136-L137](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L136-L137), [README.md#L71-L73](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L71-L73)
- memory-state (1 claim(s)):
  - [observation/documented] Users can place custom text in ~/.coderabbit-extractor to prepend a preamble to output; the bundled example preamble instructs the AI agent to critically evaluate the reviewer and its suggestions. -- evidence: [README.md#L141-L141](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L141-L141), [example-preamble.txt#L1-L1](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/example-preamble.txt#L1-L1), [README.md#L149-L150](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L149-L150), [example-preamble.txt#L7-L8](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/example-preamble.txt#L7-L8), [README.md#L146-L146](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L146-L146), [example-preamble.txt#L3-L5](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/example-preamble.txt#L3-L5)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Requirements are an authenticated GitHub CLI (gh), Python 3.6+, and the beautifulsoup4 package; requirements.txt specifies beautifulsoup4>=4.9.0. -- evidence: [README.md#L31-L33](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L31-L33), [requirements.txt#L1-L1](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/requirements.txt#L1-L1)
- limitations (1 claim(s)):
  - [observation/documented] The --since-commit option (extracting reviews after a specific commit) is documented as 'coming soon', i.e. not yet available. -- evidence: [README.md#L116-L118](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L116-L118)
- relevance (1 claim(s)):
More evidence: [full detail](coderabbit-review-helper.detail.md)

Metadata and full claim list: [full detail](coderabbit-review-helper.detail.md)
Human notes ([notes](coderabbit-review-helper.notes.md), never overwritten by build)

[Back to map index](../../index.md)
