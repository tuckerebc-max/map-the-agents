# cursor-in-browser (`cursor-in-browser`)

[Back to directory index](../index.md)

Directory membership: backing+pages.

- Category: other
- Provider/maker: Arfo-du-blo
- License: MIT
- Language: Dockerfile
- Interface: platforms=IDE, Web; install=Docker (via Docker Hub or ghcr.io)
- Model providers: unknown
- Feature flags (directory-reported):
  - mcp_support: unknown (unknown)
  - plugin_support: unknown (unknown)
  - claude_code_plugin: False (reported)
  - subagents: unknown (unknown)
  - hooks: unknown (unknown)
  - plan_mode: unknown (unknown)

Repository map entry: [arfo-du-blo/cursor-in-browser](../../repos/arfo-du-blo/cursor-in-browser.md) (source: backing, field: `source_code_url`).

## Description

Highlight (site page `what_makes_it_special`): Deploys and runs Cursor AI Code Editor directly in a web browser using Docker/KasmVNC; tracks Cursor releases for x64 and arm64

(captured site page body (agents/cursor-in-browser.md), not a verified repo-code finding)
cursor-in-browser is a containerization project that runs the Cursor AI code editor inside a Docker image and streams its UI to a browser via KasmVNC, modeled on LinuxServer-style remote-desktop images. The image exposes the editor with basic-auth protection and persistent volumes for configuration and Cursor data, and its build scripts pull current Cursor releases for both x64 and arm64, with tags tracking versions from 0.47.7 onward and a 'latest' tag following new releases. All AI functionality remains Cursor's own; the repo contributes only the packaging. It serves developers who want Cursor on Chromebooks, tablets, or locked-down machines where local installation is impractical, and it remains actively maintained with images on Docker Hub and ghcr.io.
Sources: [backing feed @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/_data/agents.json); [site page @ 61d64ce1ee2e](https://github.com/prime-radiant-inc/alltheagents.org/blob/61d64ce1ee2eae6b23dcef8ea9f31bc2c8b75fd0/agents/cursor-in-browser.md)
