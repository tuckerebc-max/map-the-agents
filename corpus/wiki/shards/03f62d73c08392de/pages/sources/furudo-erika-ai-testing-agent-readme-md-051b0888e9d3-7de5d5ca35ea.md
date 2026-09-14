---
access: public
aliases: []
claim_ids:
- clm_04db88fb63a2efe1ef38ef689517acf615396ebce448d789cec943d943850f39
- clm_07e1c93d49d31ce6288d8e82d222bed09a892e7b2b2d9fc8217b37808565b401
- clm_0ec4f1864ea1df81abc4350f7db662fba130a7c1bfec7893dcffd8327d81d84a
- clm_1e85ccd13fce97bd1a1bf72dd5d76ea778cabcec5ea42a7ae8b01c94f646ae4d
- clm_55e8736a2fb6f34fd32cb93f9ce01a2bc4215fc526cb95629c9015fcd287e12c
- clm_6b70563049e3fd3bbd9ac81b3757869ecb3dc00b4105630f289cb0d4e15f5477
- clm_79b2770a077d8ef0ec6678dcc1dad579d5c5c8a8f7f403dfaac97f04dbb58a0c
- clm_82abb1410525838df3370e0fc34fba9bc7b342aa9c55cbc5af4bdfd9281dbf1b
- clm_9896ac42d13832ca47b3f02b068423d4bed36ab030c8a6514b454a41493ee773
- clm_ac2acb17d2057bccb2fb785b33b632d3b18a8513d532d502e94f29cb2a3a0cee
- clm_d3dc4b18bbf3f1aca95d741cb9625569498d2e8887fcbec0ea5005f19e9b1c98
- clm_f7a986a587365d9051db61fe4529228e363262057fb45cbb633d4ea973b8b220
maturity: draft
page_id: pg_85006beab40f566492627de5d5ca35ea
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_1595b7df46a7593980cc84a1417717a4
title: furudo-erika/ai-testing-agent/README.md @ 051b0888e9d3
updated_at: '2026-09-14T01:50:00Z'
---

# furudo-erika/ai-testing-agent/README.md @ 051b0888e9d3

<!-- rcw:begin owner=source:src_1595b7df46a7593980cc84a1417717a4 block=evidence -->
- Documented usage workflow: start the API with uvicorn on port 8000, run python agent.py in a second terminal, then issue Plan/Generate/Run/Feedback commands. [@claim:clm_04db88fb63a2efe1ef38ef689517acf615396ebce448d789cec943d943850f39]
- Generated tests target TEST_API_URL if set, otherwise defaulting to http://localhost:8000. [@claim:clm_07e1c93d49d31ce6288d8e82d222bed09a892e7b2b2d9fc8217b37808565b401]
- By default the agent assumes the target API has specific REST routes like /api/endpoint, but users can customize this via prompts. [@claim:clm_0ec4f1864ea1df81abc4350f7db662fba130a7c1bfec7893dcffd8327d81d84a]
- The README's example install lists fastapi, uvicorn, requests, pytest, langchain, and openai as pip dependencies, and requires an OpenRouter API key. [@claim:clm_1e85ccd13fce97bd1a1bf72dd5d76ea778cabcec5ea42a7ae8b01c94f646ae4d]
- Troubleshooting guidance covers missing OPENROUTER_API_KEY, unexpected 401 responses needing an Authorization header, and mismatched generated routes, suggesting explicit prompts or feedback. [@claim:clm_55e8736a2fb6f34fd32cb93f9ce01a2bc4215fc526cb95629c9015fcd287e12c]
- api_tester.py exposes a command-line interface with subcommands plan, generate, run, and feedback, usable directly without the chat agent. [@claim:clm_6b70563049e3fd3bbd9ac81b3757869ecb3dc00b4105630f289cb0d4e15f5477]
- agent.py is a LangChain chatbot whose actions (Plan, Generate, Run, Feedback) invoke tools in agent_tools.py, which run api_tester.py commands in subprocesses. [@claim:clm_79b2770a077d8ef0ec6678dcc1dad579d5c5c8a8f7f403dfaac97f04dbb58a0c]
- The project comprises main.py (a sample FastAPI app), api_tester.py (CLI logic for plan/generate/run/feedback), agent_tools.py, agent.py, and generated_tests.py. [@claim:clm_82abb1410525838df3370e0fc34fba9bc7b342aa9c55cbc5af4bdfd9281dbf1b]
- Generated test quality appears heavily dependent on user prompting; the README notes LLM output quality depends heavily on how it is prompted and may invent routes not present in the real API. [@claim:clm_9896ac42d13832ca47b3f02b068423d4bed36ab030c8a6514b454a41493ee773]
- Running python agent.py starts an interactive prompt where the user types commands or instructions, with 'quit' or 'exit' to stop. [@claim:clm_ac2acb17d2057bccb2fb785b33b632d3b18a8513d532d502e94f29cb2a3a0cee]
- Prompting guidance advises explicitly describing endpoints, specifying desired test names and structure, and providing example test-code skeletons to steer output. [@claim:clm_d3dc4b18bbf3f1aca95d741cb9625569498d2e8887fcbec0ea5005f19e9b1c98]
- The README suggests setting temperature to 0.0 in api_tester.py to reduce randomness and obtain more deterministic LLM output. [@claim:clm_f7a986a587365d9051db61fe4529228e363262057fb45cbb633d4ea973b8b220]
<!-- rcw:end owner=source:src_1595b7df46a7593980cc84a1417717a4 block=evidence -->

## Researcher notes

