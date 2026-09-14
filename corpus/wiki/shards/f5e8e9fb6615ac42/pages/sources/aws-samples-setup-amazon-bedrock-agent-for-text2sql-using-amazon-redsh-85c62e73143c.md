---
access: public
aliases: []
claim_ids:
- clm_01851f608d08b8fa0bf7220d297e644d7046d949fcffb58a72c766c88ef286b9
- clm_339225efa510303286ae30410afd90a7194d90b4f5cb5ab0e031131993c69592
- clm_5b522c66f1b77bd124acc8ba661fe733a83c7a2e83e33a703b4404294b1b92c8
- clm_81d2c24e710f453954c9180cc036afb4e198fad4c3edf827c30645d7ae471518
- clm_9da7af181ad30fe863046c9af84b143b441130f66a8e771aeab1898fbe1a2658
- clm_de57c981c5ef25063e8ef7308cfa32163e9e74dac5ab52497ebad515cce7babe
- clm_f1d936fdf925853ab6baf684c24cb665ce0d9183afaf2a6fd1bb356503ec5b6c
- clm_f8dbe5cbaa7c91bd0cd2be68a4cff33c096d63ef893388dd806654c6d989ac70
- clm_fe3a2468b096eb0fdc611b2ec8e9bf76563aeaf13515cefb15b658df0c8baa90
maturity: draft
page_id: pg_7256717307085469bedc85c62e73143c
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_96da25b1f1b45b27bc794d935a1a3196
title: aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/README.md
  @ 892ead9ecba9
updated_at: '2026-09-14T03:36:21Z'
---

# aws-samples/Setup-Amazon-Bedrock-Agent-for-Text2SQL-Using-Amazon-Redshift-Serverless-with-Streamlit/README.md @ 892ead9ecba9

<!-- rcw:begin owner=source:src_96da25b1f1b45b27bc794d935a1a3196 block=evidence -->
- The project sets up an Amazon Bedrock agent with an action group that translates natural language into SQL queries, backed by Amazon Redshift Serverless and a Streamlit frontend. [@claim:clm_01851f608d08b8fa0bf7220d297e644d7046d949fcffb58a72c766c88ef286b9]
- Deployment is orchestrated through a CloudFormation stack whose parameters include EC2 instance type, SSH key pair, Bedrock agent name, Redshift workgroup name, S3 bucket name, and an allowed IP for SSH. [@claim:clm_339225efa510303286ae30410afd90a7194d90b4f5cb5ab0e031131993c69592]
- ACL mapping is hard-coded in the Lambda function to illustrate ACL logic; the README notes a production system would require proper authorization logic instead. [@claim:clm_5b522c66f1b77bd124acc8ba661fe733a83c7a2e83e33a703b4404294b1b92c8]
- The sample's access-control logic is only illustrative hard-coded ACL mapping in the Lambda function, so it is not production-grade authorization. [@claim:clm_81d2c24e710f453954c9180cc036afb4e198fad4c3edf827c30645d7ae471518]
- Troubleshooting guidance covers checking EC2 status, environment variables, cloud-init and Streamlit logs, Lambda configuration and invocations, Bedrock agent status, CloudWatch log groups, Redshift connectivity via Query Editor v2, and the CloudFormation events tab. [@claim:clm_9da7af181ad30fe863046c9af84b143b441130f66a8e771aeab1898fbe1a2658]
- Users access the Streamlit application in a browser at http://<EC2-Public-IP>:8501, with the EC2 public IP taken from the CloudFormation stack outputs. [@claim:clm_de57c981c5ef25063e8ef7308cfa32163e9e74dac5ab52497ebad515cce7babe]
- The solution comprises a Lambda function (lambda_function.py and redshift_serverless_functions.py), a Streamlit app directory, and a CloudFormation template (ec2-streamlit-template.yaml). [@claim:clm_f1d936fdf925853ab6baf684c24cb665ce0d9183afaf2a6fd1bb356503ec5b6c]
- Configuration relies on environment variables: the Lambda uses REDSHIFT_WORKGROUP_NAME, while the EC2 instance's /etc/profile.d/bedrock_env.sh defines AGENT_ID, AGENT_ALIAS_ID, and AWS_REGION used by the Streamlit app. [@claim:clm_f8dbe5cbaa7c91bd0cd2be68a4cff33c096d63ef893388dd806654c6d989ac70]
- The setup requires an AWS account and Bedrock model access granted for Anthropic Claude 3 Sonnet, plus familiarity with Bedrock, S3, Lambda, Redshift Serverless, and EC2. [@claim:clm_fe3a2468b096eb0fdc611b2ec8e9bf76563aeaf13515cefb15b658df0c8baa90]
<!-- rcw:end owner=source:src_96da25b1f1b45b27bc794d935a1a3196 block=evidence -->

## Researcher notes

