# TODO

- [ ] ~~Write a Solver function that solves the problem~~

- [ ] ~~A solver is all the scaffolding to evaluate, i.e orchestration + prompts + results etc.~~
- [ ] ~~This would be useful when writing the full agent too.~~
- [ ] ~~Fix the input and output format of the solver~~
- [ ] ~~Use OpenAI eval fw to evaluate the solver~~

  - [ ] ~~Metrics need to be defined~~
  - [ ] ~~Initially just accuracy is the focus~~

## Evals dataset orchestration

- [x] Write eval processor that can take the view json as input
  - [x] convert eval item to a scan specific item
  - [x] run it for multiple eval items
- [x] Write a code scanner that can take a scan item as input and perform llm scan using it
- [x] Add OpenAI and Anthropic capability
- [x] Add batching
- [x] Add metric collection capability from eval run
  - [x] Token metrics
  - [ ] ~~Accuracy metrics~~
  - [ ] ~~Script to generate a report of a eval~~
- [x] Get CWE categories that are unique and add labels accordingly

## Processing pipelines

- [x] Create a process pipeline for each eval type

  - [x] Simple query
  - [x] Batching and code items segregation
  - [x] tagged + query
  - [x] Categorization
    - [x] Create broad functional areas and associated cwe issues to use in categorization
    - [x] AI call: Categorize code into these "possible" vulnerability buckets using a llm. Pure categorization task.
  - [x] Prompt should work in chain of thought manner to detect, verify and score issues

- [x] Run eval for multiple eval sets
