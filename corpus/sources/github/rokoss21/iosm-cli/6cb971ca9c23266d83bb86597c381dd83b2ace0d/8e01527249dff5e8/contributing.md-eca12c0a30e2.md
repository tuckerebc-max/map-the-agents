# Contributing to iosm-cli

Thank you for your interest in contributing to `iosm-cli`! This guide will help you get started.

## Getting Started

### Prerequisites

- **Node.js** `>=20.6.0`
- **npm** (bundled with Node.js)
- **Git**

### Setup

```bash
# 1. Fork and clone the repository
git clone https://github.com/your-username/iosm-cli.git
cd iosm-cli

# 2. Install dependencies
npm install

# 3. Verify setup
npm run check    # Type-check
npm test         # Run tests
npm run build    # Build
```

### Development Workflow

```bash
# Start watch mode for development
npm run dev

# In another terminal, test your changes
node dist/cli.js

# Or link globally
npm link
iosm
```

## Making Changes

### Branch Naming

Use descriptive branch names:

```
feature/add-tool-xyz
fix/session-persistence-bug
docs/update-cli-reference
refactor/model-registry-cleanup
```

### Code Style

- **TypeScript** — All source code is TypeScript
- **ES Modules** — Use `import`/`export` (`"type": "module"` in package.json)
- **File extensions** — Use `.js` extensions in imports (TypeScript resolves them)
- **No default exports** in library code (except extensions which use `export default`)

### Adding a CLI Flag

1. Add the argument definition in `src/cli/args.ts`
2. Handle it in `src/main.ts`
3. Update `docs/cli-reference.md`
4. Update `README.md` if the feature is significant
5. Add tests in `test/args.test.ts`

### Adding a Built-in Tool

1. Create the tool in `src/core/tools/`
2. Register it in `src/core/tools/index.ts`
3. Export from `src/index.ts`
4. Add tests in `test/tools.test.ts`
5. Update documentation

### Adding an Extension Example

1. Create the extension in `examples/extensions/`
2. Add an entry to `examples/extensions/README.md`
3. Follow the existing patterns for hooks, tools, or UI

## Testing

### Running Tests

```bash
# Full suite
npm test

# Specific file
npm test -- test/tools.test.ts

# Pattern match
npm test -- --grep "session"

# Watch mode
npx vitest --watch
```

### Writing Tests

- Use [Vitest](https://vitest.dev/) for all tests
- Place test files in `test/` with `.test.ts` extension
- Use shared helpers from `test/utilities.ts`
- Place test fixtures in `test/fixtures/`

```typescript
import { describe, it, expect } from "vitest";

describe("MyFeature", () => {
  it("should handle the expected case", async () => {
    const result = await myFunction(input);
    expect(result).toBe(expected);
  });

  it("should handle edge cases", async () => {
    expect(() => myFunction(null)).toThrow();
  });
});
```

## Pull Request Process

1. **Create a feature branch** from `main`
2. **Make your changes** with clear, focused commits
3. **Run the checklist**:
   ```bash
   npm run check    # TypeScript type-check
   npm test         # All tests pass
   npm run build    # Build succeeds
   ```
4. **Update documentation** if needed
5. **Open a Pull Request** with a clear description
6. **Respond to feedback** from reviewers

### PR Description Template

```markdown
## What

Brief description of the change.

## Why

Motivation or issue being addressed.

## How

Technical approach taken.

## Testing

How the change was tested.
```

## Reporting Issues

When reporting issues, please include:

- **Node.js version** (`node --version`)
- **iosm-cli version** (`iosm --version`)
- **Operating system**
- **Steps to reproduce**
- **Expected vs actual behavior**
- **Error messages or logs** (if applicable)

## License

By contributing to `iosm-cli`, you agree that your contributions will be licensed under the [MIT License](./LICENSE).
