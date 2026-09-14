# The First AI Coding Style Guide 

by Xinran Wang(lidangzzz)

[中文版](README_CN.md)

## Quick Start

Open the [`AI_Coding_Style_Guide_prompts.toml`](AI_Coding_Style_Guide_prompts.toml) file in your favorite text editor, and you will find a collection of prompts that can be used to guide large language models in compressing code. You can use these prompts to instruct large language models to follow the coding style guides and compress code according to the principles outlined in this document.

If you want to use these prompts in your own projects, you can copy the contents of the `AI_Coding_Style_Guide_prompts.toml` file and paste them into your own prompt management system. You can also modify the prompts to suit your specific needs.

If you want to load these prompts into your own prompt management system, you can use the following code snippet:

```python
import toml 
from pathlib import Path
def load_prompts(file_path: str) -> dict:
    """Load prompts from a TOML file."""
    return toml.load(Path(file_path))
prompts = load_prompts("AI_Coding_Style_Guide_prompts.toml")
```

## Introduction

When I use vibe coding or SWE Agent, I often encounter the issue of insufficient context window size. If we feed multiple source code files at once and the total length exceeds the context window, we are forced to selectively include only some of the files. This can cause the large language model to lose part of the necessary context.

Another issue is that most current vibe coding or SWE Agent tools charge based on token usage, because the API providers of large language models also charge these tools according to the number of tokens consumed. In this case, the longer the source code, the more tokens are required — not only leading to a linear increase in cost but also a linear increase in the time cost of token output.

To enable large language models to process more source code files, modules, and functionalities within a fixed context window — and to save more tokens — we have designed this collection of coding style guides. This collection includes both general coding style guides for common programming languages and specific guides tailored to particular languages and scenarios.

Our goal is to maximize code compression across various programming languages while maintaining a reasonable level of human readability, so as to conserve as much of the context window as possible while achieving a balance between compactness and readability.

## Principles

We created this set of coding style guides because we believe in three fundamental trends, which reflect our first-principles thinking in both software engineering and working with large language models:

1. The capabilities of large language models will continue to improve, gradually surpassing ordinary human programmers. Large language models are already capable of understanding these extremely compressed forms of code, and their comprehension will only get stronger.

2. The context window of large language models will always feel insufficient. Whether it's 32k, 64k, 256k, 1M tokens, or beyond, prompt engineers will always want to pack in more code and context. Whereas we could previously only fit two or three files, we may eventually aim to include dozens or even hundreds of files.

3. When vibe coding or SWE Agent tools take on the primary programming tasks, the importance of code readability gradually decreases. Humans lack the time or willingness to review all the code in detail; instead, they care more about whether the functionality is complete. To maximize the efficiency of vibe coding or SWE Agents, it becomes reasonable to sacrifice code readability to some extent — reducing unnecessary redundancy like overly long variable names, extra spaces, line breaks, tabs, etc.

4. The reliability of code should increasingly rely on fine-grained unit tests rather than the outcomes of human code review. Comprehensive unit tests can help ensure code quality across the codebase. However, more unit tests mean more code overall, which further increases the need for code compression.

5. If a human engineer wishes to step in for debugging or optimization but cannot understand the highly compressed code, large language models can fully assist by explaining code snippets or reconstructing them into more verbose and human-readable forms for detailed analysis and decision-making. There’s no need to worry that compressed code will become incomprehensible — we should trust that large language models and SWE Agents are friends and helpers to humans, ready at any time to assist in restoring and clarifying compressed code.

## Basic Coding Style Rules

Based on these core principles, we have carefully designed a set of basic rules that SWE Agents or vibe coding tools should follow:

1. Minimize unnecessary indentation, spaces, and line breaks to keep the code compact.

2. For top-level functions, classes, and module names, adhere to proper and complete naming conventions as much as possible. For code within functions, classes, or modules — especially temporary variables — reduce variable name length to minimize code size.

3. Provide brief but necessary comments for top-level functions, classes, and modules to describe their purpose, inputs, and outputs. Inside functions, avoid comments unless absolutely necessary.

4. Where possible, implement more functions, classes, or modules within a single file, especially when they are interrelated. Separate code into different files only when they serve distinct modules or functionalities.

