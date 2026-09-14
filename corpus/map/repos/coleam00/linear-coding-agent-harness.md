# coleam00/linear-coding-agent-harness

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit c37dc0969930 @ d9f454e04233bbea

## Summary (orientation draft, not independently verified)

A demo harness built on the Claude Agent SDK that runs a two-agent (initializer + coding) pattern with Linear as the project-management backbone, using MCP servers for Linear and Puppeteer and a layered security model. Evidence is README-only plus a requirements file.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The repository includes modules for agent session logic, Claude SDK/MCP client configuration, security validation, progress tracking, prompt loading, and Linear configuration constants, plus prompt files for both agent roles. -- evidence: [README.md#L134-L148](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L134-L148)
  - [observation/documented] Two MCP servers are used: Linear over Streamable HTTP for issue/status/comment management, and Puppeteer over stdio for browser-based UI testing. -- evidence: [README.md#L165-L168](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L165-L168)
- design-choices (2 claim(s)):
  - [observation/documented] The demo implements a two-agent pattern: an initializer agent that sets up the Linear project and issues, and a coding agent that implements them. -- evidence: [README.md#L7-L12](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L7-L12), [README.md#L3-L3](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L3-L3)
  - [observation/documented] All work tracking and inter-agent communication happens through Linear issues, comments, and status transitions rather than local text files. -- evidence: [README.md#L112-L115](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L112-L115), [README.md#L7-L12](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L7-L12)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The entry point is autonomous_agent_demo.py, invoked with --project-dir, with optional --max-iterations (default unlimited) and --model (default claude-opus-4-5-20251101) flags. -- evidence: [README.md#L58-L61](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L58-L61), [README.md#L54-L56](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L54-L56), [README.md#L126-L130](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L126-L130)
- memory-state (1 claim(s)):
  - [observation/documented] Generated projects contain a .linear_project.json marker file holding Linear project state, alongside the copied spec, init.sh, and .claude_settings.json security settings. -- evidence: [README.md#L154-L161](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L154-L161)
- orchestration (2 claim(s)):
  - [observation/documented] The initializer agent reads app_spec.txt, creates a Linear project, generates 50 detailed issues, creates a META issue for session tracking, and sets up project structure, init.sh, and git. -- evidence: [README.md#L187-L190](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L187-L190), [README.md#L93-L98](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L93-L98)
  - [observation/documented] The coding agent queries Linear for the highest-priority Todo issue, claims it, implements and tests the feature, comments on the issue, marks it Done, and updates the META issue with a session summary. -- evidence: [README.md#L100-L108](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L100-L108)
- tools-permissions (2 claim(s)):
  - [observation/documented] The runtime uses a defense-in-depth security model: OS-level sandboxing of bash commands, filesystem restrictions to the project directory, a bash command allowlist, and explicit MCP tool permissions. -- evidence: [README.md#L174-L177](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L174-L177), [README.md#L172-L172](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L172-L172)
  - [observation/documented] The bash allowlist permits only specific commands such as npm, node, and git, and is configurable via ALLOWED_COMMANDS in security.py. -- evidence: [README.md#L174-L177](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L174-L177), [README.md#L206-L206](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L206-L206), [README.md#L219-L220](https://github.com/coleam00/Linear-Coding-Agent-Harness/blob/c37dc096993011cb0cc48a0afab176cd9c8f2375/README.md#L219-L220)
- evaluation (1 claim(s)):
More evidence: [full detail](linear-coding-agent-harness.detail.md)

Metadata and full claim list: [full detail](linear-coding-agent-harness.detail.md)
Human notes ([notes](linear-coding-agent-harness.notes.md), never overwritten by build)

[Back to map index](../../index.md)
