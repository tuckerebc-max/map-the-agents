# thefalc/multi-agent-ai-sdr-flink-orchestrator -- full detail

[Back to orientation](multi-agent-ai-sdr-flink-orchestrator.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/254986ae/6e488524/a23673a0060c791fbaff3c0598be5ebac05c35ed/00298777f2134b5f.json](../../../wiki/dossiers/254986ae/6e488524/a23673a0060c791fbaff3c0598be5ebac05c35ed/00298777f2134b5f.json)

## specifications (1 claim(s))

- [observation/documented] The application uses Microsoft Azure OpenAI, Confluent, and Apache Flink to build an AI-based SDR that automates the lead management and outreach workflow. -- evidence: [README.md#L4-L4](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L4-L4), [README.md#L2-L2](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L2-L2) (`clm_af20057da8241d9ee6384813c0f728ac2df2e9a9ffcbf80c1bfad96b4fc8f525`)

## components (3 claim(s))

- [observation/documented] The system includes five agents: Lead Ingestion, Lead Scoring, Active Outreach, Nurture Campaign, and Send Email, each handling a distinct lead-processing task. -- evidence: [README.md#L10-L14](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L10-L14) (`clm_88d1b7fcf4516ecf35dce607ccd21aed943892b01488a05a2b12a5757acef60c`)
- [observation/documented] The Send Email Agent currently only prints the email to a terminal rather than actually sending it, which would require an email relay or service in a real deployment. -- evidence: [README.md#L10-L14](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L10-L14) (`clm_1acbc824acf66ffc8235e94f9bddc2a4de228ddf8f431037054be119bff63978`)
- [observation/documented] The project splits into a NextJS web-application (React frontend, Node backend, MongoDB) and a Python agents app exposing API endpoints that Confluent connectors call. -- evidence: [README.md#L34-L34](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L34-L34), [README.md#L41-L41](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L41-L41) (`clm_2265ce135f8dc64370949aebc1f8324ef999e341e6c21c99258f2df640f0d39d`)

## design-choices (1 claim(s))

- [observation/documented] The web application is deliberately decoupled from the AI stack: it knows nothing about LLMs, Kafka, or Flink, which run on Confluent Cloud to move data between services. -- evidence: [README.md#L39-L39](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L39-L39) (`clm_7287e77f1cb7976e109843e7329621e63ce518929767bccd33fc93793808c23c`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Agent communication flows over Kafka topics agent_messages and agent_predictions, each governed by a JSON schema in Confluent Schema Registry; agent_predictions adds an agent_name field used for routing. -- evidence: [README.md#L271-L271](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L271-L271), [README.md#L183-L183](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L183-L183), [README.md#L110-L116](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L110-L116), [README.md#L193-L265](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L193-L265), [README.md#L185-L191](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L185-L191) (`clm_a947ebcf1d0fe7176cd2f6d66d8677e630911ed691fd660b8c75d0a6ae46ac31`)
- [observation/documented] HTTP sink connectors per agent deliver messages from agent_predictions to agent API endpoints, filtered by a Single Message Transform matching the agent's name. -- evidence: [README.md#L271-L271](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L271-L271), [README.md#L293-L293](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L293-L293), [README.md#L288-L291](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L288-L291) (`clm_9283fe5ae8ffb57bfd3b456b38c4a6b62c2c88c456ae4f39ed89f1b62e9551ba`)

## memory-state (1 claim(s))

- [observation/documented] Submitted leads are stored in a MongoDB database stratusdb (leads collection), and a MongoDB Atlas source connector publishes new leads into Kafka to kick off the workflow. -- evidence: [README.md#L63-L63](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L63-L63), [README.md#L25-L28](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L25-L28), [README.md#L65-L65](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L65-L65), [README.md#L90-L90](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L90-L90) (`clm_abfe578f84687bd4ff68b74398b07e817286a0a6c196780bd6099665d6246fa9`)

## orchestration (2 claim(s))

- [observation/documented] A Flink SQL job uses external model inference (an OpenAI gpt-4 model reference called agent_router) to map each agent_messages record to the next agent by name, writing results to agent_predictions. -- evidence: [README.md#L297-L297](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L297-L297), [README.md#L421-L438](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L421-L438), [README.md#L370-L380](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L370-L380) (`clm_535c230bd39a799a0b3f1e49925000f5552e2ab2d40fad7ba0022daf9b864573`)
- [observation/documented] The router's system prompt instructs the model to output only a defined agent name, or NONE if it cannot confidently map the input to an agent. -- evidence: [README.md#L409-L413](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L409-L413) (`clm_9e24949ec60398aba793aee5e96276ef09dfa3eaf2272b9cbda84cc91c97741c`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Running the application requires Node v22.5.1+, Python 3.10+, a Confluent Cloud account, an Azure OpenAI API key, and a MongoDB account. -- evidence: [README.md#L46-L50](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L46-L50) (`clm_796714e23a955cde4a61be2aa37309ea5369a74af1d7afe47c40c7cc7570b84f`)

## limitations (1 claim(s))

- [observation/documented] The author notes MongoDB is used for lead storage only for demo purposes; in a real-world scenario leads would likely live in a marketing automation platform or CRM. -- evidence: [README.md#L36-L37](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L36-L37) (`clm_536e071ebfbc508e414c28c61a727ae826fcfc63d102fba0be2f2458b2763d94`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

