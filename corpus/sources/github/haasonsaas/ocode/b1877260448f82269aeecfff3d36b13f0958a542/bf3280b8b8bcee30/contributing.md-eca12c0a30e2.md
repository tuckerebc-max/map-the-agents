# Contributing to OCode

Thank you for your interest in contributing to OCode! This guide will help you get started.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct: be respectful, inclusive, and constructive in all interactions.

## How to Contribute

### Reporting Issues

1. **Check existing issues** first to avoid duplicates
2. Use the issue templates when available
3. Include:
   - Clear description of the problem
   - Steps to reproduce
   - Expected vs actual behavior
   - System information (OS, Python version, Ollama version)
   - Relevant logs or error messages

### Suggesting Features

1. Open a discussion in the [Ideas category](https://github.com/haasonsaas/ocode/discussions)
2. Describe the use case and benefits
3. Consider implementation complexity
4. Be open to feedback and alternatives

### Contributing Code

#### 1. Fork and Clone

```bash
# Fork on GitHub, then:
git clone https://github.com/YOUR-USERNAME/ocode.git
cd ocode
git remote add upstream https://github.com/haasonsaas/ocode.git
```

#### 2. Set Up Development Environment

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in development mode
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

#### 3. Create a Branch

```bash
# Update main branch
git checkout main
git pull upstream main

# Create feature branch
git checkout -b feature/your-feature-name
# Or for fixes:
git checkout -b fix/issue-description
```

#### 4. Make Changes

Follow these guidelines:

##### Code Style
- Follow PEP 8 (enforced by Black formatter)
- Use type hints where appropriate
- Maximum line length: 88 characters
- Use descriptive variable names

##### Documentation
- Add docstrings to all public functions/classes
- Use Google docstring style
- Update relevant documentation
- Include examples where helpful

##### Testing
- Write tests for new functionality
- Ensure all tests pass
- Maintain or improve code coverage
- Test edge cases

##### Commits
- Use clear, descriptive commit messages
- Follow conventional commits format:
  ```
  type(scope): subject

  body (optional)

  footer (optional)
  ```
- Types: feat, fix, docs, style, refactor, test, chore

#### 5. Run Quality Checks

```bash
# Format code
make format

# Run linters
make lint

# Run tests
make test

# Run all checks
make ci
```

#### 6. Submit Pull Request

1. Push your branch:
   ```bash
   git push origin feature/your-feature-name
   ```

2. Create PR on GitHub with:
   - Clear title and description
   - Link to related issues
   - List of changes made
   - Screenshots if UI changes
   - Test results

3. Address review feedback promptly

## Development Guidelines

### Project Structure

```
ocode/
├── ocode_python/
│   ├── core/          # Core engine and CLI
│   ├── tools/         # Tool implementations
│   ├── languages/     # Language analyzers
│   ├── mcp/          # MCP integration
│   └── utils/        # Utilities
├── tests/
│   ├── unit/         # Unit tests
│   ├── integration/  # Integration tests
│   └── fixtures/     # Test data
├── docs/             # Documentation
└── examples/         # Example code
```

### Adding a New Tool

1. Create tool file in `ocode_python/tools/`:
   ```python
   from .base import Tool, ToolDefinition, ToolParameter, ToolResult

   class YourTool(Tool):
       @property
       def definition(self) -> ToolDefinition:
           return ToolDefinition(
               name="your_tool",
               description="Clear description",
               parameters=[
                   ToolParameter(
                       name="param",
                       description="Parameter description",
                       type="string",
                       required=True
                   )
               ],
               category="appropriate_category"
           )

       async def execute(self, **kwargs) -> ToolResult:
           try:
               # Implementation
               return ToolResult(
                   success=True,
                   output="Result"
               )
           except Exception as e:
               return ToolResult(
                   success=False,
                   output="",
                   error=str(e)
               )
   ```

2. Register in `ToolRegistry.register_core_tools()`

3. Add tests in `tests/unit/test_your_tool.py`

4. Document in `docs/user-guide/tool-reference/`

### Adding Language Support

1. Create analyzer in `ocode_python/languages/`:
   ```python
   from .base import LanguageAnalyzer, Symbol

   class YourLangAnalyzer(LanguageAnalyzer):
       file_extensions = [".ext"]

       def extract_symbols(self, content: str) -> List[Symbol]:
           # Parse and extract symbols

       def extract_imports(self, content: str) -> List[str]:
           # Extract imports
   ```

2. Register in language registry

3. Add tests with sample files

4. Update documentation

### Writing Tests

#### Unit Tests
```python
import pytest
from ocode_python.tools.your_tool import YourTool

@pytest.mark.asyncio
async def test_your_tool_success():
    tool = YourTool()
    result = await tool.execute(param="value")
    assert result.success
    assert "expected" in result.output

@pytest.mark.asyncio
async def test_your_tool_error():
    tool = YourTool()
    result = await tool.execute(param="invalid")
    assert not result.success
    assert result.error
```

#### Integration Tests
- Test component interactions
- Use real file operations when needed
- Mock external services

#### Test Markers
- `@pytest.mark.unit` - Unit tests
- `@pytest.mark.integration` - Integration tests
- `@pytest.mark.slow` - Slow tests
- `@pytest.mark.security` - Security tests

### Documentation

#### Code Documentation
```python
def process_data(data: List[Dict[str, Any]],
                options: ProcessOptions) -> ProcessResult:
    """Process data according to specified options.

    Args:
        data: List of data items to process
        options: Processing configuration options

    Returns:
        ProcessResult containing processed data and metadata

    Raises:
        ValueError: If data is empty or invalid
        ProcessingError: If processing fails

    Example:
        >>> result = process_data([{"id": 1}], options)
        >>> print(result.count)
        1
    """
```

#### User Documentation
- Clear, concise language
- Practical examples
- Common use cases
- Troubleshooting section

### Performance Considerations

1. **Async Operations**: Use async/await for I/O
2. **Streaming**: Stream large responses
3. **Caching**: Cache expensive operations
4. **Memory**: Avoid loading large files entirely
5. **Concurrency**: Use asyncio for parallel operations

### Security Guidelines

1. **Input Validation**: Always validate user input
2. **Path Security**: Use path validation utilities
3. **Command Injection**: Sanitize shell commands
4. **Permissions**: Respect security configuration
5. **Secrets**: Never log sensitive information

## Pull Request Process

1. **Pre-submission Checklist**:
   - [ ] Code follows style guidelines
   - [ ] Tests pass locally
   - [ ] Documentation updated
   - [ ] Commits are clean and descriptive
   - [ ] PR description is complete

2. **Review Process**:
   - Automated checks must pass
   - At least one maintainer review
   - Address feedback promptly
   - Keep PR focused and manageable

3. **Merge Requirements**:
   - All tests passing
   - Documentation complete
   - No unresolved conversations
   - Approved by maintainer

## Release Process

1. **Version Numbering**: Semantic versioning (MAJOR.MINOR.PATCH)
2. **Changelog**: Update CHANGELOG.md following Keep a Changelog
3. **Testing**: Full test suite passes
4. **Documentation**: All docs updated
5. **Tag**: Create git tag for release
6. **Package**: Build and publish to PyPI

## Getting Help

- **Discord**: Join our community server
- **Discussions**: GitHub Discussions for questions
- **Issues**: GitHub Issues for bugs
- **Email**: jonathan@haasonsaas.com for security issues

## Recognition

Contributors are recognized in:
- CONTRIBUTORS.md file
- Release notes
- Project documentation

## License

By contributing, you agree that your contributions will be licensed under the project's AGPL-3.0 license.
