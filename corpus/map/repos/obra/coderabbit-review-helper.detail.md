# obra/coderabbit-review-helper -- full detail

[Back to orientation](coderabbit-review-helper.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/obra/coderabbit-review-helper/de5963701c376bcaf273df36cf43c3d1a53cac25/4505dbfc98add824.json](../../../wiki/dossiers/obra/coderabbit-review-helper/de5963701c376bcaf273df36cf43c3d1a53cac25/4505dbfc98add824.json)

## specifications (1 claim(s))

- [observation/documented] The tool converts CodeRabbit GitHub PR reviews into clean, LLM-friendly text intended for AI-assisted code improvement workflows. -- evidence: [README.md#L3-L3](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L3-L3) (`clm_3fd957df9f901be7306f6fa827c387f905b4691e3ec9cd56917019c3c8a6c988`)

## components (1 claim(s))

- [observation/documented] Output groups feedback by file, sorts AI-actionable (robot-marked) items first within each file, and reports totals such as files with feedback and comment counts. -- evidence: [README.md#L86-L87](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L86-L87), [README.md#L71-L73](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L71-L73) (`clm_475b4e74ab2d89b96f846561c2cd5e04b27e6078e7eb0ff152b193d476ea9031`)

## design-choices (2 claim(s))

- [observation/documented] The output prioritizes detailed AI prompts over diffs, never shows both prompt and diff for the same suggestion, and strips GitHub web-interface HTML artifacts. -- evidence: [README.md#L76-L79](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L76-L79), [README.md#L215-L223](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L215-L223) (`clm_d30cf7656c08b6db7b696d1f60c166868b915388aa022838f60999f0f933dbf7`)
- [observation/documented] The tool organizes three feedback categories: AI-actionable items with implementation prompts, nitpick comments with simple diffs, and outside-diff-range comments with broader context. -- evidence: [README.md#L178-L178](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L178-L178), [README.md#L187-L189](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L187-L189), [README.md#L181-L184](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L181-L184), [README.md#L192-L194](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L192-L194) (`clm_4aea7d6fc977893c12a5b9ea77bca2020c020b14d1e72b957eb6ecafebb1f988`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The CLI accepts a PR as a full GitHub URL or short owner/repo/123 format, and supports --all-reviews, --since-commit (listed as coming soon), --debug, and --help flags. -- evidence: [README.md#L116-L118](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L116-L118), [README.md#L22-L22](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L22-L22), [README.md#L19-L19](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L19-L19), [README.md#L124-L125](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L124-L125), [README.md#L121-L121](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L121-L121), [README.md#L25-L26](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L25-L26) (`clm_ad550ff1ea1b7d8a9eae51253dc193f5d4401671561d8280a9fdcbcc53ca8377`)
- [observation/documented] By default the tool extracts only the latest review to avoid overwhelming output on PRs with many reviews; --all-reviews extracts every CodeRabbit review instead. -- evidence: [README.md#L116-L118](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L116-L118), [README.md#L133-L133](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L133-L133), [README.md#L136-L137](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L136-L137), [README.md#L71-L73](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L71-L73) (`clm_ef043f95d45372e533ba352c512edd009853723e55bb7173a8eb0fe7568bc1bc`)

## memory-state (1 claim(s))

- [observation/documented] Users can place custom text in ~/.coderabbit-extractor to prepend a preamble to output; the bundled example preamble instructs the AI agent to critically evaluate the reviewer and its suggestions. -- evidence: [README.md#L141-L141](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L141-L141), [example-preamble.txt#L1-L1](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/example-preamble.txt#L1-L1), [README.md#L149-L150](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L149-L150), [example-preamble.txt#L7-L8](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/example-preamble.txt#L7-L8), [README.md#L146-L146](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L146-L146), [example-preamble.txt#L3-L5](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/example-preamble.txt#L3-L5) (`clm_3466017212161a35658797a5ac9315b5c9486621ecd027eff50a5d895d2f3864`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Requirements are an authenticated GitHub CLI (gh), Python 3.6+, and the beautifulsoup4 package; requirements.txt specifies beautifulsoup4>=4.9.0. -- evidence: [README.md#L31-L33](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L31-L33), [requirements.txt#L1-L1](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/requirements.txt#L1-L1) (`clm_dc91efe3e73677a97abb3b9ddaba079fddbecc060356f6444be13efb08c9da9b`)

## limitations (1 claim(s))

- [observation/documented] The --since-commit option (extracting reviews after a specific commit) is documented as 'coming soon', i.e. not yet available. -- evidence: [README.md#L116-L118](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L116-L118) (`clm_588732bca7cd5a27c1da5c12b6be4da08970a198ec35fab3eddd87733ef1349d`)

## relevance (1 claim(s))

- [observation/documented] The tool targets AI-assisted development workflows such as automated code improvement pipelines and converting review feedback into actionable prompts, and is MIT licensed. -- evidence: [README.md#L234-L234](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L234-L234), [README.md#L9-L13](https://github.com/obra/coderabbit-review-helper/blob/de5963701c376bcaf273df36cf43c3d1a53cac25/README.md#L9-L13) (`clm_6904c9bc3951dcb7ee5c50aff53dc63e5d09abbcb38bddab0ca3b4a3a691bdf1`)

