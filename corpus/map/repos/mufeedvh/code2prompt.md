# mufeedvh/code2prompt

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 66585136062c @ 44061f456b2f99ce

## Summary (orientation draft, not independently verified)

With --json, the tool outputs a JSON object containing prompt, directory_name, token_count, model_info, and files fields. The project ships an MCP server (code2prompt-mcp) that exposes codebase context generation to LLM applications like Claude Desktop, Cursor, Roo Code, and Cline, configured via an mcpServers JSON entry.

## Source coverage

Source coverage (complete): 4 of 4 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The ecosystem comprises a Rust core library for file traversal, gitignore handling, and Git metadata; a CLI/TUI; a Python SDK with bindings to the Rust core published on PyPI; and an MCP server. -- evidence: [README.md#L109-L111](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L109-L111)
- design-choices (3 claim(s)):
  - [observation/documented] Prompt generation respects .gitignore rules, supports glob-based include/exclude filtering, and uses Handlebars templates that users can customize. -- evidence: [README.md#L121-L128](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L121-L128), [README_ES.md#L28-L37](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README_ES.md#L28-L37), [README_ES.md#L98-L98](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README_ES.md#L98-L98)
  - [observation/documented] Token counts are estimated via parallel per-file counts plus estimated template overhead; the full rendered prompt is not re-tokenized and the JSON envelope is excluded from the estimate. -- evidence: [README.md#L121-L128](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L121-L128)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: AGENTS.md instructs contributors to follow existing patterns, place reusable logic in code2prompt-core, keep Python bindings thin, include regression tests for bug fixes, and map changed paths to verification skills (verify-core, verify-cli, verify-python, verify-website). -- evidence: [AGENTS.md#L9-L19](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/AGENTS.md#L9-L19), [AGENTS.md#L23-L28](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/AGENTS.md#L23-L28)
  - [observation/documented] Repository development practice: root cargo test does not exercise the Python bindings, and contributors should not claim completion until the relevant verification skill passes. -- evidence: [AGENTS.md#L30-L31](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/AGENTS.md#L30-L31), [AGENTS.md#L9-L19](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/AGENTS.md#L9-L19)
- skills-patterns (2 claim(s)):
  - [observation/documented] An installable agent skill (skills/code2prompt/SKILL.md) teaches coding agents to use code2prompt for repository navigation and scoped context gathering, installable via the Skills CLI (npx skills add mufeedvh/code2prompt). -- evidence: [README.md#L85-L87](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L85-L87), [README.md#L82-L83](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L82-L83), [README.md#L89-L93](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L89-L93)
  - [observation/documented] The skill installer adds only the skill folder and its template, possibly cloning the repository temporarily; the rest of the repository is not installed. -- evidence: [README.md#L95-L97](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README.md#L95-L97)
- interfaces (2 claim(s)):
  - [observation/documented] With --json, the tool outputs a JSON object containing prompt, directory_name, token_count, model_info, and files fields. -- evidence: [README_ES.md#L144-L144](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README_ES.md#L144-L144), [README_ES.md#L152-L160](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/README_ES.md#L152-L160)
  - [observation/documented] The project ships an MCP server (code2prompt-mcp) that exposes codebase context generation to LLM applications like Claude Desktop, Cursor, Roo Code, and Cline, configured via an mcpServers JSON entry. -- evidence: [llms-install.md#L52-L65](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/llms-install.md#L52-L65), [llms-install.md#L3-L3](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/llms-install.md#L3-L3), [llms-install.md#L7-L7](https://github.com/mufeedvh/code2prompt/blob/66585136062c04275ddd5a01c5518a4d78c4aa76/llms-install.md#L7-L7)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](code2prompt.detail.md)

Metadata and full claim list: [full detail](code2prompt.detail.md)
Human notes ([notes](code2prompt.notes.md), never overwritten by build)

[Back to map index](../../index.md)
