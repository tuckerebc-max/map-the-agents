# leezhuuuuu/code-interpreter-api -- full detail

[Back to orientation](code-interpreter-api.md)

## Origins

- alltheagents.org-backing

## Projects


Full evidence record (JSON): [wiki/dossiers/leezhuuuuu/code-interpreter-api/541a0659e5317b4bdc957dd3b3af56411770ad81/ad6a7cc4828a4cb0.json](../../../wiki/dossiers/leezhuuuuu/code-interpreter-api/541a0659e5317b4bdc957dd3b3af56411770ad81/ad6a7cc4828a4cb0.json)

## specifications (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## components (1 claim(s))

- [observation/documented] The backend is a Flask (Python) application using PostgreSQL with SQLAlchemy as ORM, started via python3 center.py on a configured scheduling-center port. -- evidence: [README.md#L97-L99](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L97-L99), [README_EN.md#L21-L28](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L21-L28), [README_EN.md#L100-L100](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L100-L100), [README_EN.md#L96-L98](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L96-L98), [README.md#L101-L101](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L101-L101), [README.md#L22-L29](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L22-L29) (`clm_d8855ec370146463c3ba50a580a034e4d9d8bcf575da4549a466bbdd2c89b96f`)

## design-choices (1 claim(s))

- [observation/documented] Each code execution request runs in its own Docker container for security and resource isolation, with configurable memory and CPU limits and port ranges. -- evidence: [README_EN.md#L32-L38](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L32-L38), [README.md#L33-L39](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L33-L39), [README_EN.md#L65-L70](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L65-L70), [README.md#L66-L71](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L66-L71) (`clm_b2e2c3080375ea81fdae1413873c45bf3396c3d3b688b98373e1af8bf135a8b0`)

## workflows (1 claim(s))

- [observation/documented] Repository development practice: a concurrency test script concurrent_test.py can be run with python3 to verify concurrent functionality. -- evidence: [README_EN.md#L207-L209](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L207-L209), [README.md#L207-L207](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L207-L207), [README.md#L209-L211](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L209-L211), [README_EN.md#L205-L205](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L205-L205) (`clm_4075cc6e37cf993d8a5a18ed866038bd7353fef5d2b36905999a35f11d3b5974`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (3 claim(s))

- [observation/documented] The API exposes a /runcode endpoint accepting POST or GET requests with languageType, optional variables, and code fields, currently supporting only Python. -- evidence: [README.md#L109-L111](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L109-L111), [README_EN.md#L106-L106](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L106-L106), [README_EN.md#L108-L110](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L108-L110), [README.md#L107-L107](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L107-L107) (`clm_44682189eeed7fb9278fe01a7901203ac6043d490c20df8b3cb94b88b1e824a9`)
- [observation/documented] A GET /image/<filename> endpoint retrieves image data stored in the database, and /runcode responses can include an images map of URLs plus captured output. -- evidence: [README.md#L115-L115](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L115-L115), [README_EN.md#L114-L114](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L114-L114), [README.md#L171-L179](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L171-L179), [README_EN.md#L170-L178](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L170-L178) (`clm_dfb38de7c2093c1198f09923925d19b94f4c896e3c696dfaa74b80b24d889581`)
- [observation/documented] The API returns HTTP status codes for error scenarios: 400 for invalid JSON/parameters, 401 for missing or invalid token, 405 for invalid methods, and 504 for timeouts. -- evidence: [README.md#L184-L184](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L184-L184), [README_EN.md#L182-L182](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L182-L182), [README_EN.md#L184-L187](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L184-L187), [README.md#L186-L189](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L186-L189) (`clm_f21010e3529fb934ff848a5ea624eecf9db89c7c119b6c2bbaca8e84213c29fa`)

## memory-state (1 claim(s))

- [observation/documented] Images generated during code execution are converted to Base64 and stored in PostgreSQL, with connection details configured in config.yaml and served via API endpoints. -- evidence: [README.md#L197-L197](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L197-L197), [README_EN.md#L32-L38](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L32-L38), [README.md#L33-L39](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L33-L39), [README_EN.md#L195-L195](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L195-L195) (`clm_08e95a887670efc556cc12a73d40ff84ac0692dacd8681af5991717858c6635a`)

## orchestration (1 claim(s))

- [observation/documented] Concurrency is handled with threads and a semaphore that controls the number of concurrent requests. -- evidence: [README_EN.md#L199-L199](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L199-L199), [README.md#L201-L201](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L201-L201) (`clm_a1f13ff28c63de18617fff9ef454c79bfd4354bcc98e4df15f71b85b9898e9e0`)

## tools-permissions (1 claim(s))

- [observation/documented] Access can be secured with optional Bearer token authentication; missing or invalid tokens yield a 401 response. -- evidence: [README_EN.md#L184-L187](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L184-L187), [README_EN.md#L32-L38](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L32-L38), [README.md#L33-L39](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L33-L39), [README.md#L186-L189](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L186-L189) (`clm_ff24b5ea159c1dee8b1234dda70eb134bc1d7723859c2b66c714091e07e5ee1a`)

## evaluation (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (1 claim(s))

- [observation/documented] Per the documentation, code execution currently supports only Python as the language type. -- evidence: [README.md#L109-L111](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L109-L111), [README_EN.md#L32-L38](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L32-L38), [README_EN.md#L108-L110](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README_EN.md#L108-L110), [README.md#L33-L39](https://github.com/leezhuuuuu/Code-Interpreter-Api/blob/541a0659e5317b4bdc957dd3b3af56411770ad81/README.md#L33-L39) (`clm_010468d48528f26d0d473a3cb159428c4b9bade2e7edceaebe3857d0010245cc`)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