5. Use advanced language features and designs to reduce code size — for example, prefer lambda functions over full function definitions when appropriate; leverage syntactic sugar that significantly shortens code; and in statically typed languages like C++ or TypeScript, use type inference to cut down on code verbosity.

6. For modules, functions, or classes that need to be reused, abstract them into standalone units to enable reuse and reduce overall code volume.

7. Avoid unnecessary code duplication, such as repeated logic or similar functions. Instead, use higher-order functions, decorators, or mixins to encapsulate common logic.

8. When using third-party libraries, prefer concise and efficient libraries that provide the necessary functionality without excessive overhead.

9. Let the large language model handle the code compression process, as it can automatically apply these principles to achieve optimal results.

## Levels of Compression

We can further categorize the compression process into different levels, each with its own focus and trade-offs. The following table outlines these levels, their descriptions, and the specific techniques used at each stage:

| Level | Description                                 | Whitespace Removal                | Code Compression              | Variable Shortening    | Export Name Preserved | Comment Handling      | Advanced Refactoring |
| ----- | ------------------------------------------- | --------------------------------- | ----------------------------- | ---------------------- | --------------------- | --------------------- | -------------------- |
| **1** | Remove unnecessary spaces and new lines     | ✅ Basic (extra spaces & newlines) | ❌                             | ❌                      | ✅                     | ✅ Keep all comments   | ❌                    |
| **2** | Slightly compress code by merging lines     | ✅ Basic                           | ✅ Slight merging (same logic) | ❌                      | ✅                     | ✅ Keep all comments   | ❌                    |
| **3** | Shorten local variable names                | ✅ Basic                           | ✅                             | ✅ Local only           | ✅                     | ✅ Keep all comments   | ❌                    |
| **4** | Shorten local & non-exported names          | ✅ Basic                           | ✅                             | ✅ Local & non-exported | ✅                     | ✅ Keep all comments   | ❌                    |
| **5** | Remove all whitespace & shorten identifiers | ✅ Full (no space, newline)        | ✅ Maximize compactness        | ✅ Local & non-exported | ✅                     | ✅ Keep comments only  | ❌                    |
| **6** | Remove comments except for exported parts   | ✅ Full                            | ✅                             | ✅ Local & non-exported | ✅                     | ☑️ Only for exported  | ❌                    |
| **7** | Remove all comments                         | ✅ Full                            | ✅                             | ✅ Local & non-exported | ✅                     | ❌ Remove all comments | ❌                    |
| **8** | Use language features to minimize code      | ✅ Full                            | ✅ Max + Refactor              | ✅ Local & non-exported | ✅                     | ❌ Remove all comments | ✅ Use any features   |

## Example 1: KMP String Matching Algorithm

### Original Code in TypeScript(1216 characters)

Here is a simple example of how to apply these principles in TypeScript. Below is a demonstration of the KMP string matching algorithm. There are 1216 characters in the original code.

```typescript
// Function to build the Longest Prefix Suffix (LPS) array
function buildLPS(pattern: string): number[] {
    const lps: number[] = new Array(pattern.length).fill(0);
    let len = 0;
    let i = 1;

    while (i < pattern.length) {
        if (pattern[i] === pattern[len]) {
            len++;
            lps[i] = len;
            i++;
        } else {
            if (len !== 0) {
                len = lps[len - 1];
            } else {
                lps[i] = 0;
                i++;
            }
        }
    }

    return lps;
}

// KMP search function: returns all starting indices where pattern is found in text
function kmpSearch(text: string, pattern: string): number[] {
    const lps = buildLPS(pattern);
    const result: number[] = [];
    let i = 0; // index for text
    let j = 0; // index for pattern

    while (i < text.length) {
        if (pattern[j] === text[i]) {
            i++;
            j++;
        }

        if (j === pattern.length) {
            result.push(i - j); // found a match
            j = lps[j - 1];
        } else if (i < text.length && pattern[j] !== text[i]) {
            if (j !== 0) {
                j = lps[j - 1];
            } else {
                i++;
            }
        }
    }

    return result;
}
```

