---
access: public
aliases: []
claim_ids:
- clm_09003e45565102f98d3168c4bb3fe7f22f9a0d48b0aee2646e48fc301ba631ef
- clm_0e5763ee6372f991b1537f41f90b736a539a313d970833937dd88a6370b319b8
- clm_0f495dbf894e1c3a06937302fa937b83c64e8813de20f0cd16694b5e9aa86f95
- clm_3cb4573ad335aabe827764be1312b3881737bf8dda63fab96975e80008b5514b
- clm_4358309eff6d658bbc338075d2a66c0963d352053e411dd02b0d54a4b8a7799e
- clm_44277a6e0b722de587bb276fb95dff6a87c08632da073940cc992a9045fd806e
- clm_66942730338b47cba0334580b256f77caf3dc4e8f745e67075825e069cc49d99
- clm_884722d1299b559920bc9207466615de89915d8bf62a82f4f9d3f1d7cf139093
- clm_948fe740e11c0833a4b8d13853e7743fb370f3b502fa9fdf45e31ae2cc3c83a7
- clm_a7d0a0341cadb84f57656a38bf5d58105a8f7c34a6c58cbb7ff6a7143b50642e
- clm_c4fd0e5e0c1c5147a32fc79116d88def0cc58fe9362ce92d6b69563e14ccdad3
- clm_ce98890160ea249edd83407136fc2437fa2835f79abf463fd2aa295817dc6488
- clm_ded61db43c3f57585ad0f728664933c5ebff742717264563189c8cfed72f52a1
- clm_f3dc0583e6eef2779645a908216986786a68db4a043bce2c6633c5ce8c23885d
maturity: draft
page_id: pg_9057bf4fb2755b21bfd11caf42e9041c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_223e0d21fb59585da4a1cf5bca8f77fe
title: Yeachan-Heo/oh-my-claudecode/README.md @ 5281b19e0d64
updated_at: '2026-09-14T03:26:04Z'
---

# Yeachan-Heo/oh-my-claudecode/README.md @ 5281b19e0d64

<!-- rcw:begin owner=source:src_223e0d21fb59585da4a1cf5bca8f77fe block=evidence -->
- OMC exposes two surfaces: terminal CLI commands (`omc ...`) run from a shell, and in-session slash skills (`/...`) run inside a Claude Code session after plugin setup. [@claim:clm_09003e45565102f98d3168c4bb3fe7f22f9a0d48b0aee2646e48fc301ba631ef]
- OMC writes runtime state, session data, plans, logs, and artifacts under `.omc/` by default; gitignore keeps it local except `.omc/skills/**` which stays committable, and `OMC_STATE_DIR` or a `.omc-workspace` marker can relocate or share state. [@claim:clm_0e5763ee6372f991b1537f41f90b736a539a313d970833937dd88a6370b319b8]
- `omc team N:<provider>` spawns on-demand tmux worker panes for claude, codex, gemini, antigravity, grok, or cursor CLIs; workers die when their task completes, and the selected CLI plus tmux must be installed and authenticated. [@claim:clm_0f495dbf894e1c3a06937302fa937b83c64e8813de20f0cd16694b5e9aa86f95]
- Repository development practice: CONTRIBUTING.md is the developer guide covering forking, local checkout setup, linking as the active plugin, running tests, and submitting PRs. [@claim:clm_3cb4573ad335aabe827764be1312b3881737bf8dda63fab96975e80008b5514b]
- The npm package installs both `oh-my-claudecode` and a short `omc` command alias, while the repo/plugin branding is oh-my-claudecode. [@claim:clm_4358309eff6d658bbc338075d2a66c0963d352053e411dd02b0d54a4b8a7799e]
- OMC does not ship a VS Code extension or document extension-specific install flows; interactive slash commands like /autopilot and /team require an active Claude Code session and should not be relied on in CI. [@claim:clm_44277a6e0b722de587bb276fb95dff6a87c08632da073940cc992a9045fd806e]
- The CLI depends on better-sqlite3, whose upstream prebuild-install@7.1.3 dependency triggers a deprecation warning during npm install; the warning is tracked in issue #2913 and does not indicate install failure. [@claim:clm_66942730338b47cba0334580b256f77caf3dc4e8f745e67075825e069cc49d99]
- Requirements include the Claude Code CLI plus a Claude Max/Pro subscription or Anthropic API key, and tmux is required for features like `omc team` and rate-limit detection. [@claim:clm_884722d1299b559920bc9207466615de89915d8bf62a82f4f9d3f1d7cf139093]
- Named autopilot stage profiles (v1) are selected via `/autopilot --workflow <name>`, configured under `autopilot.workflows` in project or user config, and admit only four fixed stage sequences such as [ralplan, execution, qa]. [@claim:clm_948fe740e11c0833a4b8d13853e7743fb370f3b502fa9fdf45e31ae2cc3c83a7]
- Custom skills are stored at `.omc/skills/` (project, higher priority) or `~/.omc/skills/` (user fallback), with frontmatter triggers, and matching skills auto-inject into context; `/skillify` extracts patterns with quality gates. [@claim:clm_a7d0a0341cadb84f57656a38bf5d58105a8f7c34a6c58cbb7ff6a7143b50642e]
- Named autopilot profiles currently require Linux with `flock`; unsupported environments reject explicit `--workflow` invocation before changing autopilot state, while legacy autopilot remains available. [@claim:clm_c4fd0e5e0c1c5147a32fc79116d88def0cc58fe9362ce92d6b69563e14ccdad3]
- Outside a git repository OMC uses a canonical state root at `~/.omc/` (or `$OMC_STATE_DIR/non-git`) and avoids creating per-cwd state roots or writing into sensitive directories like `~/.ssh` or `~/Downloads`. [@claim:clm_ce98890160ea249edd83407136fc2437fa2835f79abf463fd2aa295817dc6488]
- Team is the canonical orchestration surface as of v4.1.7, running a staged pipeline: team-plan, team-prd, team-exec, team-verify, and team-fix (loop); the legacy `swarm` alias was removed. [@claim:clm_ded61db43c3f57585ad0f728664933c5ebff742717264563189c8cfed72f52a1]
- The npm package exports TypeScript helpers such as `createOmcSession()` and prompt-expansion utilities built on `@anthropic-ai/claude-agent-sdk` as a library surface for Node.js programs. [@claim:clm_f3dc0583e6eef2779645a908216986786a68db4a043bce2c6633c5ce8c23885d]
<!-- rcw:end owner=source:src_223e0d21fb59585da4a1cf5bca8f77fe block=evidence -->

## Researcher notes

