# ralph-workflow/ralph-workflow -- full detail

[Back to orientation](ralph-workflow.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ralph-workflow/ralph-workflow/3d9d847f41feb72c7c2f14ce8612901df08b1427/b4e9678f061e3d05.json](../../../wiki/dossiers/ralph-workflow/ralph-workflow/3d9d847f41feb72c7c2f14ce8612901df08b1427/b4e9678f061e3d05.json)

## specifications (1 claim(s))

- [observation/documented] Ralph Workflow is described as a free, open-source AI agent orchestrator for coding work that takes one well-specified task and runs a Ralph loop with the user's chosen coding agent. -- evidence: [README.md#L3-L8](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/README.md#L3-L8) (`clm_0756b1face0a85e69053abd93b70edd96b56401c1869f8bd6498593eb7621231`)

## components (1 claim(s))

- [observation/documented] The product ships nine built-in agent backends: Claude Code, Claude Code headless, Codex, OpenCode, Nanocoder, AGY, Pi, Cursor, and Kimi; the user authenticates one locally and the tool uses it. -- evidence: [README.md#L48-L53](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/README.md#L48-L53) (`clm_6138f051cd67c4496c9d03d8afea6610b0056e37bf62c5624c10fd038c6b5999`)

## design-choices (1 claim(s))

- [observation/documented] The Ralph Loop pattern is attributed to Geoffrey Huntley (ghuntley.com/ralph), with Ralph Workflow positioned as an independent reference implementation of that pattern. -- evidence: [README.md#L71-L73](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/README.md#L71-L73) (`clm_57fcee6b3aa34ec3c979336ece4ab6430d7a4cadd061ff251fff4c0a303e401d`)

## workflows (5 claim(s))

- [observation/documented] Repository development practice: AGENTS.md mandates trunk-based development with all work committed directly to main, forbids branch creation and pull requests, and permits commits only via `ralph --generate-commit`. -- evidence: [AGENTS.md#L202-L213](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/AGENTS.md#L202-L213), [AGENTS.md#L217-L217](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/AGENTS.md#L217-L217) (`clm_5f35a275a7f9bdbc9098083e74a7d98e90dafb82dcefafb0b4c315fa7c55c512`)
- [observation/documented] Repository development practice: contributors must run `make verify` from ralph-workflow/ before completion; it must pass in full with no unrelated-failure exemptions, and a red gate is owned by whoever next observes it. -- evidence: [AGENTS.md#L244-L245](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/AGENTS.md#L244-L245), [AGENTS.md#L44-L45](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/AGENTS.md#L44-L45), [AGENTS.md#L54-L54](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/AGENTS.md#L54-L54), [AGENTS.md#L239-L242](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/AGENTS.md#L239-L242) (`clm_4242f15bcc11fae734b5dffb4d0fd9978645d757a2c8a17851b57de26db5dcc5`)
- [observation/documented] Repository development practice: all tests must fit a combined 60-second wall-clock budget enforced by import-time invariants in ralph/verify.py, with non-circumvention rules against splitting suites or raising per-suite timeouts. -- evidence: [AGENTS.md#L162-L171](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/AGENTS.md#L162-L171), [AGENTS.md#L140-L143](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/AGENTS.md#L140-L143) (`clm_34ff02e0e76ad65e22f6596286f51db4a60142ead597023033688841c9732259`)
- [observation/documented] Repository development practice: a three-level fabrication_guard.py checks public-facing markdown, with level 1 as a pre-commit hook and levels 2-3 verifying external repos, packages, and stats against live sources. -- evidence: [AGENTS.md#L100-L113](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/AGENTS.md#L100-L113), [AGENTS.md#L86-L96](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/AGENTS.md#L86-L96) (`clm_faac9936e43b482813be191f4051587cbf7d43e452cf683a9a33fb48caac1eb8`)
- [observation/documented] Repository development practice: contributions are accepted under a CLA granting the project rights to relicense under AGPL-3.0-or-later, commercial, or future open-source licenses, agreed by checking a box in a GitHub or Codeberg pull request. -- evidence: [CLA.md#L7-L8](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/CLA.md#L7-L8), [CLA.md#L10-L28](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/CLA.md#L10-L28), [CLA.md#L3-L5](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/CLA.md#L3-L5) (`clm_9967166034659e175b3c0e77ba362471373692660f363fc7959a806f07699f5a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] A checkout install provides an `rdev` launcher whose `--version` ends in -build, deliberately leaving any globally installed `ralph` command in place; native Windows users are directed to install the published package via pipx or pip. -- evidence: [README.md#L31-L32](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/README.md#L31-L32), [README.md#L36-L44](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/README.md#L36-L44) (`clm_6f8e35ff842d220ab6115e4de8b5768bb5ccbf9218469d423d5dc458e858dc10`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] The core orchestration is a Ralph loop of plan, build, verify, and fix stages run with the selected coding agent, after which the user returns to inspect the result. -- evidence: [README.md#L3-L8](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/README.md#L3-L8) (`clm_c0f087015e0f49879d441108235060bca5a30d9a2f3abd16a09c2ddd6e7435d2`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The runtime requires Python 3.12 or newer and is described as local-first; the project is licensed AGPL-3.0-or-later and published on PyPI. -- evidence: [README.md#L64-L69](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/README.md#L64-L69) (`clm_ae06c66c616fb45c77e30dba95a5309912b21c26f2085e4810620ff272c51711`)

## limitations (1 claim(s))

- [observation/documented] The README states the tool is not intended for vague prompts or repositories lacking tests or other guardrails, targeting work too large to babysit but too risky to trust blindly. -- evidence: [README.md#L12-L14](https://github.com/Ralph-Workflow/Ralph-Workflow/blob/3d9d847f41feb72c7c2f14ce8612901df08b1427/README.md#L12-L14) (`clm_2f4d0597996b6c14f584cf0a60a9697d135fb11371873bfa1b7208c2c6080760`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

