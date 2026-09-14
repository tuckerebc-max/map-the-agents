# potproject/code-agent

Status: distilled - Freshness: current
Catalog classes: multiplexer
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8b17068f090d @ c663c1a26b3610b0

## Summary (orientation draft, not independently verified)

The snapshot is a README describing potproject/code-agent, a GitHub Action that runs Claude Code or Codex from issue/PR comments via /claude and /codex commands and automates commits or pull requests. Evidence covers its commands, workflow setup, action inputs, and security behaviors; no contributor-facing development guidance or evaluation evidence is present.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] When the AI modifies code, the action automatically creates a Pull Request or commits the changes; if no changes result, it posts the AI output as a comment instead. -- evidence: [README.md#L7-L10](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L7-L10)
- design-choices (2 claim(s)):
  - [observation/documented] The recommended workflow listens on issue opened, issue_comment created, and pull_request_review_comment created events, and skips runs triggered by bot senders. -- evidence: [README.md#L39-L45](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L39-L45), [README.md#L47-L54](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L47-L54)
  - [observation/documented] Setup requires repository workflow permissions for read/write access and allowing GitHub Actions to create and approve pull requests. -- evidence: [README.md#L18-L19](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L18-L19)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The action is triggered by /claude or /codex commands posted in GitHub Issues or Pull Request comments, which start Claude Code or Codex respectively. -- evidence: [README.md#L3-L3](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L3-L3), [README.md#L7-L10](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L7-L10)
  - [observation/documented] The action exposes inputs including github-token (required), event-path, and a timeout for AI processing defaulting to 600 seconds. -- evidence: [README.md#L113-L117](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L113-L117)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] Before running core logic, the action checks that the triggering user has write or admin permission on the repository. -- evidence: [README.md#L154-L155](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L154-L155)
  - [observation/documented] Secrets such as the GitHub token, API keys, and AWS credentials are masked as *** in any output the action posts to GitHub. -- evidence: [README.md#L154-L155](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L154-L155)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The product depends on external AI CLIs, Claude Code by Anthropic and Codex by OpenAI, which it invokes on behalf of the user. -- evidence: [README.md#L3-L3](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L3-L3)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
  - [inference/documented] The tool appears aimed at automating code changes directly from GitHub conversations, with an example repository linked for issues and pull requests. -- evidence: [README.md#L3-L3](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L3-L3), [README.md#L79-L79](https://github.com/potproject/code-agent/blob/8b17068f090ddc32ccb05956e08f9ca9f740fdab/README.md#L79-L79)

(3 additional claim(s) omitted for length; see [full detail](code-agent.detail.md) for every claim.)

Metadata and full claim list: [full detail](code-agent.detail.md)
Human notes ([notes](code-agent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
