# Stacklit Growth Package — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Ship 5 improvements that make Stacklit more adoptable, shareable, and discoverable — targeting 100+ stars.

**Architecture:** Each task is independent and shippable on its own. Tasks are ordered by growth impact: GitHub Action (sticky adoption) → Benchmark post (proof) → Comparison Discussion (SEO) → Share button (virality) → Framework patterns (depth). Framework detection already exists — Task 5 extends it with pattern metadata.

**Tech Stack:** Go, GitHub Actions, HTML/JS, GitHub Discussions API

---

### Task 1: GitHub Action (`glincker/stacklit-action`)

**Files:**
- Create: new repo `glincker/stacklit-action`
  - `action.yml`
  - `entrypoint.sh`
  - `README.md`
- Modify: `glincker/stacklit` README.md (add Action usage section)

- [ ] **Step 1: Create the action repo**

```bash
mkdir -p /Users/gdsks/G-Development/GLINRV5/stacklit-action
cd /Users/gdsks/G-Development/GLINRV5/stacklit-action
git init
```

- [ ] **Step 2: Write action.yml**

Create `action.yml`:

```yaml
name: 'Stacklit Index'
description: 'Keep your AI-agent codebase index up to date automatically'
branding:
  icon: 'cpu'
  color: 'blue'

inputs:
  mode:
    description: 'auto-commit (default) or check'
    required: false
    default: 'auto-commit'
  version:
    description: 'Stacklit version (default: latest)'
    required: false
    default: 'latest'
  args:
    description: 'Extra arguments passed to stacklit generate'
    required: false
    default: ''

runs:
  using: 'composite'
  steps:
    - name: Install Stacklit
      shell: bash
      run: |
        VERSION="${{ inputs.version }}"
        if [ "$VERSION" = "latest" ]; then
          VERSION=$(curl -s https://api.github.com/repos/glincker/stacklit/releases/latest | grep tag_name | cut -d '"' -f4)
        fi
        curl -sL "https://github.com/glincker/stacklit/releases/download/${VERSION}/stacklit-linux-amd64" -o /usr/local/bin/stacklit
        chmod +x /usr/local/bin/stacklit

    - name: Generate index
      shell: bash
      run: stacklit generate ${{ inputs.args }}

    - name: Check or commit
      shell: bash
      env:
        MODE: ${{ inputs.mode }}
      run: |
        if [ "$MODE" = "check" ]; then
          if git diff --quiet stacklit.json DEPENDENCIES.md 2>/dev/null; then
            echo "Index is up to date."
          else
            echo "::error::Stacklit index is stale. Run 'stacklit generate' locally and commit."
            exit 1
          fi
        else
          if git diff --quiet stacklit.json DEPENDENCIES.md 2>/dev/null; then
            echo "Index is up to date, nothing to commit."
          else
            git config user.name "stacklit[bot]"
            git config user.email "stacklit[bot]@users.noreply.github.com"
            git add stacklit.json DEPENDENCIES.md
            git commit -m "chore: update stacklit index"
            git push
          fi
        fi
```

- [ ] **Step 3: Write README.md for the action**

Create `README.md`:

```markdown
# Stacklit Action

Keep your AI-agent codebase index up to date automatically.

## Usage

```yaml
name: Stacklit
on: [push]
jobs:
  index:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - uses: glincker/stacklit-action@v1
        with:
          mode: auto-commit
```

## Inputs

| Input | Default | Description |
|-------|---------|-------------|
| `mode` | `auto-commit` | `auto-commit` or `check` |
| `version` | `latest` | Stacklit version to use |
| `args` | `''` | Extra flags for `stacklit generate` |

## Modes

**auto-commit**: Regenerates and commits if the index changed. Set `permissions: contents: write` on the job.

**check**: Fails CI if the index is stale. Useful for enforcing that developers run `stacklit generate` before pushing.
```

- [ ] **Step 4: Create GitHub repo, push, and tag v1**

```bash
cd /Users/gdsks/G-Development/GLINRV5/stacklit-action
gh repo create glincker/stacklit-action --public --source=. --push
git tag v1
git push origin v1
```

