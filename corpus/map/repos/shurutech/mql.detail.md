# shurutech/mql -- full detail

[Back to orientation](mql.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/shurutech/mql/fabf1ebc012355eab7ce536e049bee24297030f0/b7f23b7c537a4ed0.json](../../../wiki/dossiers/shurutech/mql/fabf1ebc012355eab7ce536e049bee24297030f0/b7f23b7c537a4ed0.json)

## specifications (1 claim(s))

- [observation/documented] MQL (My Query Language) transforms natural language queries into executable SQL, intended for users without coding knowledge, using a connected or uploaded database schema. -- evidence: [README.md#L3-L3](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L3-L3) (`clm_17e197f4fe12cc5875051e30de10e2fa609456dae2e4b1ef16da10dc2d5d164f`)

## components (1 claim(s))

- [observation/documented] A default login user (admin@example.com / admin) is created when running via Docker; production guidance says to delete it and create users via a scripts/create_user.py script inside the backend container. -- evidence: [README.md#L70-L76](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L70-L76), [README.md#L65-L67](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L65-L67) (`clm_b6306cd3b7f916fa7a445e2a9753641a5473ec0bd63c1d3ea9d7c76261cca850`)

## design-choices (1 claim(s))

- [inference/documented] The use of the pgvector extension and a vector database setup suggests MQL likely uses embeddings for schema or query matching, though the README does not state this mechanism explicitly. -- evidence: [README.md#L98-L98](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L98-L98), [README.md#L132-L135](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L132-L135), [README.md#L124-L124](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L124-L124) (`clm_7c6b217f580737390807d1170302d58cd3573e1319f359b9baaa86e9e953579f`)

## workflows (3 claim(s))

- [observation/documented] Repository development practice: local Docker setup requires cloning the repo, setting OPENAI_API_KEY and DATABASE_URL, then running make install; make up, make restart, and make down manage containers. -- evidence: [README.md#L54-L57](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L54-L57), [README.md#L24-L24](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L24-L24), [README.md#L49-L52](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L49-L52), [README.md#L39-L42](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L39-L42), [README.md#L35-L37](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L35-L37), [README.md#L26-L28](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L26-L28), [README.md#L30-L33](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L30-L33), [README.md#L59-L62](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L59-L62) (`clm_a13517dad52e39bc569defd6f5aa600d76d14267fc5b84ecf2546b2a5bd0e256`)
- [observation/documented] Repository development practice: contributors should fork the repo, use focused branches, write clear commits, follow coding standards, add tests where possible, and submit pull requests with issue references; a Code of Conduct applies. -- evidence: [README.md#L214-L215](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L214-L215), [CODE_OF_CONDUCT.md#L5-L5](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/CODE_OF_CONDUCT.md#L5-L5), [README.md#L207-L212](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L207-L212) (`clm_7ba2adb96f61fb7cf8744c971ba705f133acf5c0254dccf1a4447316d227636d`)
- [observation/documented] Repository development practice: bug reports should first check the issue tracker and include a clear description, reproduction steps, expected vs actual behavior, and error messages or screenshots. -- evidence: [README.md#L191-L196](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L191-L196) (`clm_779c6aef89e4af80ab10eb87f0d8be4673588916e7f3dadd1823056de371d1fa`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (1 claim(s))

- [observation/documented] After installation, the MQL dashboard is accessible at http://localhost:3000. -- evidence: [README.md#L155-L158](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L155-L158), [README.md#L44-L44](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L44-L44) (`clm_de4a278456a1e93b4dfdeb161c0e66d14ff664cf0499769f197d2f4f461f9b35`)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] Testing with 50 natural language queries against an elearning schema yielded roughly 85% success (43/50 translated), with about 74% (37/50) executing perfectly and 7 queries erroring. -- evidence: [README.md#L162-L164](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L162-L164) (`clm_e17c860981023edb7c8789ba60bf174a1f1249e0c35cbfb319b9bd3230e0959c`)

## dependencies (1 claim(s))

- [observation/documented] The tool depends on an OpenAI API key, which must be set via OPENAI_API_KEY in the server Dockerfile or server/.env. -- evidence: [README.md#L146-L147](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L146-L147), [README.md#L30-L33](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L30-L33) (`clm_21e477033f9280e1107785b19a8869821ec5b87e9d95d508bc4e4e44523ccc2e`)

## limitations (2 claim(s))

- [observation/documented] As of the current version, MQL is designed to work exclusively with PostgreSQL; MySQL support is only listed as a planned future feature. -- evidence: [README.md#L80-L80](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L80-L80), [README.md#L169-L175](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L169-L175) (`clm_421bf9c7b72b7f2a349bd4521ca4a1228d0db60523dcabb36c3c3e0ea50808d6`)
- [observation/documented] Query execution is not yet implemented; it is listed among planned next-release features, along with natural language responses, data visualization, and Slack integration. -- evidence: [README.md#L169-L175](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L169-L175) (`clm_e34f9d4af10f8cf534983fdaa85cd81b7d678e275929f8efe1f40da31a41dbe4`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

