# nicepkg/auto-company -- full detail

[Back to orientation](auto-company.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/nicepkg/auto-company/125292073565035455495c8769bca3b27775030d/3916683b1363d27f.json](../../../wiki/dossiers/nicepkg/auto-company/125292073565035455495c8769bca3b27775030d/3916683b1363d27f.json)

## specifications (1 claim(s))

- [observation/documented] The product is described as a fully autonomous AI company of 14 agents that conceives products, makes decisions, writes code, deploys, and markets with no human involvement, driven by Claude Code Agent Teams. -- evidence: [README.md#L7-L8](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L7-L8), [README.md#L10-L10](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L10-L10) (`clm_336d49c8f2fd8b9e537bf891e30a061b30c4c13ca93ab6cdca2694fefc169a62`)

## components (1 claim(s))

- [observation/documented] The repo ships 14 agent persona definitions under .claude/agents (e.g. ceo-bezos, cto-vogels, critic-munger, fullstack-dhh, qa-bach, devops-hightower, cfo-campbell, research-thompson) plus 30+ skills under .claude/skills. -- evidence: [README.md#L47-L62](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L47-L62), [README.md#L64-L64](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L64-L64), [README.md#L175-L193](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L175-L193), [CLAUDE.md#L37-L37](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/CLAUDE.md#L37-L37) (`clm_80d97e2f431a312847f8eea4efa9a659b7c2964a4ad53fba526284b96386bba7`)

## design-choices (2 claim(s))

- [observation/documented] Agents are prompted as real-world luminaries (e.g. 'you are DHH' rather than 'you are a developer') to activate the LLM's deep domain knowledge, and the charter sets decision principles like Ship > Plan > Discuss and monolith-first boring technology. -- evidence: [README.md#L45-L45](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L45-L45), [CLAUDE.md#L80-L86](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/CLAUDE.md#L80-L86) (`clm_c823a96cae53118e686fd8a8e57cab5c4377e9707e5e7788223aee602bc2da8c`)
- [inference/documented] Human steering appears to be intentionally limited to editing the 'Next Action' in memories/consensus.md (plus pause/resume), since the charter says humans guide direction only through that file while everything else stays autonomous. -- evidence: [README.md#L143-L148](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L143-L148), [CLAUDE.md#L17-L17](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/CLAUDE.md#L17-L17) (`clm_bf1dea5425fa0402ae0d898bce0423797394e7b2d18b8d4d6f92998194082f44`)

## workflows (1 claim(s))

- [observation/documented] Six standard collaboration chains are defined (new product evaluation, feature development, launch, pricing, weekly review, opportunity discovery), and convergence rules force concrete output: cycle 1 brainstorm, cycle 2 GO/NO-GO pre-mortem, and from cycle 3 onward pure discussion is forbidden. -- evidence: [README.md#L130-L137](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L130-L137), [PROMPT.md#L61-L65](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/PROMPT.md#L61-L65), [CLAUDE.md#L92-L97](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/CLAUDE.md#L92-L97), [README.md#L122-L126](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L122-L126) (`clm_12aab05b3b2550f770c5cc2bdf91244b629d5986ddf2e8eee126c5f57285f87f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Users control the loop through make targets: start, start-awake, stop, status, monitor, last, cycles, awake, install/uninstall (launchd daemon), pause, and resume. -- evidence: [README.md#L87-L101](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L87-L101) (`clm_1d9ede3bdb71359c304722ebf12833eae9e6e08d7667dd74c7186cd2c28a4d1a`)

## memory-state (1 claim(s))

- [observation/documented] Each cycle is an independent `claude -p` call, and memories/consensus.md is stated to be the only cross-cycle state, like a relay baton; the prompt requires updating it before each cycle ends with fields such as Current Phase, Key Decisions, Active Projects, Next Action, and Company State. -- evidence: [PROMPT.md#L26-L26](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/PROMPT.md#L26-L26), [README.md#L41-L41](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L41-L41), [PROMPT.md#L44-L44](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/PROMPT.md#L44-L44), [PROMPT.md#L47-L47](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/PROMPT.md#L47-L47), [PROMPT.md#L35-L35](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/PROMPT.md#L35-L35), [PROMPT.md#L50-L53](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/PROMPT.md#L50-L53) (`clm_c737d3f8bdb7d62887074d3cb1e00d4b1dcc0f4dc9fa838db7c0bf05257a3815`)

## orchestration (1 claim(s))

- [observation/documented] A launchd-managed auto-loop.sh runs an endless cycle: read PROMPT.md and consensus.md, drive one work period via `claude -p`, then handle failures (rate-limit waits, circuit breaker, consensus rollback) and sleep before the next round. -- evidence: [README.md#L27-L39](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L27-L39) (`clm_5db5de085a051b95c994193a9d557fcface3741461a1bc2cf93b02cf985067b5`)

## tools-permissions (1 claim(s))

- [observation/documented] The runtime charter grants agents all terminal tools (gh, wrangler, git, node/npm, uv/python, curl/jq listed as available) with hard safety red lines: no repo deletion, no wrangler delete, no deleting system files, no credential leaks, no force-push to main/master, and new projects must live under projects/. -- evidence: [CLAUDE.md#L122-L122](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/CLAUDE.md#L122-L122), [CLAUDE.md#L126-L133](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/CLAUDE.md#L126-L133), [CLAUDE.md#L21-L29](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/CLAUDE.md#L21-L29), [README.md#L154-L160](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L154-L160) (`clm_081ef3c5eb9b1353da916b373f3648a5b174b903adc88474ae04ad6062cb7ae6`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Requirements are macOS (launchd-based daemon; Linux/systemd listed as future), an installed and logged-in Claude Code CLI, and a Claude subscription (Max or Pro recommended); jq, gh, and wrangler are optional. -- evidence: [README.md#L197-L204](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L197-L204) (`clm_a34ca7be637b13d909aef57592040cf966f4027b92dd1861863a36839dae0ef0`)

## limitations (1 claim(s))

- [observation/documented] The project is flagged experimental: macOS-only, running but not guaranteed stable, consumes Claude API quota each cycle, acts fully autonomously without asking humans, and carries no warranty that the AI won't build unexpected things. -- evidence: [README.md#L17-L17](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L17-L17), [README.md#L210-L214](https://github.com/nicepkg/auto-company/blob/125292073565035455495c8769bca3b27775030d/README.md#L210-L214) (`clm_8d654b0e9ae9a8452f2c1abbb956a698063c87c2fc677fbebb6d073683e9cbb4`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

