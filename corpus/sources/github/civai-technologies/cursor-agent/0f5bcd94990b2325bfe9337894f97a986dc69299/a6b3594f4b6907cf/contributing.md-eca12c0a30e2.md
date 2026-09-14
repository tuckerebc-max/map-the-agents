# Contributing to Cursor Agent

Thank you for your interest in contributing to Cursor Agent! This document provides guidelines and instructions for contributing to the project.

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it before contributing.

## How Can I Contribute?

### Reporting Bugs

Before submitting a bug report:
- Check the [issue tracker](https://github.com/civai-technologies/cursor-agent/issues) to see if the issue has already been reported.
- If you're unable to find an open issue addressing the problem, open a new one.

When filing an issue, please include:
- A clear title and description of the bug
- Steps to reproduce the issue
- Expected behavior vs. actual behavior
- Environment details (OS, Python version, etc.)
- Any relevant screenshots or error messages

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion:
- Use a clear and descriptive title
- Provide a detailed description of the suggested enhancement
- Explain why this enhancement would be useful
- Include examples of how it would be used

### Pull Requests

1. Fork the repository
2. Create a new branch from `main` for your changes
3. Make your changes and commit them with clear, descriptive commit messages
4. Add or update tests as necessary
5. Update documentation as needed
6. Push your branch to your fork
7. Open a pull request against the `main` branch

#### Pull Request Guidelines

- Keep PRs focused on a single feature or fix
- Include tests for new functionality
- Update documentation for any changed functionality
- Follow the existing code style
- Make sure all tests pass before submitting your PR
- Reference related issues in your PR description

## Development Environment Setup

1. Fork and clone the repository
```bash
git clone https://github.com/civai-technologies/cursor-agent.git
cd cursor-agent
```

2. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. Install development dependencies
```bash
pip install -e ".[dev]"
```

4. Set up your API keys (for testing)
```bash
export ANTHROPIC_API_KEY="your_key_here"
export OPENAI_API_KEY="your_key_here"
```

## Testing

Run the test suite with:
```bash
python run_tests.py
```

To run specific tests:
```bash
python -m unittest tests.test_tools
```

## Coding Style

- Follow PEP 8 guidelines
- Use clear, descriptive variable and function names
- Add docstrings to all functions and classes
- Aim for a maximum line length of 100 characters
- Use type hints where appropriate

## Documentation

- Update the README.md with any new features, configuration options, or changes to usage
- Update or create examples for new functionality
- Add docstrings to your code for new functions, classes, or methods

## Review Process

- At least one project maintainer must approve a PR before it can be merged
- You may be asked to make changes to your PR based on feedback
- Once approved, the maintainer will merge your PR

## License

By contributing to Cursor Agent, you agree that your contributions will be licensed under the project's [MIT License](LICENSE).

## Questions?

If you have any questions or need help, please:
- Open an issue with the "question" label
- Reach out to Nifemi Alpine on Twitter [@usecodenaija](https://twitter.com/usecodenaija)

Thank you for contributing to make Cursor Agent better! 