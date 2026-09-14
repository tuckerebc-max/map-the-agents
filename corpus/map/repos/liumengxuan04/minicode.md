# liumengxuan04/minicode

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 40413758cc12 @ 45c51cd2158f37a9

## Summary (orientation draft, not independently verified)

MiniCode is documented as a lightweight terminal coding assistant with a model-tool-model loop, a bounded read-only multi-agent MVP, session persistence backed by provider-reported usage, local skills and MCP tools, and review-before-write file edits. Its docs list several planned-but-not-built features and explicit MVP limitations.

## Source coverage

Source coverage (partial): 3 of 12 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The README describes MiniCode as a lightweight terminal coding assistant for local development, offering Claude Code-like workflow and architectural ideas in a much smaller implementation aimed at learning, experimentation, and custom tooling. -- evidence: [README.md#L26-L26](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/README.md#L26-L26), [README.md#L28-L28](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/README.md#L28-L28)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (1 claim(s)):
  - [observation/documented] Documentation lists planned-but-not-built items including full Ink/React rendering, bridge/IDE two-way communication, remote sessions, LSP support, and a skill marketplace, while noting a minimal sub-agent runtime and basic layered memory loading are already implemented. -- evidence: [ARCHITECTURE.md#L31-L40](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/ARCHITECTURE.md#L31-L40)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: Documented development commands are npm run check and npm test, alongside a stated goal of keeping the architecture understandable, hackable, and easy to extend. -- evidence: [README.md#L222-L222](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/README.md#L222-L222), [README.md#L217-L220](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/README.md#L217-L220)
- skills-patterns (1 claim(s)):
  - [observation/documented] Documented local skills are discovered through SKILL.md files, alongside MCP tools, resources, and prompts reachable over stdio or remote HTTP. -- evidence: [README.md#L125-L136](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/README.md#L125-L136)
- interfaces (1 claim(s)):
  - [observation/documented] Documented slash commands include /plan for an in-memory Todo list, /goal with pause/resume for a Goal that persists across turns, and /loop for a recurring prompt with a default ten-minute interval and a one-minute minimum. -- evidence: [README.md#L178-L190](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/README.md#L178-L190)
- memory-state (2 claim(s)):
  - [observation/documented] Documented runtime state keeps conversation messages in memory during a turn, appends them to a per-project session log after each successful turn, and treats fresh provider-reported usage as the source of truth for context accounting, with local token estimation only as a fallback or a tail estimate. -- evidence: [ARCHITECTURE.md#L72-L77](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/ARCHITECTURE.md#L72-L77)
  - [observation/documented] Documentation states very large tool outputs are moved out of the prompt context and stored on disk, leaving the model a preview and a path to the full output. -- evidence: [ARCHITECTURE.md#L72-L77](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/ARCHITECTURE.md#L72-L77)
- orchestration (2 claim(s)):
  - [observation/documented] Documented core capabilities include multi-step tool execution within a single turn, forming a model-to-tool-to-model loop. -- evidence: [README.md#L125-L136](https://github.com/LiuMengxuan04/MiniCode/blob/40413758cc12892528d31c85edbe53e97e25a88d/README.md#L125-L136)
More evidence: [full detail](minicode.detail.md)

Metadata and full claim list: [full detail](minicode.detail.md)
Human notes ([notes](minicode.notes.md), never overwritten by build)

[Back to map index](../../index.md)
