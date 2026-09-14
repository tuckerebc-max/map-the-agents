# Visualizer Implementation

Complete guide to the ASCII art visualization system for orchestration workflows.

## Overview

The visualizer renders workflow graphs as ASCII art with real-time status updates, providing visual feedback throughout execution.

## Core Responsibilities

1. **Render workflow structure** - Display graph topology
2. **Show status indicators** - Visual representation of node states
3. **Update in real-time** - Refresh display as execution progresses
4. **Provide user interface** - Show control options and prompts
5. **Maintain readability** - Keep displays under 80 characters wide

## Status Indicators

### Indicator Symbols

| Symbol | Status | Description |
|--------|--------|-------------|
| ○ | Pending | Not yet started |
| ● | Executing | Currently running |
| ✓ | Completed | Successfully finished |
| ✗ | Failed | Execution failed |
| ⊗ | Skipped | Bypassed by user or condition |

### Color Support (Optional)

When terminal supports color:
- ○ Pending - Gray
- ● Executing - Yellow/Blinking
- ✓ Completed - Green
- ✗ Failed - Red
- ⊗ Skipped - Dim gray

## Visualization Format

### Standard Layout

```
╔════════════════════════════════════════════╗
║  Workflow: [workflow-name]                 ║
╠════════════════════════════════════════════╣
║                                            ║
║    [step-1] ○                              ║
║        │                                   ║
║    [step-2] ●                              ║
║        │                                   ║
║    [step-3] ○                              ║
║                                            ║
╠════════════════════════════════════════════╣
║ Status: [current status message]           ║
╠════════════════════════════════════════════╣
║ (c)ontinue  (e)dit  (q)uit                 ║
╚════════════════════════════════════════════╝
```

### Layout Components

**Header:**
```
╔════════════════════════════════════════════╗
║  Workflow: [name]                          ║
╠════════════════════════════════════════════╣
```

**Body:**
```
║                                            ║
║    [workflow visualization]                ║
║                                            ║
```

**Status Bar:**
```
╠════════════════════════════════════════════╣
║ Status: [message]                          ║
╠════════════════════════════════════════════╣
```

**Control Menu:**
```
║ (c)ontinue  (e)dit  (q)uit                 ║
╚════════════════════════════════════════════╝
```

## Rendering Algorithms

### Simple Sequence Visualization

```javascript
function renderSequence(nodes) {
  const lines = []

  for (let i = 0; i < nodes.length; i++) {
    const node = nodes[i]
    const status = getStatusSymbol(node.status)

    // Node line
    lines.push(`    [${node.agent || node.label}] ${status}`)

    // Connector (except last)
    if (i < nodes.length - 1) {
      lines.push(`        │`)
    }
  }

  return lines
}
```

**Output:**
```
    [explore] ✓
        │
    [implement] ●
        │
    [review] ○
```

### Parallel Branches Visualization

```javascript
function renderParallel(branches) {
  const lines = []

  // Find longest branch for alignment
  const maxDepth = Math.max(...branches.map(b => b.length))

  // Opening
  lines.push(`    ┌───┴───┐`)

  // Render each level
  for (let level = 0; level < maxDepth; level++) {
    const branchLines = []

    for (const branch of branches) {
      if (level < branch.length) {
        const node = branch[level]
        const status = getStatusSymbol(node.status)
        branchLines.push(`[${node.agent}] ${status}`)
      } else {
        branchLines.push(`         `) // Empty space
      }
    }

    lines.push(`  ${branchLines.join('  ')}`)

    // Connector
    if (level < maxDepth - 1) {
      const connectors = branches.map((b, i) =>
        level < b.length - 1 ? '    │' : '     '
      )
      lines.push(`  ${connectors.join('  ')}`)
    }
  }

  // Closing
  lines.push(`    └───┬───┘`)

  return lines
}
```

**Output:**
```
    ┌───┴───┐
  [test] ✓  [lint] ●
      │        │
  [report] ○  [fix] ○
    └───┬───┘
```

### Complex Graph Visualization

