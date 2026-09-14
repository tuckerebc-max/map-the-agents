# kuafuai/aipexbase

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit bf523cfa479f @ ba47eda61ca376d7

## Summary (orientation draft, not independently verified)

Selected evidence records: The project is described as backend-as-a-service infrastructure for the AI era, versioned 1.0.0 and licensed under Apache 2.0. The core philosophy is providing a complete backend without writing backend code, so developers can skip backend implementation and integrate via SDK from any AI coding tool.

## Source coverage

Source coverage (partial): 6 of 8 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project is described as backend-as-a-service infrastructure for the AI era, versioned 1.0.0 and licensed under Apache 2.0. -- evidence: [README.md#L3-L22](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L3-L22)
- components (2 claim(s)):
  - [observation/documented] The stack includes a Spring Boot 2 backend and a Vue 3 management console, per README badges. -- evidence: [README.md#L3-L22](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L3-L22)
  - [observation/documented] Out-of-the-box capabilities include automated data storage, user authentication with permission control, third-party AI service integration, and session/state context management. -- evidence: [README.md#L59-L62](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L59-L62)
- design-choices (1 claim(s)):
  - [observation/documented] The core philosophy is providing a complete backend without writing backend code, so developers can skip backend implementation and integrate via SDK from any AI coding tool. -- evidence: [README.md#L40-L40](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L40-L40), [README.md#L38-L38](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L38-L38)
- workflows (2 claim(s)):
  - [observation/documented] Source installation requires Java 1.8+, Node.js 18+, MySQL 8.0+, importing an init SQL script, editing JDBC config in application-mysql.yml, then running mvn spring-boot:run (service on port 8080). -- evidence: [README.md#L74-L77](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L74-L77), [README.md#L99-L100](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L99-L100), [README.md#L89-L93](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L89-L93), [README.md#L95-L97](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L95-L97), [README.md#L85-L85](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L85-L85)
  - [observation/documented] Docker Compose deployment is the recommended install method; prerequisites are Linux, Docker, and Docker Compose v2.5+, started with docker-compose up -d. -- evidence: [docs/INSTALL.md#L4-L6](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/docs/INSTALL.md#L4-L6), [README.md#L110-L110](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L110-L110), [docs/INSTALL.md#L19-L21](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/docs/INSTALL.md#L19-L21)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The product offers native MCP compatibility so models and agents can directly invoke backend capabilities, plus a unified context and data layer for long-term memory and traceable state. -- evidence: [README.md#L54-L56](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L54-L56)
  - [observation/documented] AI IDEs connect via an MCP server endpoint of the form /mcp/sse?token=<apikey>, configured in Cursor's mcpServers settings. -- evidence: [docs/IntegrationAI.md#L16-L24](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/docs/IntegrationAI.md#L16-L24), [docs/IntegrationAI.md#L12-L14](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/docs/IntegrationAI.md#L12-L14)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The platform advertises native support for Chinese ecosystem platforms including Feishu, DingTalk, and WeChat, plus HarmonyOS apps, mini-programs, and WebView containers. -- evidence: [README.md#L65-L66](https://github.com/kuafuai/aipexbase/blob/bf523cfa479f25dfe78516b78658fc98ed15c611/README.md#L65-L66)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance: unknown (no source-linked claim submitted for this facet)

(2 additional claim(s) omitted for length; see [full detail](aipexbase.detail.md) for every claim.)

Metadata and full claim list: [full detail](aipexbase.detail.md)
Human notes ([notes](aipexbase.notes.md), never overwritten by build)

[Back to map index](../../index.md)
