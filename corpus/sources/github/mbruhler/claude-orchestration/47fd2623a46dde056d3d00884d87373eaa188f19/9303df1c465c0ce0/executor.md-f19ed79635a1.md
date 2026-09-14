# Executor Implementation

Complete guide to the workflow execution engine for orchestration.

## Overview

The executor is responsible for running workflows by managing agent execution, handling parallelism, evaluating conditionals, and coordinating checkpoints.

## Core Responsibilities

1. **Execute workflow graphs** - Run nodes in correct order
2. **Manage agent lifecycle** - Launch and monitor agents
3. **Handle parallel execution** - Run multiple agents simultaneously
4. **Evaluate conditionals** - Route based on conditions
5. **Coordinate checkpoints** - Pause for user input
6. **Track execution state** - Maintain workflow status
7. **Handle errors** - Recover from failures

## Execution State

### State Structure

```javascript
{
  workflow: "original syntax string",
  graph: {
    nodes: [{id, type, agent, instruction, status}],
    edges: [{from, to, condition}]
  },
  execution: {
    current: ['node-1', 'node-2'],      // Currently executing
    completed: ['node-0'],               // Successfully finished
    failed: [],                          // Failed nodes
    skipped: [],                         // Skipped by condition or user
    outputs: {                           // Node outputs
      'node-0': {result: '...', duration: 1234}
    }
  },
  steering: {
    paused: false,                       // At checkpoint?
    position: 'node-1',                  // Current position
    command: null                        // Pending steering command
  },
  startTime: 1234567890,
  metadata: {
    totalNodes: 10,
    parallelBranches: 2,
    checkpoints: 1
  }
}
```

## Execution Algorithm

### Main Loop

```javascript
async function executeWorkflow(graph) {
  // Initialize state
  const state = initializeState(graph)

  // Initial visualization
  visualizer.render(graph)

  // Confirm with user
  const confirmed = await confirmExecution(graph)
  if (!confirmed) return

  // Main execution loop
  while (!isComplete(state)) {
    // Find executable nodes
    const ready = findExecutableNodes(state)

    if (ready.length === 0) {
      if (hasActiveNodes(state)) {
        // Wait for running nodes
        await waitForCompletion(state)
        continue
      } else {
        // Deadlock or complete
        break
      }
    }

    // Execute ready nodes
    await executeNodes(ready, state)

    // Update visualization
    visualizer.update(state.graph)

    // Check for checkpoints
    if (hasActiveCheckpoint(state)) {
      await handleCheckpoint(state)
    }

    // Check for errors
    if (hasErrors(state)) {
      const recovered = await handleErrors(state)
      if (!recovered) break
    }
  }

  // Final results
  displayResults(state)
}
```

### Finding Executable Nodes

```javascript
function findExecutableNodes(state) {
  const ready = []

  for (const node of state.graph.nodes) {
    // Skip if already processed
    if (node.status !== 'pending') continue

    // Check if dependencies are satisfied
    const incoming = state.graph.edges.filter(e => e.to === node.id)

    if (incoming.length === 0) {
      // No dependencies - ready to execute
      ready.push(node)
      continue
    }

    // Check all incoming edges
    const allSatisfied = incoming.every(edge => {
      const sourceNode = state.graph.nodes.find(n => n.id === edge.from)

      // Source must be completed
      if (sourceNode.status !== 'completed') return false

      // If edge has condition, evaluate it
      if (edge.condition) {
        return evaluateCondition(
          edge.condition,
          state.execution.outputs[edge.from]
        )
      }

      return true
    })

    if (allSatisfied) {
      ready.push(node)
    }
  }

  return ready
}
```

## Agent Mapping and Execution

### Agent Type Mapping

