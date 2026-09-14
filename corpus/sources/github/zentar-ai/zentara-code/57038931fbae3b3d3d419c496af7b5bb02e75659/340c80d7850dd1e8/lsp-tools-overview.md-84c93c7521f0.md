# LSP Tools Overview

This document provides a comprehensive overview of all Language Server Protocol (LSP) tools available in Zentara-Code These tools leverage the Language Server Protocol to provide intelligent, semantic-aware code analysis and manipulation capabilities.


## Overview

The LSP tools in this repository provide IDE-level code intelligence through the Language Server Protocol. They offer:

- **Semantic Understanding**: Unlike text-based tools, LSP tools understand code structure, scope, and relationships
- **Token Efficiency**: Provide precise information without reading entire files
- **Cross-Language Support**: Work with TypeScript, JavaScript, Python, Java, C#, Go, Rust, and more
- **Real-time Accuracy**: Information is always current with your codebase state

## Tool Categories

### 🔍 Core Discovery Tools (3 tools)

These are the primary tools for exploring and understanding codebases:

#### [`lsp_search_symbols`]
**Primary symbol discovery tool** - Finds symbols (classes, functions, methods, variables) with semantic precision.
- **Best for**: Finding specific symbols when you know their name
- **Advantage**: Takes you directly to symbol definitions, not just mentions
- **Use cases**: Class discovery, method finding, API exploration

#### [`lsp_get_document_symbols`]
**File structure analysis** - Provides a hierarchical outline of all symbols in a file.
- **Best for**: Understanding file architecture without reading entire content
- **Token efficient**: Complete structural map for fraction of read_file cost
- **Use cases**: Code review preparation, refactoring planning, file exploration

#### [`lsp_get_workspace_symbols`]
**Workspace-wide symbol search** - Searches for symbols across entire workspace by name.
- **Best for**: Finding symbols when you know the name but not location
- **Use cases**: Large codebase navigation, API discovery, refactoring preparation

### 🧭 Navigation Tools (6 tools)

Tools for navigating code relationships and understanding connections:

#### [`lsp_go_to_definition`]
**Core navigation tool** - Instantly navigates to symbol definitions.
- **Use cases**: Understanding implementations, tracing code flow, debugging

#### [`lsp_get_declaration`]
**Declaration navigation** - Finds where symbols are declared (imports, headers).
- **Use cases**: Import tracking, module dependency analysis, header navigation

#### [`lsp_get_type_definition`]
**Type navigation** - Navigates to type definitions rather than variable declarations.
- **Use cases**: Understanding data structures, API integration, type exploration

#### [`lsp_find_usages`] ⚠️ **MANDATORY**
**Usage analysis** - Finds all semantic references to a symbol.
- **CRITICAL**: Required before any code changes, debugging, or exploration
- **Use cases**: Impact analysis, refactoring preparation, dependency understanding

#### [`lsp_get_call_hierarchy`] ⚠️ **MANDATORY**
**Function relationship analysis** - Shows incoming and outgoing calls.
- **CRITICAL**: Required for debugging, error investigation, and understanding execution flows
- **Use cases**: Debugging, performance analysis, architectural understanding

#### [`lsp_find_implementations`]
**Implementation discovery** - Finds concrete implementations of interfaces/abstract classes.
- **Use cases**: Polymorphism analysis, architecture review, safe refactoring

### 📊 Analysis Tools (9 tools)

Tools for understanding code structure, types, and metadata:

#### [`lsp_get_symbol_children`] ⚠️ **MANDATORY**
**Symbol structure exploration** - Returns children of specific symbols with configurable depth.
- **CRITICAL**: Must use before `lsp_get_symbol_code_snippet` to understand structure
- **Use cases**: Class analysis, interface exploration, progressive code discovery

#### [`lsp_get_symbol_code_snippet`]
**Code extraction with enrichment** - Retrieves code snippets with call hierarchy and usage info.
- **⚠️ TOKEN-EXPENSIVE**: Use only after structure analysis with `lsp_get_symbol_children`
- **Use cases**: Detailed code examination, refactoring preparation, comprehensive analysis

#### [`lsp_get_hover_info`]
**Symbol metadata** - Retrieves rich contextual information (types, documentation).
- **Use cases**: API understanding, type verification, documentation access

#### [`lsp_get_completions`]
**Intelligent code completion** - Provides context-aware completion suggestions.
- **Use cases**: Code generation, API discovery, error prevention