```javascript
function renderGraph(graph) {
  const lines = []
  const rendered = new Set()

  function renderNode(nodeId, indent = 0) {
    if (rendered.has(nodeId)) {
      lines.push(`${' '.repeat(indent * 4)}[${nodeId}] (see above)`)
      return
    }

    const node = graph.nodes.find(n => n.id === nodeId)
    if (!node) return

    rendered.add(nodeId)

    const status = getStatusSymbol(node.status)
    const label = node.agent || node.label || node.id
    lines.push(`${' '.repeat(indent * 4)}[${label}] ${status}`)

    // Find outgoing edges
    const outgoing = graph.edges.filter(e => e.from === nodeId)

    if (outgoing.length === 0) return

    if (outgoing.length === 1) {
      // Simple sequence
      lines.push(`${' '.repeat(indent * 4)}    │`)
      renderNode(outgoing[0].to, indent)
    } else {
      // Parallel branches
      lines.push(`${' '.repeat(indent * 4)}    ┌${'─'.repeat(outgoing.length * 3)}┐`)

      for (const edge of outgoing) {
        renderNode(edge.to, indent + 1)
      }

      lines.push(`${' '.repeat(indent * 4)}    └${'─'.repeat(outgoing.length * 3)}┘`)
    }
  }

  // Find start nodes
  const startNodes = graph.nodes.filter(node =>
    !graph.edges.some(edge => edge.to === node.id)
  )

  for (const start of startNodes) {
    renderNode(start.id)
  }

  return lines
}
```

### Conditional Flow Visualization

```javascript
function renderConditional(source, condition, target) {
  const status = getStatusSymbol(source.status)

  return [
    `    [${source.agent}] ${status}`,
    `        │`,
    `    ${condition}`,
    `        ↓`,
    `    [${target.agent}] ${getStatusSymbol(target.status)}`
  ]
}
```

**Output:**
```
    [test] ✗
        │
    (if failed)
        ↓
    [fix] ●
```

## Real-Time Updates

### Update Strategy

```javascript
class WorkflowVisualizer {
  constructor(graph) {
    this.graph = graph
    this.lastRender = null
  }

  update(nodeId, status) {
    // Update node status
    const node = this.graph.nodes.find(n => n.id === nodeId)
    if (node) {
      node.status = status
    }

    // Re-render
    this.render()
  }

  render() {
    // Clear previous display (if terminal supports it)
    if (this.lastRender) {
      console.clear()
    }

    const visualization = this.buildVisualization()
    console.log(visualization)

    this.lastRender = Date.now()
  }

  buildVisualization() {
    const lines = []

    // Header
    lines.push('╔════════════════════════════════════════════╗')
    lines.push('║  Workflow: ' + this.graph.name.padEnd(32) + '║')
    lines.push('╠════════════════════════════════════════════╣')

    // Body
    lines.push('║                                            ║')
    const graphLines = renderGraph(this.graph)
    for (const line of graphLines) {
      lines.push('║ ' + line.padEnd(42) + ' ║')
    }
    lines.push('║                                            ║')

    // Status bar
    lines.push('╠════════════════════════════════════════════╣')
    lines.push('║ Status: ' + this.getCurrentStatus().padEnd(33) + '║')
    lines.push('╠════════════════════════════════════════════╣')

    // Control menu
    lines.push('║ ' + this.getControlMenu().padEnd(42) + ' ║')
    lines.push('╚════════════════════════════════════════════╝')

    return lines.join('\n')
  }

  getCurrentStatus() {
    const pending = this.graph.nodes.filter(n => n.status === 'pending').length
    const executing = this.graph.nodes.filter(n => n.status === 'executing').length
    const completed = this.graph.nodes.filter(n => n.status === 'completed').length
    const failed = this.graph.nodes.filter(n => n.status === 'failed').length

    if (executing > 0) {
      return `Executing ${executing} step(s)...`
    }
    if (failed > 0) {
      return `Failed at step ${failed}`
    }
    if (pending === 0) {
      return `Complete (${completed}/${this.graph.nodes.length})`
    }
    return `Ready (${completed}/${this.graph.nodes.length} complete)`
  }

  getControlMenu() {
    const isPaused = this.graph.nodes.some(n =>
      n.type === 'checkpoint' && n.status === 'executing'
    )

    if (isPaused) {
      return '(c)ontinue  (j)ump  (r)epeat  (e)dit  (v)iew  (q)uit'
    }

    return '(c)ontinue  (e)dit  (q)uit'
  }
}
```

