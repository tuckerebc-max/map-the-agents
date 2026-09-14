# 2389-research/translator -- full detail

[Back to orientation](translator.md)

## Origins

- alltheagents.org-site-pages

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/2389-research/translator/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/79ac5648413f6adf.json](../../../wiki/dossiers/2389-research/translator/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/79ac5648413f6adf.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (2 claim(s))

- [observation/documented] The codebase is modular, with files for CLI, config, cost, file I/O, frontmatter, language codes, log interpretation, prompts, token counting, and core translation logic. -- evidence: [README.md#L199-L209](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L199-L209) (`clm_8f9a73ef3a72c6e7b7b985b69bf7f647b3f278bb0ed6072c07c1844549545410`)
- [observation/documented] Per the spec, a provider abstraction layer offers a unified interface for OpenAI and Anthropic APIs, with model prefixes like openai:model and anthropic:model and auto-detection for unprefixed names. -- evidence: [spec.md#L313-L315](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L313-L315), [spec.md#L68-L75](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L68-L75) (`clm_018e30c72b409260de177f95b4fa64741bc99c7b87dbfc2e109e64a25651b93c`)

## design-choices (2 claim(s))

- [observation/documented] Translation follows a multi-stage pipeline: initial translation preserving formatting, an expert editing pass, and critique-revision cycles configurable from 1 to 5 loops for quality improvement. -- evidence: [README.md#L171-L174](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L171-L174), [README.md#L145-L145](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L145-L145), [README.md#L5-L5](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L5-L5), [spec.md#L225-L228](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L225-L228) (`clm_b33079a20f70abeaac9d48e6dfeb65d0e22a770a6fa8eb71790b772c8667736c`)
- [observation/documented] The tool specially supports markdown files with YAML frontmatter, detecting and preserving frontmatter metadata used by static site generators like Jekyll and Hugo. -- evidence: [README.md#L171-L174](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L171-L174), [README.md#L7-L7](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L7-L7), [spec.md#L129-L135](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L129-L135) (`clm_45e4739c007133a748e6984bce4c1cf2a9a8c7673eab49de40ba44d1b9f5f911`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: the project uses pytest for testing, run via 'uv run pytest', with a test suite covering modules including CLI, file handling, cost, and streaming. -- evidence: [README.md#L218-L220](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L218-L220), [README.md#L216-L216](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L216-L216), [spec.md#L332-L344](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L332-L344) (`clm_f4e4835e7798b232aa17cc2cfec8c700b3f112c086a09a90164502a178692642`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] An interactive 'translator config' command walks users through setup, including where to store .env configuration, the OpenAI API key, and optional settings such as the default model. -- evidence: [README.md#L48-L48](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L48-L48), [README.md#L50-L52](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L50-L52), [README.md#L54-L57](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L54-L57) (`clm_531732df3e25e5901e4d6b0de3d6f637260714d9113b2e2f217d8c72fdc9f2ab`)

## memory-state (2 claim(s))

- [observation/documented] Configuration is resolved by precedence: environment variables, then a local .env file, then ~/.translator/.env, then ~/.config/translator/.env; OPENAI_API_KEY is required for OpenAI models. -- evidence: [spec.md#L256-L260](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L256-L260), [spec.md#L294-L297](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L294-L297), [README.md#L87-L87](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L87-L87), [README.md#L59-L59](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L59-L59) (`clm_99963fd4e80e339846d1f08f6e72472738cc966c137573b914238755a9b1d8db`)
- [observation/documented] Optional .env settings include DEFAULT_MODEL (shown as o3 in an example), OUTPUT_DIR for translated files, and LOG_LEVEL with options DEBUG through CRITICAL. -- evidence: [spec.md#L256-L260](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L256-L260), [README.md#L107-L107](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L107-L107), [README.md#L110-L110](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L110-L110), [README.md#L113-L114](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L113-L114) (`clm_80e3177c2e4d9d0cad0f89895e55406d808fae615414a5dc07f475d37f888c14`)

## orchestration (1 claim(s))

- [observation/documented] The spec describes a layered flow: main.py bootstraps TranslatorCLI, which coordinates file reading, frontmatter extraction, token counting, cost estimation, translation, and output writing. -- evidence: [spec.md#L36-L39](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L36-L39), [spec.md#L187-L210](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L187-L210), [spec.md#L44-L53](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L44-L53), [spec.md#L214-L218](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L214-L218) (`clm_3aecd57346c65c1f128501048c031576335c2b59d576c09b9026bbfda5898611`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [inference/documented] The spec claims analytics including translation accuracy tracking and quality metrics; this appears to be documented intent rather than a demonstrated benchmark harness. -- evidence: [spec.md#L433-L436](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L433-L436) (`clm_e49b44f280c8efc429c65888d2fc1ea079132ee5827b839dd71c7c3ebc78e6fb`)

## dependencies (2 claim(s))

- [observation/documented] Runtime dependencies include openai>=1.78.1, python-dotenv, rich, tiktoken, pycountry, and python-frontmatter, with pytest for testing; Python 3.13+ is required. -- evidence: [README.md#L233-L241](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L233-L241), [spec.md#L395-L397](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L395-L397) (`clm_fe12b96858f7fbcd379d50aae99e7136c7faddd750b44f9f73526fbf372ffcfd`)
- [observation/documented] The spec additionally lists anthropic>=0.25.0 as a core API dependency and swarm (from GitHub) for future use. -- evidence: [spec.md#L161-L163](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L161-L163) (`clm_2b347d8345e6c34270edc78e462a8b9fe5ed3a2028b16b67d4eb22fe2f0a7f7f`)

## limitations (2 claim(s))

- [observation/documented] The spec's issues analysis lists current limitations including inefficient streaming token counting, potential memory leaks in the cancellation handler, race conditions in streaming, and hard-coded parameters and paths. -- evidence: [spec.md#L441-L450](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L441-L450) (`clm_c71fdbc188bde49dcf50eaa7e494c895c96561be423553524225f3bd2696e362`)
- [observation/documented] Documented limitations include no caching and single-file-only processing, both noted as future enhancements, plus file size constrained by model token limits. -- evidence: [spec.md#L355-L358](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L355-L358), [spec.md#L411-L416](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L411-L416), [spec.md#L361-L364](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L361-L364) (`clm_ff652c28fab1c9efa9c61895ab8cde91d18d7feb936cd6a651a542b38055ddfb`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

