---
access: public
aliases: []
claim_ids:
- clm_0342236ffe4cea150b506721513f43a2a3040cfb1946b830869165d8d12d10e0
- clm_0a90814568fcabed14766bd9ae06bc16372c53b2ab579a632deed9dc0b815fc1
- clm_0c0833d9ba1bb78e5fa275c4249624eee998c56479c2ab93e638f379094500a0
- clm_147c40d8ef14db521b4f7ab30cb438f5f4239dc2b8463d926869e414e4d2845e
- clm_38206e2fa2d294f98e74ccbc615d8a90db1bbd33b77fcdcadd53ac22d257f00a
- clm_398de9d2b9b722c8237b5085f7a2548a0eb8a6b0a417104c8a5229a48ec29810
- clm_558c6db627c162c3743654e3dfde42b716630ec7f04ad5de4370b7bb1a530537
- clm_974c349f61af1b85e37dfb31c9eceba5d24565568a8a54afc9834f5c88b1ad9d
- clm_a17c3ed4b6a94ef5c0ebe0f7a056874331986af96d160b05be07b12e0ba25287
- clm_a6ae2137ded79b6af742a27427f8195a29350c7cdc718a58b9625265b949bda3
- clm_a79f1b1a8bfa2911a6e70b31b70a99d0706942eeb96748efca7fa9118b5ef5f5
- clm_f5b413af9d02a5adc2b7859737a8b3907b7a1ed9f69cfd14991644c80e9aba9c
maturity: draft
page_id: pg_074c3800ce245f98be705738763ef6ad
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f5ef0d46254a56ba8eebb052ba0f3567
title: iamfakeguru/agent-md/README.md @ ae8117e903fe
updated_at: '2026-09-14T03:58:10Z'
---

# iamfakeguru/agent-md/README.md @ ae8117e903fe

<!-- rcw:begin owner=source:src_f5ef0d46254a56ba8eebb052ba0f3567 block=evidence -->
- Codex hook support is described as experimental and requires enabling codex_hooks = true under [features] in ~/.codex/config.toml. [@claim:clm_0342236ffe4cea150b506721513f43a2a3040cfb1946b830869165d8d12d10e0]
- agent-md.toml declares deterministic verification: a [verify] section for typecheck, lint, test, and per-file lint commands, and a [visual] section with required, artifacts_dir, and freshness_seconds. [@claim:clm_0a90814568fcabed14766bd9ae06bc16372c53b2ab579a632deed9dc0b815fc1]
- Documented limits: rules cannot force judgment, hooks only cover host-exposed events, pre-commit can be bypassed with git commit --no-verify, bash safety hooks are guardrails not a sandbox, and Cursor/Windsurf get only rules plus optional git-hook fallback. [@claim:clm_0c0833d9ba1bb78e5fa275c4249624eee998c56479c2ab93e638f379094500a0]
- The product enforces verification of agent work: stop hooks require type-check/lint/tests, and the strict visual hook requires a fresh non-empty markdown note referencing a fresh non-empty image with required fields. [@claim:clm_147c40d8ef14db521b4f7ab30cb438f5f4239dc2b8463d926869e414e4d2845e]
- Visual evidence is captured with ./.agent-md/bin/playwright-capture.sh <url> <png path>, producing artifacts under .agent/visual/ alongside a structured markdown note. [@claim:clm_38206e2fa2d294f98e74ccbc615d8a90db1bbd33b77fcdcadd53ac22d257f00a]
- Native Codex skills live under .agents/skills/<name>/SKILL.md (agent-md-verify and visual-evidence) and are invoked with $agent-md-verify or $visual-evidence, distinct from plain shell helpers in .agent-md/bin. [@claim:clm_398de9d2b9b722c8237b5085f7a2548a0eb8a6b0a417104c8a5229a48ec29810]
- install.sh accepts flags including --agent=<list>, --githooks/--no-githooks, and --claude-settings=skip|merge|replace, and can be run via a curl-piped one-liner. [@claim:clm_558c6db627c162c3743654e3dfde42b716630ec7f04ad5de4370b7bb1a530537]
- A memory/ directory with agents.md, plan.md, progress.md, verify.md, and gotchas.md serves as durable cross-session state; a state hook blocks completion when source files changed but progress.md did not. [@claim:clm_974c349f61af1b85e37dfb31c9eceba5d24565568a8a54afc9834f5c88b1ad9d]
- Bash safety is hard-blocked for Claude Code via .claude/hooks/block-destructive.sh and for Codex via .codex/hooks/pre-tool-use.sh, but is not covered for Cursor, Windsurf, or other agents. [@claim:clm_a17c3ed4b6a94ef5c0ebe0f7a056874331986af96d160b05be07b12e0ba25287]
- The design separates agent guidance into two layers: advisory rules files for judgment and process, and enforceable hooks/artifacts for checks, state updates, and visual evidence. [@claim:clm_a6ae2137ded79b6af742a27427f8195a29350c7cdc718a58b9625265b949bda3]
- Repository development practice: contributors run bats tests/ and shellcheck over hook and helper scripts, and CI runs Bats, ShellCheck, JSON validation, alias-sync checks, and installer smoke tests. [@claim:clm_a79f1b1a8bfa2911a6e70b31b70a99d0706942eeb96748efca7fa9118b5ef5f5]
- The installer provisions AGENT.md as source of truth plus agent-specific rule files, hook directories, .agents/skills, .agent-md/bin helper scripts, memory/*.md files, and an optional .githooks/pre-commit fallback. [@claim:clm_f5b413af9d02a5adc2b7859737a8b3907b7a1ed9f69cfd14991644c80e9aba9c]
<!-- rcw:end owner=source:src_f5ef0d46254a56ba8eebb052ba0f3567 block=evidence -->

## Researcher notes