### Animation Support

```javascript
function animateNode(nodeId, status) {
  // Animate status change
  if (status === 'executing') {
    // Blink or pulse
    const frames = ['●', '◐', '◑', '◒', '◓']
    let frameIndex = 0

    const interval = setInterval(() => {
      updateNodeSymbol(nodeId, frames[frameIndex])
      frameIndex = (frameIndex + 1) % frames.length
    }, 200)

    return () => clearInterval(interval)
  }
}
```

## User Confirmation Interface

### Before Execution

```javascript
function showConfirmation(graph) {
  const visualization = renderGraph(graph)

  console.log('╔════════════════════════════════════════════╗')
  console.log('║  Workflow Preview                          ║')
  console.log('╠════════════════════════════════════════════╣')
  console.log('║                                            ║')

  for (const line of visualization) {
    console.log('║ ' + line.padEnd(42) + ' ║')
  }

  console.log('║                                            ║')
  console.log('╠════════════════════════════════════════════╣')
  console.log('║ Total steps: ' + graph.nodes.length.toString().padEnd(30) + '║')
  console.log('║ Parallel branches: ' + countParallelBranches(graph).toString().padEnd(22) + '║')
  console.log('║ Checkpoints: ' + countCheckpoints(graph).toString().padEnd(28) + '║')
  console.log('╠════════════════════════════════════════════╣')
  console.log('║ Ready to execute?                          ║')
  console.log('╠════════════════════════════════════════════╣')
  console.log('║ (c)ontinue  (e)dit  (q)uit                 ║')
  console.log('╚════════════════════════════════════════════╝')
}
```

### During Execution

```javascript
function showProgress(graph, currentNode) {
  const total = graph.nodes.length
  const completed = graph.nodes.filter(n => n.status === 'completed').length
  const percentage = Math.round((completed / total) * 100)

  console.log('╠════════════════════════════════════════════╣')
  console.log('║ Progress: ' + generateProgressBar(percentage, 30) + '║')
  console.log('║ ' + `${completed}/${total} steps complete (${percentage}%)`.padEnd(42) + ' ║')
  console.log('╠════════════════════════════════════════════╣')
}

function generateProgressBar(percentage, width) {
  const filled = Math.round((percentage / 100) * width)
  const empty = width - filled
  return '[' + '█'.repeat(filled) + '░'.repeat(empty) + ']'
}
```

## Width Management

### 80-Character Constraint

```javascript
function fitToWidth(text, maxWidth = 80) {
  if (text.length <= maxWidth) {
    return text
  }

  // Truncate with ellipsis
  return text.slice(0, maxWidth - 3) + '...'
}

function wrapText(text, maxWidth = 42) {
  const words = text.split(' ')
  const lines = []
  let currentLine = ''

  for (const word of words) {
    if ((currentLine + word).length <= maxWidth) {
      currentLine += (currentLine ? ' ' : '') + word
    } else {
      lines.push(currentLine)
      currentLine = word
    }
  }

  if (currentLine) {
    lines.push(currentLine)
  }

  return lines
}
```

### Compact Mode

For large workflows (>20 nodes), use compact mode:

```javascript
function renderCompact(graph) {
  const lines = []

  // Show only key nodes
  const keyNodes = [
    ...graph.nodes.filter(n => n.type === 'checkpoint'),
    ...graph.nodes.filter(n => n.status === 'executing'),
    ...graph.nodes.filter(n => n.status === 'failed')
  ]

  for (const node of keyNodes) {
    const status = getStatusSymbol(node.status)
    lines.push(`  [${node.agent || node.label}] ${status}`)
  }

  // Summary for others
  const other = graph.nodes.length - keyNodes.length
  if (other > 0) {
    lines.push(`  ... ${other} more steps`)
  }

  return lines
}
```

## Error Visualization

