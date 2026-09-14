# thefalc/multi-agent-ai-sdr-flink-orchestrator

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a23673a0060c @ 00298777f2134b5f

## Summary (orientation draft, not independently verified)

The application uses Microsoft Azure OpenAI, Confluent, and Apache Flink to build an AI-based SDR that automates the lead management and outreach workflow. The system includes five agents: Lead Ingestion, Lead Scoring, Active Outreach, Nurture Campaign, and Send Email, each handling a distinct lead-processing task.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The application uses Microsoft Azure OpenAI, Confluent, and Apache Flink to build an AI-based SDR that automates the lead management and outreach workflow. -- evidence: [README.md#L4-L4](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L4-L4), [README.md#L2-L2](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L2-L2)
- components (3 claim(s)):
  - [observation/documented] The system includes five agents: Lead Ingestion, Lead Scoring, Active Outreach, Nurture Campaign, and Send Email, each handling a distinct lead-processing task. -- evidence: [README.md#L10-L14](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L10-L14)
  - [observation/documented] The Send Email Agent currently only prints the email to a terminal rather than actually sending it, which would require an email relay or service in a real deployment. -- evidence: [README.md#L10-L14](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L10-L14)
- design-choices (1 claim(s)):
  - [observation/documented] The web application is deliberately decoupled from the AI stack: it knows nothing about LLMs, Kafka, or Flink, which run on Confluent Cloud to move data between services. -- evidence: [README.md#L39-L39](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L39-L39)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Agent communication flows over Kafka topics agent_messages and agent_predictions, each governed by a JSON schema in Confluent Schema Registry; agent_predictions adds an agent_name field used for routing. -- evidence: [README.md#L271-L271](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L271-L271), [README.md#L183-L183](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L183-L183), [README.md#L110-L116](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L110-L116), [README.md#L193-L265](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L193-L265), [README.md#L185-L191](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L185-L191)
  - [observation/documented] HTTP sink connectors per agent deliver messages from agent_predictions to agent API endpoints, filtered by a Single Message Transform matching the agent's name. -- evidence: [README.md#L271-L271](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L271-L271), [README.md#L293-L293](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L293-L293), [README.md#L288-L291](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L288-L291)
- memory-state (1 claim(s)):
  - [observation/documented] Submitted leads are stored in a MongoDB database stratusdb (leads collection), and a MongoDB Atlas source connector publishes new leads into Kafka to kick off the workflow. -- evidence: [README.md#L63-L63](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L63-L63), [README.md#L25-L28](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L25-L28), [README.md#L65-L65](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L65-L65), [README.md#L90-L90](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L90-L90)
- orchestration (2 claim(s)):
  - [observation/documented] A Flink SQL job uses external model inference (an OpenAI gpt-4 model reference called agent_router) to map each agent_messages record to the next agent by name, writing results to agent_predictions. -- evidence: [README.md#L297-L297](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L297-L297), [README.md#L421-L438](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L421-L438), [README.md#L370-L380](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L370-L380)
  - [observation/documented] The router's system prompt instructs the model to output only a defined agent name, or NONE if it cannot confidently map the input to an agent. -- evidence: [README.md#L409-L413](https://github.com/thefalc/multi-agent-ai-sdr-flink-orchestrator/blob/a23673a0060c791fbaff3c0598be5ebac05c35ed/README.md#L409-L413)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](multi-agent-ai-sdr-flink-orchestrator.detail.md)

Metadata and full claim list: [full detail](multi-agent-ai-sdr-flink-orchestrator.detail.md)
Human notes ([notes](multi-agent-ai-sdr-flink-orchestrator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
