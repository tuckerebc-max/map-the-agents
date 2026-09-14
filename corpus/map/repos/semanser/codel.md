# semanser/codel

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fe1e846c9e04 @ 2955eed67fb2e7e8

## Summary (orientation draft, not independently verified)

The snapshot is the README and DEVELOPMENT.md of 'codel', a self-hosted autonomous AI agent that runs tasks in sandboxed Docker with terminal, browser, and editor tools, configurable via environment variables for OpenAI or Ollama models. Evidence covers product features, deployment, configuration, and contributor setup, but no code internals.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 13 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

13 claim(s) across 9 facet(s); 4 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] Codel is described as a fully autonomous AI agent that performs complicated tasks and projects using a terminal, browser, and editor. -- evidence: [README.md#L1-L3](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L1-L3)
- components (1 claim(s)):
  - [observation/documented] The product includes a built-in browser for fetching up-to-date web information and a built-in text editor to view modified files in the browser. -- evidence: [README.md#L8-L15](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L8-L15)
- design-choices (1 claim(s)):
  - [observation/documented] The product claims to run everything inside a sandboxed Docker environment for security. -- evidence: [README.md#L8-L15](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L8-L15)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors need golang, nodejs, docker, and postgresql; they copy .env.example files for backend and frontend, run 'go run .' in backend, and use 'yarn' then 'yarn dev' in frontend. -- evidence: [DEVELOPMENT.md#L10-L10](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L10-L10), [DEVELOPMENT.md#L27-L28](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L27-L28), [DEVELOPMENT.md#L4-L7](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L4-L7), [DEVELOPMENT.md#L36-L38](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L36-L38)
  - [observation/documented] Repository development practice: the frontend expects VITE_API_URL without a URL scheme (e.g. localhost:8080, not http://localhost:8080), and backend optionally takes PORT (default 8080) and DATABASE_URL. -- evidence: [DEVELOPMENT.md#L13-L16](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L13-L16), [DEVELOPMENT.md#L22-L23](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L22-L23), [DEVELOPMENT.md#L18-L20](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L18-L20)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (2 claim(s)):
  - [observation/documented] Users access Codel through a web UI at localhost:3000 after running the Docker image with port 3000 mapped to 8080. -- evidence: [README.md#L24-L33](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L24-L33), [README.md#L37-L37](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L37-L37)
  - [observation/documented] The backend exposes a GraphQL playground, indicated by the successful-start message pointing to http://localhost:<port>/playground. -- evidence: [DEVELOPMENT.md#L30-L34](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L30-L34)
- memory-state (1 claim(s)):
  - [observation/documented] All history commands and their outputs are saved in a PostgreSQL database. -- evidence: [README.md#L8-L15](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L8-L15)
- orchestration (1 claim(s)):
  - [observation/documented] The agent automatically detects the next step of a task and executes it, and can pick a Docker image automatically based on the user's task. -- evidence: [README.md#L8-L15](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L8-L15)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies (3 claim(s)):
  - [observation/documented] The product supports OpenAI models (default gpt-4-0125-preview) and locally hosted Ollama models, selected via environment variables including optional custom server URLs. -- evidence: [README.md#L24-L33](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L24-L33), [README.md#L42-L47](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L42-L47)
  - [inference/documented] The backend appears to be written in Go, since the OpenAI model list is referenced via the go-openai Go package and development requires golang. -- evidence: [DEVELOPMENT.md#L4-L7](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L4-L7), [README.md#L42-L47](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L42-L47)
More evidence: [full detail](codel.detail.md)

Metadata and full claim list: [full detail](codel.detail.md)
Human notes ([notes](codel.notes.md), never overwritten by build)

[Back to map index](../../index.md)
