---
access: public
aliases: []
claim_ids:
- clm_1e1fcb7891b3f3663901f0fc084712e086fee96dca92b206f018936b5b269410
- clm_26ed6a72d58732b5aca84b214ae1975bf4f7134c46eadde8b7dca50e5fe96b53
- clm_608b8f9dbd536ce1e371eed49e127fae4e691f6c44602eacde1dfa2a02d7e8f6
- clm_6f1e8eaa727ae8418f8f8845e84321a82542b68cf3a4bf233ba772c3c13f4786
- clm_7b7e508c1960b4aa3cd0bdc0e940c25b4add1f6b5f2d5b92019bf15175b7c250
- clm_8b6555cb0f50383509f9d63583306c8c531c856dcd5e23e53e84932baac59a07
- clm_8e51ee806a3525e85811682abecf35488bea205c979d1d32f97b9a621f248a12
- clm_c5407aae2cf27f5af7bfe3863285182fdb950c5cc12a1576d56cf62e8b6c24a0
- clm_d0f4b1aac6b74f505909b37059a66fc02fe0016591dd956252fb52bcbf1d9f36
- clm_d9a14fe47b596c9d295992924dcf21c6e9950551b293bb0a9fe82dfc5006ebf8
- clm_dc6e088defa02c278a24c58de49b0eadff42dca0b327b40d04bc88beb1e7cba1
maturity: draft
page_id: pg_baf66271c7f156e5a5250815737e2bcb
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_6cb75e35c1dc58b9b87c99646821fb44
title: SylphAI-Inc/adal-cli/README.md @ f278cb8ab54b
updated_at: '2026-09-14T03:16:53Z'
---

# SylphAI-Inc/adal-cli/README.md @ f278cb8ab54b

<!-- rcw:begin owner=source:src_6cb75e35c1dc58b9b87c99646821fb44 block=evidence -->
- The product claims to work with Claude, GPT, Gemini, GLM, Kimi, DeepSeek, MiniMax, and local models. [@claim:clm_1e1fcb7891b3f3663901f0fc084712e086fee96dca92b206f018936b5b269410]
- Repository development practice: contributing a skill involves forking SylphAI-Inc/skills, creating skills/<name>/SKILL.md with frontmatter (name, description, author, version), registering it in .claude-plugin/marketplace.json, and opening a pull request. [@claim:clm_26ed6a72d58732b5aca84b214ae1975bf4f7134c46eadde8b7dca50e5fe96b53]
- The CLI appears to support CLI-to-IDE handoff, allowing the same session to be opened in AdaL's agentic IDE via the /ide command. [@claim:clm_608b8f9dbd536ce1e371eed49e127fae4e691f6c44602eacde1dfa2a02d7e8f6]
- Skills are markdown files that teach the agent a repeatable workflow without touching CLI internals, stored in the SylphAI-Inc/skills repository and installable via /plugin marketplace add and /plugin install commands. [@claim:clm_6f1e8eaa727ae8418f8f8845e84321a82542b68cf3a4bf233ba772c3c13f4786]
- Native install is recommended and is said to manage AdaL's runtime and updates across platforms; install scripts are fetched from adal.sylph.ai for macOS/Linux/WSL and Windows. [@claim:clm_7b7e508c1960b4aa3cd0bdc0e940c25b4add1f6b5f2d5b92019bf15175b7c250]
- The CLI advertises review-first behavior: tool calls, file edits, diffs, and plans stay visible before sign-off, plus a command palette for switching models. [@claim:clm_8b6555cb0f50383509f9d63583306c8c531c856dcd5e23e53e84932baac59a07]
- AdaL is described as an AI coding agent that runs in the terminal, created by SylphAI and named after Ada Lovelace. [@claim:clm_8e51ee806a3525e85811682abecf35488bea205c979d1d32f97b9a621f248a12]
- The CLI exposes slash commands including /model for model choice, /ide to open the session in an IDE, /resume to restore prior context, and /stats for session health and usage. [@claim:clm_c5407aae2cf27f5af7bfe3863285182fdb950c5cc12a1576d56cf62e8b6c24a0]
- Documented feature areas include MCP server support, deep research, web search, browser use, image generation and analysis, headless mode, cron-scheduled prompts, local models, and bring-your-own API key. [@claim:clm_d0f4b1aac6b74f505909b37059a66fc02fe0016591dd956252fb52bcbf1d9f36]
- Repository development practice: issue reports should include expected vs actual behavior, reproduction steps, the CLI version from `adal -v`, OS, and terminal. [@claim:clm_d9a14fe47b596c9d295992924dcf21c6e9950551b293bb0a9fe82dfc5006ebf8]
- Running the `adal` command starts the CLI, and the first run opens the browser for authentication. [@claim:clm_dc6e088defa02c278a24c58de49b0eadff42dca0b327b40d04bc88beb1e7cba1]
<!-- rcw:end owner=source:src_6cb75e35c1dc58b9b87c99646821fb44 block=evidence -->

## Researcher notes

