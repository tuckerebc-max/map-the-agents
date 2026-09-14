# IBM Bob Premium Package for Java Modernization

Bring Enterprise Java modernization directly into Bob. **IBM Bob Premium Package for Java** extends [IBM Bob](https://bob.ibm.com) with AI-assisted workflows surfaced natively in Bob chat — upgrade runtimes, migrate from WebSphere to Liberty, generate test coverage, rearchitect legacy UIs, and eliminate CVEs — all without leaving Bob.

<details>
<summary>Table of Contents</summary>

- [Workflows at a Glance](#workflows-at-a-glance)
- [Why Bob Premium Package for Java](#why-bob-premium-package-for-java)
- [Key Capabilities](#key-capabilities)
    - [Java Upgrade](#java-upgrade)
    - [Liberty Modernization](#websphere-to-liberty-modernization)
    - [Java Unit Test Generation](#java-unit-test-generation)
    - [UI Modernization](#ui-modernization)
    - [Java Vulnerability Remediation](#java-vulnerability-remediation)
    - [Spring Boot to Quarkus Migration](#spring-boot-to-quarkus-migration)
- [Getting Started](#getting-started)
- [Requirements](#requirements)
- [Screenshots](#screenshots)
- [FAQ](#faq)
- [Feedback and Support](#feedback-and-support)
- [License](#license)

</details>

## Workflows at a Glance

| Workflow                                                     | What it does                                                                  |
| ------------------------------------------------------------ | ----------------------------------------------------------------------------- |
| [**Java Upgrade**](#java-upgrade)                            | Upgrade to Java 11 → 17 → 21 → 25 with automated recipes + agentic fix loops  |
| [**Liberty Modernization**](#websphere-to-liberty-modernization) | Modernize from WebSphere traditional to Liberty using AMA analysis reports      |
| [**Java Unit Testing**](#java-unit-test-generation)          | Auto-generate JUnit tests with JaCoCo coverage, guided by a strategy document |
| [**UI Modernization**](#ui-modernization)                    | Split JSF/Struts monoliths into a Java backend + React frontend               |
| [**Java Vulnerability Remediation**](#java-vulnerability-remediation) | Scan every Maven/Gradle dependency against CVE database                       |
| [**Spring Boot to Quarkus Migration**](#spring-boot-to-quarkus-migration)        | Modular, gate-driven skill flow with validations after every phase |

![alt text][screens-flows]

[screens-flows]: ./assets/screenshots/flows.png "Java Modernization flows in chat"

## Why Bob Premium Package for Java

Modernizing Java applications takes more than generating code. It requires deep knowledge of the ecosystem, a structured approach to each scenario, and tooling that can handle the complexity of real enterprise codebases — multi-module projects, legacy middleware, aging test suites, and dependency sprawl.

Bob Premium Package for Java brings that expertise directly into Bob as guided, multi-step workflows. Each workflow encodes proven modernization practices into discrete, repeatable steps that run inside the editor where the code lives.

## Key Capabilities

### Java Upgrade

Upgrades Java applications across four LTS targets: **Java 11, 17, 21, and 25**.

The workflow:

1. **Detects your environment** — reads installed JDKs, identifies your build tool (Maven or Gradle), Java EE version, and multi-module layout.
2. **Installs and switches Java** via SDKMAN (Linux/macOS) or WinGet (Windows).
3. **Runs Automated recipes** — selects the correct recipe and applies it against your build, tracking every modified file as a diff.
4. **Optional Jakarta EE migration** — simultaneously upgrades `javax.*` namespaces to `jakarta.*` using targeted EE recipes.
5. **Builds and parses** — runs your build, extracts structured errors and warnings from Maven or Gradle logs, and groups them by root cause.
6. **Agentic fix loop** — an AI subagent works through each error category, applies fixes, and re-builds until the project compiles cleanly.
7. **Generates a Mermaid diagram** summarizing every task, token spend, and execution time.

Supports Maven and Gradle projects, including multi-module builds.

### WebSphere to Liberty Modernization

Modernizes applications from **WebSphere Application Server traditional** to **IBM WebSphere Liberty**, guided by an [IBM Application Modernization Accelerator (AMA)](https://www.ibm.com/docs/en/ama?topic=about-application-modernization-accelerator) analysis report.

The workflow:

1. **Reads your AMA migration plan** — unpacks the archive and the enrichment report
2. **Injects Liberty config** — copies `server.xml` and a `Containerfile` from the AMA into the correct project paths, handling multi-module layouts automatically.
3. **Runs Liberty recipes** — applies OpenRewrite Liberty replatforming recipes via Maven or Gradle.
4. **Agentic replatforming** — an AI subagent resolves remaining compatibility issues flagged in the AMA report.
5. **Generates deployment guidance** — produces a Liberty deployment step and a Mermaid progress diagram.

### Java Unit Test Generation

Systematically grows test coverage using an AI-driven, strategy-first approach.

The workflow:

1. **Detects your test setup** — finds existing test files, frameworks (JUnit, TestNG), build commands, and coverage tools.
2. **Installs JaCoCo** — if no coverage tool is configured, adds JaCoCo to the build automatically.
3. **Generates a strategy document** — creates a project-specific unit testing strategy file that guides all subsequent generation.
4. **Selects candidates** — lets you choose which packages, classes, or methods to target (supports git-diff-based selection for changed code only).
5. **Generates tests** — runs targeted AI generation at the package, class, or method level, using the strategy document and existing test files as context.
6. **Runs tests and reports** — executes the new tests and summarizes pass/fail results.

Test generation is scoped to the right granularity: a single method gets a focused prompt; a full package gets a broader one.

### UI Modernization

Separates legacy **JSF or Struts** monoliths into a decoupled **Java backend + React frontend** — with control over which parts to modernize.

The workflow:

1. **Analyzes the architecture** — examines the project's UI framework, dependencies, and module boundaries.
2. **Configures targets** — lets you choose the target backend framework, frontend framework, and design system.
3. **Backend migration** — an AI subagent extracts backend logic and exposes REST APIs.
4. **Frontend scaffolding** — sets up the React project and design system.
5. **Component & page generation** — generates React components, the home page, and remaining pages with backend integration.
6. **Validates the result** — runs the migrated frontend and backend to confirm correctness.

Each phase is independent — you can run backend migration, frontend setup, or both.

### Java Vulnerability Remediation

Scans project dependencies against the **[OSV.dev](https://osv.dev)** open-source vulnerability database.

The workflow:

1. **Detects dependencies** — parses Maven POM files or Gradle build files to extract the full dependency list with versions.
2. **Queries OSV in batch** — sends all dependencies to the OSV batch API in a single request, then fetches full CVE details (severity, affected versions, summary) for each hit.
3. **Displays results** — renders a structured vulnerability list with CVSS scores directly in chat.
4. **Optionally fixes** — launches a Bob subtask that updates or replaces vulnerable packages and verifies the build still passes.

### Spring Boot to Quarkus Migration

Migrates **Spring Boot** applications to **Quarkus** using a modular, gate-driven flow that compiles after every phase.

The workflow:

1. **Analyzes & plans** — detects existing Spring Boot footprint (starters, annotations, config) and prompts you to choose Spring Compatibility or Full Quarkus migration strategy.
2. **Runs gated modules** — executes Spring Boot build, JPA mappings, and UI templates with their Quarkus equivalents — compiling after each phase.
3. **Verifies & reports** — confirms a clean build, no leftover Spring dependencies, passing tests, and a live health endpoint; produces a structured migration report.

---

## Getting Started

1. Install [IBM Bob](https://bob.ibm.com).
2. Subscribe to IBM Bob Premium Package for Java Modernization.
3. Open your Java project or workspace in Bob.
4. Click **Start Workflow**, or type any of the workflow names below in the Bob prompt to launch it directly:
   - `Java Upgrade`
   - `Liberty Replatforming`
   - `Java Unit Testing`
   - `UI Modernization`
   - `Java Vulnerability Remediation`
   - `Spring Boot to Quarkus`

> **Tip:** You can also launch the Spring Boot to Quarkus migration instantly by typing `/migrate-spring-to-quarkus` in the prompt window.

## Requirements

- [IBM Bob](https://bob.ibm.com)
- IBM Bob Premium Package for Java Modernization subscription

## Screenshots

![alt text][screens-tools-inline]

[screens-tools-inline]: ./assets/screenshots/tools-inline.png "Java agent tools and inline edits"

![alt text][screens-mermaid-flowchart]

[screens-mermaid-flowchart]: ./assets/screenshots/UT-mermaid-big-changes.png "Mermaid flowchart for applied changes"

![alt text][screens-subagents]

[screens-subagents]: ./assets/screenshots/UT-subagents.png "Multiple subagents running in parallel"

## FAQ

### Does this extension work by itself?

No. This add-on extends [IBM Bob](https://bob.ibm.com) and requires it as a dependency.

### What Java versions are supported for upgrade?

The following upgrade paths are supported:

- **Java version upgrades:** You can upgrade from Java 8 to any of the modern LTS releases — Java 11, 17, 21, or 25. This covers both short incremental jumps (e.g. 8 → 11) and longer leaps across multiple versions (e.g. 8 → 25).
- **Jakarta EE upgrades:** You can upgrade from Jakarta EE 7 (formerly Java EE 7) to any of EE 8, 9, 10, or 11.
- Java and Jakarta EE upgrades can be run simultaneously, so you can modernise your runtime version and your API namespace in a single pass.

### Do I need SDKMAN or WinGet?

Only for the Java Upgrade workflow's automatic JDK install and switch steps.

### Does it work with multi-module Maven/Gradle projects?

Yes. Build detection, recipe execution, and log analysis all handle multi-module layouts, including correct `server.xml` placement for Liberty migration.

### Does the Liberty migration workflow require an AMA file?

Yes. The Liberty Replatforming workflow is built around the IBM AMA analysis report. You'll be prompted to select the AMA zip at the start of the workflow.

## Feedback and Support

- Issues: https://github.com/IBM/ibm-bob/issues
- Source: https://github.com/IBM/ibm-bob-java

## License

See [`LICENSE`](LICENSE).
