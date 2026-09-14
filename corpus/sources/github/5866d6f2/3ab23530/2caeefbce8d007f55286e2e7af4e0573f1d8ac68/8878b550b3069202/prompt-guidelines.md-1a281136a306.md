# Prompt Guidelines

## Core Principles

1. Direct AI Instructions
- Write prompts as clear directives to the AI
- Focus on process steps and expected outputs
- Exclude metadata and human-focused documentation

2. Separation of Concerns
- Keep prompt instructions in `.md` files
- Store usage documentation in `.meta.md` files
- Maintain clean separation between AI and human documentation

3. Prompt Structure
- Start with clear workflow name
- List steps in logical order
- Define output formats
- Include validation rules

4. Output Formats
- Use consistent markdown structures
- Include file paths in code blocks
- Separate command-line instructions
- Maintain clear formatting

5. Workflow Chain Integration
- Design prompts to fit into chains
- Define clear inputs and outputs
- Include chain verification points
- Support systematic progress tracking

## Best Practices

1. Keep prompts focused
- One primary task per prompt
- Clear scope boundaries
- Minimal complexity
- Define chain position if applicable

2. Enable interaction
- Break complex decisions into steps
- Allow for user input and revision
- Provide clear options
- Support chain status checks

3. Maintain context
- Reference existing project files
- Consider current development stage
- Check for conflicts and dependencies
- Track chain dependencies

4. Support validation
- Include quality checks
- Verify compatibility
- Confirm requirements alignment
- Validate chain integrity

## Chain Integration

1. Input/Output Definition
- List required inputs
- Specify expected outputs
- Document dependencies
- Define validation criteria

2. Chain Position
- Identify preceding phases
- Document following phases
- Specify verification points
- Include progress tracking

3. Status Commands
- Provide status check commands
- Include progress indicators
- Support chain integrity checks
- Enable workflow validation

## Testing Prompts

1. Individual Testing
- Verify prompt works across different AI models
- Test with various project types and sizes
- Confirm output consistency
- Validate standalone operation

2. Chain Testing
- Test chain integration
- Verify input/output flow
- Validate chain integrity
- Confirm progress tracking
