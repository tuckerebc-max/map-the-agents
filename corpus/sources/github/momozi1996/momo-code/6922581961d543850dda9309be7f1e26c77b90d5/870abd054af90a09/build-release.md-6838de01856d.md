# Build and Release Guide

## Development Setup

```bash
# Clone the repo
git clone https://github.com/momo-team/momo-code.git
cd momo-code

# Install dependencies
bun install

# Type check
bun typecheck

# Run tests
bun test
```

## Build

```bash
# Build all packages
bun run build

# Build specific package
bun run packages/opencode/script/build.ts
```

## Release Process

### Automated Release (GitHub Actions)

1. Go to **Actions > Release** in the GitHub repo
2. Click **Run workflow**
3. Select version bump type (patch/minor/major)
4. Click **Run workflow**

The workflow will:
1. Check for opencode brand leakage
2. Type-check the codebase
3. Build all packages
4. Bump version
5. Publish to npm
6. Create GitHub release

### Manual Release

```bash
# Set environment
export MOMO_NPM_TOKEN=your_token_here

# Run release script
bun run script/release.ts patch
```

## Platform Binaries

momo Code publishes platform-specific binaries:

| Platform | Architecture | Package |
|----------|-------------|---------|
| macOS | ARM64 | `momocode-darwin-arm64` |
| macOS | x64 | `momocode-darwin-x64` |
| Linux | ARM64 | `momocode-linux-arm64` |
| Linux | x64 | `momocode-linux-x64` |
| Windows | ARM64 | `momocode-win32-arm64` |
| Windows | x64 | `momocode-win32-x64` |

## Pre-release Checklist

- [ ] All tests pass
- [ ] TypeScript compiles without errors
- [ ] Rebrand check passes (`bash scripts/check-rebrand.sh`)
- [ ] CHANGELOG.md is updated
- [ ] Version is bumped correctly
- [ ] npm packages build successfully
- [ ] GitHub release notes are prepared
