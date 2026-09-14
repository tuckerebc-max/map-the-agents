# Aws-Mwaa-Local-Runner (`aws-mwaa-local-runner`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: aws
- License: MIT-0
- Language: Shell, Python, Docker
- Interface: platforms=CLI, IDE; install=git clone, docker
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: yes (Airflow plugins directory) (yes)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [aws/aws-mwaa-local-runner](../../repos/aws/aws-mwaa-local-runner.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Not an agent harness — a CLI utility that replicates an Amazon Managed Workflows for Apache Airflow (MWAA) environment locally via Docker, enabling local development/testing of DAGs, custom plugins, and dependencies before deploying to MWAA. Transitioning to legacy (production Docker image moved to amazon-mwaa-docker-images for Airflow 3.x).

(captured site page body (agents/aws-mwaa-local-runner.md), not a verified repo-code finding)
This AWS repository has nothing to do with coding agents: it is a CLI utility that builds a Docker container replicating an Amazon MWAA (Managed Workflows for Apache Airflow) environment locally, so developers can test DAGs, custom plugins, and requirements.txt packages before deploying to the managed service. Commands cover building the image, starting the local environment, and testing requirements/startup scripts against the MWAA production configuration. The repository was archived by AWS in August 2026, read-only, with users directed to the amazon-mwaa-docker-images repository, which open-sources MWAA's actual production images and supports Airflow 2.9+ and future 3.x releases. It appears in this census only because keyword-driven gap sweeps can misclassify infrastructure tooling; the correct category is 'other'.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/aws-mwaa-local-runner.md)
