# Collaboration Guide

Welcome to Claude Autopilot! This guide outlines how to contribute to the project and collaborate effectively with the community.

## 🤝 Getting Started

### Prerequisites
- **Node.js 16+** and **npm**
- **VS Code** or **Cursor** IDE
- **TypeScript** knowledge
- **Claude Code CLI** installed
- **Python 3.8+** for PTY wrapper

### Development Setup
1. Fork the repository on GitHub
2. Clone your fork locally:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Claude-Autopilot.git
   cd Claude-Autopilot
   ```
3. Install dependencies:
   ```bash
   npm install
   ```
4. Build the extension:
   ```bash
   npm run compile
   ```
5. Press `F5` in VS Code to launch the Extension Development Host

## 📋 How to Contribute

### 🐛 Bug Reports
1. Check [existing issues](https://github.com/benbasha/Claude-Autopilot/issues) first
2. Create a new issue with:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - Environment details (OS, VS Code version, Claude CLI version)
   - Screenshots if applicable

### ✨ Feature Requests
1. Check [discussions](https://github.com/benbasha/Claude-Autopilot/discussions) for similar ideas
2. Create a discussion or issue with:
   - Use case description
   - Proposed solution
   - Alternative approaches considered
   - Implementation complexity estimate

### 🔧 Code Contributions

#### Branch Strategy
- `main` - Stable releases
- `develop` - Integration branch for new features
- `feature/feature-name` - Individual feature branches
- `fix/issue-number` - Bug fix branches

#### Pull Request Process
1. Create a feature branch from `develop`:
   ```bash
   git checkout develop
   git pull origin develop
   git checkout -b feature/your-feature-name
   ```

2. Make your changes following our coding standards
3. Test thoroughly:
   ```bash
   npm run compile
   npm run test # if tests exist
   ```

4. Commit with descriptive messages:
   ```bash
   git commit -m "Add auto-retry mechanism for failed Claude sessions

   - Implement exponential backoff for connection retries
   - Add configuration option for max retry attempts
   - Include retry status in UI feedback
   
   Fixes #123"
   ```

5. Push and create a pull request:
   ```bash
   git push origin feature/your-feature-name
   ```

6. Fill out the PR template with:
   - Description of changes
   - Testing performed
   - Screenshots for UI changes
   - Breaking changes (if any)

## 🏗️ Project Structure

```
src/
├── core/           # Core state management and configuration
├── claude/         # Claude CLI integration
├── queue/          # Message queue processing
├── services/       # External service integrations
├── ui/             # User interface (webview)
├── utils/          # Shared utilities
└── webview/        # HTML/CSS/JS for webview
```

### Key Files
- `src/extension.ts` - Main extension entry point
- `src/claude_pty_wrapper.py` - Python PTY wrapper
- `package.json` - Extension manifest and dependencies
- `CLAUDE.md` - Instructions for Claude Code assistance

## 📝 Coding Standards

### TypeScript
- Use TypeScript strict mode
- Prefer `interface` over `type` for object shapes
- Use meaningful variable and function names
- Add JSDoc comments for public APIs
- Follow existing naming conventions:
  - `camelCase` for variables and functions
  - `PascalCase` for classes and interfaces
  - `SCREAMING_SNAKE_CASE` for constants

### Architecture Principles
- **Modular Design**: Keep components focused and loosely coupled
- **Error Handling**: Comprehensive error handling with user-friendly messages
- **Configuration**: Make behavior configurable through VS Code settings
- **Logging**: Use the debug logging system for troubleshooting
- **Performance**: Optimize for responsiveness and memory usage

### Code Examples
```typescript
// Good: Clear interface with documentation
interface QueueMessage {
    id: string;
    content: string;
    timestamp: Date;
    status: 'pending' | 'processing' | 'completed' | 'failed';
}

// Good: Error handling with logging
async function processMessage(message: QueueMessage): Promise<void> {
    try {
        await claudeSession.sendMessage(message.content);
        debugLog(`✅ Message ${message.id} processed successfully`);
    } catch (error) {
        debugLog(`❌ Failed to process message ${message.id}: ${error}`);
        throw new ProcessingError(`Message processing failed: ${error.message}`);
    }
}
```

## 🧪 Testing

### Manual Testing
- Test core functionality: queue processing, session management
- Test error scenarios: network failures, Claude CLI issues
- Test on different platforms: Windows, macOS, Linux
- Test with different VS Code versions
- Verify configuration changes take effect

### Extension Testing
1. Use Extension Development Host (`F5`)
2. Test with real Claude CLI interactions
3. Verify webview functionality
4. Check that all commands work from Command Palette

## 📚 Documentation

### Required Documentation
- Update `README.md` for user-facing changes
- Update `CLAUDE.md` for architecture changes
- Add inline comments for complex logic
- Update configuration documentation

### Documentation Style
- Use clear, concise language
- Include code examples
- Add screenshots for UI changes
- Keep documentation up-to-date with code changes

## 🚀 Release Process

### Version Numbering
We follow [Semantic Versioning](https://semver.org/):
- `MAJOR.MINOR.PATCH`
- Major: Breaking changes
- Minor: New features (backward compatible)
- Patch: Bug fixes (backward compatible)

### Release Checklist
- [ ] All tests pass
- [ ] Documentation updated
- [ ] `CHANGELOG.md` updated
- [ ] Version bumped in `package.json`
- [ ] Extension tested in clean environment
- [ ] Release notes prepared

## 💬 Communication

### Channels
- **Issues**: Bug reports and feature requests
- **Discussions**: General questions and ideas
- **Pull Requests**: Code review and collaboration

### Response Times
- **Issues**: We aim to respond within 48 hours
- **Pull Requests**: Initial review within 72 hours
- **Security Issues**: Please report privately first

### Getting Help
1. Check the [README](README.md) and documentation
2. Search existing [issues](https://github.com/benbasha/Claude-Autopilot/issues)
3. Ask in [discussions](https://github.com/benbasha/Claude-Autopilot/discussions)
4. Create a new issue if needed

## 🙏 Recognition

Contributors are recognized in:
- `README.md` contributors section
- Release notes for significant contributions
- Git commit history and GitHub contributions graph

### Types of Contributions
- Code contributions
- Documentation improvements
- Bug reports and testing
- Feature suggestions and design feedback
- Community support and discussions

## 📄 License

By contributing to Claude Autopilot, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

Thank you for contributing to Claude Autopilot! Your contributions help make automated Claude Code processing accessible to everyone. 🚀