```javascript
const AGENT_MAPPING = {
  'explore': 'Explore',
  'general-purpose': 'general-purpose',
  'code-reviewer': 'superpowers:code-reviewer',
  'implementation-architect': 'implementation-architect',
  'expert-code-implementer': 'expert-code-implementer'
}

function getSubagentType(agentName) {
  return AGENT_MAPPING[agentName] || agentName
}
```

### Single Agent Execution

```javascript
async function executeAgent(node, state) {
  // Update status
  node.status = 'executing'
  state.execution.current.push(node.id)
  visualizer.update(state.graph)

  // Build instruction
  const instruction = buildInstruction(node, state)

  // Launch agent via Task tool
  const startTime = Date.now()

  try {
    const result = await Task({
      subagent_type: getSubagentType(node.agent),
      task: instruction
    })

    // Record success
    node.status = 'completed'
    state.execution.current = state.execution.current.filter(id => id !== node.id)
    state.execution.completed.push(node.id)
    state.execution.outputs[node.id] = {
      result: result,
      duration: Date.now() - startTime,
      success: true
    }

  } catch (error) {
    // Record failure
    node.status = 'failed'
    state.execution.current = state.execution.current.filter(id => id !== node.id)
    state.execution.failed.push(node.id)
    state.execution.outputs[node.id] = {
      error: error.message,
      duration: Date.now() - startTime,
      success: false
    }

    throw error
  }

  visualizer.update(state.graph)
}

function buildInstruction(node, state) {
  if (node.instruction) {
    // Explicit instruction
    return node.instruction
  }

  // Infer from context
  const completed = state.execution.completed
    .map(id => state.graph.nodes.find(n => n.id === id))
    .filter(n => n.agent)
    .map(n => n.agent)

  return `Continue workflow after: ${completed.join(', ')}`
}
```

### Parallel Execution

```javascript
async function executeParallel(nodes, state) {
  // Mark all as executing
  for (const node of nodes) {
    node.status = 'executing'
    state.execution.current.push(node.id)
  }
  visualizer.update(state.graph)

  // Launch all agents in parallel using multiple Task calls
  const promises = nodes.map(node => executeAgent(node, state))

  // Wait for all to complete
  const results = await Promise.allSettled(promises)

  // Process results
  for (let i = 0; i < results.length; i++) {
    const result = results[i]
    const node = nodes[i]

    if (result.status === 'fulfilled') {
      // Already handled in executeAgent
    } else {
      // Handle failure
      console.error(`Parallel branch [${node.agent}] failed:`, result.reason)
    }
  }

  visualizer.update(state.graph)

  return results
}
```

### Execute Multiple Nodes

```javascript
async function executeNodes(nodes, state) {
  if (nodes.length === 1) {
    // Single node execution
    await executeAgent(nodes[0], state)
  } else {
    // Parallel execution
    await executeParallel(nodes, state)
  }
}
```

## Conditional Evaluation

### Condition Types

```javascript
const CONDITION_EVALUATORS = {
  'if passed': (output) => output.success === true,
  'if failed': (output) => output.success === false,
  'if all success': (outputs) => outputs.every(o => o.success),
  'if any success': (outputs) => outputs.some(o => o.success),
  'if all failed': (outputs) => outputs.every(o => !o.success),
  'if any failed': (outputs) => outputs.some(o => !o.success)
}
```

### Evaluation Function

```javascript
function evaluateCondition(conditionStr, output) {
  // Remove parentheses
  const condition = conditionStr.replace(/^\(|\)$/g, '').trim()

  // Check built-in conditions
  if (CONDITION_EVALUATORS[condition]) {
    return CONDITION_EVALUATORS[condition](output)
  }

  // Custom condition - search output for keywords
  return evaluateCustomCondition(condition, output)
}

function evaluateCustomCondition(condition, output) {
  // Extract condition type and value
  // Examples:
  //   "if contains error" -> check if output contains "error"
  //   "if count > 5" -> parse and evaluate expression
  //   "if status === success" -> check output.status

  const outputStr = JSON.stringify(output).toLowerCase()
  const conditionLower = condition.toLowerCase()

  // Simple keyword matching
  if (conditionLower.startsWith('if contains ')) {
    const keyword = conditionLower.slice('if contains '.length)
    return outputStr.includes(keyword)
  }

  if (conditionLower.startsWith('if not contains ')) {
    const keyword = conditionLower.slice('if not contains '.length)
    return !outputStr.includes(keyword)
  }

  // Default: check for success indicators
  return output.success === true
}
```

