# Setup-Amazon-Bedrock-Agent-For-Text2Sql-Using-Amazon-Redshift-Serverless-With-Streamlit (`setup-amazon-bedrock-agent-for-text2sql-using-amazon-redshift-serverless-with-streamlit`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: aws-samples
- License: MIT-0
- Language: Python
- Interface: platforms=Web; install=Multi-step AWS deployment: create SSH key pair, Redshift Serverless workgroup, load sample data, prepare Lambda function, update Streamlit credentials, create S3 bucket, upload files, create CloudFormation stack, access Streamlit app on port 8501
- Model providers: Amazon Bedrock (Anthropic Claude 3 Sonnet)
- Feature flags (directory-reported):
  - mcp_support: False (reported)
  - plugin_support: False (reported)
  - claude_code_plugin: False (reported)
  - subagents: False (reported)
  - hooks: False (reported)
  - plan_mode: False (reported)

Repository map entry: [aws-samples/setup-amazon-bedrock-agent-for-text2sql-using-amazon-redshift-serverless-with-streamlit](../../repos/aws-samples/setup-amazon-bedrock-agent-for-text2sql-using-amazon-redshift-serverless-with-streamlit.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): End-to-end natural language interface for querying databases by integrating Amazon Bedrock for AI-powered text-to-SQL conversion, AWS Lambda for database operations, and Streamlit for UI, all deployed via AWS CloudFormation. Sample/reference project with only 4 commits.

(captured site page body (agents/setup-amazon-bedrock-agent-for-text2sql-using-amazon-redshift-serverless-with-streamlit.md), not a verified repo-code finding)
The repo demonstrates the full path from a natural-language question to governed SQL execution on Amazon Redshift Serverless: a Bedrock agent backed by Claude 3 Sonnet translates the question, a Lambda action group executes the SQL, and a Streamlit UI hosted on EC2 presents results, all provisioned by a CloudFormation template. The nine-step README covers Redshift setup, sample data, S3 staging, deployment, and an unusually thorough troubleshooting section spanning IAM, CloudWatch, and connectivity. It is a small AWS Samples artifact — four commits, a handful of stars — published as a learning pattern under MIT-0 rather than maintained software. Its audience is AWS architects evaluating Bedrock agents for analytics access, and the security posture (row-level control illustration, EC2-hosted frontend) marks it as a starting point requiring hardening.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/setup-amazon-bedrock-agent-for-text2sql-using-amazon-redshift-serverless-with-streamlit.md)
