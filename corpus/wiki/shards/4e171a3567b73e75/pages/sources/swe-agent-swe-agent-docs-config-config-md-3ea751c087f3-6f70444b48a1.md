---
access: public
aliases: []
claim_ids:
- clm_05528c43d5e9fee1fe2d4db10c2780d030a926c7594d3d8bda04c111a6def000
- clm_83ef7e99d45bee501f3512b5baaf6fbaa5dd7152c2e0d5c65acbc1eed0f9c84c
- clm_bd553d401c0673abbf71a9748552733091a2d9957534a7ebccd7e1f6e785dc4e
- clm_c657bdca80777e0df4caf25540ef69f81dbe37b2fa030cf08e41f71e1308f0ad
maturity: draft
page_id: pg_6fa6a3d07b335d89acab6f70444b48a1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_7da161cf69c45f85bc6607ef9dafe3bd
title: SWE-agent/SWE-agent/docs/config/config.md @ 3ea751c087f3
updated_at: '2026-09-14T03:16:49Z'
---

# SWE-agent/SWE-agent/docs/config/config.md @ 3ea751c087f3

<!-- rcw:begin owner=source:src_7da161cf69c45f85bc6607ef9dafe3bd block=evidence -->
- Multimodal support is provided via config/default_mm_with_images.yaml, which enables GitHub issue image processing to base64, an image_tools bundle, a web_browser bundle, and an image_parsing history processor. [@claim:clm_05528c43d5e9fee1fe2d4db10c2780d030a926c7594d3d8bda04c111a6def000]
- A single YAML configuration governs the agent: it defines tools, prompts shown deterministically or conditionally during a trajectory, demonstrations, model behavior, and the agent-environment input/output interface. [@claim:clm_83ef7e99d45bee501f3512b5baaf6fbaa5dd7152c2e0d5c65acbc1eed0f9c84c]
- Configurations are YAML files passed via the --config flag to commands like 'sweagent run' and 'sweagent run-batch'; multiple config files can be given and are merged in a nested way. [@claim:clm_bd553d401c0673abbf71a9748552733091a2d9957534a7ebccd7e1f6e785dc4e]
- Repository development practice: relative paths in config files resolve to the SWE_AGENT_CONFIG_ROOT environment variable if set, otherwise the repository root. [@claim:clm_c657bdca80777e0df4caf25540ef69f81dbe37b2fa030cf08e41f71e1308f0ad]
<!-- rcw:end owner=source:src_7da161cf69c45f85bc6607ef9dafe3bd block=evidence -->

## Researcher notes