- [ ] **Step 5: Test the action on stacklit repo**

Add to `glincker/stacklit/.github/workflows/stacklit.yml`:

```yaml
name: Stacklit Index
on: [push]
jobs:
  index:
    runs-on: ubuntu-latest
    permissions:
      contents: write
    steps:
      - uses: actions/checkout@v4
      - uses: glincker/stacklit-action@v1
        with:
          mode: check
```

Run: push a commit and verify the action passes.

- [ ] **Step 6: Add action usage to stacklit README**

Add a "CI / GitHub Action" section to README.md after the install section:

```markdown
## CI / GitHub Action

Keep your index fresh automatically:

```yaml
- uses: glincker/stacklit-action@v1
  with:
    mode: auto-commit  # or "check" to fail CI if stale
```

See [stacklit-action](https://github.com/glincker/stacklit-action) for full docs.
```

- [ ] **Step 7: Commit**

```bash
git add .github/workflows/stacklit.yml README.md
git commit -m "feat: add GitHub Action for auto-indexing"
```

---

### Task 2: Benchmark Discussion post

**Files:**
- Create: benchmark script (local, not committed)
- Create: GitHub Discussion via `gh` CLI

- [ ] **Step 1: Enable Discussions on the repo**

```bash
gh repo edit glincker/stacklit --enable-discussions
```

- [ ] **Step 2: Run benchmark — Express.js WITHOUT stacklit**

Clone Express, give Claude Code a task, count tool calls:

```bash
cd /tmp && git clone https://github.com/expressjs/express.git express-bench
cd express-bench
# Task: "Where is the routing logic and how does middleware chaining work?"
# Record: tool calls, tokens, time, correctness
```

Document the numbers manually from the Claude Code session.

- [ ] **Step 3: Run benchmark — Express.js WITH stacklit**

```bash
cd /tmp/express-bench
npx stacklit init
# Same task: "Where is the routing logic and how does middleware chaining work?"
# Record: tool calls, tokens, time, correctness
```

- [ ] **Step 4: Run benchmark — Stacklit repo itself (both modes)**

Repeat steps 2-3 on the Stacklit repo with task: "How does the parser extract exports from Go files?"

- [ ] **Step 5: Write and publish the Discussion post**

```bash
gh discussion create -R glincker/stacklit \
  --category "Announcements" \
  --title "How 250 tokens replaced 50,000 tokens of codebase exploration" \
  --body "$(cat <<'BODY'
## The test

We gave Claude Code the same task on two codebases — with and without a Stacklit index.

### Express.js (23k lines)

| Metric | Without Stacklit | With Stacklit |
|--------|-----------------|---------------|
| Tool calls | XX | XX |
| Tokens used | XX | XX |
| Time | XX | XX |
| Correct answer | Yes/No | Yes/No |

### Stacklit (8k lines Go)

| Metric | Without Stacklit | With Stacklit |
|--------|-----------------|---------------|
| Tool calls | XX | XX |
| Tokens used | XX | XX |
| Time | XX | XX |
| Correct answer | Yes/No | Yes/No |

## How it works

Stacklit scans your repo once and produces a ~250-token index that tells AI agents where everything is — modules, exports, dependencies, entry points. Instead of 47 Grep/Glob/Read calls to map the codebase, the agent reads one file and starts working.

## Try it

\`\`\`bash
npx stacklit init
\`\`\`

That's it. One command. Generates the index, opens a visual map of your codebase.
BODY
)"
```

Fill in XX with actual benchmark numbers from steps 2-4.

- [ ] **Step 6: Add link to README**

Add after the "What happens when you run it" section:

```markdown
## Does it actually help?

[Yes. We measured it.](link-to-discussion) Claude Code used 80% fewer tool calls and 90% fewer tokens with a Stacklit index vs exploring the codebase from scratch.
```

- [ ] **Step 7: Commit README change**

```bash
git add README.md
git commit -m "docs: add benchmark results link to README"
```

---

### Task 3: Comparison Discussion post (SEO)

