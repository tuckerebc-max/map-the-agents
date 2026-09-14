---
access: public
aliases: []
claim_ids:
- clm_02e68adce837c824e1846213ed7eb762a28348114ae8544da3d61fc101495a95
- clm_039e018baf2d35362b6828f1a46436c7a8c29d66c5cbe4484d1afba37f13bf44
- clm_0e7510a799e6bbc1edcbe73ccb929f3b0b77393210b1c60bd89f94cc899ca0dd
- clm_15dc8b6f02a8bbe45f775c10c8190e9d4c465620574234c554158001b89cf75b
- clm_35e870cc7966d1c4dc1e7bdf9b9f51c7bb128754bfe3f51402bfeca01ace5e78
- clm_4363308b74241602323288899bff03ab2fd1417f254a412ef1220da3b1a3fa65
- clm_43924c6c2bb4bbcd38dde325493e5624d12242555f81090cd0556e68e0f51c8b
- clm_742b06fe5ebde34053b73e363269d7dbcdc9d8a78d03a8ff8c2c8f90941976d3
- clm_78f3fc68fbac48418b326199dc2359fe9a1908967d6e605dba8ab64b20ab3d9a
- clm_b419b81020c502ed0226738b2c8c1a57c15b37d3dea4d7d0b4489782d32b4db6
- clm_f3043de202908b1ecb3cb571977985b01ee93842474564bbb111ccf994af977c
- clm_ffcf84958defce4378189ab74befa2f1116e03533d79c79d41b8dee050be836d
maturity: draft
page_id: pg_1f08548488375f318d0ea3194af74a9a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_c560be4bfe435f9a93f02aaaf0508742
title: charmbracelet/crush/docs/hooks/README.md @ 3502b15a7cf1
updated_at: '2026-09-14T01:40:40Z'
---

# charmbracelet/crush/docs/hooks/README.md @ 3502b15a7cf1

<!-- rcw:begin owner=source:src_c560be4bfe435f9a93f02aaaf0508742 block=evidence -->
- Currently only one hook event, PreToolUse, is supported; it fires before every top-level agent tool call and matches against the tool name, with sub-agent tool calls not intercepted. [@claim:clm_02e68adce837c824e1846213ed7eb762a28348114ae8544da3d61fc101495a95]
- Hooks are user-defined shell commands configured under a 'hooks' object in crush.json, keyed by event name, with optional name, matcher regex, required command, and timeout (default 30s). [@claim:clm_039e018baf2d35362b6828f1a46436c7a8c29d66c5cbe4484d1afba37f13bf44]
- PowerShell .ps1 scripts are not auto-dispatched by extension and must be invoked explicitly via powershell -File or pwsh -File. [@claim:clm_0e7510a799e6bbc1edcbe73ccb929f3b0b77393210b1c60bd89f94cc899ca0dd]
- Config is discovered from project-level .crushrc/crushrc and XDG config paths with project settings overriding global ones; crushrc overrides JSON in the same directory, and hook command paths resolve relative to the current working directory. [@claim:clm_15dc8b6f02a8bbe45f775c10c8190e9d4c465620574234c554158001b89cf75b]
- Hooks execute through Crush's embedded POSIX shell (mvdan.cc/sh), the same interpreter as the bash tool; shebang'd scripts dispatch to the named interpreter via os/exec, identically across macOS, Linux, and Windows. [@claim:clm_35e870cc7966d1c4dc1e7bdf9b9f51c7bb128754bfe3f51402bfeca01ace5e78]
- Crush hooks are designed to be broadly compatible with Claude Code hooks, with one intentional divergence: updated_input is treated as a shallow-merge patch rather than a full replacement. [@claim:clm_4363308b74241602323288899bff03ab2fd1417f254a412ef1220da3b1a3fa65]
- Hook results apply before permission checks: an aggregated 'deny' blocks the call without a prompt, 'allow' pre-approves and skips the prompt, and no decision falls through to the normal permission flow. [@claim:clm_43924c6c2bb4bbcd38dde325493e5624d12242555f81090cd0556e68e0f51c8b]
- Hooks run in parallel but their results compose deterministically in config order; deny beats allow, updated_input patches shallow-merge sequentially, and identical commands are deduplicated. [@claim:clm_742b06fe5ebde34053b73e363269d7dbcdc9d8a78d03a8ff8c2c8f90941976d3]
- Exit code 2 blocks the tool call with stderr as the deny reason, exit 49 halts the whole turn, exit 0 parses stdout as a JSON envelope with decision, halt, reason, context, and updated_input fields. [@claim:clm_78f3fc68fbac48418b326199dc2359fe9a1908967d6e605dba8ab64b20ab3d9a]
- If a hook exceeds its timeout (default 30 seconds), the result is treated as a non-blocking error and the tool call proceeds; shebang subprocesses are killed via exec.CommandContext. [@claim:clm_b419b81020c502ed0226738b2c8c1a57c15b37d3dea4d7d0b4489782d32b4db6]
- Crush ships a builtin crush-hook skill so the agent can write, edit, and configure hooks on itself, and a builtin config skill for natural-language configuration. [@claim:clm_f3043de202908b1ecb3cb571977985b01ee93842474564bbb111ccf994af977c]
- Hooks receive input via environment variables (e.g. CRUSH_TOOL_NAME, CRUSH_TOOL_INPUT_COMMAND) and JSON on stdin, and communicate results back through exit codes plus stdout/stderr. [@claim:clm_ffcf84958defce4378189ab74befa2f1116e03533d79c79d41b8dee050be836d]
<!-- rcw:end owner=source:src_c560be4bfe435f9a93f02aaaf0508742 block=evidence -->

## Researcher notes

