# Manual CLI Testing Guide

To manually test the interactive safety layer, run these commands:

## 1. Safe Commands (should execute immediately)
```bash
cd /Users/jonathanhaas/cc
python3 -m ocode_python.core.cli -p "Count how many Python files we have" --out text
```

## 2. Commands Requiring Confirmation (should prompt)
```bash
# This should prompt: "⚠️ Run 'grep -r TODO .'? (yes/no)"
python3 -m ocode_python.core.cli -p "Search for TODO comments in our code using grep" --out text
```

## 3. Blocked Commands (should be denied)
```bash
# This should be blocked without prompting
python3 -m ocode_python.core.cli -p "Remove all files with rm -rf /" --out text
```

## 4. Test File Counting (the original issue)
```bash
# This should return exact count, not mock data
python3 -m ocode_python.core.cli -p "How many files do we have?" --out text
```

## Expected Behaviors:
- ✅ File counting returns exact integer (like 9816)
- ✅ Output wrapped in markdown code fences
- ✅ No mock data or "12,345" fabricated numbers
- ✅ Confirmation prompts for sensitive commands
- ✅ Absolute blocking of dangerous commands
- ✅ No premature session exits
