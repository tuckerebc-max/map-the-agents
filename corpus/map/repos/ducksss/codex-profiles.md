# ducksss/codex-profiles

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 5a8084bf8a3a @ 07c8aeb13ebe19ba

## Summary (orientation draft, not independently verified)

codex-profiles is a community-maintained, dependency-free Bash CLI that manages named Codex homes (~/.codex-<name>) and, on macOS, named ChatGPT windows with separate local state, plus workspace bindings, shell integration, and config-sharing commands. Evidence is documentation-only (README, agent.md, llms.txt, USAGE.md); no source code is shown. Evidence coverage: 149 of 292 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 10 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] launcher create builds a small unsigned macOS app in ~/Applications (overridable via CODEX_PROFILE_LAUNCHER_ROOT) that calls codex-profile app <profile>, with named/color-coded identities and list/path/remove subcommands. -- evidence: [docs/llms.txt#L221-L223](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L221-L223), [docs/llms.txt#L214-L219](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L214-L219), [docs/llms.txt#L208-L212](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L208-L212)
- design-choices (3 claim(s)):
  - [observation/documented] Profile selection maps the name 'default' to ~/.codex and any other name <x> to ~/.codex-<x>, so each profile gets its own Codex home. -- evidence: [docs/llms.txt#L8-L118](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L8-L118), [README.md#L170-L174](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/README.md#L170-L174)
  - [observation/documented] init --share-with links only a fixed allowlist of configuration entries (config.toml, AGENTS.md, instructions.md, rules/, plugins/, etc.) while auth.json, sessions, and Electron data stay per-profile; the tool never reads or copies authentication tokens or cookies. -- evidence: [README.md#L180-L184](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/README.md#L180-L184), [docs/llms.txt#L249-L253](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L249-L253), [docs/llms.txt#L255-L260](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L255-L260)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors are pointed to a contributor guide and coding-agent instructions; there is no build step, and the README instructs running 'make check' as the complete local gate before submitting changes. -- evidence: [README.md#L273-L275](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/README.md#L273-L275), [README.md#L277-L279](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/README.md#L277-L279)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The tool exposes a CLI with commands including setup, init, login, cli, app, run, list, status, doctor, path, shell-init, workspace bind, launcher create, env, and detach. -- evidence: [README.md#L235-L245](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/README.md#L235-L245), [docs/llms.txt#L142-L164](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L142-L164)
  - [observation/documented] shell-init prints shell code for bash/zsh/fish that enables 'use <profile>' in the current shell, with optional --prompt and --completions; it never edits shell startup files. -- evidence: [USAGE.md#L47-L48](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/USAGE.md#L47-L48), [docs/llms.txt#L227-L245](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L227-L245)
- memory-state (1 claim(s)):
  - [observation/documented] Workspace bindings store only a canonical path and profile name under ${XDG_CONFIG_HOME:-~/.config}/codex-profile with private permissions, relocatable via CODEX_PROFILE_CONFIG_HOME; nested bindings override ancestors. -- evidence: [docs/llms.txt#L171-L176](https://github.com/Ducksss/codex-profiles/blob/5a8084bf8a3ab8f94d739a4f513cca246194c7cd/docs/llms.txt#L171-L176)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](codex-profiles.detail.md)

Metadata and full claim list: [full detail](codex-profiles.detail.md)
Human notes ([notes](codex-profiles.notes.md), never overwritten by build)

[Back to map index](../../index.md)
