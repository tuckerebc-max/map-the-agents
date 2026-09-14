# Workflow-Dispatch (`workflow-dispatch`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: benc-uk
- License: MIT
- Language: TypeScript
- Interface: install=Add to a GitHub Actions workflow YAML: uses: benc-uk/workflow-dispatch@v1
- Model providers: None — CI/CD action, no AI models
- Feature flags (directory-reported):
  - mcp_support: no (no)
  - plugin_support: no (no)
  - claude_code_plugin: no (no)
  - subagents: no (no)
  - hooks: no (no)
  - plan_mode: no (no)

Repository map entry: [benc-uk/workflow-dispatch](../../repos/benc-uk/workflow-dispatch.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): GitHub Action for triggering other GitHub Actions workflows via the workflow_dispatch event; can wait for triggered workflow completion, poll run status, sync status, trigger workflows in other repos, and pass JSON inputs between workflows. (Not a coding agent harness — it's a CI/CD workflow chaining tool.)

(captured site page body (agents/workflow-dispatch.md), not a verified repo-code finding)
workflow-dispatch addresses the lack of native workflow-to-workflow chaining in GitHub Actions: it triggers other workflows through the workflow_dispatch event, optionally waits for their completion, polls run status, triggers workflows in other repositories, and passes JSON inputs between chained workflows. It is a conventional CI/CD action with no AI or agent behavior, included in the census only as a boundary case. CI authors use it to chain pipelines across repositories with status polling and JSON input passing.
Sources: [backing feed @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/_data/agents.json); [site page @ 0709cccb49af](https://github.com/prime-radiant-inc/alltheagents.org/blob/0709cccb49aff08a4b10beb95a214005a810a363/agents/workflow-dispatch.md)