#### [`lsp_get_signature_help`]
**Function signature assistance** - Provides detailed help for function parameters.
- **Use cases**: Function call assistance, API exploration, parameter validation

#### [`lsp_get_type_hierarchy`]
**Inheritance analysis** - Explores class/type inheritance hierarchies.
- **Use cases**: OOP design analysis, refactoring planning, architecture understanding

#### [`lsp_get_code_actions`]
**Refactoring suggestions** - Provides context-aware code actions and quick fixes.
- **Use cases**: Error resolution, code quality improvement, refactoring discovery

#### [`lsp_get_document_highlights`]
**In-file symbol highlighting** - Highlights all occurrences of a symbol within a file.
- **Use cases**: Local variable tracking, focused refactoring, scope visualization

#### [`lsp_get_symbols_overview`]
**Multi-file symbol overview** - Gets symbol overview for files or directories.
- **Use cases**: Code exploration, architectural analysis, API discovery

### 🔧 Code Modification Tools (4 tools)

Tools for making precise code changes:

#### [`lsp_rename`]
**Safe symbol renaming** - Performs semantic rename across entire workspace.
- **Use cases**: Symbol refactoring, API evolution, consistency enforcement

#### [`lsp_insert_before_symbol`]
**Precise insertion before symbols** - Inserts content before symbol definitions.
- **Use cases**: Documentation addition, decorator insertion, import management

#### [`lsp_insert_after_symbol`]
**Precise insertion after symbols** - Inserts content after symbol definitions.
- **Use cases**: Function extension, method chaining, code generation

#### [`lsp_replace_symbol_body`]
**Symbol body replacement** - Replaces entire symbol implementations.
- **Use cases**: Complete rewrites, algorithm replacement, bug fixes

### 🔬 Advanced Analysis Tools (3 tools)

Specialized tools for detailed code analysis:

#### [`lsp_get_semantic_tokens`]
**Token-level semantic analysis** - Provides detailed semantic classification of every token.
- **Use cases**: Code analysis tools, custom syntax highlighting, metrics collection

#### [`lsp_get_code_lens`]
**Contextual code information** - Retrieves actionable information interleaved with code.
- **Use cases**: Test management, reference analysis, quick actions

#### [`lsp_get_selection_range`]
**Smart selection hierarchy** - Provides semantically meaningful selection ranges.
- **Use cases**: Precision code selection, automated refactoring, scope analysis




### Common Workflow Patterns of Zentara

#### 🔍 **Code Exploration Pattern**
1. `lsp_search_symbols` or `lsp_get_workspace_symbols` → find target symbols
2. `lsp_get_document_symbols` → understand file structure
3. `lsp_find_usages` → understand dependencies (MANDATORY)
4. `lsp_get_call_hierarchy` → understand function relationships (MANDATORY)
5. `lsp_get_symbol_children` → explore symbol structure
6. `lsp_get_symbol_code_snippet` → examine specific implementations

#### 🐛 **Debugging Pattern**
1. `lsp_find_usages` → find all places where problematic symbol is used (MANDATORY)
2. `lsp_get_call_hierarchy` → trace execution paths and error propagation (MANDATORY)
3. `lsp_go_to_definition` → examine implementations
4. `lsp_get_hover_info` → understand types and signatures

#### 🔧 **Refactoring Pattern**
1. `lsp_find_usages` → understand full impact scope (MANDATORY)
2. `lsp_get_call_hierarchy` → understand function dependencies (MANDATORY)
3. `lsp_get_symbol_children` → understand structure before changes
4. `lsp_rename` or modification tools → make changes

#### 📚 **API Discovery Pattern**
1. `lsp_search_symbols` → find relevant classes/modules
2. `lsp_get_symbol_children` → explore available methods/properties
3. `lsp_get_hover_info` → understand signatures and documentation
4. `lsp_get_completions` → discover available options




## Language Support

All LSP tools work across multiple programming languages:

- **TypeScript/JavaScript**: Full support for all features
- **Python**: Excellent support for classes, functions, and modules
- **Java**: Complete support for OOP features and packages
- **C#**: Full support for .NET features and namespaces
- **Go**: Good support for packages and interfaces
- **Rust**: Support for traits, structs, and modules
- **C++**: Support for classes, namespaces, and templates


## Conclusion

The LSP tools in this repository provide powerful, semantic-aware code analysis capabilities that far exceed simple text-based approaches. By following the mandatory workflows and best practices outlined in this document, you can efficiently navigate, understand, and modify codebases with precision and confidence.

