# 首个AI编程风格指南

作者：Xinran Wang(lidangzzz)

## 快速开始

在您喜欢的文本编辑器中打开 [`AI_Coding_Style_Guide_prompts.toml`](AI_Coding_Style_Guide_prompts.toml) 文件，您将找到一组可用于指导大型语言模型压缩代码的提示。您可以使用这些提示来指导大型语言模型遵循编码风格指南，并根据本文档中概述的原则压缩代码。

如果您想在自己的项目中使用这些提示，您可以复制 `AI_Coding_Style_Guide_prompts.toml` 文件的内容并将其粘贴到您自己的提示管理系统中。您也可以修改这些提示以满足您的特定需求。

如果您想将这些提示加载到您自己的提示管理系统中，您可以使用以下代码片段：

```python
import toml 
from pathlib import Path
def load_prompts(file_path: str) -> dict:
    """从 TOML 文件中加载提示。"""
    return toml.load(Path(file_path))
prompts = load_prompts("AI_Coding_Style_Guide_prompts.toml")
```

## 引言

当我使用氛围编程（vibe coding）或SWE Agent时，经常遇到上下文窗口大小不足的问题。如果我们一次性输入多个源代码文件，而总长度超过了上下文窗口，就被迫只能选择性地包含部分文件。这会导致大语言模型丢失部分必要的上下文。

另一个问题是，大多数当前的氛围编程或SWE Agent工具都按token使用量收费，因为大语言模型的API提供商也是按消耗的token数量向这些工具收费。在这种情况下，源代码越长，需要的token就越多——不仅导致成本线性增加，还会导致token输出的时间成本线性增加。

为了使大语言模型能够在固定的上下文窗口内处理更多的源代码文件、模块和功能——并节省更多token——我们设计了这套编程风格指南。这套指南既包括常见编程语言的通用编程风格指南，也包括针对特定语言和场景的专用指南。

我们的目标是在各种编程语言中最大化代码压缩，同时保持合理的人类可读性水平，以便在实现紧凑性和可读性之间平衡的同时，尽可能节省上下文窗口。

## 原则

我们创建这套编程风格指南是因为我们相信三个基本趋势，这些趋势反映了我们在软件工程和与大语言模型协作方面的第一性原理思考：

1. 大语言模型的能力将持续提升，逐渐超越普通的人类程序员。大语言模型已经能够理解这些极度压缩的代码形式，而且它们的理解能力只会变得更强。

2. 大语言模型的上下文窗口总是感觉不够用。无论是32k、64k、256k、1M token还是更多，提示工程师总是希望能够塞入更多的代码和上下文。以前我们只能放入两三个文件，最终可能希望包含数十个甚至数百个文件。

3. 当氛围编程或SWE Agent工具承担主要编程任务时，代码可读性的重要性逐渐降低。人类缺乏时间或意愿详细审查所有代码；相反，他们更关心功能是否完整。为了最大化氛围编程或SWE Agent的效率，在某种程度上牺牲代码可读性变得合理——减少不必要的冗余，如过长的变量名、多余的空格、换行符、制表符等。

4. 代码的可靠性应该越来越依赖于细粒度的单元测试，而不是人工代码审查的结果。全面的单元测试可以帮助确保整个代码库的代码质量。然而，更多的单元测试意味着更多的整体代码，这进一步增加了代码压缩的需求。

5. 如果人类工程师希望介入进行调试或优化，但无法理解高度压缩的代码，大语言模型可以通过解释代码片段或将其重构为更详细、更易于人类阅读的形式来提供全面协助，以便进行详细分析和决策。无需担心压缩代码会变得无法理解——我们应该相信大语言模型和SWE Agent是人类的朋友和助手，随时准备协助恢复和澄清压缩代码。

## 基本编程风格规则

基于这些核心原则，我们精心设计了一套SWE Agent或氛围编程工具应该遵循的基本规则：

1. 最小化不必要的缩进、空格和换行符，保持代码紧凑。

2. 对于顶层函数、类和模块名称，尽可能坚持正确和完整的命名约定。对于函数、类或模块内部的代码——特别是临时变量——减少变量名长度以最小化代码大小。

3. 为顶层函数、类和模块提供简洁但必要的注释，描述它们的目的、输入和输出。在函数内部，除非绝对必要，否则避免注释。

4. 在可能的情况下，在单个文件中实现更多的函数、类或模块，特别是当它们相互关联时。只有当代码服务于不同的模块或功能时，才将代码分离到不同的文件中。

