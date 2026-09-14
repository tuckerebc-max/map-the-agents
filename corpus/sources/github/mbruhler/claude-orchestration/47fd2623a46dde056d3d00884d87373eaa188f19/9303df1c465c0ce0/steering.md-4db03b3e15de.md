# Steering Implementation

Complete guide to interactive workflow control and user decision points.

## Overview

Steering provides interactive control over workflow execution through checkpoints, error recovery, and user commands. It allows users to pause, navigate, modify, and inspect workflows during execution.

## Core Responsibilities

1. **Handle checkpoints** - Pause at designated points
2. **Provide control menu** - Show available commands
3. **Process user commands** - Execute navigation and control actions
4. **Manage decision points** - Guide users through choices
5. **Enable workflow editing** - Modify workflows mid-execution
6. **Support navigation** - Jump to specific workflow points

## Checkpoint System

### Checkpoint Types

**Explicit Checkpoints:**
```
explore -> @review -> implement
```

**Automatic Checkpoints:**
- Before executing risky operations
- After errors occur
- At parallel branch merge points
- Before workflow completion

### Checkpoint State

```javascript
{
  id: 'checkpoint-1',
  type: 'checkpoint',
  label: '@review',
  prompt: 'Review findings before implementation',
  status: 'executing',
  timestamp: 1234567890,
  context: {
    completedSteps: ['explore'],
    pendingSteps: ['implement'],
    outputs: {...}
  }
}
```

## Control Menu

### Standard Menu

```javascript
function getStandardMenu() {
  return {
    options: [
      {
        key: 'c',
        label: 'Continue',
        description: 'Resume from current point',
        action: 'continue'
      },
      {
        key: 'e',
        label: 'Edit',
        description: 'Modify workflow syntax',
        action: 'edit'
      },
      {
        key: 'q',
        label: 'Quit',
        description: 'Abort with summary',
        action: 'quit'
      }
    ]
  }
}
```

### Checkpoint Menu

```javascript
function getCheckpointMenu() {
  return {
    options: [
      {
        key: 'c',
        label: 'Continue',
        description: 'Resume from current point',
        action: 'continue'
      },
      {
        key: 'j',
        label: 'Jump',
        description: 'Jump to specific node',
        action: 'jump'
      },
      {
        key: 'r',
        label: 'Repeat',
        description: 'Re-execute last node',
        action: 'repeat'
      },
      {
        key: 'e',
        label: 'Edit',
        description: 'Modify workflow syntax',
        action: 'edit'
      },
      {
        key: 'v',
        label: 'View output',
        description: 'Display full node output',
        action: 'view'
      },
      {
        key: 'q',
        label: 'Quit',
        description: 'Abort with summary',
        action: 'quit'
      }
    ]
  }
}
```

### Error Recovery Menu

```javascript
function getErrorMenu(error) {
  const contextualOptions = getContextualRecoveryOptions(error)

  return {
    options: [
      {
        key: 'r',
        label: 'Retry',
        description: 'Re-execute failed node',
        action: 'retry',
        recommended: error.type === 'timeout'
      },
      {
        key: 'e',
        label: 'Edit',
        description: 'Modify workflow',
        action: 'edit',
        recommended: error.type === 'syntax'
      },
      {
        key: 's',
        label: 'Skip',
        description: 'Continue past failure',
        action: 'skip',
        recommended: false
      },
      {
        key: 'd',
        label: 'Debug',
        description: 'Insert debug step',
        action: 'debug',
        recommended: error.type === 'logic'
      },
      {
        key: 'f',
        label: 'Fork',
        description: 'Try parallel approaches',
        action: 'fork',
        recommended: error.type === 'uncertain'
      },
      {
        key: 'q',
        label: 'Quit',
        description: 'Abort execution',
        action: 'quit',
        recommended: false
      },
      ...contextualOptions
    ]
  }
}
```

## User Input Collection

### Using AskUserQuestion

```javascript
async function getSteeringCommand(checkpoint) {
  const menu = getCheckpointMenu()

  const response = await AskUserQuestion({
    questions: [{
      question: checkpoint.prompt || "What would you like to do?",
      header: "Control",
      multiSelect: false,
      options: menu.options.map(opt => ({
        label: opt.label,
        description: opt.description
      }))
    }]
  })

  // Map response to action
  return mapResponseToAction(response, menu)
}

function mapResponseToAction(response, menu) {
  const selectedLabel = Object.values(response)[0]
  const option = menu.options.find(opt => opt.label === selectedLabel)
  return option ? option.action : 'continue'
}
```

## Command Processing

