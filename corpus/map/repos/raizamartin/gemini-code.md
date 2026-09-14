# raizamartin/gemini-code

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 6da9a30cb311 @ 9eb3066a1eb58a2e

## Summary (orientation draft, not independently verified)

Selected evidence records: The product is a terminal CLI offering interactive chat sessions, launched with the `gemini` command, with markdown rendering of responses in the terminal. Users can start a session with a specific model via `gemini --model <model>`, set a default model with `set-default-model`, and list available models with `list-models`.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 6 facet(s); 7 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components: unknown (no source-linked claim submitted for this facet)
- design-choices (2 claim(s)):
  - [observation/documented] The design intentionally mimics Claude Code: tools are used behind the scenes by the assistant to make interaction natural, and a changelog entry describes moving to Gemini's native function calling for more reliable tool usage. -- evidence: [README.md#L81-L81](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L81-L81), [README.md#L97-L102](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L97-L102)
  - [observation/documented] The system prompt was tuned to make the assistant a proactive coding partner that prioritizes creating and modifying files over printing code, with a thinking/planning phase whose output is filtered from final responses. -- evidence: [README.md#L111-L115](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L111-L115)
- workflows: unknown (no source-linked claim submitted for this facet)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The product is a terminal CLI offering interactive chat sessions, launched with the `gemini` command, with markdown rendering of responses in the terminal. -- evidence: [README.md#L3-L4](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L3-L4), [README.md#L52-L52](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L52-L52), [README.md#L8-L17](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L8-L17)
  - [observation/documented] Users can start a session with a specific model via `gemini --model <model>`, set a default model with `set-default-model`, and list available models with `list-models`. -- evidence: [README.md#L55-L55](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L55-L55), [README.md#L58-L58](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L58-L58), [README.md#L61-L62](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L61-L62)
- memory-state (2 claim(s)):
  - [observation/documented] Configuration and API keys are stored in `~/.config/gemini-code/config.yaml`, and the README notes basic history management that prevents excessive conversation length. -- evidence: [INSTALL.md#L73-L75](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/INSTALL.md#L73-L75), [INSTALL.md#L42-L42](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/INSTALL.md#L42-L42), [README.md#L8-L17](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L8-L17)
  - [observation/documented] Logs are documented as not persistent between sessions. -- evidence: [INSTALL.md#L73-L75](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/INSTALL.md#L73-L75)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions (2 claim(s)):
  - [observation/documented] The assistant automatically invokes tools itself rather than exposing them as user commands: file operations (view, edit, list, grep, glob), directory operations (ls, tree, create_directory), and bash system commands. -- evidence: [README.md#L75-L75](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L75-L75), [README.md#L77-L79](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L77-L79), [README.md#L8-L17](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L8-L17)
  - [observation/documented] The tool set also includes quality-check tools (linting, formatting), a test_runner tool for running automated tests such as pytest, and utility tools named directory_tools, quality_tools, task_complete_tool, and summarizer_tool. -- evidence: [README.md#L89-L93](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L89-L93), [README.md#L8-L17](https://github.com/raizamartin/gemini-code/blob/6da9a30cb31195d8ca19719cfd58230c43c74687/README.md#L8-L17)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
More evidence: [full detail](gemini-code.detail.md)

Metadata and full claim list: [full detail](gemini-code.detail.md)
Human notes ([notes](gemini-code.notes.md), never overwritten by build)

[Back to map index](../../index.md)