### Conditional Flow Example

```javascript
// Workflow: test (if failed)~> fix -> test

// After test fails:
const testOutput = state.execution.outputs['test-node']
const condition = '(if failed)'
const shouldExecuteFix = evaluateCondition(condition, testOutput)

if (shouldExecuteFix) {
  // Execute fix node
  await executeAgent(fixNode, state)
}
```

## Checkpoint Handling

### Checkpoint Detection

```javascript
function hasActiveCheckpoint(state) {
  return state.graph.nodes.some(node =>
    node.type === 'checkpoint' &&
    node.status === 'executing'
  )
}

function getActiveCheckpoint(state) {
  return state.graph.nodes.find(node =>
    node.type === 'checkpoint' &&
    node.status === 'executing'
  )
}
```

### Checkpoint Execution

```javascript
async function handleCheckpoint(state) {
  const checkpoint = getActiveCheckpoint(state)

  // Pause execution
  state.steering.paused = true
  state.steering.position = checkpoint.id

  // Show checkpoint display
  visualizer.showCheckpoint(checkpoint)

  // Wait for user command
  const command = await getSteeringCommand(checkpoint)

  // Process command (see steering.md)
  await processSteeringCommand(command, state)

  // Resume execution
  checkpoint.status = 'completed'
  state.steering.paused = false
  state.execution.completed.push(checkpoint.id)

  visualizer.update(state.graph)
}
```

## Parallel Branch Management

### Parallel Entry Point

```javascript
async function executeParallelEntry(node, state) {
  // Find all outgoing branches
  const branches = state.graph.edges.filter(e => e.from === node.id)

  // Mark as executing
  node.status = 'executing'

  // Find branch nodes
  const branchNodes = branches.map(edge =>
    state.graph.nodes.find(n => n.id === edge.to)
  )

  // Execute all branches in parallel
  await executeParallel(branchNodes, state)

  // Mark entry as completed
  node.status = 'completed'
  state.execution.completed.push(node.id)
}
```

### Parallel Merge Point

```javascript
function isReadyToMerge(mergeNode, state) {
  // Find all incoming branches
  const incoming = state.graph.edges.filter(e => e.to === mergeNode.id)

  // Check if all branches are complete
  return incoming.every(edge => {
    const sourceNode = state.graph.nodes.find(n => n.id === edge.from)
    return sourceNode.status === 'completed' ||
           sourceNode.status === 'skipped'
  })
}

async function executeMerge(node, state) {
  // Collect outputs from all branches
  const incoming = state.graph.edges.filter(e => e.to === node.id)
  const branchOutputs = incoming.map(edge =>
    state.execution.outputs[edge.from]
  )

  // Merge logic (can be customized)
  const mergedOutput = mergeBranchOutputs(branchOutputs)

  // Store merged result
  node.status = 'completed'
  state.execution.completed.push(node.id)
  state.execution.outputs[node.id] = mergedOutput

  visualizer.update(state.graph)
}

function mergeBranchOutputs(outputs) {
  // Default merge: collect all results
  return {
    success: outputs.every(o => o.success),
    results: outputs.map(o => o.result),
    duration: Math.max(...outputs.map(o => o.duration))
  }
}
```

## Error Handling

### Error Detection

```javascript
function hasErrors(state) {
  return state.execution.failed.length > 0
}

function getFailedNodes(state) {
  return state.execution.failed.map(id =>
    state.graph.nodes.find(n => n.id === id)
  )
}
```

