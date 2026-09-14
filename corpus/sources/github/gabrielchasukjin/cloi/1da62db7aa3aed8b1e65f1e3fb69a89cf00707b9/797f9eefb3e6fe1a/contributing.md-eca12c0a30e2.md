# Contributing to Cloi

Thank you for your interest in contributing to Cloi! This document provides guidelines and instructions for contributing to the project. Please read it carefully before submitting any contributions.

## Code of Conduct

By participating in this project, you agree to abide by our Code of Conduct. Please be respectful and considerate of others in all interactions related to this project.

### Our Pledge
We are committed to making participation in this project a harassment-free experience for everyone, regardless of age, body size, disability, ethnicity, gender identity and expression, level of experience, education, socio-economic status, nationality, personal appearance, race, religion, or sexual identity and orientation.

### Our Standards
Examples of behavior that contributes to a positive environment include:
- Using welcoming and inclusive language
- Being respectful of differing viewpoints and experiences
- Gracefully accepting constructive criticism
- Focusing on what is best for the community
- Showing empathy towards other community members

Examples of unacceptable behavior include:
- The use of sexualized language or imagery and unwelcome sexual attention or advances
- Trolling, insulting/derogatory comments, and personal or political attacks
- Public or private harassment
- Publishing others' private information without explicit permission
- Other conduct which could reasonably be considered inappropriate in a professional setting

### Enforcement
- Project maintainers have the right and responsibility to remove, edit, or reject comments, commits, code, and other contributions that are not aligned with this Code of Conduct
- Project maintainers who do not follow the Code of Conduct may be removed from the project team

### Reporting
If you experience or witness unacceptable behavior, or have any other concerns, please report it by contacting the project maintainers at [contact email/issue tracker].

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Git
- A GitHub account
- Basic understanding of command-line tools

### Development Setup
1. Fork the repository
2. Clone your fork:
```bash
git clone https://github.com/YOUR-USERNAME/cloi.git
cd cloi
```

3. Set up the development environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -e ".[dev]"
```

4. Install pre-commit hooks:
```bash
pre-commit install
```

## Development Workflow

### Branching Strategy
- `main`: Production-ready code
- `develop`: Development branch
- Feature branches: `feature/your-feature-name`
- Bug fix branches: `fix/issue-description`
- Documentation branches: `docs/description`

### Making Changes
1. Create a new branch for your changes:
```bash
git checkout -b feature/your-feature-name
```

2. Make your changes following our coding standards
3. Write or update tests as needed
4. Run tests locally:
```bash
pytest
```

5. Commit your changes with clear, descriptive commit messages:
```bash
git commit -m "feat: add new feature X"
```

### Commit Message Format
We follow the [Conventional Commits](https://www.conventionalcommits.org/) specification:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, etc.)
- `refactor`: Code changes that neither fix bugs nor add features
- `test`: Adding or modifying tests
- `chore`: Changes to build process or auxiliary tools

### Pull Request Process
1. Update the README.md with details of changes if needed
2. Update the documentation if you're changing functionality
3. The PR will be merged once you have the sign-off of at least one maintainer
4. Ensure all CI checks pass

## Coding Standards

### Python Code Style
- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) guidelines
- Use type hints for all function parameters and return values
- Maximum line length: 88 characters (Black formatter default)
- Use Black for code formatting
- Use isort for import sorting
- Use flake8 for linting

### Documentation
- Use Google-style docstrings
- Include examples in docstrings where appropriate
- Keep README.md and other documentation up to date
- Document all public APIs

### Testing
- Write unit tests for all new features
- Maintain or improve test coverage
- Use pytest for testing
- Include both positive and negative test cases

## Project Structure
```
bin/
  ├── index.js          # Main CLI entry point
  └── cloi-setup.cjs    # Installation setup script
src/
  ├── ui/               # User interface components
  │   ├── boxen.js      # Boxed UI components
  │   └── prompt.js     # User prompts and input handling
  ├── core/             # Core functionality
  │   ├── command.js    # Command execution
  │   ├── history.js    # Shell history management
  │   ├── llm.js        # LLM interaction and analysis
  │   └── patch.js      # Code patching utilities
  ├── utils/            # Utility functions
  │   ├── file.js       # File operations
  │   └── traceback.js  # Error traceback parsing
  └── cli/              # CLI implementation
      └── index.js      # Main CLI logic
```

## License Considerations

### CC BY-NC 4.0 License
By contributing to this project, you agree that your contributions will be licensed under the [Creative Commons Attribution-NonCommercial 4.0 International License](https://creativecommons.org/licenses/by-nc/4.0/).

Key points:
- Your contributions must be your own work
- You retain copyright to your contributions
- You grant the project a non-exclusive license to use your contributions
- The project cannot be used for commercial purposes
- All users must provide attribution

### Third-Party Code
- Do not include code from other projects without proper attribution
- Ensure any third-party code is compatible with CC BY-NC 4.0
- Document all third-party dependencies

## Getting Help

- Open an issue for bug reports or feature requests
- Join our community chat for discussions
- Check existing issues and pull requests before creating new ones

## Recognition

Contributors will be recognized in the following ways:
- Listed in the project's README.md
- Mentioned in release notes
- Given credit in documentation where appropriate

## Release Process

1. Version bump (following semantic versioning)
2. Update CHANGELOG.md
3. Create release notes
4. Tag the release
5. Update documentation

## Additional Resources

- [Python Documentation](https://docs.python.org/)
- [GitHub Flow](https://guides.github.com/introduction/flow/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [Black Code Style](https://black.readthedocs.io/)
- [Pytest Documentation](https://docs.pytest.org/)

Thank you for contributing to Cloi!