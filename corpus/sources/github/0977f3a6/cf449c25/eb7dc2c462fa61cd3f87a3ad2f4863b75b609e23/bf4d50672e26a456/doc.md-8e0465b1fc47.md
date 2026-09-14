# Requirements

* The [ldc-doc](https://github.com/waikato-llm/ldc-doc) library.
* The `antiword` binary available on `PATH`

  * Debian/Ubuntu: `sudo apt install antiword`
  * Windows: [Softpedia](https://www.softpedia.com/get/Office-tools/Other-Office-Tools/Antiword.shtml)


# Plugins

## Extracting text from MS Word (.doc) documents

```bash
ldc-convert \
  -l INFO \
  from-doc-pt \
    -l INFO \
    --input "./input/*.doc" \
  to-txt-pt \
    -l INFO \
    --output "./output/"
```