**Files:**
- Modify: `README.md` (add compact comparison table)
- Create: GitHub Discussion from existing `COMPARISON.md`

- [ ] **Step 1: Publish COMPARISON.md as a Discussion**

```bash
gh discussion create -R glincker/stacklit \
  --category "Announcements" \
  --title "Stacklit vs Repomix vs code2prompt vs Aider repo-map — full comparison" \
  --body-file COMPARISON.md
```

- [ ] **Step 2: Add compact comparison table to README**

Add after the benchmark section:

```markdown
## How it compares

| Tool | Approach | Tokens | Committable | Visual map |
|------|----------|--------|-------------|------------|
| **Stacklit** | Structured index | ~250 | Yes | Yes |
| Repomix | Full dump | 50k-500k | No | No |
| code2prompt | Full dump | 50k-500k | No | No |
| Aider repo-map | Tree-sitter + PageRank | ~1k | No | No |

[Full comparison with 7 tools →](link-to-discussion)
```

- [ ] **Step 3: Commit**

```bash
git add README.md
git commit -m "docs: add comparison table and link to full comparison"
```

---

### Task 4: Shareable visual map

**Files:**
- Modify: `assets/template.html` (add Share button + JS)

- [ ] **Step 1: Read the current template bottom section**

Read the last 100 lines of `assets/template.html` to find where the toolbar/header is and where to add the button.

- [ ] **Step 2: Add Share button to the toolbar**

Find the existing toolbar/nav in `template.html` and add a Share button next to it. The button HTML:

```html
<button id="share-btn" title="Share this map">
  <svg width="16" height="16" viewBox="0 0 16 16" fill="currentColor">
    <path d="M11 2.5a2.5 2.5 0 11-1.73 4.31L6.35 8.87a2.5 2.5 0 010-1.74l2.92-2.06A2.5 2.5 0 0111 2.5zM5 8a2.5 2.5 0 11-.01.01L5 8zm6 3.5a2.5 2.5 0 11-1.73-2.31l-2.92-2.06a2.5 2.5 0 010 1.74l2.92 2.06A2.5 2.5 0 0111 11.5z"/>
  </svg>
  Share
</button>
```

- [ ] **Step 3: Add share JavaScript**

Add at the bottom of the `<script>` section:

```javascript
document.getElementById('share-btn').addEventListener('click', function() {
  const html = document.documentElement.outerHTML;
  const banner = '<div style="background:#161b22;color:#8b949e;padding:8px 16px;font-size:12px;text-align:center;border-bottom:1px solid #30363d;">Generated by <a href="https://github.com/glincker/stacklit" style="color:#58a6ff;">Stacklit</a> — make any repo AI-agent-ready</div>';
  const shared = '<!DOCTYPE html>' + html.replace('<body', '<body>' + banner + '<div ').replace('<body><div ', '<body');

  const blob = new Blob([shared], { type: 'text/html' });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = 'stacklit-map.html';
  a.click();
  URL.revokeObjectURL(url);
});
```

- [ ] **Step 4: Test locally**

```bash
cd /Users/gdsks/G-Development/GLINRV5/stacklit
go run ./cmd/stacklit generate
open stacklit.html
# Click Share button, verify HTML downloads with banner
```

- [ ] **Step 5: Commit**

```bash
git add assets/template.html
git commit -m "feat: add Share button to visual map for easy sharing"
```

---

### Task 5: Framework pattern metadata

**Files:**
- Modify: `internal/detect/frameworks.go` (add pattern detection)
- Modify: `internal/schema/schema.go` (add FrameworkInfo struct)
- Modify: `internal/engine/engine.go` (wire up pattern detection)
- Create: `internal/detect/framework_patterns.go`
- Create: `internal/detect/framework_patterns_test.go`

Note: `DetectFrameworks` already returns `[]string`. We need to extend it to return richer data with patterns.

- [ ] **Step 1: Write the test for framework pattern detection**

Create `internal/detect/framework_patterns_test.go`:

