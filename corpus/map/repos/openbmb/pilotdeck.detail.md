# openbmb/pilotdeck -- full detail

[Back to orientation](pilotdeck.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/openbmb/pilotdeck/97633a08a73eca3d65c79494f9aa31cc18fd019f/2d0f9ca69f85ae00.json](../../../wiki/dossiers/openbmb/pilotdeck/97633a08a73eca3d65c79494f9aa31cc18fd019f/2d0f9ca69f85ae00.json)

## specifications (1 claim(s))

- [observation/documented] PilotDeck is an open-source agent operating system organized around a 'WorkSpace' concept, jointly developed by THUNLP, ModelBest, OpenBMB, and AI9Stars, targeting general-purpose multi-task scenarios. -- evidence: [README.md#L42-L42](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L42-L42) (`clm_353d9a7d81fda036d67aa24bbca27f16df3d8c815e80f383cdcc589a5cb11f7e`)

## components (1 claim(s))

- [observation/documented] An open plugin architecture separates the open-source core from plugin customization, supporting MCP servers, custom tools and skills, lifecycle hooks such as PreToolUse and UserPromptSubmit, and pluggable memory store providers. -- evidence: [README.md#L479-L479](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L479-L479), [README.md#L481-L484](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L481-L484) (`clm_dffb020f6f5d6e1f8ada354fc07232594384f67d49a0e9626e78b0713830f1bf`)

## design-choices (1 claim(s))

- [observation/documented] The WorkSpace is the fundamental isolation unit: each project gets its own file system, memory store, and skill set, so parallel work does not interfere and retrieval stays scoped. -- evidence: [README.md#L63-L63](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L63-L63), [README.md#L53-L53](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L53-L53) (`clm_330c7d586383df4b4d3f15f05bb7ed63bc959977788cd8f00361dc0437651d4a`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributions follow a fork, feature branch, and pull-request workflow, and bugs or feature requests go through GitHub Issues. -- evidence: [README.md#L492-L492](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L492-L492), [README.md#L498-L499](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L498-L499) (`clm_0f1b91cc92b93d26e096484baf5445f4dc5bd6b1aebf80fb42557d110037cd1a`)
- [observation/documented] Repository development practice: source installs use corepack pnpm with a committed pnpm-lock.yaml and workspace filters, and Git LFS demo media is skipped by default for a lightweight clone. -- evidence: [README.md#L388-L388](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L388-L388), [README.md#L399-L399](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L399-L399), [README.md#L394-L397](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L394-L397) (`clm_7f1d60229243aa44a3a735bef6e286a2059571f7dd5c510c5a9e8bf18861b637`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The system natively supports the Model Context Protocol (MCP) and is described as behaving consistently across Web, CLI, and IM front-ends. -- evidence: [README.md#L53-L53](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L53-L53) (`clm_1514bca954507da6077cc47dfe99e0c4746f3602a85cbf7aa8e46ad417177ecf`)
- [observation/documented] PilotDeck ships a Web UI with WorkSpace management, white-box memory editing, and visualization of multi-agent collaboration; the 'pilotdeck' command starts the server at http://localhost:3001. -- evidence: [README.md#L221-L221](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L221-L221), [README.md#L315-L318](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L315-L318) (`clm_c49998f58098f61fcbb321b230105bd82a5b7f69bed7607b0bd060939eff54eb`)
- [observation/documented] Configuration is read from ~/.pilotdeck/pilotdeck.yaml; if the file is missing, the Web UI starts without the Gateway, and saving a valid provider and key writes the config and starts the Gateway automatically. -- evidence: [README.md#L403-L404](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L403-L404), [README.md#L406-L406](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L406-L406) (`clm_6524358f8ea020f90c44269c575966149d3434d89aee58b1e6133b3ae65c0c51`)

## memory-state (1 claim(s))

- [observation/documented] Memory is white-box and traceable: generation, extraction, storage, and retrieval are visible, entries can be edited or deleted, and a Dream Mode consolidates memory in idle windows with one-click rollback. -- evidence: [README.md#L180-L215](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L180-L215), [README.md#L74-L74](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L74-L74) (`clm_80c3f6bbe92b22ca892cc8aa682d73d0d7e22c2e5333ed8efdc9fc95a2b26f91`)

## orchestration (2 claim(s))

- [observation/documented] Smart Routing auto-detects task difficulty and sends complex calls to flagship models while simple tasks go to lighter sub-agent models, aiming to reduce token cost. -- evidence: [README.md#L87-L87](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L87-L87) (`clm_3fca21040a10f86abb1ad201431e9a5425c52d01470b0fb53b7b7516b4e47214`)
- [observation/documented] The system supports always-on background execution: after the user signs off, the agent continues discovering tasks, running long-horizon monitors, and writing deliverables as local files with a summary report. -- evidence: [README.md#L98-L98](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L98-L98) (`clm_990900e6c75a742ff4b2374cdf41f966989cdd96f3cedc57301a713e5a858d37`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The README reports benchmarks: on 7 complex tasks, a Sonnet 4.6 main plus MiniMax-M2.7 sub setup scored 70.6 at $3.15 versus 69.1 at $18.36 for a Sonnet 4.6 single agent, and Smart Routing cut a social-media workload's cost from $12.58 to $2.83. -- evidence: [README.md#L148-L148](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L148-L148), [README.md#L150-L174](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L150-L174), [README.md#L114-L114](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L114-L114), [README.md#L116-L144](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L116-L144) (`clm_46f587a7b683a4f1df69d9c6499f7610eaf58734ad6090d611497fbaec330ea4`)

## dependencies (2 claim(s))

- [observation/documented] The installer requires Node.js 22.13+ and below v23 for the built-in SQLite runtime, and the Windows installer checks node:sqlite support and uses prebuilt native packages such as node-pty, better-sqlite3, bcrypt, and sharp. -- evidence: [README.md#L335-L335](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L335-L335), [README.md#L303-L303](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L303-L303), [README.md#L376-L376](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L376-L376) (`clm_29121366b984960178770f2b86797f3182694daa76db2f8371223a4b1998b4fa`)
- [observation/documented] Supported model provider protocols include OpenAI, Anthropic, native Google Gemini, DeepSeek, Qwen, Kimi, MiniMax, and other OpenAI-compatible endpoints, including local Ollama without an API key. -- evidence: [README.md#L436-L437](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L436-L437), [README.md#L403-L404](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L403-L404) (`clm_f841e2cca6472ab1ed2a2f8332dcb4a371dc86a91bb4e88bd3249d259d920201`)

## limitations (1 claim(s))

- [observation/documented] The project is licensed under the GNU Affero General Public License v3.0. -- evidence: [README.md#L564-L564](https://github.com/OpenBMB/PilotDeck/blob/97633a08a73eca3d65c79494f9aa31cc18fd019f/README.md#L564-L564) (`clm_f68da8f92fe9fcafcc131e07be048059a7e17c7092b7a4adbb49ff6227598d5a`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

