---
access: public
aliases: []
claim_ids:
- clm_111333e0ec5f4641838fcd7bdf3220a76191363e4640ae84c236f6fe940eb7b0
- clm_35cbb63a9e2dd4fa78dec510a42a690cd88eb139e0f87a0c57a4d2680307596e
- clm_620008029b840c2f25863d3d1c3c672a238390191135ad0196dacae85337a154
- clm_62de6e6420ef19144425acf55d975c9a5d9c0019ff3d7fd9c1b74ad2d7a4215f
- clm_6efb3d94c59d592d18e89f0f33ae4ff8382e062f7afbb69c9695155d8f124663
- clm_8307ac53e12a541524e3f2da5e7e18e92c209253b3fb6d0b946271e0c60d6fcb
- clm_b8e66a000b23991763ca64ecaa7bfb9653601054c36ec2ac57f0621d11cdf58c
- clm_c9dd4d526b9ec87c46ba77d37fc07ddce5ae522cb5c9c998b58cd4efa1787123
- clm_d99197d77b03246bf9966e916cfebd819dd43c3167bdc2627ee31a99d60690de
- clm_e2b150bff901d759eb53891ea1e31a7105affd6394c98af17ffcb1a9b02eba42
- clm_eb47de5620060f9f1d740b292106a2816903214d62491807e6cd87520afffeec
- clm_f88027b7f1be01fe37654700cd607e314ad93535b2a4bf063b7c568c268a07f3
maturity: draft
page_id: pg_2873ae34b7b2577db9454eeacc216ba0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e9a9ea742c28567390a52a64ee936617
title: jo-inc/pi-mem/README.md @ ffb706b8805d
updated_at: '2026-09-14T04:01:13Z'
---

# jo-inc/pi-mem/README.md @ ffb706b8805d

<!-- rcw:begin owner=source:src_e9a9ea742c28567390a52a64ee936617 block=evidence -->
- pi-mem is a memory package for the pi coding agent, installable via 'pi install git:github.com/jo-inc/pi-mem'. [@claim:clm_111333e0ec5f4641838fcd7bdf3220a76191363e4640ae84c236f6fe940eb7b0]
- Exposes tools memory_write (long_term/daily/note targets with append and overwrite modes), memory_read (long_term, scratchpad, daily, note, file, list), memory_search, and a scratchpad checklist tool. [@claim:clm_35cbb63a9e2dd4fa78dec510a42a690cd88eb139e0f87a0c57a4d2680307596e]
- The memory layout includes MEMORY.md (curated long-term memory), SCRATCHPAD.md (checklist), daily/YYYY-MM-DD.md append-only logs, and LLM-created notes/*.md files. [@claim:clm_620008029b840c2f25863d3d1c3c672a238390191135ad0196dacae85337a154]
- A dashboard widget shows an auto-generated 'Last 24h' summary at session start and switch, scanning recent session files for titles, costs, and sub-agent counts, grouping topics via an LLM call with a flat-list fallback, rebuilt every 15 minutes in the background, and also showing open scratchpad items. [@claim:clm_62de6e6420ef19144425acf55d975c9a5d9c0019ff3d7fd9c1b74ad2d7a4215f]
- When PI_AUTOCOMMIT is 1 or true, the tool auto-commits memory changes to git after every write; it defaults to false. [@claim:clm_6efb3d94c59d592d18e89f0f33ae4ff8382e062f7afbb69c9695155d8f124663]
- Configuration is via environment variables or a .pi-mem.json file in the memory directory, with environment variables taking precedence when both are set. [@claim:clm_8307ac53e12a541524e3f2da5e7e18e92c209253b3fb6d0b946271e0c60d6fcb]
- Supported settings include searchDirs, contextFiles, and autocommit in .pi-mem.json, plus env vars PI_MEMORY_DIR, PI_DAILY_DIR, PI_CONTEXT_FILES, PI_SEARCH_DIRS, PI_AUTOCOMMIT, and PI_TIMEZONE. [@claim:clm_b8e66a000b23991763ca64ecaa7bfb9653601054c36ec2ac57f0621d11cdf58c]
- Before every agent turn, the system prompt is automatically injected with PI_CONTEXT_FILES entries, MEMORY.md, open SCRATCHPAD.md items, and today's and yesterday's daily logs. [@claim:clm_c9dd4d526b9ec87c46ba77d37fc07ddce5ae522cb5c9c998b58cd4efa1787123]
- Memory files live under ~/.pi/agent/memory/ by default, overridable via the PI_MEMORY_DIR environment variable. [@claim:clm_d99197d77b03246bf9966e916cfebd819dd43c3167bdc2627ee31a99d60690de]
- Notes files and older daily logs are deliberately not injected into context; they remain accessible on demand via memory_search and memory_read. [@claim:clm_e2b150bff901d759eb53891ea1e31a7105affd6394c98af17ffcb1a9b02eba42]
- The project is MIT-licensed, published on npm as @askjo/pi-mem, and part of a pi ecosystem including pi-reflect, pi-boss, and pi-room. [@claim:clm_eb47de5620060f9f1d740b292106a2816903214d62491807e6cd87520afffeec]
- memory_search performs case-insensitive keyword search over filenames and content across root, notes/, and daily/ directories. [@claim:clm_f88027b7f1be01fe37654700cd607e314ad93535b2a4bf063b7c568c268a07f3]
<!-- rcw:end owner=source:src_e9a9ea742c28567390a52a64ee936617 block=evidence -->

## Researcher notes

