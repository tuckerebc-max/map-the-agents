# palm1r/qodeassist

Status: distilled - Freshness: current
Catalog classes: agent
Origins: alltheagents.org-backing - Projects: none
Latest snapshot: commit 558208df21ce @ 68a0798e723b5f74

## Summary (orientation draft, not independently verified)

QodeAssist is a GPL-3.0 Qt Creator plugin providing AI coding assistance (completion, chat, refactoring, agent tools, skills, MCP server/client, ACP agents) for C++/QML; the project is now archived by its author. Evidence is documentation-only from README and docs pages. Evidence coverage: 123 of 157 packet slices were shown to the model; the rest were withheld by the prompt budget.

## Source coverage

Source coverage (partial): 6 of 15 candidate file(s) selected (selection incomplete); repository tree complete. Claims by basis: 20 documented, 0 code-inspected. A current commit is not the same as complete source coverage.

## Facets

20 claim(s) across 11 facet(s); 2 facet(s) unknown.

- specifications (2 claim(s)):
  - [observation/documented] QodeAssist is licensed under GPL-3.0 with additional attribution terms under GPLv3 Section 7(b), and a separate commercial license is offered for proprietary use. -- evidence: [README.md#L532-L534](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L532-L534), [README.md#L545-L547](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L545-L547)
  - [observation/documented] The README states the project is archived: the author shut it down after copyright notices were removed without permission. -- evidence: [README.md#L10-L15](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L10-L15)
- components (1 claim(s)):
  - [observation/documented] The plugin adds AI code completion for C++ and QML, multi-panel chat, inline quick refactoring, agent tools, skills, and MCP server/client capabilities to Qt Creator. -- evidence: [README.md#L18-L18](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L18-L18), [README.md#L37-L47](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L37-L47)
- design-choices (2 claim(s)):
  - [observation/documented] Code completion offers two trigger modes: hint-based (indicator after typing 3+ characters, suited to paid APIs to avoid charges) and automatic (default, suited to local models). -- evidence: [README.md#L206-L206](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L206-L206), [README.md#L208-L213](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L208-L213), [README.md#L215-L219](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L215-L219)
  - [observation/documented] Prompt composition differs by model type: FIM models get a template with prefix/suffix code context, while non-FIM chat models get a system prompt with formatting instructions plus a user completion request. -- evidence: [README.md#L315-L332](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L315-L332), [README.md#L424-L431](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L424-L431), [README.md#L339-L359](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L339-L359)
- workflows (2 claim(s)):
  - [observation/documented] Repository development practice: contributors should follow the QML Coding Guide, use the project's .clang-format for C++, and run formatting before submitting PRs; detailed guidelines live in .cursor/rules.mdc. -- evidence: [README.md#L522-L524](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L522-L524), [README.md#L528-L528](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L528-L528)
  - [observation/documented] Repository development practice: build steps are mkdir build, then cmake with CMAKE_PREFIX_PATH pointing at Qt Creator and RelWithDebInfo, followed by cmake --build. -- evidence: [README.md#L507-L510](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L507-L510), [README.md#L501-L503](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L501-L503), [README.md#L512-L516](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L512-L516)
- skills-patterns (2 claim(s)):
  - [observation/documented] Agent Skills follow the open agentskills.io format: a folder with a SKILL.md containing YAML frontmatter (name, description) plus Markdown instructions, discovered from .qodeassist/skills/ and .claude/skills/ plus global directories. -- evidence: [README.md#L261-L261](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L261-L261), [README.md#L279-L281](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L279-L281), [README.md#L259-L259](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L259-L259)
  - [observation/documented] Skills are used in chat three ways: automatically via a load_skill tool (requires tool-calling models), explicitly via a / command, or always-on when frontmatter sets metadata always-on to true. -- evidence: [README.md#L285-L288](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L285-L288)
- interfaces (4 claim(s)):
  - [observation/documented] Chat and Quick Refactor can invoke tools such as list_project_files, read_file, edit_file, build_project, get_issues_list, execute_terminal_command (with confirmation), and todo_tool, each individually toggleable in settings. -- evidence: [README.md#L244-L255](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L244-L255), [README.md#L242-L242](https://github.com/Palm1r/QodeAssist/blob/558208df21ce8dfd844fdc0d7d07a75a2fb5d5a5/README.md#L242-L242)
More evidence: [full detail](qodeassist.detail.md)

Metadata and full claim list: [full detail](qodeassist.detail.md)
Human notes ([notes](qodeassist.notes.md), never overwritten by build)

[Back to map index](../../index.md)
