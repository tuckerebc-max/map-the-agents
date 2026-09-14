# ppipada/agent-repoguardian -- full detail

[Back to orientation](agent-repoguardian.md)

## Origins

- github-verified-rename
- alltheagents.org-backing

## Projects

- Observatory

Full evidence record (JSON): [wiki/dossiers/ppipada/agent-repoguardian/d4c3972590727560ed91aed8b73462f83375f04f/4bfd542db638737c.json](../../../wiki/dossiers/ppipada/agent-repoguardian/d4c3972590727560ed91aed8b73462f83375f04f/4bfd542db638737c.json)

## specifications (1 claim(s))

- [observation/documented] The project is described as an AI agent that performs security scans and vulnerability analysis of code. -- evidence: [README.md#L3-L3](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/README.md#L3-L3) (`clm_2dea46e0bb4b006c246f8147c52cb16cec94a1953307005d5c40e910fc866339`)

## components (3 claim(s))

- [observation/documented] A completed todo item records an eval processor that takes a view JSON as input, converts eval items into scan-specific items, and runs them across multiple eval items. -- evidence: [todo.md#L15-L25](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L15-L25) (`clm_ad78299240d3b41bc7d447f7abb3cafbcbf0b692b926a7a75f996ded47ef1a19`)
- [observation/documented] A code scanner component takes a scan item as input and performs an LLM-based scan, with OpenAI and Anthropic provider capability and batching marked as done. -- evidence: [todo.md#L15-L25](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L15-L25) (`clm_32904783195847554eea3af0bdce96cfcef4cdf6259f1e3d763eb76c300f1c24`)
- [observation/documented] The pipeline includes an LLM categorization step that assigns code to broad functional areas mapped to CWE vulnerability buckets, with unique CWE categories labeled. -- evidence: [todo.md#L15-L25](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L15-L25), [todo.md#L31-L37](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L31-L37) (`clm_427d60857dea3563f3a955f520ce8cd0ad678dba27169295a1f08123fb162e53`)

## design-choices (1 claim(s))

- [observation/documented] The detection prompt is designed to work in a chain-of-thought manner to detect, verify, and score issues. -- evidence: [todo.md#L31-L37](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L31-L37) (`clm_767123d6e0e486100e5a43431fb753f4a0c062d86455a5e551cad3dc41da1fee`)

## workflows (1 claim(s))

- [inference/documented] The todo suggests an earlier 'solver' scaffolding for orchestration, prompts, and results was planned for evaluation with the OpenAI eval framework, though these items are struck through and unchecked. -- evidence: [todo.md#L3-L3](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L3-L3), [todo.md#L5-L8](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L5-L8) (`clm_e366f805ded7cb5d716e63316d2187da09a8c584a0b42e7846581307f4bb3d1b`)

## skills-patterns (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## interfaces (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## memory-state (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## orchestration (1 claim(s))

- [observation/documented] Completed pipeline items cover multiple eval types (simple query, batching with code-item segregation, tagged plus query, categorization) and running evals across multiple eval sets. -- evidence: [todo.md#L39-L39](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L39-L39), [todo.md#L29-L29](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L29-L29), [todo.md#L31-L37](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L31-L37) (`clm_db05f9ab590d2a02a6b0f4b65bfa5374a130fea799336797bd7a19d00cbf4cd4`)

## tools-permissions (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## evaluation (1 claim(s))

- [observation/documented] The todo records metric collection from eval runs including token metrics, while accuracy metrics and an eval report script remain unchecked. -- evidence: [todo.md#L15-L25](https://github.com/ppipada/agent-repoguardian/blob/d4c3972590727560ed91aed8b73462f83375f04f/todo.md#L15-L25) (`clm_a8df54aa49f5fc4ab443aebda1fa028ee6fe31206680a9181a9062f97d80b4a2`)

## dependencies (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## limitations (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

## relevance (0 claim(s))

- unknown (no source-linked claim submitted for this facet)

