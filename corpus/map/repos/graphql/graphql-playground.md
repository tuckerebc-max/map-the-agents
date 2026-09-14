# graphql/graphql-playground

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 05861783f778 @ 99da569e84ccb8e2

## Summary (orientation draft, not independently verified)

GraphQL Playground is a GraphQL IDE built on GraphiQL components, distributed as a Yarn-workspaces monorepo containing a React core, an HTML renderer, four framework middlewares, and an Electron app; the evidence documents its interfaces, dependencies, and two documented XSS vulnerabilities with patched versions.

## Source coverage

Source coverage (complete): 5 of 5 candidate file(s) selected; repository tree complete. Claims by basis: 15 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

15 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] GraphQL Playground is a GraphQL IDE for better development workflows, supporting GraphQL Subscriptions, interactive docs, and collaboration. -- evidence: [README.md#L18-L18](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L18-L18)
  - [observation/documented] Playground uses GraphiQL components under the hood and adds multi-column docs, automatic schema reloading, subscriptions, query history, HTTP header configuration, and tabs. -- evidence: [README.md#L79-L84](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L79-L84), [README.md#L77-L77](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L77-L77)
- components (2 claim(s)):
  - [observation/documented] The packages folder contains an Electron app, an HTML page renderer, Express/Hapi/Koa/Lambda middlewares, and the React core, with each middleware using graphql-playground-html. -- evidence: [README.md#L380-L386](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L380-L386)
  - [observation/documented] The repository is a Yarn-workspaces monorepo whose package versions are not synchronized; release-page versions refer to the Electron app. -- evidence: [README.md#L374-L374](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L374-L374)
- design-choices: unknown (no source-linked claim submitted for this facet)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributions are managed by EasyCLA; contributors must sign the GraphQL Specification Membership agreement, and the EasyCLA bot blocks merges without one. -- evidence: [README.md#L333-L333](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L333-L333), [README.md#L335-L335](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L335-L335)
  - [observation/documented] Repository development practice: local development of graphql-playground-react is done by running yarn and yarn start in packages/graphql-playground-react, then opening a localhost:3000 localDev page. -- evidence: [README.md#L328-L329](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L328-L329), [README.md#L322-L326](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L322-L326)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The React component and all middlewares expose options including endpoint, subscriptionEndpoint, workspaceName, config, settings, schema (introspection override), and tabs. -- evidence: [README.md#L166-L167](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L166-L167), [README.md#L137-L142](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L137-L142), [README.md#L135-L135](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L135-L135)
  - [observation/documented] The React component additionally accepts createApolloLink, equivalent to GraphiQL's fetcher; it is unavailable in middlewares because their content must be serializable into an HTML template. -- evidence: [README.md#L185-L185](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L185-L185), [README.md#L182-L183](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L182-L183)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] Using the graphql-playground-react component requires React 16 plus the Open Sans and Source Code Pro fonts. -- evidence: [README.md#L209-L210](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L209-L210), [README.md#L206-L207](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L206-L207), [README.md#L212-L212](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L212-L212)
- limitations (4 claim(s)):
  - [observation/documented] The desktop app only partially supports graphql-config: multi-environment setups work but sending HTTP headers is not supported. -- evidence: [README.md#L92-L93](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L92-L93)
More evidence: [full detail](graphql-playground.detail.md)

Metadata and full claim list: [full detail](graphql-playground.detail.md)
Human notes ([notes](graphql-playground.notes.md), never overwritten by build)

[Back to map index](../../index.md)