### Error Display

```javascript
function showError(node, error) {
  console.log('╔════════════════════════════════════════════╗')
  console.log('║  ERROR: Agent Execution Failed             ║')
  console.log('╠════════════════════════════════════════════╣')
  console.log('║                                            ║')
  console.log('║  Node: [' + (node.agent || node.label) + '] ✗'.padEnd(42) + ' ║')
  console.log('║                                            ║')
  console.log('║  Error:                                    ║')

  const errorLines = wrapText(error.message, 38)
  for (const line of errorLines) {
    console.log('║  ' + line.padEnd(42) + ' ║')
  }

  console.log('║                                            ║')
  console.log('╠════════════════════════════════════════════╣')
  console.log('║  Recovery options:                         ║')
  console.log('║  (r)etry  (e)dit  (s)kip  (d)ebug  (q)uit  ║')
  console.log('╚════════════════════════════════════════════╝')
}
```

## Checkpoint Display

### Checkpoint Pause

```javascript
function showCheckpoint(checkpoint) {
  console.log('╔════════════════════════════════════════════╗')
  console.log('║  CHECKPOINT: ' + checkpoint.label.padEnd(29) + '║')
  console.log('╠════════════════════════════════════════════╣')
  console.log('║                                            ║')

  const prompt = checkpoint.prompt || 'Review progress before continuing'
  const promptLines = wrapText(prompt, 38)
  for (const line of promptLines) {
    console.log('║  ' + line.padEnd(42) + ' ║')
  }

  console.log('║                                            ║')
  console.log('╠════════════════════════════════════════════╣')
  console.log('║  Commands:                                 ║')
  console.log('║  (c)ontinue  (j)ump  (r)epeat  (e)dit      ║')
  console.log('║  (v)iew-output  (q)uit                     ║')
  console.log('╚════════════════════════════════════════════╝')
}
```

## Completion Display

### Workflow Summary

```javascript
function showCompletion(graph, duration) {
  const completed = graph.nodes.filter(n => n.status === 'completed').length
  const failed = graph.nodes.filter(n => n.status === 'failed').length
  const skipped = graph.nodes.filter(n => n.status === 'skipped').length

  console.log('╔════════════════════════════════════════════╗')
  console.log('║  Workflow Complete                         ║')
  console.log('╠════════════════════════════════════════════╣')
  console.log('║                                            ║')
  console.log('║  Total steps: ' + graph.nodes.length.toString().padEnd(28) + ' ║')
  console.log('║  Completed: ' + completed.toString().padEnd(30) + '✓║')
  console.log('║  Failed: ' + failed.toString().padEnd(33) + '✗║')
  console.log('║  Skipped: ' + skipped.toString().padEnd(32) + '⊗║')
  console.log('║  Duration: ' + formatDuration(duration).padEnd(31) + '║')
  console.log('║                                            ║')
  console.log('╠════════════════════════════════════════════╣')
  console.log('║  Next steps:                               ║')
  console.log('║  (v)iew results  (s)ave template           ║')
  console.log('║  (r)un again  (m)enu                       ║')
  console.log('╚════════════════════════════════════════════╝')
}

function formatDuration(ms) {
  const seconds = Math.floor(ms / 1000)
  const minutes = Math.floor(seconds / 60)
  const hours = Math.floor(minutes / 60)

  if (hours > 0) {
    return `${hours}h ${minutes % 60}m ${seconds % 60}s`
  }
  if (minutes > 0) {
    return `${minutes}m ${seconds % 60}s`
  }
  return `${seconds}s`
}
```

## Advanced Visualization Features

### Mini-Map for Large Workflows

```javascript
function renderMiniMap(graph, currentNode) {
  const lines = []

  // Group nodes by status
  const groups = {
    completed: graph.nodes.filter(n => n.status === 'completed'),
    executing: graph.nodes.filter(n => n.status === 'executing'),
    pending: graph.nodes.filter(n => n.status === 'pending'),
    failed: graph.nodes.filter(n => n.status === 'failed')
  }

  lines.push('Mini-map:')
  lines.push('[' +
    '✓'.repeat(groups.completed.length) +
    '●'.repeat(groups.executing.length) +
    '○'.repeat(groups.pending.length) +
    '✗'.repeat(groups.failed.length) +
    '] <- You are here'
  )

  return lines
}
```

