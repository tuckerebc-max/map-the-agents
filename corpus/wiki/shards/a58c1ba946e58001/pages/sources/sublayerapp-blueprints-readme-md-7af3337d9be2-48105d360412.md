---
access: public
aliases: []
claim_ids:
- clm_18af7774347af85d50b9bdc14bc93ac2c2fc8671748934cc8b26dcbb3cb0c947
- clm_3ba16f52d426518000b1cda2bc4afd53a35cdc110f53f9e6e0b2d4129bdcd897
- clm_40117f1a9f326954dda82be8ee636fcc6162264eb45f097f3c5c120418b3bf67
- clm_4b28b9ef37e2ad618a2c639b3fda66713de6ae646d2557414ee78612608f63eb
- clm_77a57a3ab8e860518ef47f4e491f777294aec9ec2a8d85f95b0d2afaebacd4d8
- clm_82d7d805eeba38c335ad3a4040107f7e48be13cc083398b913dac6628326a2d2
- clm_887dfdec9d68c7dab2c3ca3bf61cdb9c14b68215f6b654518a128c6cda9d2800
- clm_a2c657e34463e112e2d899cf21cfd8a429c60ee04b3d4c1db740c7a7d92f3f8c
- clm_c6183f3d9e109d122b688d2e3aaca069360baee6cc1d7e6bf11d550d38bd2700
- clm_ef1f24be1034960b57022095cb5a652ae3a929193d5ac4fcb1e7371eddbdb762
- clm_fc58ecdd732395b6a10e84e3ad8277f318498510794379f6b8a9a3a07d910427
maturity: draft
page_id: pg_b3204fef67ef5aa2b4b548105d360412
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_52a80191d2d9551abf517887a09f8241
title: sublayerapp/blueprints/README.md @ 7af3337d9be2
updated_at: '2026-09-14T04:24:21Z'
---

# sublayerapp/blueprints/README.md @ 7af3337d9be2

<!-- rcw:begin owner=source:src_52a80191d2d9551abf517887a09f8241 block=evidence -->
- Editor plugins for Vim, VSCode, IntelliJ, and Sublime Text are listed as clients that interact with the app. [@claim:clm_18af7774347af85d50b9bdc14bc93ac2c2fc8671748934cc8b26dcbb3cb0c947]
- Editor plugins POST highlighted code to a blueprints#create endpoint, and highlighted descriptions to blueprint_variants#create. [@claim:clm_3ba16f52d426518000b1cda2bc4afd53a35cdc110f53f9e6e0b2d4129bdcd897]
- The project is a Ruby on Rails application for storing code chunks called 'blueprints' and using them as a base for GPT-4 to generate new code. [@claim:clm_40117f1a9f326954dda82be8ee636fcc6162264eb45f097f3c5c120418b3bf67]
- Blueprint variant creation finds the closest blueprint by description, sends its description and code plus the new description to GPT-4, and replaces the highlighted editor text with the result. [@claim:clm_4b28b9ef37e2ad618a2c639b3fda66713de6ae646d2557414ee78612608f63eb]
- The app serves a web UI at http://localhost:3000 where users can view stored blueprints and their descriptions. [@claim:clm_77a57a3ab8e860518ef47f4e491f777294aec9ec2a8d85f95b0d2afaebacd4d8]
- An alternative Google Gemini provider is supported by setting GEMINI_API_KEY and changing config.ai_provider to 'google' in config/application.rb. [@claim:clm_82d7d805eeba38c335ad3a4040107f7e48be13cc083398b913dac6628326a2d2]
- Creating a blueprint sends code to GPT-4 to generate a name and description, then stores vector embeddings of the description with the record in the database. [@claim:clm_887dfdec9d68c7dab2c3ca3bf61cdb9c14b68215f6b654518a128c6cda9d2800]
- The app depends on Postgres with pgvector (installed via Homebrew per setup instructions) and requires an OpenAI API key in the OPENAI_API_KEY environment variable. [@claim:clm_a2c657e34463e112e2d899cf21cfd8a429c60ee04b3d4c1db740c7a7d92f3f8c]
- Repository development practice: setup involves cloning the repo, running bundle install, creating and migrating the database with bin/rails commands, building Tailwind CSS, and starting the server with bin/rails s. [@claim:clm_c6183f3d9e109d122b688d2e3aaca069360baee6cc1d7e6bf11d550d38bd2700]
- Repository development practice: LLM performance specs are run by listing models in spec_perforamnce/llms/ai_models.yml and running 'rspec spec_performance', with appropriate LLM setup required per the sublayer repo. [@claim:clm_ef1f24be1034960b57022095cb5a652ae3a929193d5ac4fcb1e7371eddbdb762]
- The project targets developers using LLMs for code generation, with a demo video and blog post provided, and invites community participation via the Sublayer Discord. [@claim:clm_fc58ecdd732395b6a10e84e3ad8277f318498510794379f6b8a9a3a07d910427]
<!-- rcw:end owner=source:src_52a80191d2d9551abf517887a09f8241 block=evidence -->

## Researcher notes

