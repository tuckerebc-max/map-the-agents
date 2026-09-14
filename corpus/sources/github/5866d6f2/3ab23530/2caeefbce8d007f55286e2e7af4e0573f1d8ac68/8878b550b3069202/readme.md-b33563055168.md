# Software Development Prompt Library

> **⚠️ Work in Progress**: 
> - The library contains prompts at various stages of development
> - Prompts within the [Post-Scaffolding Sprint Workflow](workflows/assistant-specific/aider/sprint/post-scaffolding-sprint-workflow-chain.md) have been most rigorously tested
> - Many individual prompts are not yet part of a defined workflow and have not been fully tested
> - Ongoing development and validation is in progress

A collection of AI-powered prompts designed to streamline software development workflows. Each prompt is crafted to work directly with AI coding assistants, providing consistent guidance across different development phases.

## Core Features

- **AI Workflow Chains**
  - Structured sequences of connected prompts
  - Input/output dependencies between phases
  - Verification points for chain integrity
  - Systematic development processes
  - Progress tracking and validation

- **Project Initialization**
  - Requirements generation and refinement
  - Technology stack selection with BOM
  - Architecture design
  - Project scaffolding

- **Development Support**
  - Feature story creation
  - Code health analysis
  - System visualization
  - Unit test generation

- **Documentation**
  - README generation
  - Code explanation and tutoring

## Using the Library

### Individual Prompts
1. Navigate to the relevant prompt in `/prompts` directory
2. Share the raw URL with your AI assistant
3. Begin using the workflow

Each prompt has two components:
- `[prompt-name].md` - AI instructions
- `[prompt-name].meta.md` - Usage documentation

### Workflow Chains
1. Review available workflows in `/workflows` directory
2. Choose a workflow that matches your development phase
3. Follow the chain sequence, ensuring each phase's:
   - Required inputs are available
   - Outputs are validated
   - Dependencies are satisfied

## Project Structure

```plaintext
software-dev-prompt-library/
├── prompts/
│   ├── architecture/
│   ├── documentation/
│   ├── planning/
│   ├── testing/
│   └── visualization/
├── workflows/
│   └── [workflow guides]
└── docs/
    ├── getting-started.md
    └── prompt-guidelines.md
```
## Key Benefits

- Streamlined development workflows from project inception to maintenance
- Intelligent adaptation to different programming languages and frameworks
- Focused, single-purpose prompts that chain together for complex tasks
- Built-in validation and best practices
- Promotes consistent development patterns across teams
- Reduces cognitive load during development tasks
- Enables rapid prototyping and iteration

## Getting Started

1. Review [getting-started.md](docs/guides/getting-started.md) to understand available workflows
2. Choose your starting point:
   - New project? Start with requirements generation
   - Existing project? Begin with code health analysis
3. Follow the workflow guides for your chosen development path
4. Chain prompts together as needed for more complex tasks

## Contributing

1. Review [prompt-guidelines.md](docs/guides/prompt-guidelines.md) for prompt structure and principles
2. Each prompt needs both implementation (.md) and documentation (.meta.md)
3. Test prompts across different AI models and project types
4. Submit additions that focus on specific development tasks
5. Maintain language and framework agnosticism
