---
access: public
aliases: []
claim_ids:
- clm_22a5f068dd9d869c544ebf8abf4dab345d92ef90dc150b6e3a9a03dda7350c55
- clm_6be59e5437a83962e159b3e71ae1025d596b4947d261194c03d16ca8a7fc0faa
- clm_c66aa905b7d4da8c920a39493b50fa5c334f5a6b7afc3cb8ad623affb7a61016
- clm_d22a1356d705cadd61f4b1b0cd4653eb2706a23b2fe945b9c246b1df39e81eeb
maturity: draft
page_id: pg_8ed3f3144ad05fda9c004177c8ecefe9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7f9f1b45f5f15ce38184740e65c4d8e4
title: browser-use/video-use/install.md @ 9575612f066a
updated_at: '2026-09-14T03:39:36Z'
---

# browser-use/video-use/install.md @ 9575612f066a

<!-- rcw:begin owner=source:src_7f9f1b45f5f15ce38184740e65c4d8e4 block=evidence -->
- The repo is installed as an agent skill by symlinking the whole directory into the agent's skills folder (e.g. ~/.claude/skills/video-use), keeping SKILL.md and helpers/ as siblings. [@claim:clm_22a5f068dd9d869c544ebf8abf4dab345d92ef90dc150b6e3a9a03dda7350c55]
- The skill ships helper scripts including transcribe.py, transcribe_batch.py, pack_transcripts.py, timeline_view.py, render.py, and grade.py, invoked directly as python helpers/<name>.py. [@claim:clm_6be59e5437a83962e159b3e71ae1025d596b4947d261194c03d16ca8a7fc0faa]
- Repository development practice: install.md instructs the installing agent to verify with one real command (not file-existence checks), never run transcription during install verification because Scribe costs money, and never echo or commit the API key. [@claim:clm_c66aa905b7d4da8c920a39493b50fa5c334f5a6b7afc3cb8ad623affb7a61016]
- Python dependencies are requests, librosa, matplotlib, pillow, and numpy; ffmpeg and ffprobe are hard requirements, yt-dlp is optional, and an ElevenLabs API key is required for Scribe transcription. [@claim:clm_d22a1356d705cadd61f4b1b0cd4653eb2706a23b2fe945b9c246b1df39e81eeb]
<!-- rcw:end owner=source:src_7f9f1b45f5f15ce38184740e65c4d8e4 block=evidence -->

## Researcher notes

