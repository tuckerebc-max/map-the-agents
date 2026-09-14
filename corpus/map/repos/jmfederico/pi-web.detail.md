# jmfederico/pi-web -- full detail

[Back to orientation](pi-web.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/jmfederico/pi-web/46579c049a305b6a146d1028e539ca6d071fbfb4/3287e18d140e16b7.json](../../../wiki/dossiers/jmfederico/pi-web/46579c049a305b6a146d1028e539ca6d071fbfb4/3287e18d140e16b7.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The product organizes work hierarchically: a machine is a runtime endpoint, a project is a folder on it, a workspace is a provider-owned working folder, and a session is a Pi Coding Agent chat inside a workspace. -- evidence: [README.md#L78-L83](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/README.md#L78-L83) (`clm_1589f315b690b13265b2e92e0b57bae1bc305df92dc0668dd4d97ae6e326e6e3`)
- [observation/documented] Sessions are designed to survive browser disconnects, letting users supervise agents from any browser while work continues on the host machine. -- evidence: [README.md#L24-L29](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/README.md#L24-L29), [README.md#L31-L31](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/README.md#L31-L31) (`clm_d60f58ee64c1335c77a3db2cdbda825769fcaafa33eba90b80c6f1faa15a259c`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] Configuration resolves as defaults, then the global config file, then environment overrides; project-local <project>/.pi-web/config.json can override upload and attachment defaults and merge allowed paths. -- evidence: [docs/config.md#L36-L38](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L36-L38), [docs/config.md#L40-L40](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L40-L40), [docs/config.md#L108-L108](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L108-L108) (`clm_f998c5bb9928e7ded53452411afad097e2584eec3bed5c2d253048c983e6e9c6`)

## memory-state (2 claim(s))

- [observation/documented] PI_WEB_DATA_DIR sets the root for managed runtime state (default ~/.pi-web), holding project and machine registries, discovered plugins, the session-daemon socket, and session archives; each data directory starts independent and empty. -- evidence: [docs/config.md#L198-L198](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L198-L198), [docs/config.md#L200-L200](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L200-L200) (`clm_d93387b1a99c554df0f156da90a3c302707cccbcc40c0346c3d9f69519e5bcde`)
- [observation/documented] One live session daemon owns each data directory, recording ownership in sessiond-owner.json; a second daemon pointed at the same directory fails loudly at startup, while stale markers from dead daemons are taken over automatically. -- evidence: [docs/config.md#L202-L202](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L202-L202) (`clm_e50a8246cedf5912f0eae6378494203698501ec6ef69568902a56b87cd1b1640`)

## orchestration (1 claim(s))

- [observation/documented] PI WEB can register other PI WEB runtimes as remote machines, with one browser-facing instance proxying projects, files, git state, sessions, terminals, and Pi package management from trusted remote machines. -- evidence: [README.md#L105-L105](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/README.md#L105-L105) (`clm_fa44460aebcf86a4b35d21cf46d876604f4f4c08595a17520f18b6c93974cb11`)

## tools-permissions (1 claim(s))

- [observation/documented] By default workspace-relative file reads stay inside the workspace and absolute paths are denied; pathAccess.allowedPaths grants the file explorer access to specific external filesystem roots, with symlink escapes rejected, though this is not a sandbox for the agent or OS user. -- evidence: [docs/config.md#L230-L230](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L230-L230), [docs/config.md#L226-L226](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L226-L226), [docs/config.md#L216-L216](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L216-L216), [docs/config.md#L218-L218](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/docs/config.md#L218-L218) (`clm_e59eb1dd41b81a120cdc28850402c76e612d4b7040b2482363470b04bb408920`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Running PI WEB requires Node.js 22.19.0 or newer, npm, a Pi Coding Agent of at least version 0.84.0, and git plus the development tools agents need. -- evidence: [README.md#L37-L40](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/README.md#L37-L40) (`clm_8967c45b5d29a110cdac6308247608e5f58ccb0c57c0ee54df69052f026a0011`)
- [observation/documented] Installation uses npm with the scoped --allow-scripts=node-pty flag so node-pty can build its native module without enabling install scripts for other packages. -- evidence: [README.md#L50-L50](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/README.md#L50-L50), [README.md#L44-L48](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/README.md#L44-L48) (`clm_a4d9cf321f8ecae1861ede17de1fd1a7e7553eb219d6e9ed4c289cf1f66d1714`)

## limitations (1 claim(s))

- [observation/documented] The security model assumes trusted users, repositories, and server paths; the product is explicitly not a sandbox, permission system, or multi-tenant platform and should not be exposed directly to the public internet. -- evidence: [README.md#L171-L171](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/README.md#L171-L171), [README.md#L169-L169](https://github.com/jmfederico/pi-web/blob/46579c049a305b6a146d1028e539ca6d071fbfb4/README.md#L169-L169) (`clm_d530a1f25c83e05f228999bdb8b54f6c8ade851927ab79df85ac03529400b050`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

