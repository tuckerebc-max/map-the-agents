---
access: public
aliases: []
claim_ids:
- clm_06bb76789dfc3e916b0109c921b13b6eb23f90a16f7f92d1488d4dee025098de
- clm_0e9f065cdf2484fe05d6b3b70664c9a3b0b93767e7f9425889f11527a1449b93
- clm_13ca6cdd1bebbe1eb04971d6171499b0bf4e64ab2be3562bbf571eef5fa22d3d
- clm_1a03d8f7ebe2fd511a51c2b51785c7078dc7761c1aa4d92dc0ae29b4b84cced9
- clm_2d356680516396ac4bd74b9fa23af0464fac7f7bb24a977270aba83a8876a183
- clm_657aa16d28ceeacc66b5e731fad36e26a1e856498ff0af666df1ec2715583279
- clm_69578c6cef61e07b6ae58db8535d69a7faece0a88d01872ac8df0344f2bf4f01
- clm_e3930ee3d6991f6f0073ce384a48e199b5e2ae7b6cae66b1cc93d16496d1b4aa
- clm_f75c71fdbafcf0cd881c6b47ec33712830ef9b89af499a6ccf7306ca5c0066a2
maturity: draft
page_id: pg_1da2138217e957148a33ff12ce91d82a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_49a8b5e9f0ac576a9683d64fb5fc3068
title: superagent-ai/vibekit/LLM.md @ c670afd2e332
updated_at: '2026-09-14T03:17:07Z'
---

# superagent-ai/vibekit/LLM.md @ c670afd2e332

<!-- rcw:begin owner=source:src_49a8b5e9f0ac576a9683d64fb5fc3068 block=evidence -->
- The core package is @vibe-kit/vibekit at version 0.0.43 with main entry dist/index.js. [@claim:clm_06bb76789dfc3e916b0109c921b13b6eb23f90a16f7f92d1488d4dee025098de]
- The SDK exposes event listeners via .on('update') and .on('error') for streaming progress and errors. [@claim:clm_0e9f065cdf2484fe05d6b3b70664c9a3b0b93767e7f9425889f11527a1449b93]
- Common environment variables include OPENAI_API_KEY, ANTHROPIC_API_KEY, GOOGLE_API_KEY, E2B_API_KEY, DAYTONA_API_KEY, NORTHFLANK_API_KEY, and GITHUB_TOKEN. [@claim:clm_13ca6cdd1bebbe1eb04971d6171499b0bf4e64ab2be3562bbf571eef5fa22d3d]
- The SDK uses a builder pattern: new VibeKit() configured via withAgent (type, provider, apiKey, model), withSandbox, withGithub, withSecrets, and withWorkingDirectory. [@claim:clm_1a03d8f7ebe2fd511a51c2b51785c7078dc7761c1aa4d92dc0ae29b4b84cced9]
- Sandbox providers are separate packages: @vibe-kit/e2b, @vibe-kit/daytona, @vibe-kit/northflank, @vibe-kit/cloudflare (Workers only), and @vibe-kit/modal. [@claim:clm_2d356680516396ac4bd74b9fa23af0464fac7f7bb24a977270aba83a8876a183]
- Documented SDK methods include generateCode(prompt, mode) with 'code' or 'ask' modes, executeCommand, getHost(port), pause, resume, createPullRequest, and kill. [@claim:clm_657aa16d28ceeacc66b5e731fad36e26a1e856498ff0af666df1ec2715583279]
- VibeKit is described as a TypeScript SDK for running AI coding agents (Claude, Codex, Gemini, OpenCode) in secure sandboxes with GitHub integration. [@claim:clm_69578c6cef61e07b6ae58db8535d69a7faece0a88d01872ac8df0344f2bf4f01]
- Cloudflare sandboxes only work inside Cloudflare Workers and cannot be used in regular Node.js applications or other environments; they use Durable Object bindings instead of API keys. [@claim:clm_e3930ee3d6991f6f0073ce384a48e199b5e2ae7b6cae66b1cc93d16496d1b4aa]
- The SDK is documented as fully typed with TypeScript definitions, exporting types such as VibeKit, AgentResponse, AgentType, ModelProvider, and per-provider config types. [@claim:clm_f75c71fdbafcf0cd881c6b47ec33712830ef9b89af499a6ccf7306ca5c0066a2]
<!-- rcw:end owner=source:src_49a8b5e9f0ac576a9683d64fb5fc3068 block=evidence -->

## Researcher notes

