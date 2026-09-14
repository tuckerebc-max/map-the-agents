# guanyang/open-agent-hub

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c90c4f2b25ba @ 18ff33ab1ed1652b

## Summary (orientation draft, not independently verified)

Selected evidence records: The `oah` CLI provides list, status, enable, disable, and sync commands, with filters (--skills/--agents/--commands), --global, --target, and --path options. The --target option supports claude, antigravity, gemini, codex, cursor, trae, opencode, kiro, and all, defaulting to claude.

## Source coverage

Source coverage (partial): 6 of 13 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Five expert agent prompts are provided: architect (Orchestrator), reviewer and tester (Evaluators), refactorer and debugger (Optimizers). -- evidence: [docs/Agent_Guidelines.md#L11-L25](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/docs/Agent_Guidelines.md#L11-L25)
- design-choices (2 claim(s)):
  - [observation/documented] Activation works by dynamically symlinking Skills, Agents, and Commands into subdirectories (skills/, agents/, commands/) of each assistant's project or global config directory. -- evidence: [README.md#L85-L85](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L85-L85), [README.md#L62-L63](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L62-L63), [README.md#L49-L49](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L49-L49)
  - [observation/documented] Components use standardized Markdown prompts with YAML frontmatter metadata, which host agents parse to decide when to trigger and load skills. -- evidence: [docs/Skill_Guidelines.md#L22-L22](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/docs/Skill_Guidelines.md#L22-L22), [docs/Skill_Guidelines.md#L24-L29](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/docs/Skill_Guidelines.md#L24-L29), [README.md#L49-L49](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L49-L49)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: GEMINI.md provides project-level LLM coding behavioral guidelines (think before coding, simplicity first, surgical changes, goal-driven execution) derived from andrej-karpathy-skills, and CONTRIBUTING.md covers contribution guidelines. -- evidence: [GEMINI.md#L54-L56](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/GEMINI.md#L54-L56), [GEMINI.md#L13-L16](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/GEMINI.md#L13-L16), [GEMINI.md#L22-L26](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/GEMINI.md#L22-L26), [GEMINI.md#L36-L39](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/GEMINI.md#L36-L39), [README.md#L169-L170](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L169-L170), [GEMINI.md#L3-L3](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/GEMINI.md#L3-L3), [README.md#L11-L33](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L11-L33)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The `oah` CLI provides list, status, enable, disable, and sync commands, with filters (--skills/--agents/--commands), --global, --target, and --path options. -- evidence: [README.md#L113-L113](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L113-L113), [README.md#L107-L107](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L107-L107), [README.md#L134-L135](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L134-L135), [README.md#L104-L104](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L104-L104), [README.md#L138-L148](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L138-L148), [README.md#L110-L110](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L110-L110)
  - [observation/documented] The --target option supports claude, antigravity, gemini, codex, cursor, trae, opencode, kiro, and all, defaulting to claude. -- evidence: [README.md#L138-L148](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L138-L148)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Agent prompts support three collaboration patterns: handoff contracts with expected input/structured output, evaluator-optimizer loops with strict exit conditions, and XML compaction blocks for context pruning. -- evidence: [docs/Agent_Guidelines.md#L34-L34](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/docs/Agent_Guidelines.md#L34-L34), [docs/Agent_Guidelines.md#L41-L41](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/docs/Agent_Guidelines.md#L41-L41), [docs/Agent_Guidelines.md#L37-L38](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/docs/Agent_Guidelines.md#L37-L38)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The tool is described as a lightweight, zero-dependency CLI for managing and activating AI coding assistant capabilities. -- evidence: [README.md#L5-L5](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L5-L5)
  - [observation/documented] Skills can alternatively be installed via Vercel's `skills` CLI (npx skills@latest add guanyang/open-agent-hub) without cloning the repository. -- evidence: [README.md#L80-L81](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L80-L81), [README.md#L69-L69](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L69-L69), [README.md#L77-L77](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L77-L77), [README.md#L73-L73](https://github.com/guanyang/open-agent-hub/blob/c90c4f2b25baea05248025dd0442358709c5cc25/README.md#L73-L73)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(1 additional claim(s) omitted for length; see [full detail](open-agent-hub.detail.md) for every claim.)

Metadata and full claim list: [full detail](open-agent-hub.detail.md)
Human notes ([notes](open-agent-hub.notes.md), never overwritten by build)

[Back to map index](../../index.md)
