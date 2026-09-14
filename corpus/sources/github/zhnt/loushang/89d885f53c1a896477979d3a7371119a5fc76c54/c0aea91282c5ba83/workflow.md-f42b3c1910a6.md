# `workflow`

## Role

- prompt workflow loader / runner boundary
- testable automation surface for multi-step prompt flows against coding sessions

## Owns

- workflow file loading and validation
- workflow step schema
- workflow runner and fake runtime adapter
- workflow report formatting

## Depends On

- `session` through `AgentSessionWorkflowAdapter`
- `mode` semantics for prompt/follow-up/steer/abort style actions
- filesystem for workflow files

## Commands

- `load_workflow(...)`
- `resolve_workflow_files(...)`
- `run_workflow(...)`
- `run_prompt_steps_workflow(...)`

## Queries

- `find_event(...)`
- `event_matches(...)`
- workflow result/report projections

## Events

- `WorkflowEvent`

## Key Data

- `Workflow`
- `WorkflowStep`
- `PromptStep`
- `WaitForStep`
- `WaitStep`
- `SteerStep`
- `FollowUpStep`
- `AbortStep`
- `ExpectStep`
- `WorkflowExpectation`
- `WorkflowResult`
- `WorkflowStepResult`
- `EventPattern`

## Out Of Scope

- replacing method plans
- session persistence
- provider selection
- TUI method status rendering

## Reference Implementation Alignment

- Provides a deterministic workflow harness around the existing session/runtime boundary.
- Keeps prompt workflows separate from `loushang.method`; method plans are domain assets, while prompt workflows are automation/test harness assets.