### Continue Command

```javascript
async function processContinue(state) {
  // Simply resume execution
  state.steering.paused = false
  state.steering.command = null

  // Mark checkpoint as complete
  const checkpoint = getActiveCheckpoint(state)
  if (checkpoint) {
    checkpoint.status = 'completed'
    state.execution.completed.push(checkpoint.id)
  }

  visualizer.update(state.graph)
  return {action: 'continue', success: true}
}
```

### Jump Command

```javascript
async function processJump(state) {
  // Get available jump targets
  const targets = getJumpTargets(state)

  // Ask user to select target
  const response = await AskUserQuestion({
    questions: [{
      question: "Which node would you like to jump to?",
      header: "Jump",
      multiSelect: false,
      options: targets.map(node => ({
        label: node.agent || node.label,
        description: `Status: ${node.status}`
      }))
    }]
  })

  const selectedLabel = Object.values(response)[0]
  const targetNode = targets.find(n =>
    (n.agent || n.label) === selectedLabel
  )

  if (!targetNode) {
    return {action: 'jump', success: false, error: 'Invalid target'}
  }

  // Reset target and subsequent nodes to pending
  resetFromNode(targetNode, state)

  // Move execution position
  state.steering.position = targetNode.id
  state.steering.paused = false

  visualizer.update(state.graph)
  return {action: 'jump', success: true, target: targetNode.id}
}

function getJumpTargets(state) {
  // Can jump to:
  // 1. Any completed node (to re-execute)
  // 2. Any pending node (to skip ahead)
  // 3. Checkpoints
  return state.graph.nodes.filter(node =>
    node.status === 'completed' ||
    node.status === 'pending' ||
    node.type === 'checkpoint'
  )
}

function resetFromNode(node, state) {
  // Reset node and all downstream nodes to pending
  const toReset = new Set([node.id])
  const visited = new Set()

  function visitDownstream(nodeId) {
    if (visited.has(nodeId)) return
    visited.add(nodeId)
    toReset.add(nodeId)

    const outgoing = state.graph.edges.filter(e => e.from === nodeId)
    for (const edge of outgoing) {
      visitDownstream(edge.to)
    }
  }

  visitDownstream(node.id)

  // Reset status
  for (const id of toReset) {
    const n = state.graph.nodes.find(n => n.id === id)
    if (n && n.type !== 'checkpoint') {
      n.status = 'pending'
      // Remove from completed/failed lists
      state.execution.completed = state.execution.completed.filter(cid => cid !== id)
      state.execution.failed = state.execution.failed.filter(fid => fid !== id)
      // Clear output
      delete state.execution.outputs[id]
    }
  }
}
```

### Repeat Command

```javascript
async function processRepeat(state) {
  // Find last executed node
  const lastNodeId = state.execution.completed[state.execution.completed.length - 1]
  const lastNode = state.graph.nodes.find(n => n.id === lastNodeId)

  if (!lastNode) {
    return {action: 'repeat', success: false, error: 'No node to repeat'}
  }

  // Reset node
  lastNode.status = 'pending'
  state.execution.completed = state.execution.completed.filter(id => id !== lastNodeId)
  delete state.execution.outputs[lastNodeId]

  // Re-execute
  state.steering.paused = false
  visualizer.update(state.graph)

  return {action: 'repeat', success: true, node: lastNodeId}
}
```

### Edit Command

```javascript
async function processEdit(state) {
  // Show current workflow
  console.log('Current workflow:')
  console.log(state.workflow)
  console.log('')

  // Ask for new syntax
  const response = await AskUserQuestion({
    questions: [{
      question: "Enter new workflow syntax (or 'cancel' to abort):",
      header: "Edit",
      multiSelect: false,
      options: [
        {label: 'Edit workflow', description: 'Provide new syntax'},
        {label: 'Cancel', description: 'Keep current workflow'}
      ]
    }]
  })

  const action = Object.values(response)[0]

  if (action === 'Cancel') {
    return {action: 'edit', success: false, cancelled: true}
  }

  // For 'Edit workflow', we need to get the actual syntax
  // In practice, this would open an editor or prompt for input
  const newSyntax = await getWorkflowSyntaxFromUser()

  if (!newSyntax || newSyntax === 'cancel') {
    return {action: 'edit', success: false, cancelled: true}
  }

  // Parse new workflow
  try {
    const parsed = parseWorkflow(newSyntax)

    // Validate
    const validation = validateGraph(parsed.graph, parsed.tokens)
    if (!validation.valid) {
      console.error('Validation error:', validation.error)
      return {action: 'edit', success: false, error: validation.error}
    }

    // Update state
    state.workflow = newSyntax
    state.graph = parsed.graph

    // Reset execution state
    state.execution = {
      current: [],
      completed: [],
      failed: [],
      skipped: [],
      outputs: {}
    }

    state.steering.paused = false
    state.steering.position = null

    visualizer.update(state.graph)
    return {action: 'edit', success: true}

  } catch (error) {
    console.error('Parse error:', error)
    return {action: 'edit', success: false, error: error.message}
  }
}
```