### Error Recovery

```javascript
async function handleErrors(state) {
  const failedNodes = getFailedNodes(state)

  for (const node of failedNodes) {
    // Show error
    const error = state.execution.outputs[node.id].error
    visualizer.showError(node, {message: error})

    // Get recovery action
    const action = await getRecoveryAction(node, error)

    // Process recovery
    const recovered = await processRecovery(action, node, state)

    if (!recovered) {
      return false
    }
  }

  return true
}

async function processRecovery(action, node, state) {
  switch (action) {
    case 'retry':
      // Reset node status and retry
      node.status = 'pending'
      state.execution.failed = state.execution.failed.filter(id => id !== node.id)
      await executeAgent(node, state)
      return true

    case 'skip':
      // Mark as skipped
      node.status = 'skipped'
      state.execution.failed = state.execution.failed.filter(id => id !== node.id)
      state.execution.skipped.push(node.id)
      return true

    case 'edit':
      // Re-parse workflow (see steering.md)
      return await editAndReparse(state)

    case 'quit':
      return false

    default:
      return false
  }
}
```

## State Transitions

### Node Status Lifecycle

```
pending -> executing -> completed
                     -> failed -> (retry) -> pending
                              -> (skip) -> skipped
```

### State Diagram

```javascript
const STATE_MACHINE = {
  pending: {
    canTransitionTo: ['executing'],
    action: 'Start execution'
  },
  executing: {
    canTransitionTo: ['completed', 'failed'],
    action: 'Wait for result'
  },
  completed: {
    canTransitionTo: [],
    action: 'Done'
  },
  failed: {
    canTransitionTo: ['pending', 'skipped'],
    action: 'Recover'
  },
  skipped: {
    canTransitionTo: [],
    action: 'Bypassed'
  }
}

function canTransition(node, newStatus) {
  const current = STATE_MACHINE[node.status]
  return current.canTransitionTo.includes(newStatus)
}
```

## Execution Context

### Context Passing

```javascript
function buildExecutionContext(node, state) {
  // Gather outputs from dependencies
  const incoming = state.graph.edges.filter(e => e.to === node.id)
  const dependencies = incoming.map(edge => ({
    node: state.graph.nodes.find(n => n.id === edge.from),
    output: state.execution.outputs[edge.from]
  }))

  return {
    node: node,
    dependencies: dependencies,
    workflowState: {
      completed: state.execution.completed.length,
      total: state.graph.nodes.length,
      parallel: isParallelContext(node, state)
    }
  }
}

function isParallelContext(node, state) {
  // Check if node is part of parallel branch
  const incoming = state.graph.edges.filter(e => e.to === node.id)
  return incoming.some(edge => {
    const source = state.graph.nodes.find(n => n.id === edge.from)
    return source.type === 'parallel-entry'
  })
}
```

## Performance Optimization

### Parallel Execution Limits

```javascript
const MAX_PARALLEL_AGENTS = 5

async function executeParallelBatched(nodes, state) {
  const batches = []

  // Split into batches
  for (let i = 0; i < nodes.length; i += MAX_PARALLEL_AGENTS) {
    batches.push(nodes.slice(i, i + MAX_PARALLEL_AGENTS))
  }

  // Execute batches sequentially
  for (const batch of batches) {
    await executeParallel(batch, state)
  }
}
```

### Execution Timeout

```javascript
async function executeWithTimeout(node, state, timeoutMs = 300000) {
  return Promise.race([
    executeAgent(node, state),
    new Promise((_, reject) =>
      setTimeout(() => reject(new Error('Execution timeout')), timeoutMs)
    )
  ])
}
```

### State Snapshots

```javascript
function createSnapshot(state) {
  return JSON.parse(JSON.stringify(state))
}

function restoreSnapshot(state, snapshot) {
  Object.assign(state, snapshot)
  visualizer.update(state.graph)
}
```

