# databricks-solutions/ai-dev-kit

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit b059fd017a2c @ 8f133f51eafee394

## Summary (orientation draft, not independently verified)

The kit ships as four composable pieces: skills, a full-stack Builder App, a Python library (databricks-tools-core), and a standalone MCP server exposing 40+ Databricks tools. The databricks-tools-core Python library exposes functions such as execute_sql for direct use in Python projects, and is described as compatible with LangChain and the OpenAI Agents SDK. Evidence coverage: 162 of 175 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 7 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 16 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

16 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The kit ships as four composable pieces: skills, a full-stack Builder App, a Python library (databricks-tools-core), and a standalone MCP server exposing 40+ Databricks tools. -- evidence: [README.md#L382-L382](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L382-L382), [README.md#L390-L396](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L390-L396)
- design-choices (2 claim(s)):
  - [observation/documented] The databricks-apps-python skill defaults to AppKit (TypeScript + React) and falls back to Python frameworks (Dash, Streamlit, Flask, FastAPI, Gradio, Reflex); the APX framework lives in a separate repo. -- evidence: [README.md#L138-L138](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L138-L138)
  - [observation/documented] By default `databricks aitools install` installs the official databricks plugin through each agent's own plugin CLI for Claude Code, Codex, and Copilot, and writes raw skill files for Cursor, OpenCode, and Antigravity; --skills-only forces raw files everywhere. -- evidence: [README.md#L342-L347](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L342-L347)
- workflows (3 claim(s)):
  - [observation/documented] The installer records resolved refs, commit SHAs, and the aitools release in a skills.lock file inside a scope-local .ai-dev-kit/ state directory. -- evidence: [README.md#L248-L248](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L248-L248)
  - [observation/documented] For Genie Code, skills are uploaded to /Workspace/Users/<you>/.assistant/skills using a provided notebook that downloads skills from GitHub and uploads them via the Databricks SDK, including on serverless compute. -- evidence: [README.md#L360-L363](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L360-L363), [README.md#L356-L358](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L356-L358)
- skills-patterns (2 claim(s)):
  - [observation/documented] Skills are no longer bundled in this repo; they come from databricks/databricks-agent-skills via `databricks aitools install` and from mlflow/skills fetched from main (overridable with MLFLOW_REF). -- evidence: [README.md#L227-L228](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L227-L228), [README.md#L230-L233](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L230-L233), [README.md#L371-L378](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L371-L378), [README.md#L349-L352](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L349-L352)
  - [observation/documented] Several skills were renamed or consolidated in the official install, e.g. databricks-bundles to databricks-dabs, databricks-genie to databricks-genie-agents, and databricks-config merged into databricks-core. -- evidence: [README.md#L36-L37](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L36-L37), [README.md#L39-L45](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L39-L45)
- interfaces (3 claim(s)):
  - [observation/documented] The databricks-tools-core Python library exposes functions such as execute_sql for direct use in Python projects, and is described as compatible with LangChain and the OpenAI Agents SDK. -- evidence: [README.md#L329-L329](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L329-L329), [README.md#L323-L324](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L323-L324), [README.md#L321-L321](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L321-L321), [README.md#L326-L327](https://github.com/databricks-solutions/ai-dev-kit/blob/b059fd017a2c5743c31a0ff30dc8a618723aae4f/README.md#L326-L327)
More evidence: [full detail](ai-dev-kit.detail.md)

Metadata and full claim list: [full detail](ai-dev-kit.detail.md)
Human notes ([notes](ai-dev-kit.notes.md), never overwritten by build)

[Back to map index](../../index.md)
