---
access: public
aliases: []
claim_ids:
- clm_187d21c4871adfb1d833f955a812ec9f161514c38fb363b94ec46312d317ae6f
- clm_439511c98d56f73f7f7db548c6068e46ca99ea540692f2ea6a03813347666a16
- clm_70c6c2da4e267b54ea274e165b360112b852453fc8b413c8e11e036d055bcdb3
- clm_98441b90c9ba6b8d69b494593e6a869e75118b628af1caed10ad80d5afc72176
- clm_abe44b3c00221e3daa5aed1796b2d6f5c02df2133a80fdcc30b22bf4f7baf0c5
- clm_d2ab8a4f9033991bfa9270820bd1b6ae5562843ca4a543aef03676aa5f9ecc2d
maturity: draft
page_id: pg_9de8bd6c7d9257fb99ec985ec7c71819
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_175a0ce911c458ec9f58127bbf9fe95c
title: vocodedev/vocode-core/README.md @ e054c33a7278
updated_at: '2026-09-14T04:31:45Z'
---

# vocodedev/vocode-core/README.md @ e054c33a7278

<!-- rcw:begin owner=source:src_175a0ce911c458ec9f58127bbf9fe95c block=evidence -->
- Repository development practice: contributing is welcomed via a Contribution Guide and a roadmap file in the repo, with a Discord community for ideas and contributions, and the project seeks community maintainers. [@claim:clm_187d21c4871adfb1d833f955a812ec9f161514c38fb363b94ec46312d317ae6f]
- The quickstart configures settings (OpenAI, Azure, Deepgram keys) via pydantic-settings, overridable through environment variables or a .env file. [@claim:clm_439511c98d56f73f7f7db548c6068e46ca99ea540692f2ea6a03813347666a16]
- A StreamingConversation composes a transcriber (e.g. Deepgram with punctuation endpointing), an agent (e.g. ChatGPTAgent with prompt and initial message), and a synthesizer (e.g. Azure). [@claim:clm_70c6c2da4e267b54ea274e165b360112b852453fc8b413c8e11e036d055bcdb3]
- The library is installed via pip as the 'vocode' package and exposes a Python API including StreamingConversation, ChatGPTAgent, DeepgramTranscriber, and AzureSynthesizer. [@claim:clm_98441b90c9ba6b8d69b494593e6a869e75118b628af1caed10ad80d5afc72176]
- Documented out-of-the-box transcription integrations include AssemblyAI, Deepgram, Gladia, Google Cloud, Azure, RevAI, Whisper, and Whisper.cpp; LLM integrations include OpenAI and Anthropic. [@claim:clm_abe44b3c00221e3daa5aed1796b2d6f5c02df2133a80fdcc30b22bf4f7baf0c5]
- Vocode is an open source library for building voice-based LLM apps, supporting real-time streaming conversations deployable to phone calls, Zoom meetings, and more. [@claim:clm_d2ab8a4f9033991bfa9270820bd1b6ae5562843ca4a543aef03676aa5f9ecc2d]
<!-- rcw:end owner=source:src_175a0ce911c458ec9f58127bbf9fe95c block=evidence -->

## Researcher notes

