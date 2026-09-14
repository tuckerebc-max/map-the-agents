# vibra-code (`vibra-code`)

[Back to directory index](../index.md)

Directory membership: published+backing+pages.

- Category: agent
- Provider/maker: sa4hnd
- License: AGPL-3.0
- Language: TypeScript
- Interface: install=git clone --recurse-submodules, npm install (backend); macOS/Xcode/CocoaPods for mobile app
- Model providers: Claude,Cursor,Gemini
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [sa4hnd/vibra-code](../../repos/sa4hnd/vibra-code.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): First open-source AI mobile app builder (open-source alternative to Lovable/Bolt.new/Rork); describes app in plain English and generates code in E2B cloud sandbox with real-time native preview on phone; customizable AI prompts and provider swapping; entire project (backend + 60fps native iOS chat UI via Texture/IGListKit) built by a single 19-year-old using Claude Code.

(captured site page body (agents/vibra-code.md), not a verified repo-code finding)
Vibra Code exists to open mobile app creation to people who describe rather than program, as an open-source counterpart to closed builders like Lovable, Bolt.new, and Rork that anyone can self-host and modify. A user describes an app in plain English (or voice/image input) on their phone; a Next.js/Convex backend spawns an E2B cloud sandbox where a coding agent — Claude Code by default, Cursor or Gemini selectable via environment variable — writes the application, Inngest orchestrates the work, and Convex streams every change back to a native 60fps iOS chat interface built on Texture and IGListKit, with live preview through a tunnel URL and optional GitHub push of the finished project. Indie developers and hobbyists who want an open, self-hostable mobile app builder use it; it is AGPL-3.0 licensed, early-stage (7 commits), and was built end-to-end by a single developer working with Claude Code.
Sources: [published index (sha256:ae063493534e)](https://alltheagents.org/agents.json); [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/vibra-code.md)
