---
access: public
aliases: []
claim_ids:
- clm_17e197f4fe12cc5875051e30de10e2fa609456dae2e4b1ef16da10dc2d5d164f
- clm_21e477033f9280e1107785b19a8869821ec5b87e9d95d508bc4e4e44523ccc2e
- clm_421bf9c7b72b7f2a349bd4521ca4a1228d0db60523dcabb36c3c3e0ea50808d6
- clm_779c6aef89e4af80ab10eb87f0d8be4673588916e7f3dadd1823056de371d1fa
- clm_7ba2adb96f61fb7cf8744c971ba705f133acf5c0254dccf1a4447316d227636d
- clm_7c6b217f580737390807d1170302d58cd3573e1319f359b9baaa86e9e953579f
- clm_a13517dad52e39bc569defd6f5aa600d76d14267fc5b84ecf2546b2a5bd0e256
- clm_b6306cd3b7f916fa7a445e2a9753641a5473ec0bd63c1d3ea9d7c76261cca850
- clm_de4a278456a1e93b4dfdeb161c0e66d14ff664cf0499769f197d2f4f461f9b35
- clm_e17c860981023edb7c8789ba60bf174a1f1249e0c35cbfb319b9bd3230e0959c
- clm_e34f9d4af10f8cf534983fdaa85cd81b7d678e275929f8efe1f40da31a41dbe4
maturity: draft
page_id: pg_3f568e7ea66e563bb2d21f6ea4c64edc
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_b491d849cd665d07b8f31d0aea8fc57f
title: shurutech/mql/README.md @ fabf1ebc0123
updated_at: '2026-09-14T04:21:52Z'
---

# shurutech/mql/README.md @ fabf1ebc0123

<!-- rcw:begin owner=source:src_b491d849cd665d07b8f31d0aea8fc57f block=evidence -->
- MQL (My Query Language) transforms natural language queries into executable SQL, intended for users without coding knowledge, using a connected or uploaded database schema. [@claim:clm_17e197f4fe12cc5875051e30de10e2fa609456dae2e4b1ef16da10dc2d5d164f]
- The tool depends on an OpenAI API key, which must be set via OPENAI_API_KEY in the server Dockerfile or server/.env. [@claim:clm_21e477033f9280e1107785b19a8869821ec5b87e9d95d508bc4e4e44523ccc2e]
- As of the current version, MQL is designed to work exclusively with PostgreSQL; MySQL support is only listed as a planned future feature. [@claim:clm_421bf9c7b72b7f2a349bd4521ca4a1228d0db60523dcabb36c3c3e0ea50808d6]
- Repository development practice: bug reports should first check the issue tracker and include a clear description, reproduction steps, expected vs actual behavior, and error messages or screenshots. [@claim:clm_779c6aef89e4af80ab10eb87f0d8be4673588916e7f3dadd1823056de371d1fa]
- Repository development practice: contributors should fork the repo, use focused branches, write clear commits, follow coding standards, add tests where possible, and submit pull requests with issue references; a Code of Conduct applies. [@claim:clm_7ba2adb96f61fb7cf8744c971ba705f133acf5c0254dccf1a4447316d227636d]
- The use of the pgvector extension and a vector database setup suggests MQL likely uses embeddings for schema or query matching, though the README does not state this mechanism explicitly. [@claim:clm_7c6b217f580737390807d1170302d58cd3573e1319f359b9baaa86e9e953579f]
- Repository development practice: local Docker setup requires cloning the repo, setting OPENAI_API_KEY and DATABASE_URL, then running make install; make up, make restart, and make down manage containers. [@claim:clm_a13517dad52e39bc569defd6f5aa600d76d14267fc5b84ecf2546b2a5bd0e256]
- A default login user (admin@example.com / admin) is created when running via Docker; production guidance says to delete it and create users via a scripts/create_user.py script inside the backend container. [@claim:clm_b6306cd3b7f916fa7a445e2a9753641a5473ec0bd63c1d3ea9d7c76261cca850]
- After installation, the MQL dashboard is accessible at http://localhost:3000. [@claim:clm_de4a278456a1e93b4dfdeb161c0e66d14ff664cf0499769f197d2f4f461f9b35]
- Testing with 50 natural language queries against an elearning schema yielded roughly 85% success (43/50 translated), with about 74% (37/50) executing perfectly and 7 queries erroring. [@claim:clm_e17c860981023edb7c8789ba60bf174a1f1249e0c35cbfb319b9bd3230e0959c]
- Query execution is not yet implemented; it is listed among planned next-release features, along with natural language responses, data visualization, and Slack integration. [@claim:clm_e34f9d4af10f8cf534983fdaa85cd81b7d678e275929f8efe1f40da31a41dbe4]
<!-- rcw:end owner=source:src_b491d849cd665d07b8f31d0aea8fc57f block=evidence -->

## Researcher notes

