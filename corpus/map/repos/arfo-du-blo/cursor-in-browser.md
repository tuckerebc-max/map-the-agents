# arfo-du-blo/cursor-in-browser

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit a86ef5f7c0f4 @ b3923197696e61b8

## Summary (orientation draft, not independently verified)

The repository provides a Docker image that runs the Cursor AI code editor in a web browser, with images published on Docker Hub and ghcr.io. Evidence is limited to the README, covering usage, volumes, environment variables, and known browser-sandbox limitations.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] Prebuilt images are distributed via Docker Hub (arfodublo/cursor-in-browser) and GitHub Container Registry (ghcr.io/arfo-du-blo/cursor-in-browser); users may also clone and rebuild the image themselves. -- evidence: [README.md#L11-L11](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L11-L11), [README.md#L19-L19](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L19-L19), [README.md#L21-L21](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L21-L21)
- design-choices (1 claim(s)):
  - [observation/documented] Image tags encode Cursor version and CPU architecture, e.g. latest-x64, latest-arm64, or a pinned version like 1.2.3-x64. -- evidence: [README.md#L63-L63](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L63-L63)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (4 claim(s)):
  - [observation/documented] The product is deployed as a Docker container exposing port 8080 internally, mapped in examples to host port 8050, and run detached via docker run. -- evidence: [README.md#L27-L35](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L27-L35), [README.md#L39-L47](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L39-L47)
  - [observation/documented] Access is configured through CUSTOM_USER and PASSWORD environment variables passed at container start. -- evidence: [README.md#L27-L35](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L27-L35), [README.md#L39-L47](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L39-L47)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (2 claim(s)):
  - [observation/documented] The image packages Cursor; all x64 and arm64 Cursor versions from 0.47.7 onward are available, and the latest tag tracks the newest Cursor release. -- evidence: [README.md#L7-L7](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L7-L7)
  - [observation/documented] Versioned Cursor builds with required files are stored in a cursor_versions folder, and root Dockerfiles target the latest Cursor version via an API call to Cursor's download endpoint. -- evidence: [README.md#L9-L9](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L9-L9)
- limitations (2 claim(s)):
  - [observation/documented] Due to browser sandbox restrictions, some buttons like Log in cannot be clicked directly; a popup shows external URLs so users can copy them into a new tab. -- evidence: [README.md#L67-L67](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L67-L67)
  - [observation/documented] Closing Cursor leaves a black screen; users must right-click it and select the Cursor entry from the appearing menu to reopen the editor. -- evidence: [README.md#L69-L69](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L69-L69)
- relevance (1 claim(s)):
  - [observation/documented] The project is strongly inspired by sytone/obsidian-remote, which packaged Obsidian for browser use in a similar way. -- evidence: [README.md#L91-L91](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L91-L91), [README.md#L5-L5](https://github.com/Arfo-du-blo/cursor-in-browser/blob/a86ef5f7c0f4e0304e7488a91914694d63460537/README.md#L5-L5)

(2 additional claim(s) omitted for length; see [full detail](cursor-in-browser.detail.md) for every claim.)

Metadata and full claim list: [full detail](cursor-in-browser.detail.md)
Human notes ([notes](cursor-in-browser.notes.md), never overwritten by build)

[Back to map index](../../index.md)
