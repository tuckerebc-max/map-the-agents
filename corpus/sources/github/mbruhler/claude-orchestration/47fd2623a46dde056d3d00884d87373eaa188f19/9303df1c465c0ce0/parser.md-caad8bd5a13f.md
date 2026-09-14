# Parser Implementation

Complete guide to the orchestration syntax parser implementation.

## Overview

The parser transforms workflow syntax strings into executable directed graphs through four phases:
1. Tokenization - Break syntax into tokens
2. AST Construction - Build abstract syntax tree
3. Graph Creation - Convert tree to directed graph
4. Validation - Verify graph integrity

## Phase 1: Tokenization

### Purpose
Break raw workflow syntax into structured tokens for parsing.

### Token Types

**Operators:**
- `->` Sequential operator (flows to next step)
- `||` Parallel operator (execute simultaneously)
- `~>` Conditional operator (conditional flow)
- `@` Checkpoint marker (pause point)
- `[...]` Subgraph brackets (group operations)

**Elements:**
- Agent names (explore, general-purpose, code-reviewer, etc.)
- Instructions (quoted strings: "do something")
- Conditions (parenthesized: `(if passed)`)
- Labels (checkpoint names: `@security-gate`)

### Tokenization Algorithm

```javascript
function tokenize(workflow) {
  const tokens = []
  let position = 0
  let current = ''

  while (position < workflow.length) {
    const char = workflow[position]

    // Handle operators
    if (char === '-' && workflow[position + 1] === '>') {
      if (current.trim()) tokens.push({type: 'agent', value: current.trim()})
      tokens.push({type: 'sequential', value: '->'})
      current = ''
      position += 2
      continue
    }

    if (char === '|' && workflow[position + 1] === '|') {
      if (current.trim()) tokens.push({type: 'agent', value: current.trim()})
      tokens.push({type: 'parallel', value: '||'})
      current = ''
      position += 2
      continue
    }

    if (char === '~' && workflow[position + 1] === '>') {
      if (current.trim()) tokens.push({type: 'agent', value: current.trim()})
      tokens.push({type: 'conditional', value: '~>'})
      current = ''
      position += 2
      continue
    }

    // Handle checkpoint marker
    if (char === '@') {
      if (current.trim()) tokens.push({type: 'agent', value: current.trim()})
      // Read until whitespace or operator
      let label = '@'
      position++
      while (position < workflow.length &&
             !/[\s\-\|\~\[\]\(\)]/.test(workflow[position])) {
        label += workflow[position++]
      }
      tokens.push({type: 'checkpoint', value: label})
      current = ''
      continue
    }

    // Handle subgraph brackets
    if (char === '[') {
      if (current.trim()) tokens.push({type: 'agent', value: current.trim()})
      tokens.push({type: 'open-bracket', value: '['})
      current = ''
      position++
      continue
    }

    if (char === ']') {
      if (current.trim()) tokens.push({type: 'agent', value: current.trim()})
      tokens.push({type: 'close-bracket', value: ']'})
      current = ''
      position++
      continue
    }

    // Handle conditions
    if (char === '(' && workflow.slice(position, position + 4) === '(if ') {
      if (current.trim()) tokens.push({type: 'agent', value: current.trim()})
      // Read until closing paren
      let condition = ''
      while (position < workflow.length && workflow[position] !== ')') {
        condition += workflow[position++]
      }
      condition += ')'
      position++
      tokens.push({type: 'condition', value: condition})
      current = ''
      continue
    }

    // Handle quoted instructions
    if (char === '"') {
      // Agent name is in current
      const agent = current.trim()
      current = ''
      position++
      let instruction = ''
      while (position < workflow.length && workflow[position] !== '"') {
        instruction += workflow[position++]
      }
      position++ // Skip closing quote
      tokens.push({
        type: 'agent-with-instruction',
        agent: agent,
        instruction: instruction
      })
      continue
    }

    // Accumulate characters
    if (!/\s/.test(char)) {
      current += char
    } else if (current.trim()) {
      tokens.push({type: 'agent', value: current.trim()})
      current = ''
    }

    position++
  }

  // Flush remaining
  if (current.trim()) {
    tokens.push({type: 'agent', value: current.trim()})
  }

  return tokens
}
```

