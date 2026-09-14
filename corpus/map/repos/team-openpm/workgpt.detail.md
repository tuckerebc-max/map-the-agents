# team-openpm/workgpt -- full detail

[Back to orientation](workgpt.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/team-openpm/workgpt/f737a092dd4debec8c518f665b1049922319d39f/0760abb7ff749389.json](../../../wiki/dossiers/team-openpm/workgpt/f737a092dd4debec8c518f665b1049922319d39f/0760abb7ff749389.json)

## specifications (1 claim(s))

- [observation/documented] WorkGPT is described as an agent framework, similar to AutoGPT or LangChain, that converses with the AI back and forth until a given directive is complete. -- evidence: [README.md#L5-L5](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L5-L5) (`clm_bdc8e258a1e1b91209d895ad08682b0a274abc76653bebe02f9931a652ed21af`)

## components (2 claim(s))

- [observation/documented] Ships with built-in API components including Calculator, FactApi, OpenpmApi, and a TextBrowser that uses Puppeteer as a text-based browser returning plain text instead of HTML. -- evidence: [README.md#L58-L58](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L58-L58), [README.md#L88-L88](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L88-L88), [README.md#L17-L22](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L17-L22) (`clm_cae8afde4545eb0b2a377870e99af64bfbefb1ac21b030c0c6aa9f78e50a97d3`)
- [observation/documented] Includes an OpenAiAgent chat agent configurable with verbose, temperature, and model options, with gpt-4-0613 shown in examples. -- evidence: [README.md#L82-L86](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L82-L86), [README.md#L24-L28](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L24-L28) (`clm_cdd991253786272893af6bb69cf7c7427ac1847b7cfa5571ac249e2dbc712384`)

## design-choices (2 claim(s))

- [observation/documented] Custom APIs can act as finishing programs: invokable methods with a zod schema (e.g. onFinish) let the LLM return structured data and halt the program. -- evidence: [README.md#L60-L60](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L60-L60), [README.md#L62-L80](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L62-L80) (`clm_694d209397e715cbae3bf609dba8020759b200fc88aed292d2dfb1ec015b2a40`)
- [inference/documented] The framework appears to rely on OpenAI function-calling-style models, since examples use gpt-4-0613 and expose endpoints as invokable functions to the LLM. -- evidence: [README.md#L54-L54](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L54-L54), [README.md#L24-L28](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L24-L28) (`clm_c3485812617890c43d4f864649c5499c88020b2493537ae0cff70a282336642d`)

## workflows (1 claim(s))

- [observation/documented] Repository is MIT licensed. -- evidence: [README.md#L104-L104](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L104-L104) (`clm_e317f61e2b2a835e16933736553708c7018640a57ed368078bbe025cc438e7dc`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Any API representable as an OpenAPI file is supported; OpenPM, a package manager for OpenAPI files, can supply packages such as ipinfo by package id. -- evidence: [README.md#L52-L52](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L52-L52), [README.md#L7-L7](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L7-L7) (`clm_65d216110451a12be851558558316afc32a717b583198394d96941eb19bfdd4b`)
- [observation/documented] API endpoints are exposed to the LLM as local functions ready to be invoked; users pass an authKey and the library handles authorization. -- evidence: [README.md#L54-L54](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L54-L54) (`clm_708593d061537a4c5799fdde6bfd2ee8e423e68d8b4d53780a7098919bbf494a`)
- [observation/documented] Programmatic usage centers on a WorkGptRunner constructed with an agent and an array of APIs, driven via runWithDirective(directive) which returns a result. -- evidence: [README.md#L43-L45](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L43-L45), [README.md#L38-L41](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L38-L41) (`clm_60b7484d262b453fb47a0c9c05559c73635b51c6de79b5f6b9a19529acd532d1`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Distributed as the npm package 'workgpt', installable via npm install; the crawling example depends on Puppeteer for web access. -- evidence: [README.md#L58-L58](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L58-L58), [README.md#L3-L3](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L3-L3), [README.md#L11-L13](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L11-L13) (`clm_2f8232385e103529ca9759e41ebcb84a2c732f90b7cf2e30f24cc17b0de31a4f`)

## limitations (1 claim(s))

- [observation/documented] The text-based browser returns only text rather than HTML; the README notes this is nonetheless sufficient for GPT-4 to extract data. -- evidence: [README.md#L58-L58](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L58-L58) (`clm_c8626990e136e33afafb19e68a4ea10c841f09ec2e71da42d9b76e39a613ace2`)

## relevance (1 claim(s))

- [observation/documented] Example directives include web research, website crawling, IP-to-city lookup with population, and ordering an Uber, indicating general tool-using agent use cases. -- evidence: [README.md#L95-L97](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L95-L97), [README.md#L43-L45](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L43-L45), [README.md#L7-L7](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L7-L7) (`clm_6b20478958cbac6a64123f694941feb0ae6c6d60d7ad23f2f7cbdb56f493dd65`)

