# Contributing to am-i-vibing

Thank you for your interest in contributing to am-i-vibing! This guide covers how to add new providers or update existing ones for AI coding tools detection.

## Provider Guidelines

### Research Requirements

Before adding a new provider, ensure you have:

1. **Verified Environment Variables**: Use actual environment variables from real usage, not speculation
2. **Tested Detection**: Confirm the detection method works in the actual tool
3. **Documented Source**: Note where you found the environment variable information

### Detection Method Priority

Use detection methods in this order of preference:

1. **Environment Variables (String)**: Simple presence check. Use if there is a unique variable that indicates the tool's presence.

   ```typescript
   envVars: ["TOOL_SPECIFIC_VAR"]
   ```

2. **Environment Variables (Tuple)**: Name/value validation. Use if the variable name is generic but the value is specific to the tool.

   ```typescript
   envVars: [["TERM_PROGRAM", "tool-name"]]
   ```

3. **Environment Variables (Groups)**: Complex logical combinations using `all`, `any`, and `none`.

   ```typescript
   envVars: [{ all: [["VAR1", "value1"], "VAR2"] }]
   ```

4. **Process Tree Analysis**: For tools that don't set unique environment variables. Do not use unless environment variables are not available or reliable.

   ```typescript
   processChecks: ["tool-process-name"]
   ```

5. **Custom Detectors**: Only for complex checks
   ```typescript
   customDetectors: [() => {
     // Complex detection logic
     return Boolean(condition);
   }]
   ```

### Provider Categories

Classify your provider correctly:

- **`agent`**: Agent can execute commands autonomously
- **`interactive`**: User is executing the command withing an AI-assisted environment
- **`hybrid`**: Can operate in both modes depending on context, and we cannot determine which mode is active

### Environment Variable Guidelines

#### String Detection

Use for unique variables that indicate the tool's presence:

```typescript
envVars: ["UNIQUE_TOOL_VAR"]
```

#### Tuple Detection

Use when you need to validate both name and value:

```typescript
envVars: [["GENERIC_VAR", "specific-value"]]
```

#### Environment Variable Groups

Use for complex logical combinations:

- **any**: ANY of these conditions can match (OR logic) - this is the default behavior
- **all**: ALL of these conditions must match (AND logic)  
- **none**: NONE of these conditions should match (NOT logic)

```typescript
// All conditions must be true
envVars: [{ all: [["VAR1", "value1"], "VAR2"] }]

// Any condition can be true (default behavior, rarely needs explicit syntax)
envVars: [{ any: [["VAR1", "value1"], "VAR2"] }]

// None of these should be true (exclusion)
envVars: [{ none: [["VAR1", "unwanted-value"]] }]

// Complex combinations
envVars: [{ 
  all: [["TERM_PROGRAM", "tool"], "REQUIRED_VAR"],
  none: [["MODE", "interactive"]]
}]
```

### Provider Definition Template

```typescript
{
  id: 'tool-name',
  name: 'Tool Display Name',
  type: 'agent' | 'interactive' | 'hybrid',
  envVars?: ['ENV_VAR'] | [['ENV_VAR', 'value']] | [{ all: [...], any: [...], none: [...] }],
  processChecks?: ['process-name'],
  customDetectors?: [() => boolean]
}
```

### Real-World Examples

#### Simple Environment Variable

```typescript
{
  id: 'claude-code',
  name: 'Claude Code',
  type: 'agent',
  envVars: ['CLAUDECODE']
}
```

#### Tuple Detection

```typescript
{
  id: 'cursor',
  name: 'Cursor',
  type: 'interactive',
  envVars: ['CURSOR_TRACE_ID']
}
```

#### Multiple Conditions (ALL)

```typescript
{
  id: 'zed-agent',
  name: 'Zed Agent',
  type: 'agent',
  envVars: [
    {
      all: [
        ['TERM_PROGRAM', 'zed'],
        ['PAGER', 'cat']
      ]
    }
  ]
}
```

#### Complex Logic with ALL and NONE

```typescript
{
  id: 'bolt',
  name: 'Bolt.new',
  type: 'interactive',
  envVars: [
    {
      all: [['SHELL', '/bin/jsh']],
      none: ['npm_config_yes']
    }
  ]
}
```

#### Process Detection

```typescript
{
  id: 'aider',
  name: 'Aider',
  type: 'agent',
  envVars: ['AIDER_API_KEY'],
  processChecks: ['aider']
}
```

### Testing Your Provider

1. **Unit Tests**: Add tests in `test/detector.test.ts`

   ```typescript
   test("detects your-tool correctly", () => {
     const mockEnv = { YOUR_TOOL_VAR: "value" };
     const result = detectAgenticEnvironment(mockEnv);
     expect(result.id).toBe("your-tool");
     expect(result.isAgentic).toBe(true);
   });
   ```

2. **Real Environment Testing**: Test in the actual tool environment

   ```bash
   pnpm run cli
   pnpm run cli --debug
   ```

3. **False Positive Testing**: Ensure your detection doesn't trigger in other environments

### Common Pitfalls to Avoid

1. **Don't Guess**: Only use verified environment variables
2. **Avoid Generic Variables**: Don't use common variables like `TERM` or `PATH`
3. **Be Specific**: Use tuple detection for generic variable names
4. **Test Thoroughly**: Verify detection works and doesn't create false positives
5. **Document Sources**: Note where you found the environment variable information

### Submission Checklist

- [ ] Provider definition added to `src/providers.ts`
- [ ] Unit tests added to `test/detector.test.ts`
- [ ] Tested in real environment
- [ ] Tested for false positives
- [ ] Documentation updated if needed
- [ ] Changeset created (`pnpm changeset`)

## Development Setup

```bash
# Install dependencies
pnpm install

# Run tests
pnpm run test

# Test CLI
pnpm run cli

# Type check
pnpm run check

# Build
pnpm run build
```

## Creating a Changeset

After making changes, create a changeset to document your contribution:

```bash
pnpm changeset
```

Choose the appropriate change type:

- **patch**: Bug fixes, small provider updates
- **minor**: New providers, feature enhancements
- **major**: Breaking changes (rare)

## Questions or Need Help?

- Check existing providers in `src/providers.ts` for examples
- Review test patterns in `test/detector.test.ts`
- Open an issue for questions about detection methods
- Test your changes thoroughly before submitting

Thank you for helping improve am-i-vibing's detection capabilities!
