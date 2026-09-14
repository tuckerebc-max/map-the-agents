# shurutech/mql

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit fabf1ebc0123 @ b7f23b7c537a4ed0

## Summary (orientation draft, not independently verified)

MQL (My Query Language) transforms natural language queries into executable SQL, intended for users without coding knowledge, using a connected or uploaded database schema. The tool depends on an OpenAI API key, which must be set via OPENAI_API_KEY in the server Dockerfile or server/.env.

## Source coverage

Source coverage (complete): 2 of 2 candidate file(s) selected; repository tree complete. Claims by basis: 11 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

11 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications (1 claim(s)):
  - [observation/documented] MQL (My Query Language) transforms natural language queries into executable SQL, intended for users without coding knowledge, using a connected or uploaded database schema. -- evidence: [README.md#L3-L3](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L3-L3)
- components (1 claim(s)):
  - [observation/documented] A default login user (admin@example.com / admin) is created when running via Docker; production guidance says to delete it and create users via a scripts/create_user.py script inside the backend container. -- evidence: [README.md#L70-L76](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L70-L76), [README.md#L65-L67](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L65-L67)
- design-choices (1 claim(s)):
  - [inference/documented] The use of the pgvector extension and a vector database setup suggests MQL likely uses embeddings for schema or query matching, though the README does not state this mechanism explicitly. -- evidence: [README.md#L98-L98](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L98-L98), [README.md#L132-L135](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L132-L135), [README.md#L124-L124](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L124-L124)
- workflows (3 claim(s)):
  - [observation/documented] Repository development practice: local Docker setup requires cloning the repo, setting OPENAI_API_KEY and DATABASE_URL, then running make install; make up, make restart, and make down manage containers. -- evidence: [README.md#L54-L57](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L54-L57), [README.md#L24-L24](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L24-L24), [README.md#L49-L52](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L49-L52), [README.md#L39-L42](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L39-L42), [README.md#L35-L37](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L35-L37), [README.md#L26-L28](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L26-L28), [README.md#L30-L33](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L30-L33), [README.md#L59-L62](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L59-L62)
  - [observation/documented] Repository development practice: contributors should fork the repo, use focused branches, write clear commits, follow coding standards, add tests where possible, and submit pull requests with issue references; a Code of Conduct applies. -- evidence: [README.md#L214-L215](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L214-L215), [CODE_OF_CONDUCT.md#L5-L5](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/CODE_OF_CONDUCT.md#L5-L5), [README.md#L207-L212](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L207-L212)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (1 claim(s)):
  - [observation/documented] After installation, the MQL dashboard is accessible at http://localhost:3000. -- evidence: [README.md#L155-L158](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L155-L158), [README.md#L44-L44](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L44-L44)
- memory-state: unknown (no source-linked claim submitted for this facet)
- orchestration: unknown (no source-linked claim submitted for this facet)
- tools-permissions: unknown (no source-linked claim submitted for this facet)
- evaluation (1 claim(s)):
  - [observation/documented] Testing with 50 natural language queries against an elearning schema yielded roughly 85% success (43/50 translated), with about 74% (37/50) executing perfectly and 7 queries erroring. -- evidence: [README.md#L162-L164](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L162-L164)
- dependencies (1 claim(s)):
  - [observation/documented] The tool depends on an OpenAI API key, which must be set via OPENAI_API_KEY in the server Dockerfile or server/.env. -- evidence: [README.md#L146-L147](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L146-L147), [README.md#L30-L33](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L30-L33)
- limitations (2 claim(s)):
  - [observation/documented] As of the current version, MQL is designed to work exclusively with PostgreSQL; MySQL support is only listed as a planned future feature. -- evidence: [README.md#L80-L80](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L80-L80), [README.md#L169-L175](https://github.com/shurutech/mql/blob/fabf1ebc012355eab7ce536e049bee24297030f0/README.md#L169-L175)
More evidence: [full detail](mql.detail.md)

Metadata and full claim list: [full detail](mql.detail.md)
Human notes ([notes](mql.notes.md), never overwritten by build)

[Back to map index](../../index.md)
