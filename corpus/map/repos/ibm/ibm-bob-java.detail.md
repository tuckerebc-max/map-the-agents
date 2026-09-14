# ibm/ibm-bob-java -- full detail

[Back to orientation](ibm-bob-java.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ibm/ibm-bob-java/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/cba65145881bc2a7.json](../../../wiki/dossiers/ibm/ibm-bob-java/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/cba65145881bc2a7.json)

## specifications (2 claim(s))

- [observation/documented] The package is an add-on extending IBM Bob with AI-assisted Java modernization workflows surfaced natively in Bob chat, covering runtime upgrades, WebSphere-to-Liberty migration, test generation, UI modernization, and CVE elimination. -- evidence: [README.md#L3-L3](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L3-L3) (`clm_c88f4d38bf6f2d40f5fe54fc0829002177a9e5ab406379ba229d7b8e1a1313e5`)
- [observation/documented] Java upgrade supports moving from Java 8 to LTS targets 11, 17, 21, or 25, and Jakarta EE 7 to EE 8, 9, 10, or 11, with Java and Jakarta EE upgrades runnable simultaneously. -- evidence: [README.md#L174-L176](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L174-L176) (`clm_fbdcc359b5cbc33456c416fce8dee558f055fc512c4bd3928ca2861a804d4e22`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (6 claim(s))

- [observation/documented] The Java Upgrade workflow detects the environment (JDKs, Maven/Gradle, Java EE version, multi-module layout), installs JDKs via SDKMAN or WinGet, applies recipes, optionally migrates javax.* to jakarta.*, and runs an agentic fix loop until the build compiles. -- evidence: [README.md#L55-L61](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L55-L61) (`clm_a1aa1ea87ca3819eace909bf33628d78817a20034e736e582815f7b15569e7b7`)
- [observation/documented] The Liberty Modernization workflow requires an IBM AMA analysis report zip, injects server.xml and a Containerfile, runs OpenRewrite Liberty recipes via Maven or Gradle, and uses an AI subagent for remaining compatibility issues. -- evidence: [README.md#L67-L67](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L67-L67), [README.md#L188-L188](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L188-L188), [README.md#L71-L75](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L71-L75) (`clm_fd0734775fe1e9d2b34ba73934cacb1c299c252107146a04d7f7cc84d2f41887`)
- [observation/documented] The unit test workflow detects existing test setup, adds JaCoCo if absent, generates a project-specific strategy document, supports git-diff-based candidate selection, generates tests at package/class/method granularity, and reports pass/fail results. -- evidence: [README.md#L90-L90](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L90-L90), [README.md#L83-L88](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L83-L88) (`clm_97389520db7b604cd54b71fcaf0d38223d43a93300f40966b7e12bdac0cc4d3d`)
- [observation/documented] The UI Modernization workflow splits JSF/Struts monoliths into a Java backend exposing REST APIs plus a React frontend, with independently runnable phases and a validation step that runs both tiers. -- evidence: [README.md#L98-L103](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L98-L103), [README.md#L94-L94](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L94-L94), [README.md#L105-L105](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L105-L105) (`clm_bd29001a8dd6c50470f159340e8f8d26c5fc9847f1340bdd4e5a4df657889592`)
- [observation/documented] The vulnerability workflow parses Maven POM or Gradle files, queries the OSV.dev batch API in one request, renders CVSS-scored results in chat, and can launch a subtask that fixes vulnerable packages and verifies the build. -- evidence: [README.md#L109-L109](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L109-L109), [README.md#L113-L116](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L113-L116) (`clm_4ce42be0d1b32e89ad6522020ade52bd73ab3123386b4080d30876c9f5d4ac24`)
- [observation/documented] The Spring Boot to Quarkus migration uses a modular, gate-driven flow that compiles after each phase, offers Spring Compatibility or Full Quarkus strategies, and verifies a clean build with no leftover Spring dependencies and a live health endpoint. -- evidence: [README.md#L120-L120](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L120-L120), [README.md#L124-L126](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L124-L126) (`clm_4ace73f6aae3d01a8fd82a97011feb302808ae387dd11a612aabd6e60c7c3503`)

## skills-patterns (1 claim(s))

- [observation/documented] Six workflows are offered: Java Upgrade, Liberty Modernization, Java Unit Testing, UI Modernization, Java Vulnerability Remediation, and Spring Boot to Quarkus Migration. -- evidence: [README.md#L8-L22](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L8-L22), [README.md#L28-L35](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L28-L35) (`clm_895a28e90ba4371319e28942c0a389e1f4206b5dec6c18ee87f6ed8fcffbf817`)

## interfaces (1 claim(s))

- [observation/documented] Workflows are launched from Bob by clicking Start Workflow or typing workflow names in the prompt; the Spring Boot to Quarkus migration can also be started with the /migrate-spring-to-quarkus command. -- evidence: [README.md#L143-L143](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L143-L143), [README.md#L132-L141](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L132-L141) (`clm_e84d446d01f94472c6d8dd712f8195f219c750a562cdd8b0d1c15febb70c74ec`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The add-on does not work standalone: it requires IBM Bob as a dependency plus a Premium Package for Java Modernization subscription. -- evidence: [README.md#L147-L148](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L147-L148), [README.md#L168-L168](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L168-L168) (`clm_c0f29fa768eb53fcefcaa4a77fa6b934acc5d0523696bc17b0ad4d9566878d18`)

## limitations (1 claim(s))

- [observation/documented] SDKMAN or WinGet is needed only for the Java Upgrade workflow's automatic JDK install and switch steps, implying other workflows do not require them. -- evidence: [README.md#L55-L61](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L55-L61), [README.md#L180-L180](https://github.com/IBM/ibm-bob-java/blob/4fcfbdf947ec673321f7a08d5fe67958f0dc12ae/README.md#L180-L180) (`clm_52c1a6f6b8562d47913994678fa0400ede3abc9130f92a8fdef95211219a8cb6`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

Superseded claim IDs (kept as history): clm_95016b22570053fcb57a7b5e6576cca5a486d4ee95257eedb9006a92aa59d856

