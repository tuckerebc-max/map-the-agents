---
access: public
aliases: []
claim_ids:
- clm_0da58cbbccd0cdedcddeaa778e6a35c4f6172c56226bd49b1fbe7d97458ceb05
- clm_209bb2b47a7a28a149d54378bc24c5df7acdc92ff73a89881952a1fb590cda02
- clm_2d458782080ac05711005eb2d16071a3da437edb4c722158a397813ac7a780e9
- clm_36f042374a40c6010c9afdc4946bf5e42e0b9cf8de34242f02ccd2256bec98a9
- clm_54abca795f30238fb681dd0b20f5d883b0d0d5385f66deae53522525751c5c92
- clm_9ebcb6464a93f4e78dac1644d17cb39e6fc0eeb4c88a9d053dad58aa68e3fc57
- clm_b48fa5399ce7ed549d0944cb7cf741e9e9117ab4b3f1681668c64dc7403da2fa
- clm_cbec1da8466f99ca19c3ee75882494268ff16a84afb140541b1b5f0d66867243
- clm_cf2e05f296d0b4155cea5ee668384b0a05a7a4754f05b2595e466a29b2fae661
- clm_d08eb6835ac7539709254d7d53125c00de0256c412665b63a2e3dede59ac3b79
- clm_d7aa6ba873592ff1fea817eb6fc190deb17ed6ffb04a6c9beadf4c425495ed2a
- clm_df3010ec7ac245a8fa69c394965f5ece7c13a3b9744bf6f470d64c890bedc37d
- clm_e4a159098b8a0eaa49a309bc4b4677585ea54c77ce1b81486c0c5f1c5cf9e0e1
- clm_f896a25cc41854b9e1d2f7d703f458e5af665adc114093b9e16cb213fb05309b
maturity: draft
page_id: pg_12e1194b42d05881a28e2a7f208f5a48
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_51b61ebd06dd547d83571663cb0e8c05
title: graphql/graphql-playground/README.md @ 05861783f778
updated_at: '2026-09-14T03:55:02Z'
---

# graphql/graphql-playground/README.md @ 05861783f778

<!-- rcw:begin owner=source:src_51b61ebd06dd547d83571663cb0e8c05 block=evidence -->
- GraphQL Playground is a GraphQL IDE for better development workflows, supporting GraphQL Subscriptions, interactive docs, and collaboration. [@claim:clm_0da58cbbccd0cdedcddeaa778e6a35c4f6172c56226bd49b1fbe7d97458ceb05]
- From graphql-playground-react@1.7.0 a codeTheme property allows customizing editor colors via an EditorColours interface. [@claim:clm_209bb2b47a7a28a149d54378bc24c5df7acdc92ff73a89881952a1fb590cda02]
- Repository development practice: contributions are managed by EasyCLA; contributors must sign the GraphQL Specification Membership agreement, and the EasyCLA bot blocks merges without one. [@claim:clm_2d458782080ac05711005eb2d16071a3da437edb4c722158a397813ac7a780e9]
- The React component and all middlewares expose options including endpoint, subscriptionEndpoint, workspaceName, config, settings, schema (introspection override), and tabs. [@claim:clm_36f042374a40c6010c9afdc4946bf5e42e0b9cf8de34242f02ccd2256bec98a9]
- The desktop app only partially supports graphql-config: multi-environment setups work but sending HTTP headers is not supported. [@claim:clm_54abca795f30238fb681dd0b20f5d883b0d0d5385f66deae53522525751c5c92]
- Playground uses GraphiQL components under the hood and adds multi-column docs, automatic schema reloading, subscriptions, query history, HTTP header configuration, and tabs. [@claim:clm_9ebcb6464a93f4e78dac1644d17cb39e6fc0eeb4c88a9d053dad58aa68e3fc57]
- graphql-playground-html and its middleware dependents had an XSS Reflection vulnerability (CVE-2020-4038) with unsanitized user input, resolved in graphql-playground-html 1.6.22 and specific safe versions of each middleware. [@claim:clm_b48fa5399ce7ed549d0944cb7cf741e9e9117ab4b3f1681668c64dc7403da2fa]
- The React component additionally accepts createApolloLink, equivalent to GraphiQL's fetcher; it is unavailable in middlewares because their content must be serializable into an HTML template. [@claim:clm_cbec1da8466f99ca19c3ee75882494268ff16a84afb140541b1b5f0d66867243]
- Repository development practice: local development of graphql-playground-react is done by running yarn and yarn start in packages/graphql-playground-react, then opening a localhost:3000 localDev page. [@claim:clm_cf2e05f296d0b4155cea5ee668384b0a05a7a4754f05b2595e466a29b2fae661]
- The repository is a Yarn-workspaces monorepo whose package versions are not synchronized; release-page versions refer to the Electron app. [@claim:clm_d08eb6835ac7539709254d7d53125c00de0256c412665b63a2e3dede59ac3b79]
- Using the graphql-playground-react component requires React 16 plus the Open Sans and Source Code Pro fonts. [@claim:clm_d7aa6ba873592ff1fea817eb6fc190deb17ed6ffb04a6c9beadf4c425495ed2a]
- User-facing settings include editor cursor shape, font family, size and theme, prettier options, request.credentials, schema polling enable/filter/interval, and tracing options. [@claim:clm_df3010ec7ac245a8fa69c394965f5ece7c13a3b9744bf6f470d64c890bedc37d]
- When tabs are injected via the tabs prop, they are reset each time the page is reloaded. [@claim:clm_e4a159098b8a0eaa49a309bc4b4677585ea54c77ce1b81486c0c5f1c5cf9e0e1]
- The packages folder contains an Electron app, an HTML page renderer, Express/Hapi/Koa/Lambda middlewares, and the React core, with each middleware using graphql-playground-html. [@claim:clm_f896a25cc41854b9e1d2f7d703f458e5af665adc114093b9e16cb213fb05309b]
<!-- rcw:end owner=source:src_51b61ebd06dd547d83571663cb0e8c05 block=evidence -->

## Researcher notes

