# leezhuuuuu/code-interpreter-api

Status: distilled - Freshness: current
Catalog classes: none recorded
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 541a0659e531 @ ad6a7cc4828a4cb0

## Summary (orientation draft, not independently verified)

The API exposes a /runcode endpoint accepting POST or GET requests with languageType, optional variables, and code fields, currently supporting only Python. A GET /image/<filename> endpoint retrieves image data stored in the database, and /runcode responses can include an images map of URLs plus captured output.

## Source coverage

Source coverage (complete): 3 of 3 candidate file(s) selected; repository tree complete. Claims by basis: 10 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

10 claim(s) across 8 facet(s); 5 facet(s) unknown.

- specifications: unknown (no source-linked claim submitted for this facet)
- components (1 claim(s)):
  - [observation/documented] The backend is a Flask (Python) application using PostgreSQL with SQLAlchemy as ORM, started via python3 center.py on a configured scheduling-center port. -- evidence: [README.md#L97-L99](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L97-L99), [README_EN.md#L21-L28](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L21-L28), [README_EN.md#L100-L100](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L100-L100), [README_EN.md#L96-L98](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L96-L98), [README.md#L101-L101](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L101-L101), [README.md#L22-L29](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L22-L29)
- design-choices (1 claim(s)):
  - [observation/documented] Each code execution request runs in its own Docker container for security and resource isolation, with configurable memory and CPU limits and port ranges. -- evidence: [README_EN.md#L32-L38](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L32-L38), [README.md#L33-L39](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L33-L39), [README_EN.md#L65-L70](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L65-L70), [README.md#L66-L71](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L66-L71)
- workflows (1 claim(s)):
  - [observation/documented] Repository development practice: a concurrency test script concurrent_test.py can be run with python3 to verify concurrent functionality. -- evidence: [README_EN.md#L207-L209](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L207-L209), [README.md#L207-L207](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L207-L207), [README.md#L209-L211](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L209-L211), [README_EN.md#L205-L205](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L205-L205)
- skills-patterns: unknown (no source-linked claim submitted for this facet)
- interfaces (3 claim(s)):
  - [observation/documented] The API exposes a /runcode endpoint accepting POST or GET requests with languageType, optional variables, and code fields, currently supporting only Python. -- evidence: [README.md#L109-L111](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L109-L111), [README_EN.md#L106-L106](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L106-L106), [README_EN.md#L108-L110](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L108-L110), [README.md#L107-L107](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L107-L107)
  - [observation/documented] A GET /image/<filename> endpoint retrieves image data stored in the database, and /runcode responses can include an images map of URLs plus captured output. -- evidence: [README.md#L115-L115](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L115-L115), [README_EN.md#L114-L114](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L114-L114), [README.md#L171-L179](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L171-L179), [README_EN.md#L170-L178](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L170-L178)
- memory-state (1 claim(s)):
  - [observation/documented] Images generated during code execution are converted to Base64 and stored in PostgreSQL, with connection details configured in config.yaml and served via API endpoints. -- evidence: [README.md#L197-L197](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L197-L197), [README_EN.md#L32-L38](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L32-L38), [README.md#L33-L39](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L33-L39), [README_EN.md#L195-L195](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L195-L195)
- orchestration (1 claim(s)):
  - [observation/documented] Concurrency is handled with threads and a semaphore that controls the number of concurrent requests. -- evidence: [README_EN.md#L199-L199](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L199-L199), [README.md#L201-L201](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L201-L201)
- tools-permissions (1 claim(s)):
  - [observation/documented] Access can be secured with optional Bearer token authentication; missing or invalid tokens yield a 401 response. -- evidence: [README_EN.md#L184-L187](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L184-L187), [README_EN.md#L32-L38](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L32-L38), [README.md#L33-L39](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L33-L39), [README.md#L186-L189](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L186-L189)
- evaluation: unknown (no source-linked claim submitted for this facet)
- dependencies: unknown (no source-linked claim submitted for this facet)
- limitations (1 claim(s)):
  - [observation/documented] Per the documentation, code execution currently supports only Python as the language type. -- evidence: [README.md#L109-L111](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L109-L111), [README_EN.md#L32-L38](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L32-L38), [README_EN.md#L108-L110](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L108-L110), [README.md#L33-L39](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L33-L39)
- relevance: unknown (no source-linked claim submitted for this facet)

(1 additional claim(s) omitted for length; see [full detail](code-interpreter-api.detail.md) for every claim.)

Metadata and full claim list: [full detail](code-interpreter-api.detail.md)
Human notes ([notes](code-interpreter-api.notes.md), never overwritten by build)

[Back to map index](../../index.md)
