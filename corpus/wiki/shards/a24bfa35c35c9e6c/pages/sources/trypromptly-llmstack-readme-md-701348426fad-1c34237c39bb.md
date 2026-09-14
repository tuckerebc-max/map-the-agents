---
access: public
aliases: []
claim_ids:
- clm_095ad55b96737dda8ff00ba26ee48fb458e395c9c1c46fad3b962c61f8f6eb0a
- clm_0a07b35a56a0f57322a1746e31a04a4f7e830143b96e43f6fd478f995cae9dc2
- clm_19de94b7df26fb78e2f72291a875c2106afb07b7107ef650185350e90d97b751
- clm_2dbc34207ae0368104e2bfaa4082f44e4af937ff016853c7d24822901db97bb7
- clm_2e7e378454908a2f9c21b3f602996858fe362f51ac4a76ef9acd031cca1a8203
- clm_529ae893abf637d42048e603b9c207f5a9539308ae2a8d90d45978902fa8b581
- clm_82a5924e8a6fa220f2a908c991e5dd8c431f13a529bbedf7d6c64da678a2a9f8
- clm_8e1aa3539afa8ba79a52e218b04d1782046a15f40025fa56e8b28499655edd8c
- clm_c8b27b667a39b21f951c65d2b597d7138e39d239e276f981aeadcd774a76c82a
- clm_cacd7bafe2215e6c96412e95c28f83a6222ef60e1a6448fedf23ed21d62c4ddf
- clm_d3d6484d92e2e7a1cf870c0cc559980e188bbf86c0a5fa167538929ed9dcf09a
- clm_ff254f7fedafae0dca9ad21c52aee8e0c90cc659ec6760320653e55279297a32
maturity: draft
page_id: pg_9bc03928f89956f9ac001c34237c39bb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_44e60023ac6c5bbf96a13df01bbfb9d7
title: trypromptly/LLMStack/README.md @ 701348426fad
updated_at: '2026-09-14T04:27:54Z'
---

# trypromptly/LLMStack/README.md @ 701348426fad

<!-- rcw:begin owner=source:src_44e60023ac6c5bbf96a13df01bbfb9d7 block=evidence -->
- An admin panel at localhost:3000/admin lets administrators add users and assign them to organizations. [@claim:clm_095ad55b96737dda8ff00ba26ee48fb458e395c9c1c46fad3b962c61f8f6eb0a]
- Users can add provider API keys (e.g., OpenAI, Cohere, Stability) from the Settings page, and instance-wide default keys can be placed in ~/.llmstack/config. [@claim:clm_0a07b35a56a0f57322a1746e31a04a4f7e830143b96e43f6fd478f995cae9dc2]
- Running jobs requires a background Docker container, so Docker must be installed on the machine to use the jobs feature. [@claim:clm_19de94b7df26fb78e2f72291a875c2106afb07b7107ef650185350e90d97b751]
- On first run, LLMStack creates a .llmstack directory in the user's home containing the database and config files, and opens a browser to localhost:3000. [@claim:clm_2dbc34207ae0368104e2bfaa4082f44e4af937ff016853c7d24822901db97bb7]
- Repository development practice: the README points contributors to an external development guide and a contributing guide at docs.trypromptly.com for how to run, develop, and contribute to LLMStack. [@claim:clm_2e7e378454908a2f9c21b3f602996858fe362f51ac4a76ef9acd031cca1a8203]
- The platform imports data types such as CSV, TXT, PDF, DOCX, and PPTX from sources like Google Drive, Notion, websites, and uploads, then preprocesses and vectorizes it into an out-of-the-box vector database. [@claim:clm_529ae893abf637d42048e603b9c207f5a9539308ae2a8d90d45978902fa8b581]
- Apps and chatbots built with LLMStack are accessible via an HTTP API, and AI chains can be triggered from Slack or Discord. [@claim:clm_82a5924e8a6fa220f2a908c991e5dd8c431f13a529bbedf7d6c64da678a2a9f8]
- LLMStack is installed with 'pip install llmstack' and started with the 'llmstack' command; Windows users are directed to use WSL2. [@claim:clm_8e1aa3539afa8ba79a52e218b04d1782046a15f40025fa56e8b28499655edd8c]
- The platform lets users chain multiple LLMs together to build generative AI applications without coding, via a no-code builder. [@claim:clm_c8b27b667a39b21f951c65d2b597d7138e39d239e276f981aeadcd774a76c82a]
- LLMStack is multi-tenant: users can create multiple organizations, and users can only access data and AI chains belonging to their organization. [@claim:clm_cacd7bafe2215e6c96412e95c28f83a6222ef60e1a6448fedf23ed21d62c4ddf]
- LLMStack is described as a no-code platform for building generative AI agents, workflows, and chatbots that connect to data and business processes. [@claim:clm_d3d6484d92e2e7a1cf870c0cc559980e188bbf86c0a5fa167538929ed9dcf09a]
- A default admin account ships with credentials 'admin' and 'promptly', and the documentation instructs changing the password from the admin panel after login. [@claim:clm_ff254f7fedafae0dca9ad21c52aee8e0c90cc659ec6760320653e55279297a32]
<!-- rcw:end owner=source:src_44e60023ac6c5bbf96a13df01bbfb9d7 block=evidence -->

## Researcher notes

