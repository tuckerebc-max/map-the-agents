---
access: public
aliases: []
claim_ids:
- clm_492fe4224b66939bba3c3a8b914a0be18a60a1659068d5a1822bdc13c2dc4703
- clm_4b19cac82ac6a678f1de8a0360404531a712e531d133268f72cb747d8ed1147f
- clm_61e3a2097ccb09183007140808967f63dfe2473e26af14198f7149f398051f36
- clm_67f68a82347f866d9bf2fe1fe11a3310620511f11b24afb5d28f942e5836d472
- clm_7e78b400345be338d2b7a19a44ee1ec445231de17c2acdc889bb794cf7cd79de
- clm_8a058060035a375dfc64a2e379fb2da6dd2fcea840ef965b22cec1eff20ed4c1
- clm_8dd44c98b08cf31c8704b1fd2da600583c0b6cd5b2819d5284a8a43c534db94e
- clm_93c59eb9f5faadee666edcb6067c6a4898e0d9726fdea38fb2656109b5685bf0
- clm_a4b59dd6e0551a6b8c13b58ba849cc03e392dc1d209b40c54a42b216781bc46e
- clm_a69d1f72d67d72b2cd4235e25e4e2b93e618116551e3827663eb7e93d8c20c35
- clm_b07188ce0de84d81a9aba7f8620e2f1046c859be5da3b09d71f0e7cf0fabda8f
- clm_f2c2603a052e4fc08a33f3f528d0d894f988cb73315db7fd22460730b81a75d7
maturity: draft
page_id: pg_fb341bd7f99c58f3af6d8e52dcd8dccc
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_03b44c47bcdd5a7e856ad23a4925d9b8
title: willynikes2/agent-orchestrator/README.md @ f99e1eaf7414
updated_at: '2026-09-14T03:23:40Z'
---

# willynikes2/agent-orchestrator/README.md @ f99e1eaf7414

<!-- rcw:begin owner=source:src_03b44c47bcdd5a7e856ad23a4925d9b8 block=evidence -->
- Auto-downtime detection maps error patterns to actions: usage caps disable until reset, rate limits trigger a 5-minute cooldown, auth failures and bad models require manual re-enabling via /service up. [@claim:clm_492fe4224b66939bba3c3a8b914a0be18a60a1659068d5a1822bdc13c2dc4703]
- When a knowledge-base-server is running, the orchestrator searches it for relevant context before each response and injects KB results for the active task; kb_port is configurable for non-default ports. [@claim:clm_4b19cac82ac6a678f1de8a0360404531a712e531d133268f72cb747d8ed1147f]
- The REPL exposes slash commands including /setup, /models, /modes, /task, /run, /smoke, /kb, /service status/down/up/recover, /allow-dir, and /quit. [@claim:clm_61e3a2097ccb09183007140808967f63dfe2473e26af14198f7149f398051f36]
- Codex and Gemini CLI permission modes are configurable between full-host-unattended (default) and sandboxed-auto; the former runs Codex with --dangerously-bypass-approvals-and-sandbox and Gemini with yolo approval and sandbox disabled. [@claim:clm_67f68a82347f866d9bf2fe1fe11a3310620511f11b24afb5d28f942e5836d472]
- The implementation is a single ~1100-line Python file, daniel.py, containing config handling, per-agent CLI/API call functions, failover logic, auto-downtime detection, and KB context search. [@claim:clm_7e78b400345be338d2b7a19a44ee1ec445231de17c2acdc889bb794cf7cd79de]
- requirements.txt lists openai>=1.0.0, anthropic>=0.34.0, google-genai>=1.0.0, and python-dotenv>=1.0.0; the README requires Python 3.10+ and at least one installed AI CLI. [@claim:clm_8a058060035a375dfc64a2e379fb2da6dd2fcea840ef965b22cec1eff20ed4c1]
- Messages are routed through ordered role chains; when an agent fails or is down, the next agent in the chain is tried, and if all fail an error with recovery options is shown. [@claim:clm_8dd44c98b08cf31c8704b1fd2da600583c0b6cd5b2819d5284a8a43c534db94e]
- In full-host-unattended mode the agents can act without pausing for human approval, and directory whitelisting controls which directories agents may access. [@claim:clm_93c59eb9f5faadee666edcb6067c6a4898e0d9726fdea38fb2656109b5685bf0]
- Default role chains differ by role: orchestrator and review prefer Claude first, implementation prefers Codex first, and uidocs prefers Gemini first. [@claim:clm_a4b59dd6e0551a6b8c13b58ba849cc03e392dc1d209b40c54a42b216781bc46e]
- The product is a terminal-based orchestrator wrapping Claude, Codex, and Gemini CLIs with automatic failover and a shared knowledge base, advertised at roughly $60/month in subscriptions. [@claim:clm_a69d1f72d67d72b2cd4235e25e4e2b93e618116551e3827663eb7e93d8c20c35]
- Prefix routing sends 'impl:' messages to the implementation chain and 'ui:' to the UI chain, while @claude/@codex/@gemini address a specific agent directly, bypassing failover. [@claim:clm_b07188ce0de84d81a9aba7f8620e2f1046c859be5da3b09d71f0e7cf0fabda8f]
- Repository development practice: setup involves cloning, creating a virtualenv, installing requirements, and running 'python3 daniel.py --setup', whose wizard asks for name, per-agent mode, permission mode, optional API keys, model IDs, and chain preferences. [@claim:clm_f2c2603a052e4fc08a33f3f528d0d894f988cb73315db7fd22460730b81a75d7]
<!-- rcw:end owner=source:src_03b44c47bcdd5a7e856ad23a4925d9b8 block=evidence -->

## Researcher notes

