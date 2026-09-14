---
access: public
aliases: []
claim_ids:
- clm_11b155fae820130f6b2e57ed1cff76ebe9979c2126b04a30ad99827e1b97982b
- clm_1ea081c8d8f82949a172903bc4b5b471f3eff431a7c530630f335d28997d2ceb
- clm_21b796a4bf6d31a5ce6e41b8ee98702675533a89284c8c96e62cb6aea1cf082c
- clm_61a3f5fdf3ef12024c7679ea81d7e75b70628f52267a52f7c64c0a252618a4fa
- clm_93b032eebe4dc60c8a58ea9bd5727dd46e4cdf57e03e718bcba44e8326b77175
- clm_d782d826851893b948b1e0bdd2a9f31d84714013714695bd66b66957966293a7
- clm_e8e585d9f5405bcd4ce7afe08b501f314913f8a68cbb7687cd53fa5ef4e4f0f1
maturity: draft
page_id: pg_3f4727c7407d5854a3ab62d04c68fb30
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8a57cf60df025ae5a1deb672ab8df8b1
title: proxysoul/Empryo/README.md @ f771fc238e64
updated_at: '2026-09-14T02:32:49Z'
---

# proxysoul/Empryo/README.md @ f771fc238e64

<!-- rcw:begin owner=source:src_8a57cf60df025ae5a1deb672ab8df8b1 block=evidence -->
- Three surfaces share one code graph: a native desktop app, a full terminal UI, and a headless CLI for scripts and CI. [@claim:clm_11b155fae820130f6b2e57ed1cff76ebe9979c2126b04a30ad99827e1b97982b]
- The README reports head-to-head benchmarks against pi on bug-fixing tasks (e.g. 8/9 vs 7/9 bugs fixed, 28% lower cost, 57% faster), with methodology and a reproduction repo at proxysoul/pi-vs-empryo-bench. [@claim:clm_1ea081c8d8f82949a172903bc4b5b471f3eff431a7c530630f335d28997d2ceb]
- Empryo builds codebase understanding before mutating code: on launch, tree-sitter parses the repo into a live graph of symbols, imports, and call sites ranked by PageRank and git co-change. [@claim:clm_21b796a4bf6d31a5ce6e41b8ee98702675533a89284c8c96e62cb6aea1cf082c]
- The agent supports 22 LLM providers including Anthropic, OpenAI, Google, Groq, DeepSeek, and Bedrock, plus OpenAI-compatible endpoints and fully local Ollama/LM Studio; an llmgateway provider ships built in. [@claim:clm_61a3f5fdf3ef12024c7679ea81d7e75b70628f52267a52f7c64c0a252618a4fa]
- Every prompt creates a git checkpoint ('time machine'), letting users rewind code and conversation together to any turn. [@claim:clm_93b032eebe4dc60c8a58ea9bd5727dd46e4cdf57e03e718bcba44e8326b77175]
- The product offers 65+ symbol-level AST editing operations with atomic all-or-nothing rollback and structural edits across 30+ languages, with a typecheck as the gate. [@claim:clm_d782d826851893b948b1e0bdd2a9f31d84714013714695bd66b66957966293a7]
- A task router assigns models to ten routable roles (e.g. spark for read-only scouting, ember for code edits, verify for review), configurable per tab, per project, or globally, with custom agents definable. [@claim:clm_e8e585d9f5405bcd4ce7afe08b501f314913f8a68cbb7687cd53fa5ef4e4f0f1]
<!-- rcw:end owner=source:src_8a57cf60df025ae5a1deb672ab8df8b1 block=evidence -->

## Researcher notes

