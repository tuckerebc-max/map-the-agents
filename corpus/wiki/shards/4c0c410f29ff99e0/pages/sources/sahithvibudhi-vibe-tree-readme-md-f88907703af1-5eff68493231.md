---
access: public
aliases: []
claim_ids:
- clm_038be0631a5b316ce43a12c48361046d211de994430d6a8a7bf263b734a821e9
- clm_205f718d29f83017b4dd1053175d525326c958d35a7637161c44bdc52bd82bda
- clm_570f150a49075883bf351b0166be5dd84cc2af6c1288cccc544c302a1751003d
- clm_6bbfe589dc93ac98ce2be6097884687e70eaa6e5474380c79c60a604e33c1847
- clm_78a0f40fdd92ef82d64cf8bb0182e42bd399a308354d37e7387ed4cfd7536611
- clm_db6fedb16fd6d15dffc4b1d1aa9c491ac9f2c450f8e6a2406264bd173e66ceb5
- clm_e665bba61dedeba4332280ee61f483389303b23b9c92b03eeba5dd0307ce192e
maturity: draft
page_id: pg_ce8fb38ffdfd54fc892c5eff68493231
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3f637e20494258919062b55db48b640e
title: sahithvibudhi/vibe-tree/README.md @ f88907703af1
updated_at: '2026-09-14T02:38:42Z'
---

# sahithvibudhi/vibe-tree/README.md @ f88907703af1

<!-- rcw:begin owner=source:src_3f637e20494258919062b55db48b640e block=evidence -->
- Repository development practice: contributors run pnpm install, pnpm dev:desktop/dev:all, unit tests via pnpm test:run, Playwright e2e suites, and pnpm typecheck && pnpm lint; CI runs lint, typecheck, unit tests, builds, and e2e. [@claim:clm_038be0631a5b316ce43a12c48361046d211de994430d6a8a7bf263b734a821e9]
- VibeTree runs each AI coding agent in its own git worktree in parallel, giving every task an isolated checkout with its own branch and terminal. [@claim:clm_205f718d29f83017b4dd1053175d525326c958d35a7637161c44bdc52bd82bda]
- macOS builds are not yet notarized; users must approve the app once under System Settings, Privacy and Security, or install via the provided Homebrew cask. [@claim:clm_570f150a49075883bf351b0166be5dd84cc2af6c1288cccc544c302a1751003d]
- The desktop app embeds its server on 127.0.0.1 with a per-launch token so nothing is exposed to the network; the standalone server can require login via AUTH_REQUIRED, VIBETREE_USERNAME, and VIBETREE_PASSWORD. [@claim:clm_6bbfe589dc93ac98ce2be6097884687e70eaa6e5474380c79c60a604e33c1847]
- The product works with terminal-based agent CLIs including Claude Code, OpenAI Codex CLI, Gemini CLI, Aider, and opencode, since agents run in a real terminal. [@claim:clm_78a0f40fdd92ef82d64cf8bb0182e42bd399a308354d37e7387ed4cfd7536611]
- Worktree lifecycle hooks (.vibetree/hooks/post-create and pre-remove) run around git worktree add/remove; failures warn but never block, and pre-remove cannot block deletion. [@claim:clm_db6fedb16fd6d15dffc4b1d1aa9c491ac9f2c450f8e6a2406264bd173e66ceb5]
- It ships as an Electron desktop app and as a standalone server drivable from any browser or phone, including QR pairing for mobile access. [@claim:clm_e665bba61dedeba4332280ee61f483389303b23b9c92b03eeba5dd0307ce192e]
<!-- rcw:end owner=source:src_3f637e20494258919062b55db48b640e block=evidence -->

## Researcher notes

