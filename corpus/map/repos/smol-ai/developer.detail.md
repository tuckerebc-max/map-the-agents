# smol-ai/developer -- full detail

[Back to orientation](developer.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/smol-ai/developer/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/7aee3279a6f05064.json](../../../wiki/dossiers/smol-ai/developer/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/7aee3279a6f05064.json)

## specifications (1 claim(s))

- [observation/documented] The tool is described as a 'junior developer' agent that scaffolds an entire codebase from a product spec, or provides building blocks to embed a similar agent in other apps. -- evidence: [readme.md#L20-L21](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L20-L21), [readme.md#L18-L18](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L18-L18) (`clm_40e8742748f4b353e4ab660fa9abb1d37056bbfa74d9b9ca256705cdcff6697b`)

## components (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## design-choices (2 claim(s))

- [observation/documented] For whole-program coherence, the tool adds an intermediate step generating shared_dependencies.md and insists on using it when generating each file, since hallucinated cross-file dependencies break programs. -- evidence: [readme.md#L206-L224](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L206-L224) (`clm_5d66398481cecc9e6dca38a982a4972da34aedd4647540ca7b9dd29dfb03572d`)
- [observation/documented] The workflow is human-in-the-loop: the human writes/extends a markdown prompt, runs generated code, and pastes errors back into the prompt; debugger.py reads the whole codebase to suggest specific fixes. -- evidence: [readme.md#L60-L67](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L60-L67), [readme.md#L58-L58](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L58-L58) (`clm_4170e27e02cc42fc0cdb0a3b06496b14d3a24e1eb0e926a39a46cdc164378528`)

## workflows (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## skills-patterns (1 claim(s))

- [observation/documented] The bundled prompt.md is a detailed spec for a Chrome Manifest V3 extension that summarizes page content via the Anthropic Claude API, choosing claude-instant-v1 or the 100k model based on content length. -- evidence: [prompt.md#L1-L1](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/prompt.md#L1-L1), [prompt.md#L49-L69](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/prompt.md#L49-L69) (`clm_1a503605b8c6bb30c022066e51d40172e52eacbbae83de9659b1e989592eda1b`)

## interfaces (4 claim(s))

- [observation/documented] In git repo mode the CLI is run as 'python main.py' with a prompt string argument, defaulting to gpt-4-0613, and supports --prompt and --debug flags. -- evidence: [readme.md#L42-L44](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L42-L44), [readme.md#L38-L38](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L38-L38) (`clm_de4b3dcc199b979c1c8a31ca1cba229cf0effd5b92a3eb30f1550755b4f825bd`)
- [observation/documented] Library mode exposes functions plan(), specify_file_paths(), and generate_code_sync() from smol_dev.prompts, plus an async generate_code() variant, installable via pip as smol_dev. -- evidence: [readme.md#L99-L100](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L99-L100), [readme.md#L79-L81](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L79-L81), [readme.md#L102-L104](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L102-L104), [readme.md#L85-L86](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L85-L86), [readme.md#L90-L90](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L90-L90) (`clm_6de23617388c9955e472d89de91b27965f3e49d63b4fcb1a3edd41d793b0e82a`)
- [observation/documented] specify_file_paths reportedly relies on OpenAI's Function Calling API to guarantee JSON output of file paths. -- evidence: [readme.md#L94-L94](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L94-L94) (`clm_d46d9cd4fa4a473c72a80352c464eda15edba5034589e4ffab62e9bf3b901f48`)
- [observation/documented] An API mode implements the Agent Protocol: start with 'poetry run api' or 'python smol_dev/api.py', then create tasks and execute steps via POST endpoints on localhost:8000. -- evidence: [readme.md#L107-L114](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L107-L114), [readme.md#L118-L126](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L118-L126), [readme.md#L135-L138](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L135-L138) (`clm_e0755b3cbd2e4cf37b6c09685056b0fb17121a4f24ecd2ec96aa16ceba3db888`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (1 claim(s))

- [observation/documented] The repo is installed with poetry ('poetry install') in git repo mode, and the library is published as the pip package smol_dev. -- evidence: [readme.md#L79-L81](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L79-L81), [readme.md#L33-L35](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L33-L35) (`clm_87b8ad6587bdbdd17dfcd877e5a0b68cce67d0c668b26c9db35865373c468892`)

## limitations (3 claim(s))

- [observation/documented] Generation is slow: the README reports roughly 2-4 minutes to generate a program with GPT4 even with parallelization via Modal, occasionally spiking higher. -- evidence: [readme.md#L234-L234](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L234-L234) (`clm_25a22abb2fce87d1fdebcc579ff996b5087be6662439dbec544342611709e7ab`)
- [observation/documented] The shared_dependencies.md approach is acknowledged as imperfect, sometimes not comprehensive about hard dependencies between files, requiring explicit names in the prompt as a workaround. -- evidence: [readme.md#L206-L224](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L206-L224) (`clm_48a92d73476203355692fa7c90fb2535b48f5d4841e452f12384498c7abd6248`)
- [observation/documented] Using Anthropic as the coding layer reportedly does not work well because Anthropic does not follow instructions to generate file code reliably. -- evidence: [readme.md#L241-L254](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L241-L254) (`clm_ed74e1f69cdf1d5dcd11f67b12bf2314572b3a3f62ca2ae79938e737b55f069e`)

## relevance (1 claim(s))

- [observation/documented] Community forks exist in JS/TS, C#/.NET, and Go, and the README links demos including a Chrome extension and a React/Node/MongoDB full-stack scaffold. -- evidence: [readme.md#L183-L183](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L183-L183), [readme.md#L177-L179](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L177-L179), [readme.md#L195-L199](https://github.com/smol-ai/developer/blob/a6747d1a6ccd983c54a483c4a4fb1fa4bf740e82/readme.md#L195-L199) (`clm_16fc195e30b88a6f14b3c4327b712a21a8e9a48e454e2eb808cb1d3f047c6a00`)