### Diff View for Edits

```javascript
function showDiff(originalGraph, modifiedGraph) {
  console.log('╔════════════════════════════════════════════╗')
  console.log('║  Workflow Changes                          ║')
  console.log('╠════════════════════════════════════════════╣')
  console.log('║                                            ║')
  console.log('║  Before:                                   ║')

  for (const line of renderGraph(originalGraph)) {
    console.log('║  - ' + line.padEnd(40) + ' ║')
  }

  console.log('║                                            ║')
  console.log('║  After:                                    ║')

  for (const line of renderGraph(modifiedGraph)) {
    console.log('║  + ' + line.padEnd(40) + ' ║')
  }

  console.log('║                                            ║')
  console.log('╠════════════════════════════════════════════╣')
  console.log('║  (a)ccept  (r)eject  (e)dit again          ║')
  console.log('╚════════════════════════════════════════════╝')
}
```

## Performance Optimization

### Lazy Rendering

```javascript
class LazyVisualizer {
  constructor(graph) {
    this.graph = graph
    this.visibleRange = {start: 0, end: 10}
  }

  renderVisible() {
    const visibleNodes = this.graph.nodes.slice(
      this.visibleRange.start,
      this.visibleRange.end
    )

    return renderGraph({
      nodes: visibleNodes,
      edges: this.graph.edges.filter(e =>
        visibleNodes.some(n => n.id === e.from || n.id === e.to)
      )
    })
  }

  scroll(direction) {
    if (direction === 'up' && this.visibleRange.start > 0) {
      this.visibleRange.start--
      this.visibleRange.end--
    } else if (direction === 'down' &&
               this.visibleRange.end < this.graph.nodes.length) {
      this.visibleRange.start++
      this.visibleRange.end++
    }
  }
}
```

### Debounced Updates

```javascript
class DebouncedVisualizer {
  constructor(graph, delay = 100) {
    this.graph = graph
    this.delay = delay
    this.updateTimer = null
  }

  scheduleUpdate() {
    if (this.updateTimer) {
      clearTimeout(this.updateTimer)
    }

    this.updateTimer = setTimeout(() => {
      this.render()
      this.updateTimer = null
    }, this.delay)
  }

  render() {
    // Actual rendering logic
  }
}
```

## Testing

### Visualization Tests

```javascript
describe('Visualizer', () => {
  test('renders simple sequence', () => {
    const graph = {
      nodes: [
        {id: '1', agent: 'explore', status: 'completed'},
        {id: '2', agent: 'implement', status: 'executing'}
      ],
      edges: [{from: '1', to: '2'}]
    }

    const output = renderGraph(graph)
    expect(output).toContain('[explore] ✓')
    expect(output).toContain('[implement] ●')
  })

  test('renders parallel branches', () => {
    const graph = createParallelGraph(['test', 'lint'])
    const output = renderGraph(graph)

    expect(output).toContain('┌───┴───┐')
    expect(output).toContain('[test]')
    expect(output).toContain('[lint]')
    expect(output).toContain('└───┬───┘')
  })

  test('fits within 80 characters', () => {
    const graph = createLargeGraph()
    const lines = renderGraph(graph)

    for (const line of lines) {
      expect(line.length).toBeLessThanOrEqual(80)
    }
  })
})
```

## Best Practices

1. **Keep it simple** - ASCII art should be clear and minimal
2. **Update frequently** - Refresh display as status changes
3. **Respect width** - Stay within 80 characters
4. **Use symbols consistently** - Same meaning everywhere
5. **Provide context** - Show current status and options
6. **Handle errors gracefully** - Clear error displays
7. **Test rendering** - Verify all graph types render correctly

## See Also

- [parser.md](parser.md) - Syntax parsing
- [executor.md](executor.md) - Graph execution
- [steering.md](steering.md) - Interactive control
- [../features/error-handling.md](../features/error-handling.md) - Error display patterns