5. 使用高级语言特性和设计来减少代码大小——例如，在适当的时候优先使用lambda函数而不是完整的函数定义；利用能显著缩短代码的语法糖；在C++或TypeScript等静态类型语言中，使用类型推断来减少代码冗长。

6. 对于需要重用的模块、函数或类，将它们抽象为独立单元以实现重用并减少总体代码量。

7. 避免不必要的代码重复，如重复的逻辑或类似的函数。相反，使用高阶函数、装饰器或mixins来封装通用逻辑。

8. 使用第三方库时，优先选择简洁高效的库，它们能提供必要的功能而不会产生过多开销。

9. 让大语言模型处理代码压缩过程，因为它可以自动应用这些原则以达到最佳效果。

## 压缩级别

我们可以进一步将压缩过程分为不同的级别，每个级别都有其自己的重点和权衡。下表概述了这些级别、它们的描述以及每个阶段使用的具体技术：

| 级别 | 描述 | 空白符移除 | 代码压缩 | 变量名缩短 | 导出名称保留 | 注释处理 | 高级重构 |
| ----- | ------------------------------------------- | --------------------------------- | ----------------------------- | ---------------------- | --------------------- | --------------------- | -------------------- |
| **1** | 移除不必要的空格和换行符 | ✅ 基本（多余空格和换行符） | ❌ | ❌ | ✅ | ✅ 保留所有注释 | ❌ |
| **2** | 通过合并行轻微压缩代码 | ✅ 基本 | ✅ 轻微合并（相同逻辑） | ❌ | ✅ | ✅ 保留所有注释 | ❌ |
| **3** | 缩短局部变量名 | ✅ 基本 | ✅ | ✅ 仅局部 | ✅ | ✅ 保留所有注释 | ❌ |
| **4** | 缩短局部和非导出名称 | ✅ 基本 | ✅ | ✅ 局部和非导出 | ✅ | ✅ 保留所有注释 | ❌ |
| **5** | 移除所有空白符并缩短标识符 | ✅ 完全（无空格、换行符） | ✅ 最大化紧凑性 | ✅ 局部和非导出 | ✅ | ✅ 仅保留注释 | ❌ |
| **6** | 移除注释（导出部分除外） | ✅ 完全 | ✅ | ✅ 局部和非导出 | ✅ | ☑️ 仅为导出部分 | ❌ |
| **7** | 移除所有注释 | ✅ 完全 | ✅ | ✅ 局部和非导出 | ✅ | ❌ 移除所有注释 | ❌ |
| **8** | 使用语言特性最小化代码 | ✅ 完全 | ✅ 最大化+重构 | ✅ 局部和非导出 | ✅ | ❌ 移除所有注释 | ✅ 使用任何特性 |

## 示例1：KMP字符串匹配算法

### TypeScript原始代码（1216个字符）

以下是如何在TypeScript中应用这些原则的简单示例。下面是KMP字符串匹配算法的演示。原始代码中有1216个字符。

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

### TypeScript轻微压缩代码（795个字符，约为原始大小的65.4%）

在移除不必要的空格和换行符但保留所有代码缩进后，代码减少到795个字符（约为原始大小的65.4%）：

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

### 深度压缩至715个字符（约为原始大小的58.7%）

接下来，让我们移除所有不必要的空格、换行符和缩进，得到高度压缩的代码版本，只有715个字符（约为原始大小的58.7%）：

```typescript
// Function to build the Longest Prefix Suffix (LPS) array
function buildLPS(pattern:string):number[]{const lps:number[]=new Array(pattern.length).fill(0);let len=0,i=1;while(i<pattern.length){if(pattern[i]===pattern[len]){len++;lps[i]=len;i++;}else{if(len!==0){len=lps[len-1];}else{lps[i]=0;i++;}}}return lps;}
// KMP search function: returns all starting indices where pattern is found in text
function kmpSearch(text:string,pattern:string):number[]{const lps=buildLPS(pattern);const result:number[]=[];let i=0,j=0;while(i<text.length){if(pattern[j]===text[i]){i++;j++;}if(j===pattern.length){result.push(i-j);j=lps[j-1];}else if(i<text.length&&pattern[j]!==text[i]){if(j!==0){j=lps[j-1];}else{i++;}}}return result;}
```

### 进一步压缩至443个字符（约为原始大小的36.4%）

接下来，让我们移除注释并将变量名减少到必要的最小值，同时保持它们的可理解性。最终代码只有443个字符（约为原始大小的36.4%）：

