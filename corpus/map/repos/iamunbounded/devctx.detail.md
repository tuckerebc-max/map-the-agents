# iamunbounded/devctx -- full detail

[Back to orientation](devctx.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/iamunbounded/devctx/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/1681c23458a06fb3.json](../../../wiki/dossiers/iamunbounded/devctx/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/1681c23458a06fb3.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (1 claim(s))

- [observation/documented] The tool is designed to work with any AI coding tool by managing the prompt itself, described as the universal interface for LLMs; agents without MCP can run save/resume/log via terminal access as a fallback. -- evidence: [README.md#L104-L104](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L104-L104), [README.md#L115-L115](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L115-L115) (`clm_a2981742f7bde15ba9c8c5071b2c5b9b5f118341e52346364d40b632b22b24c0`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (5 claim(s))

- [observation/documented] DevContext is documented as a CLI tool that automatically captures and restores AI coding context, scoped to the current repo and branch. -- evidence: [README.md#L15-L15](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L15-L15) (`clm_04de95dfd2a6b3916cae6ff078323e133778187ce715cb6d439b7888a0b59889`)
- [observation/documented] Core commands are init, save (with a non-interactive --auto mode), resume (generates an AI prompt and copies to clipboard), log, and diff; these are described as working locally with zero dependencies. -- evidence: [README.md#L50-L58](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L50-L58) (`clm_fbf842dffe44b15d17cffbc47f7366525ac0f2acee0dd33a4328829feca369c6`)
- [observation/documented] Team/automation commands include handoff @user, share (committing the .devctx/ folder to git), watch (auto-save on file changes using chokidar), and hook install for a git post-commit hook. -- evidence: [README.md#L61-L66](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L61-L66) (`clm_6d8eb8e40255aa82143b1aa92145960e88ecccb5a0d3edb9aaa91f283be4f262`)
- [observation/documented] An MCP server lets AI agents natively read/write context; it is configured via npx -y devctx mcp and exposes tools devctx_save, devctx_resume, devctx_log and the resource devctx://context. -- evidence: [README.md#L86-L86](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L86-L86), [README.md#L88-L99](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L88-L99) (`clm_1d54f1e132766987ae5511154d1b8e0b3e90cab68009fa1eaca233e5adc5a8c3`)
- [observation/documented] Configuration is managed with devctx config set <key> <val> (e.g. aiProvider, watchInterval) and devctx config list. -- evidence: [README.md#L78-L81](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L78-L81) (`clm_3d417e0e9f12e1b5cf0b777f63bfe3f39bc358cb444508371cdb5ce9c3791295`)

## memory-state (1 claim(s))

- [observation/documented] Context is stored in a .devctx/ folder in the repo; each entry captures task, goal, approaches tried (and failures), key architectural decisions, and where work left off. -- evidence: [README.md#L108-L113](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L108-L113) (`clm_bab354b54149f2d84941fe7dd023667e8a84b7829ac8172c2274f6646fda6955`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] Installation is via npm (npm install -g devctx), and the watch feature uses the chokidar library. -- evidence: [README.md#L61-L66](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L61-L66), [README.md#L27-L29](https://github.com/IAmUnbounded/devctx/blob/7308ec5a514e1a81c5cc30e7a2acf11c41a97e26/README.md#L27-L29) (`clm_5b22fb3e6fb10158a4f0f35005600b8e63160a6e15f0a27416c958af25ef36c7`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

