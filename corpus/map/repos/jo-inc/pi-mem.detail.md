# jo-inc/pi-mem -- full detail

[Back to orientation](pi-mem.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jo-inc/pi-mem/ffb706b8805d64e04919ceff4c82084a67504e5d/58a9a9ca9ca30992.json](../../../wiki/dossiers/jo-inc/pi-mem/ffb706b8805d64e04919ceff4c82084a67504e5d/58a9a9ca9ca30992.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] pi-mem is a memory package for the pi coding agent, installable via 'pi install git:github.com/jo-inc/pi-mem'. -- evidence: [README.md#L1-L15](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L1-L15), [README.md#L97-L99](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L97-L99) (`clm_111333e0ec5f4641838fcd7bdf3220a76191363e4640ae84c236f6fe940eb7b0`)
- [observation/documented] A dashboard widget shows an auto-generated 'Last 24h' summary at session start and switch, scanning recent session files for titles, costs, and sub-agent counts, grouping topics via an LLM call with a flat-list fallback, rebuilt every 15 minutes in the background, and also showing open scratchpad items. -- evidence: [README.md#L85-L89](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L85-L89) (`clm_62de6e6420ef19144425acf55d975c9a5d9c0019ff3d7fd9c1b74ad2d7a4215f`)

## design-choices (2 claim(s))

- [observation/documented] Notes files and older daily logs are deliberately not injected into context; they remain accessible on demand via memory_search and memory_read. -- evidence: [README.md#L52-L52](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L52-L52) (`clm_e2b150bff901d759eb53891ea1e31a7105affd6394c98af17ffcb1a9b02eba42`)
- [observation/documented] When PI_AUTOCOMMIT is 1 or true, the tool auto-commits memory changes to git after every write; it defaults to false. -- evidence: [README.md#L74-L81](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L74-L81) (`clm_6efb3d94c59d592d18e89f0f33ae4ff8382e062f7afbb69c9695155d8f124663`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] Exposes tools memory_write (long_term/daily/note targets with append and overwrite modes), memory_read (long_term, scratchpad, daily, note, file, list), memory_search, and a scratchpad checklist tool. -- evidence: [README.md#L36-L41](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L36-L41) (`clm_35cbb63a9e2dd4fa78dec510a42a690cd88eb139e0f87a0c57a4d2680307596e`)
- [observation/documented] memory_search performs case-insensitive keyword search over filenames and content across root, notes/, and daily/ directories. -- evidence: [README.md#L36-L41](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L36-L41) (`clm_f88027b7f1be01fe37654700cd607e314ad93535b2a4bf063b7c568c268a07f3`)
- [observation/documented] Configuration is via environment variables or a .pi-mem.json file in the memory directory, with environment variables taking precedence when both are set. -- evidence: [README.md#L56-L56](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L56-L56), [README.md#L72-L72](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L72-L72) (`clm_8307ac53e12a541524e3f2da5e7e18e92c209253b3fb6d0b946271e0c60d6fcb`)
- [observation/documented] Supported settings include searchDirs, contextFiles, and autocommit in .pi-mem.json, plus env vars PI_MEMORY_DIR, PI_DAILY_DIR, PI_CONTEXT_FILES, PI_SEARCH_DIRS, PI_AUTOCOMMIT, and PI_TIMEZONE. -- evidence: [README.md#L74-L81](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L74-L81), [README.md#L62-L68](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L62-L68) (`clm_b8e66a000b23991763ca64ecaa7bfb9653601054c36ec2ac57f0621d11cdf58c`)

## memory-state (2 claim(s))

- [observation/documented] Memory files live under ~/.pi/agent/memory/ by default, overridable via the PI_MEMORY_DIR environment variable. -- evidence: [README.md#L23-L23](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L23-L23), [README.md#L74-L81](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L74-L81) (`clm_d99197d77b03246bf9966e916cfebd819dd43c3167bdc2627ee31a99d60690de`)
- [observation/documented] The memory layout includes MEMORY.md (curated long-term memory), SCRATCHPAD.md (checklist), daily/YYYY-MM-DD.md append-only logs, and LLM-created notes/*.md files. -- evidence: [README.md#L25-L30](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L25-L30) (`clm_620008029b840c2f25863d3d1c3c672a238390191135ad0196dacae85337a154`)

## orchestration (1 claim(s))

- [observation/documented] Before every agent turn, the system prompt is automatically injected with PI_CONTEXT_FILES entries, MEMORY.md, open SCRATCHPAD.md items, and today's and yesterday's daily logs. -- evidence: [README.md#L47-L50](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L47-L50), [README.md#L45-L45](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L45-L45) (`clm_c9dd4d526b9ec87c46ba77d37fc07ddce5ae522cb5c9c998b58cd4efa1787123`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The project is MIT-licensed, published on npm as @askjo/pi-mem, and part of a pi ecosystem including pi-reflect, pi-boss, and pi-room. -- evidence: [README.md#L107-L113](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L107-L113), [README.md#L1-L15](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L1-L15), [README.md#L103-L103](https://github.com/jo-inc/pi-mem/blob/ffb706b8805d64e04919ceff4c82084a67504e5d/README.md#L103-L103) (`clm_eb47de5620060f9f1d740b292106a2816903214d62491807e6cd87520afffeec`)