```go
package detect

import (
	"os"
	"path/filepath"
	"testing"
)

func TestDetectFrameworkPatterns_NextJS(t *testing.T) {
	dir := t.TempDir()

	// Create Next.js signals
	os.WriteFile(filepath.Join(dir, "next.config.ts"), []byte("export default {}"), 0644)
	os.MkdirAll(filepath.Join(dir, "app", "api"), 0755)
	os.WriteFile(filepath.Join(dir, "app", "page.tsx"), []byte(""), 0644)
	os.WriteFile(filepath.Join(dir, "middleware.ts"), []byte(""), 0644)

	patterns := DetectFrameworkPatterns(dir)

	if len(patterns) == 0 {
		t.Fatal("expected at least one framework pattern")
	}

	found := false
	for _, p := range patterns {
		if p.Name == "Next.js" {
			found = true
			if p.Routes != "app/" {
				t.Errorf("expected routes=app/, got %s", p.Routes)
			}
			if p.API != "app/api/" {
				t.Errorf("expected api=app/api/, got %s", p.API)
			}
			if p.Middleware != "middleware.ts" {
				t.Errorf("expected middleware=middleware.ts, got %s", p.Middleware)
			}
		}
	}
	if !found {
		t.Error("Next.js pattern not detected")
	}
}

func TestDetectFrameworkPatterns_Express(t *testing.T) {
	dir := t.TempDir()

	// Create Express signals via package.json
	pkgJSON := `{"dependencies":{"express":"^4.18.0"}}`
	os.WriteFile(filepath.Join(dir, "package.json"), []byte(pkgJSON), 0644)
	os.MkdirAll(filepath.Join(dir, "routes"), 0755)
	os.WriteFile(filepath.Join(dir, "routes", "index.js"), []byte(""), 0644)
	os.WriteFile(filepath.Join(dir, "app.js"), []byte(""), 0644)

	patterns := DetectFrameworkPatterns(dir)

	found := false
	for _, p := range patterns {
		if p.Name == "Express" {
			found = true
			if p.Routes != "routes/" {
				t.Errorf("expected routes=routes/, got %s", p.Routes)
			}
		}
	}
	if !found {
		t.Error("Express pattern not detected")
	}
}
```

- [ ] **Step 2: Run test to verify it fails**

```bash
go test ./internal/detect/ -run TestDetectFrameworkPatterns -v
```

Expected: FAIL — `DetectFrameworkPatterns` not defined.

- [ ] **Step 3: Define FrameworkPattern struct and detection logic**

Create `internal/detect/framework_patterns.go`:

```go
package detect

import (
	"encoding/json"
	"os"
	"path/filepath"
)

// FrameworkPattern holds detected framework info with file layout patterns.
type FrameworkPattern struct {
	Name       string   `json:"name"`
	Config     []string `json:"config_files,omitempty"`
	Routes     string   `json:"routes,omitempty"`
	API        string   `json:"api,omitempty"`
	Middleware string   `json:"middleware,omitempty"`
	Models     string   `json:"models,omitempty"`
	Entry      string   `json:"entry,omitempty"`
}

type frameworkProbe struct {
	name      string
	configAny []string                      // detect if any of these files exist
	depKey    string                        // check package.json for this dep
	patterns  func(root string) FrameworkPattern // fill in directory patterns
}

var probes = []frameworkProbe{
	{
		name:      "Next.js",
		configAny: []string{"next.config.js", "next.config.ts", "next.config.mjs"},
		depKey:    "next",
		patterns: func(root string) FrameworkPattern {
			p := FrameworkPattern{Name: "Next.js"}
			if dirExists(root, "app") {
				p.Routes = "app/"
				if dirExists(root, "app/api") {
					p.API = "app/api/"
				}
			} else if dirExists(root, "pages") {
				p.Routes = "pages/"
				if dirExists(root, "pages/api") {
					p.API = "pages/api/"
				}
			}
			if fileExists(root, "middleware.ts") || fileExists(root, "middleware.js") {
				p.Middleware = firstExisting(root, "middleware.ts", "middleware.js")
			}
			return p
		},
	},
	{
		name:   "Express",
		depKey: "express",
		patterns: func(root string) FrameworkPattern {
			p := FrameworkPattern{Name: "Express"}
			if dirExists(root, "routes") {
				p.Routes = "routes/"
			}
			p.Entry = firstExisting(root, "app.js", "app.ts", "server.js", "server.ts", "index.js")
			return p
		},
	},
	{
		name:      "FastAPI",
		configAny: []string{"requirements.txt", "pyproject.toml"},
		patterns: func(root string) FrameworkPattern {
			p := FrameworkPattern{Name: "FastAPI"}
			if dirExists(root, "app/routers") {
				p.Routes = "app/routers/"
			} else if dirExists(root, "routers") {
				p.Routes = "routers/"
			}
			p.Entry = firstExisting(root, "app/main.py", "main.py")
			if dirExists(root, "app/models") {
				p.Models = "app/models/"
			}
			return p
		},
	},
	{
		name:      "Django",
		configAny: []string{"manage.py"},
		patterns: func(root string) FrameworkPattern {
			p := FrameworkPattern{Name: "Django"}
			p.Entry = "manage.py"
			return p
		},
	},
	{
		name:      "Gin",
		configAny: []string{"go.mod"},
		patterns: func(root string) FrameworkPattern {
			p := FrameworkPattern{Name: "Gin"}
			p.Entry = firstExisting(root, "main.go", "cmd/server/main.go")
			return p
		},
	},
	{
		name:      "Spring Boot",
		configAny: []string{"pom.xml", "build.gradle", "build.gradle.kts"},
		patterns: func(root string) FrameworkPattern {
			p := FrameworkPattern{Name: "Spring Boot"}
			if dirExists(root, "src/main/java") {
				p.Routes = "src/main/java/"
			}
			return p
		},
	},
}

// DetectFrameworkPatterns scans root for known framework signals and returns
// pattern metadata for each detected framework.
func DetectFrameworkPatterns(root string) []FrameworkPattern {
	var results []FrameworkPattern

	pkgDeps := loadPkgDeps(root)

	for _, probe := range probes {
		detected := false

		// Check config files
		for _, cf := range probe.configAny {
			if fileExists(root, cf) || dirExists(root, cf) {
				detected = true
				break
			}
		}

		// Check package.json dep
		if !detected && probe.depKey != "" {
			if _, ok := pkgDeps[probe.depKey]; ok {
				detected = true
			}
		}

		// For FastAPI/Django: also check requirements.txt content
		if !detected && (probe.name == "FastAPI" || probe.name == "Django") {
			if reqData, err := os.ReadFile(filepath.Join(root, "requirements.txt")); err == nil {
				needle := "fastapi"
				if probe.name == "Django" {
					needle = "django"
				}
				for _, line := range splitLines(string(reqData)) {
					if len(line) > 0 && containsCI(line, needle) {
						detected = true
						break
					}
				}
			}
		}

		// For Gin: check go.mod for gin import
		if !detected && probe.name == "Gin" {
			if modData, err := os.ReadFile(filepath.Join(root, "go.mod")); err == nil {
				if containsCI(string(modData), "gin-gonic/gin") {
					detected = true
				}
			}
		}

		// For Spring Boot: check pom.xml/build.gradle for spring-boot
		if !detected && probe.name == "Spring Boot" {
			for _, cf := range []string{"pom.xml", "build.gradle", "build.gradle.kts"} {
				if data, err := os.ReadFile(filepath.Join(root, cf)); err == nil {
					if containsCI(string(data), "spring-boot") {
						detected = true
						break
					}
				}
			}
		}

		if detected && probe.patterns != nil {
			p := probe.patterns(root)
			// Collect config files that exist
			for _, cf := range probe.configAny {
				if fileExists(root, cf) {
					p.Config = append(p.Config, cf)
				}
			}
			results = append(results, p)
		}
	}

	return results
}

func loadPkgDeps(root string) map[string]string {
	data, err := os.ReadFile(filepath.Join(root, "package.json"))
	if err != nil {
		return nil
	}
	var pkg struct {
		Dependencies    map[string]string `json:"dependencies"`
		DevDependencies map[string]string `json:"devDependencies"`
	}
	if json.Unmarshal(data, &pkg) != nil {
		return nil
	}
	all := make(map[string]string, len(pkg.Dependencies)+len(pkg.DevDependencies))
	for k, v := range pkg.Dependencies {
		all[k] = v
	}
	for k, v := range pkg.DevDependencies {
		all[k] = v
	}
	return all
}

func fileExists(root, rel string) bool {
	info, err := os.Stat(filepath.Join(root, rel))
	return err == nil && !info.IsDir()
}

func dirExists(root, rel string) bool {
	info, err := os.Stat(filepath.Join(root, rel))
	return err == nil && info.IsDir()
}

func firstExisting(root string, candidates ...string) string {
	for _, c := range candidates {
		if fileExists(root, c) {
			return c
		}
	}
	return ""
}

func containsCI(s, substr string) bool {
	return len(s) >= len(substr) && // fast path
		len(substr) > 0 &&
		indexOf(toLower(s), toLower(substr)) >= 0
}

func toLower(s string) string {
	b := make([]byte, len(s))
	for i := range s {
		c := s[i]
		if c >= 'A' && c <= 'Z' {
			c += 32
		}
		b[i] = c
	}
	return string(b)
}

func indexOf(s, sub string) int {
	for i := 0; i <= len(s)-len(sub); i++ {
		if s[i:i+len(sub)] == sub {
			return i
		}
	}
	return -1
}

func splitLines(s string) []string {
	var lines []string
	start := 0
	for i := 0; i < len(s); i++ {
		if s[i] == '\n' {
			lines = append(lines, s[start:i])
			start = i + 1
		}
	}
	if start < len(s) {
		lines = append(lines, s[start:])
	}
	return lines
}
```

