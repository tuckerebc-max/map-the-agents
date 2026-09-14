---
access: public
aliases: []
claim_ids:
- clm_1176f09332c5614cc004d9b9eeb3ebd6559e421adfe33d32b6505671c4bdc9e1
- clm_1b722a96998551c2e371ccd69cb681aff5ce7826205a90242f0e3ba809be73b9
- clm_52653c22300f4bf762d55655160607ebada35949b0ede69d870973b2ed46199c
- clm_7f26c1b592ffbe2129326498d0d5cce2264b8fc21bcb9f65126676d220a41058
- clm_bf240727f34ea7d66dad7a62252e6ffdd0813477d8cbf800033efacd24ee93ea
- clm_f02872071bd0737ac15bb3d378e35a9ef8f52c8eda09471ede5acaf61b1d7ef8
maturity: draft
page_id: pg_50d1044e6cf45908a058ab414f01c169
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_e0d83cbec32e5a5397fe3c37998b1556
title: anomalyco/opencode/packages/opencode/src/agent/agent.ts @ df23b7f9488a
updated_at: '2026-09-14T01:33:42Z'
---

# anomalyco/opencode/packages/opencode/src/agent/agent.ts @ df23b7f9488a

<!-- rcw:begin owner=source:src_e0d83cbec32e5a5397fe3c37998b1556 block=evidence -->
- An agent 'generate' capability creates new agent configurations from a natural-language description via a model generateObject call with a JSON schema (identifier, whenToUse, systemPrompt), avoiding existing agent names. [@claim:clm_1176f09332c5614cc004d9b9eeb3ebd6559e421adfe33d32b6505671c4bdc9e1]
- The plan agent's permission config denies all edit tools except plan markdown files under .opencode/plans and the global plans data directory, and denies the general task subagent. [@claim:clm_1b722a96998551c2e371ccd69cb681aff5ce7826205a90242f0e3ba809be73b9]
- The agent implementation uses the Effect ecosystem (Effect, Context, Layer, Schema), the Vercel AI SDK (generateObject/streamObject), remeda, and OpenTelemetry tracing when experimental.openTelemetry is enabled. [@claim:clm_52653c22300f4bf762d55655160607ebada35949b0ede69d870973b2ed46199c]
- The agent module defines default permission rules: wildcard allow, ask for doom_loop and external directories, deny for question and plan transitions, and ask for reading .env files while allowing .env.example. [@claim:clm_7f26c1b592ffbe2129326498d0d5cce2264b8fc21bcb9f65126676d220a41058]
- Agent configuration is a schema with name, description, mode (subagent/primary/all), permission ruleset, optional model, prompt, temperature, topP, steps, variant, color, and hidden fields. [@claim:clm_bf240727f34ea7d66dad7a62252e6ffdd0813477d8cbf800033efacd24ee93ea]
- Users can define custom agents in config; entries can disable built-ins or add new agents whose properties (model, prompt, permissions, mode, etc.) are merged over defaults. [@claim:clm_f02872071bd0737ac15bb3d378e35a9ef8f52c8eda09471ede5acaf61b1d7ef8]
<!-- rcw:end owner=source:src_e0d83cbec32e5a5397fe3c37998b1556 block=evidence -->

## Researcher notes

