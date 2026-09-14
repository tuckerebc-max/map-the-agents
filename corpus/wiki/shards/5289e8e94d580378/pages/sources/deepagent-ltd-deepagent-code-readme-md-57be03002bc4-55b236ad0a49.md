---
access: public
aliases: []
claim_ids:
- clm_02bfd67211e541db19d07f1dea0d607b7eb65749e2da63599f7027bba43f32c8
- clm_23081dd23f39173f016b8f9cf5aba564230e7a1160bbb8ba433677875c1df6ef
- clm_28e6d3a3240321e8276a3f13a1f7554d883fa3ece3870444b9e4f00ede23033f
- clm_54771ee885d68ccc5c4750792639e52ed121b90a3747c4cefdade68ee4b46554
- clm_6673651db53f53de51238100a758a96a3f38c7e41a8c8393ddbbb68db52363a0
- clm_6f658f2e0cb6000519a44b1de0a87934e4d06e6efca5fbb06f28fa916f986ba4
- clm_7d43ca997771a9a73ee3c124ea1adc7cbe2163bb18489bbc320cbff4a5d384b4
- clm_8816eb9058ae23b4ed3f99e85eb7a97a840410ca9c21a66301dc83963196c4aa
- clm_b526bd398a1ba102298cf99934337f3e19584661910112bc7809b387e1303448
- clm_b6a1fe8e96f4337e9ffba6228b83f5e6bd7ee541dc29d05ef11e2270d79f2487
- clm_ccccd1d6a08d85c7d54bac050862c7777dc5632dd5833efc4b91ae7ac3c3a7f0
- clm_ead25eab29b929c50ad91e7a5f2755df919d8dabba2ead37f599a5f7f32eb0a9
maturity: draft
page_id: pg_2f740df261f454dda68a55b236ad0a49
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_448ea9efc95653d1a54d8255e0154afb
title: deepagent-ltd/deepagent-code/README.md @ 57be03002bc4
updated_at: '2026-09-14T01:45:25Z'
---

# deepagent-ltd/deepagent-code/README.md @ 57be03002bc4

<!-- rcw:begin owner=source:src_448ea9efc95653d1a54d8255e0154afb block=evidence -->
- For high-risk decisions an Expert Panel reviews a frozen question through correctness, security, performance, architecture, and reproducibility lenses, debating anonymously up to three rounds before a deterministic arbiter that preserves minority opinions and fails closed to human review. [@claim:clm_02bfd67211e541db19d07f1dea0d607b7eb65749e2da63599f7027bba43f32c8]
- The preset MCP catalog derives risk tiers from the catalog template rather than user config, and servers default to not-connected with write and external-fetch operations behind approval gates. [@claim:clm_23081dd23f39173f016b8f9cf5aba564230e7a1160bbb8ba433677875c1df6ef]
- Persistent state lives in typed documents (knowledge, strategy, methodology, skill, memory, design, worklog, diagnosis, eval) linked via supports/blocks/conflicts/validates into a traversable graph, with scope layers from session-private to sealed audit-only material. [@claim:clm_28e6d3a3240321e8276a3f13a1f7554d883fa3ece3870444b9e4f00ede23033f]
- The product ships as a desktop app and a terminal CLI; the CLI supports `deepagent auth login`, `deepagent auth list`, and `deepagent-code run "<task>"`. [@claim:clm_54771ee885d68ccc5c4750792639e52ed121b90a3747c4cefdade68ee4b46554]
- The project builds with Bun 1.3.14 and is provider-agnostic, supporting 75+ providers via the AI SDK and models.dev plus any OpenAI- or Anthropic-compatible endpoint. [@claim:clm_6673651db53f53de51238100a758a96a3f38c7e41a8c8393ddbbb68db52363a0]
- The project is licensed AGPL-3.0-or-later and is derived from opencode under the MIT License with NOTICE attribution; an enterprise edition exists in a separate repository. [@claim:clm_6f658f2e0cb6000519a44b1de0a87934e4d06e6efca5fbb06f28fa916f986ba4]
- Context assembly uses a durable Context Epoch: stable system instructions stay byte-stable for prompt caching while volatile state is appended in a dedicated tail block, and context changes are admitted only at safe provider-turn boundaries. [@claim:clm_7d43ca997771a9a73ee3c124ea1adc7cbe2163bb18489bbc320cbff4a5d384b4]
- Write-capable subagents get dedicated worktrees and return compact summaries; a Reviewer session checks each exact worker SHA, the coordinator performs serial `--no-ff` merges, and generation fencing prevents stale workers from settling or overwriting newer work. [@claim:clm_8816eb9058ae23b4ed3f99e85eb7a97a840410ca9c21a66301dc83963196c4aa]
- Providers are configured in `~/.deepagent/code/config.jsonc`; a custom OpenAI-compatible endpoint can set `discovery: true` for runtime model refresh or list models explicitly under `models`. [@claim:clm_b526bd398a1ba102298cf99934337f3e19584661910112bc7809b387e1303448]
- The `deepagent-code` npm package is not yet publicly published; installation is via the desktop app or a curl install script. [@claim:clm_b6a1fe8e96f4337e9ffba6228b83f5e6bd7ee541dc29d05ef11e2270d79f2487]
- Learning follows a governed lifecycle: evidence creates a candidate, isolated review or human decision changes its status, and regression/ablation gates publish a reproducible knowledge snapshot; rejection reasons persist so discarded patterns are not silently relearned. [@claim:clm_ccccd1d6a08d85c7d54bac050862c7777dc5632dd5833efc4b91ae7ac3c3a7f0]
- Three collaboration modes are offered: Auto (end-to-end execution), Loop (editable `goal+plan.md` advanced through plan, execute, verify, iterate ticks), and Design (faithful execution of a user-written plan); autonomy and permission levels are independent of mode. [@claim:clm_ead25eab29b929c50ad91e7a5f2755df919d8dabba2ead37f599a5f7f32eb0a9]
<!-- rcw:end owner=source:src_448ea9efc95653d1a54d8255e0154afb block=evidence -->

## Researcher notes

