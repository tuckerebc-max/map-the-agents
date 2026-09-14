# coze-dev/coze-studio

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fefb05ff27be @ 9ba9c01ea3d00373

## Summary (orientation draft, not independently verified)

Coze Studio is described as an all-in-one AI agent development tool offering models, tools, and development modes from development through deployment. Feature modules include model service management, agent building, app building, workflow building, resource development (plugins, knowledge bases, databases, prompts), and API/SDK integration.

## Source coverage

Source coverage (partial): 5 of 5 candidate file(s) selected; repository tree truncated (partial listing). Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Coze Studio is described as an all-in-one AI agent development tool offering models, tools, and development modes from development through deployment. -- evidence: [README.md#L20-L20](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md#L20-L20)
- components (1 claim(s)):
  - [observation/documented] Feature modules include model service management, agent building, app building, workflow building, resource development (plugins, knowledge bases, databases, prompts), and API/SDK integration. -- evidence: [README.md#L29-L36](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md#L29-L36)
- design-choices (1 claim(s)):
  - [observation/documented] The backend is written in Golang, the frontend in React + TypeScript, with a microservices architecture following domain-driven design principles. -- evidence: [README.md#L27-L27](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md#L27-L27)
- workflows (5 claim(s)):
  - [observation/documented] Repository development practice: contributors use a Rush.js monorepo with 135+ frontend packages, run tests via rush test / go test, and follow coverage targets by package level (80% for level 1). -- evidence: [CLAUDE.md#L70-L71](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CLAUDE.md#L70-L71), [CLAUDE.md#L56-L60](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CLAUDE.md#L56-L60), [CLAUDE.md#L151-L153](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CLAUDE.md#L151-L153), [CLAUDE.md#L7-L7](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CLAUDE.md#L7-L7)
  - [observation/documented] Repository development practice: PRs should follow AngularJS commit message conventions, pass lint (gofmt, golangci-lint), and include test cases; git-flow branching is used. -- evidence: [CONTRIBUTING.md#L44-L47](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CONTRIBUTING.md#L44-L47), [CONTRIBUTING.md#L25-L41](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CONTRIBUTING.md#L25-L41), [CONTRIBUTING.md#L7-L7](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/CONTRIBUTING.md#L7-L7)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] The Community Edition API and Chat SDK authenticate via Personal Access Token and provide conversation and workflow APIs; agents or apps can be embedded via Chat SDK. -- evidence: [README.md#L89-L94](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md#L89-L94), [README.md#L75-L83](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md#L75-L83)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The project credits the Eino framework for agent/workflow runtime and knowledge retrieval, FlowGram for the workflow canvas editor, and Hertz as the Go HTTP framework. -- evidence: [README.md#L129-L132](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md#L129-L132)
- limitations (2 claim(s)):
  - [observation/documented] The README warns that public-network deployment carries risks including account registration, Python execution in workflow code nodes, SSRF, and API privilege-escalation issues, recommending protective measures. -- evidence: [README.md#L70-L71](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md#L70-L71)
  - [observation/documented] Some features, such as tone customization, are limited to the commercial version and not available in the open-source edition. -- evidence: [README.md#L86-L86](https://github.com/coze-dev/coze-studio/blob/fefb05ff27be1da939612fbf9faf5db62583b8ae/README.md#L86-L86)
- relevance: unknown (no source-linked claim submitted for this facet)

(3 additional claim(s) omitted for length; see [full detail](coze-studio.detail.md) for every claim.)

Metadata and full claim list: [full detail](coze-studio.detail.md)
Human notes ([notes](coze-studio.notes.md), never overwritten by build)

[Back to map index](../../index.md)
