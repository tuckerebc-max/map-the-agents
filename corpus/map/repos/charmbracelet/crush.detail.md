# charmbracelet/crush -- full detail

[Back to orientation](crush.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/charmbracelet/crush/3502b15a7cf14c081b87285f5cee05343806a86a/7bb77b7deb239b31.json](../../../wiki/dossiers/charmbracelet/crush/3502b15a7cf14c081b87285f5cee05343806a86a/7bb77b7deb239b31.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Crush ships a builtin crush-hook skill so the agent can write, edit, and configure hooks on itself, and a builtin config skill for natural-language configuration. -- evidence: [docs/config/README.md#L6-L13](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/config/README.md#L6-L13), [docs/hooks/README.md#L15-L23](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L15-L23) (`clm_f3043de202908b1ecb3cb571977985b01ee93842474564bbb111ccf994af977c`)

## design-choices (3 claim(s))

- [observation/documented] Hooks run in parallel but their results compose deterministically in config order; deny beats allow, updated_input patches shallow-merge sequentially, and identical commands are deduplicated. -- evidence: [docs/hooks/README.md#L383-L385](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L383-L385), [docs/hooks/README.md#L174-L175](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L174-L175), [docs/hooks/README.md#L15-L23](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L15-L23), [docs/hooks/README.md#L389-L398](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L389-L398), [docs/hooks/README.md#L726-L733](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L726-L733), [docs/hooks/README.md#L207-L219](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L207-L219) (`clm_742b06fe5ebde34053b73e363269d7dbcdc9d8a78d03a8ff8c2c8f90941976d3`)
- [observation/documented] Hooks execute through Crush's embedded POSIX shell (mvdan.cc/sh), the same interpreter as the bash tool; shebang'd scripts dispatch to the named interpreter via os/exec, identically across macOS, Linux, and Windows. -- evidence: [docs/hooks/README.md#L95-L99](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L95-L99) (`clm_35e870cc7966d1c4dc1e7bdf9b9f51c7bb128754bfe3f51402bfeca01ace5e78`)
- [observation/documented] Crush hooks are designed to be broadly compatible with Claude Code hooks, with one intentional divergence: updated_input is treated as a shallow-merge patch rather than a full replacement. -- evidence: [docs/hooks/README.md#L15-L23](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L15-L23), [docs/hooks/README.md#L582-L584](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L582-L584), [docs/hooks/README.md#L576-L580](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L576-L580) (`clm_4363308b74241602323288899bff03ab2fd1417f254a412ef1220da3b1a3fa65`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (6 claim(s))

- [observation/documented] Hooks are user-defined shell commands configured under a 'hooks' object in crush.json, keyed by event name, with optional name, matcher regex, required command, and timeout (default 30s). -- evidence: [docs/hooks/README.md#L608-L609](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L608-L609), [docs/hooks/README.md#L137-L150](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L137-L150), [docs/hooks/README.md#L614-L617](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L614-L617), [docs/hooks/README.md#L611-L612](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L611-L612), [docs/hooks/README.md#L602-L606](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L602-L606), [docs/hooks/README.md#L200-L201](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L200-L201), [docs/hooks/README.md#L6-L8](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L6-L8) (`clm_039e018baf2d35362b6828f1a46436c7a8c29d66c5cbe4484d1afba37f13bf44`)
- [observation/documented] Currently only one hook event, PreToolUse, is supported; it fires before every top-level agent tool call and matches against the tool name, with sub-agent tool calls not intercepted. -- evidence: [docs/hooks/README.md#L183-L185](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L183-L185), [docs/hooks/README.md#L187-L188](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L187-L188), [docs/hooks/README.md#L194-L198](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L194-L198), [docs/hooks/README.md#L15-L23](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L15-L23) (`clm_02e68adce837c824e1846213ed7eb762a28348114ae8544da3d61fc101495a95`)
- [observation/documented] Hooks receive input via environment variables (e.g. CRUSH_TOOL_NAME, CRUSH_TOOL_INPUT_COMMAND) and JSON on stdin, and communicate results back through exit codes plus stdout/stderr. -- evidence: [docs/hooks/README.md#L227-L229](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L227-L229), [docs/hooks/README.md#L235-L246](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L235-L246), [docs/hooks/README.md#L291-L293](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L291-L293), [docs/hooks/README.md#L254-L254](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L254-L254) (`clm_ffcf84958defce4378189ab74befa2f1116e03533d79c79d41b8dee050be836d`)
- [observation/documented] Exit code 2 blocks the tool call with stderr as the deny reason, exit 49 halts the whole turn, exit 0 parses stdout as a JSON envelope with decision, halt, reason, context, and updated_input fields. -- evidence: [docs/hooks/README.md#L702-L707](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L702-L707), [docs/hooks/README.md#L303-L308](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L303-L308), [docs/hooks/README.md#L312-L318](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L312-L318), [docs/hooks/README.md#L324-L333](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L324-L333) (`clm_78f3fc68fbac48418b326199dc2359fe9a1908967d6e605dba8ab64b20ab3d9a`)
- [observation/documented] Configuration is Bash-based via builtin commands (provider, model, mcp, lsp, hook, permissions, option) in a crushrc file that runs at startup; legacy JSON config is still supported but deprecated and receives no new features. -- evidence: [docs/config/README.md#L67-L68](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/config/README.md#L67-L68), [docs/config/README.md#L117-L126](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/config/README.md#L117-L126), [docs/config/README.md#L15-L18](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/config/README.md#L15-L18), [docs/config/README.md#L113-L115](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/config/README.md#L113-L115) (`clm_445ecab51d2efcdc492926e8559a07e0d850ff7096daf102bd67a06b8ef3e8f3`)
- [observation/documented] Config is discovered from project-level .crushrc/crushrc and XDG config paths with project settings overriding global ones; crushrc overrides JSON in the same directory, and hook command paths resolve relative to the current working directory. -- evidence: [docs/hooks/README.md#L152-L172](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L152-L172), [docs/config/README.md#L97-L100](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/config/README.md#L97-L100), [docs/hooks/README.md#L134-L135](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L134-L135), [docs/config/README.md#L91-L95](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/config/README.md#L91-L95) (`clm_15dc8b6f02a8bbe45f775c10c8190e9d4c465620574234c554158001b89cf75b`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Hook results apply before permission checks: an aggregated 'deny' blocks the call without a prompt, 'allow' pre-approves and skips the prompt, and no decision falls through to the normal permission flow. -- evidence: [docs/hooks/README.md#L339-L344](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L339-L344), [docs/hooks/README.md#L726-L733](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L726-L733), [docs/hooks/README.md#L686-L690](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L686-L690), [docs/hooks/README.md#L207-L219](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L207-L219) (`clm_43924c6c2bb4bbcd38dde325493e5624d12242555f81090cd0556e68e0f51c8b`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (2 claim(s))

- [observation/documented] PowerShell .ps1 scripts are not auto-dispatched by extension and must be invoked explicitly via powershell -File or pwsh -File. -- evidence: [docs/hooks/README.md#L103-L130](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L103-L130) (`clm_0e7510a799e6bbc1edcbe73ccb929f3b0b77393210b1c60bd89f94cc899ca0dd`)
- [observation/documented] If a hook exceeds its timeout (default 30 seconds), the result is treated as a non-blocking error and the tool call proceeds; shebang subprocesses are killed via exec.CommandContext. -- evidence: [docs/hooks/README.md#L402-L407](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L402-L407), [docs/hooks/README.md#L103-L130](https://github.com/charmbracelet/crush/blob/3502b15a7cf14c081b87285f5cee05343806a86a/docs/hooks/README.md#L103-L130) (`clm_b419b81020c502ed0226738b2c8c1a57c15b37d3dea4d7d0b4489782d32b4db6`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

