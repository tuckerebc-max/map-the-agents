# gemini-cli-extensions/code-review -- full detail

[Back to orientation](code-review.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/gemini-cli-extensions/code-review/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/00fa2a8e0549be11.json](../../../wiki/dossiers/gemini-cli-extensions/code-review/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/00fa2a8e0549be11.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The extension is an open-source Gemini CLI extension authored by the creators of the Gemini Code Assist GitHub App. -- evidence: [README.md#L3-L3](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L3-L3), [README.md#L5-L5](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L5-L5) (`clm_8845cf22cecf8409c55853f0426f2a9c805416637aa972b741d89ff37493389d`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributions must be accompanied by a Contributor License Agreement, and all submissions, including from project members, go through GitHub pull-request review. -- evidence: [docs/contributing.md#L9-L13](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/docs/contributing.md#L9-L13), [docs/contributing.md#L30-L32](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/docs/contributing.md#L30-L32) (`clm_220aacc23277de4871c76f067c74fe711694be62568a816f88431b8f44dd79ef`)
- [observation/documented] Repository development practice: the project follows a Contributor Covenant-derived code of conduct with a Project Steward handling reported violations and an escalation path via opensource@google.com. -- evidence: [docs/code-of-conduct.md#L74-L80](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/docs/code-of-conduct.md#L74-L80), [docs/code-of-conduct.md#L93-L95](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/docs/code-of-conduct.md#L93-L95) (`clm_60c8208c38606fc61daac560edf7eb718b391333ad185984061f1acfd4b33cc7`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] The extension adds a /code-review command to Gemini CLI that analyzes code changes on the current branch for quality issues. -- evidence: [README.md#L22-L22](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L22-L22), [README.md#L3-L3](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L3-L3) (`clm_e81fb2b5c4e8fc0dd7a72d9903b0a953f44775db0780c8f5340afed36d390867`)
- [observation/documented] A /pr-code-review command analyzes code changes on a pull request, invoked either with a PR link argument or via configured environment variables. -- evidence: [README.md#L28-L31](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L28-L31), [README.md#L26-L26](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L26-L26) (`clm_1e48a32aacd15f41a3840738efc9ef3afe5322a3d760afe8c287a41105289063`)
- [observation/documented] Pull-request review can be configured through REPOSITORY, PULL_REQUEST_NUMBER, and ADDITIONAL_CONTEXT environment variables, with ADDITIONAL_CONTEXT supplying focus areas. -- evidence: [README.md#L28-L31](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L28-L31) (`clm_031dc6d7d06b95dad9d9ee75b6d55d9d243899b4889b86cddd08f5e190e54da6`)
- [observation/documented] The bundled GEMINI.md instructs the CLI agent to prefer /code-review when users request change reviews, and for PR review to check $REPOSITORY, $PULL_REQUEST_NUMBER, and $ADDITIONAL_CONTEXT, asking for clarification if missing or ambiguous. -- evidence: [GEMINI.md#L5-L5](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/GEMINI.md#L5-L5), [GEMINI.md#L9-L9](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/GEMINI.md#L9-L9), [GEMINI.md#L1-L1](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/GEMINI.md#L1-L1) (`clm_496444317e55db264bc44bb8c08df7b6958a2c55bba59d844439472fe7cdadcb`)
- [inference/documented] GEMINI.md names the pull-request command /pr-review while the README calls it /pr-code-review, suggesting a possible naming inconsistency between the two files. -- evidence: [README.md#L26-L26](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L26-L26), [GEMINI.md#L7-L7](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/GEMINI.md#L7-L7) (`clm_3108043ff185cbb892cf1948165b98cd3702bd758ac2df0f53c3b884ab849047`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Installation requires Gemini CLI version 0.4.0 or newer, installed via the gemini extensions install command pointing at the extension's GitHub repository. -- evidence: [README.md#L15-L16](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L15-L16), [README.md#L11-L13](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L11-L13), [README.md#L9-L9](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L9-L9) (`clm_779f4c7fa8c1e8282451db0abd15151bbe9d87c2d37fd342ecf48fb225dfab3b`)
- [observation/documented] Using the pull-request review feature requires enabling the GitHub MCP server in Gemini CLI. -- evidence: [README.md#L28-L31](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L28-L31) (`clm_e0fca234114faf5c2bf4a25abec56f0e5ef03dbd8ea421e186a2af3cf22826c9`)

## limitations (1 claim(s))

- [inference/documented] The extension appears to focus on reviewing code changes rather than generating them; documented functionality is limited to analysis of branch or pull-request diffs for quality issues. -- evidence: [README.md#L26-L26](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L26-L26), [README.md#L22-L22](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L22-L22), [README.md#L3-L3](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L3-L3) (`clm_6586c90dc20e00554ef4bb521d75735761b95c314d7c8f516d22088a0c6c60b3`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

