# ashish200729/orbiteditor -- full detail

[Back to orientation](orbiteditor.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ashish200729/orbiteditor/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/54376e9db6bf1f87.json](../../../wiki/dossiers/ashish200729/orbiteditor/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/54376e9db6bf1f87.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Most of Orbit's code lives in src/vs/workbench/contrib/orbit/, per the codebase guide and contributing doc. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L5-L5](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L5-L5), [HOW_TO_CONTRIBUTE.md#L19-L19](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/HOW_TO_CONTRIBUTE.md#L19-L19) (`clm_7e1a43cb0f6aa65928d780e7926c044503100635297dbcfdd2da5e0786e2c98c`)
- [observation/documented] The LLM pipeline spans chatThreadService (threads/streaming/checkpoints), convertToLLMMessageService, sendLLMMessage impl/channel, modelCapabilities, and orbitSettingsTypes. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L43-L50](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L43-L50) (`clm_334e25b38984fe51b970be6520c331b9564a32f283547b38c3286e57e0ea24c0`)

## design-choices (2 claim(s))

- [observation/documented] LLM messages are sent from the Electron main process, which the guide says avoids CSP issues with local providers and eases node_modules use. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L15-L20](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L15-L20), [ORBIT_CODEBASE_GUIDE.md#L39-L39](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L39-L39) (`clm_e0c648a2e274629352267e907dfdaaffb1b847ab05064ee71cd6d0d72e48d32d`)
- [observation/documented] Apply has two modes: Fast Apply using Search/Replace blocks and Slow Apply that rewrites the whole file; Edit tool calls and Cmd+K reuse the same Apply machinery. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L72-L72](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L72-L72), [ORBIT_CODEBASE_GUIDE.md#L98-L100](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L98-L100), [ORBIT_CODEBASE_GUIDE.md#L88-L88](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L88-L88) (`clm_e82f2b87b0e646cd29f287d5d63d68542d6c190229d9c0f21a1384a9a8fd2a25`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors use a Developer Mode flow (npm install, Ctrl+Shift+B build, scripts/code.sh) with Node 20.18.2 from .nvmrc, and PR guidelines ask contributors not to use AI to write pull requests. -- evidence: [HOW_TO_CONTRIBUTE.md#L141-L144](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/HOW_TO_CONTRIBUTE.md#L141-L144), [HOW_TO_CONTRIBUTE.md#L57-L70](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/HOW_TO_CONTRIBUTE.md#L57-L70), [HOW_TO_CONTRIBUTE.md#L76-L86](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/HOW_TO_CONTRIBUTE.md#L76-L86) (`clm_89351dfdc4354c2145b1ccfc60282563df32bcd41a818694c08f04058f06116b`)

## skills-patterns (1 claim(s))

- [observation/documented] Skills are reusable instruction packs loaded on demand via a skill tool, sourced from built-in, user (~/.orbit/skills), and project (.orbit/skills) registries. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L139-L143](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L139-L143), [ORBIT_CODEBASE_GUIDE.md#L137-L137](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L137-L137) (`clm_0a06aad296b9046fe8f2d030107618997089cf5fc5e61b4cdca1c40c401bb1a5`)

## interfaces (1 claim(s))

- [observation/documented] Orbit defines three chat modes — agent, plan, normal — with a capability matrix differing in file edit, terminal, plan tools, MCP, and subagent access. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L62-L66](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L62-L66), [ORBIT_CODEBASE_GUIDE.md#L58-L60](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L58-L60) (`clm_b672104f8c674fb6231b51f1fdf4820d1d8d6fdfb546f748947e7a12dff25716`)

## memory-state (1 claim(s))

- [observation/documented] Orbit snapshots file state before each user message and LLM edit, letting users restore checkpoints to roll back changes. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L163-L163](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L163-L163) (`clm_8ffae93eac7cf6da6818754083bf8106b27c9d55ae0f439ddef72c91c3d9e1ff`)

## orchestration (1 claim(s))

- [observation/documented] A subagent system lets the main agent delegate bounded tasks to isolated child agents with restricted tool policies that return structured summaries; built-ins include explore, plan, and general. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L121-L121](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L121-L121), [ORBIT_CODEBASE_GUIDE.md#L131-L131](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L131-L131) (`clm_fd150437a2d27656e73624d9d5998cbc985f63e55200bcb462f4ad6cfbb6d643`)

## tools-permissions (1 claim(s))

- [observation/documented] MCP servers extend agent mode with extra tools, configured at ~/.orbit-editor/mcp.json, with a built-in orbit-ide-browser server exposing 17 tools and toggleable via browserAutomationEnabled. -- evidence: [ORBIT_CODEBASE_GUIDE.md#L151-L151](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L151-L151), [ORBIT_CODEBASE_GUIDE.md#L147-L147](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L147-L147), [ORBIT_CODEBASE_GUIDE.md#L153-L157](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/ORBIT_CODEBASE_GUIDE.md#L153-L157) (`clm_7c408b454ab80018c5ec9d03ceba53567f3f6a962f5354f4aa049672830e7dda`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Orbit is a fork of Void Editor, itself a fork of VS Code; additions are Apache 2.0 while the VS Code base remains MIT. -- evidence: [readme.md#L86-L86](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/readme.md#L86-L86), [readme.md#L88-L88](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/readme.md#L88-L88), [LICENSE-VS-Code.txt#L1-L2](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/LICENSE-VS-Code.txt#L1-L2), [readme.md#L65-L65](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/readme.md#L65-L65) (`clm_19b15ed3b38521c10eaaef69b1b71e041722d6b68c2429aa243717b6585f2356`)

## limitations (1 claim(s))

- [observation/documented] The product is in beta and available only for macOS (Apple Silicon and Intel); Windows and Linux support is stated as coming soon. -- evidence: [readme.md#L36-L36](https://github.com/ashish200729/orbiteditor/blob/6acd0c1e9ae08fc11f0ab7abacfb22c892a75b6c/readme.md#L36-L36) (`clm_7c41acae6aed8b3f0e957d919e859eb0d7851133a9c3960e5b8dfca6c5f4b74b`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

