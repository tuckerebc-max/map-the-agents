# ibm/ibm-bob-java

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 4fcfbdf947ec @ cba65145881bc2a7

## Summary (orientation draft, not independently verified)

The package is an add-on extending IBM Bob with AI-assisted Java modernization workflows surfaced natively in Bob chat, covering runtime upgrades, WebSphere-to-Liberty migration, test generation, UI modernization, and CVE elimination, offering six workflows: Java Upgrade, Liberty Modernization, Java Unit Testing, UI Modernization, Java Vulnerability Remediation, and Spring Boot to Quarkus Migration. Evidence: 2 of 2 candidate files stored (README.md, CHANGELOG.md); selection complete.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 12 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

12 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] The package is an add-on extending IBM Bob with AI-assisted Java modernization workflows surfaced natively in Bob chat, covering runtime upgrades, WebSphere-to-Liberty migration, test generation, UI modernization, and CVE elimination. -- evidence: [README.md#L3-L3](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L3-L3)
  - [observation/documented] Java upgrade supports moving from Java 8 to LTS targets 11, 17, 21, or 25, and Jakarta EE 7 to EE 8, 9, 10, or 11, with Java and Jakarta EE upgrades runnable simultaneously. -- evidence: [README.md#L174-L176](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L174-L176)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (6 claim(s)):
  - [observation/documented] The Java Upgrade workflow detects the environment (JDKs, Maven/Gradle, Java EE version, multi-module layout), installs JDKs via SDKMAN or WinGet, applies recipes, optionally migrates javax.* to jakarta.*, and runs an agentic fix loop until the build compiles. -- evidence: [README.md#L55-L61](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L55-L61)
  - [observation/documented] The Liberty Modernization workflow requires an IBM AMA analysis report zip, injects server.xml and a Containerfile, runs OpenRewrite Liberty recipes via Maven or Gradle, and uses an AI subagent for remaining compatibility issues. -- evidence: [README.md#L67-L67](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L67-L67), [README.md#L188-L188](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L188-L188), [README.md#L71-L75](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L71-L75)
- skills-patterns (1 claim(s)):
  - [observation/documented] Six workflows are offered: Java Upgrade, Liberty Modernization, Java Unit Testing, UI Modernization, Java Vulnerability Remediation, and Spring Boot to Quarkus Migration. -- evidence: [README.md#L8-L22](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L8-L22), [README.md#L28-L35](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L28-L35)
- interfaces (1 claim(s)):
  - [observation/documented] Workflows are launched from Bob by clicking Start Workflow or typing workflow names in the prompt; the Spring Boot to Quarkus migration can also be started with the /migrate-spring-to-quarkus command. -- evidence: [README.md#L143-L143](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L143-L143), [README.md#L132-L141](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L132-L141)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The add-on does not work standalone: it requires IBM Bob as a dependency plus a Premium Package for Java Modernization subscription. -- evidence: [README.md#L147-L148](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L147-L148), [README.md#L168-L168](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L168-L168)
- limitations (1 claim(s)):
More evidence: [full detail](ibm-bob-java.detail.md)

Metadata and full claim list: [full detail](ibm-bob-java.detail.md)
Human notes ([notes](ibm-bob-java.notes.md), never overwritten by build)

[Back to map index](../../index.md)
