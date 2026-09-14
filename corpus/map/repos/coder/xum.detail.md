# coder/xum -- full detail

[Back to orientation](xum.md)

## Origins

- github-rename-resolution
- alltheagents.org-backing
- github-verified-rename

## Projects

- navy-yard
- Observatory

Full evidence record (JSON): [wiki/dossiers/coder/xum/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/519b231f1435b189.json](../../../wiki/dossiers/coder/xum/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/519b231f1435b189.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] Xum is a coding-agent multiplexer that runs parallel agents, each in its own isolated workspace, with a central view of git divergence; runtimes include local directories, git worktrees, and SSH remote execution. -- evidence: [docs/index.mdx#L31-L31](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/index.mdx#L31-L31), [docs/index.mdx#L5-L5](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/index.mdx#L5-L5), [README.md#L25-L34](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/README.md#L25-L34), [docs/index.mdx#L33-L36](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/index.mdx#L33-L36) (`clm_79f0bccc15085c6d6f5922e37564e57589feb2e4621790fb300e8edc77649634`)
- [observation/documented] The product supports multiple model families (sonnet-4-*, grok-*, gpt-5-*, opus-4-*), with Ollama for local LLMs and OpenRouter for a long tail of providers. -- evidence: [README.md#L25-L34](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/README.md#L25-L34), [docs/index.mdx#L33-L36](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/index.mdx#L33-L36) (`clm_8c2a446b27271eca602381c34353bdc6498f8f8c2a591069699e668ee42a99ce`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: docs are built with Mintlify, served locally via `make docs-server`, auto-deployed on push to main, and CI runs `mintlify broken-links` on every PR to validate internal links. -- evidence: [docs/README.md#L16-L18](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/README.md#L16-L18), [docs/README.md#L11-L12](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/README.md#L11-L12), [docs/README.md#L52-L53](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/README.md#L52-L53) (`clm_2f517a82e38908149685dede68a390eb11a6131e7123fbccfd5800f3948f4f8b`)
- [observation/documented] Repository development practice: a documentation style guide (STYLE.md) instructs writers to skip obvious or expected behavior, document deviations and complex workflows, and follow conventions for mermaid diagrams; new pages need frontmatter and docs.json navigation entries. -- evidence: [docs/README.md#L48-L48](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/README.md#L48-L48), [docs/STYLE.md#L7-L11](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/STYLE.md#L7-L11), [docs/STYLE.md#L3-L3](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/STYLE.md#L3-L3), [docs/README.md#L32-L35](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/README.md#L32-L35), [docs/STYLE.md#L42-L45](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/STYLE.md#L42-L45) (`clm_81ace0a7e8c3b7c7d11b5bd31411a2bf69b207724c032669e198802972f04ed2`)
- [observation/documented] Repository development practice: the README points contributors to AGENTS.md for development setup and guidelines. -- evidence: [README.md#L98-L98](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/README.md#L98-L98) (`clm_93a0a5e055fe399cc563a31d9ebe9418fbed127ead43b62f01fb986d88d55478`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] A CLI is available via npm: `npx @coder/xum run "..."` runs agent tasks and `npx @coder/xum server --port 3000` starts a server for remote/mobile access; the legacy `mux` package forwards to Xum during the rename transition. -- evidence: [docs/install.mdx#L103-L103](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/install.mdx#L103-L103), [docs/install.mdx#L87-L87](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/install.mdx#L87-L87), [docs/install.mdx#L94-L95](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/install.mdx#L94-L95), [docs/install.mdx#L91-L91](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/install.mdx#L91-L91) (`clm_3e69f344286be336ffe7f8c428e1cda6aa1beee7adcc15aa88992ad6ef6ac4c1`)
- [observation/documented] Release distribution includes signed/notarized macOS DMGs (separate Intel and Apple Silicon builds), a Linux AppImage, and a Windows installer exe; only main-branch builds are signed, so PR builds need Gatekeeper bypass on macOS. -- evidence: [docs/install.mdx#L75-L78](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/install.mdx#L75-L78), [docs/install.mdx#L22-L26](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/install.mdx#L22-L26), [docs/install.mdx#L14-L16](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/install.mdx#L14-L16) (`clm_e1015f08e7883bc2517b0f2d8b775ac0aeeba453268062488b79d5fc275a1817`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (3 claim(s))

- [observation/documented] Tool hooks let users run their own scripts around tool executions: `.xum/tool_pre` runs before every tool and a non-zero exit blocks the tool with the error shown to the agent; `.xum/tool_post` runs after tools and reports failures via hook_output. -- evidence: [docs/hooks/tools.mdx#L13-L13](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/hooks/tools.mdx#L13-L13), [docs/hooks/tools.mdx#L169-L172](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/hooks/tools.mdx#L169-L172), [docs/hooks/tools.mdx#L60-L60](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/hooks/tools.mdx#L60-L60), [docs/hooks/tools.mdx#L108-L108](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/hooks/tools.mdx#L108-L108), [docs/hooks/tools.mdx#L33-L33](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/hooks/tools.mdx#L33-L33) (`clm_b916462f5c03094e21402d3237f0369b2dcc8baa35f813b05d6538c51c0597ae`)
- [observation/documented] Hooks receive environment variables such as XUM_TOOL, XUM_WORKSPACE_ID, and XUM_TOOL_INPUT_PATH; tool input is flattened into XUM_TOOL_INPUT_<...> variables with fields over 8KB omitted, and hooks are looked up first at project level (.xum/) then user level (~/.xum/). -- evidence: [docs/hooks/tools.mdx#L216-L216](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/hooks/tools.mdx#L216-L216), [docs/hooks/tools.mdx#L149-L153](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/hooks/tools.mdx#L149-L153), [docs/hooks/tools.mdx#L155-L155](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/hooks/tools.mdx#L155-L155), [docs/hooks/tools.mdx#L180-L181](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/hooks/tools.mdx#L180-L181) (`clm_d8eec0153141ea63c52567e4958c50d9d903eb666b13d3afee02b3790425a16a`)
- [observation/documented] A `.xum/tool_env` file is sourced (not executed) before every bash tool call to configure the shell environment, affecting only bash tools; hooks must finish within 10 seconds or be terminated. -- evidence: [docs/hooks/tools.mdx#L136-L139](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/hooks/tools.mdx#L136-L139), [docs/hooks/tools.mdx#L120-L120](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/hooks/tools.mdx#L120-L120), [docs/hooks/tools.mdx#L191-L191](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/hooks/tools.mdx#L191-L191) (`clm_d4f60a455fd7c8c3144c118644502e1dd488a051684758cb7c070e05425de8a3`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The project is licensed under AGPL-3.0 (version 3 of the GNU Affero General Public License), copyright Coder Technologies, Inc. -- evidence: [README.md#L104-L104](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/README.md#L104-L104), [docs/index.mdx#L48-L48](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/index.mdx#L48-L48) (`clm_ae4318a0f2f69f6411a51610b4ba2a514d1bd895e79805c447cb395a68f9dd36`)

## limitations (1 claim(s))

- [observation/documented] Windows support is in alpha, requires Git for Windows (WSL is explicitly not supported), and tool hooks are documented as experimental with expected breaking changes. -- evidence: [docs/install.mdx#L68-L71](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/install.mdx#L68-L71), [docs/hooks/tools.mdx#L6-L6](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/hooks/tools.mdx#L6-L6), [docs/install.mdx#L60-L61](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/install.mdx#L60-L61), [docs/install.mdx#L14-L16](https://github.com/coder/xum/blob/fbbea2b16403ceb6f52f71af33a13a06c9c466fa/docs/install.mdx#L14-L16) (`clm_ede2b000b3899b1ef050a5e4526d80d4c18de1bc3ee4549498eb6d257d0ccfbc`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

