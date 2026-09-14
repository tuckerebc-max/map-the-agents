# browser-use/video-use

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 9575612f066a @ 0e448881ca040508

## Summary (orientation draft, not independently verified)

video-use is an open-source skill that lets an LLM agent (Claude Code, Codex, etc.) edit raw video footage conversationally via ffmpeg/PIL helper scripts, transcript-driven cut planning, and a self-eval render loop. Evidence covers its helper tooling, EDL interface, memory file, sub-agent orchestration, dependencies, and agent-facing install workflow. Evidence coverage: 137 of 141 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The skill ships helper scripts including transcribe.py, transcribe_batch.py, pack_transcripts.py, timeline_view.py, render.py, and grade.py, invoked directly as python helpers/<name>.py. -- evidence: [install.md#L49-L49](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/install.md#L49-L49), [SKILL.md#L74-L79](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L74-L79)
- design-choices (3 claim(s)):
  - [observation/documented] The LLM never watches the video; it reasons from a packed word-level transcript plus on-demand visual composites (filmstrip + waveform PNGs) generated only at decision points. -- evidence: [README.md#L73-L73](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/README.md#L73-L73), [README.md#L87-L87](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/README.md#L87-L87), [README.md#L79-L79](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/README.md#L79-L79)
  - [observation/documented] Editing is audio-first: cut candidates come from word boundaries and silence gaps, cuts never fall inside a word, edges are padded 30-200ms to absorb Scribe timestamp drift, and 30ms audio fades prevent pops. -- evidence: [SKILL.md#L104-L110](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L104-L110), [SKILL.md#L22-L33](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L22-L33)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: install.md instructs the installing agent to verify with one real command (not file-existence checks), never run transcription during install verification because Scribe costs money, and never echo or commit the API key. -- evidence: [install.md#L26-L29](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/install.md#L26-L29), [install.md#L116-L116](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/install.md#L116-L116), [install.md#L137-L137](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/install.md#L137-L137)
- skills-patterns (1 claim(s)):
  - [observation/documented] The repo is installed as an agent skill by symlinking the whole directory into the agent's skills folder (e.g. ~/.claude/skills/video-use), keeping SKILL.md and helpers/ as siblings. -- evidence: [README.md#L56-L57](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/README.md#L56-L57), [install.md#L72-L72](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/install.md#L72-L72), [install.md#L76-L79](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/install.md#L76-L79)
- interfaces (2 claim(s)):
  - [observation/documented] Cut decisions are expressed as an edl.json file with sources, time ranges with beat/quote/reason, a grade (preset name or raw ffmpeg filter), overlay clips, optional subtitles, and total duration. -- evidence: [SKILL.md#L289-L289](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L289-L289), [SKILL.md#L270-L287](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L270-L287)
  - [observation/documented] render.py defaults output scale to 1080p from any source and supports a --preview 720p fast mode; grade.py offers presets like warm_cinematic and neutral_punch plus a --filter flag for arbitrary ffmpeg chains. -- evidence: [SKILL.md#L170-L172](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L170-L172), [SKILL.md#L74-L79](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L74-L79), [SKILL.md#L266-L266](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L266-L266)
- memory-state (1 claim(s)):
  - [observation/documented] Session memory persists in <videos_dir>/edit/project.md, appended each session so later sessions resume prior context; transcripts are also cached per source and never re-transcribed unless the file changed. -- evidence: [SKILL.md#L293-L293](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L293-L293), [README.md#L15-L21](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/README.md#L15-L21), [SKILL.md#L22-L33](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L22-L33)
- orchestration (1 claim(s)):
More evidence: [full detail](video-use.detail.md)

Metadata and full claim list: [full detail](video-use.detail.md)
Human notes ([notes](video-use.notes.md), never overwritten by build)

[Back to map index](../../index.md)
