---
access: public
aliases: []
claim_ids:
- clm_2a131aa5ca522dc99601d54d6a811461b6c9497152a456bdeada6cbcdf4018c0
- clm_6157dcd8aa7837420527ecf6abe3255d81d8ade69b6438cef458dca2553578f5
- clm_7113bde0f45b0da92bbb4996fd1f6dbab00a8bb93db8c3aed13e2e5f26bd835f
- clm_85e23c8e780bebe07c64698b34364a98dd16ff6259c98d519d335c97b2e64bf6
- clm_a6811946eda9ac369ac397b5883cacc6cfaaa6cf2c204704cda8ef51fd81ae30
- clm_ad41e2d9e7e91d51623c3539bec180871338261fee67b92bd0280621cb5c1f93
- clm_cd49d6f3f5ff4ea1ea8c43a96af2cc9d4596ccc1b141ad622b664bccef1825fd
- clm_e11b39d8b2fbcd856ced9908a2d0d741b702180dd5852ed46954256e297b99e0
maturity: draft
page_id: pg_1789f27bf37e5d5885055944e86193ed
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_94422215930c52ccbbbbe48e8ae68797
title: agent-of-empires/agent-of-empires/docs/api.md @ bdf21c256673
updated_at: '2026-09-14T03:30:42Z'
---

# agent-of-empires/agent-of-empires/docs/api.md @ bdf21c256673

<!-- rcw:begin owner=source:src_94422215930c52ccbbbbe48e8ae68797 block=evidence -->
- Skill sync propagates managed skills into agents' own directories with a never-overwrite rule: hand-edited copies are reported as conflicts and left untouched unless explicitly named in a `replace` list; automatic syncs never replace anything. [@claim:clm_2a131aa5ca522dc99601d54d6a811461b6c9497152a456bdeada6cbcdf4018c0]
- POST /api/sessions supports callback_url (fired on Waiting/Idle/Error transitions with loopback/private address rejection and fire-and-forget delivery) and idempotency_key so retries return the existing session instead of duplicating it. [@claim:clm_6157dcd8aa7837420527ecf6abe3255d81d8ade69b6438cef458dca2553578f5]
- `aoe serve` exposes an HTTP API so external orchestrators such as other agents, MCP tools, or CI scripts can drive sessions without attaching to a terminal; the web dashboard uses the same API plus internal routes. [@claim:clm_7113bde0f45b0da92bbb4996fd1f6dbab00a8bb93db8c3aed13e2e5f26bd835f]
- All HTTP endpoints require a token unless the server starts with --no-auth; the token is printed by `aoe serve` and accepted via bearer header, query parameter, or cookie. A --read-only mode blocks write endpoints with 403. [@claim:clm_85e23c8e780bebe07c64698b34364a98dd16ff6259c98d519d335c97b2e64bf6]
- Session status values are PascalCase on the wire (Starting, Running, Waiting, Idle, Error, Stopped, Unknown, Deleting, Creating), differing from the lowercase form used by the CLI and status-hook env vars. [@claim:clm_a6811946eda9ac369ac397b5883cacc6cfaaa6cf2c204704cda8ef51fd81ae30]
- GET /api/sessions/{id}/output returns a tmux pane snapshot with configurable trailing-line count (clamped 1..=2000) and text or ansi format, and works under read-only mode. [@claim:clm_ad41e2d9e7e91d51623c3539bec180871338261fee67b92bd0280621cb5c1f93]
- The send and output endpoints together form a documented primitive for driving an AoE session as a controlled subagent: send a prompt, poll output until stable or status returns to Idle, then capture the reply. [@claim:clm_cd49d6f3f5ff4ea1ea8c43a96af2cc9d4596ccc1b141ad622b664bccef1825fd]
- AoE discovers Agent Skills packages from a managed store and user-level agent directories (e.g. ~/.claude/skills, ~/.agents/skills, ~/.gemini/skills); a skill is a directory with a SKILL.md containing name and description frontmatter. [@claim:clm_e11b39d8b2fbcd856ced9908a2d0d741b702180dd5852ed46954256e297b99e0]
<!-- rcw:end owner=source:src_94422215930c52ccbbbbe48e8ae68797 block=evidence -->

## Researcher notes