```typescript
function buildLPS(p:string):number[]{const l:number[]=new Array(p.length).fill(0);let l0=0,i=1;while(i<p.length){if(p[i]===p[l0]){l0++;l[i]=l0;i++;}else if(l0){l0=l[l0-1];}else{l[i]=0;i++;}}return l;}
function kmpSearch(t:string,p:string):number[]{const l=buildLPS(p),r:number[]=[];let i=0,j=0;while(i<t.length){if(p[j]===t[i]){i++;j++;}if(j===p.length){r.push(i-j);j=l[j-1];}else if(i<t.length&&p[j]!==t[i]){if(j)j=l[j-1];else i++;}}return r;}
```

### 最终结果：283个字符（约为原始大小的23.3%）

最后，让我们请大语言模型进一步压缩代码，提供任何可能的额外优化。最终结果只有283个字符（约为原始大小的23.3%）：

```typescript
function k(t:string,p:string){let l=new Array(p.length).fill(0),r=[],i=1,j=0;while(i<p.length)p[i]===p[j]?l[i++]=++j:j?j=l[j-1]:l[i++]=0;i=j=0;while(i<t.length){if(p[j]===t[i]){i++;j++;}if(j===p.length){r.push(i-j);j=l[j-1];}else if(i<t.length&&p[j]!==t[i])j?j=l[j-1]:i++;}return r;}
```

### JSCompress压缩的JavaScript输出（348个字符，约为原始大小的28.6%）

以下是JSCompress的输出，这是最受欢迎的JavaScript压缩工具之一。我们将原始TypeScript代码编译成JavaScript，然后使用JSCompress进行压缩。但这个压缩代码仍然包含348个字符（约为原始大小的28.6%）。考虑到上面的代码是带有类型注释的TypeScript，最终压缩代码实际上比这个还要短。

```javascript
function buildLPS(n){const t=new Array(n.length).fill(0);let e=0,l=1;for(;l<n.length;)n[l]===n[e]?(e++,t[l]=e,l++):0!==e?e=t[e-1]:(t[l]=0,l++);return t}function kmpSearch(n,t){var e=buildLPS(t);const l=[];let r=0,h=0;for(;r<n.length;)t[h]===n[r]&&(r++,h++),h===t.length?(l.push(r-h),h=e[h-1]):r<n.length&&t[h]!==n[r]&&(0!==h?h=e[h-1]:r++);return l}
```

### 解压缩代码并解释

现在深度压缩的代码显著缩短了，同时仍然保留了原始算法的核心功能。变量名已经缩短，不必要的空白符已被移除。这展示了代码压缩技术在减少文件大小和提高加载时间方面的强大能力，而不会牺牲性能。

然而，人类可能难以理解压缩代码。我们可以使用大语言模型来解释代码，并将其重构为更易读的形式。

> 解释这段代码
> 
> function k(t:string,p:string){let l=new Array(p.length).fill(0),r=[],i=1,j=0;while(i<p.length)p[i]===p[j]?l[i++]=++j:j?j=l[j-1]:l[i++]=0;i=j=0;while(i<t.length){if(p[j]===t[i]){i++;j++;}if(j===p.length){r.push(i-j);j=l[j-1];}else if(i<t.length&&p[j]!==t[i])j?j=l[j-1]:i++;}return r;}

以下是大语言模型提供的解释：

```markdown
以下TypeScript函数实现了**Knuth-Morris-Pratt (KMP)**字符串搜索算法，用于在文本`t`中查找模式`p`的所有出现位置。

function k(t: string, p: string) {
    let l = new Array(p.length).fill(0), // LPS（最长前缀后缀）数组
        r = [],                          // 结果数组：匹配的起始索引
        i = 1,                           // 用于构建LPS的索引
        j = 0;                           // 前缀长度或模式索引

    // 构建LPS数组
    while (i < p.length)
        if (p[i] === p[j])
            l[i++] = ++j;
        else
            j ? j = l[j - 1] : l[i++] = 0;

    i = j = 0; // 重置索引以进行搜索

    // 在文本中搜索
    while (i < t.length) {
        if (p[j] === t[i]) { i++; j++; }

        if (j === p.length) {
            r.push(i - j);        // 找到匹配，记录位置
            j = l[j - 1];         // 继续搜索下一个匹配
        }
        else if (i < t.length && p[j] !== t[i])
            j ? j = l[j - 1] : i++;
    }
    return r;
}

代码功能
✅ 输入
- t: 要搜索的文本
- p: 要搜索的模式

✅ 输出
- 返回数组r，包含p在t中出现的起始索引。

✅ 步骤
1️⃣ 构建LPS数组(l)
LPS数组告诉我们对于p中的每个位置，最长的既是前缀又是后缀的长度——它用于在发生不匹配时跳过字符。

2️⃣ 搜索
遍历t：
- 如果字符匹配，推进i（文本索引）和j（模式索引）。
- 如果找到完整匹配（j == p.length），记录起始位置并使用LPS更新j。
- 如果不匹配：
  - 如果j > 0，使用LPS跳过字符。
  - 否则，移动到文本中的下一个字符。

示例用法

console.log(k("ababcabcabababd", "ababd")); 
// 输出: [10]  （模式在文本中从索引10开始）

总结
👉 函数k使用KMP高效搜索模式的所有出现位置。
👉 时间复杂度：O(t.length + p.length)
👉 空间复杂度：O(p.length)（用于LPS数组）
```