### Edge Cases

**Nested quotes:**
```
agent:"instruction with \"nested\" quotes"
```
Handle by escaping or using single quotes internally.

**Whitespace in operators:**
```
agent - > next-agent
```
Normalize by ignoring whitespace around operators.

**Ambiguous syntax:**
```
agent->next||parallel
```
Parse left-to-right with operator precedence.

**Empty tokens:**
```
agent -> -> next
```
Detect and report error: "Empty step between operators"

## Phase 2: AST Construction

### Purpose
Build a hierarchical abstract syntax tree respecting operator precedence.

### Operator Precedence
1. `[...]` Subgraphs (highest - group first)
2. `||` Parallel (execute together)
3. `->` Sequential (execute in order)
4. `~>` Conditional (lowest - after evaluation)

### AST Node Types

```javascript
// Sequential node
{
  type: 'sequence',
  steps: [node1, node2, node3]
}

// Parallel node
{
  type: 'parallel',
  branches: [node1, node2, node3]
}

// Conditional node
{
  type: 'conditional',
  source: node,
  condition: 'if passed',
  target: node
}

// Agent node
{
  type: 'agent',
  name: 'explore',
  instruction: 'analyze code'
}

// Checkpoint node
{
  type: 'checkpoint',
  label: '@review'
}

// Subgraph node
{
  type: 'subgraph',
  children: astNode
}
```

### Parsing Algorithm

```javascript
function buildAST(tokens) {
  let position = 0

  function parseExpression(precedence = 0) {
    let left = parsePrimary()

    while (position < tokens.length) {
      const token = tokens[position]
      const opPrecedence = getOperatorPrecedence(token.type)

      if (opPrecedence < precedence) break

      position++ // Consume operator

      if (token.type === 'sequential') {
        const right = parseExpression(opPrecedence + 1)
        left = {
          type: 'sequence',
          steps: left.type === 'sequence' ? [...left.steps, right] : [left, right]
        }
      }
      else if (token.type === 'parallel') {
        const right = parseExpression(opPrecedence + 1)
        left = {
          type: 'parallel',
          branches: left.type === 'parallel' ? [...left.branches, right] : [left, right]
        }
      }
      else if (token.type === 'conditional') {
        // Previous token should have condition
        const condition = findCondition(position - 2)
        const right = parseExpression(opPrecedence + 1)
        left = {
          type: 'conditional',
          source: left,
          condition: condition || 'if failed',
          target: right
        }
      }
    }

    return left
  }

  function parsePrimary() {
    const token = tokens[position++]

    if (token.type === 'agent') {
      return {type: 'agent', name: token.value, instruction: null}
    }

    if (token.type === 'agent-with-instruction') {
      return {type: 'agent', name: token.agent, instruction: token.instruction}
    }

    if (token.type === 'checkpoint') {
      return {type: 'checkpoint', label: token.value}
    }

    if (token.type === 'open-bracket') {
      const subgraph = parseExpression(0)
      if (tokens[position]?.type !== 'close-bracket') {
        throw new Error(`Unclosed subgraph bracket at position ${position}`)
      }
      position++ // Consume close bracket
      return {type: 'subgraph', children: subgraph}
    }

    throw new Error(`Unexpected token: ${token.type} at position ${position}`)
  }

  function getOperatorPrecedence(type) {
    if (type === 'open-bracket') return 4
    if (type === 'parallel') return 3
    if (type === 'sequential') return 2
    if (type === 'conditional') return 1
    return 0
  }

  return parseExpression()
}
```

### AST Examples

**Simple sequence:**
```
explore -> implement -> review
```
AST:
```javascript
{
  type: 'sequence',
  steps: [
    {type: 'agent', name: 'explore', instruction: null},
    {type: 'agent', name: 'implement', instruction: null},
    {type: 'agent', name: 'review', instruction: null}
  ]
}
```

