---
access: public
aliases: []
claim_ids:
- clm_62c117de4ded26410eb724f0fcc8271166c43e9219430589de5e69647fb51b55
- clm_7a57cadd1c414fb6b86affaf23659e238323b1f38ce4fc1872cd33a8db67904e
- clm_9199d2916301eb69ee465747887bbc77c211d10431e79444f9d89588f0caa566
- clm_f550331e2cdc019645cd24aa3e4dbd228fbc6d345391de39c7ca3e2ae8054b5e
maturity: draft
page_id: pg_eea2524bb68e5fd6ab357fc33ba8bd76
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_37fbb8c2c9bb5d9790b97afd84976bce
title: sondera-ai/sondera-coding-agent-hooks/README.md @ 9efefedd249e
updated_at: '2026-09-14T04:22:24Z'
---

# sondera-ai/sondera-coding-agent-hooks/README.md @ 9efefedd249e

<!-- rcw:begin owner=source:src_37fbb8c2c9bb5d9790b97afd84976bce block=evidence -->
- The signature engine and Cedar policies run with no external dependencies or API keys; the optional LLM classifiers support Ollama (the default when enabled), OpenAI-compatible servers, Anthropic, Gemini, and Vertex AI via Application Default Credentials. [@claim:clm_62c117de4ded26410eb724f0fcc8271166c43e9219430589de5e69647fb51b55]
- Enforcement hooks fail closed: a hook that cannot reach the harness denies preventive events and never proceeds unadjudicated, so losing the server blocks the agent rather than ungoverning it. [@claim:clm_7a57cadd1c414fb6b86affaf23659e238323b1f38ce4fc1872cd33a8db67904e]
- The project targets AI coding agents — Claude Code, Cursor, GitHub Copilot, and Gemini CLI, plus adapters for Antigravity, Codex, Hermes, OpenCode, OpenHands, and VS Code — intercepting shell commands, file operations, and web requests. [@claim:clm_9199d2916301eb69ee465747887bbc77c211d10431e79444f9d89588f0caa566]
- Adapters can act on decisions as block (deny, fail-closed), ask (escalate to the host approval UI), steer (inject context), redact (replace tool output), terminate (stop the loop), or observe only, with capability varying per adapter and hook group. [@claim:clm_f550331e2cdc019645cd24aa3e4dbd228fbc6d345391de39c7ca3e2ae8054b5e]
<!-- rcw:end owner=source:src_37fbb8c2c9bb5d9790b97afd84976bce block=evidence -->

## Researcher notes

