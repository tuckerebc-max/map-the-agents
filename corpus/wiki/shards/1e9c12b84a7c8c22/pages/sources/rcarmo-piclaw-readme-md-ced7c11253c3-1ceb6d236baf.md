---
access: public
aliases: []
claim_ids:
- clm_3826b62a98cbd3ef0e11e9d2e8676f4d5284ca58bfc630fd9a0478cf8922b74b
- clm_4804ca20917a57b36b3868d5c2b9a502d97ad5cc560ad63b87b744f6888a69d8
- clm_6dc90be39abbbece5ef9a8f07b1f75731eeeb60cbaa514eb6a6676a0f929f720
- clm_88e25c6a1efc253bfb4517b444d4cca2462dcc618a1d8c2e204abf135a6502aa
- clm_99795eb62a4baa9dfbf7b3ce1daf70030f4001df8cce3935375bb78940928d98
- clm_dd393718da3970cb5f37864fae731ff97ee8a53cd2c7558a8da6bb17dcd41fea
- clm_f0a7cc3e86fbac9884abe3a994002947b60be7eae74b1fbe05842a4576589645
- clm_fa3e7d1dde6d50ddf70860dd3b2b54d7d695c2c7625b99fb18ef15c53972b5b7
maturity: draft
page_id: pg_cb36119a59e850b9b9bc1ceb6d236baf
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_79e39465f3695215a27c7ec88babebfc
title: rcarmo/piclaw/README.md @ ced7c11253c3
updated_at: '2026-09-14T02:35:00Z'
---

# rcarmo/piclaw/README.md @ ced7c11253c3

<!-- rcw:begin owner=source:src_79e39465f3695215a27c7ec88babebfc block=evidence -->
- A fresh instance has no web login gate, so the Docker quick start publishes the port on localhost only until browser authentication is configured. [@claim:clm_3826b62a98cbd3ef0e11e9d2e8676f4d5284ca58bfc630fd9a0478cf8922b74b]
- The web UI supports English, Simplified Chinese and Japanese with desktop and mobile layouts, and model requests go to the configured provider including local OpenAI-compatible servers. [@claim:clm_4804ca20917a57b36b3868d5c2b9a502d97ad5cc560ad63b87b744f6888a69d8]
- PiClaw is built on the Pi Coding Agent core (earendil-works/pi) and is not directly affiliated with pi.dev; Docker deployment bundles Bun and command-line tools. [@claim:clm_6dc90be39abbbece5ef9a8f07b1f75731eeeb60cbaa514eb6a6676a0f929f720]
- The agent runs with its process user's permissions; native installs can access that user's files and commands, and containers expose mounted files and configured network access. [@claim:clm_88e25c6a1efc253bfb4517b444d4cca2462dcc618a1d8c2e204abf135a6502aa]
- Multi-user family mode is experimental: family-shared deployments share one workspace and process without filesystem isolation, isolated-container mode is unavailable, and no family-mode release gate has passed. [@claim:clm_99795eb62a4baa9dfbf7b3ce1daf70030f4001df8cce3935375bb78940928d98]
- Repository development practice: code changes should follow docs/development.md and the repository workflow in AGENTS.md, and be submitted via pull request; issues use dedicated templates. [@claim:clm_dd393718da3970cb5f37864fae731ff97ee8a53cd2c7558a8da6bb17dcd41fea]
- PiClaw is a self-hosted, single-user-by-default AI workspace built on the Pi Coding Agent, letting users chat with an agent, edit files, and run commands in one browser window. [@claim:clm_f0a7cc3e86fbac9884abe3a994002947b60be7eae74b1fbe05842a4576589645]
- Chat commands include /login for provider setup, /model for model selection, /dream for memory consolidation, /tasks and /scheduled for scheduled tasks, and /theme and /tint for UI theming. [@claim:clm_fa3e7d1dde6d50ddf70860dd3b2b54d7d695c2c7625b99fb18ef15c53972b5b7]
<!-- rcw:end owner=source:src_79e39465f3695215a27c7ec88babebfc block=evidence -->

## Researcher notes

