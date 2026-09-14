# sublayerapp/blueprints

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 7af3337d9be2 @ 701e6aedcbb26b2c

## Summary (orientation draft, not independently verified)

Blueprints is a Ruby on Rails app that stores code snippets ('blueprints') with GPT-4-generated descriptions and vector embeddings, and generates new code from them via editor plugins. Evidence is README-only, covering setup, usage, API flow, and LLM performance spec instructions.

## Source coverage

Source coverage (complete): 1 of 1 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 7 facet(s); 6 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] The project is a Ruby on Rails application for storing code chunks called 'blueprints' and using them as a base for GPT-4 to generate new code. -- evidence: [README.md#L3-L5](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L3-L5)
- components (2 claim(s)):
  - [observation/documented] Creating a blueprint sends code to GPT-4 to generate a name and description, then stores vector embeddings of the description with the record in the database. -- evidence: [README.md#L58-L59](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L58-L59), [README.md#L61-L62](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L61-L62)
  - [observation/documented] Blueprint variant creation finds the closest blueprint by description, sends its description and code plus the new description to GPT-4, and replaces the highlighted editor text with the result. -- evidence: [README.md#L67-L69](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L67-L69), [README.md#L71-L73](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L71-L73)
- design-choices (1 claim(s)):
  - [observation/documented] An alternative Google Gemini provider is supported by setting GEMINI_API_KEY and changing config.ai_provider to 'google' in config/application.rb. -- evidence: [README.md#L18-L20](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L18-L20)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: setup involves cloning the repo, running bundle install, creating and migrating the database with bin/rails commands, building Tailwind CSS, and starting the server with bin/rails s. -- evidence: [README.md#L31-L37](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L31-L37)
  - [observation/documented] Repository development practice: LLM performance specs are run by listing models in spec_perforamnce/llms/ai_models.yml and running 'rspec spec_performance', with appropriate LLM setup required per the sublayer repo. -- evidence: [README.md#L49-L50](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L49-L50), [README.md#L52-L52](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L52-L52)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] Editor plugins for Vim, VSCode, IntelliJ, and Sublime Text are listed as clients that interact with the app. -- evidence: [README.md#L25-L29](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L25-L29)
  - [observation/documented] Editor plugins POST highlighted code to a blueprints#create endpoint, and highlighted descriptions to blueprint_variants#create. -- evidence: [README.md#L67-L69](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L67-L69), [README.md#L58-L59](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L58-L59)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (1 claim(s)):
  - [observation/documented] The app depends on Postgres with pgvector (installed via Homebrew per setup instructions) and requires an OpenAI API key in the OPENAI_API_KEY environment variable. -- evidence: [README.md#L22-L23](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L22-L23), [README.md#L14-L15](https://github.com/sublayerapp/blueprints/blob/7af3337d9be220a01480034416257a2058eddb9c/README.md#L14-L15)
- limitations: unknown (no source-linked claim submitted for this facet)
- relevance (1 claim(s)):
More evidence: [full detail](blueprints.detail.md)

Metadata and full claim list: [full detail](blueprints.detail.md)
Human notes ([notes](blueprints.notes.md), never overwritten by build)

[Back to map index](../../index.md)
