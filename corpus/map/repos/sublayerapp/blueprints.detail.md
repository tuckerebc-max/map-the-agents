# sublayerapp/blueprints -- full detail

[Back to orientation](blueprints.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/sublayerapp/blueprints/7af3337d9be220a01480034416257a2058eddb9c/701e6aedcbb26b2c.json](../../../wiki/dossiers/sublayerapp/blueprints/7af3337d9be220a01480034416257a2058eddb9c/701e6aedcbb26b2c.json)

## specifications (1 claim(s))

- [observation/documented] The project is a Ruby on Rails application for storing code chunks called 'blueprints' and using them as a base for GPT-4 to generate new code. -- evidence: [README.md#L3-L5](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L3-L5) (`clm_40117f1a9f326954dda82be8ee636fcc6162264eb45f097f3c5c120418b3bf67`)

## components (2 claim(s))

- [observation/documented] Creating a blueprint sends code to GPT-4 to generate a name and description, then stores vector embeddings of the description with the record in the database. -- evidence: [README.md#L58-L59](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L58-L59), [README.md#L61-L62](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L61-L62) (`clm_887dfdec9d68c7dab2c3ca3bf61cdb9c14b68215f6b654518a128c6cda9d2800`)
- [observation/documented] Blueprint variant creation finds the closest blueprint by description, sends its description and code plus the new description to GPT-4, and replaces the highlighted editor text with the result. -- evidence: [README.md#L67-L69](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L67-L69), [README.md#L71-L73](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L71-L73) (`clm_4b28b9ef37e2ad618a2c639b3fda66713de6ae646d2557414ee78612608f63eb`)

## design-choices (1 claim(s))

- [observation/documented] An alternative Google Gemini provider is supported by setting GEMINI_API_KEY and changing config.ai_provider to 'google' in config/application.rb. -- evidence: [README.md#L18-L20](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L18-L20) (`clm_82d7d805eeba38c335ad3a4040107f7e48be13cc083398b913dac6628326a2d2`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: setup involves cloning the repo, running bundle install, creating and migrating the database with bin/rails commands, building Tailwind CSS, and starting the server with bin/rails s. -- evidence: [README.md#L31-L37](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L31-L37) (`clm_c6183f3d9e109d122b688d2e3aaca069360baee6cc1d7e6bf11d550d38bd2700`)
- [observation/documented] Repository development practice: LLM performance specs are run by listing models in spec_perforamnce/llms/ai_models.yml and running 'rspec spec_performance', with appropriate LLM setup required per the sublayer repo. -- evidence: [README.md#L49-L50](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L49-L50), [README.md#L52-L52](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L52-L52) (`clm_ef1f24be1034960b57022095cb5a652ae3a929193d5ac4fcb1e7371eddbdb762`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] Editor plugins for Vim, VSCode, IntelliJ, and Sublime Text are listed as clients that interact with the app. -- evidence: [README.md#L25-L29](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L25-L29) (`clm_18af7774347af85d50b9bdc14bc93ac2c2fc8671748934cc8b26dcbb3cb0c947`)
- [observation/documented] Editor plugins POST highlighted code to a blueprints#create endpoint, and highlighted descriptions to blueprint_variants#create. -- evidence: [README.md#L67-L69](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L67-L69), [README.md#L58-L59](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L58-L59) (`clm_3ba16f52d426518000b1cda2bc4afd53a35cdc110f53f9e6e0b2d4129bdcd897`)
- [observation/documented] The app serves a web UI at http://localhost:3000 where users can view stored blueprints and their descriptions. -- evidence: [README.md#L44-L45](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L44-L45), [README.md#L41-L42](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L41-L42) (`clm_77a57a3ab8e860518ef47f4e491f777294aec9ec2a8d85f95b0d2afaebacd4d8`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The app depends on Postgres with pgvector (installed via Homebrew per setup instructions) and requires an OpenAI API key in the OPENAI_API_KEY environment variable. -- evidence: [README.md#L22-L23](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L22-L23), [README.md#L14-L15](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L14-L15) (`clm_a2c657e34463e112e2d899cf21cfd8a429c60ee04b3d4c1db740c7a7d92f3f8c`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The project targets developers using LLMs for code generation, with a demo video and blog post provided, and invites community participation via the Sublayer Discord. -- evidence: [README.md#L7-L7](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L7-L7), [README.md#L9-L9](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L9-L9), [README.md#L80-L80](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L80-L80) (`clm_fc58ecdd732395b6a10e84e3ad8277f318498510794379f6b8a9a3a07d910427`)

