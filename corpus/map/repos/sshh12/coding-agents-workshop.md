# sshh12/coding-agents-workshop

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f89984463925 @ 7cd8717963f377d9

## Summary (orientation draft, not independently verified)

The repository contains workshop materials for 'Optimizing Codebases for Agents': two versions of an ML Experiment Tracker demo app, an AI-readiness scorecard, and agent race narration notes with headless race scripts. Evidence covers the demo apps' documented structure, the race evaluation harness, and the scorecard dimensions.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The repo contains README.md, scorecard.md, race.md, slides.html with embedded speaker notes, and demo directories A/ (deliberate anti-patterns) and B/ (agent-optimized). -- evidence: [README.md#L62-L70](https://github.com/sshh12/coding-agents-workshop/blob/f89984463925cfc238740aa540c209613291b0ae/README.md#L62-L70)
  - [observation/documented] Both A/ and B/ implement the same ML Experiment Tracker with experiment tracking, run logging with metrics, run comparison charts, and a dashboard. -- evidence: [README.md#L88-L88](https://github.com/sshh12/coding-agents-workshop/blob/f89984463925cfc238740aa540c209613291b0ae/README.md#L88-L88), [README.md#L90-L93](https://github.com/sshh12/coding-agents-workshop/blob/f89984463925cfc238740aa540c209613291b0ae/README.md#L90-L93)
- design-choices (1 claim(s)):
  - [observation/documented] The two demo versions differ in code organization, not functionality: Version A is a realistic mess while Version B is optimized for coding agents. -- evidence: [README.md#L95-L95](https://github.com/sshh12/coding-agents-workshop/blob/f89984463925cfc238740aa540c209613291b0ae/README.md#L95-L95)
- workflows (6 claim(s)):
  - [observation/documented] The repo holds materials for the 'Optimizing Codebases for Agents' workshop: a demo app in before/after versions, an AI-readiness scorecard, and agent race narrator notes. -- evidence: [README.md#L19-L19](https://github.com/sshh12/coding-agents-workshop/blob/f89984463925cfc238740aa540c209613291b0ae/README.md#L19-L19)
  - [observation/documented] Prerequisites include a laptop with a dev environment, an authenticated AI coding tool (Claude Code, Gemini CLI, Codex CLI, or Cursor), Python 3.10+, and a repo to audit. -- evidence: [README.md#L23-L26](https://github.com/sshh12/coding-agents-workshop/blob/f89984463925cfc238740aa540c209613291b0ae/README.md#L23-L26)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces: unknown (no source-linked claim submitted for this facet)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (2 claim(s)):
  - [observation/documented] The race demo measures agent performance by giving identical prompts to two agents on the two codebases, comparing files changed, test integrity, timing, and tool usage. -- evidence: [race.md#L46-L49](https://github.com/sshh12/coding-agents-workshop/blob/f89984463925cfc238740aa540c209613291b0ae/race.md#L46-L49), [race.md#L273-L281](https://github.com/sshh12/coding-agents-workshop/blob/f89984463925cfc238740aa540c209613291b0ae/race.md#L273-L281), [race.md#L187-L196](https://github.com/sshh12/coding-agents-workshop/blob/f89984463925cfc238740aa540c209613291b0ae/race.md#L187-L196)
  - [observation/documented] Headless scripts automate the race: race.sh launches claude -p in both dirs with stream-json output, race-reset.sh resets git state and deletes SQLite files, and race-analyze.sh parses timing, tool usage, tokens, and test results. -- evidence: [race.md#L267-L269](https://github.com/sshh12/coding-agents-workshop/blob/f89984463925cfc238740aa540c209613291b0ae/race.md#L267-L269)
- dependencies (1 claim(s)):
  - [observation/documented] The race narrative notes Pydantic 2.9.0 is listed in Version A's requirements but never imported, and alembic and redis are installed but unconfigured. -- evidence: [race.md#L76-L85](https://github.com/sshh12/coding-agents-workshop/blob/f89984463925cfc238740aa540c209613291b0ae/race.md#L76-L85)
- limitations (1 claim(s)):
  - [observation/documented] The race demo has a documented fallback if the live demo fails: play a pre-recorded side-by-side video or walk through the codebases manually. -- evidence: [race.md#L219-L224](https://github.com/sshh12/coding-agents-workshop/blob/f89984463925cfc238740aa540c209613291b0ae/race.md#L219-L224), [race.md#L217-L217](https://github.com/sshh12/coding-agents-workshop/blob/f89984463925cfc238740aa540c209613291b0ae/race.md#L217-L217)
More evidence: [full detail](coding-agents-workshop.detail.md)

Metadata and full claim list: [full detail](coding-agents-workshop.detail.md)
Human notes ([notes](coding-agents-workshop.notes.md), never overwritten by build)

[Back to map index](../../index.md)
