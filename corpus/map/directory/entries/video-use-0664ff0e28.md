# video-use (`video-use`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: browser-use
- License: MIT
- Language: Python
- Interface: platforms=IDE; install=pip
- Model providers: Claude Code, Codex, Hermes, Openclaw, any shell-access agent
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (skills-based; symlinks into agent skill directories) (yes)
  - claude_code_plugin: yes (via ~/.claude/skills/video-use) (yes)
  - subagents: yes (spawns parallel sub-agents for animations) (yes)
  - hooks: no (no)
  - plan_mode: yes (asks for strategy approval before executing) (yes)

Repository map entry: [browser-use/video-use](../../repos/browser-use/video-use.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Enables coding agents to edit raw video footage by reading word-level audio transcripts and on-demand visual composites instead of processing every frame, achieving precise word-boundary cuts with minimal token usage and a self-evaluation loop at every cut boundary.

(captured site page body (agents/video-use.md), not a verified repo-code finding)
Raw video has been beyond coding agents: minutes of footage mean tens of thousands of frames, orders of magnitude beyond any context window, so automated editing stayed outside the agent ecosystem. video-use, from the browser-use team ('browser-use, but for video'), makes footage legible by substituting representation for pixels: an ElevenLabs Scribe transcript with word-level timestamps and speaker diarization is packed into a small markdown file, and a timeline_view tool renders filmstrip and waveform composites only when the agent needs to inspect a moment. The agent plans an edit decision list over that text — filler-word removal, dead-space cuts, per-segment color grading, burned-in subtitles — and a rendering pipeline executes it with ffmpeg, self-evaluating output at every cut boundary and retrying up to three times; animation overlays run as parallel sub-agents. Creators and developers already working in Claude Code or Codex use it to batch-edit talking-head video from the terminal; it requires an ElevenLabs key and ffmpeg.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/video-use.md)