**Parallel with merge:**
```
[test || lint] -> merge
```
AST:
```javascript
{
  type: 'sequence',
  steps: [
    {
      type: 'subgraph',
      children: {
        type: 'parallel',
        branches: [
          {type: 'agent', name: 'test', instruction: null},
          {type: 'agent', name: 'lint', instruction: null}
        ]
      }
    },
    {type: 'agent', name: 'merge', instruction: null}
  ]
}
```

**Conditional flow:**
```
test (if failed)~> fix -> test
```
AST:
```javascript
{
  type: 'conditional',
  source: {type: 'agent', name: 'test', instruction: null},
  condition: 'if failed',
  target: {
    type: 'sequence',
    steps: [
      {type: 'agent', name: 'fix', instruction: null},
      {type: 'agent', name: 'test', instruction: null}
    ]
  }
}
```

## Phase 3: Graph Creation

### Purpose
Convert AST into directed graph with nodes and edges for execution.

### Graph Structure

```javascript
{
  nodes: [
    {
      id: 'node-1',
      type: 'agent',
      agent: 'explore',
      instruction: 'analyze code',
      status: 'pending'
    }
  ],
  edges: [
    {
      from: 'node-1',
      to: 'node-2',
      condition: null
    }
  ]
}
```

### Conversion Algorithm

```javascript
function astToGraph(ast) {
  const nodes = []
  const edges = []
  let nodeIdCounter = 0

  function generateId() {
    return `node-${nodeIdCounter++}`
  }

  function processNode(astNode, parentId = null) {
    if (astNode.type === 'agent') {
      const nodeId = generateId()
      nodes.push({
        id: nodeId,
        type: 'agent',
        agent: astNode.name,
        instruction: astNode.instruction,
        status: 'pending'
      })
      if (parentId) {
        edges.push({from: parentId, to: nodeId, condition: null})
      }
      return nodeId
    }

    if (astNode.type === 'checkpoint') {
      const nodeId = generateId()
      nodes.push({
        id: nodeId,
        type: 'checkpoint',
        label: astNode.label,
        status: 'pending'
      })
      if (parentId) {
        edges.push({from: parentId, to: nodeId, condition: null})
      }
      return nodeId
    }

    if (astNode.type === 'sequence') {
      let prevId = parentId
      for (const step of astNode.steps) {
        prevId = processNode(step, prevId)
      }
      return prevId
    }

    if (astNode.type === 'parallel') {
      // Create entry point for parallel
      const entryId = generateId()
      nodes.push({
        id: entryId,
        type: 'parallel-entry',
        status: 'pending'
      })
      if (parentId) {
        edges.push({from: parentId, to: entryId, condition: null})
      }

      // Process branches
      const branchExits = []
      for (const branch of astNode.branches) {
        const branchExit = processNode(branch, entryId)
        branchExits.push(branchExit)
      }

      // Create merge point
      const mergeId = generateId()
      nodes.push({
        id: mergeId,
        type: 'parallel-merge',
        waitFor: branchExits,
        status: 'pending'
      })
      for (const exitId of branchExits) {
        edges.push({from: exitId, to: mergeId, condition: null})
      }

      return mergeId
    }

    if (astNode.type === 'conditional') {
      const sourceId = processNode(astNode.source, parentId)
      const targetId = processNode(astNode.target, sourceId)
      // Update edge with condition
      const edge = edges.find(e => e.from === sourceId && e.to === targetId)
      if (edge) {
        edge.condition = astNode.condition
      }
      return targetId
    }

    if (astNode.type === 'subgraph') {
      return processNode(astNode.children, parentId)
    }

    throw new Error(`Unknown AST node type: ${astNode.type}`)
  }

  processNode(ast)

  return {nodes, edges}
}
```

## Phase 4: Validation

### Purpose
Verify graph integrity before execution.

### Validation Rules