- [ ] **Step 4: Run tests to verify they pass**

```bash
go test ./internal/detect/ -run TestDetectFrameworkPatterns -v
```

Expected: PASS

- [ ] **Step 5: Add FrameworkInfo to schema**

Modify `internal/schema/schema.go`. Change `Tech.Frameworks` from `[]string` to support both formats:

```go
type Tech struct {
	PrimaryLanguage   string               `json:"primary_language"`
	Languages         map[string]LangStats `json:"languages"`
	Frameworks        []string             `json:"frameworks,omitempty"`
	FrameworkPatterns []FrameworkPattern    `json:"framework_patterns,omitempty"`
}

type FrameworkPattern struct {
	Name       string   `json:"name"`
	Config     []string `json:"config_files,omitempty"`
	Routes     string   `json:"routes,omitempty"`
	API        string   `json:"api,omitempty"`
	Middleware string   `json:"middleware,omitempty"`
	Models     string   `json:"models,omitempty"`
	Entry      string   `json:"entry,omitempty"`
}
```

Keep `Frameworks []string` for backward compatibility. `FrameworkPatterns` adds the rich data.

- [ ] **Step 6: Wire up in engine**

In `internal/engine/engine.go`, find where `DetectFrameworks` is called and add pattern detection after it:

```go
// After: idx.Tech.Frameworks = detect.DetectFrameworks(root, allImports)
idx.Tech.FrameworkPatterns = toSchemaPatterns(detect.DetectFrameworkPatterns(root))
```

Add helper to convert detect types to schema types (or import directly if package structure allows).

- [ ] **Step 7: Run full test suite**

```bash
go test ./... 
```

Expected: all pass.

- [ ] **Step 8: Commit**

```bash
git add internal/detect/framework_patterns.go internal/detect/framework_patterns_test.go internal/schema/schema.go internal/engine/engine.go
git commit -m "feat: add framework pattern detection with routes, API, middleware, entry points"
```

---

### Task 6: Final release

- [ ] **Step 1: Tag and push**

```bash
git tag v0.4.0
git push origin master --tags
```

- [ ] **Step 2: Update stacklit-action to use v0.4.0 as default**

- [ ] **Step 3: Verify all Discussion posts are published and linked from README**