### View Command

```javascript
async function processView(state) {
  // Get available nodes with outputs
  const nodesWithOutputs = state.execution.completed
    .concat(state.execution.failed)
    .map(id => state.graph.nodes.find(n => n.id === id))
    .filter(n => n)

  if (nodesWithOutputs.length === 0) {
    console.log('No outputs to view yet.')
    return {action: 'view', success: false, error: 'No outputs'}
  }

  // Ask which node to view
  const response = await AskUserQuestion({
    questions: [{
      question: "Which node's output would you like to view?",
      header: "View",
      multiSelect: false,
      options: nodesWithOutputs.map(node => ({
        label: node.agent || node.label,
        description: `Status: ${node.status}`
      }))
    }]
  })

  const selectedLabel = Object.values(response)[0]
  const selectedNode = nodesWithOutputs.find(n =>
    (n.agent || n.label) === selectedLabel
  )

  if (!selectedNode) {
    return {action: 'view', success: false, error: 'Invalid selection'}
  }

  // Display output
  const output = state.execution.outputs[selectedNode.id]
  displayNodeOutput(selectedNode, output)

  return {action: 'view', success: true, node: selectedNode.id}
}

function displayNodeOutput(node, output) {
  console.log('╔════════════════════════════════════════════╗')
  console.log('║  Output: ' + (node.agent || node.label).padEnd(34) + '║')
  console.log('╠════════════════════════════════════════════╣')
  console.log('║                                            ║')

  if (output.success) {
    console.log('║  Status: Success ✓'.padEnd(44) + '║')
    console.log('║  Duration: ' + output.duration + 'ms'.padEnd(32) + '║')
    console.log('║                                            ║')
    console.log('║  Result:                                   ║')

    const resultLines = wrapText(JSON.stringify(output.result, null, 2), 38)
    for (const line of resultLines) {
      console.log('║  ' + line.padEnd(42) + ' ║')
    }
  } else {
    console.log('║  Status: Failed ✗'.padEnd(44) + '║')
    console.log('║  Duration: ' + output.duration + 'ms'.padEnd(32) + '║')
    console.log('║                                            ║')
    console.log('║  Error:                                    ║')

    const errorLines = wrapText(output.error, 38)
    for (const line of errorLines) {
      console.log('║  ' + line.padEnd(42) + ' ║')
    }
  }

  console.log('║                                            ║')
  console.log('╚════════════════════════════════════════════╝')
}
```

### Quit Command

```javascript
async function processQuit(state) {
  // Show summary
  const summary = generateExecutionSummary(state)
  displaySummary(summary)

  // Confirm quit
  const response = await AskUserQuestion({
    questions: [{
      question: "Are you sure you want to quit?",
      header: "Quit",
      multiSelect: false,
      options: [
        {label: 'Yes', description: 'Abort workflow execution'},
        {label: 'No', description: 'Return to execution'}
      ]
    }]
  })

  const confirmed = Object.values(response)[0] === 'Yes'

  if (confirmed) {
    state.steering.paused = true
    state.steering.command = 'quit'
    return {action: 'quit', success: true, confirmed: true}
  }

  return {action: 'quit', success: false, cancelled: true}
}

function generateExecutionSummary(state) {
  return {
    total: state.graph.nodes.length,
    completed: state.execution.completed.length,
    failed: state.execution.failed.length,
    skipped: state.execution.skipped.length,
    pending: state.graph.nodes.filter(n => n.status === 'pending').length,
    duration: Date.now() - state.startTime
  }
}

function displaySummary(summary) {
  console.log('╔════════════════════════════════════════════╗')
  console.log('║  Execution Summary                         ║')
  console.log('╠════════════════════════════════════════════╣')
  console.log('║                                            ║')
  console.log('║  Total steps: ' + summary.total.toString().padEnd(28) + ' ║')
  console.log('║  Completed: ' + summary.completed.toString().padEnd(30) + '✓║')
  console.log('║  Failed: ' + summary.failed.toString().padEnd(33) + '✗║')
  console.log('║  Skipped: ' + summary.skipped.toString().padEnd(32) + '⊗║')
  console.log('║  Pending: ' + summary.pending.toString().padEnd(32) + '○║')
  console.log('║                                            ║')
  console.log('║  Duration: ' + formatDuration(summary.duration).padEnd(31) + '║')
  console.log('║                                            ║')
  console.log('╚════════════════════════════════════════════╝')
}
```

