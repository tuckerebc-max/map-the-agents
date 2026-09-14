# zhinjs/zhin -- full detail

[Back to orientation](zhin.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/zhinjs/zhin/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/5af28cbf7a2c96f7.json](../../../wiki/dossiers/zhinjs/zhin/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/5af28cbf7a2c96f7.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repo is a pnpm workspace monorepo whose packages include @zhin.js/core (IM layer), @zhin.js/ai, @zhin.js/agent, @zhin.js/cli (composition root), and the zhin.js facade package. -- evidence: [docs/concepts/architecture.md#L3-L3](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/concepts/architecture.md#L3-L3), [docs/concepts/architecture.md#L62-L75](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/concepts/architecture.md#L62-L75), [README.md#L205-L211](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L205-L211) (`clm_abff7469470d5505d35a9932eb59730bf18bcb730b97cc91ad6f5666ce616958`)

## design-choices (2 claim(s))

- [observation/documented] Package dependency direction is unidirectional downward: upper layers may depend on lower ones, and lower layers never reference upper layers; @zhin.js/cli is the sole exception allowed to import across all layers. -- evidence: [docs/en/concepts/architecture.md#L3-L3](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/en/concepts/architecture.md#L3-L3), [docs/en/concepts/architecture.md#L76-L76](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/en/concepts/architecture.md#L76-L76), [docs/concepts/architecture.md#L79-L79](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/concepts/architecture.md#L79-L79), [docs/concepts/architecture.md#L3-L3](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/concepts/architecture.md#L3-L3) (`clm_717080968ab6f9bf8e5a296089876e17ba0d4f90cac83c089c3139c00481a50a`)
- [observation/documented] Plugin hot reload is described as a Generation transaction: the next plugin tree is prepared and validated off-path, then published atomically, so a failed candidate leaves the active Generation serving traffic. -- evidence: [README.md#L125-L129](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L125-L129) (`clm_45643162a7971bd6d0315bc62a4ebd68bc958dd0c9f691519745b01cf5f3c84f`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: `pnpm check:architecture` runs in CI to block lower-layer packages importing upper-layer packages, and the layering rule is enforced by harness checks rather than convention. -- evidence: [docs/en/concepts/architecture.md#L3-L3](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/en/concepts/architecture.md#L3-L3), [docs/concepts/architecture.md#L3-L3](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/concepts/architecture.md#L3-L3) (`clm_55c4f9919c082483d9be940ffb4c0d445d7974be41a35028e3e1c30db73dab61`)
- [observation/documented] Repository development practice: adapter doc pages are auto-generated from in-package READMEs; contributors edit the package README and run `pnpm sync:adapter-docs`. -- evidence: [docs/adapters/sandbox.md#L7-L9](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/adapters/sandbox.md#L7-L9), [docs/en/adapters/sandbox.md#L7-L9](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/en/adapters/sandbox.md#L7-L9) (`clm_e87be9744b935be051d8b79994bdb712fdb35f8132797906cd9376b206db4775`)
- [observation/documented] Repository development practice: the API reference is generated from source via `pnpm docs:api`, validated with `pnpm check:api-docs`, and CI gates fail on unknown JSDoc tags, broken symbol links, or TypeScript errors. -- evidence: [docs/reference/api.md#L37-L37](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/reference/api.md#L37-L37), [docs/reference/api.md#L35-L35](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/reference/api.md#L35-L35), [docs/reference/api.md#L33-L33](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/reference/api.md#L33-L33) (`clm_59aacd3b8e135ac3d84b018fcb400cd7c531dbf108b352aaf71712cbaadd1d95`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The CLI exposes commands including `zhin runtime start`, `zhin setup`, `zhin doctor`, `zhin new my-plugin`, and `zhin search <kw>`. -- evidence: [README.md#L228-L234](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L228-L234), [README.md#L81-L81](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L81-L81), [docs/concepts/architecture.md#L81-L81](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/concepts/architecture.md#L81-L81) (`clm_b9c24ac9810c1ff33a5dff9b6032c1d6c69af2f6e0693b34d31d121a5a5d135f`)
- [observation/documented] The Sandbox adapter is a WebSocket-based local testing adapter exposing a `/sandbox` WebSocket endpoint plus a browser chat UI, requiring no third-party platform account. -- evidence: [docs/en/adapters/sandbox.md#L15-L15](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/en/adapters/sandbox.md#L15-L15), [docs/en/adapters/sandbox.md#L19-L23](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/en/adapters/sandbox.md#L19-L23), [docs/adapters/sandbox.md#L19-L23](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/adapters/sandbox.md#L19-L23), [docs/adapters/sandbox.md#L15-L15](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/adapters/sandbox.md#L15-L15) (`clm_980de79dbd94318509b356ce3ec54b47e617e63c7539e4f22814bd9145c3fc22`)
- [observation/documented] The README lists adapter packages for 20+ platforms including QQ, Discord, Slack, Telegram, DingTalk, OneBot 11/12, GitHub, email, and LINE. -- evidence: [README.md#L40-L42](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L40-L42), [README.md#L192-L199](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L192-L199) (`clm_148ec180642b27f97f5ec935696b67327b094ea58cb2d0151678e1033807a1e9`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (1 claim(s))

- [observation/documented] Agent execution security is configurable via zhin.config.yml, e.g. execSecurity: allowlist and execApprovalMode: ask; the stability table lists a baseline security tier with bash allowlist, file policy, and approval. -- evidence: [README.md#L173-L186](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L173-L186), [README.md#L134-L141](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L134-L141) (`clm_eb67dd8f0432bf3c98a117c61d62611dc8b064ef7da1f4dfd07669603fe171f5`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] AI is opt-in: the default install is an IM core under ~10MB, and agent capability requires adding @zhin.js/agent, zod, ai, and a provider package such as @ai-sdk/openai. -- evidence: [README.md#L40-L42](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L40-L42), [README.md#L151-L158](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L151-L158), [docs/en/concepts/architecture.md#L56-L56](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/docs/en/concepts/architecture.md#L56-L56), [README.md#L166-L169](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L166-L169) (`clm_1647a43c812099acae398b4762bd603e833ed3720643ba94cc6c17cc549caeef`)
- [observation/documented] Scaffolded TypeScript projects require Node.js >=22.12.0 and pnpm 9+, while the compiled IM library supports Node ^20.19.0 or >=22.12.0. -- evidence: [README.md#L83-L83](https://github.com/zhinjs/zhin/blob/494dd81f1ac5b79b6d1af44e5d0ebd1142165121/README.md#L83-L83) (`clm_70fa064569a1d6f6888439a94782834fd4063d51b1cab18b7e26d788a69ed80a`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

