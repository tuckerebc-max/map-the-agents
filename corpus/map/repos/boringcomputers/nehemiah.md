# boringcomputers/nehemiah

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fea6f0a52991 @ 492454999a25ebcf

## Summary (orientation draft, not independently verified)

The local daemon exposes a REST API on port 8080 (machine create/list/get/delete, branch, and a /tty WebSocket with binary frames) plus an open /healthz endpoint. An MCP server package (nehemiah-mcp) lets clients like Claude Desktop and Cursor spin up and drive Nehemiah computers as a tool, configured via npx with a NEHEMIAH_URL env var. Evidence coverage: 110 of 179 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 24 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The repo is a Turborepo/npm-workspaces monorepo: apps/web (SvelteKit site), nehemiahd (Go host daemon), packages/sdk (Effect-native TypeScript client), packages/mcp, and infra/latitude provisioning. -- evidence: [README.md#L111-L111](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/README.md#L111-L111), [README.md#L113-L119](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/README.md#L113-L119)
- design-choices (2 claim(s)):
  - [observation/documented] Each machine is a hardware-virtualized Firecracker microVM with its own kernel, jailed and resource-capped, restored from a memory snapshot in milliseconds, with guests network-isolated behind an egress firewall. -- evidence: [README.md#L7-L12](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/README.md#L7-L12), [README.md#L101-L107](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/README.md#L101-L107)
  - [observation/documented] In local mode the guest shell runs over serial: the kernel boots with console=ttyS0 and nehemiahd pumps the Firecracker child's stdin/stdout as the terminal, working identically for cold-boot and snapshot-restored VMs. -- evidence: [docs/architecture.md#L139-L141](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/architecture.md#L139-L141), [docs/architecture.md#L136-L137](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/architecture.md#L136-L137), [docs/architecture.md#L133-L134](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/architecture.md#L133-L134)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: contributors use npm workspaces commands (npm run dev/build/check/lint) and are pointed to CONTRIBUTING.md; a route-inventory test fails if the exported OpenAPI contract drifts. -- evidence: [README.md#L131-L132](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/README.md#L131-L132), [docs/nehemiah/api-contract.md#L15-L20](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/nehemiah/api-contract.md#L15-L20), [README.md#L121-L127](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/README.md#L121-L127)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] The local daemon exposes a REST API on port 8080 (machine create/list/get/delete, branch, and a /tty WebSocket with binary frames) plus an open /healthz endpoint. -- evidence: [docs/architecture.md#L169-L172](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/architecture.md#L169-L172), [docs/architecture.md#L174-L182](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/architecture.md#L174-L182)
  - [observation/documented] An MCP server package (nehemiah-mcp) lets clients like Claude Desktop and Cursor spin up and drive Nehemiah computers as a tool, configured via npx with a NEHEMIAH_URL env var. -- evidence: [README.md#L84-L94](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/README.md#L84-L94), [README.md#L80-L82](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/README.md#L80-L82)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration (2 claim(s)):
  - [observation/documented] Managed machines move through persisted lifecycle states (requested, placing, starting, running, stopping, stopped, failed, lost); terminal records never regress, and a machine declared lost is never presented as recovered. -- evidence: [docs/nehemiah/architecture.md#L152-L154](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/nehemiah/architecture.md#L152-L154), [docs/nehemiah/architecture.md#L134-L143](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/nehemiah/architecture.md#L134-L143)
  - [observation/documented] The scheduler filters hosts by region, architecture, size, template availability, health, and hard quotas, reserving capacity in one PostgreSQL transaction and preferring hosts with the requested template cached. -- evidence: [docs/nehemiah/architecture.md#L208-L212](https://github.com/boringcomputers/nehemiah/blob/fea6f0a5299154cb40da9f302a51547e61d40076/docs/nehemiah/architecture.md#L208-L212)
- tools-permissions (1 claim(s)):
More evidence: [full detail](nehemiah.detail.md)

Metadata and full claim list: [full detail](nehemiah.detail.md)
Human notes ([notes](nehemiah.notes.md), never overwritten by build)

[Back to map index](../../index.md)