### Slightly Compressed Code in TypeScript(795 characters, ~65.4% of the original size)

After removing unnecessary spaces and line breaks but keeping all code indentations, the code is reduced to 795 characters(~65.4% of the original size):

```typescript
// Function to build the Longest Prefix Suffix (LPS) array
function buildLPS(pattern:string):number[]{
 let lps:number[]=new Array(pattern.length).fill(0);
 let len=0,i=1;
 while(i<pattern.length){
  if(pattern[i]===pattern[len]){
   len++;
   lps[i]=len;
   i++;
  }else{
   if(len!==0){
    len=lps[len-1];
   }else{
    lps[i]=0;
    i++;
   }
  }
 }
 return lps;
}

// KMP search function: returns all starting indices where pattern is found in text
function kmpSearch(text:string,pattern:string):number[]{
 let lps=buildLPS(pattern);
 let result:number[]=[];
 let i=0,j=0;
 while(i<text.length){
  if(pattern[j]===text[i]){
   i++;
   j++;
  }
  if(j===pattern.length){
   result.push(i-j);
   j=lps[j-1];
  }else if(i<text.length&&pattern[j]!==text[i]){
   if(j!==0){
    j=lps[j-1];
   }else{
    i++;
   }
  }
 }
 return result;
}
```

### Deeper Compression to 715 characters (~58.7% of the original size)

Next, let's remove all unnecessary spaces, line breaks and indentation, resulting in a highly compressed version of the code with only 715 characters (~58.7% of the original size):

```typescript
// Function to build the Longest Prefix Suffix (LPS) array
function buildLPS(pattern:string):number[]{const lps:number[]=new Array(pattern.length).fill(0);let len=0,i=1;while(i<pattern.length){if(pattern[i]===pattern[len]){len++;lps[i]=len;i++;}else{if(len!==0){len=lps[len-1];}else{lps[i]=0;i++;}}}return lps;}
// KMP search function: returns all starting indices where pattern is found in text
function kmpSearch(text:string,pattern:string):number[]{const lps=buildLPS(pattern);const result:number[]=[];let i=0,j=0;while(i<text.length){if(pattern[j]===text[i]){i++;j++;}if(j===pattern.length){result.push(i-j);j=lps[j-1];}else if(i<text.length&&pattern[j]!==text[i]){if(j!==0){j=lps[j-1];}else{i++;}}}return result;}
```

### Further Compression to 443 characters (~36.4% of the original size)

Next, let's remove the comments and reduce the variable names to the minimum necessary while still keeping them understandable. The final code is only 443 characters long (~36.4% of the original size):

```typescript
function buildLPS(p:string):number[]{const l:number[]=new Array(p.length).fill(0);let l0=0,i=1;while(i<p.length){if(p[i]===p[l0]){l0++;l[i]=l0;i++;}else if(l0){l0=l[l0-1];}else{l[i]=0;i++;}}return l;}
function kmpSearch(t:string,p:string):number[]{const l=buildLPS(p),r:number[]=[];let i=0,j=0;while(i<t.length){if(p[j]===t[i]){i++;j++;}if(j===p.length){r.push(i-j);j=l[j-1];}else if(i<t.length&&p[j]!==t[i]){if(j)j=l[j-1];else i++;}}return r;}
```

### The Final Result: 283 characters (~23.3% of the original size)

Finally, let's ask large language models to further compress the code with any additional optimizations they can provide. The final result is only 283 characters long (~23.3% of the original size):

```typescript
function k(t:string,p:string){let l=new Array(p.length).fill(0),r=[],i=1,j=0;while(i<p.length)p[i]===p[j]?l[i++]=++j:j?j=l[j-1]:l[i++]=0;i=j=0;while(i<t.length){if(p[j]===t[i]){i++;j++;}if(j===p.length){r.push(i-j);j=l[j-1];}else if(i<t.length&&p[j]!==t[i])j?j=l[j-1]:i++;}return r;}
```

### Compressed JavaScript Output from JSCompress(348 characters, ~28.6% of the original size)

And below is the output from JSCompress, one of the most popular JavaScript compression tools. We compiled the original TypeScript code into JavaScript and then used JSCompress to compress it. But still this compressed code contains 348 characters (~28.6% of the original size). Considering that the above code is in TypeScript with type annotations, the final compressed code is actually even shorter than this.

