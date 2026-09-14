# jo-inc/pi-mem

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit ffb706b8805d @ 58a9a9ca9ca30992

## Summary (orientation draft, not independently verified)

pi-mem is a memory extension for the pi coding agent, providing file-based memory under ~/.pi/agent/memory with tools for reading/writing/searching memory, automatic context injection, configuration via env vars or .pi-mem.json, and a dashboard widget. Evidence is README-only.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] pi-mem is a memory package for the pi coding agent, installable via 'pi install git:github.com/jo-inc/pi-mem'. -- evidence: [README.md#L1-L15](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L1-L15), [README.md#L97-L99](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L97-L99)
  - [observation/documented] A dashboard widget shows an auto-generated 'Last 24h' summary at session start and switch, scanning recent session files for titles, costs, and sub-agent counts, grouping topics via an LLM call with a flat-list fallback, rebuilt every 15 minutes in the background, and also showing open scratchpad items. -- evidence: [README.md#L85-L89](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L85-L89)
- design-choices (2 claim(s)):
  - [observation/documented] Notes files and older daily logs are deliberately not injected into context; they remain accessible on demand via memory_search and memory_read. -- evidence: [README.md#L52-L52](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L52-L52)
  - [observation/documented] When PI_AUTOCOMMIT is 1 or true, the tool auto-commits memory changes to git after every write; it defaults to false. -- evidence: [README.md#L74-L81](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L74-L81)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] Exposes tools memory_write (long_term/daily/note targets with append and overwrite modes), memory_read (long_term, scratchpad, daily, note, file, list), memory_search, and a scratchpad checklist tool. -- evidence: [README.md#L36-L41](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L36-L41)
  - [observation/documented] memory_search performs case-insensitive keyword search over filenames and content across root, notes/, and daily/ directories. -- evidence: [README.md#L36-L41](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L36-L41)
- memory-state (2 claim(s)):
  - [observation/documented] Memory files live under ~/.pi/agent/memory/ by default, overridable via the PI_MEMORY_DIR environment variable. -- evidence: [README.md#L23-L23](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L23-L23), [README.md#L74-L81](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L74-L81)
  - [observation/documented] The memory layout includes MEMORY.md (curated long-term memory), SCRATCHPAD.md (checklist), daily/YYYY-MM-DD.md append-only logs, and LLM-created notes/*.md files. -- evidence: [README.md#L25-L30](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L25-L30)
- orchestration (1 claim(s)):
  - [observation/documented] Before every agent turn, the system prompt is automatically injected with PI_CONTEXT_FILES entries, MEMORY.md, open SCRATCHPAD.md items, and today's and yesterday's daily logs. -- evidence: [README.md#L47-L50](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L47-L50), [README.md#L45-L45](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L45-L45)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
  - [observation/documented] The project is MIT-licensed, published on npm as @askjo/pi-mem, and part of a pi ecosystem including pi-reflect, pi-boss, and pi-room. -- evidence: [README.md#L107-L113](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L107-L113), [README.md#L1-L15](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L1-L15), [README.md#L103-L103](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L103-L103)
More evidence: [full detail](pi-mem.detail.md)

Metadata and full claim list: [full detail](pi-mem.detail.md)
Human notes ([notes](pi-mem.notes.md), never overwritten by build)

[Back to map index](../../index.md)
