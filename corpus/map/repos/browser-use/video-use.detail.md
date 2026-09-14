# browser-use/video-use -- full detail

[Back to orientation](video-use.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/browser-use/video-use/9575612f066aa517354790a645fd90f9f95a743b/0e448881ca040508.json](../../../wiki/dossiers/browser-use/video-use/9575612f066aa517354790a645fd90f9f95a743b/0e448881ca040508.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The skill ships helper scripts including transcribe.py, transcribe_batch.py, pack_transcripts.py, timeline_view.py, render.py, and grade.py, invoked directly as python helpers/<name>.py. -- evidence: [install.md#L49-L49](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/install.md#L49-L49), [SKILL.md#L74-L79](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L74-L79) (`clm_6be59e5437a83962e159b3e71ae1025d596b4947d261194c03d16ca8a7fc0faa`)

## design-choices (3 claim(s))

- [observation/documented] The LLM never watches the video; it reasons from a packed word-level transcript plus on-demand visual composites (filmstrip + waveform PNGs) generated only at decision points. -- evidence: [README.md#L73-L73](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/README.md#L73-L73), [README.md#L87-L87](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/README.md#L87-L87), [README.md#L79-L79](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/README.md#L79-L79) (`clm_1cf926f717c38d13c7ee6546b33f5d5267566ee407b242d65b8523cd21a26243`)
- [observation/documented] Editing is audio-first: cut candidates come from word boundaries and silence gaps, cuts never fall inside a word, edges are padded 30-200ms to absorb Scribe timestamp drift, and 30ms audio fades prevent pops. -- evidence: [SKILL.md#L104-L110](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L104-L110), [SKILL.md#L22-L33](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L22-L33) (`clm_fe8af2e6db8e6f20015286cd4219d99912f120c7efe4b3378bdb57421b8bc562`)
- [observation/documented] The skill separates non-negotiable production-correctness hard rules (e.g. subtitles applied last in the filter chain) from artistic choices, which are treated as worked examples the agent may deviate from. -- evidence: [SKILL.md#L20-L20](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L20-L20), [SKILL.md#L35-L35](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L35-L35), [SKILL.md#L22-L33](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L22-L33) (`clm_0ba71e2ab07599a4fa64fd07e0d4c724e389e1c76816e1eb50d2a6635d0ea495`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: install.md instructs the installing agent to verify with one real command (not file-existence checks), never run transcription during install verification because Scribe costs money, and never echo or commit the API key. -- evidence: [install.md#L26-L29](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/install.md#L26-L29), [install.md#L116-L116](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/install.md#L116-L116), [install.md#L137-L137](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/install.md#L137-L137) (`clm_c66aa905b7d4da8c920a39493b50fa5c334f5a6b7afc3cb8ad623affb7a61016`)

## skills-patterns (1 claim(s))

- [observation/documented] The repo is installed as an agent skill by symlinking the whole directory into the agent's skills folder (e.g. ~/.claude/skills/video-use), keeping SKILL.md and helpers/ as siblings. -- evidence: [README.md#L56-L57](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/README.md#L56-L57), [install.md#L72-L72](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/install.md#L72-L72), [install.md#L76-L79](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/install.md#L76-L79) (`clm_22a5f068dd9d869c544ebf8abf4dab345d92ef90dc150b6e3a9a03dda7350c55`)

## interfaces (2 claim(s))

- [observation/documented] Cut decisions are expressed as an edl.json file with sources, time ranges with beat/quote/reason, a grade (preset name or raw ffmpeg filter), overlay clips, optional subtitles, and total duration. -- evidence: [SKILL.md#L289-L289](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L289-L289), [SKILL.md#L270-L287](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L270-L287) (`clm_ba0a88598ad55009d14b96d84a4b5ec10476baef8d4f42511f0f36f15496f17e`)
- [observation/documented] render.py defaults output scale to 1080p from any source and supports a --preview 720p fast mode; grade.py offers presets like warm_cinematic and neutral_punch plus a --filter flag for arbitrary ffmpeg chains. -- evidence: [SKILL.md#L170-L172](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L170-L172), [SKILL.md#L74-L79](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L74-L79), [SKILL.md#L266-L266](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L266-L266) (`clm_dee29301d8f550c6800b6b7815755548b67f9fcaa7aa57ced1d9453ae70c5e1e`)

## memory-state (1 claim(s))

- [observation/documented] Session memory persists in <videos_dir>/edit/project.md, appended each session so later sessions resume prior context; transcripts are also cached per source and never re-transcribed unless the file changed. -- evidence: [SKILL.md#L293-L293](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L293-L293), [README.md#L15-L21](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/README.md#L15-L21), [SKILL.md#L22-L33](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L22-L33) (`clm_7cd86aae3491204cb697df5141dde3bc09c770f16910c9b4793d3135185860d5`)

## orchestration (1 claim(s))

- [observation/documented] Multiple animations are built by parallel sub-agents spawned via the Agent tool, one sub-agent per animation slot with a self-contained prompt and unique output filenames. -- evidence: [SKILL.md#L22-L33](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L22-L33), [SKILL.md#L262-L262](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L262-L262), [SKILL.md#L249-L249](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L249-L249) (`clm_6eb5c1dd6d80fb2bab2dc640cbb7a53749d9b2a77f9e5e96942ee515bb8633e1`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] A self-eval loop runs timeline_view on the rendered output at every cut boundary to catch visual jumps, audio pops, and hidden subtitles, capped at 3 fix-and-re-render passes before flagging issues to the user. -- evidence: [SKILL.md#L99-L100](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/SKILL.md#L99-L100), [README.md#L96-L100](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/README.md#L96-L100), [README.md#L102-L102](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/README.md#L102-L102) (`clm_ff1f1174c991c2b9f10f9261d8b51d1ac9350c843f6c099ee6e079d9341f69d7`)

## dependencies (1 claim(s))

- [observation/documented] Python dependencies are requests, librosa, matplotlib, pillow, and numpy; ffmpeg and ffprobe are hard requirements, yt-dlp is optional, and an ElevenLabs API key is required for Scribe transcription. -- evidence: [install.md#L53-L53](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/install.md#L53-L53), [install.md#L49-L49](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/install.md#L49-L49), [install.md#L94-L94](https://github.com/browser-use/video-use/blob/9575612f066aa517354790a645fd90f9f95a743b/install.md#L94-L94) (`clm_d22a1356d705cadd61f4b1b0cd4653eb2706a23b2fe945b9c246b1df39e81eeb`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

