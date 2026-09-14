# timwuhaotian/the-pair

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 8d678875f777 @ 26b6dc489930ec38

## Summary (orientation draft, not independently verified)

The Pair is an open-source (Apache 2.0) Tauri 2 desktop app for macOS/Windows/Linux that runs two AI coding agents — a read-only Mentor and an Executor — which cross-check each other's work, with multi-provider CLI support and local orchestration. Evidence is almost entirely README/llms.txt documentation; no source code slices are present. Evidence coverage: 141 of 380 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 21 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The Pair is a free, open-source desktop app running two AI coding agents: a read-only Mentor that plans and reviews, and an Executor that writes code and runs commands, cross-checking each other's work. -- evidence: [README.md#L53-L53](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L53-L53), [llms.txt#L3-L3](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/llms.txt#L3-L3)
- components (1 claim(s)):
  - [observation/documented] The documented Rust backend includes PairManager (lifecycle), MessageBroker (state machine), ProcessSpawner (multi-provider), ContextBridge, QualityGate, SmartPause, Git Tracker, Worktrees, Session Snapshot, Resource Monitoring, Acceptance, and Report Generator modules. -- evidence: [README.md#L266-L301](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L266-L301)
- design-choices (1 claim(s)):
  - [observation/documented] Design principles emphasize trust through transparency (visible agent activity, resource usage, git changes), status-driven color coding (blue mentoring, purple executing, amber paused, green finished), and refined glassmorphism aesthetics. -- evidence: [.impeccable.md#L22-L26](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/.impeccable.md#L22-L26), [.impeccable.md#L15-L15](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/.impeccable.md#L15-L15)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the README's Development section documents npm scripts for building and testing, including npm test for JS and Rust unit tests, typecheck, lint, e2e, and platform-specific build commands. -- evidence: [README.md#L373-L394](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L373-L394), [README.md#L343-L348](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L343-L348), [README.md#L171-L176](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L171-L176)
- skills-patterns (1 claim(s)):
  - [observation/documented] The Japanese README documents a skill system that lets users attach project-specific skill files to guide agent behavior. -- evidence: [README.ja.md#L80-L91](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.ja.md#L80-L91)
- interfaces (2 claim(s)):
  - [observation/documented] The product is model-agnostic: it can pair provider CLIs including opencode, Claude Code, OpenAI Codex, Gemini CLI, and Kimi Code in any combination, plus local models via Ollama. -- evidence: [README.md#L53-L53](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L53-L53), [README.md#L422-L422](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L422-L422), [llms.txt#L17-L22](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/llms.txt#L17-L22)
  - [observation/documented] Besides the desktop app, a terminal CLI edition called Pair Code is available on npm (installable globally via npm install -g pair-code), sharing the same Mentor + Executor design. -- evidence: [README.md#L117-L120](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L117-L120), [README.md#L115-L115](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L115-L115), [README.md#L122-L122](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L122-L122)
- memory-state (1 claim(s)):
  - [observation/documented] Session snapshots are saved automatically; on relaunch the app detects interrupted sessions and offers to restore them with full conversation history and turn state. -- evidence: [llms.txt#L26-L31](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/llms.txt#L26-L31), [README.md#L446-L446](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L446-L446), [README.md#L89-L101](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L89-L101)
- orchestration (2 claim(s)):
  - [observation/documented] The agent workflow loops through Mentoring, Executing, and Reviewing stages, and runs are capped at a flat 20-iteration default, pausing for human review when the budget is reached. -- evidence: [README.md#L442-L442](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L442-L442), [README.md#L319-L319](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L319-L319), [README.md#L305-L317](https://github.com/timwuhaotian/the-pair/blob/8d678875f777fb838ed944daf376d5220e39bd59/README.md#L305-L317)
More evidence: [full detail](the-pair.detail.md)

Metadata and full claim list: [full detail](the-pair.detail.md)
Human notes ([notes](the-pair.notes.md), never overwritten by build)

[Back to map index](../../index.md)