```javascript
function buildLPS(n){const t=new Array(n.length).fill(0);let e=0,l=1;for(;l<n.length;)n[l]===n[e]?(e++,t[l]=e,l++):0!==e?e=t[e-1]:(t[l]=0,l++);return t}function kmpSearch(n,t){var e=buildLPS(t);const l=[];let r=0,h=0;for(;r<n.length;)t[h]===n[r]&&(r++,h++),h===t.length?(l.push(r-h),h=e[h-1]):r<n.length&&t[h]!==n[r]&&(0!==h?h=e[h-1]:r++);return l}
```

### Uncompress the Code and Explain

Now the deeply compressed code is significantly shorter while still preserving the core functionality of the original algorithm. The variable names have been shortened, and unnecessary whitespace has been removed. This demonstrates the power of code compression techniques in reducing file sizes and improving load times without sacrificing performance.

However, it may be difficult for humans to understand the compressed code. We can use large language models to explain the code, and reconstruct it into a more readable form.

> explain this code
> 
> function k(t:string,p:string){let l=new Array(p.length).fill(0),r=[],i=1,j=0;while(i<p.length)p[i]===p[j]?l[i++]=++j:j?j=l[j-1]:l[i++]=0;i=j=0;while(i<t.length){if(p[j]===t[i]){i++;j++;}if(j===p.length){r.push(i-j);j=l[j-1];}else if(i<t.length&&p[j]!==t[i])j?j=l[j-1]:i++;}return r;}

And here is the explanation provided by the large language model:

```markdown
The following TypeScript function implements the **Knuth-Morris-Pratt (KMP)** string search algorithm to find all occurrences of a pattern `p` in text `t`.


function k(t: string, p: string) {
    let l = new Array(p.length).fill(0), // LPS (Longest Prefix Suffix) array
        r = [],                          // result array: starting indices of matches
        i = 1,                           // index for building LPS
        j = 0;                           // prefix length or pattern index

    // Build the LPS array
    while (i < p.length)
        if (p[i] === p[j])
            l[i++] = ++j;
        else
            j ? j = l[j - 1] : l[i++] = 0;

    i = j = 0; // reset indices for searching

    // Search in text
    while (i < t.length) {
        if (p[j] === t[i]) { i++; j++; }

        if (j === p.length) {
            r.push(i - j);        // match found, record position
            j = l[j - 1];         // continue searching for next match
        }
        else if (i < t.length && p[j] !== t[i])
            j ? j = l[j - 1] : i++;
    }
    return r;
}

What the code does
✅ Inputs
- t: the text to search within
- p: the pattern to search for

✅ Outputs
- Returns an array r of starting indices where p occurs in t.

✅ Steps
1️⃣ Build LPS array (l)
The LPS array tells us for each position in p, the length of the longest proper prefix which is also a suffix — it’s used to skip characters when a mismatch happens.

2️⃣ Search
Iterate through t:
- If characters match, advance both i (text index) and j (pattern index).
- If a full match is found (j == p.length), record the starting position and update j using LPS.
- If mismatch:
  - If j > 0, use LPS to skip characters.
  - Else, move to next char in text.

Example usage

console.log(k("ababcabcabababd", "ababd")); 
// Output: [10]  (pattern starts at index 10 in the text)


Summary
👉 The function k efficiently searches for all occurrences of a pattern using KMP.
👉 Time complexity: O(t.length + p.length)
👉 Space complexity: O(p.length) (for the LPS array)
```

From the explanation, we can see that the compressed code is indeed a valid implementation of the KMP algorithm, and it provides a clear understanding of how the algorithm works. The large language model can help us reconstruct the code into a more readable form if needed. This demonstrates the power of large language models in understanding and explaining even highly compressed code.

## Example 2: JSON simple parser in C++

### Original Code in C++(2708 characters)

Here is another example of a simple JSON parser in C++. The original code is 2708 characters long.

