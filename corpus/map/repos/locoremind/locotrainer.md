# locoremind/locotrainer

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 08a2a06e2122 @ d3f570970b8c0cf2

## Summary (orientation draft, not independently verified)

LocoTrainer is a Python agent framework (pip-installable CLI) that pairs with the LocoTrainer-4B model — a Qwen3-4B-Instruct-2507 distilled via SFT from Qwen3-Coder-Next — to analyze MS-SWIFT codebases and emit markdown reports via a Claude Code-style tool-calling loop. Evidence is README-only documentation.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] LocoTrainer-4B is described as a 4B-parameter MS-SWIFT domain expert agent distilled from Qwen3-Coder-Next, combining tool-calling with framework knowledge. -- evidence: [README.md#L47-L47](https://github.com/LocoreMind/LocoTrainer/blob/08a2a06e212244925423fc08d26b605edd3dcfb4/README.md#L47-L47), [README.md#L17-L17](https://github.com/LocoreMind/LocoTrainer/blob/08a2a06e212244925423fc08d26b605edd3dcfb4/README.md#L17-L17)
  - [observation/documented] The model was trained with full-parameter SFT on 361,830 samples (agent trajectories, MS-SWIFT knowledge, project paths) at 32,768 max sequence length on 8x H100 80GB for about 25 hours. -- evidence: [README.md#L51-L60](https://github.com/LocoreMind/LocoTrainer/blob/08a2a06e212244925423fc08d26b605edd3dcfb4/README.md#L51-L60), [README.md#L277-L295](https://github.com/LocoreMind/LocoTrainer/blob/08a2a06e212244925423fc08d26b605edd3dcfb4/README.md#L277-L295)
- components (1 claim(s)):
  - [observation/documented] The framework comprises modules for prompts (SYSTEM_PROMPT, get_system_reminder), a ToolExecutor (Read/Grep/Glob/Write/Bash), an agent loop, config loading, ms-swift auto-clone logic, and a Click CLI. -- evidence: [README.md#L244-L257](https://github.com/LocoreMind/LocoTrainer/blob/08a2a06e212244925423fc08d26b605edd3dcfb4/README.md#L244-L257)
- design-choices (1 claim(s)):
  - [observation/documented] The framework simulates a Claude Code-style agent environment, matching what LocoTrainer-4B was trained on, and injects absolute paths into user content plus tolerant tool argument parsing for reliability. -- evidence: [README.md#L120-L122](https://github.com/LocoreMind/LocoTrainer/blob/08a2a06e212244925423fc08d26b605edd3dcfb4/README.md#L120-L122), [README.md#L102-L102](https://github.com/LocoreMind/LocoTrainer/blob/08a2a06e212244925423fc08d26b605edd3dcfb4/README.md#L102-L102)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The CLI exposes `locotrainer run` with options -q (question), -c (codebase path), -o (output dir), -m (model), --max-turns (default 20), and --quiet. -- evidence: [README.md#L232-L240](https://github.com/LocoreMind/LocoTrainer/blob/08a2a06e212244925423fc08d26b605edd3dcfb4/README.md#L232-L240)
  - [observation/documented] Configuration uses environment variables such as LOCOTRAINER_API_KEY, LOCOTRAINER_BASE_URL (default OpenAI endpoint), LOCOTRAINER_MODEL (default gpt-4o), LOCOTRAINER_MAX_TURNS, LOCOTRAINER_MAX_TOKENS, LOCOTRAINER_ENABLE_THINKING, LOCOTRAINER_CODEBASE, and LOCOTRAINER_OUTPUT_DIR. -- evidence: [README.md#L261-L270](https://github.com/LocoreMind/LocoTrainer/blob/08a2a06e212244925423fc08d26b605edd3dcfb4/README.md#L261-L270)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The agent loop sends tool calls (Read/Grep/Glob/Bash) against the real filesystem, feeds results back for the next turn, and writes a final markdown report plus a full trajectory JSON to the output directory. -- evidence: [README.md#L77-L100](https://github.com/LocoreMind/LocoTrainer/blob/08a2a06e212244925423fc08d26b605edd3dcfb4/README.md#L77-L100)
- tools-permissions (1 claim(s)):
  - [observation/documented] The agent emits structured tool-call JSON for Read, Grep, Glob, Bash, and Write tools executed against the target codebase. -- evidence: [README.md#L66-L71](https://github.com/LocoreMind/LocoTrainer/blob/08a2a06e212244925423fc08d26b605edd3dcfb4/README.md#L66-L71), [README.md#L77-L100](https://github.com/LocoreMind/LocoTrainer/blob/08a2a06e212244925423fc08d26b605edd3dcfb4/README.md#L77-L100)
- evaluation (1 claim(s)):
  - [observation/documented] Reported evaluation on MS-SWIFT analysis tasks across 3 iterations shows Read success rising from 0% (relative paths) to 100% (absolute paths), and Write success reaching 100% only with tolerant argument parsing, with the final test producing a 225-line report in 9 turns. -- evidence: [README.md#L106-L106](https://github.com/LocoreMind/LocoTrainer/blob/08a2a06e212244925423fc08d26b605edd3dcfb4/README.md#L106-L106), [README.md#L110-L116](https://github.com/LocoreMind/LocoTrainer/blob/08a2a06e212244925423fc08d26b605edd3dcfb4/README.md#L110-L116)
- dependencies (1 claim(s)):
More evidence: [full detail](locotrainer.detail.md)

Metadata and full claim list: [full detail](locotrainer.detail.md)
Human notes ([notes](locotrainer.notes.md), never overwritten by build)

[Back to map index](../../index.md)
