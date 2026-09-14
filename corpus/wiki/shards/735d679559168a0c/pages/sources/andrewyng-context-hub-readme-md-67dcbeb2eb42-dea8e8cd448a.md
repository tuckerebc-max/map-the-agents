---
access: public
aliases: []
claim_ids:
- clm_2aff4e41def7e685b8214d11777e2457e9bb71ffa196269a587af06a507e0703
- clm_7a6716dcba05b3390693224fe5a4befc9aa70c5bde4f88c309b9686b1baf7067
- clm_8beffb885d0430f3af8f61df56c218d13dea62acc9794a8099b920d9810a6d8f
- clm_ca0862d3589d7febbe2cdfebec82f61c6aa66f02e0d1e1d97fb728d475802d31
- clm_cbf258251a6c39233fdad18cb3adff84bd46f3a411329ebde6d8445eeb4ecb74
- clm_ddf7bebf19103cf7014976772071eeaffe604f74483163030d7c717d51b26995
- clm_e1a200125d6287a726b95e49e67d77bf0706484d7044ff58b506f5e74d1b348b
- clm_ea370d5d003fee4a5b2ab5de8e0636c9ac0ee741992678599ef1d8231aa34b84
maturity: draft
page_id: pg_5471dc2f382c5e10bafbdea8e8cd448a
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4f4c7fac03c65112adc2bcf67130f190
title: andrewyng/context-hub/README.md @ 67dcbeb2eb42
updated_at: '2026-09-14T03:33:52Z'
---

# andrewyng/context-hub/README.md @ 67dcbeb2eb42

<!-- rcw:begin owner=source:src_4f4c7fac03c65112adc2bcf67130f190 block=evidence -->
- Docs can have multiple reference files; --file fetches specific references and --full fetches everything, aimed at avoiding wasted tokens. [@claim:clm_2aff4e41def7e685b8214d11777e2457e9bb71ffa196269a587af06a507e0703]
- Feedback is up/down ratings sent to doc authors so content improves for everyone, separate from local annotations. [@claim:clm_7a6716dcba05b3390693224fe5a4befc9aa70c5bde4f88c309b9686b1baf7067]
- The product is an npm-distributed CLI requiring Node.js >= 18, installed globally as @aisuite/chub. [@claim:clm_8beffb885d0430f3af8f61df56c218d13dea62acc9794a8099b920d9810a6d8f]
- The project is MIT licensed and content is plain markdown with YAML frontmatter maintained in the repo. [@claim:clm_ca0862d3589d7febbe2cdfebec82f61c6aa66f02e0d1e1d97fb728d475802d31]
- Agents can use Chub via a SKILL.md agent skill; for Claude Code the README suggests placing it in ~/.claude/skills/get-api-docs. [@claim:clm_cbf258251a6c39233fdad18cb3adff84bd46f3a411329ebde6d8445eeb4ecb74]
- The CLI exposes commands including chub search [query], chub get <id> [--lang py|js], chub annotate (note, --clear, --list), and chub feedback <id> <up|down>. [@claim:clm_ddf7bebf19103cf7014976772071eeaffe604f74483163030d7c717d51b26995]
- Fetches support language variants via --lang (e.g. py or js) for the same doc ID such as openai/chat. [@claim:clm_e1a200125d6287a726b95e49e67d77bf0706484d7044ff58b506f5e74d1b348b]
- Annotations are local notes persisted across sessions and re-injected on future fetches only with --with-annotations, which is off by default, with contents treated as untrusted input. [@claim:clm_ea370d5d003fee4a5b2ab5de8e0636c9ac0ee741992678599ef1d8231aa34b84]
<!-- rcw:end owner=source:src_4f4c7fac03c65112adc2bcf67130f190 block=evidence -->

## Researcher notes