```cpp
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <memory>
#include <cctype>

struct JsonValue {
    enum Type { OBJECT, ARRAY, STRING, NUMBER, BOOL, NIL } type;
    std::map<std::string, std::shared_ptr<JsonValue>> obj;
    std::vector<std::shared_ptr<JsonValue>> arr;
    std::string str;
    double num = 0;
    bool boolean = false;

    JsonValue(Type t) : type(t) {}
};

struct JsonParser {
    std::string s;
    size_t i = 0;

    JsonParser(const std::string& s) : s(s) {}

    void skip() {
        while (i < s.size() && isspace(s[i])) i++;
    }

    std::shared_ptr<JsonValue> parse() {
        skip();
        if (s[i] == '{') return parseObject();
        if (s[i] == '[') return parseArray();
        if (s[i] == '"') return parseString();
        if (isdigit(s[i]) || s[i] == '-') return parseNumber();
        if (s.compare(i, 4, "true") == 0) { i += 4; auto v = std::make_shared<JsonValue>(JsonValue::BOOL); v->boolean = true; return v; }
        if (s.compare(i, 5, "false") == 0) { i += 5; auto v = std::make_shared<JsonValue>(JsonValue::BOOL); v->boolean = false; return v; }
        if (s.compare(i, 4, "null") == 0) { i += 4; return std::make_shared<JsonValue>(JsonValue::NIL); }
        return nullptr;
    }

    std::shared_ptr<JsonValue> parseObject() {
        auto v = std::make_shared<JsonValue>(JsonValue::OBJECT);
        i++; skip();
        if (s[i] == '}') { i++; return v; }
        while (true) {
            skip();
            auto key = parseString();
            skip();
            i++; // skip :
            skip();
            v->obj[key->str] = parse();
            skip();
            if (s[i] == '}') { i++; break; }
            i++; // skip ,
        }
        return v;
    }

    std::shared_ptr<JsonValue> parseArray() {
        auto v = std::make_shared<JsonValue>(JsonValue::ARRAY);
        i++; skip();
        if (s[i] == ']') { i++; return v; }
        while (true) {
            v->arr.push_back(parse());
            skip();
            if (s[i] == ']') { i++; break; }
            i++; // skip ,
        }
        return v;
    }

    std::shared_ptr<JsonValue> parseString() {
        auto v = std::make_shared<JsonValue>(JsonValue::STRING);
        i++; // skip "
        while (s[i] != '"') {
            if (s[i] == '\\') i++; // skip escape
            v->str += s[i++];
        }
        i++; // skip "
        return v;
    }

    std::shared_ptr<JsonValue> parseNumber() {
        auto v = std::make_shared<JsonValue>(JsonValue::NUMBER);
        size_t start = i;
        if (s[i] == '-') i++;
        while (isdigit(s[i])) i++;
        if (s[i] == '.') {
            i++;
            while (isdigit(s[i])) i++;
        }
        v->num = std::stod(s.substr(start, i - start));
        return v;
    }
};
```

### The Compressed Code in C++(1330 characters, ~49.1% of the original size)

Here is the compressed version of the code, which is 1330 characters long (~49.1% of the original size):

```cpp
#include<iostream>
#include<string>
#include<map>
#include<vector>
#include<memory>
#include<cctype>
using namespace std;
struct J{enum T{O,A,S,N,B,L}t;map<string,shared_ptr<J>>o;vector<shared_ptr<J>>a;string s;double n=0;bool b=0;J(T t):t(t){}};
struct P{string s;size_t i=0;P(const string&x):s(x){}void k(){while(i<s.size()&&isspace(s[i]))i++;}shared_ptr<J>p(){k();if(s[i]=='{')return po();if(s[i]=='[')return pa();if(s[i]=='"')return ps();if(isdigit(s[i])||s[i]=='-')return pn();if(s.compare(i,4,"true")==0){i+=4;auto v=make_shared<J>(J::B);v->b=1;return v;}if(s.compare(i,5,"false")==0){i+=5;auto v=make_shared<J>(J::B);return v;}if(s.compare(i,4,"null")==0){i+=4;return make_shared<J>(J::L);}return 0;}shared_ptr<J>po(){auto v=make_shared<J>(J::O);i++;k();if(s[i]=='}'){i++;return v;}while(1){k();auto k_=ps();k();i++;k();v->o[k_->s]=p();k();if(s[i]=='}'){i++;break;}i++;}return v;}shared_ptr<J>pa(){auto v=make_shared<J>(J::A);i++;k();if(s[i]==']'){i++;return v;}while(1){v->a.push_back(p());k();if(s[i]==']'){i++;break;}i++;}return v;}shared_ptr<J>ps(){auto v=make_shared<J>(J::S);i++;while(s[i]!='"'){if(s[i]=='\\')i++;v->s+=s[i++];}i++;return v;}shared_ptr<J>pn(){auto v=make_shared<J>(J::N);size_t st=i;if(s[i]=='-')i++;while(isdigit(s[i]))i++;if(s[i]=='.'){i++;while(isdigit(s[i]))i++;}v->n=stod(s.substr(st,i-st));return v;}};
```

