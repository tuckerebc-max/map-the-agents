# raizamartin/gemini-code -- full detail

[Back to orientation](gemini-code.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/raizamartin/gemini-code/6da9a30cb31195d8ca19719cfd58230c43c74687/9eb3066a1eb58a2e.json](../../../wiki/dossiers/raizamartin/gemini-code/6da9a30cb31195d8ca19719cfd58230c43c74687/9eb3066a1eb58a2e.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] The design intentionally mimics Claude Code: tools are used behind the scenes by the assistant to make interaction natural, and a changelog entry describes moving to Gemini's native function calling for more reliable tool usage. -- evidence: [README.md#L81-L81](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L81-L81), [README.md#L97-L102](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L97-L102) (`clm_3aae5a308510d3a434dfaff69ece4212dd7f183b1847f9d163c3f4f66adb4b68`)
- [observation/documented] The system prompt was tuned to make the assistant a proactive coding partner that prioritizes creating and modifying files over printing code, with a thinking/planning phase whose output is filtered from final responses. -- evidence: [README.md#L111-L115](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L111-L115) (`clm_2b987f4b25d74c599760dd3c0cc90db23102816fddc1476308af1c61f84d9694`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The product is a terminal CLI offering interactive chat sessions, launched with the `gemini` command, with markdown rendering of responses in the terminal. -- evidence: [README.md#L3-L4](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L3-L4), [README.md#L52-L52](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L52-L52), [README.md#L8-L17](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L8-L17) (`clm_ec7d5ccf6dad4a7e5f182e73ef9ddb75e947a61065dcc827e169ed2385ebf450`)
- [observation/documented] Users can start a session with a specific model via `gemini --model <model>`, set a default model with `set-default-model`, and list available models with `list-models`. -- evidence: [README.md#L55-L55](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L55-L55), [README.md#L58-L58](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L58-L58), [README.md#L61-L62](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L61-L62) (`clm_1b88c573f706913b85a7634b11e8d4cc5bb2ad8ca57c717cab113a4684ea7d2e`)
- [observation/documented] Interactive sessions support in-chat commands including `/exit` to leave the session and `/help` to display help information. -- evidence: [README.md#L68-L69](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L68-L69), [INSTALL.md#L60-L61](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/INSTALL.md#L60-L61) (`clm_db359971d16c28036788ca5ecee633676d2ea3b48e25c21d84672bb5208bfc18`)

## memory-state (2 claim(s))

- [observation/documented] Configuration and API keys are stored in `~/.config/gemini-code/config.yaml`, and the README notes basic history management that prevents excessive conversation length. -- evidence: [INSTALL.md#L73-L75](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/INSTALL.md#L73-L75), [INSTALL.md#L42-L42](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/INSTALL.md#L42-L42), [README.md#L8-L17](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L8-L17) (`clm_f029ec0e629e5ad43e70585bc34f37ee6c2414434a59941a54bdcddb2aa1ec55`)
- [observation/documented] Logs are documented as not persistent between sessions. -- evidence: [INSTALL.md#L73-L75](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/INSTALL.md#L73-L75) (`clm_d70b0a6afec5f6bbeba4ac80a78c758df931667f6f8ebd1e94c47cbd4583cc1f`)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (2 claim(s))

- [observation/documented] The assistant automatically invokes tools itself rather than exposing them as user commands: file operations (view, edit, list, grep, glob), directory operations (ls, tree, create_directory), and bash system commands. -- evidence: [README.md#L75-L75](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L75-L75), [README.md#L77-L79](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L77-L79), [README.md#L8-L17](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L8-L17) (`clm_0247b9ab9dd034769fb40325b7d32697a68894b7933fc13b4a0359299a2f1f9d`)
- [observation/documented] The tool set also includes quality-check tools (linting, formatting), a test_runner tool for running automated tests such as pytest, and utility tools named directory_tools, quality_tools, task_complete_tool, and summarizer_tool. -- evidence: [README.md#L89-L93](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L89-L93), [README.md#L8-L17](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L8-L17) (`clm_a25c8b4c01aa396d3446a157208708dd97c9fa7ab71b11baf07e066e0e90a5cb`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The tool is powered by Gemini 2.5 Pro by default with support for other models such as Gemini 1.5 Pro, and requires a Google API key configured via `gemini setup`. -- evidence: [INSTALL.md#L33-L35](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/INSTALL.md#L33-L35), [README.md#L3-L4](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L3-L4), [README.md#L45-L46](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L45-L46), [README.md#L8-L17](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L8-L17) (`clm_c32702d4528c66a9f9b2253d2cd2eea72d28794184acf3da111b5b969295f6f1`)

## limitations (1 claim(s))

- [observation/documented] A known issue: config files created with earlier versions may need to be deleted (`rm -rf ~/.config/gemini-code`) to get correct defaults. -- evidence: [README.md#L146-L149](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L146-L149) (`clm_46cd36846b7029eece92760c7224d3aea82ffba72eeb587f0a31accfdc326c56`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

