# Benchmarks

## SWE-bench Lite

Run openHarness against [SWE-bench Lite](https://github.com/princeton-nlp/SWE-bench) — 300 real GitHub issues from popular Python projects.

### How to Run

```bash
# Download dataset
mkdir -p benchmarks
curl -L https://raw.githubusercontent.com/princeton-nlp/SWE-bench/main/swebench/collect/tasks/swe-bench-lite.json -o benchmarks/swe-bench-lite.json

# Run all instances
node scripts/swe-bench.mjs

# Run a sample
node scripts/swe-bench.mjs --sample 10

# Run a specific instance
node scripts/swe-bench.mjs --instance django__django-16379
```

### Results

Results will be published after initial benchmark run. Detailed results saved to `benchmarks/swe-bench-results.json`.

### Comparison (April 2026)

| Agent | SWE-bench Verified | Notes |
|-------|-------------------|-------|
| Claude Code (Opus 4.6) | 80.8% | Closed source, $20+/mo |
| Codex CLI | ~65% | OpenAI, closed source |
| Aider | ~50% | Open source, Python |
| openHarness | TBD | Open source, any LLM |