## Completion Detection

### Is Workflow Complete?

```javascript
function isComplete(state) {
  // All nodes must be in terminal state
  return state.graph.nodes.every(node =>
    ['completed', 'failed', 'skipped'].includes(node.status)
  )
}

function isSuccessful(state) {
  // No failed nodes
  return state.execution.failed.length === 0 &&
         state.execution.completed.length > 0
}
```

### Final Results

```javascript
function displayResults(state) {
  const duration = Date.now() - state.startTime

  visualizer.showCompletion(state.graph, duration)

  // Offer next actions
  const action = await getUserAction([
    'view-results',
    'save-template',
    'run-again',
    'return-to-menu'
  ])

  await processCompletionAction(action, state)
}
```

## Execution Hooks

### Lifecycle Hooks

```javascript
const HOOKS = {
  beforeExecution: [],
  beforeNode: [],
  afterNode: [],
  onError: [],
  afterExecution: []
}

function registerHook(hookName, callback) {
  if (HOOKS[hookName]) {
    HOOKS[hookName].push(callback)
  }
}

async function triggerHook(hookName, ...args) {
  for (const callback of HOOKS[hookName]) {
    await callback(...args)
  }
}

// Usage:
await triggerHook('beforeNode', node, state)
await executeAgent(node, state)
await triggerHook('afterNode', node, state)
```

### Custom Hooks Example

```javascript
registerHook('beforeNode', async (node, state) => {
  console.log(`Starting ${node.agent}...`)
})

registerHook('afterNode', async (node, state) => {
  const output = state.execution.outputs[node.id]
  console.log(`Completed ${node.agent} in ${output.duration}ms`)
})

registerHook('onError', async (node, error, state) => {
  console.error(`Failed ${node.agent}:`, error)
  // Could send notification, log to file, etc.
})
```

## Testing

### Execution Tests

```javascript
describe('Executor', () => {
  test('executes simple sequence', async () => {
    const graph = createSequenceGraph(['explore', 'implement'])
    const state = await executeWorkflow(graph)

    expect(state.execution.completed).toHaveLength(2)
    expect(state.execution.failed).toHaveLength(0)
  })

  test('executes parallel branches', async () => {
    const graph = createParallelGraph(['test', 'lint'])
    const state = await executeWorkflow(graph)

    expect(state.execution.completed).toHaveLength(2)
    // Both should execute simultaneously
    const durations = Object.values(state.execution.outputs)
      .map(o => o.duration)
    expect(Math.max(...durations)).toBeLessThan(
      durations.reduce((a, b) => a + b)
    )
  })

  test('evaluates conditionals', async () => {
    const graph = createConditionalGraph()
    const state = await executeWorkflow(graph)

    // Fix should only execute if test failed
    const testFailed = !state.execution.outputs['test'].success
    const fixExecuted = state.execution.completed.includes('fix')
    expect(fixExecuted).toBe(testFailed)
  })

  test('handles checkpoints', async () => {
    const graph = createGraphWithCheckpoint()
    const state = await executeWorkflow(graph)

    // Should pause at checkpoint
    expect(state.steering.paused).toBe(true)
  })
})
```

## Best Practices

1. **Execute in order** - Respect dependencies
2. **Parallelize safely** - Limit concurrent agents
3. **Update frequently** - Keep visualization current
4. **Handle errors gracefully** - Provide recovery options
5. **Track state carefully** - Maintain accurate execution state
6. **Timeout long operations** - Prevent hanging workflows
7. **Snapshot for recovery** - Allow rollback on errors
8. **Test thoroughly** - Cover all execution paths

## See Also

- [parser.md](parser.md) - Graph creation
- [visualizer.md](visualizer.md) - Execution visualization
- [steering.md](steering.md) - User control during execution
- [../features/error-handling.md](../features/error-handling.md) - Error recovery strategies
