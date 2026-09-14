# eigent-ai/eigent

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6bb55842f737 @ dc36965489dec4b6

## Summary (orientation draft, not independently verified)

The evidence is limited to the README and a design-system document of the eigent repository. It documents Eigent as an open-source, Electron-based multi-agent 'Cowork' desktop application built on CAMEL, with local or cloud deployment modes, plus contributor-facing setup and UI design guidelines. Evidence coverage: 162 of 400 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 9 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Eigent is described as an open-source Cowork desktop application for building, managing, and deploying a custom AI workforce that automates complex workflows. -- evidence: [README.md#L31-L31](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L31-L31)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The product is stated to be model agnostic, supporting cloud APIs, enterprise gateways, or local inference without vendor lock-in. -- evidence: [README.md#L37-L46](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L37-L46), [README.md#L185-L185](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L185-L185)
  - [observation/documented] Local deployment is the recommended mode: a local backend server with full API, local model integration (vLLM, Ollama, LM Studio, etc.), and complete isolation from cloud services with no account required. -- evidence: [README.md#L102-L105](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L102-L105), [README.md#L96-L96](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L96-L96), [README.md#L124-L124](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L124-L124)
- workflows (4 claim(s)):
  - [observation/documented] Repository development practice: the cloud-connected quick start instructs cloning the repo, running npm install and npm run dev (Node.js 18-22 required), and notes this mode connects to Eigent cloud services and needs account registration. -- evidence: [README.md#L113-L113](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L113-L113), [README.md#L117-L122](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L117-L122), [README.md#L124-L124](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L124-L124)
  - [observation/documented] Repository development practice: after pulling new code, contributors are told to update frontend dependencies with npm install and backend Python dependencies via 'cd backend && uv sync'. -- evidence: [README.md#L132-L132](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L132-L132), [README.md#L135-L137](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L135-L137), [README.md#L128-L128](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L128-L128)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The README lists built-in browser and terminal toolkits, MCP integration, and skill integration as product capabilities. -- evidence: [README.md#L37-L46](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L37-L46)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (1 claim(s)):
  - [observation/documented] The product advertises a multi-agent workforce that divides work among specialized agents, collaborates in parallel, and executes multi-step workflows, alongside a single-agent mode for focused tasks. -- evidence: [README.md#L33-L33](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L33-L33), [README.md#L173-L173](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L173-L173), [README.md#L37-L46](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L37-L46), [README.md#L169-L169](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L169-L169)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The backend stack is documented as FastAPI with uv as package manager, Uvicorn as async server, OAuth 2.0 and Passlib for authentication, and CAMEL as the multi-agent framework. -- evidence: [README.md#L255-L259](https://github.com/eigent-ai/eigent/blob/6bb55842f73766f7b219aa5ef5bcf5965f3acdaa/README.md#L255-L259)
More evidence: [full detail](eigent.detail.md)

Metadata and full claim list: [full detail](eigent.detail.md)
Human notes ([notes](eigent.notes.md), never overwritten by build)

[Back to map index](../../index.md)
