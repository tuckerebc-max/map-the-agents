# OCode Documentation

Welcome to the OCode documentation. This comprehensive guide covers everything from getting started to advanced development.

## Quick Links

- **New to OCode?** Start with the [Quickstart Guide](getting-started/quickstart.md)
- **Need help with tools?** See the [Tool Reference](user-guide/tool-reference/overview.md)
- **Configuring OCode?** Check the [Configuration Guide](user-guide/configuration.md)
- **Want to contribute?** Read our [Contributing Guide](../CONTRIBUTING.md)

## Documentation Structure

### Getting Started
- [Quickstart Guide](getting-started/quickstart.md) - Get up and running in 5 minutes
- [Installation Guide](getting-started/installation.md) - Detailed installation instructions
- [First Project](getting-started/first-project.md) - Your first OCode project walkthrough
- [Troubleshooting](getting-started/troubleshooting.md) - Common issues and solutions

### User Guide
- [Configuration](user-guide/configuration.md) - Complete configuration reference
- [Tool Reference](user-guide/tool-reference/overview.md) - All available tools
  - [File Operations](user-guide/tool-reference/file-operations.md)
  - [Text Processing](user-guide/tool-reference/text-processing.md)
  - [Data Processing](user-guide/tool-reference/data-processing.md)
  - [System Operations](user-guide/tool-reference/system-operations.md)
  - [Development Tools](user-guide/tool-reference/development-tools.md)
- [Workflows](user-guide/workflows.md) - Common workflows and patterns
- [Best Practices](user-guide/best-practices.md) - Tips for effective usage

### Developer Guide
- [Architecture](developer-guide/architecture.md) - System architecture overview
- [Creating Tools](developer-guide/creating-tools.md) - How to build custom tools
- [Language Support](developer-guide/language-support.md) - Adding language analyzers
- [Testing](developer-guide/testing.md) - Testing strategies and patterns
- [Contributing](../CONTRIBUTING.md) - Contribution guidelines

### API Reference
- [Tools API](api-reference/tools.md) - Complete tool system API
- [Engine API](api-reference/engine.md) - Core engine API
- [Context Manager API](api-reference/context-manager.md) - Context system API
- [MCP Protocol](api-reference/mcp-protocol.md) - Model Context Protocol

### Advanced Topics
- [Security](advanced/security.md) - Security model and configuration
- [Performance](advanced/performance.md) - Performance optimization
- [MCP Integration](advanced/mcp-integration.md) - Advanced MCP usage
- [Deployment](advanced/deployment.md) - Production deployment

### Technical Documentation
- [Timeout Analysis](timeout-analysis.md) - Timeout implementation across codebase
- [Reliability Improvements](reliability-improvements.md) - Error handling improvements
- [Manual CLI Testing](manual-cli-testing.md) - CLI testing procedures

## Key Concepts

### Tools
OCode provides 19+ specialized tools for various tasks:
- **File Operations**: Read, write, edit, search files
- **Text Processing**: Grep, diff, sort, analyze text
- **System Tools**: Execute commands, manage environment
- **Development**: Git operations, testing, notebooks
- **Analysis**: Architecture analysis, extended reasoning

### Context Management
OCode intelligently analyzes your project to provide relevant context:
- Automatic file discovery and ranking
- Language-specific symbol extraction
- Dependency tracking
- Git integration

### Security Model
Multi-layer security system:
- Path-based restrictions
- Command validation
- Permission system
- User confirmation for dangerous operations

## Getting Help

### In OCode
```bash
# General help
ocode -p "What can you do?"

# Tool-specific help
ocode -p "How do I use the grep tool?"

# Feature help
ocode -p "How do I search for text in files?"
```

### Community
- [GitHub Discussions](https://github.com/haasonsaas/ocode/discussions) - Ask questions
- [Issue Tracker](https://github.com/haasonsaas/ocode/issues) - Report bugs
- [Discord Server](https://discord.gg/ocode) - Live chat with community

## Contributing to Documentation

We welcome documentation improvements! When contributing:

1. **Follow Structure**: Place docs in appropriate directories
2. **Be Clear**: Write for your target audience (users vs developers)
3. **Include Examples**: Show, don't just tell
4. **Stay Current**: Update docs when features change
5. **Test Code**: Ensure all code examples work

See our [Contributing Guide](../CONTRIBUTING.md) for details.

## Version

This documentation is for OCode v2.0+. For older versions, see the [releases page](https://github.com/haasonsaas/ocode/releases).
