# aws-samples/setup-amazon-bedrock-agent-for-text2sql-using-amazon-redshift-serverless-with-streamlit -- full detail

[Back to orientation](setup-amazon-bedrock-agent-for-text2sql-using-amazon-redshift-serverless-with-streamlit.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/f5e8e9fb/6615ac42/892ead9ecba9927fe5f17bf9695de21589f2a634/7f8b0354074963f5.json](../../../wiki/dossiers/f5e8e9fb/6615ac42/892ead9ecba9927fe5f17bf9695de21589f2a634/7f8b0354074963f5.json)

## specifications (1 claim(s))

- [observation/documented] The project sets up an Amazon Bedrock agent with an action group that translates natural language into SQL queries, backed by Amazon Redshift Serverless and a Streamlit frontend. -- evidence: [README.md#L4-L4](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L4-L4) (`clm_01851f608d08b8fa0bf7220d297e644d7046d949fcffb58a72c766c88ef286b9`)

## components (1 claim(s))

- [observation/documented] The solution comprises a Lambda function (lambda_function.py and redshift_serverless_functions.py), a Streamlit app directory, and a CloudFormation template (ec2-streamlit-template.yaml). -- evidence: [README.md#L42-L48](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L42-L48), [README.md#L65-L75](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L65-L75) (`clm_f1d936fdf925853ab6baf684c24cb665ce0d9183afaf2a6fd1bb356503ec5b6c`)

## design-choices (1 claim(s))

- [observation/documented] ACL mapping is hard-coded in the Lambda function to illustrate ACL logic; the README notes a production system would require proper authorization logic instead. -- evidence: [README.md#L51-L53](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L51-L53) (`clm_5b522c66f1b77bd124acc8ba661fe733a83c7a2e83e33a703b4404294b1b92c8`)

## workflows (3 claim(s))

- [observation/documented] Configuration relies on environment variables: the Lambda uses REDSHIFT_WORKGROUP_NAME, while the EC2 instance's /etc/profile.d/bedrock_env.sh defines AGENT_ID, AGENT_ALIAS_ID, and AWS_REGION used by the Streamlit app. -- evidence: [README.md#L119-L120](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L119-L120), [README.md#L144-L144](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L144-L144), [README.md#L123-L131](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L123-L131) (`clm_f8dbe5cbaa7c91bd0cd2be68a4cff33c096d63ef893388dd806654c6d989ac70`)
- [observation/documented] Troubleshooting guidance covers checking EC2 status, environment variables, cloud-init and Streamlit logs, Lambda configuration and invocations, Bedrock agent status, CloudWatch log groups, Redshift connectivity via Query Editor v2, and the CloudFormation events tab. -- evidence: [README.md#L191-L194](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L191-L194), [README.md#L205-L215](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L205-L215), [README.md#L197-L202](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L197-L202), [README.md#L237-L240](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L237-L240), [README.md#L152-L154](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L152-L154), [README.md#L185-L188](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L185-L188) (`clm_9da7af181ad30fe863046c9af84b143b441130f66a8e771aeab1898fbe1a2658`)
- [observation/documented] Repository development practice: contributors should file GitHub issues with reproducible steps, base pull requests on the latest main branch, keep changes focused, ensure local tests pass, and monitor CI failures; security issues must go through AWS's vulnerability reporting page rather than public issues. -- evidence: [CONTRIBUTING.md#L17-L20](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/CONTRIBUTING.md#L17-L20), [CONTRIBUTING.md#L32-L37](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/CONTRIBUTING.md#L32-L37), [CONTRIBUTING.md#L54-L54](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/CONTRIBUTING.md#L54-L54), [CONTRIBUTING.md#L26-L28](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/CONTRIBUTING.md#L26-L28) (`clm_de3f0f6b9147f79724926b2c8dbbea6a309374a210d88491487af23331fc3322`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Users access the Streamlit application in a browser at http://<EC2-Public-IP>:8501, with the EC2 public IP taken from the CloudFormation stack outputs. -- evidence: [README.md#L78-L79](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L78-L79) (`clm_de57c981c5ef25063e8ef7308cfa32163e9e74dac5ab52497ebad515cce7babe`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Deployment is orchestrated through a CloudFormation stack whose parameters include EC2 instance type, SSH key pair, Bedrock agent name, Redshift workgroup name, S3 bucket name, and an allowed IP for SSH. -- evidence: [README.md#L65-L75](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L65-L75) (`clm_339225efa510303286ae30410afd90a7194d90b4f5cb5ab0e031131993c69592`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The setup requires an AWS account and Bedrock model access granted for Anthropic Claude 3 Sonnet, plus familiarity with Bedrock, S3, Lambda, Redshift Serverless, and EC2. -- evidence: [README.md#L7-L9](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L7-L9) (`clm_fe3a2468b096eb0fdc611b2ec8e9bf76563aeaf13515cefb15b658df0c8baa90`)

## limitations (1 claim(s))

- [observation/documented] The sample's access-control logic is only illustrative hard-coded ACL mapping in the Lambda function, so it is not production-grade authorization. -- evidence: [README.md#L51-L53](https://github.com/aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/blob/892ead9ecba9927fe5f17bf9695de21589f2a634/README.md#L51-L53) (`clm_81d2c24e710f453954c9180cc036afb4e198fad4c3edf827c30645d7ae471518`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

