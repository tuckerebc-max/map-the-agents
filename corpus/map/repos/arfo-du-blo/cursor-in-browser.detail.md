# arfo-du-blo/cursor-in-browser -- full detail

[Back to orientation](cursor-in-browser.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/arfo-du-blo/cursor-in-browser/a86ef5f7c0f4e0304e7488a91914694d63460537/b3923197696e61b8.json](../../../wiki/dossiers/arfo-du-blo/cursor-in-browser/a86ef5f7c0f4e0304e7488a91914694d63460537/b3923197696e61b8.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] Prebuilt images are distributed via Docker Hub (arfodublo/cursor-in-browser) and GitHub Container Registry (ghcr.io/arfo-du-blo/cursor-in-browser); users may also clone and rebuild the image themselves. -- evidence: [README.md#L11-L11](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L11-L11), [README.md#L19-L19](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L19-L19), [README.md#L21-L21](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L21-L21) (`clm_31cbfe80f1a4f1b782a65b0c1db65bc8f3af3e4cc75ab5253449b5fc9e684335`)

## design-choices (1 claim(s))

- [observation/documented] Image tags encode Cursor version and CPU architecture, e.g. latest-x64, latest-arm64, or a pinned version like 1.2.3-x64. -- evidence: [README.md#L63-L63](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L63-L63) (`clm_94f6824941f7f6f5ce7807da29954b9f1b384f1dd71fc4ad29309881fee16933`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (4 claim(s))

- [observation/documented] The product is deployed as a Docker container exposing port 8080 internally, mapped in examples to host port 8050, and run detached via docker run. -- evidence: [README.md#L27-L35](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L27-L35), [README.md#L39-L47](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L39-L47) (`clm_5dda39d62153b14f99b81cdffccf592cca235e447b9677275e54521f245699b0`)
- [observation/documented] Access is configured through CUSTOM_USER and PASSWORD environment variables passed at container start. -- evidence: [README.md#L27-L35](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L27-L35), [README.md#L39-L47](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L39-L47) (`clm_f53e747c6e86c5e0934c01844a3bf4fc6331363148c1361e15369f1aa344b584`)
- [observation/documented] The container uses two volumes: /config for Cursor configuration files and /cursor for Cursor data files. -- evidence: [README.md#L51-L52](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L51-L52) (`clm_17d422b228a73f179d320671f97c534d01ef5c3e7a891b020b1cf265f1259100`)
- [observation/documented] Configurable environment variables include PUID and PGID (default 911), TZ (default Etc/UTC), and DOCKER_MODS for adding mods such as universal-git. -- evidence: [README.md#L73-L87](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L73-L87) (`clm_b04b47561fb4f08f1ed08ff4f942e83244e22933a8c12dafd4db44914301e616`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] The image packages Cursor; all x64 and arm64 Cursor versions from 0.47.7 onward are available, and the latest tag tracks the newest Cursor release. -- evidence: [README.md#L7-L7](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L7-L7) (`clm_469e42d86c416f7a1f82c0dcda63f18cdc1147d25341b6d50a1d9a4f947585ef`)
- [observation/documented] Versioned Cursor builds with required files are stored in a cursor_versions folder, and root Dockerfiles target the latest Cursor version via an API call to Cursor's download endpoint. -- evidence: [README.md#L9-L9](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L9-L9) (`clm_1df9617b3b8875a3183b2cc1246e4ff6104bcad1115cb76eae5c3f160ae244f3`)

## limitations (2 claim(s))

- [observation/documented] Due to browser sandbox restrictions, some buttons like Log in cannot be clicked directly; a popup shows external URLs so users can copy them into a new tab. -- evidence: [README.md#L67-L67](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L67-L67) (`clm_7ae78ebd74cc346bd53a0993c5bab5b79adfa60b65f4ae2cfea7fe730dc2fb22`)
- [observation/documented] Closing Cursor leaves a black screen; users must right-click it and select the Cursor entry from the appearing menu to reopen the editor. -- evidence: [README.md#L69-L69](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L69-L69) (`clm_47d9e5faa4311d3ae0fbd10983330c6047dd0d9e00a64cfc4ac5d1690d0c1ef9`)

## relevance (1 claim(s))

- [observation/documented] The project is strongly inspired by sytone/obsidian-remote, which packaged Obsidian for browser use in a similar way. -- evidence: [README.md#L91-L91](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L91-L91), [README.md#L5-L5](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L5-L5) (`clm_7ac2c15ad361e20923a29a2c9b38a13c4816992894a5413899256e87870e6e7f`)

