---
access: public
aliases: []
claim_ids:
- clm_060003b334feee4cddf876978ffc53b64a5dacca9898cd2aef0df35b2cddc67b
- clm_30d3b35379f60d8f0917647627dcfc8073b0a1728cb175477537cf0a191f75df
- clm_6958916bfa90d723cf5f585a5c3c6b0fe08bcc8f6e2211dfec689a95f558e77c
- clm_9781279ae74a51310e0d834cc581a3d0c107d9dcc5512a4b1796c01c81674eac
- clm_a3bc70f454faed6412c3f84621b845dc5f4b8289c4991103006c79d7b7ee1867
- clm_b96ffcab46e1fec9c2749f3b96f41c7e2b26b4af0d2a2bf93cf6ee67d3a678fe
- clm_dd771ce5f8d5eb61eb1233ea25f693cd3a7a5d71b273abd19b54b2649f5d15c1
- clm_e774cb2c29cd89db77b6cabfb3c6b2e48ad61363f1387f8db0c26747d047eb6f
- clm_fd0894890cdff7c2bd4f24dffd90a58ddfb4d6e45efd76fd2db1a788a48bd8fb
maturity: draft
page_id: pg_2852e74951fc5a3498beae91e642b419
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_bf87810bf3e05ea191273485af8a8373
title: 2389-research/claude-plugins/README.md @ 017d34612ebf
updated_at: '2026-09-14T03:28:23Z'
---

# 2389-research/claude-plugins/README.md @ 017d34612ebf

<!-- rcw:begin owner=source:src_bf87810bf3e05ea191273485af8a8373 block=evidence -->
- The thrifty plugin is documented as benchmarked at roughly 64% lower cost than Opus at equal quality, suggesting some agent-performance evaluation exists, though no eval harness appears in the evidence. [@claim:clm_060003b334feee4cddf876978ffc53b64a5dacca9898cd2aef0df35b2cddc67b]
- Plugins can be installed in any agent (Claude Code, Cursor, Codex) via vercel-labs/skills using 'npx skills add 2389-research/<plugin>'. [@claim:clm_30d3b35379f60d8f0917647627dcfc8073b0a1728cb175477537cf0a191f75df]
- The repository is a marketplace of 28 plugins and MCP servers for Claude Code covering parallel exploration, iterative refinement, binary reverse engineering, and structured decision-making. [@claim:clm_6958916bfa90d723cf5f585a5c3c6b0fe08bcc8f6e2211dfec689a95f558e77c]
- Repository development practice: adding a plugin requires creating a repo under 2389-research/, adding a marketplace.json entry, running 'npm run generate', then committing and pushing. [@claim:clm_9781279ae74a51310e0d834cc581a3d0c107d9dcc5512a4b1796c01c81674eac]
- Native Claude Code installation uses '/plugin marketplace add 2389-research/claude-plugins' followed by '/plugin install <plugin>@2389-research'. [@claim:clm_a3bc70f454faed6412c3f84621b845dc5f4b8289c4991103006c79d7b7ee1867]
- The marketplace is MIT-licensed, published by 2389 Research, browsable at 2389-research.github.io/claude-plugins, with contact email hello@2389.ai. [@claim:clm_b96ffcab46e1fec9c2749f3b96f41c7e2b26b4af0d2a2bf93cf6ee67d3a678fe]
- The marketplace lists four MCP servers: agent-drugs, socialmedia, journal, and slack-mcp, providing behavior modification, social media, journaling, and Slack integration. [@claim:clm_dd771ce5f8d5eb61eb1233ea25f693cd3a7a5d71b273abd19b54b2649f5d15c1]
- The catalog includes plugins such as simmer (iterative refinement with investigation-first judges), test-kitchen (parallel implementation exploration), thrifty (tiered Sonnet/Haiku delegation), and binary-re (ELF reverse engineering). [@claim:clm_e774cb2c29cd89db77b6cabfb3c6b2e48ad61363f1387f8db0c26747d047eb6f]
- The four MCP servers (journal, socialmedia, slack-mcp, agent-drugs) install via Claude Code only and ship no skills for npx. [@claim:clm_fd0894890cdff7c2bd4f24dffd90a58ddfb4d6e45efd76fd2db1a788a48bd8fb]
<!-- rcw:end owner=source:src_bf87810bf3e05ea191273485af8a8373 block=evidence -->

## Researcher notes