**1. Unclosed Subgraphs**
```javascript
function validateBrackets(tokens) {
  let depth = 0
  for (let i = 0; i < tokens.length; i++) {
    if (tokens[i].type === 'open-bracket') depth++
    if (tokens[i].type === 'close-bracket') depth--
    if (depth < 0) {
      throw new Error(`Unexpected ']' at position ${i}`)
    }
  }
  if (depth > 0) {
    throw new Error(`Unclosed '[' - missing ${depth} closing bracket(s)`)
  }
}
```

**2. Unknown Agents**
```javascript
const VALID_AGENTS = [
  'explore',
  'general-purpose',
  'code-reviewer',
  'implementation-architect',
  'expert-code-implementer'
]

function validateAgents(graph) {
  for (const node of graph.nodes) {
    if (node.type === 'agent' && !VALID_AGENTS.includes(node.agent)) {
      const suggestions = findSimilar(node.agent, VALID_AGENTS)
      throw new Error(
        `Unknown agent '${node.agent}'. ` +
        `Valid agents: ${VALID_AGENTS.join(', ')}. ` +
        (suggestions.length ? `Did you mean '${suggestions[0]}'?` : '')
      )
    }
  }
}
```

**3. Orphaned Nodes**
```javascript
function validateConnectivity(graph) {
  const reachable = new Set()

  // Find start nodes (no incoming edges)
  const startNodes = graph.nodes.filter(node =>
    !graph.edges.some(edge => edge.to === node.id)
  )

  if (startNodes.length === 0) {
    throw new Error('No start node found - workflow has no entry point')
  }

  // DFS to find reachable nodes
  function visit(nodeId) {
    if (reachable.has(nodeId)) return
    reachable.add(nodeId)
    const outgoing = graph.edges.filter(e => e.from === nodeId)
    for (const edge of outgoing) {
      visit(edge.to)
    }
  }

  for (const start of startNodes) {
    visit(start.id)
  }

  // Check for orphaned nodes
  const orphaned = graph.nodes.filter(node => !reachable.has(node.id))
  if (orphaned.length > 0) {
    throw new Error(
      `Orphaned nodes detected (not reachable from start): ` +
      orphaned.map(n => n.agent || n.label).join(', ')
    )
  }
}
```

**4. Circular Dependencies**
```javascript
function validateNoCycles(graph) {
  const visiting = new Set()
  const visited = new Set()

  function visit(nodeId, path = []) {
    if (visiting.has(nodeId)) {
      // Found cycle
      const cycleStart = path.indexOf(nodeId)
      const cycle = path.slice(cycleStart).concat(nodeId)
      throw new Error(
        `Circular dependency detected: ${cycle.join(' -> ')}\n` +
        `Workflows cannot have cycles without exit conditions. ` +
        `Use conditional flow to create loops: @try -> step (if failed)~> @try`
      )
    }

    if (visited.has(nodeId)) return

    visiting.add(nodeId)
    path.push(nodeId)

    const outgoing = graph.edges.filter(e => e.from === nodeId)
    for (const edge of outgoing) {
      // Allow cycles with conditions (they have exit paths)
      if (!edge.condition) {
        visit(edge.to, [...path])
      }
    }

    visiting.delete(nodeId)
    visited.add(nodeId)
  }

  for (const node of graph.nodes) {
    if (!visited.has(node.id)) {
      visit(node.id)
    }
  }
}
```

**5. Invalid Conditions**
```javascript
const VALID_CONDITIONS = [
  'if passed',
  'if failed',
  'if all success',
  'if any success',
  'if all failed',
  'if any failed'
]

function validateConditions(graph) {
  for (const edge of graph.edges) {
    if (edge.condition) {
      const condition = edge.condition.replace(/^\(|\)$/g, '').trim()

      if (!VALID_CONDITIONS.includes(condition)) {
        // Allow custom conditions but warn
        console.warn(
          `Custom condition '${condition}' - will be evaluated from output. ` +
          `Built-in conditions: ${VALID_CONDITIONS.join(', ')}`
        )
      }
    }
  }
}
```

### Complete Validation Function

