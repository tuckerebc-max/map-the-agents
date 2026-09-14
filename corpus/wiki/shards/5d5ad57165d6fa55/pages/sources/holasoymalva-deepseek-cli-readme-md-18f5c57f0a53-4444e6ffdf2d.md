---
access: public
aliases: []
claim_ids:
- clm_0b49e44eae0d6f75000740e730fd9bb0c31499e52951f11f4a3172b43ff0a457
- clm_23a99ad150f103d31f45d2502bc2a64c40907e9686cf88b1ec1cb1dad0732cf7
- clm_285caf2684ad69c68f08dd3bf292f5e471e5a4e54de134aa96a10d34849672f0
- clm_3709556df144f9e03e1d826f757a93068fb82e85577181c9d2b036acdae5969c
- clm_54dc8ead1474aa04af021fab0527ebd6e3ffd3478aa20820cb261f510bcf471d
- clm_62fcda64728896ed31da080e7c2e724c24c8bf511400a65fc2d66ebc779f6061
- clm_8e8c81f1842663578b7239f0dccdf34ef0585f5afd2988aec1a945aa647a96ce
- clm_9d59647431191d78e427360bbdb7cbdae2094d0d0f7131fb9b6dd4fc66beddc1
- clm_9e3ca3eb82627843c6e15e661055d3f76d90d809f79d54b19c967792f01bc761
- clm_d9b9c25e69d44e022c6ac93bc017953783a158987342ec87fd19ba537e58b69f
- clm_ed3777558493ccb1fbf7d1877f1d1fb0383571cad9e1ab4c254a48311be1056c
maturity: draft
page_id: pg_8fd096a6cc8a5cca84184444e6ffdf2d
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_f2da7fb0caac5e65afa835ba69638f2f
title: holasoymalva/deepseek-cli/README.md @ 18f5c57f0a53
updated_at: '2026-09-14T02:04:22Z'
---

# holasoymalva/deepseek-cli/README.md @ 18f5c57f0a53

<!-- rcw:begin owner=source:src_f2da7fb0caac5e65afa835ba69638f2f block=evidence -->
- Local Ollama mode is the default (DEEPSEEK_USE_LOCAL defaults to true), with cloud API mode available when an API key is configured. [@claim:clm_0b49e44eae0d6f75000740e730fd9bb0c31499e52951f11f4a3172b43ff0a457]
- The project is a command-line AI coding assistant for code generation, refactoring, debugging, review, and scaffolding, built on Gemini CLI's foundation and DeepSeek Coder models. [@claim:clm_23a99ad150f103d31f45d2502bc2a64c40907e9686cf88b1ec1cb1dad0732cf7]
- Repository development practice: contributors fork and clone, run npm install, npm test, and npm run dev; building from source uses npm run build and npm run package. [@claim:clm_285caf2684ad69c68f08dd3bf292f5e471e5a4e54de134aa96a10d34849672f0]
- It uses DeepSeek Coder models in 1.3B, 6.7B, and 33B sizes, with documented RAM needs of 2GB, 8GB, and 32GB respectively. [@claim:clm_3709556df144f9e03e1d826f757a93068fb82e85577181c9d2b036acdae5969c]
- The setup command checks for Ollama, starts the service if needed, downloads the specified model, and verifies the installation. [@claim:clm_54dc8ead1474aa04af021fab0527ebd6e3ffd3478aa20820cb261f510bcf471d]
- The CLI maintains context across interactions in multi-turn conversations and automatically includes relevant project files as context. [@claim:clm_62fcda64728896ed31da080e7c2e724c24c8bf511400a65fc2d66ebc779f6061]
- The tool requires Node.js 18 or higher and Ollama for local operation; the npm package is run-deepseek-cli installed globally. [@claim:clm_8e8c81f1842663578b7239f0dccdf34ef0585f5afd2988aec1a945aa647a96ce]
- Repository context can be controlled via flags such as --include-all for the whole repo and --include with specific files or directories. [@claim:clm_9d59647431191d78e427360bbdb7cbdae2094d0d0f7131fb9b6dd4fc66beddc1]
- The CLI exposes commands including interactive mode (deepseek), single-prompt mode (deepseek chat), setup, --local, --model, --help, and --version. [@claim:clm_9e3ca3eb82627843c6e15e661055d3f76d90d809f79d54b19c967792f01bc761]
- Interactive mode is described as a REPL with syntax highlighting, session history, automatic file-context inclusion, and multi-turn conversations. [@claim:clm_d9b9c25e69d44e022c6ac93bc017953783a158987342ec87fd19ba537e58b69f]
- Documented model context windows are 16K tokens for the 1.3b, 6.7b, and 33b instruct variants, and the 33b model is noted as slower. [@claim:clm_ed3777558493ccb1fbf7d1877f1d1fb0383571cad9e1ab4c254a48311be1056c]
<!-- rcw:end owner=source:src_f2da7fb0caac5e65afa835ba69638f2f block=evidence -->

## Researcher notes

