# ui5/plugins-coding-agents -- full detail

[Back to orientation](plugins-coding-agents.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/ui5/plugins-coding-agents/4c3754ae5b6621a8a42a547c1b376933507a2020/72a0a0048c55923a.json](../../../wiki/dossiers/ui5/plugins-coding-agents/4c3754ae5b6621a8a42a547c1b376933507a2020/72a0a0048c55923a.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repository ships three plugins: 'ui5' (project creation, API lookup, linter integration, best-practice skills), 'ui5-modernization', and 'ui5-typescript-conversion'. -- evidence: [README.md#L28-L32](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/README.md#L28-L32) (`clm_2b0f03197023a5afc6f5ded524d110cc4d74767ce3af4321a3490bf9925d39c4`)

## design-choices (1 claim(s))

- [observation/documented] The TypeScript conversion plugin provides a step-by-step playbook addressing UI5-specific migration challenges like the class system, sap.ui.define loader, and runtime-generated getters/setters. -- evidence: [CHANGELOG.md#L107-L107](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L107-L107) (`clm_3b4f40bfc68d6cbe7e9e80433c89580cfe6840845ee8c1f50bc726f5361838d9`)

## workflows (4 claim(s))

- [observation/documented] Repository development practice: contributors must run 'npm run prettier' to format .mcp.json and .claude-plugin/plugin.json before committing. -- evidence: [docs/Guidelines.md#L5-L5](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/docs/Guidelines.md#L5-L5) (`clm_824301e499a084cc972530d4b5693bf812d823c4fcf66c192d1f3590174ec5f2`)
- [observation/documented] Repository development practice: the project uses Conventional Commits with a required lowercase type, optional scope, and Sentence Case description, and asks for rebase instead of merge commits. -- evidence: [docs/Guidelines.md#L15-L15](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/docs/Guidelines.md#L15-L15), [docs/Guidelines.md#L11-L11](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/docs/Guidelines.md#L11-L11), [docs/Guidelines.md#L29-L31](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/docs/Guidelines.md#L29-L31), [docs/Guidelines.md#L25-L27](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/docs/Guidelines.md#L25-L27) (`clm_e0257854d8e00ae5dabaff00c522ffe933395ae48328efcd1a18d4acee935ae7`)
- [observation/documented] Repository development practice: contributors must accept the Developer Certificate of Origin via CLA assistant before their first pull request, and follow the Development Conventions and Guidelines. -- evidence: [CONTRIBUTING.md#L102-L104](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CONTRIBUTING.md#L102-L104), [CONTRIBUTING.md#L108-L109](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CONTRIBUTING.md#L108-L109) (`clm_8dec6ef16e8df6f4c98957e533071bdfc778ec6fc3a25a2accece162c01e7fe9`)
- [observation/documented] Repository development practice: bug reports should be reproducible, well-documented, one bug per report, in English, and security issues must go through the security policy rather than GitHub issues. -- evidence: [CONTRIBUTING.md#L44-L44](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CONTRIBUTING.md#L44-L44), [CONTRIBUTING.md#L22-L36](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CONTRIBUTING.md#L22-L36) (`clm_43574a8d0f2c6c5dc9d9e34bd67774995b548a8ea3791763d1dd874eb3832ebc`)

## skills-patterns (2 claim(s))

- [observation/documented] The ui5-modernization plugin includes skills such as fix-cyclic-deps, fix-js-globals, fix-xml-globals, modernize-flp-sandbox, modernize-test-starter, and modernize-ui5-app. -- evidence: [CHANGELOG.md#L8-L19](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L8-L19) (`clm_ef6457b8044213fda2048a57ec7451c3c485226be0858eae67ac627e6d330940`)
- [observation/documented] The changelog records added skills for the ui5 plugin covering accessibility, QUnit, Smart & MDC controls, tables, OPA5 guidelines, UI Integration Cards, and general UI5 guidelines. -- evidence: [CHANGELOG.md#L50-L50](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L50-L50), [CHANGELOG.md#L26-L28](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L26-L28), [CHANGELOG.md#L77-L78](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L77-L78), [CHANGELOG.md#L42-L43](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L42-L43) (`clm_7750d26c7e78dbf70875212a4767be27ed9b68e103c8ae466da01d2f6d4cd808`)

## interfaces (2 claim(s))

- [observation/documented] The ui5 plugin can be installed via 'claude plugin install ui5@claude-plugins-official' or the in-app '/plugin install ui5@claude-plugins-official' command. -- evidence: [CHANGELOG.md#L95-L97](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L95-L97), [CHANGELOG.md#L101-L103](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L101-L103) (`clm_a137df06aca6815ef8f1275fc2286eece18bf93679bc42446afe54cf6e9b2f6a`)
- [observation/documented] The ui5-typescript-conversion plugin is installed with 'claude plugin install ui5-typescript-conversion@claude-plugins-official'. -- evidence: [CHANGELOG.md#L111-L113](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L111-L113) (`clm_4a5a9da267d38cb2d4bad0be9cd4c72691f9a8a2d4d7d58a3345c0321b9be4e8`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The ui5 plugin is described as a wrapper around the UI5 MCP server, with possible future additions such as more skills. -- evidence: [CHANGELOG.md#L91-L91](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/CHANGELOG.md#L91-L91) (`clm_a5209f299104933aec0a0702ea80c97af5b4fdc6d791b48de2b770324571f86a`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The project targets developers using coding agents on UI5 projects, aiming to help create UI5 projects, detect and fix UI5-specific errors, and supply UI5-specific information. -- evidence: [README.md#L5-L5](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/README.md#L5-L5), [README.md#L22-L24](https://github.com/UI5/plugins-coding-agents/blob/4c3754ae5b6621a8a42a547c1b376933507a2020/README.md#L22-L24) (`clm_b2ae8d8b502681dee7afe10bcb90242173676b4ea973063aeda06c8ff7624392`)