从解释中可以看出，压缩代码确实是KMP算法的有效实现，它清楚地说明了算法的工作原理。如果需要，大语言模型可以帮助我们将代码重构为更易读的形式。这展示了大语言模型在理解和解释甚至高度压缩代码方面的强大能力。

## 示例2：C++中的简单JSON解析器

### C++原始代码（2708个字符）

这是C++中简单JSON解析器的另一个示例。原始代码有2708个字符。

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

### C++压缩代码（1330个字符，约为原始大小的49.1%）

这是代码的压缩版本，有1330个字符（约为原始大小的49.1%）：

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

### 通过 jsonminify.com 压缩的 C++ 代码（2144 字符，约为原始大小的 79.2%）

以下是来自 jsonminify.com 的输出，这是一个流行的 JSON 压缩工具。原始代码被编译成类似 JSON 的格式，然后进行压缩。结果长度为 2144 字符（约为原始大小的 79.2%）。

```cpp
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <memory>
#include <cctype>
struct JsonValue { enum Type { OBJECT, ARRAY, STRING, NUMBER, BOOL, NIL } type; std::map<std::string, std::shared_ptr<JsonValue>> obj; std::vector<std::shared_ptr<JsonValue>> arr; std::string str; double num = 0; bool boolean = false; JsonValue(Type t) : type(t) {}};struct JsonParser { std::string s; size_t i = 0; JsonParser(const std::string& s) : s(s) {} void skip() { while (i < s.size() && isspace(s[i])) i++; } std::shared_ptr<JsonValue> parse() { skip(); if (s[i] == '{') return parseObject(); if (s[i] == '[') return parseArray(); if (s[i] == '"') return parseString(); if (isdigit(s[i]) || s[i] == '-') return parseNumber(); if (s.compare(i, 4, "true") == 0) { i += 4; auto v = std::make_shared<JsonValue>(JsonValue::BOOL); v->boolean = true; return v; } if (s.compare(i, 5, "false") == 0) { i += 5; auto v = std::make_shared<JsonValue>(JsonValue::BOOL); v->boolean = false; return v; } if (s.compare(i, 4, "null") == 0) { i += 4; return std::make_shared<JsonValue>(JsonValue::NIL); } return nullptr; } std::shared_ptr<JsonValue> parseObject() { auto v = std::make_shared<JsonValue>(JsonValue::OBJECT); i++; skip(); if (s[i] == '}') { i++; return v; } while (true) { skip(); auto key = parseString(); skip(); i++;  skip(); v->obj[key->str] = parse(); skip(); if (s[i] == '}') { i++; break; } i++;  } return v; } std::shared_ptr<JsonValue> parseArray() { auto v = std::make_shared<JsonValue>(JsonValue::ARRAY); i++; skip(); if (s[i] == ']') { i++; return v; } while (true) { v->arr.push_back(parse()); skip(); if (s[i] == ']') { i++; break; } i++;  } return v; } std::shared_ptr<JsonValue> parseString() { auto v = std::make_shared<JsonValue>(JsonValue::STRING); i++;  while (s[i] != '"') { if (s[i] == '\\') i++;  v->str += s[i++]; } i++;  return v; } std::shared_ptr<JsonValue> parseNumber() { auto v = std::make_shared<JsonValue>(JsonValue::NUMBER); size_t start = i; if (s[i] == '-') i++; while (isdigit(s[i])) i++; if (s[i] == '.') { i++; while (isdigit(s[i])) i++; } v->num = std::stod(s.substr(start, i - start)); return v; }};
```

## 结论

这项探索展示了将系统化代码压缩技术应用于最大化大型语言模型（LLMs）在软件工程工作流程中的实用性的巨大潜力，例如氛围编码和 SWE Agent 操作。通过遵循精心设计的风格指南，强调最小化不必要的空白、缩短变量名、减少结构冗余，并利用高级语言特性，我们可以显著减少源代码大小——通常能够实现减少到原始字符数的 20-50%，而不会牺牲核心功能。