## Context-Aware Guidance

### Contextual Suggestions

```javascript
function getContextualSuggestions(state, checkpoint) {
  const suggestions = []

  // Check recent outputs for issues
  const recentOutputs = getRecentOutputs(state, 3)
  for (const output of recentOutputs) {
    if (containsWarnings(output)) {
      suggestions.push({
        type: 'warning',
        message: 'Recent output contains warnings - consider reviewing before continuing'
      })
    }
  }

  // Check for failed branches
  if (state.execution.failed.length > 0) {
    suggestions.push({
      type: 'error',
      message: 'Some steps have failed - use (v)iew to inspect errors'
    })
  }

  // Check for long-running steps
  const longRunning = state.execution.current.filter(id => {
    const startTime = state.execution.outputs[id]?.startTime
    return startTime && (Date.now() - startTime) > 60000
  })

  if (longRunning.length > 0) {
    suggestions.push({
      type: 'info',
      message: 'Some steps are taking longer than expected'
    })
  }

  return suggestions
}

function displaySuggestions(suggestions) {
  if (suggestions.length === 0) return

  console.log('╠════════════════════════════════════════════╣')
  console.log('║  Suggestions:                              ║')
  console.log('║                                            ║')

  for (const suggestion of suggestions) {
    const icon = {
      error: '✗',
      warning: '⚠',
      info: 'ℹ'
    }[suggestion.type] || '•'

    const lines = wrapText(suggestion.message, 38)
    for (let i = 0; i < lines.length; i++) {
      const prefix = i === 0 ? `  ${icon} ` : '    '
      console.log('║' + prefix + lines[i].padEnd(42 - prefix.length) + '║')
    }
  }

  console.log('║                                            ║')
}
```

### Smart Defaults

```javascript
function getRecommendedAction(context) {
  // Based on context, recommend best action

  if (context.hasErrors) {
    // Errors present - suggest retry or edit
    return context.errorType === 'timeout' ? 'retry' : 'edit'
  }

  if (context.atCheckpoint) {
    // At checkpoint - usually continue
    return 'continue'
  }

  if (context.hasWarnings) {
    // Warnings - suggest viewing output
    return 'view'
  }

  return 'continue'
}
```

## Steering State Management

### State Tracking

```javascript
const steeringState = {
  paused: false,
  position: null,
  command: null,
  history: [],
  snapshots: []
}

function recordCommand(command, result) {
  steeringState.history.push({
    command: command,
    result: result,
    timestamp: Date.now()
  })
}

function createSteringSnapshot(state) {
  steeringState.snapshots.push({
    state: createSnapshot(state),
    timestamp: Date.now()
  })
}
```

### Undo/Redo Support

```javascript
async function processUndo(state) {
  if (steeringState.snapshots.length === 0) {
    return {action: 'undo', success: false, error: 'No snapshots to restore'}
  }

  // Get previous snapshot
  const snapshot = steeringState.snapshots.pop()

  // Restore state
  restoreSnapshot(state, snapshot.state)

  visualizer.update(state.graph)
  return {action: 'undo', success: true}
}
```

## Advanced Commands

### Debug Command

```javascript
async function processDebug(state) {
  // Find current execution point
  const currentNode = state.graph.nodes.find(n => n.id === state.steering.position)

  // Create debug node
  const debugNode = {
    id: `debug-${Date.now()}`,
    type: 'agent',
    agent: 'explore',
    instruction: `Debug: Investigate state before ${currentNode.agent}`,
    status: 'pending'
  }

  // Insert into graph
  insertNodeBefore(debugNode, currentNode, state.graph)

  // Execute debug node
  state.steering.paused = false
  await executeAgent(debugNode, state)

  // Pause again for review
  state.steering.paused = true
  visualizer.update(state.graph)

  return {action: 'debug', success: true, node: debugNode.id}
}

function insertNodeBefore(newNode, targetNode, graph) {
  // Add node
  graph.nodes.push(newNode)

  // Find incoming edges to target
  const incoming = graph.edges.filter(e => e.to === targetNode.id)

  // Redirect to new node
  for (const edge of incoming) {
    edge.to = newNode.id
  }

  // Connect new node to target
  graph.edges.push({
    from: newNode.id,
    to: targetNode.id,
    condition: null
  })
}
```

