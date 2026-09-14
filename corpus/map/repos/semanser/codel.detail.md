# semanser/codel -- full detail

[Back to orientation](codel.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/semanser/codel/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/2955eed67fb2e7e8.json](../../../wiki/dossiers/semanser/codel/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/2955eed67fb2e7e8.json)

## specifications (1 claim(s))

- [observation/documented] Codel is described as a fully autonomous AI agent that performs complicated tasks and projects using a terminal, browser, and editor. -- evidence: [README.md#L1-L3](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L1-L3) (`clm_b79c2d540c5df10d202b04e44e934e10c46e5d8397852159a4a223bb51ac25ec`)

## components (1 claim(s))

- [observation/documented] The product includes a built-in browser for fetching up-to-date web information and a built-in text editor to view modified files in the browser. -- evidence: [README.md#L8-L15](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L8-L15) (`clm_d0dbc240606b08bd7ee8eade7ffd024adac789086fdffa94b85d170e7653d200`)

## design-choices (1 claim(s))

- [observation/documented] The product claims to run everything inside a sandboxed Docker environment for security. -- evidence: [README.md#L8-L15](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L8-L15) (`clm_839efc5eac60d8e32466e2360eed23358893308048a5ee7661847ef8ea23290a`)

## workflows (2 claim(s))

- [observation/documented] Repository development practice: contributors need golang, nodejs, docker, and postgresql; they copy .env.example files for backend and frontend, run 'go run .' in backend, and use 'yarn' then 'yarn dev' in frontend. -- evidence: [DEVELOPMENT.md#L10-L10](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L10-L10), [DEVELOPMENT.md#L27-L28](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L27-L28), [DEVELOPMENT.md#L4-L7](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L4-L7), [DEVELOPMENT.md#L36-L38](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L36-L38) (`clm_195c79988df5c73ee518bbb2fa0dc62a136a817846d08eb70933c659cb3f609d`)
- [observation/documented] Repository development practice: the frontend expects VITE_API_URL without a URL scheme (e.g. localhost:8080, not http://localhost:8080), and backend optionally takes PORT (default 8080) and DATABASE_URL. -- evidence: [DEVELOPMENT.md#L13-L16](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L13-L16), [DEVELOPMENT.md#L22-L23](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L22-L23), [DEVELOPMENT.md#L18-L20](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L18-L20) (`clm_432c46a1516460a0a88f397f8d18bfe7da13b338d494b2ddfece6f03403fe7a3`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (2 claim(s))

- [observation/documented] Users access Codel through a web UI at localhost:3000 after running the Docker image with port 3000 mapped to 8080. -- evidence: [README.md#L24-L33](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L24-L33), [README.md#L37-L37](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L37-L37) (`clm_1c18b11fd6338e5e504d71a7f14cec90a4b68d0a5c08288fc9707c21da1246a4`)
- [observation/documented] The backend exposes a GraphQL playground, indicated by the successful-start message pointing to http://localhost:<port>/playground. -- evidence: [DEVELOPMENT.md#L30-L34](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L30-L34) (`clm_c23581621ffc9beba7d5a02ab9bb11a29725159cadee817a948735d204eb9ed4`)

## memory-state (1 claim(s))

- [observation/documented] All history commands and their outputs are saved in a PostgreSQL database. -- evidence: [README.md#L8-L15](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L8-L15) (`clm_368f4041d0045a98d84702e22fd9ee75cbdcf46c440caf3fb24becc4fc05495f`)

## orchestration (1 claim(s))

- [observation/documented] The agent automatically detects the next step of a task and executes it, and can pick a Docker image automatically based on the user's task. -- evidence: [README.md#L8-L15](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L8-L15) (`clm_dead2bf3dca191353b82e6c06b75df1d69f89af89a9f18485c33422fb5f2df84`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (3 claim(s))

- [observation/documented] The product supports OpenAI models (default gpt-4-0125-preview) and locally hosted Ollama models, selected via environment variables including optional custom server URLs. -- evidence: [README.md#L24-L33](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L24-L33), [README.md#L42-L47](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L42-L47) (`clm_a6bd7b6e1e50eb0a4ff979a89c06d27b95cded1688a0142a0781434e17ba684a`)
- [inference/documented] The backend appears to be written in Go, since the OpenAI model list is referenced via the go-openai Go package and development requires golang. -- evidence: [DEVELOPMENT.md#L4-L7](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/DEVELOPMENT.md#L4-L7), [README.md#L42-L47](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L42-L47) (`clm_25361fec5631fe529025b1f554ecee245f266b11a53756eac5aff8fdbf3d0c63`)
- [observation/documented] The recommended deployment is a pre-built Docker image from GitHub Container Registry, run with the Docker socket mounted into the container. -- evidence: [README.md#L18-L18](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L18-L18), [README.md#L24-L33](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L24-L33) (`clm_dafc022f8b570e01bf79715b9e400d1a8bdf6d63790ca0c6fb9c85fff14f366b`)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (1 claim(s))

- [observation/documented] The project credits two arXiv papers, the Devin announcement, the go-rod browser-automation library, and JsonGenius as inspirations or dependencies. -- evidence: [README.md#L60-L65](https://github.com/semanser/codel/blob/fe1e846c9e04f41209498ed0d88e92b15dcdfad2/README.md#L60-L65) (`clm_e7e06a8534fe79bb57799ed2d04ff6284c46ebbb7b4f2c5542025e650b6c0afc`)

