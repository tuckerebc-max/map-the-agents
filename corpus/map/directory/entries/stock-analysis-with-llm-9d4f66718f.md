# Stock-Analysis-With-Llm (`stock-analysis-with-llm`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: bauer-jan
- License: MIT
- Language: Python
- Interface: platforms=IDE; install=cdk deploy in infrastructure folder, run deploy_agents.py, configure Action Groups in AWS Bedrock Console, update src/config.ini and redeploy
- Model providers: Amazon Bedrock (Anthropic Claude 3)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: False (reported)

Repository map entry: [bauer-jan/stock-analysis-with-llm](../../repos/bauer-jan/stock-analysis-with-llm.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Automated stock analysis and portfolio management system using AWS Bedrock Agents with Anthropic Claude 3. Analyzes stocks across S&P 500, Nasdaq 100, and EURO STOXX 50 using balance sheets, technical indicators, news, and market sentiment, then provides BUY/SELL recommendations and portfolio updates. Two modules: Stock Analyst and Portfolio Manager. Only 1 commit (one-time upload).

(captured site page body (agents/stock-analysis-with-llm.md), not a verified repo-code finding)
The repository wires Amazon Bedrock Agents into a financial workflow: a Stock Analyst module ranks equities across major indices using balance-sheet data, technical indicators, and news, while a Portfolio Manager module applies those recommendations to a simulated portfolio, with user prompts able to steer selection and weighting. Action groups run through Lambda, market data comes from Yahoo Finance, results persist in DynamoDB, and EventBridge schedules ECS tasks on a weekly cadence; no real trades are executed. Infrastructure is defined in AWS CDK with a Python script registering the agents in the Bedrock console. It is a single-commit demonstration with no follow-up development, and it appears in this census only as a misfiled entry — nothing in it creates or modifies code.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/stock-analysis-with-llm.md)
