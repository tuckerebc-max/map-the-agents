# trypromptly/llmstack

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 701348426fad @ 99e229211c89b3bc

## Summary (orientation draft, not independently verified)

The snapshot consists of README documentation describing LLMStack as a no-code platform for building generative AI agents, chains, and chatbots, including deployment, data import, multi-tenancy, and admin features; no source code is present in the provided slices.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] LLMStack is described as a no-code platform for building generative AI agents, workflows, and chatbots that connect to data and business processes. -- evidence: [README.md#L1-L9](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L1-L9)
- components (3 claim(s)):
  - [observation/documented] The platform imports data types such as CSV, TXT, PDF, DOCX, and PPTX from sources like Google Drive, Notion, websites, and uploads, then preprocesses and vectorizes it into an out-of-the-box vector database. -- evidence: [README.md#L66-L66](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L66-L66)
  - [observation/documented] On first run, LLMStack creates a .llmstack directory in the user's home containing the database and config files, and opens a browser to localhost:3000. -- evidence: [README.md#L47-L47](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L47-L47)
- design-choices (2 claim(s)):
  - [observation/documented] The platform lets users chain multiple LLMs together to build generative AI applications without coding, via a no-code builder. -- evidence: [README.md#L64-L64](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L64-L64), [README.md#L13-L13](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L13-L13), [README.md#L68-L68](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L68-L68)
  - [observation/documented] LLMStack is multi-tenant: users can create multiple organizations, and users can only access data and AI chains belonging to their organization. -- evidence: [README.md#L74-L74](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L74-L74)
- workflows (2 claim(s)):
  - [observation/documented] LLMStack is installed with 'pip install llmstack' and started with the 'llmstack' command; Windows users are directed to use WSL2. -- evidence: [README.md#L39-L39](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L39-L39), [README.md#L43-L45](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L43-L45), [README.md#L35-L37](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L35-L37)
  - [observation/documented] Repository development practice: the README points contributors to an external development guide and a contributing guide at docs.trypromptly.com for how to run, develop, and contribute to LLMStack. -- evidence: [README.md#L116-L116](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L116-L116), [README.md#L112-L112](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L112-L112)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Apps and chatbots built with LLMStack are accessible via an HTTP API, and AI chains can be triggered from Slack or Discord. -- evidence: [README.md#L72-L72](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L72-L72), [README.md#L96-L96](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L96-L96)
  - [observation/documented] An admin panel at localhost:3000/admin lets administrators add users and assign them to organizations. -- evidence: [README.md#L100-L100](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L100-L100)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (1 claim(s)):
  - [observation/documented] Users can add provider API keys (e.g., OpenAI, Cohere, Stability) from the Settings page, and instance-wide default keys can be placed in ~/.llmstack/config. -- evidence: [README.md#L49-L49](https://github.com/trypromptly/LLMStack/blob/701348426fadd0536de8b72536216a9c0365f25b/README.md#L49-L49)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](llmstack.detail.md)

Metadata and full claim list: [full detail](llmstack.detail.md)
Human notes ([notes](llmstack.notes.md), never overwritten by build)

[Back to map index](../../index.md)
