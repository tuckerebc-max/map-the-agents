# team-openpm/workgpt

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit f737a092dd4d @ 0760abb7ff749389

## Summary (orientation draft, not independently verified)

WorkGPT is an npm-published agent framework (MIT) that iterates with an LLM (e.g. GPT-4) against a set of APIs, including OpenAPI/OpenPM-based APIs and a Puppeteer text browser, until a user directive is completed.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] WorkGPT is described as an agent framework, similar to AutoGPT or LangChain, that converses with the AI back and forth until a given directive is complete. -- evidence: [README.md#L5-L5](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L5-L5)
- components (2 claim(s)):
  - [observation/documented] Ships with built-in API components including Calculator, FactApi, OpenpmApi, and a TextBrowser that uses Puppeteer as a text-based browser returning plain text instead of HTML. -- evidence: [README.md#L58-L58](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L58-L58), [README.md#L88-L88](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L88-L88), [README.md#L17-L22](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L17-L22)
  - [observation/documented] Includes an OpenAiAgent chat agent configurable with verbose, temperature, and model options, with gpt-4-0613 shown in examples. -- evidence: [README.md#L82-L86](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L82-L86), [README.md#L24-L28](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L24-L28)
- design-choices (2 claim(s)):
  - [observation/documented] Custom APIs can act as finishing programs: invokable methods with a zod schema (e.g. onFinish) let the LLM return structured data and halt the program. -- evidence: [README.md#L60-L60](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L60-L60), [README.md#L62-L80](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L62-L80)
  - [inference/documented] The framework appears to rely on OpenAI function-calling-style models, since examples use gpt-4-0613 and expose endpoints as invokable functions to the LLM. -- evidence: [README.md#L54-L54](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L54-L54), [README.md#L24-L28](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L24-L28)
- workflows (1 claim(s)):
  - [observation/documented] Repository is MIT licensed. -- evidence: [README.md#L104-L104](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L104-L104)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Any API representable as an OpenAPI file is supported; OpenPM, a package manager for OpenAPI files, can supply packages such as ipinfo by package id. -- evidence: [README.md#L52-L52](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L52-L52), [README.md#L7-L7](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L7-L7)
  - [observation/documented] API endpoints are exposed to the LLM as local functions ready to be invoked; users pass an authKey and the library handles authorization. -- evidence: [README.md#L54-L54](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L54-L54)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Distributed as the npm package 'workgpt', installable via npm install; the crawling example depends on Puppeteer for web access. -- evidence: [README.md#L58-L58](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L58-L58), [README.md#L3-L3](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L3-L3), [README.md#L11-L13](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L11-L13)
- limitations (1 claim(s)):
  - [observation/documented] The text-based browser returns only text rather than HTML; the README notes this is nonetheless sufficient for GPT-4 to extract data. -- evidence: [README.md#L58-L58](https://github.com/team-openpm/workgpt/blob/f737a092dd4debec8c518f665b1049922319d39f/README.md#L58-L58)
- relevance (1 claim(s)):
More evidence: [full detail](workgpt.detail.md)

Metadata and full claim list: [full detail](workgpt.detail.md)
Human notes ([notes](workgpt.notes.md), never overwritten by build)

[Back to map index](../../index.md)
