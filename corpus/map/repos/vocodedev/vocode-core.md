# vocodedev/vocode-core

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: github-verified-rename, alltheagents.org-backing - Projects: Observatory
Formerly: vocodedev/vocode-python (github id 606164768).
Latest snapshot: commit e054c33a7278 @ 2171ee039aec7f17

## Summary (orientation draft, not independently verified)

Selected evidence records: Vocode is an open source library for building voice-based LLM apps, supporting real-time streaming conversations deployable to phone calls, Zoom meetings, and more. The library is installed via pip as the 'vocode' package and exposes a Python API including StreamingConversation, ChatGPTAgent, DeepgramTranscriber, and AzureSynthesizer.

## Source coverage

Source coverage (partial): 6 of 104 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Vocode is an open source library for building voice-based LLM apps, supporting real-time streaming conversations deployable to phone calls, Zoom meetings, and more. -- evidence: [README.md#L17-L17](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L17-L17)
- components (2 claim(s)):
  - [observation/documented] A StreamingConversation composes a transcriber (e.g. Deepgram with punctuation endpointing), an agent (e.g. ChatGPTAgent with prompt and initial message), and a synthesizer (e.g. Azure). -- evidence: [README.md#L127-L154](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L127-L154)
  - [observation/documented] The quickstart configures settings (OpenAI, Azure, Deepgram keys) via pydantic-settings, overridable through environment variables or a .env file. -- evidence: [README.md#L101-L103](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L101-L103), [README.md#L95-L99](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L95-L99), [README.md#L107-L113](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L107-L113)
- design-choices (2 claim(s)):
  - [observation/documented] Actions fire via two trigger mechanisms: the default FunctionCallActionTrigger, where the agent decides based on prompting, or PhraseBasedActionTrigger, which fires after the bot speaks a configured phrase. -- evidence: [docs/action-triggers.mdx#L8-L8](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/action-triggers.mdx#L8-L8), [docs/action-triggers.mdx#L64-L66](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/action-triggers.mdx#L64-L66), [docs/actions.mdx#L8-L9](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/actions.mdx#L8-L9)
  - [observation/documented] The only supported phrase-trigger condition type is 'phrase_condition_type_contains', which matches case-insensitively against the bot's spoken turn. -- evidence: [docs/action-triggers.mdx#L39-L39](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/action-triggers.mdx#L39-L39)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributing is welcomed via a Contribution Guide and a roadmap file in the repo, with a Discord community for ideas and contributions, and the project seeks community maintainers. -- evidence: [README.md#L19-L19](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L19-L19), [README.md#L64-L64](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L64-L64), [README.md#L60-L60](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L60-L60), [README.md#L58-L58](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L58-L58), [README.md#L62-L62](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L62-L62)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The library is installed via pip as the 'vocode' package and exposes a Python API including StreamingConversation, ChatGPTAgent, DeepgramTranscriber, and AzureSynthesizer. -- evidence: [README.md#L78-L90](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L78-L90), [README.md#L68-L70](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L68-L70), [README.md#L127-L154](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L127-L154)
  - [observation/documented] A hosted REST API at api.vocode.dev exposes endpoints such as /v1/actions/create and /v1/numbers/update with Bearer-token authentication, shown in Python, TypeScript, and cURL examples. -- evidence: [docs/actions.mdx#L133-L140](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/actions.mdx#L133-L140), [docs/actions.mdx#L19-L25](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/actions.mdx#L19-L25), [docs/actions.mdx#L27-L31](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/actions.mdx#L27-L31), [docs/actions.mdx#L125-L131](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/actions.mdx#L125-L131), [docs/actions.mdx#L33-L41](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/actions.mdx#L33-L41), [docs/actions.mdx#L142-L152](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/actions.mdx#L142-L152)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Documented out-of-the-box transcription integrations include AssemblyAI, Deepgram, Gladia, Google Cloud, Azure, RevAI, Whisper, and Whisper.cpp; LLM integrations include OpenAI and Anthropic. -- evidence: [README.md#L23-L52](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L23-L52)
- limitations: unknown (no source-linked claim submitted for this facet)
More evidence: [full detail](vocode-core.detail.md)

Metadata and full claim list: [full detail](vocode-core.detail.md)
Human notes ([notes](vocode-core.notes.md), never overwritten by build)

[Back to map index](../../index.md)
