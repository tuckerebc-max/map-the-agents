# Requirements

Requires the [ldc-docx](https://github.com/waikato-llm/ldc-docx) library.

# Plugins

## Extracting text from MS Word (.docx) documents

```bash
ldc-convert \
  -l INFO \
  from-docx-pt \
    -l INFO \
    --input "./input/*.docx" \
  to-txt-pt \
    -l INFO \
    --output "./output/"
```
