# Workflow Templates

Workflow templates are pre-defined "recipes" for common orchestration patterns. They are DAGs configured via YAML files which are converted into beads epics and tasks.

---

## Built-in Templates

| Template | Description |
|----------|-------------|
| **Cook** | Sequential task execution with code review |
| **Research to Tasks** | Research a topic and convert findings to actionable tasks |
| **Debate** | Multi-agent debate for exploring solutions |
| **Mediated Investigation** | Structured investigation with mediator |
| **Research Proposal** | Collaborative proposal development |
| **Quick Plan** | Rapid planning and task breakdown |

List all available templates with:

```bash
perles workflows
```

---

## Typical Workflow

A common development cycle uses multiple workflows in sequence:

### 1. Research Proposal

Start by generating a research document or proposal:

- Launch the **Research Proposal** workflow
- Provide a topic or problem description
- The coordinator assigns workers to research and draft a proposal
- Output: a proposal document in your configured `document_path`

### 2. Research to Tasks

Break down the proposal into actionable work:

- Launch **Research to Tasks** with the proposal document
- Workers analyze the proposal and create beads epics and tasks
- Output: a structured epic with prioritized tasks

### 3. Cook

Execute the tasks with code review:

- Launch **Cook** with the epic from step 2
- The coordinator assigns tasks to workers sequentially
- Each task goes through implementation, review, and commit phases
- Workers automatically cycle through phases with built-in code review

---

## Cook Workflow Details

Cook is the primary implementation workflow. It processes an existing epic's tasks in order:

1. **Task Assignment**: Coordinator assigns the next task to an available worker
2. **Implementation**: Worker implements the task (`impl` phase)
3. **Review**: Worker reviews their own work or another worker reviews (`review` phase)
4. **Feedback**: If review has issues, worker addresses feedback (`feedback` phase)
5. **Commit**: Worker commits changes (`commit` phase)
6. **Next Task**: Coordinator moves to the next task

Workers that run out of context are automatically replaced with fresh instances.
