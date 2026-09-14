# agi-is-going-to-arrive/ahadiff -- full detail

[Back to orientation](ahadiff.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/agi-is-going-to-arrive/ahadiff/36da35e9fd4092da79c00fadec03f3b62615ba58/6283c64863f1d387.json](../../../wiki/dossiers/agi-is-going-to-arrive/ahadiff/36da35e9fd4092da79c00fadec03f3b62615ba58/6283c64863f1d387.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] Deterministic scoring covers eight dimensions with required evidence and safety checks; an optional LLM judge gives feedback but cannot override the final verdict. -- evidence: [README.md#L128-L132](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L128-L132) (`clm_c9d11cfdbd4a4b0abbd50ab2e04c973f977c85a9bca96ebb8d0ef573ee24adc0`)
- [observation/documented] Snapshots store a sanitized copy of an earlier file for later comparison without modifying originals, and are learning references rather than full backups. -- evidence: [README.md#L13-L17](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L13-L17), [README.md#L102-L102](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L102-L102) (`clm_0b3a056311e989daf947b7caa3cd1ae1682fc22615e5ce23a6e55cd99b3fe7ff`)

## design-choices (1 claim(s))

- [observation/documented] Default privacy mode is strict_local; redacted_remote or explicit_remote must be chosen before remote providers, and the tool checks for secrets and suspicious instructions while advising user inspection. -- evidence: [README.md#L122-L122](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L122-L122) (`clm_aac25ea095e6a57f610dc7d102acaf65b600ee144660cf12e1d1ed226bc57422`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: building from source requires cloning the repo, running 'uv sync --locked --dev', and building the viewer with pnpm before an editable uv tool install. -- evidence: [README.md#L188-L195](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L188-L195), [README.md#L186-L186](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L186-L186) (`clm_9d921746b939c8d1966037af9b50f7e5cefe63e1c2bd32cbfee085b678aa89f8`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] ahadiff serve creates local state and opens a WebUI at http://127.0.0.1:8765, with a --no-browser option; ordinary folders work while init and doctor target Git repositories. -- evidence: [README.md#L54-L54](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L54-L54) (`clm_4ed23ddcbc03f3f6c674e8e600f5b5dd2f593266340e9f57e257c7bfd3a5c3be`)
- [observation/documented] The WebUI supports five learning sources: Git changes, two files, a pasted diff, a saved snapshot, or a single Markdown document, with local preview before a generation request. -- evidence: [README.md#L13-L17](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L13-L17), [README.md#L61-L67](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L61-L67) (`clm_77d6678623dd8b141f1382865910a300ba1b915fa8ed1189178c45413c446bed`)
- [observation/documented] A read-only MCP server can be registered with tools like Claude or Codex via 'ahadiff mcp-server --repo-root /path/to/workspace'. -- evidence: [README.md#L149-L149](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L149-L149), [README.md#L151-L154](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L151-L154) (`clm_cb7e292e59de524ca91d765fdb90dcd08d4d004e75dc95cff20ced5ce7c01352`)

## memory-state (1 claim(s))

- [observation/documented] Learning history and review records are stored under .ahadiff/ in each working folder; API keys go into a scope-specific .env with an environment-variable reference in config.toml. -- evidence: [README.md#L124-L124](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L124-L124), [README.md#L42-L42](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L42-L42) (`clm_2a38d9559b3b741bdaa06e734f7b3221b43cd041c00fc473e36c192379427a0a`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (2 claim(s))

- [observation/documented] Installable via pipx or uv tool; an optional 'optimizer' extra adds torch for FSRS parameter optimization, which base review and scheduling do not need. -- evidence: [README.md#L26-L26](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L26-L26), [README.md#L23-L24](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L23-L24), [README.md#L44-L44](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L44-L44) (`clm_ce97dfe7885cb2c9f63e4f0a44f317884a99bc12761d61973c35326daf48b9f8`)
- [observation/documented] Provider classes include openai, openai_responses, gemini, anthropic, azure, newapi, openai_compat, lmstudio, and ollama, covering local and remote LLM endpoints. -- evidence: [README.md#L116-L116](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L116-L116) (`clm_3c7c4ad2b5103bf40b8561d79c921f82bb03942894df8d4eaf13a14f5c6e6b32`)

## limitations (2 claim(s))

- [observation/documented] Documented limits: no PDF ingestion or web-page capture; directory comparison and Git hooks require macOS/Linux; browser-selected files capped at 256 KiB each (512 KiB per pair) and pasted diffs at 64 KiB. -- evidence: [README.md#L69-L69](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L69-L69), [README.md#L158-L162](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L158-L162) (`clm_abc8b65115441dd9d047a6433a1e36944cbf6cbe32ade01160de710671af6703`)
- [observation/documented] The tool does not execute exercise or notebook code; practice statistics reflect recorded attempts and self-assessments, not measured learning gain. -- evidence: [README.md#L128-L132](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L128-L132), [README.md#L158-L162](https://github.com/AGI-is-going-to-arrive/ahadiff/blob/36da35e9fd4092da79c00fadec03f3b62615ba58/README.md#L158-L162) (`clm_a10df509f6f6fcb6df4aee8bb732524ce867ff7cfb08f75ab02f5a64fec1493c`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

