# vocodedev/vocode-core -- full detail

[Back to orientation](vocode-core.md)

## Origins

- github-verified-rename
- alltheagents.org-backing

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/vocodedev/vocode-core/e054c33a72787b6a4920f91eb8598ad0bafb4240/2171ee039aec7f17.json](../../../wiki/dossiers/vocodedev/vocode-core/e054c33a72787b6a4920f91eb8598ad0bafb4240/2171ee039aec7f17.json)

## specifications (1 claim(s))

- [observation/documented] Vocode is an open source library for building voice-based LLM apps, supporting real-time streaming conversations deployable to phone calls, Zoom meetings, and more. -- evidence: [README.md#L17-L17](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L17-L17) (`clm_d2ab8a4f9033991bfa9270820bd1b6ae5562843ca4a543aef03676aa5f9ecc2d`)

## components (2 claim(s))

- [observation/documented] A StreamingConversation composes a transcriber (e.g. Deepgram with punctuation endpointing), an agent (e.g. ChatGPTAgent with prompt and initial message), and a synthesizer (e.g. Azure). -- evidence: [README.md#L127-L154](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L127-L154) (`clm_70c6c2da4e267b54ea274e165b360112b852453fc8b413c8e11e036d055bcdb3`)
- [observation/documented] The quickstart configures settings (OpenAI, Azure, Deepgram keys) via pydantic-settings, overridable through environment variables or a .env file. -- evidence: [README.md#L101-L103](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L101-L103), [README.md#L95-L99](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L95-L99), [README.md#L107-L113](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L107-L113) (`clm_439511c98d56f73f7f7db548c6068e46ca99ea540692f2ea6a03813347666a16`)

## design-choices (2 claim(s))

- [observation/documented] Actions fire via two trigger mechanisms: the default FunctionCallActionTrigger, where the agent decides based on prompting, or PhraseBasedActionTrigger, which fires after the bot speaks a configured phrase. -- evidence: [docs/action-triggers.mdx#L8-L8](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/action-triggers.mdx#L8-L8), [docs/action-triggers.mdx#L64-L66](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/action-triggers.mdx#L64-L66), [docs/actions.mdx#L8-L9](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/actions.mdx#L8-L9) (`clm_14a69fd5e9aa4cdfe323c078de6e61ff61da7e610e14ecc091c1802b026f5609`)
- [observation/documented] The only supported phrase-trigger condition type is 'phrase_condition_type_contains', which matches case-insensitively against the bot's spoken turn. -- evidence: [docs/action-triggers.mdx#L39-L39](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/action-triggers.mdx#L39-L39) (`clm_cf11b136c8a82144e1ff2886eb3c9d6bc424ece6fa771e12d775b2f509b03dce`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributing is welcomed via a Contribution Guide and a roadmap file in the repo, with a Discord community for ideas and contributions, and the project seeks community maintainers. -- evidence: [README.md#L19-L19](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L19-L19), [README.md#L64-L64](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L64-L64), [README.md#L60-L60](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L60-L60), [README.md#L58-L58](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L58-L58), [README.md#L62-L62](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L62-L62) (`clm_187d21c4871adfb1d833f955a812ec9f161514c38fb363b94ec46312d317ae6f`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The library is installed via pip as the 'vocode' package and exposes a Python API including StreamingConversation, ChatGPTAgent, DeepgramTranscriber, and AzureSynthesizer. -- evidence: [README.md#L78-L90](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L78-L90), [README.md#L68-L70](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L68-L70), [README.md#L127-L154](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L127-L154) (`clm_98441b90c9ba6b8d69b494593e6a869e75118b628af1caed10ad80d5afc72176`)
- [observation/documented] A hosted REST API at api.vocode.dev exposes endpoints such as /v1/actions/create and /v1/numbers/update with Bearer-token authentication, shown in Python, TypeScript, and cURL examples. -- evidence: [docs/actions.mdx#L133-L140](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/actions.mdx#L133-L140), [docs/actions.mdx#L19-L25](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/actions.mdx#L19-L25), [docs/actions.mdx#L27-L31](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/actions.mdx#L27-L31), [docs/actions.mdx#L125-L131](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/actions.mdx#L125-L131), [docs/actions.mdx#L33-L41](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/actions.mdx#L33-L41), [docs/actions.mdx#L142-L152](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/actions.mdx#L142-L152) (`clm_0df76e340b358da39d08cadc318614a1b41ebf0703fbb54750ca874f4ea62313`)
- [observation/documented] An Enterprise-plan feature lets users connect their own OpenAI account via account connections and use custom or fine-tuned models through an openai_model_name_override agent parameter. -- evidence: [docs/bring-your-own-openai.mdx#L61-L61](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/bring-your-own-openai.mdx#L61-L61), [docs/bring-your-own-openai.mdx#L63-L63](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/bring-your-own-openai.mdx#L63-L63), [docs/bring-your-own-openai.mdx#L1-L4](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/bring-your-own-openai.mdx#L1-L4), [docs/bring-your-own-openai.mdx#L8-L8](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/bring-your-own-openai.mdx#L8-L8) (`clm_6000df28c4541a07313c0709c13ea804fbe26c3976299baa511f074dcf54a23c`)
- [observation/documented] An Enterprise-plan feature lets users link their own Twilio accounts and phone numbers via a /v1/numbers/link endpoint, with call objects exposing telephonyId and telephonyAccountConnection fields. -- evidence: [docs/bring-your-own-telephony.mdx#L33-L33](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/bring-your-own-telephony.mdx#L33-L33), [docs/bring-your-own-telephony.mdx#L8-L8](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/bring-your-own-telephony.mdx#L8-L8), [docs/bring-your-own-telephony.mdx#L48-L50](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/bring-your-own-telephony.mdx#L48-L50), [docs/bring-your-own-telephony.mdx#L1-L4](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/docs/bring-your-own-telephony.mdx#L1-L4) (`clm_d13bc45e636bd6fcc0afb3daab02ea904f35b262a1e7d2311e8426ecc31e7597`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Documented out-of-the-box transcription integrations include AssemblyAI, Deepgram, Gladia, Google Cloud, Azure, RevAI, Whisper, and Whisper.cpp; LLM integrations include OpenAI and Anthropic. -- evidence: [README.md#L23-L52](https://github.com/vocodedev/vocode-core/blob/e054c33a72787b6a4920f91eb8598ad0bafb4240/README.md#L23-L52) (`clm_abe44b3c00221e3daa5aed1796b2d6f5c02df2133a80fdcc30b22bf4f7baf0c5`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

