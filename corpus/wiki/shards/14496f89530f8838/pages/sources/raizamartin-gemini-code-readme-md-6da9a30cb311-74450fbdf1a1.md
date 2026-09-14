---
access: public
aliases: []
claim_ids:
- clm_0247b9ab9dd034769fb40325b7d32697a68894b7933fc13b4a0359299a2f1f9d
- clm_1b88c573f706913b85a7634b11e8d4cc5bb2ad8ca57c717cab113a4684ea7d2e
- clm_2b987f4b25d74c599760dd3c0cc90db23102816fddc1476308af1c61f84d9694
- clm_3aae5a308510d3a434dfaff69ece4212dd7f183b1847f9d163c3f4f66adb4b68
- clm_46cd36846b7029eece92760c7224d3aea82ffba72eeb587f0a31accfdc326c56
- clm_a25c8b4c01aa396d3446a157208708dd97c9fa7ab71b11baf07e066e0e90a5cb
- clm_c32702d4528c66a9f9b2253d2cd2eea72d28794184acf3da111b5b969295f6f1
- clm_db359971d16c28036788ca5ecee633676d2ea3b48e25c21d84672bb5208bfc18
- clm_ec7d5ccf6dad4a7e5f182e73ef9ddb75e947a61065dcc827e169ed2385ebf450
- clm_f029ec0e629e5ad43e70585bc34f37ee6c2414434a59941a54bdcddb2aa1ec55
maturity: draft
page_id: pg_c77c4a58bc245d0a8e4074450fbdf1a1
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_8f574270adde57c099a742575aa8bad2
title: raizamartin/gemini-code/README.md @ 6da9a30cb311
updated_at: '2026-09-14T02:34:11Z'
---

# raizamartin/gemini-code/README.md @ 6da9a30cb311

<!-- rcw:begin owner=source:src_8f574270adde57c099a742575aa8bad2 block=evidence -->
- The assistant automatically invokes tools itself rather than exposing them as user commands: file operations (view, edit, list, grep, glob), directory operations (ls, tree, create_directory), and bash system commands. [@claim:clm_0247b9ab9dd034769fb40325b7d32697a68894b7933fc13b4a0359299a2f1f9d]
- Users can start a session with a specific model via `gemini --model <model>`, set a default model with `set-default-model`, and list available models with `list-models`. [@claim:clm_1b88c573f706913b85a7634b11e8d4cc5bb2ad8ca57c717cab113a4684ea7d2e]
- The system prompt was tuned to make the assistant a proactive coding partner that prioritizes creating and modifying files over printing code, with a thinking/planning phase whose output is filtered from final responses. [@claim:clm_2b987f4b25d74c599760dd3c0cc90db23102816fddc1476308af1c61f84d9694]
- The design intentionally mimics Claude Code: tools are used behind the scenes by the assistant to make interaction natural, and a changelog entry describes moving to Gemini's native function calling for more reliable tool usage. [@claim:clm_3aae5a308510d3a434dfaff69ece4212dd7f183b1847f9d163c3f4f66adb4b68]
- A known issue: config files created with earlier versions may need to be deleted (`rm -rf ~/.config/gemini-code`) to get correct defaults. [@claim:clm_46cd36846b7029eece92760c7224d3aea82ffba72eeb587f0a31accfdc326c56]
- The tool set also includes quality-check tools (linting, formatting), a test_runner tool for running automated tests such as pytest, and utility tools named directory_tools, quality_tools, task_complete_tool, and summarizer_tool. [@claim:clm_a25c8b4c01aa396d3446a157208708dd97c9fa7ab71b11baf07e066e0e90a5cb]
- The tool is powered by Gemini 2.5 Pro by default with support for other models such as Gemini 1.5 Pro, and requires a Google API key configured via `gemini setup`. [@claim:clm_c32702d4528c66a9f9b2253d2cd2eea72d28794184acf3da111b5b969295f6f1]
- Interactive sessions support in-chat commands including `/exit` to leave the session and `/help` to display help information. [@claim:clm_db359971d16c28036788ca5ecee633676d2ea3b48e25c21d84672bb5208bfc18]
- The product is a terminal CLI offering interactive chat sessions, launched with the `gemini` command, with markdown rendering of responses in the terminal. [@claim:clm_ec7d5ccf6dad4a7e5f182e73ef9ddb75e947a61065dcc827e169ed2385ebf450]
- Configuration and API keys are stored in `~/.config/gemini-code/config.yaml`, and the README notes basic history management that prevents excessive conversation length. [@claim:clm_f029ec0e629e5ad43e70585bc34f37ee6c2414434a59941a54bdcddb2aa1ec55]
<!-- rcw:end owner=source:src_8f574270adde57c099a742575aa8bad2 block=evidence -->

## Researcher notes

