# 2389-research/translator

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-site-pages - Projects: Observatory
Latest snapshot: commit e9ccc74351d8 @ 79ac5648413f6adf

## Summary (orientation draft, not independently verified)

Selected evidence records: An interactive 'translator config' command walks users through setup, including where to store .env configuration, the OpenAI API key, and optional settings such as the default model. Translation follows a multi-stage pipeline: initial translation preserving formatting, an expert editing pass, and critique-revision cycles configurable from 1 to 5 loops for quality improvement.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 14 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

14 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (2 claim(s)):
  - [observation/documented] The codebase is modular, with files for CLI, config, cost, file I/O, frontmatter, language codes, log interpretation, prompts, token counting, and core translation logic. -- evidence: [README.md#L199-L209](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L199-L209)
  - [observation/documented] Per the spec, a provider abstraction layer offers a unified interface for OpenAI and Anthropic APIs, with model prefixes like openai:model and anthropic:model and auto-detection for unprefixed names. -- evidence: [spec.md#L313-L315](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L313-L315), [spec.md#L68-L75](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L68-L75)
- design-choices (2 claim(s)):
  - [observation/documented] Translation follows a multi-stage pipeline: initial translation preserving formatting, an expert editing pass, and critique-revision cycles configurable from 1 to 5 loops for quality improvement. -- evidence: [README.md#L171-L174](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L171-L174), [README.md#L145-L145](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L145-L145), [README.md#L5-L5](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L5-L5), [spec.md#L225-L228](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L225-L228)
  - [observation/documented] The tool specially supports markdown files with YAML frontmatter, detecting and preserving frontmatter metadata used by static site generators like Jekyll and Hugo. -- evidence: [README.md#L171-L174](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L171-L174), [README.md#L7-L7](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L7-L7), [spec.md#L129-L135](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L129-L135)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: the project uses pytest for testing, run via 'uv run pytest', with a test suite covering modules including CLI, file handling, cost, and streaming. -- evidence: [README.md#L218-L220](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L218-L220), [README.md#L216-L216](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L216-L216), [spec.md#L332-L344](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L332-L344)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] An interactive 'translator config' command walks users through setup, including where to store .env configuration, the OpenAI API key, and optional settings such as the default model. -- evidence: [README.md#L48-L48](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L48-L48), [README.md#L50-L52](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L50-L52), [README.md#L54-L57](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L54-L57)
- memory-state (2 claim(s)):
  - [observation/documented] Configuration is resolved by precedence: environment variables, then a local .env file, then ~/.translator/.env, then ~/.config/translator/.env; OPENAI_API_KEY is required for OpenAI models. -- evidence: [spec.md#L256-L260](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L256-L260), [spec.md#L294-L297](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L294-L297), [README.md#L87-L87](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L87-L87), [README.md#L59-L59](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L59-L59)
  - [observation/documented] Optional .env settings include DEFAULT_MODEL (shown as o3 in an example), OUTPUT_DIR for translated files, and LOG_LEVEL with options DEBUG through CRITICAL. -- evidence: [spec.md#L256-L260](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L256-L260), [README.md#L107-L107](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L107-L107), [README.md#L110-L110](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L110-L110), [README.md#L113-L114](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/README.md#L113-L114)
- orchestration (1 claim(s)):
  - [observation/documented] The spec describes a layered flow: main.py bootstraps TranslatorCLI, which coordinates file reading, frontmatter extraction, token counting, cost estimation, translation, and output writing. -- evidence: [spec.md#L36-L39](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L36-L39), [spec.md#L187-L210](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L187-L210), [spec.md#L44-L53](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L44-L53), [spec.md#L214-L218](https://github.com/2389-research/translator/blob/e9ccc74351d8978cffca5f35e2d1c44eb2eb8d05/spec.md#L214-L218)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
More evidence: [full detail](translator.detail.md)

Metadata and full claim list: [full detail](translator.detail.md)
Human notes ([notes](translator.notes.md), never overwritten by build)

[Back to map index](../../index.md)
