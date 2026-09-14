# bauer-jan/stock-analysis-with-llm

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 96b8039f7b24 @ 5d2b26a1fe4cc741

## Summary (orientation draft, not independently verified)

README-only evidence for an LLM-based stock analysis and portfolio management system built on AWS Bedrock (Claude 3), EventBridge, ECS, Lambda and DynamoDB, with Yahoo Finance data and no real trade execution.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project aims to build an automated stock analysis and portfolio management system using balance sheet data, technical indicators, news, industry information and market sentiment, powered by LLMs such as Claude 3 on AWS Bedrock. -- evidence: [README.md#L3-L3](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L3-L3)
- components (2 claim(s)):
  - [observation/documented] A Stock Analyst module performs weekly analysis of S&P 500, Nasdaq 100 and EURO STOXX 50 stocks, ranks them within their industries using balance sheet data, technical indicators and news, and stores results in a database. -- evidence: [README.md#L7-L14](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L7-L14)
  - [observation/documented] A Portfolio Manager module updates the portfolio weekly based on analyst BUY/SELL recommendations and market sentiment, accepts user prompts to influence selection and weighting, and stores the portfolio in a database. -- evidence: [README.md#L16-L19](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L16-L19)
- design-choices (1 claim(s)):
  - [observation/documented] Prompt templates are externalized in src/schema/prompts.yaml so model behavior can be tuned by editing prompts; an internet-search action group schema is provided at src/schema/internet-search-schema.json. -- evidence: [README.md#L116-L116](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L116-L116), [README.md#L83-L96](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L83-L96)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: setup involves deploying infrastructure with 'cdk deploy', running infrastructure/deploy_agents.py to create Bedrock Agents (not CDK-supported), manually configuring action groups and prompt templates in the console, and updating src/config.ini before redeploying. -- evidence: [README.md#L101-L104](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L101-L104), [README.md#L83-L96](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L83-L96), [README.md#L98-L99](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L98-L99), [README.md#L106-L108](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L106-L108)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Behavior is configured via src/config.ini, e.g. setting COMPARE_SYMBOLS_WITHOUT_INDUSTRY, INDEX_SYMBOLS and SYMBOLS to compare individual stocks or rank all stocks in an index by industry. -- evidence: [README.md#L45-L68](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L45-L68), [README.md#L43-L43](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L43-L43), [README.md#L72-L80](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L72-L80)
- memory-state (1 claim(s)):
  - [observation/documented] LLM recommendations and summarized data are saved in Amazon DynamoDB. -- evidence: [README.md#L29-L37](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L29-L37)
- orchestration (2 claim(s)):
  - [observation/documented] The pipeline is triggered by AWS EventBridge events that start ECS tasks fetching earnings reports from Yahoo Finance, then prompts a Bedrock Agent for web searches and news summarization before Claude ranks stocks. -- evidence: [README.md#L29-L37](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L29-L37)
  - [observation/documented] Portfolio management is separately triggered by an EventBridge event; a Bedrock Agent collects general market news, and the LLM acts as portfolio manager using analyst-provided information. -- evidence: [README.md#L29-L37](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L29-L37)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](stock-analysis-with-llm.detail.md)

Metadata and full claim list: [full detail](stock-analysis-with-llm.detail.md)
Human notes ([notes](stock-analysis-with-llm.notes.md), never overwritten by build)

[Back to map index](../../index.md)
