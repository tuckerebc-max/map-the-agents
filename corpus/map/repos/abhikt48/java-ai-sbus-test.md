# abhikt48/java-ai-sbus-test

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit aa74eebe6809 @ a3b129d437f0a736

## Summary (orientation draft, not independently verified)

The repository is a small test project for the Application Insights Java agent: the README describes attaching applicationinsights-agent-3.5.2.jar via a -javaagent VM argument to a Service Bus test class and viewing results in App Insights.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 6 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

6 claim(s) across 5 facet(s); 8 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The project is described as a test project for applicationinsights-agent. -- evidence: [README.md#L2-L2](https://github.com/abhikt48/java-ai-sbus-test/blob/aa74eebe680943700ad9eb4ff4190657c95bb90c/README.md#L2-L2)
- design-choices (1 claim(s)):
  - [inference/documented] The 'codeless agent' naming and single -javaagent VM argument suggest the project uses agent-based (codeless) instrumentation rather than SDK code changes. -- evidence: [README.md#L5-L10](https://github.com/abhikt48/java-ai-sbus-test/blob/aa74eebe680943700ad9eb4ff4190657c95bb90c/README.md#L5-L10), [README.md#L2-L2](https://github.com/abhikt48/java-ai-sbus-test/blob/aa74eebe680943700ad9eb4ff4190657c95bb90c/README.md#L2-L2)
- workflows (2 claim(s)):
  - [observation/documented] Setup involves updating the connection string in applicationinsights.json and downloading/copying applicationinsights-agent-3.5.2.jar into the agent directory. -- evidence: [README.md#L5-L10](https://github.com/abhikt48/java-ai-sbus-test/blob/aa74eebe680943700ad9eb4ff4190657c95bb90c/README.md#L5-L10)
  - [observation/documented] The Service Bus configuration in TestCodelessAgentWithSbus.java is updated first, then the class is run with the single VM argument -javaagent pointing at the agent jar, which should start successfully. -- evidence: [README.md#L5-L10](https://github.com/abhikt48/java-ai-sbus-test/blob/aa74eebe680943700ad9eb4ff4190657c95bb90c/README.md#L5-L10)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] Per the README's final step, results are viewed by opening App Insight to inspect a dependency tree. -- evidence: [README.md#L5-L10](https://github.com/abhikt48/java-ai-sbus-test/blob/aa74eebe680943700ad9eb4ff4190657c95bb90c/README.md#L5-L10)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The project relies on the Application Insights Java agent version 3.5.2 jar, downloaded separately and attached via -javaagent. -- evidence: [README.md#L5-L10](https://github.com/abhikt48/java-ai-sbus-test/blob/aa74eebe680943700ad9eb4ff4190657c95bb90c/README.md#L5-L10)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

Every claim for this repository is shown above and in [full detail](java-ai-sbus-test.detail.md).

Metadata and full claim list: [full detail](java-ai-sbus-test.detail.md)
Human notes ([notes](java-ai-sbus-test.notes.md), never overwritten by build)

[Back to map index](../../index.md)
