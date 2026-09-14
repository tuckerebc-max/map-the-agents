---
access: public
aliases: []
claim_ids:
- clm_1cf926f717c38d13c7ee6546b33f5d5267566ee407b242d65b8523cd21a26243
- clm_22a5f068dd9d869c544ebf8abf4dab345d92ef90dc150b6e3a9a03dda7350c55
- clm_7cd86aae3491204cb697df5141dde3bc09c770f16910c9b4793d3135185860d5
- clm_ff1f1174c991c2b9f10f9261d8b51d1ac9350c843f6c099ee6e079d9341f69d7
maturity: draft
page_id: pg_a0eaf4606a345cf59d482034260fe6e2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_05639d90f96a53e3acb37e27cd0394a3
title: browser-use/video-use/README.md @ 9575612f066a
updated_at: '2026-09-14T03:39:36Z'
---

# browser-use/video-use/README.md @ 9575612f066a

<!-- rcw:begin owner=source:src_05639d90f96a53e3acb37e27cd0394a3 block=evidence -->
- The LLM never watches the video; it reasons from a packed word-level transcript plus on-demand visual composites (filmstrip + waveform PNGs) generated only at decision points. [@claim:clm_1cf926f717c38d13c7ee6546b33f5d5267566ee407b242d65b8523cd21a26243]
- The repo is installed as an agent skill by symlinking the whole directory into the agent's skills folder (e.g. ~/.claude/skills/video-use), keeping SKILL.md and helpers/ as siblings. [@claim:clm_22a5f068dd9d869c544ebf8abf4dab345d92ef90dc150b6e3a9a03dda7350c55]
- Session memory persists in <videos_dir>/edit/project.md, appended each session so later sessions resume prior context; transcripts are also cached per source and never re-transcribed unless the file changed. [@claim:clm_7cd86aae3491204cb697df5141dde3bc09c770f16910c9b4793d3135185860d5]
- A self-eval loop runs timeline_view on the rendered output at every cut boundary to catch visual jumps, audio pops, and hidden subtitles, capped at 3 fix-and-re-render passes before flagging issues to the user. [@claim:clm_ff1f1174c991c2b9f10f9261d8b51d1ac9350c843f6c099ee6e079d9341f69d7]
<!-- rcw:end owner=source:src_05639d90f96a53e3acb37e27cd0394a3 block=evidence -->

## Researcher notes

