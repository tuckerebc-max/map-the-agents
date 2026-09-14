# aws-samples/setup-amazon-bedrock-agent-for-text2sql-using-amazon-redshift-serverless-with-streamlit

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 892ead9ecba9 @ 7f8b0354074963f5

## Summary (orientation draft, not independently verified)

Selected evidence records: The project sets up an Amazon Bedrock agent with an action group that translates natural language into SQL queries, backed by Amazon Redshift Serverless and a Streamlit frontend. The solution comprises a Lambda function (lambda_function.py and redshift_serverless_functions.py), a Streamlit app directory, and a CloudFormation template (ec2-streamlit-template.yaml).

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project sets up an Amazon Bedrock agent with an action group that translates natural language into SQL queries, backed by Amazon Redshift Serverless and a Streamlit frontend. -- evidence: [README.md#L4-L4](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L4-L4)
- components (1 claim(s)):
  - [observation/documented] The solution comprises a Lambda function (lambda_function.py and redshift_serverless_functions.py), a Streamlit app directory, and a CloudFormation template (ec2-streamlit-template.yaml). -- evidence: [README.md#L42-L48](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L42-L48), [README.md#L65-L75](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L65-L75)
- design-choices (1 claim(s)):
  - [observation/documented] ACL mapping is hard-coded in the Lambda function to illustrate ACL logic; the README notes a production system would require proper authorization logic instead. -- evidence: [README.md#L51-L53](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L51-L53)
- workflows (3 claim(s)):
  - [observation/documented] Configuration relies on environment variables: the Lambda uses REDSHIFT_WORKGROUP_NAME, while the EC2 instance's /etc/profile.d/bedrock_env.sh defines AGENT_ID, AGENT_ALIAS_ID, and AWS_REGION used by the Streamlit app. -- evidence: [README.md#L119-L120](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L119-L120), [README.md#L144-L144](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L144-L144), [README.md#L123-L131](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L123-L131)
  - [observation/documented] Troubleshooting guidance covers checking EC2 status, environment variables, cloud-init and Streamlit logs, Lambda configuration and invocations, Bedrock agent status, CloudWatch log groups, Redshift connectivity via Query Editor v2, and the CloudFormation events tab. -- evidence: [README.md#L191-L194](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L191-L194), [README.md#L205-L215](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L205-L215), [README.md#L197-L202](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L197-L202), [README.md#L237-L240](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L237-L240), [README.md#L152-L154](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L152-L154), [README.md#L185-L188](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L185-L188)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Users access the Streamlit application in a browser at http://<EC2-Public-IP>:8501, with the EC2 public IP taken from the CloudFormation stack outputs. -- evidence: [README.md#L78-L79](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L78-L79)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] Deployment is orchestrated through a CloudFormation stack whose parameters include EC2 instance type, SSH key pair, Bedrock agent name, Redshift workgroup name, S3 bucket name, and an allowed IP for SSH. -- evidence: [README.md#L65-L75](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L65-L75)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The setup requires an AWS account and Bedrock model access granted for Anthropic Claude 3 Sonnet, plus familiarity with Bedrock, S3, Lambda, Redshift Serverless, and EC2. -- evidence: [README.md#L7-L9](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L7-L9)
- limitations (1 claim(s)):
  - [observation/documented] The sample's access-control logic is only illustrative hard-coded ACL mapping in the Lambda function, so it is not production-grade authorization. -- evidence: [README.md#L51-L53](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L51-L53)
More evidence: [full detail](setup-amazon-bedrock-agent-for-text2sql-using-amazon-redshift-serverless-with-streamlit.detail.md)

Metadata and full claim list: [full detail](setup-amazon-bedrock-agent-for-text2sql-using-amazon-redshift-serverless-with-streamlit.detail.md)
Human notes ([notes](setup-amazon-bedrock-agent-for-text2sql-using-amazon-redshift-serverless-with-streamlit.notes.md), never overwritten by build)

[Back to map index](../../index.md)
