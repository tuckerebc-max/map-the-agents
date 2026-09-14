# intellegix/intellegix-code-agent-toolkit

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 852325000c29 @ 120c3f08bfd79547

## Summary (orientation draft, not independently verified)

The repository is a modular configuration toolkit for Claude Code CLI comprising an automated loop driver, orchestrator slash commands, Perplexity-based council/research automation, an MCP browser bridge, and portfolio governance; contributor and security policies are documented separately.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 24 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

24 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The toolkit ships an automated loop driver (loop_driver.py with NDJSON parser, state tracker, research bridge, and log redactor), agent definitions, hooks, slash commands, council automation, and an MCP browser bridge. -- evidence: [README.md#L23-L113](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L23-L113), [README.md#L8-L8](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L8-L8)
  - [observation/documented] The /frontend-e2e command runs browser-based end-to-end tests in seven tiers covering rendering, accessibility, visual/UX, navigation, responsive breakpoints, interactivity, and performance, producing pass/fail reports with failure screenshots. -- evidence: [README.md#L388-L388](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L388-L388), [README.md#L376-L376](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L376-L376), [README.md#L378-L386](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L378-L386)
- design-choices (6 claim(s)):
  - [observation/documented] The loop driver includes model-aware scaling (Opus gets 2x timeout and a 25-turn cap), Opus-to-Sonnet fallback after two consecutive timeouts, exponential backoff, stagnation detection, and per-iteration plus cumulative budget enforcement. -- evidence: [README.md#L249-L255](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L249-L255), [README.md#L640-L656](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L640-L656)
  - [observation/documented] The loop never edits CLAUDE.md itself; the human operator revises it between runs as the project's source of truth, retaining editorial control. -- evidence: [README.md#L298-L298](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L298-L298), [README.md#L296-L296](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L296-L296)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: contributors must open an issue first, fork and branch, keep PRs small and one-concern, run pytest automated-loop/tests/ -v with all tests passing, add tests for new features, and avoid new dependencies without prior discussion. -- evidence: [CONTRIBUTING.md#L7-L10](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/CONTRIBUTING.md#L7-L10), [CONTRIBUTING.md#L14-L17](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/CONTRIBUTING.md#L14-L17)
  - [observation/documented] Repository development practice: Python code style requires type hints on all functions, async/await for I/O, Pydantic for validation, and no dynamic code execution or unsanitized shell input. -- evidence: [CONTRIBUTING.md#L29-L31](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/CONTRIBUTING.md#L29-L31)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (5 claim(s)):
  - [observation/documented] The loop driver invokes Claude Code CLI with stream-json output and --resume for session continuity, parsing NDJSON events (init, assistant, result, system) to extract cost, turns, and completion markers. -- evidence: [README.md#L269-L269](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L269-L269), [README.md#L265-L267](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L265-L267)
  - [observation/documented] The loop driver exposes CLI flags including --project, --max-iterations, --max-cost, --dry-run, --smoke-test, --model, --timeout, and --verbose. -- evidence: [README.md#L238-L238](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L238-L238), [README.md#L235-L235](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L235-L235), [README.md#L241-L241](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L241-L241), [README.md#L183-L184](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L183-L184), [README.md#L177-L177](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L177-L177), [README.md#L180-L180](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L180-L180)
- memory-state (1 claim(s)):
  - [observation/documented] The loop persists state under <project>/.workflow/: state.json with cycle history, append-only trace.jsonl events, metrics_summary.json on exit, and research_result.md. -- evidence: [README.md#L273-L273](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L273-L273), [README.md#L275-L280](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L275-L280)
- orchestration (2 claim(s)):
  - [observation/documented] Three orchestrator commands cover greenfield bootstrapping, single-loop execution, and multi-agent parallel work via git worktrees; all enforce role separation so the orchestrator writes instructions without touching source code. -- evidence: [README.md#L325-L329](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L325-L329), [README.md#L323-L323](https://github.com/intellegix/intellegix-code-agent-toolkit/blob/852325000c29124dd8662d442f5207bed9da18b1/README.md#L323-L323)
More evidence: [full detail](intellegix-code-agent-toolkit.detail.md)

Metadata and full claim list: [full detail](intellegix-code-agent-toolkit.detail.md)
Human notes ([notes](intellegix-code-agent-toolkit.notes.md), never overwritten by build)

[Back to map index](../../index.md)
