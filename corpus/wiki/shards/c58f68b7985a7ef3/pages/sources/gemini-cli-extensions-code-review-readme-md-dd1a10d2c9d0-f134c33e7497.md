---
access: public
aliases: []
claim_ids:
- clm_031dc6d7d06b95dad9d9ee75b6d55d9d243899b4889b86cddd08f5e190e54da6
- clm_1e48a32aacd15f41a3840738efc9ef3afe5322a3d760afe8c287a41105289063
- clm_3108043ff185cbb892cf1948165b98cd3702bd758ac2df0f53c3b884ab849047
- clm_6586c90dc20e00554ef4bb521d75735761b95c314d7c8f516d22088a0c6c60b3
- clm_779f4c7fa8c1e8282451db0abd15151bbe9d87c2d37fd342ecf48fb225dfab3b
- clm_8845cf22cecf8409c55853f0426f2a9c805416637aa972b741d89ff37493389d
- clm_e0fca234114faf5c2bf4a25abec56f0e5ef03dbd8ea421e186a2af3cf22826c9
- clm_e81fb2b5c4e8fc0dd7a72d9903b0a953f44775db0780c8f5340afed36d390867
maturity: draft
page_id: pg_55404c1324375af19a03f134c33e7497
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_ab14adc57c1c5e4cb7527b5a4009eead
title: gemini-cli-extensions/code-review/README.md @ dd1a10d2c9d0
updated_at: '2026-09-14T03:52:39Z'
---

# gemini-cli-extensions/code-review/README.md @ dd1a10d2c9d0

<!-- rcw:begin owner=source:src_ab14adc57c1c5e4cb7527b5a4009eead block=evidence -->
- Pull-request review can be configured through REPOSITORY, PULL_REQUEST_NUMBER, and ADDITIONAL_CONTEXT environment variables, with ADDITIONAL_CONTEXT supplying focus areas. [@claim:clm_031dc6d7d06b95dad9d9ee75b6d55d9d243899b4889b86cddd08f5e190e54da6]
- A /pr-code-review command analyzes code changes on a pull request, invoked either with a PR link argument or via configured environment variables. [@claim:clm_1e48a32aacd15f41a3840738efc9ef3afe5322a3d760afe8c287a41105289063]
- GEMINI.md names the pull-request command /pr-review while the README calls it /pr-code-review, suggesting a possible naming inconsistency between the two files. [@claim:clm_3108043ff185cbb892cf1948165b98cd3702bd758ac2df0f53c3b884ab849047]
- The extension appears to focus on reviewing code changes rather than generating them; documented functionality is limited to analysis of branch or pull-request diffs for quality issues. [@claim:clm_6586c90dc20e00554ef4bb521d75735761b95c314d7c8f516d22088a0c6c60b3]
- Installation requires Gemini CLI version 0.4.0 or newer, installed via the gemini extensions install command pointing at the extension's GitHub repository. [@claim:clm_779f4c7fa8c1e8282451db0abd15151bbe9d87c2d37fd342ecf48fb225dfab3b]
- The extension is an open-source Gemini CLI extension authored by the creators of the Gemini Code Assist GitHub App. [@claim:clm_8845cf22cecf8409c55853f0426f2a9c805416637aa972b741d89ff37493389d]
- Using the pull-request review feature requires enabling the GitHub MCP server in Gemini CLI. [@claim:clm_e0fca234114faf5c2bf4a25abec56f0e5ef03dbd8ea421e186a2af3cf22826c9]
- The extension adds a /code-review command to Gemini CLI that analyzes code changes on the current branch for quality issues. [@claim:clm_e81fb2b5c4e8fc0dd7a72d9903b0a953f44775db0780c8f5340afed36d390867]
<!-- rcw:end owner=source:src_ab14adc57c1c5e4cb7527b5a4009eead block=evidence -->

## Researcher notes

