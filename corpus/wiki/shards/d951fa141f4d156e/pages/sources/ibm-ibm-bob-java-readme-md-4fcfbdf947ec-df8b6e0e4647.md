---
access: public
aliases: []
claim_ids:
- clm_4ace73f6aae3d01a8fd82a97011feb302808ae387dd11a612aabd6e60c7c3503
- clm_4ce42be0d1b32e89ad6522020ade52bd73ab3123386b4080d30876c9f5d4ac24
- clm_52c1a6f6b8562d47913994678fa0400ede3abc9130f92a8fdef95211219a8cb6
- clm_895a28e90ba4371319e28942c0a389e1f4206b5dec6c18ee87f6ed8fcffbf817
- clm_97389520db7b604cd54b71fcaf0d38223d43a93300f40966b7e12bdac0cc4d3d
- clm_a1aa1ea87ca3819eace909bf33628d78817a20034e736e582815f7b15569e7b7
- clm_bd29001a8dd6c50470f159340e8f8d26c5fc9847f1340bdd4e5a4df657889592
- clm_c0f29fa768eb53fcefcaa4a77fa6b934acc5d0523696bc17b0ad4d9566878d18
- clm_c88f4d38bf6f2d40f5fe54fc0829002177a9e5ab406379ba229d7b8e1a1313e5
- clm_e84d446d01f94472c6d8dd712f8195f219c750a562cdd8b0d1c15febb70c74ec
- clm_fbdcc359b5cbc33456c416fce8dee558f055fc512c4bd3928ca2861a804d4e22
- clm_fd0734775fe1e9d2b34ba73934cacb1c299c252107146a04d7f7cc84d2f41887
maturity: draft
page_id: pg_43b98516dca95aa1a6a3df8b6e0e4647
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_3075a4f240a150ddac8f28b99edaaca7
title: IBM/ibm-bob-java/README.md @ 4fcfbdf947ec
updated_at: '2026-09-14T04:56:03Z'
---

# IBM/ibm-bob-java/README.md @ 4fcfbdf947ec

<!-- rcw:begin owner=source:src_3075a4f240a150ddac8f28b99edaaca7 block=evidence -->
- The Spring Boot to Quarkus migration uses a modular, gate-driven flow that compiles after each phase, offers Spring Compatibility or Full Quarkus strategies, and verifies a clean build with no leftover Spring dependencies and a live health endpoint. [@claim:clm_4ace73f6aae3d01a8fd82a97011feb302808ae387dd11a612aabd6e60c7c3503]
- The vulnerability workflow parses Maven POM or Gradle files, queries the OSV.dev batch API in one request, renders CVSS-scored results in chat, and can launch a subtask that fixes vulnerable packages and verifies the build. [@claim:clm_4ce42be0d1b32e89ad6522020ade52bd73ab3123386b4080d30876c9f5d4ac24]
- SDKMAN or WinGet is needed only for the Java Upgrade workflow's automatic JDK install and switch steps, implying other workflows do not require them. [@claim:clm_52c1a6f6b8562d47913994678fa0400ede3abc9130f92a8fdef95211219a8cb6]
- Six workflows are offered: Java Upgrade, Liberty Modernization, Java Unit Testing, UI Modernization, Java Vulnerability Remediation, and Spring Boot to Quarkus Migration. [@claim:clm_895a28e90ba4371319e28942c0a389e1f4206b5dec6c18ee87f6ed8fcffbf817]
- The unit test workflow detects existing test setup, adds JaCoCo if absent, generates a project-specific strategy document, supports git-diff-based candidate selection, generates tests at package/class/method granularity, and reports pass/fail results. [@claim:clm_97389520db7b604cd54b71fcaf0d38223d43a93300f40966b7e12bdac0cc4d3d]
- The Java Upgrade workflow detects the environment (JDKs, Maven/Gradle, Java EE version, multi-module layout), installs JDKs via SDKMAN or WinGet, applies recipes, optionally migrates javax.* to jakarta.*, and runs an agentic fix loop until the build compiles. [@claim:clm_a1aa1ea87ca3819eace909bf33628d78817a20034e736e582815f7b15569e7b7]
- The UI Modernization workflow splits JSF/Struts monoliths into a Java backend exposing REST APIs plus a React frontend, with independently runnable phases and a validation step that runs both tiers. [@claim:clm_bd29001a8dd6c50470f159340e8f8d26c5fc9847f1340bdd4e5a4df657889592]
- The add-on does not work standalone: it requires IBM Bob as a dependency plus a Premium Package for Java Modernization subscription. [@claim:clm_c0f29fa768eb53fcefcaa4a77fa6b934acc5d0523696bc17b0ad4d9566878d18]
- The package is an add-on extending IBM Bob with AI-assisted Java modernization workflows surfaced natively in Bob chat, covering runtime upgrades, WebSphere-to-Liberty migration, test generation, UI modernization, and CVE elimination. [@claim:clm_c88f4d38bf6f2d40f5fe54fc0829002177a9e5ab406379ba229d7b8e1a1313e5]
- Workflows are launched from Bob by clicking Start Workflow or typing workflow names in the prompt; the Spring Boot to Quarkus migration can also be started with the /migrate-spring-to-quarkus command. [@claim:clm_e84d446d01f94472c6d8dd712f8195f219c750a562cdd8b0d1c15febb70c74ec]
- Java upgrade supports moving from Java 8 to LTS targets 11, 17, 21, or 25, and Jakarta EE 7 to EE 8, 9, 10, or 11, with Java and Jakarta EE upgrades runnable simultaneously. [@claim:clm_fbdcc359b5cbc33456c416fce8dee558f055fc512c4bd3928ca2861a804d4e22]
- The Liberty Modernization workflow requires an IBM AMA analysis report zip, injects server.xml and a Containerfile, runs OpenRewrite Liberty recipes via Maven or Gradle, and uses an AI subagent for remaining compatibility issues. [@claim:clm_fd0734775fe1e9d2b34ba73934cacb1c299c252107146a04d7f7cc84d2f41887]
<!-- rcw:end owner=source:src_3075a4f240a150ddac8f28b99edaaca7 block=evidence -->

## Researcher notes

