---
access: public
aliases: []
claim_ids:
- clm_1acbc824acf66ffc8235e94f9bddc2a4de228ddf8f431037054be119bff63978
- clm_2265ce135f8dc64370949aebc1f8324ef999e341e6c21c99258f2df640f0d39d
- clm_535c230bd39a799a0b3f1e49925000f5552e2ab2d40fad7ba0022daf9b864573
- clm_536e071ebfbc508e414c28c61a727ae826fcfc63d102fba0be2f2458b2763d94
- clm_7287e77f1cb7976e109843e7329621e63ce518929767bccd33fc93793808c23c
- clm_796714e23a955cde4a61be2aa37309ea5369a74af1d7afe47c40c7cc7570b84f
- clm_88d1b7fcf4516ecf35dce607ccd21aed943892b01488a05a2b12a5757acef60c
- clm_9283fe5ae8ffb57bfd3b456b38c4a6b62c2c88c456ae4f39ed89f1b62e9551ba
- clm_9e24949ec60398aba793aee5e96276ef09dfa3eaf2272b9cbda84cc91c97741c
- clm_a947ebcf1d0fe7176cd2f6d66d8677e630911ed691fd660b8c75d0a6ae46ac31
- clm_abfe578f84687bd4ff68b74398b07e817286a0a6c196780bd6099665d6246fa9
- clm_af20057da8241d9ee6384813c0f728ac2df2e9a9ffcbf80c1bfad96b4fc8f525
maturity: draft
page_id: pg_b03efebc7ec95eeeaae54292115bd6b9
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_34ebeca89338519681132a82efc23551
title: thefalc/multi-agent-ai-sdr-flink-orchestrator/README.md @ a23673a0060c
updated_at: '2026-09-14T04:26:31Z'
---

# thefalc/multi-agent-ai-sdr-flink-orchestrator/README.md @ a23673a0060c

<!-- rcw:begin owner=source:src_34ebeca89338519681132a82efc23551 block=evidence -->
- The Send Email Agent currently only prints the email to a terminal rather than actually sending it, which would require an email relay or service in a real deployment. [@claim:clm_1acbc824acf66ffc8235e94f9bddc2a4de228ddf8f431037054be119bff63978]
- The project splits into a NextJS web-application (React frontend, Node backend, MongoDB) and a Python agents app exposing API endpoints that Confluent connectors call. [@claim:clm_2265ce135f8dc64370949aebc1f8324ef999e341e6c21c99258f2df640f0d39d]
- A Flink SQL job uses external model inference (an OpenAI gpt-4 model reference called agent_router) to map each agent_messages record to the next agent by name, writing results to agent_predictions. [@claim:clm_535c230bd39a799a0b3f1e49925000f5552e2ab2d40fad7ba0022daf9b864573]
- The author notes MongoDB is used for lead storage only for demo purposes; in a real-world scenario leads would likely live in a marketing automation platform or CRM. [@claim:clm_536e071ebfbc508e414c28c61a727ae826fcfc63d102fba0be2f2458b2763d94]
- The web application is deliberately decoupled from the AI stack: it knows nothing about LLMs, Kafka, or Flink, which run on Confluent Cloud to move data between services. [@claim:clm_7287e77f1cb7976e109843e7329621e63ce518929767bccd33fc93793808c23c]
- Running the application requires Node v22.5.1+, Python 3.10+, a Confluent Cloud account, an Azure OpenAI API key, and a MongoDB account. [@claim:clm_796714e23a955cde4a61be2aa37309ea5369a74af1d7afe47c40c7cc7570b84f]
- The system includes five agents: Lead Ingestion, Lead Scoring, Active Outreach, Nurture Campaign, and Send Email, each handling a distinct lead-processing task. [@claim:clm_88d1b7fcf4516ecf35dce607ccd21aed943892b01488a05a2b12a5757acef60c]
- HTTP sink connectors per agent deliver messages from agent_predictions to agent API endpoints, filtered by a Single Message Transform matching the agent's name. [@claim:clm_9283fe5ae8ffb57bfd3b456b38c4a6b62c2c88c456ae4f39ed89f1b62e9551ba]
- The router's system prompt instructs the model to output only a defined agent name, or NONE if it cannot confidently map the input to an agent. [@claim:clm_9e24949ec60398aba793aee5e96276ef09dfa3eaf2272b9cbda84cc91c97741c]
- Agent communication flows over Kafka topics agent_messages and agent_predictions, each governed by a JSON schema in Confluent Schema Registry; agent_predictions adds an agent_name field used for routing. [@claim:clm_a947ebcf1d0fe7176cd2f6d66d8677e630911ed691fd660b8c75d0a6ae46ac31]
- Submitted leads are stored in a MongoDB database stratusdb (leads collection), and a MongoDB Atlas source connector publishes new leads into Kafka to kick off the workflow. [@claim:clm_abfe578f84687bd4ff68b74398b07e817286a0a6c196780bd6099665d6246fa9]
- The application uses Microsoft Azure OpenAI, Confluent, and Apache Flink to build an AI-based SDR that automates the lead management and outreach workflow. [@claim:clm_af20057da8241d9ee6384813c0f728ac2df2e9a9ffcbf80c1bfad96b4fc8f525]
<!-- rcw:end owner=source:src_34ebeca89338519681132a82efc23551 block=evidence -->

## Researcher notes

