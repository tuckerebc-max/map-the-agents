---
access: public
aliases: []
claim_ids:
- clm_03a7158d89e6bacf74bd5b958629670b055c8180ab8496acbc559e9706606918
- clm_78145070fba69f2d173d5a216dca54c3329b9c27dd660f8d03730ea3b7613bd9
- clm_8b82a09e4e018106e3a4669f45a48ac1782f2f47ab0ae029df06319b6299ad91
- clm_c527cd885acece952ead5836dcc5051135f126b3c9a9e85f92015429de1d6baf
- clm_cbea6b719deefdd1e687304fd00b32e40375e52d034d5ad81e5605f34c067c49
- clm_d1cc5dadf9eb1d6e5dffebd7572c3d6e16b487a6f3aaf1961c60b243e2550b03
- clm_db369e10891cc1804f16eabb655f543d6c0f68789c639ecca92ea63a26f48b2c
- clm_ee21edf5f502abee4183d2bf0cbf5db3d7512f0ac7cea0c5745a43b7c443c4d1
- clm_fb941bb5e91e20baa0148d463c45ba18af0ed02c88388be7e11fba5b5c186d21
maturity: draft
page_id: pg_70f4e979f20d58009f63818de3767e24
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_32ea4d56ab1a52db8960f0035c9b095f
title: Aider-AI/aider/HISTORY.md @ 5dc9490bb35f
updated_at: '2026-09-14T01:31:25Z'
---

# Aider-AI/aider/HISTORY.md @ 5dc9490bb35f

<!-- rcw:begin owner=source:src_32ea4d56ab1a52db8960f0035c9b095f block=evidence -->
- Aider supports multiple edit formats per model family, including diff, udiff-simple, patch, editor-diff, editor-whole and editor-diff-fenced, and can auto-select the best format in architect mode. [@claim:clm_03a7158d89e6bacf74bd5b958629670b055c8180ab8496acbc559e9706606918]
- Model-specific behaviors are configurable: thinking-tokens and reasoning-effort settings, temperature disabling for GPT-5 models, and per-model weak/editor model defaults. [@claim:clm_78145070fba69f2d173d5a216dca54c3329b9c27dd660f8d03730ea3b7613bd9]
- Aider connects to a wide range of LLM providers (Anthropic, OpenAI, DeepSeek, Gemini, OpenRouter, Bedrock, Vertex AI, Ollama, xAI) and works with most popular programming languages. [@claim:clm_8b82a09e4e018106e3a4669f45a48ac1782f2f47ab0ae029df06319b6299ad91]
- Aider builds a map of the entire codebase (repo map) to work well in larger projects, with tree-sitter based support for many languages including Fortran, Haskell, Julia, Zig, Kotlin, Scala, OCaml, Dart and MATLAB. [@claim:clm_c527cd885acece952ead5836dcc5051135f126b3c9a9e85f92015429de1d6baf]
- Aider depends on litellm for LLM connectivity; several releases bumped litellm (e.g. 1.75.0) to pick up provider fixes, and the deprecated google-generativeai dependency was removed. [@claim:clm_cbea6b719deefdd1e687304fd00b32e40375e52d034d5ad81e5605f34c067c49]
- The project maintains a public code-editing leaderboard; release notes cite model scores on it (e.g. Claude 3.5 Haiku at 75%) and benchmark statistics include token counts. [@claim:clm_d1cc5dadf9eb1d6e5dffebd7572c3d6e16b487a6f3aaf1961c60b243e2550b03]
- A watch-files mode lets users add AI-prefixed comments in any file from their IDE or editor to trigger aider, and a --copy-paste mode streamlines working with LLM web chat UIs. [@claim:clm_db369e10891cc1804f16eabb655f543d6c0f68789c639ecca92ea63a26f48b2c]
- Repository development practice: release notes state that Aider itself wrote a large share of each release's code (e.g. 88% in v0.86.0 and 92% in v0.82.0), indicating heavy dogfooding of the tool in its own development. [@claim:clm_ee21edf5f502abee4183d2bf0cbf5db3d7512f0ac7cea0c5745a43b7c443c4d1]
- Aider provides slash commands such as /model, /undo, /clear, /run, /test, /diff, /editor, /copy-context, /save and /load for in-session control. [@claim:clm_fb941bb5e91e20baa0148d463c45ba18af0ed02c88388be7e11fba5b5c186d21]
<!-- rcw:end owner=source:src_32ea4d56ab1a52db8960f0035c9b095f block=evidence -->

## Researcher notes

