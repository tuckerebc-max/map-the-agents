---
access: public
aliases: []
claim_ids:
- clm_148ec180642b27f97f5ec935696b67327b094ea58cb2d0151678e1033807a1e9
- clm_1647a43c812099acae398b4762bd603e833ed3720643ba94cc6c17cc549caeef
- clm_45643162a7971bd6d0315bc62a4ebd68bc958dd0c9f691519745b01cf5f3c84f
- clm_70fa064569a1d6f6888439a94782834fd4063d51b1cab18b7e26d788a69ed80a
- clm_abff7469470d5505d35a9932eb59730bf18bcb730b97cc91ad6f5666ce616958
- clm_b9c24ac9810c1ff33a5dff9b6032c1d6c69af2f6e0693b34d31d121a5a5d135f
- clm_eb67dd8f0432bf3c98a117c61d62611dc8b064ef7da1f4dfd07669603fe171f5
maturity: draft
page_id: pg_652a10a4e1e756769cec679da0d1040f
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_67a66dcba7b057f6b7f2a12c6ac1cad8
title: zhinjs/zhin/README.md @ 494dd81f1ac5
updated_at: '2026-09-14T04:33:46Z'
---

# zhinjs/zhin/README.md @ 494dd81f1ac5

<!-- rcw:begin owner=source:src_67a66dcba7b057f6b7f2a12c6ac1cad8 block=evidence -->
- The README lists adapter packages for 20+ platforms including QQ, Discord, Slack, Telegram, DingTalk, OneBot 11/12, GitHub, email, and LINE. [@claim:clm_148ec180642b27f97f5ec935696b67327b094ea58cb2d0151678e1033807a1e9]
- AI is opt-in: the default install is an IM core under ~10MB, and agent capability requires adding @zhin.js/agent, zod, ai, and a provider package such as @ai-sdk/openai. [@claim:clm_1647a43c812099acae398b4762bd603e833ed3720643ba94cc6c17cc549caeef]
- Plugin hot reload is described as a Generation transaction: the next plugin tree is prepared and validated off-path, then published atomically, so a failed candidate leaves the active Generation serving traffic. [@claim:clm_45643162a7971bd6d0315bc62a4ebd68bc958dd0c9f691519745b01cf5f3c84f]
- Scaffolded TypeScript projects require Node.js >=22.12.0 and pnpm 9+, while the compiled IM library supports Node ^20.19.0 or >=22.12.0. [@claim:clm_70fa064569a1d6f6888439a94782834fd4063d51b1cab18b7e26d788a69ed80a]
- The repo is a pnpm workspace monorepo whose packages include @zhin.js/core (IM layer), @zhin.js/ai, @zhin.js/agent, @zhin.js/cli (composition root), and the zhin.js facade package. [@claim:clm_abff7469470d5505d35a9932eb59730bf18bcb730b97cc91ad6f5666ce616958]
- The CLI exposes commands including `zhin runtime start`, `zhin setup`, `zhin doctor`, `zhin new my-plugin`, and `zhin search <kw>`. [@claim:clm_b9c24ac9810c1ff33a5dff9b6032c1d6c69af2f6e0693b34d31d121a5a5d135f]
- Agent execution security is configurable via zhin.config.yml, e.g. execSecurity: allowlist and execApprovalMode: ask; the stability table lists a baseline security tier with bash allowlist, file policy, and approval. [@claim:clm_eb67dd8f0432bf3c98a117c61d62611dc8b064ef7da1f4dfd07669603fe171f5]
<!-- rcw:end owner=source:src_67a66dcba7b057f6b7f2a12c6ac1cad8 block=evidence -->

## Researcher notes

