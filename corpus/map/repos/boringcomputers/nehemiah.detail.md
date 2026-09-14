# boringcomputers/nehemiah -- full detail

[Back to orientation](nehemiah.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/boringcomputers/nehemiah/fea6f0a5299154cb40da9f302a51547e61d40076/492454999a25ebcf.json](../../../wiki/dossiers/boringcomputers/nehemiah/fea6f0a5299154cb40da9f302a51547e61d40076/492454999a25ebcf.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The repo is a Turborepo/npm-workspaces monorepo: apps/web (SvelteKit site), nehemiahd (Go host daemon), packages/sdk (Effect-native TypeScript client), packages/mcp, and infra/latitude provisioning. -- evidence: [README.md#L111-L111](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/README.md#L111-L111), [README.md#L113-L119](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/README.md#L113-L119) (`clm_7c6e2a602675cae366b0be89cf922f8135be106869c65a19921311896fa5adf1`)

## design-choices (2 claim(s))

- [observation/documented] Each machine is a hardware-virtualized Firecracker microVM with its own kernel, jailed and resource-capped, restored from a memory snapshot in milliseconds, with guests network-isolated behind an egress firewall. -- evidence: [README.md#L7-L12](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/README.md#L7-L12), [README.md#L101-L107](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/README.md#L101-L107) (`clm_36e37e49562b2b017ce12be1619d556474c724bd230b1c52a17f99bd2a1ada70`)
- [observation/documented] In local mode the guest shell runs over serial: the kernel boots with console=ttyS0 and nehemiahd pumps the Firecracker child's stdin/stdout as the terminal, working identically for cold-boot and snapshot-restored VMs. -- evidence: [docs/architecture.md#L139-L141](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/architecture.md#L139-L141), [docs/architecture.md#L136-L137](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/architecture.md#L136-L137), [docs/architecture.md#L133-L134](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/architecture.md#L133-L134) (`clm_9a76a549662b2421f785e6ccdb42c4f38db9fe766c43ed4b58f73a2b59a93389`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: contributors use npm workspaces commands (npm run dev/build/check/lint) and are pointed to CONTRIBUTING.md; a route-inventory test fails if the exported OpenAPI contract drifts. -- evidence: [README.md#L131-L132](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/README.md#L131-L132), [docs/nehemiah/api-contract.md#L15-L20](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/nehemiah/api-contract.md#L15-L20), [README.md#L121-L127](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/README.md#L121-L127) (`clm_616922b72dacd88ed2014b9ecf1c50ce4239a640098c3e2837e8098b0eb00d73`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] The local daemon exposes a REST API on port 8080 (machine create/list/get/delete, branch, and a /tty WebSocket with binary frames) plus an open /healthz endpoint. -- evidence: [docs/architecture.md#L169-L172](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/architecture.md#L169-L172), [docs/architecture.md#L174-L182](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/architecture.md#L174-L182) (`clm_ae6737a936e8bc68260bf5dd36c5888da7c61e3071fb7c20dbde768e804bcf57`)
- [observation/documented] An MCP server package (nehemiah-mcp) lets clients like Claude Desktop and Cursor spin up and drive Nehemiah computers as a tool, configured via npx with a NEHEMIAH_URL env var. -- evidence: [README.md#L84-L94](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/README.md#L84-L94), [README.md#L80-L82](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/README.md#L80-L82) (`clm_7170227d3bda5cb1fdc4dc7708451a7879aa84ad27d64922ec960c1d430e7bfa`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (2 claim(s))

- [observation/documented] Managed machines move through persisted lifecycle states (requested, placing, starting, running, stopping, stopped, failed, lost); terminal records never regress, and a machine declared lost is never presented as recovered. -- evidence: [docs/nehemiah/architecture.md#L152-L154](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/nehemiah/architecture.md#L152-L154), [docs/nehemiah/architecture.md#L134-L143](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/nehemiah/architecture.md#L134-L143) (`clm_2e3794f01aab746fc7dda899a695426344f9c6c9a78fbc6579a0ba48eafd8831`)
- [observation/documented] The scheduler filters hosts by region, architecture, size, template availability, health, and hard quotas, reserving capacity in one PostgreSQL transaction and preferring hosts with the requested template cached. -- evidence: [docs/nehemiah/architecture.md#L208-L212](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/nehemiah/architecture.md#L208-L212) (`clm_f730ad3510737a84b75bedd0560736e078d47424bb18529a606e56cb6c785f7c`)

## tools-permissions (1 claim(s))

- [observation/documented] File access uses capability-scoped session tokens sent only as bearer headers; query tokens, cookies, and redirects are forbidden, uploads are capped at 16 MiB, and sessions can be revoked with a typed DELETE endpoint. -- evidence: [docs/nehemiah/api-contract.md#L41-L47](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/nehemiah/api-contract.md#L41-L47), [docs/nehemiah/api-contract.md#L59-L66](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/nehemiah/api-contract.md#L59-L66) (`clm_d3919cbdc044126fbc9daea90f000aa2f1855cd501eefc732da80825d116b3a4`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (2 claim(s))

- [observation/documented] Managed OCI image import/pull is not implemented: requests receive a typed 501 not_supported response, and the field is documented only as a deprecated reserved field. -- evidence: [docs/nehemiah/api-contract.md#L81-L86](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/nehemiah/api-contract.md#L81-L86) (`clm_6b0e262d57faa44b56d27264b0a2bbe7ef8c715c3f5fcd150ed319347f33d110`)
- [observation/documented] Managed host-local LLM agents are not implemented; agent-capability session issuance fails with typed not_supported, and users are directed to run agents inside the guest via exec/TTY/file primitives. -- evidence: [docs/nehemiah/api-contract.md#L88-L92](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/nehemiah/api-contract.md#L88-L92) (`clm_8ce63f73fc921269d564c3fb8a18964c6ca7e74625abbc3e7eb1671dd9146aaa`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

