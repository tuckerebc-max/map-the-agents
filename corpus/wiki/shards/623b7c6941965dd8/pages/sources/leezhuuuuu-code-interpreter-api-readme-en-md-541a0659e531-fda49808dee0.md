---
access: public
aliases: []
claim_ids:
- clm_010468d48528f26d0d473a3cb159428c4b9bade2e7edceaebe3857d0010245cc
- clm_08e95a887670efc556cc12a73d40ff84ac0692dacd8681af5991717858c6635a
- clm_4075cc6e37cf993d8a5a18ed866038bd7353fef5d2b36905999a35f11d3b5974
- clm_44682189eeed7fb9278fe01a7901203ac6043d490c20df8b3cb94b88b1e824a9
- clm_a1f13ff28c63de18617fff9ef454c79bfd4354bcc98e4df15f71b85b9898e9e0
- clm_b2e2c3080375ea81fdae1413873c45bf3396c3d3b688b98373e1af8bf135a8b0
- clm_d8855ec370146463c3ba50a580a034e4d9d8bcf575da4549a466bbdd2c89b96f
- clm_dfb38de7c2093c1198f09923925d19b94f4c896e3c696dfaa74b80b24d889581
- clm_f21010e3529fb934ff848a5ea624eecf9db89c7c119b6c2bbaca8e84213c29fa
- clm_ff24b5ea159c1dee8b1234dda70eb134bc1d7723859c2b66c714091e07e5ee1a
maturity: draft
page_id: pg_f2e87c0f4c0e5d999aa2fda49808dee0
page_type: source
review_state: mechanically_checked
schema_version: '1.0'
source_ids:
- src_4bb7a0680682566eb6266ba3310c0f7b
title: leezhuuuuu/Code-Interpreter-Api/README_EN.md @ 541a0659e531
updated_at: '2026-09-14T04:05:44Z'
---

# leezhuuuuu/Code-Interpreter-Api/README_EN.md @ 541a0659e531

<!-- rcw:begin owner=source:src_4bb7a0680682566eb6266ba3310c0f7b block=evidence -->
- Per the documentation, code execution currently supports only Python as the language type. [@claim:clm_010468d48528f26d0d473a3cb159428c4b9bade2e7edceaebe3857d0010245cc]
- Images generated during code execution are converted to Base64 and stored in PostgreSQL, with connection details configured in config.yaml and served via API endpoints. [@claim:clm_08e95a887670efc556cc12a73d40ff84ac0692dacd8681af5991717858c6635a]
- Repository development practice: a concurrency test script concurrent_test.py can be run with python3 to verify concurrent functionality. [@claim:clm_4075cc6e37cf993d8a5a18ed866038bd7353fef5d2b36905999a35f11d3b5974]
- The API exposes a /runcode endpoint accepting POST or GET requests with languageType, optional variables, and code fields, currently supporting only Python. [@claim:clm_44682189eeed7fb9278fe01a7901203ac6043d490c20df8b3cb94b88b1e824a9]
- Concurrency is handled with threads and a semaphore that controls the number of concurrent requests. [@claim:clm_a1f13ff28c63de18617fff9ef454c79bfd4354bcc98e4df15f71b85b9898e9e0]
- Each code execution request runs in its own Docker container for security and resource isolation, with configurable memory and CPU limits and port ranges. [@claim:clm_b2e2c3080375ea81fdae1413873c45bf3396c3d3b688b98373e1af8bf135a8b0]
- The backend is a Flask (Python) application using PostgreSQL with SQLAlchemy as ORM, started via python3 center.py on a configured scheduling-center port. [@claim:clm_d8855ec370146463c3ba50a580a034e4d9d8bcf575da4549a466bbdd2c89b96f]
- A GET /image/<filename> endpoint retrieves image data stored in the database, and /runcode responses can include an images map of URLs plus captured output. [@claim:clm_dfb38de7c2093c1198f09923925d19b94f4c896e3c696dfaa74b80b24d889581]
- The API returns HTTP status codes for error scenarios: 400 for invalid JSON/parameters, 401 for missing or invalid token, 405 for invalid methods, and 504 for timeouts. [@claim:clm_f21010e3529fb934ff848a5ea624eecf9db89c7c119b6c2bbaca8e84213c29fa]
- Access can be secured with optional Bearer token authentication; missing or invalid tokens yield a 401 response. [@claim:clm_ff24b5ea159c1dee8b1234dda70eb134bc1d7723859c2b66c714091e07e5ee1a]
<!-- rcw:end owner=source:src_4bb7a0680682566eb6266ba3310c0f7b block=evidence -->

## Researcher notes

