# ashish200729/orbiteditor

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6acd0c1e9ae0 @ 54376e9db6bf1f87

## Summary (orientation draft, not independently verified)

Orbit Editor is an open-source AI code editor forked from Void Editor/VS Code, with agent chat modes, subagents, MCP, skills, and checkpoints; evidence is mostly documentation (readme, codebase guide, contributing guide) rather than source code. Evidence coverage: 140 of 189 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 24 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 10 facet(s); 3 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] Most of Orbit's code lives in src/vs/workbench/contrib/orbit/, per the codebase guide and contributing doc. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L5-L5](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L5-L5), [HOW_TO_CONTRIBUTE.md#L19-L19](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/HOW_TO_CONTRIBUTE.md#L19-L19)
  - [observation/documented] The LLM pipeline spans chatThreadService (threads/streaming/checkpoints), convertToLLMMessageService, sendLLMMessage impl/channel, modelCapabilities, and orbitSettingsTypes. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L43-L50](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L43-L50)
- design-choices (2 claim(s)):
  - [observation/documented] LLM messages are sent from the Electron main process, which the guide says avoids CSP issues with local providers and eases node_modules use. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L15-L20](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L15-L20), [ORBIT_CODEBASE_GUIDE.md#L39-L39](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L39-L39)
  - [observation/documented] Apply has two modes: Fast Apply using Search/Replace blocks and Slow Apply that rewrites the whole file; Edit tool calls and Cmd+K reuse the same Apply machinery. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L72-L72](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L72-L72), [ORBIT_CODEBASE_GUIDE.md#L98-L100](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L98-L100), [ORBIT_CODEBASE_GUIDE.md#L88-L88](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L88-L88)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors use a Developer Mode flow (npm install, Ctrl+Shift+B build, scripts/code.sh) with Node 20.18.2 from .nvmrc, and PR guidelines ask contributors not to use AI to write pull requests. -- evidence: [HOW_TO_CONTRIBUTE.md#L141-L144](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/HOW_TO_CONTRIBUTE.md#L141-L144), [HOW_TO_CONTRIBUTE.md#L57-L70](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/HOW_TO_CONTRIBUTE.md#L57-L70), [HOW_TO_CONTRIBUTE.md#L76-L86](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/HOW_TO_CONTRIBUTE.md#L76-L86)
- skills-patterns (1 claim(s)):
  - [observation/documented] Skills are reusable instruction packs loaded on demand via a skill tool, sourced from built-in, user (~/.orbit/skills), and project (.orbit/skills) registries. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L139-L143](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L139-L143), [ORBIT_CODEBASE_GUIDE.md#L137-L137](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L137-L137)
- interfaces (1 claim(s)):
  - [observation/documented] Orbit defines three chat modes — agent, plan, normal — with a capability matrix differing in file edit, terminal, plan tools, MCP, and subagent access. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L62-L66](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L62-L66), [ORBIT_CODEBASE_GUIDE.md#L58-L60](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L58-L60)
- memory-state (1 claim(s)):
  - [observation/documented] Orbit snapshots file state before each user message and LLM edit, letting users restore checkpoints to roll back changes. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L163-L163](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L163-L163)
- orchestration (1 claim(s)):
  - [observation/documented] A subagent system lets the main agent delegate bounded tasks to isolated child agents with restricted tool policies that return structured summaries; built-ins include explore, plan, and general. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L121-L121](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L121-L121), [ORBIT_CODEBASE_GUIDE.md#L131-L131](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L131-L131)
- tools-permissions (1 claim(s)):
  - [observation/documented] MCP servers extend agent mode with extra tools, configured at ~/.orbit-editor/mcp.json, with a built-in orbit-ide-browser server exposing 17 tools and toggleable via browserAutomationEnabled. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L151-L151](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L151-L151), [ORBIT_CODEBASE_GUIDE.md#L147-L147](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L147-L147), [ORBIT_CODEBASE_GUIDE.md#L153-L157](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L153-L157)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](orbiteditor.detail.md)

Metadata and full claim list: [full detail](orbiteditor.detail.md)
Human notes ([notes](orbiteditor.notes.md), never overwritten by build)

[Back to map index](../../index.md)