### Fork Command

```javascript
async function processFork(state) {
  // Ask for fork strategies
  const response = await AskUserQuestion({
    questions: [{
      question: "How many alternative approaches to try?",
      header: "Fork",
      multiSelect: false,
      options: [
        {label: '2', description: 'Try 2 different approaches'},
        {label: '3', description: 'Try 3 different approaches'},
        {label: 'Custom', description: 'Specify approaches manually'}
      ]
    }]
  })

  const count = parseInt(Object.values(response)[0]) || 2

  // Create fork branches
  const branches = []
  for (let i = 0; i < count; i++) {
    const approach = await getApproachFromUser(i + 1)
    branches.push(createBranchNode(approach, state))
  }

  // Insert parallel structure
  insertParallelBranches(branches, state)

  // Execute branches
  state.steering.paused = false
  await executeParallel(branches, state)

  // Pause to review results
  state.steering.paused = true
  visualizer.update(state.graph)

  return {action: 'fork', success: true, branches: branches.length}
}
```

## Integration with Executor

### Executor-Steering Interface

```javascript
// Executor calls steering at checkpoints
async function executeCheckpoint(checkpoint, state) {
  // Pause execution
  state.steering.paused = true
  state.steering.position = checkpoint.id

  // Show checkpoint UI
  visualizer.showCheckpoint(checkpoint)

  // Get command from steering
  const command = await getSteeringCommand(checkpoint)

  // Process command
  const result = await processSteeringCommand(command, state)

  // Resume or abort based on result
  if (result.success && result.action !== 'quit') {
    state.steering.paused = false
  }

  return result
}

// Steering provides command processing
async function processSteeringCommand(command, state) {
  switch (command) {
    case 'continue': return await processContinue(state)
    case 'jump': return await processJump(state)
    case 'repeat': return await processRepeat(state)
    case 'edit': return await processEdit(state)
    case 'view': return await processView(state)
    case 'quit': return await processQuit(state)
    case 'debug': return await processDebug(state)
    case 'fork': return await processFork(state)
    default:
      return {action: command, success: false, error: 'Unknown command'}
  }
}
```

## Testing

### Steering Tests

```javascript
describe('Steering', () => {
  test('processes continue command', async () => {
    const state = createStateAtCheckpoint()
    const result = await processContinue(state)

    expect(result.success).toBe(true)
    expect(state.steering.paused).toBe(false)
  })

  test('processes jump command', async () => {
    const state = createStateWithMultipleNodes()
    const result = await processJump(state)

    expect(result.success).toBe(true)
    expect(state.steering.position).toBeDefined()
  })

  test('processes edit command', async () => {
    const state = createState()
    const result = await processEdit(state)

    if (result.success) {
      expect(state.workflow).not.toBe(state.originalWorkflow)
    }
  })

  test('displays contextual suggestions', () => {
    const state = createStateWithErrors()
    const suggestions = getContextualSuggestions(state)

    expect(suggestions.length).toBeGreaterThan(0)
    expect(suggestions[0].type).toBe('error')
  })
})
```

## Best Practices

1. **Provide clear options** - Show what each command does
2. **Context matters** - Give situational guidance
3. **Confirm destructive actions** - Ask before quit/edit
4. **Show current state** - User needs to know where they are
5. **Enable exploration** - Allow viewing outputs anytime
6. **Support undo** - Let users go back
7. **Recommend actions** - Suggest best next step
8. **Handle errors gracefully** - Invalid commands shouldn't crash

## User Experience Guidelines

### Menu Design

**Clear Labels:**
- Use single-letter shortcuts: (c), (e), (q)
- Provide full word labels: Continue, Edit, Quit
- Include descriptions: "Resume from current point"

**Visual Hierarchy:**
- Highlight recommended actions
- Group related commands
- Show context-specific options

**Consistent Formatting:**
- Same box drawing characters throughout
- Consistent spacing and alignment
- Clear visual separation between sections

### Prompt Design

**Checkpoint Prompts:**
- Explain what was just completed
- State what will happen next
- Ask clear question

**Error Prompts:**
- Describe what went wrong
- Suggest likely causes
- Offer recovery options

**Confirmation Prompts:**
- Confirm understanding
- Show consequences
- Provide escape hatch

## See Also

- [executor.md](executor.md) - Execution engine integration
- [visualizer.md](visualizer.md) - Display components
- [parser.md](parser.md) - Workflow editing and re-parsing
- [../features/error-handling.md](../features/error-handling.md) - Error recovery patterns
