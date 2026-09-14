---
access: public
aliases: []
claim_ids:
- clm_3466017212161a35658797a5ac9315b5c9486621ecd027eff50a5d895d2f3864
- clm_3fd957df9f901be7306f6fa827c387f905b4691e3ec9cd56917019c3c8a6c988
- clm_475b4e74ab2d89b96f846561c2cd5e04b27e6078e7eb0ff152b193d476ea9031
- clm_4aea7d6fc977893c12a5b9ea77bca2020c020b14d1e72b957eb6ecafebb1f988
- clm_588732bca7cd5a27c1da5c12b6be4da08970a198ec35fab3eddd87733ef1349d
- clm_6904c9bc3951dcb7ee5c50aff53dc63e5d09abbcb38bddab0ca3b4a3a691bdf1
- clm_ad550ff1ea1b7d8a9eae51253dc193f5d4401671561d8280a9fdcbcc53ca8377
- clm_d30cf7656c08b6db7b696d1f60c166868b915388aa022838f60999f0f933dbf7
- clm_dc91efe3e73677a97abb3b9ddaba079fddbecc060356f6444be13efb08c9da9b
- clm_ef043f95d45372e533ba352c512edd009853723e55bb7173a8eb0fe7568bc1bc
maturity: draft
page_id: pg_63366fc7864d5a4ead9b706093910d12
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8079d90abe065cc9a2bea3f717950767
title: obra/coderabbit-review-helper/README.md @ de5963701c37
updated_at: '2026-09-14T04:13:15Z'
---

# obra/coderabbit-review-helper/README.md @ de5963701c37

<!-- rcw:begin owner=source:src_8079d90abe065cc9a2bea3f717950767 block=evidence -->
- Users can place custom text in ~/.coderabbit-extractor to prepend a preamble to output; the bundled example preamble instructs the AI agent to critically evaluate the reviewer and its suggestions. [@claim:clm_3466017212161a35658797a5ac9315b5c9486621ecd027eff50a5d895d2f3864]
- The tool converts CodeRabbit GitHub PR reviews into clean, LLM-friendly text intended for AI-assisted code improvement workflows. [@claim:clm_3fd957df9f901be7306f6fa827c387f905b4691e3ec9cd56917019c3c8a6c988]
- Output groups feedback by file, sorts AI-actionable (robot-marked) items first within each file, and reports totals such as files with feedback and comment counts. [@claim:clm_475b4e74ab2d89b96f846561c2cd5e04b27e6078e7eb0ff152b193d476ea9031]
- The tool organizes three feedback categories: AI-actionable items with implementation prompts, nitpick comments with simple diffs, and outside-diff-range comments with broader context. [@claim:clm_4aea7d6fc977893c12a5b9ea77bca2020c020b14d1e72b957eb6ecafebb1f988]
- The --since-commit option (extracting reviews after a specific commit) is documented as 'coming soon', i.e. not yet available. [@claim:clm_588732bca7cd5a27c1da5c12b6be4da08970a198ec35fab3eddd87733ef1349d]
- The tool targets AI-assisted development workflows such as automated code improvement pipelines and converting review feedback into actionable prompts, and is MIT licensed. [@claim:clm_6904c9bc3951dcb7ee5c50aff53dc63e5d09abbcb38bddab0ca3b4a3a691bdf1]
- The CLI accepts a PR as a full GitHub URL or short owner/repo/123 format, and supports --all-reviews, --since-commit (listed as coming soon), --debug, and --help flags. [@claim:clm_ad550ff1ea1b7d8a9eae51253dc193f5d4401671561d8280a9fdcbcc53ca8377]
- The output prioritizes detailed AI prompts over diffs, never shows both prompt and diff for the same suggestion, and strips GitHub web-interface HTML artifacts. [@claim:clm_d30cf7656c08b6db7b696d1f60c166868b915388aa022838f60999f0f933dbf7]
- Requirements are an authenticated GitHub CLI (gh), Python 3.6+, and the beautifulsoup4 package; requirements.txt specifies beautifulsoup4>=4.9.0. [@claim:clm_dc91efe3e73677a97abb3b9ddaba079fddbecc060356f6444be13efb08c9da9b]
- By default the tool extracts only the latest review to avoid overwhelming output on PRs with many reviews; --all-reviews extracts every CodeRabbit review instead. [@claim:clm_ef043f95d45372e533ba352c512edd009853723e55bb7173a8eb0fe7568bc1bc]
<!-- rcw:end owner=source:src_8079d90abe065cc9a2bea3f717950767 block=evidence -->

## Researcher notes

