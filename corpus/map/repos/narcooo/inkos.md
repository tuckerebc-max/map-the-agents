# narcooo/inkos

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 091048383f41 @ 856156b1ba1f1007

## Summary (orientation draft, not independently verified)

InkOS is a story-creation and translation AI agent system distributed as the npm package @actalk/inkos, built on a pi-agent harness with Studio/TUI/CLI interfaces, specialized agents, standard SKILL.md skills, layered memory, and documented LLM configuration paths. Evidence coverage: 164 of 331 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 6 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 21 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

21 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] InkOS is distributed as the npm package @actalk/inkos, requires Node.js 22 or higher, and is licensed under AGPL-3.0. -- evidence: [README.md#L101-L101](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L101-L101), [README.md#L8-L14](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L8-L14), [README.md#L685-L685](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L685-L685)
- components (2 claim(s)):
  - [observation/documented] The long-form pipeline uses specialized agents: Radar, Planner, Composer, Architect, Writer, Observer, Reflector, Normalizer, Auditor, and Reviser, each with documented responsibilities. -- evidence: [README.md#L437-L448](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L437-L448)
  - [observation/documented] Version 1.8.0 ships 15 built-in professional skills (long-form writing/review, shorts, Play, scripts, storyboards, interactive film, translation, import, covers, de-AI-flavor, etc.), each with its own SKILL.md. -- evidence: [README.md#L58-L67](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L58-L67), [CHANGELOG.en.md#L13-L16](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/CHANGELOG.en.md#L13-L16)
- design-choices (4 claim(s)):
  - [observation/documented] Chapter production follows plan → compose → write → audit → revise → state sync; context is organized into protected/compressible layers, and runtime artifacts (intent.md, context.json, rule-stack.yaml, trace.json) are compiled per chapter. -- evidence: [README.md#L381-L381](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L381-L381), [README.md#L479-L484](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L479-L484), [README.md#L430-L430](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L430-L430), [README.md#L76-L76](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L76-L76)
  - [observation/documented] Prose, state, hooks, and run snapshots are validated in a chapter workspace and atomically committed together, so failures do not leave state advanced without persisted text. -- evidence: [CHANGELOG.en.md#L20-L23](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/CHANGELOG.en.md#L20-L23), [README.md#L58-L67](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L58-L67)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors use pnpm install, pnpm dev, pnpm test, and pnpm typecheck, and are invited to open issues or PRs. -- evidence: [README.md#L637-L637](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L637-L637), [README.md#L639-L644](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L639-L644)
- skills-patterns (2 claim(s)):
  - [observation/documented] InkOS consumes standard SKILL.md packages directly; skills provide instructions and static references only, add no execution permissions, and can be forced per turn with @skill-id or auto-selected by the chat agent via use_skill. -- evidence: [README.md#L129-L129](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L129-L129), [README.md#L133-L137](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L133-L137)
  - [observation/documented] Skills can be placed in skills/, .agents/skills/, user directories like ~/.agents/skills/, or pointed to via the INKOS_SKILL_DIRS environment variable; Studio can import full skill folders. -- evidence: [README.md#L133-L137](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L133-L137)
- interfaces (4 claim(s)):
  - [observation/documented] The product supports Studio (web workbench), TUI, and CLI interaction forms, all sharing one execution surface for creation tasks. -- evidence: [README.md#L27-L27](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L27-L27), [README.md#L278-L278](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L278-L278)
  - [observation/documented] CLI commands include book create, write next, plan chapter, compose chapter, draft, audit, revise, and export with an EPUB format option; all commands support --json structured output. -- evidence: [README.md#L572-L615](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L572-L615), [README.md#L618-L618](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L618-L618), [README.md#L288-L296](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L288-L296), [README.md#L525-L525](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L525-L525), [README.md#L517-L523](https://github.com/Narcooo/inkos/blob/091048383f411eb99948a8764f42b6fd13006f9b/README.md#L517-L523)
- memory-state (2 claim(s)):
More evidence: [full detail](inkos.detail.md)

Metadata and full claim list: [full detail](inkos.detail.md)
Human notes ([notes](inkos.notes.md), never overwritten by build)

[Back to map index](../../index.md)
