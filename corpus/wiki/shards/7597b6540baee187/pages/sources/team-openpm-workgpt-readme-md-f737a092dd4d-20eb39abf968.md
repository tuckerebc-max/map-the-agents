---
access: public
aliases: []
claim_ids:
- clm_2f8232385e103529ca9759e41ebcb84a2c732f90b7cf2e30f24cc17b0de31a4f
- clm_60b7484d262b453fb47a0c9c05559c73635b51c6de79b5f6b9a19529acd532d1
- clm_65d216110451a12be851558558316afc32a717b583198394d96941eb19bfdd4b
- clm_694d209397e715cbae3bf609dba8020759b200fc88aed292d2dfb1ec015b2a40
- clm_6b20478958cbac6a64123f694941feb0ae6c6d60d7ad23f2f7cbdb56f493dd65
- clm_708593d061537a4c5799fdde6bfd2ee8e423e68d8b4d53780a7098919bbf494a
- clm_bdc8e258a1e1b91209d895ad08682b0a274abc76653bebe02f9931a652ed21af
- clm_c3485812617890c43d4f864649c5499c88020b2493537ae0cff70a282336642d
- clm_c8626990e136e33afafb19e68a4ea10c841f09ec2e71da42d9b76e39a613ace2
- clm_cae8afde4545eb0b2a377870e99af64bfbefb1ac21b030c0c6aa9f78e50a97d3
- clm_cdd991253786272893af6bb69cf7c7427ac1847b7cfa5571ac249e2dbc712384
- clm_e317f61e2b2a835e16933736553708c7018640a57ed368078bbe025cc438e7dc
maturity: draft
page_id: pg_e2f4620de7b1572a94d420eb39abf968
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b63af54be75d51b4be0029a3865e0e57
title: team-openpm/workgpt/README.md @ f737a092dd4d
updated_at: '2026-09-14T03:18:48Z'
---

# team-openpm/workgpt/README.md @ f737a092dd4d

<!-- rcw:begin owner=source:src_b63af54be75d51b4be0029a3865e0e57 block=evidence -->
- Distributed as the npm package 'workgpt', installable via npm install; the crawling example depends on Puppeteer for web access. [@claim:clm_2f8232385e103529ca9759e41ebcb84a2c732f90b7cf2e30f24cc17b0de31a4f]
- Programmatic usage centers on a WorkGptRunner constructed with an agent and an array of APIs, driven via runWithDirective(directive) which returns a result. [@claim:clm_60b7484d262b453fb47a0c9c05559c73635b51c6de79b5f6b9a19529acd532d1]
- Any API representable as an OpenAPI file is supported; OpenPM, a package manager for OpenAPI files, can supply packages such as ipinfo by package id. [@claim:clm_65d216110451a12be851558558316afc32a717b583198394d96941eb19bfdd4b]
- Custom APIs can act as finishing programs: invokable methods with a zod schema (e.g. onFinish) let the LLM return structured data and halt the program. [@claim:clm_694d209397e715cbae3bf609dba8020759b200fc88aed292d2dfb1ec015b2a40]
- Example directives include web research, website crawling, IP-to-city lookup with population, and ordering an Uber, indicating general tool-using agent use cases. [@claim:clm_6b20478958cbac6a64123f694941feb0ae6c6d60d7ad23f2f7cbdb56f493dd65]
- API endpoints are exposed to the LLM as local functions ready to be invoked; users pass an authKey and the library handles authorization. [@claim:clm_708593d061537a4c5799fdde6bfd2ee8e423e68d8b4d53780a7098919bbf494a]
- WorkGPT is described as an agent framework, similar to AutoGPT or LangChain, that converses with the AI back and forth until a given directive is complete. [@claim:clm_bdc8e258a1e1b91209d895ad08682b0a274abc76653bebe02f9931a652ed21af]
- The framework appears to rely on OpenAI function-calling-style models, since examples use gpt-4-0613 and expose endpoints as invokable functions to the LLM. [@claim:clm_c3485812617890c43d4f864649c5499c88020b2493537ae0cff70a282336642d]
- The text-based browser returns only text rather than HTML; the README notes this is nonetheless sufficient for GPT-4 to extract data. [@claim:clm_c8626990e136e33afafb19e68a4ea10c841f09ec2e71da42d9b76e39a613ace2]
- Ships with built-in API components including Calculator, FactApi, OpenpmApi, and a TextBrowser that uses Puppeteer as a text-based browser returning plain text instead of HTML. [@claim:clm_cae8afde4545eb0b2a377870e99af64bfbefb1ac21b030c0c6aa9f78e50a97d3]
- Includes an OpenAiAgent chat agent configurable with verbose, temperature, and model options, with gpt-4-0613 shown in examples. [@claim:clm_cdd991253786272893af6bb69cf7c7427ac1847b7cfa5571ac249e2dbc712384]
- Repository is MIT licensed. [@claim:clm_e317f61e2b2a835e16933736553708c7018640a57ed368078bbe025cc438e7dc]
<!-- rcw:end owner=source:src_b63af54be75d51b4be0029a3865e0e57 block=evidence -->

## Researcher notes

