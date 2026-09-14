# langlang03/linecodepro

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 247903d320ec @ cd6eed6d0012dec2

## Summary (orientation draft, not independently verified)

Evidence consists of the English and Chinese READMEs for LineCode Pro v1.2.8-max, an Android 8.0+ self-hosted AI coding assistant with a tool-call loop, multiple model protocols, SSH/IPC execution modes, and documented build/contribution workflows. Evidence coverage: 125 of 212 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 3 of 4 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] LineCode Pro targets Android 8.0+ (API 26), is at version 1.2.8-max, is written in Java 11, and is licensed GPL-3.0-or-later. -- evidence: [README.md#L430-L430](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L430-L430), [README.md#L10-L13](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L10-L13)
  - [observation/documented] The app id is cn.lineai and the project is a multi-module Gradle build with 14 modules plus :build-logic as a composite build. -- evidence: [README.md#L43-L43](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L43-L43)
- components (1 claim(s)):
  - [observation/documented] Architecture: a single MainActivity hosts MainCoordinator (presenter) delegating to per-concern MVP controllers, with UI state flowing through ChatUiStateAssembler to ChatUiState to the view. -- evidence: [README.md#L208-L212](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L208-L212)
- design-choices (1 claim(s)):
  - [observation/documented] The app is intentionally Java-only with no Kotlin runtime and no XML layouts, built entirely in Java 11 for transparency and reviewability. -- evidence: [README.md#L415-L420](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L415-L420), [README.md#L106-L115](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L106-L115)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors must keep app code pure Java (Kotlin stdlib excluded from the runtime classpath), place code in the lowest-level fitting module, and run testDebugUnitTest, lintDebug, assembleDebug, and assembleRelease gates before sending a PR. -- evidence: [README.md#L422-L424](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L422-L424), [README.md#L415-L420](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L415-L420)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] ModelProtocolFactory dispatches on four protocol types: OPENAI_COMPATIBLE, CODEX_RESPONSES, ANTHROPIC_MESSAGES, and LOCAL_GGUF, each declaring capabilities like native tools and image support. -- evidence: [README.md#L208-L212](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L208-L212), [README.md#L268-L273](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L268-L273)
  - [observation/documented] Tools implement a BaseTool contract exposing name, description, category, a JSON argument schema, and an execute(JSONObject, ToolContext) returning a ToolResult. -- evidence: [README.md#L281-L281](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L281-L281), [README.md#L283-L285](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L283-L285)
- memory-state (1 claim(s)):
  - [observation/documented] ContextCompactionService performs dynamic compaction at 50% (summarizing oldest 70%, keeping recent 30%) and 80% hard triggers, and durable knowledge saved via memory_update is reinjected next session. -- evidence: [README.md#L76-L79](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L76-L79), [README.md#L51-L57](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L51-L57)
- orchestration (1 claim(s)):
  - [observation/documented] Sub-agent tools (agent, agent_pipeline, agent_output) delegate work to another LLM loop, rendered with live progress cards. -- evidence: [README.md#L90-L91](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L90-L91), [README.md#L63-L70](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L63-L70)
- tools-permissions (2 claim(s)):
  - [observation/documented] Every file-touching tool routes paths through FileToolPathPolicy so the model acts only inside the opened workspace; shell commands run via Termux or an IPC provider, never in the app process. -- evidence: [README.md#L72-L72](https://github.com/LangLang03/LineCodePro/blob/247903d320ec126d9e7540f658527d743572c1ac/README.md#L72-L72)
More evidence: [full detail](linecodepro.detail.md)

Metadata and full claim list: [full detail](linecodepro.detail.md)
Human notes ([notes](linecodepro.notes.md), never overwritten by build)

[Back to map index](../../index.md)
