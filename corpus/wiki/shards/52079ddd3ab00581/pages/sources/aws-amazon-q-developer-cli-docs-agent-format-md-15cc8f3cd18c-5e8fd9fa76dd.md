---
access: public
aliases: []
claim_ids:
- clm_11c8952ee4dd045db2b1fbf14af4701ddfc82f9c64f2da36143ddb7ad079735a
- clm_38051fa623c098bb314426402b8dabfb3b1c0c20d449a21a2eb35b7d131dd7b0
- clm_b400a4c7ebbb5a9d4ec926f0792c8c0de9874fbd1a0c8c6bb60e5425a4fdd314
- clm_e73a9f1cec7ee8e60e3c1afbf841c371d725b5d8b6390a1ca2ef22aba960911b
maturity: draft
page_id: pg_d27cb5e1b6a05b458b4d5e8fd9fa76dd
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_5f5191cabf8754eda03cc24c4622618c
title: aws/amazon-q-developer-cli/docs/agent-format.md @ 15cc8f3cd18c
updated_at: '2026-09-14T01:59:48Z'
---

# aws/amazon-q-developer-cli/docs/agent-format.md @ 15cc8f3cd18c

<!-- rcw:begin owner=source:src_5f5191cabf8754eda03cc24c4622618c block=evidence -->
- Each MCP server is configured with a required command plus optional args, env variables, and a per-request timeout in milliseconds defaulting to 120000. [@claim:clm_11c8952ee4dd045db2b1fbf14af4701ddfc82f9c64f2da36143ddb7ad079735a]
- Agent configurations are JSON files whose filename (minus .json) becomes the agent name; sections include name, description, prompt, mcpServers, tools, toolAliases, allowedTools, toolsSettings, resources, hooks, useLegacyMcpJson, and model. [@claim:clm_38051fa623c098bb314426402b8dabfb3b1c0c20d449a21a2eb35b7d131dd7b0]
- The prompt field accepts inline text or file:// URIs; relative paths resolve against the agent config file's directory and absolute paths are used as-is. [@claim:clm_b400a4c7ebbb5a9d4ec926f0792c8c0de9874fbd1a0c8c6bb60e5425a4fdd314]
- Hooks run commands at lifecycle trigger points: agentSpawn, userPromptSubmit, preToolUse (which can block tool use), postToolUse, and stop; each hook has a required command and an optional tool-name matcher. [@claim:clm_e73a9f1cec7ee8e60e3c1afbf841c371d725b5d8b6390a1ca2ef22aba960911b]
<!-- rcw:end owner=source:src_5f5191cabf8754eda03cc24c4622618c block=evidence -->

## Researcher notes