```javascript
function validateGraph(graph, tokens) {
  try {
    validateBrackets(tokens)
    validateAgents(graph)
    validateConnectivity(graph)
    validateNoCycles(graph)
    validateConditions(graph)
    return {valid: true}
  } catch (error) {
    return {valid: false, error: error.message}
  }
}
```

## Parser Output

### Success Case

```javascript
{
  success: true,
  graph: {
    nodes: [
      {id: 'node-0', type: 'agent', agent: 'explore', instruction: null, status: 'pending'},
      {id: 'node-1', type: 'checkpoint', label: '@review', status: 'pending'},
      {id: 'node-2', type: 'agent', agent: 'implement', instruction: null, status: 'pending'}
    ],
    edges: [
      {from: 'node-0', to: 'node-1', condition: null},
      {from: 'node-1', to: 'node-2', condition: null}
    ]
  }
}
```

### Error Case

```javascript
{
  success: false,
  error: {
    type: 'syntax-error',
    message: 'Unclosed subgraph bracket at position 42',
    position: 42,
    context: '[test -> lint -> ',
    suggestion: 'Add closing bracket: [test -> lint] -> next'
  }
}
```

## Error Messages

All error messages should be:
1. **Clear** - Explain what's wrong
2. **Contextual** - Show relevant code
3. **Actionable** - Suggest how to fix
4. **Specific** - Include position/line numbers

### Error Templates

```javascript
const ERROR_TEMPLATES = {
  unclosedBracket: (position) =>
    `Syntax error: Unclosed subgraph bracket at position ${position}.\n` +
    `Expected ']' before end of workflow.`,

  unknownAgent: (agent, suggestions) =>
    `Unknown agent '${agent}'. Valid agents:\n` +
    `  - explore\n  - general-purpose\n  - code-reviewer\n\n` +
    (suggestions.length ? `Did you mean '${suggestions[0]}'?` : ''),

  orphanedNode: (nodes) =>
    `Validation error: Node(s) not connected to workflow:\n` +
    nodes.map(n => `  - ${n}`).join('\n') + '\n\n' +
    `All nodes must be reachable from the start.`,

  circularDependency: (cycle) =>
    `Validation error: Circular dependency detected:\n` +
    `  ${cycle.join(' -> ')}\n\n` +
    `Workflows cannot have cycles without exit conditions.\n` +
    `Use conditional flow to create loops:\n` +
    `  @try -> step (if failed)~> @try`,

  invalidCondition: (condition) =>
    `Syntax error: Invalid condition format '${condition}'.\n` +
    `Expected format: (if condition)~>\n` +
    `Valid conditions: if passed, if failed, if all success, if any success`
}
```

## Performance Considerations

1. **Token caching** - Cache tokenization results for repeated parsing
2. **Lazy validation** - Only validate graph, not AST
3. **Incremental parsing** - For large workflows, parse in chunks
4. **Parallel validation** - Run validation rules concurrently

## Testing

### Unit Tests

```javascript
// Test tokenization
expect(tokenize('explore -> implement')).toEqual([
  {type: 'agent', value: 'explore'},
  {type: 'sequential', value: '->'},
  {type: 'agent', value: 'implement'}
])

// Test AST construction
expect(buildAST(tokens)).toMatchObject({
  type: 'sequence',
  steps: [
    {type: 'agent', name: 'explore'},
    {type: 'agent', name: 'implement'}
  ]
})

// Test graph creation
expect(astToGraph(ast).nodes.length).toBe(2)
expect(astToGraph(ast).edges.length).toBe(1)

// Test validation
expect(validateGraph(graph, tokens).valid).toBe(true)
```

## Best Practices

1. **Parse early** - Validate syntax before execution
2. **Fail fast** - Stop at first error with clear message
3. **Context matters** - Show surrounding code in errors
4. **Suggest fixes** - Provide actionable suggestions
5. **Test thoroughly** - Cover all syntax combinations

## See Also

- [executor.md](executor.md) - Graph execution
- [visualizer.md](visualizer.md) - Graph visualization
- [steering.md](steering.md) - Interactive control
- [../reference/syntax.md](../reference/best-practices.md) - Syntax reference