### The compressed code in C++ by jsonminify.com(2144 characters, ~79.2% of the original size)

Below is the output from jsonminify.com, a popular JSON compression tool. The original code is compiled into a JSON-like format and then compressed. The result is 2144 characters long (~79.2% of the original size).

```cpp
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <memory>
#include <cctype>
struct JsonValue { enum Type { OBJECT, ARRAY, STRING, NUMBER, BOOL, NIL } type; std::map<std::string, std::shared_ptr<JsonValue>> obj; std::vector<std::shared_ptr<JsonValue>> arr; std::string str; double num = 0; bool boolean = false; JsonValue(Type t) : type(t) {}};struct JsonParser { std::string s; size_t i = 0; JsonParser(const std::string& s) : s(s) {} void skip() { while (i < s.size() && isspace(s[i])) i++; } std::shared_ptr<JsonValue> parse() { skip(); if (s[i] == '{') return parseObject(); if (s[i] == '[') return parseArray(); if (s[i] == '"') return parseString(); if (isdigit(s[i]) || s[i] == '-') return parseNumber(); if (s.compare(i, 4, "true") == 0) { i += 4; auto v = std::make_shared<JsonValue>(JsonValue::BOOL); v->boolean = true; return v; } if (s.compare(i, 5, "false") == 0) { i += 5; auto v = std::make_shared<JsonValue>(JsonValue::BOOL); v->boolean = false; return v; } if (s.compare(i, 4, "null") == 0) { i += 4; return std::make_shared<JsonValue>(JsonValue::NIL); } return nullptr; } std::shared_ptr<JsonValue> parseObject() { auto v = std::make_shared<JsonValue>(JsonValue::OBJECT); i++; skip(); if (s[i] == '}') { i++; return v; } while (true) { skip(); auto key = parseString(); skip(); i++;  skip(); v->obj[key->str] = parse(); skip(); if (s[i] == '}') { i++; break; } i++;  } return v; } std::shared_ptr<JsonValue> parseArray() { auto v = std::make_shared<JsonValue>(JsonValue::ARRAY); i++; skip(); if (s[i] == ']') { i++; return v; } while (true) { v->arr.push_back(parse()); skip(); if (s[i] == ']') { i++; break; } i++;  } return v; } std::shared_ptr<JsonValue> parseString() { auto v = std::make_shared<JsonValue>(JsonValue::STRING); i++;  while (s[i] != '"') { if (s[i] == '\\') i++;  v->str += s[i++]; } i++;  return v; } std::shared_ptr<JsonValue> parseNumber() { auto v = std::make_shared<JsonValue>(JsonValue::NUMBER); size_t start = i; if (s[i] == '-') i++; while (isdigit(s[i])) i++; if (s[i] == '.') { i++; while (isdigit(s[i])) i++; } v->num = std::stod(s.substr(start, i - start)); return v; }};
```

## Conclusion

This exploration demonstrates the significant potential of applying systematic code compression techniques to maximize the utility of large language models (LLMs) in software engineering workflows such as vibe coding and SWE Agent operations. By following carefully designed style guides that emphasize minimizing unnecessary whitespace, shortening variable names, reducing structural redundancy, and leveraging advanced language features, we can dramatically reduce source code size — often achieving reductions to 20-50% of the original character count without sacrificing core functionality.