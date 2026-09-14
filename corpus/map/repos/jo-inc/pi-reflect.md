# jo-inc/pi-reflect

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 33a72886c8d5 @ 48284f3d7486af39

## Summary (orientation draft, not independently verified)

pi-reflect is a pi coding-agent extension that iteratively improves markdown files (rules, memory, personality) by collecting evidence, sending it to an LLM, and applying safety-checked edits with git auto-commits. Evidence is documentation-only (README and an agent-facing setup guide); no source code slices are present.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] pi-reflect provides iterative self-improvement for pi coding agents: it reads recent conversations and reference material, compares actual behavior against a defined target, and edits the target file to close the gap. -- evidence: [README.md#L18-L18](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L18-L18), [README.md#L14-L14](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L14-L14), [README.md#L16-L16](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L16-L16)
- components (1 claim(s)):
  - [observation/documented] Each run collects evidence from transcripts, daily logs, and reference files, sends evidence plus the target file and a prompt to an LLM, then applies the LLM's proposed edits with safety checks. -- evidence: [README.md#L45-L48](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L45-L48)
- design-choices (2 claim(s)):
  - [observation/documented] Edit safety measures include backing up the original, skipping ambiguous matches, rejecting suspiciously large deletions, and auto-committing to git when the target is in a repository. -- evidence: [README.md#L45-L48](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L45-L48), [README.md#L50-L50](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L50-L50)
  - [observation/documented] Data sources support three types (files with glob patterns, shell commands capturing stdout, and HTTP URLs), all with {lookbackDays} interpolation and per-source maxBytes caps; file sources are date-pruned by filename. -- evidence: [README.md#L58-L62](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L58-L62), [README.md#L64-L64](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L64-L64)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors clone the repo, run npm install and npm test (137 tests), and can test locally with pi -e ./extensions/index.ts without installing. -- evidence: [README.md#L163-L167](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L163-L167)
  - [observation/documented] Repository development practice: SETUP.md is an instruction guide addressed to the coding agent for installing, locating a target file, running a first /reflect, and scheduling daily runs via launchd or cron. -- evidence: [SETUP.md#L60-L97](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/SETUP.md#L60-L97), [SETUP.md#L3-L3](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/SETUP.md#L3-L3), [SETUP.md#L115-L118](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/SETUP.md#L115-L118), [SETUP.md#L42-L42](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/SETUP.md#L42-L42)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The product exposes slash commands: /reflect (optionally with a file path), /reflect-config, /reflect-history, /reflect-stats, and /reflect-backfill. -- evidence: [README.md#L32-L39](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L32-L39)
  - [observation/documented] Configuration lives in ~/.pi/agent/reflect.json with a targets array; each target requires a path and model, and supports lookbackDays, maxSessionBytes, transcripts, transcriptSource, context, prompt, and backupDir fields. -- evidence: [README.md#L124-L135](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L124-L135), [README.md#L137-L147](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L137-L147), [README.md#L122-L122](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L122-L122)
- memory-state (1 claim(s)):
  - [observation/documented] Targets are any markdown file, e.g. AGENTS.md for behavioral rules, MEMORY.md for long-term memory, or SOUL.md for personality; the prompt determines whether reflect strengthens rules, extracts durable facts, or sharpens identity. -- evidence: [README.md#L20-L20](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L20-L20), [README.md#L94-L98](https://github.com/jo-inc/pi-reflect/blob/33a72886c8d5882b8b89a4a0ace1bb8d35403ef2/README.md#L94-L98)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
More evidence: [full detail](pi-reflect.detail.md)

Metadata and full claim list: [full detail](pi-reflect.detail.md)
Human notes ([notes](pi-reflect.notes.md), never overwritten by build)

[Back to map index](../../index.md)
