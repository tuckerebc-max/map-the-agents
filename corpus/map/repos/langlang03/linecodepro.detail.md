# langlang03/linecodepro -- full detail

[Back to orientation](linecodepro.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/langlang03/linecodepro/247903d320ec126d9e7540f658527d743572c1ac/cd6eed6d0012dec2.json](../../../wiki/dossiers/langlang03/linecodepro/247903d320ec126d9e7540f658527d743572c1ac/cd6eed6d0012dec2.json)

## specifications (2 claim(s))

- [observation/documented] LineCode Pro targets Android 8.0+ (API 26), is at version 1.2.8-max, is written in Java 11, and is licensed GPL-3.0-or-later. -- evidence: [README.md#L430-L430](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L430-L430), [README.md#L10-L13](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L10-L13) (`clm_4b5ebea99320ed718e66d8f900d41efa354c0574b40e587630488f157593c4fc`)
- [observation/documented] The app id is cn.lineai and the project is a multi-module Gradle build with 14 modules plus :build-logic as a composite build. -- evidence: [README.md#L43-L43](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L43-L43) (`clm_87d9a52f336a0ea000f24aae8c24b78cce48bd0b19a6d5e3a29bda873a1fde1c`)

## components (1 claim(s))

- [observation/documented] Architecture: a single MainActivity hosts MainCoordinator (presenter) delegating to per-concern MVP controllers, with UI state flowing through ChatUiStateAssembler to ChatUiState to the view. -- evidence: [README.md#L208-L212](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L208-L212) (`clm_748c5d52147da8c644d03b84bf835b940dc7c0ef05a3f991661d82c2213c5e04`)

## design-choices (1 claim(s))

- [observation/documented] The app is intentionally Java-only with no Kotlin runtime and no XML layouts, built entirely in Java 11 for transparency and reviewability. -- evidence: [README.md#L415-L420](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L415-L420), [README.md#L106-L115](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L106-L115) (`clm_4bd3d2626c543b4d832986c940672ceafcb84cf531591ab66600be1de30d2890`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors must keep app code pure Java (Kotlin stdlib excluded from the runtime classpath), place code in the lowest-level fitting module, and run testDebugUnitTest, lintDebug, assembleDebug, and assembleRelease gates before sending a PR. -- evidence: [README.md#L422-L424](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L422-L424), [README.md#L415-L420](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L415-L420) (`clm_44d2ebc2ec9121517ca04b2c3495f1b3a668c5cdf0a4c1098865e8d6e0e7b62a`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] ModelProtocolFactory dispatches on four protocol types: OPENAI_COMPATIBLE, CODEX_RESPONSES, ANTHROPIC_MESSAGES, and LOCAL_GGUF, each declaring capabilities like native tools and image support. -- evidence: [README.md#L208-L212](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L208-L212), [README.md#L268-L273](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L268-L273) (`clm_8c83d89a469af673baa1ef432d34bca764201e076df54f16c19633d969dc0edb`)
- [observation/documented] Tools implement a BaseTool contract exposing name, description, category, a JSON argument schema, and an execute(JSONObject, ToolContext) returning a ToolResult. -- evidence: [README.md#L281-L281](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L281-L281), [README.md#L283-L285](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L283-L285) (`clm_30069f15275d452ed3adeef6ab067285c2c290ebdf32ff136a404f2153bab3b5`)

## memory-state (1 claim(s))

- [observation/documented] ContextCompactionService performs dynamic compaction at 50% (summarizing oldest 70%, keeping recent 30%) and 80% hard triggers, and durable knowledge saved via memory_update is reinjected next session. -- evidence: [README.md#L76-L79](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L76-L79), [README.md#L51-L57](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L51-L57) (`clm_bfc1e9a3eeb768e83b78b3d782ee10fb82ce983ac61bf14b7881d94adba72995`)

## orchestration (1 claim(s))

- [observation/documented] Sub-agent tools (agent, agent_pipeline, agent_output) delegate work to another LLM loop, rendered with live progress cards. -- evidence: [README.md#L90-L91](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L90-L91), [README.md#L63-L70](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L63-L70) (`clm_5a97c930329a34a01bf7a27ab18273bc4361840f9a66e0d1b3d119d9bcfc7763`)

## tools-permissions (2 claim(s))

- [observation/documented] Every file-touching tool routes paths through FileToolPathPolicy so the model acts only inside the opened workspace; shell commands run via Termux or an IPC provider, never in the app process. -- evidence: [README.md#L72-L72](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L72-L72) (`clm_60ab6a9b3954be0be934d350a18f67118469a553e7673c08d5f8e233f6cb3f8f`)
- [observation/documented] Tool calls pass through PermissionModeController with automatic, confirmation, and read-only modes; confirmation supports one-time or persistent exact-match permissions scoped by mode, tool, command, and working directory. -- evidence: [README.md#L296-L296](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L296-L296) (`clm_8d4c9acef5f939d6a6a664d9a038df0af9e30ea159ce3c01c315a1e02a8f7508`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Third-party libraries include jsch for SSH, commonmark (BSD-2) for Markdown rendering, and org.json (JSON License); tests use JUnit 4 and Robolectric 4.16. -- evidence: [README.md#L340-L340](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L340-L340), [README.md#L448-L448](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L448-L448), [README.md#L415-L420](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L415-L420) (`clm_cfd2231eaf340e692b62500ab7b3fdfd026e46bc7d121ceefe8590be1a667b87`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

