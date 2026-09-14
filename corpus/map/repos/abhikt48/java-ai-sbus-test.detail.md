# abhikt48/java-ai-sbus-test -- full detail

[Back to orientation](java-ai-sbus-test.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/abhikt48/java-ai-sbus-test/aa74eebe680943700ad9eb4ff4190657c95bb90c/a3b129d437f0a736.json](../../../wiki/dossiers/abhikt48/java-ai-sbus-test/aa74eebe680943700ad9eb4ff4190657c95bb90c/a3b129d437f0a736.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The project is described as a test project for applicationinsights-agent. -- evidence: [README.md#L2-L2](https://github.com/abhikt48/java-ai-sbus-test/blob/aa74eebe680943700ad9eb4ff4190657c95bb90c/README.md#L2-L2) (`clm_ea839858e2cbf89826bfdd3e4335a033df6588116c527c9bbd1f81174867257b`)

## design-choices (1 claim(s))

- [inference/documented] The 'codeless agent' naming and single -javaagent VM argument suggest the project uses agent-based (codeless) instrumentation rather than SDK code changes. -- evidence: [README.md#L5-L10](https://github.com/abhikt48/java-ai-sbus-test/blob/aa74eebe680943700ad9eb4ff4190657c95bb90c/README.md#L5-L10), [README.md#L2-L2](https://github.com/abhikt48/java-ai-sbus-test/blob/aa74eebe680943700ad9eb4ff4190657c95bb90c/README.md#L2-L2) (`clm_6454df724824f1fded497d67b5e2822690b27adaf8f7592cb68b7f3ce8799808`)

## workflows (2 claim(s))

- [observation/documented] Setup involves updating the connection string in applicationinsights.json and downloading/copying applicationinsights-agent-3.5.2.jar into the agent directory. -- evidence: [README.md#L5-L10](https://github.com/abhikt48/java-ai-sbus-test/blob/aa74eebe680943700ad9eb4ff4190657c95bb90c/README.md#L5-L10) (`clm_e2526cb2c7b5e71ed264664d8acbdbccc8729ecba1ebcbf46d808e521688ef37`)
- [observation/documented] The Service Bus configuration in TestCodelessAgentWithSbus.java is updated first, then the class is run with the single VM argument -javaagent pointing at the agent jar, which should start successfully. -- evidence: [README.md#L5-L10](https://github.com/abhikt48/java-ai-sbus-test/blob/aa74eebe680943700ad9eb4ff4190657c95bb90c/README.md#L5-L10) (`clm_9975cef44d162449e3667bab2e857960a5f3f0067c2d73dc8d45273f3fc0363b`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Per the README's final step, results are viewed by opening App Insight to inspect a dependency tree. -- evidence: [README.md#L5-L10](https://github.com/abhikt48/java-ai-sbus-test/blob/aa74eebe680943700ad9eb4ff4190657c95bb90c/README.md#L5-L10) (`clm_f05c8e989e1830473c4af717d5b9f1145dfb9443af69d2277e17794f64e376b8`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project relies on the Application Insights Java agent version 3.5.2 jar, downloaded separately and attached via -javaagent. -- evidence: [README.md#L5-L10](https://github.com/abhikt48/java-ai-sbus-test/blob/aa74eebe680943700ad9eb4ff4190657c95bb90c/README.md#L5-L10) (`clm_355ee9a63c09aa2bbd0936da238d7b4608c957eec306ff6d38f8030f93dc24e2`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

