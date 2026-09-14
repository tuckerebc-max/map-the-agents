# graphql/graphql-playground -- full detail

[Back to orientation](graphql-playground.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/graphql/graphql-playground/05861783f77896012a4493442b2ce2b0de9ce95f/99da569e84ccb8e2.json](../../../wiki/dossiers/graphql/graphql-playground/05861783f77896012a4493442b2ce2b0de9ce95f/99da569e84ccb8e2.json)

## specifications (2 claim(s))

- [observation/documented] GraphQL Playground is a GraphQL IDE for better development workflows, supporting GraphQL Subscriptions, interactive docs, and collaboration. -- evidence: [README.md#L18-L18](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L18-L18) (`clm_0da58cbbccd0cdedcddeaa778e6a35c4f6172c56226bd49b1fbe7d97458ceb05`)
- [observation/documented] Playground uses GraphiQL components under the hood and adds multi-column docs, automatic schema reloading, subscriptions, query history, HTTP header configuration, and tabs. -- evidence: [README.md#L79-L84](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L79-L84), [README.md#L77-L77](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L77-L77) (`clm_9ebcb6464a93f4e78dac1644d17cb39e6fc0eeb4c88a9d053dad58aa68e3fc57`)

## components (2 claim(s))

- [observation/documented] The packages folder contains an Electron app, an HTML page renderer, Express/Hapi/Koa/Lambda middlewares, and the React core, with each middleware using graphql-playground-html. -- evidence: [README.md#L380-L386](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L380-L386) (`clm_f896a25cc41854b9e1d2f7d703f458e5af665adc114093b9e16cb213fb05309b`)
- [observation/documented] The repository is a Yarn-workspaces monorepo whose package versions are not synchronized; release-page versions refer to the Electron app. -- evidence: [README.md#L374-L374](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L374-L374) (`clm_d08eb6835ac7539709254d7d53125c00de0256c412665b63a2e3dede59ac3b79`)

## design-choices (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributions are managed by EasyCLA; contributors must sign the GraphQL Specification Membership agreement, and the EasyCLA bot blocks merges without one. -- evidence: [README.md#L333-L333](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L333-L333), [README.md#L335-L335](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L335-L335) (`clm_2d458782080ac05711005eb2d16071a3da437edb4c722158a397813ac7a780e9`)
- [observation/documented] Repository development practice: local development of graphql-playground-react is done by running yarn and yarn start in packages/graphql-playground-react, then opening a localhost:3000 localDev page. -- evidence: [README.md#L328-L329](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L328-L329), [README.md#L322-L326](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L322-L326) (`clm_cf2e05f296d0b4155cea5ee668384b0a05a7a4754f05b2595e466a29b2fae661`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The React component and all middlewares expose options including endpoint, subscriptionEndpoint, workspaceName, config, settings, schema (introspection override), and tabs. -- evidence: [README.md#L166-L167](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L166-L167), [README.md#L137-L142](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L137-L142), [README.md#L135-L135](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L135-L135) (`clm_36f042374a40c6010c9afdc4946bf5e42e0b9cf8de34242f02ccd2256bec98a9`)
- [observation/documented] The React component additionally accepts createApolloLink, equivalent to GraphiQL's fetcher; it is unavailable in middlewares because their content must be serializable into an HTML template. -- evidence: [README.md#L185-L185](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L185-L185), [README.md#L182-L183](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L182-L183) (`clm_cbec1da8466f99ca19c3ee75882494268ff16a84afb140541b1b5f0d66867243`)
- [observation/documented] User-facing settings include editor cursor shape, font family, size and theme, prettier options, request.credentials, schema polling enable/filter/interval, and tracing options. -- evidence: [README.md#L110-L129](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L110-L129) (`clm_df3010ec7ac245a8fa69c394965f5ece7c13a3b9744bf6f470d64c890bedc37d`)
- [observation/documented] From graphql-playground-react@1.7.0 a codeTheme property allows customizing editor colors via an EditorColours interface. -- evidence: [README.md#L343-L344](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L343-L344), [README.md#L346-L370](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L346-L370) (`clm_209bb2b47a7a28a149d54378bc24c5df7acdc92ff73a89881952a1fb590cda02`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Using the graphql-playground-react component requires React 16 plus the Open Sans and Source Code Pro fonts. -- evidence: [README.md#L209-L210](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L209-L210), [README.md#L206-L207](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L206-L207), [README.md#L212-L212](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L212-L212) (`clm_d7aa6ba873592ff1fea817eb6fc190deb17ed6ffb04a6c9beadf4c425495ed2a`)

## limitations (4 claim(s))

- [observation/documented] The desktop app only partially supports graphql-config: multi-environment setups work but sending HTTP headers is not supported. -- evidence: [README.md#L92-L93](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L92-L93) (`clm_54abca795f30238fb681dd0b20f5d883b0d0d5385f66deae53522525751c5c92`)
- [observation/documented] When tabs are injected via the tabs prop, they are reset each time the page is reloaded. -- evidence: [README.md#L166-L167](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L166-L167) (`clm_e4a159098b8a0eaa49a309bc4b4677585ea54c77ce1b81486c0c5f1c5cf9e0e1`)
- [observation/documented] graphql-playground-html and its middleware dependents had an XSS Reflection vulnerability (CVE-2020-4038) with unsanitized user input, resolved in graphql-playground-html 1.6.22 and specific safe versions of each middleware. -- evidence: [README.md#L11-L11](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L11-L11), [README.md#L59-L65](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/README.md#L59-L65) (`clm_b48fa5399ce7ed549d0944cb7cf741e9e9117ab4b3f1681668c64dc7403da2fa`)
- [observation/documented] graphql-playground-react versions before 1.7.28 are vulnerable to XSS via compromised introspection responses or malicious schema prop type names, exploitable on autocomplete; 1.7.28 fixes it via HTML escaping and schema validation. -- evidence: [docs/security/2021-schema-xss-phishing-attack.md#L35-L35](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/docs/security/2021-schema-xss-phishing-attack.md#L35-L35), [docs/security/2021-schema-xss-phishing-attack.md#L37-L37](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/docs/security/2021-schema-xss-phishing-attack.md#L37-L37), [docs/security/2021-schema-xss-phishing-attack.md#L33-L33](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/docs/security/2021-schema-xss-phishing-attack.md#L33-L33), [docs/security/2021-schema-xss-phishing-attack.md#L16-L16](https://github.com/graphql/graphql-playground/blob/05861783f77896012a4493442b2ce2b0de9ce95f/docs/security/2021-schema-xss-phishing-attack.md#L16-L16) (`clm_274c2197b0b289771ea55ccbbc7f8b863db8423592e9d83dc70f78115556b852`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

