# bauer-jan/stock-analysis-with-llm -- full detail

[Back to orientation](stock-analysis-with-llm.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/bauer-jan/stock-analysis-with-llm/96b8039f7b242934c0ab8d831931eef96f4c2bd9/5d2b26a1fe4cc741.json](../../../wiki/dossiers/bauer-jan/stock-analysis-with-llm/96b8039f7b242934c0ab8d831931eef96f4c2bd9/5d2b26a1fe4cc741.json)

## specifications (1 claim(s))

- [observation/documented] The project aims to build an automated stock analysis and portfolio management system using balance sheet data, technical indicators, news, industry information and market sentiment, powered by LLMs such as Claude 3 on AWS Bedrock. -- evidence: [README.md#L3-L3](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L3-L3) (`clm_34b35ecac0826dc527af21fcd1dd434ae2019264ceb7baa4faca14ef8c8c00b6`)

## components (2 claim(s))

- [observation/documented] A Stock Analyst module performs weekly analysis of S&P 500, Nasdaq 100 and EURO STOXX 50 stocks, ranks them within their industries using balance sheet data, technical indicators and news, and stores results in a database. -- evidence: [README.md#L7-L14](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L7-L14) (`clm_23761bd24a1bdf07a31dd8e994afc8ad193e772a44641ba10e104c7c457b5bed`)
- [observation/documented] A Portfolio Manager module updates the portfolio weekly based on analyst BUY/SELL recommendations and market sentiment, accepts user prompts to influence selection and weighting, and stores the portfolio in a database. -- evidence: [README.md#L16-L19](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L16-L19) (`clm_13432828e7dbc90d04592b5b2cd27e127a85dcdd3e77badc2ab858dabcdc4c75`)

## design-choices (1 claim(s))

- [observation/documented] Prompt templates are externalized in src/schema/prompts.yaml so model behavior can be tuned by editing prompts; an internet-search action group schema is provided at src/schema/internet-search-schema.json. -- evidence: [README.md#L116-L116](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L116-L116), [README.md#L83-L96](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L83-L96) (`clm_a0b9b288517aa973a1ddf2198d3bba8e08e9072a5d69d9535c3478ac7d40d7de`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: setup involves deploying infrastructure with 'cdk deploy', running infrastructure/deploy_agents.py to create Bedrock Agents (not CDK-supported), manually configuring action groups and prompt templates in the console, and updating src/config.ini before redeploying. -- evidence: [README.md#L101-L104](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L101-L104), [README.md#L83-L96](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L83-L96), [README.md#L98-L99](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L98-L99), [README.md#L106-L108](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L106-L108) (`clm_9c73abf3364eb0e0621bf0c5764b9d48faf211bded3847bec7ac88c62641bb68`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Behavior is configured via src/config.ini, e.g. setting COMPARE_SYMBOLS_WITHOUT_INDUSTRY, INDEX_SYMBOLS and SYMBOLS to compare individual stocks or rank all stocks in an index by industry. -- evidence: [README.md#L45-L68](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L45-L68), [README.md#L43-L43](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L43-L43), [README.md#L72-L80](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L72-L80) (`clm_7e46f06dd23e17e63d7b4c41d8570c52e5cd457cfc963255ae4f35dd196a0142`)

## memory-state (1 claim(s))

- [observation/documented] LLM recommendations and summarized data are saved in Amazon DynamoDB. -- evidence: [README.md#L29-L37](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L29-L37) (`clm_871f069517a5411e9440e4279a34cefdab75acaad11e490fe76fa0557a99e752`)

## orchestration (2 claim(s))

- [observation/documented] The pipeline is triggered by AWS EventBridge events that start ECS tasks fetching earnings reports from Yahoo Finance, then prompts a Bedrock Agent for web searches and news summarization before Claude ranks stocks. -- evidence: [README.md#L29-L37](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L29-L37) (`clm_9e61eebdb2c705794a9e78a2904d90bb197b3c0d8721e9791f714fa80aa98415`)
- [observation/documented] Portfolio management is separately triggered by an EventBridge event; a Bedrock Agent collects general market news, and the LLM acts as portfolio manager using analyst-provided information. -- evidence: [README.md#L29-L37](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L29-L37) (`clm_90329ab9305aa9ffc41de1c695227587d77d1372aa13c02ed6ac79531ad46a57`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The system depends on AWS services (EventBridge, ECS, Bedrock, DynamoDB, Lambda, CDK) and the Yahoo Finance API, and requires Anthropic Claude 3 model access enabled in the Bedrock console. -- evidence: [README.md#L29-L37](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L29-L37), [README.md#L83-L96](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L83-L96), [README.md#L106-L108](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L106-L108), [README.md#L27-L27](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L27-L27) (`clm_05fd5985ce77a9020d4792441f2ce373e8f1cea26246a0fdfd5c4529db737be3`)

## limitations (2 claim(s))

- [observation/documented] No real trades are executed; stock data comes from the Yahoo API. -- evidence: [README.md#L21-L21](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L21-L21) (`clm_f2fce7a7d60cc1b39f81f9fcbabef8aa55638b48654fca53370adf05247ac966`)
- [observation/documented] Comparing all stocks within indexes can incur high Bedrock costs due to the large number of stocks involved. -- evidence: [README.md#L70-L70](https://github.com/bauer-jan/stock-analysis-with-llm/blob/96b8039f7b242934c0ab8d831931eef96f4c2bd9/README.md#L70-L70) (`clm_9a80d7085e6796b01e6a5ae3498bda2b86106fb7e96e4f8537af168b561524c8`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

