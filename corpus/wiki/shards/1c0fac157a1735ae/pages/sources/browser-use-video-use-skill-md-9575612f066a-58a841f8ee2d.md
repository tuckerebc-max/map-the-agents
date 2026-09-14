---
access: public
aliases: []
claim_ids:
- clm_0ba71e2ab07599a4fa64fd07e0d4c724e389e1c76816e1eb50d2a6635d0ea495
- clm_6be59e5437a83962e159b3e71ae1025d596b4947d261194c03d16ca8a7fc0faa
- clm_6eb5c1dd6d80fb2bab2dc640cbb7a53749d9b2a77f9e5e96942ee515bb8633e1
- clm_7cd86aae3491204cb697df5141dde3bc09c770f16910c9b4793d3135185860d5
- clm_ba0a88598ad55009d14b96d84a4b5ec10476baef8d4f42511f0f36f15496f17e
- clm_dee29301d8f550c6800b6b7815755548b67f9fcaa7aa57ced1d9453ae70c5e1e
- clm_fe8af2e6db8e6f20015286cd4219d99912f120c7efe4b3378bdb57421b8bc562
- clm_ff1f1174c991c2b9f10f9261d8b51d1ac9350c843f6c099ee6e079d9341f69d7
maturity: draft
page_id: pg_51f4db0dfc9e596e89aa58a841f8ee2d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_011f6104b74950aba1746daa5ce48413
title: browser-use/video-use/SKILL.md @ 9575612f066a
updated_at: '2026-09-14T03:39:36Z'
---

# browser-use/video-use/SKILL.md @ 9575612f066a

<!-- rcw:begin owner=source:src_011f6104b74950aba1746daa5ce48413 block=evidence -->
- The skill separates non-negotiable production-correctness hard rules (e.g. subtitles applied last in the filter chain) from artistic choices, which are treated as worked examples the agent may deviate from. [@claim:clm_0ba71e2ab07599a4fa64fd07e0d4c724e389e1c76816e1eb50d2a6635d0ea495]
- The skill ships helper scripts including transcribe.py, transcribe_batch.py, pack_transcripts.py, timeline_view.py, render.py, and grade.py, invoked directly as python helpers/<name>.py. [@claim:clm_6be59e5437a83962e159b3e71ae1025d596b4947d261194c03d16ca8a7fc0faa]
- Multiple animations are built by parallel sub-agents spawned via the Agent tool, one sub-agent per animation slot with a self-contained prompt and unique output filenames. [@claim:clm_6eb5c1dd6d80fb2bab2dc640cbb7a53749d9b2a77f9e5e96942ee515bb8633e1]
- Session memory persists in <videos_dir>/edit/project.md, appended each session so later sessions resume prior context; transcripts are also cached per source and never re-transcribed unless the file changed. [@claim:clm_7cd86aae3491204cb697df5141dde3bc09c770f16910c9b4793d3135185860d5]
- Cut decisions are expressed as an edl.json file with sources, time ranges with beat/quote/reason, a grade (preset name or raw ffmpeg filter), overlay clips, optional subtitles, and total duration. [@claim:clm_ba0a88598ad55009d14b96d84a4b5ec10476baef8d4f42511f0f36f15496f17e]
- render.py defaults output scale to 1080p from any source and supports a --preview 720p fast mode; grade.py offers presets like warm_cinematic and neutral_punch plus a --filter flag for arbitrary ffmpeg chains. [@claim:clm_dee29301d8f550c6800b6b7815755548b67f9fcaa7aa57ced1d9453ae70c5e1e]
- Editing is audio-first: cut candidates come from word boundaries and silence gaps, cuts never fall inside a word, edges are padded 30-200ms to absorb Scribe timestamp drift, and 30ms audio fades prevent pops. [@claim:clm_fe8af2e6db8e6f20015286cd4219d99912f120c7efe4b3378bdb57421b8bc562]
- A self-eval loop runs timeline_view on the rendered output at every cut boundary to catch visual jumps, audio pops, and hidden subtitles, capped at 3 fix-and-re-render passes before flagging issues to the user. [@claim:clm_ff1f1174c991c2b9f10f9261d8b51d1ac9350c843f6c099ee6e079d9341f69d7]
<!-- rcw:end owner=source:src_011f6104b74950aba1746daa5ce48413 block=evidence -->

## Researcher notes

