---
access: public
aliases: []
claim_ids:
- clm_22e53c0df0dbc699689299f26bb9bfa8ee848755b0fbb7f7092597f9a362ffb7
- clm_3745db136312b68cb39333b6f9539ad8882c82a20a2d1ad0bf7b757e9a07c9ea
- clm_46f2b966e1746f8d27133217200ad2398e2a57f4088e6650b3caf89747da31fc
- clm_6c25410aa4145661b46467d1e9135cf0aec4e4d2d82efaca0f242da2c8c57173
- clm_8f807df959a3eb7fd4db477965219320e493f8917fc87958dafd653ae9f6ac59
- clm_980fd1e6782178c00af303b83b33d0c86f9200650be8081bf8168062765eecd0
- clm_a75511beb25b34f32b212d997afee17d4c6dc290d70d1abe5580445c5012d57e
- clm_fc16f955102927f6a6e2cac42dc5e1cb985819da37a53d146ef028066536bcef
maturity: draft
page_id: pg_5de9e841ea1359179c83d0119519aa58
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_754ec9c4306750ea870916b123fe40af
title: aduermael/herm/README.md @ 4bcb16ba05da
updated_at: '2026-09-14T01:29:52Z'
---

# aduermael/herm/README.md @ 4bcb16ba05da

<!-- rcw:begin owner=source:src_754ec9c4306750ea870916b123fe40af block=evidence -->
- Herm extends container environments by writing Dockerfiles dynamically, with environments scoped per project (the current working directory). [@claim:clm_22e53c0df0dbc699689299f26bb9bfa8ee848755b0fbb7f7092597f9a362ffb7]
- Repository development practice: the README points contributors to CONTRIBUTING.md for setup, tests, CI checks, coding standards, and pull request expectations, and CI badges cover test, prompt-length, and ci-checks GitHub Actions workflows. [@claim:clm_3745db136312b68cb39333b6f9539ad8882c82a20a2d1ad0bf7b757e9a07c9ea]
- The CLI supports multiple providers (Anthropic, OpenAI, Gemini, Grok, OpenRouter, Ollama, Azure OpenAI, Vertex AI, Bedrock) and models can be mixed, e.g. a different model for the main agent, exploration, or vision. [@claim:clm_46f2b966e1746f8d27133217200ad2398e2a57f4088e6650b3caf89747da31fc]
- Herm is described as a model-agnostic, general-purpose AI agent built for safe, flexible execution, natively supporting multiple isolation methods including containers, in-process Unix-like sandboxes, and host sandboxes such as sandbox_exec on macOS or bubblewrap on Linux. [@claim:clm_6c25410aa4145661b46467d1e9135cf0aec4e4d2d82efaca0f242da2c8c57173]
- The repository also contains a SwiftUI iOS/macOS app that uses an in-process Unix-like sandbox and a Luau-scriptable runtime for on-device tasks; it is not usable as a coding agent in that context and is not yet on the App Store. [@claim:clm_8f807df959a3eb7fd4db477965219320e493f8917fc87958dafd653ae9f6ac59]
- Building from source requires Go 1.24+ and, for the default container backend, Docker; the repo uses git submodules (langdag for LLM client/orchestration and cpsl for the native sandbox backend) that must be initialized before building. [@claim:clm_980fd1e6782178c00af303b83b33d0c86f9200650be8081bf8168062765eecd0]
- By default the CLI runs the agent inside Docker containers that can only access files from the current working directory, with no permission prompts. [@claim:clm_a75511beb25b34f32b212d997afee17d4c6dc290d70d1abe5580445c5012d57e]
- Benchmarking Herm against coding agents such as Claude Code, Codex, and Grok Build is listed as the top roadmap item, i.e. planned rather than an existing evaluation harness. [@claim:clm_fc16f955102927f6a6e2cac42dc5e1cb985819da37a53d146ef028066536bcef]
<!-- rcw:end owner=source:src_754ec9c4306750ea870916b123fe40af block=evidence -->

## Researcher notes

