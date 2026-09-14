---
access: public
aliases: []
claim_ids:
- clm_13727861b09edf775d51e1eeed662317e425bd2f693da1590234cbb99a45e2b0
- clm_147e89f771065bcc89af4309e8e6c133022464e0e817f742b562d29e6e2bbf6f
- clm_5315fed80e403e031415a87be7d61065f669cdd77f6b123459b8e3d1e044358e
- clm_7dbd129df1bbcaccdda3283960c665d4fb75adcc50e55ffb18ec1923991db512
- clm_8d4a16d014f6a851e63fb00ead2cbe9f5c82a76b88cbef174bf913669e57d5db
- clm_8fe42009510d3705d71eabb048e566865ff15528ab82f674c9c1c9f7ede94c0b
- clm_b21356fc24fb5c7571891599b88c9be6e6559adc28e51fbfafcacf4de4c3f53f
- clm_bf5de17e4dedac00ffd37fe9c375666165e1cc9882790d81103535113734962e
- clm_eb8936d9ebfd494ca25f96b9b5b51bf201eec1762595c9c87890db0d1f92d7ec
- clm_fc9ecd126a7b8c1590632529267490703f00ea2de01aa20141f8960d264b2723
maturity: draft
page_id: pg_d93ef11e99fe5e9e8b79115972a938f2
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f04ea5b7b3615a67bd10d659bf81662c
title: bhouston/mycoder/README.md @ 774e068e5dae
updated_at: '2026-09-14T01:37:43Z'
---

# bhouston/mycoder/README.md @ 774e068e5dae

<!-- rcw:begin owner=source:src_f04ea5b7b3615a67bd10d659bf81662c block=evidence -->
- MyCoder is a command-line interface for AI-powered coding tasks, installable globally via npm. [@claim:clm_13727861b09edf775d51e1eeed662317e425bd2f693da1590234cbb99a45e2b0]
- Configuration is resolved from multiple locations in precedence order (project-root mycoder.config.js variants, .mycoder.rc, package.json 'mycoder' field, XDG user config) and supports many file formats; CLI arguments override config-file settings. [@claim:clm_147e89f771065bcc89af4309e8e6c133022464e0e817f742b562d29e6e2bbf6f]
- The repository is a monorepo with packages for the CLI (mycoder), the agent module (mycoder-agent), and a documentation website (mycoder-docs). [@claim:clm_5315fed80e403e031415a87be7d61065f669cdd77f6b123459b8e3d1e044358e]
- Repository development practice: contributors clone the repo, run pnpm install/build/test/commit, and releases follow Conventional Commits with an automated CI/CD pipeline that versions, generates a changelog, creates a GitHub Release, tags, and publishes to NPM after PR review and merge to main. [@claim:clm_7dbd129df1bbcaccdda3283960c665d4fb75adcc50e55ffb18ec1923991db512]
- The agent leverages Anthropic's Claude, OpenAI models, and Ollama, and uses Playwright for browser automation, which normally requires separate browser installation. [@claim:clm_8d4a16d014f6a851e63fb00ead2cbe9f5c82a76b88cbef174bf913669e57d5db]
- The CLI supports interactive mode (-i), prompt arguments, prompt files (-f), an --interactive correction mode, and flags like --userPrompt false and --upgradeCheck false for automated runs. [@claim:clm_8fe42009510d3705d71eabb048e566865ff15528ab82f674c9c1c9f7ede94c0b]
- MyCoder supports Model Context Protocol (MCP) server configuration with named servers, bearer auth, default resources, and default tools, plus a GitHub mode for working with issues and PRs including /mycoder comment commands. [@claim:clm_b21356fc24fb5c7571891599b88c9be6e6559adc28e51fbfafcacf4de4c3f53f]
- MyCoder can spawn sub-agents for concurrent task processing, and status updates report active sub-agents, shell processes, and browser sessions. [@claim:clm_bf5de17e4dedac00ffd37fe9c375666165e1cc9882790d81103535113734962e]
- A system browser detection feature lets MyCoder use installed Chrome, Edge, Firefox and other browsers on Windows, macOS, and Linux, falling back to Playwright's bundled browsers when none is found. [@claim:clm_eb8936d9ebfd494ca25f96b9b5b51bf201eec1762595c9c87890db0d1f92d7ec]
- With --interactive, users can press Ctrl+M during execution to send corrections to the running agent, which incorporates them into its decision-making; this can also be enabled via an 'interactive: true' config option. [@claim:clm_fc9ecd126a7b8c1590632529267490703f00ea2de01aa20141f8960d264b2723]
<!-- rcw:end owner=source:src_f04ea5b7b3615a67bd10d659bf81662c block=evidence -->

## Researcher notes

