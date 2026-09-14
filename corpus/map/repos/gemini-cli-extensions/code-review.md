# gemini-cli-extensions/code-review

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit dd1a10d2c9d0 @ 00fa2a8e0549be11

## Summary (orientation draft, not independently verified)

The repository provides a Gemini CLI extension that adds code-review commands analyzing branch or pull-request changes for quality issues; evidence is mostly README documentation plus contributor/community docs.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The extension is an open-source Gemini CLI extension authored by the creators of the Gemini Code Assist GitHub App. -- evidence: [README.md#L3-L3](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L3-L3), [README.md#L5-L5](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L5-L5)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributions must be accompanied by a Contributor License Agreement, and all submissions, including from project members, go through GitHub pull-request review. -- evidence: [docs/contributing.md#L9-L13](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/docs/contributing.md#L9-L13), [docs/contributing.md#L30-L32](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/docs/contributing.md#L30-L32)
  - [observation/documented] Repository development practice: the project follows a Contributor Covenant-derived code of conduct with a Project Steward handling reported violations and an escalation path via opensource@google.com. -- evidence: [docs/code-of-conduct.md#L74-L80](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/docs/code-of-conduct.md#L74-L80), [docs/code-of-conduct.md#L93-L95](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/docs/code-of-conduct.md#L93-L95)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The extension adds a /code-review command to Gemini CLI that analyzes code changes on the current branch for quality issues. -- evidence: [README.md#L22-L22](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L22-L22), [README.md#L3-L3](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L3-L3)
  - [observation/documented] A /pr-code-review command analyzes code changes on a pull request, invoked either with a PR link argument or via configured environment variables. -- evidence: [README.md#L28-L31](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L28-L31), [README.md#L26-L26](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L26-L26)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] Installation requires Gemini CLI version 0.4.0 or newer, installed via the gemini extensions install command pointing at the extension's GitHub repository. -- evidence: [README.md#L15-L16](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L15-L16), [README.md#L11-L13](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L11-L13), [README.md#L9-L9](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L9-L9)
  - [observation/documented] Using the pull-request review feature requires enabling the GitHub MCP server in Gemini CLI. -- evidence: [README.md#L28-L31](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L28-L31)
- limitations (1 claim(s)):
  - [inference/documented] The extension appears to focus on reviewing code changes rather than generating them; documented functionality is limited to analysis of branch or pull-request diffs for quality issues. -- evidence: [README.md#L26-L26](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L26-L26), [README.md#L22-L22](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L22-L22), [README.md#L3-L3](https://github.com/gemini-cli-extensions/code-review/blob/dd1a10d2c9d07b2ebade866590fdfa59cd8f9d04/README.md#L3-L3)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](code-review.detail.md) for every claim.)

Metadata and full claim list: [full detail](code-review.detail.md)
Human notes ([notes](code-review.notes.md), never overwritten by build)

[Back to map index](../../index.md)
