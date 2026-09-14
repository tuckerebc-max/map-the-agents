# 首個AI程式風格指南

作者：Xinran Wang(lidangzzz)

## 快速開始

在您喜歡的文本編輯器中打開 [`AI_Coding_Style_Guide_prompts.toml`](AI_Coding_Style_Guide_prompts.toml) 檔案，您將找到一組可用於指導大型語言模型壓縮程式碼的提示。您可以使用這些提示來指導大型語言模型遵循編碼風格指南，並根據本文檔中概述的原則壓縮程式碼。

如果您想在自己的專案中使用這些提示，您可以複製 `AI_Coding_Style_Guide_prompts.toml` 檔案的內容並將其貼到您自己的提示管理系統中。您也可以修改這些提示以滿足您的特定需求。

如果您想將這些提示載入您自己的提示管理系統中，您可以使用以下程式碼片段：

```python
import toml 
from pathlib import Path
def load_prompts(file_path: str) -> dict:
    """從 TOML 文件中加載提示。"""
    return toml.load(Path(file_path))
prompts = load_prompts("AI_Coding_Style_Guide_prompts.toml")
```

## 引言

當我使用氛圍編程（vibe coding）或SWE Agent時，經常遇到上下文視窗大小不足的問題。如果我們一次性輸入多個源碼檔案，而總長度超過了上下文視窗，就被迫只能選擇性地包含部分檔案。這會導致大型語言模型丟失部分必要的上下文。

另一個問題是，大多數當前的氛圍編程或SWE Agent工具都按token使用量收費，因為大型語言模型的API提供商也是按消耗的token數量向這些工具收費。在這種情況下，源碼越長，需要的token就越多——不僅導致成本線性增加，還會導致token輸出的時間成本線性增加。

為了使大型語言模型能夠在固定的上下文視窗內處理更多的源碼檔案、模組和功能——並節省更多token——我們設計了這套編程風格指南。這套指南既包括常見編程語言的通用編程風格指南，也包括針對特定語言和場景的專用指南。

我們的目標是在各種編程語言中最大化程式碼壓縮，同時保持合理的人類可讀性水平，以便在實現緊湊性和可讀性之間平衡的同時，盡可能節省上下文視窗。

## 原則

我們創建這套編程風格指南是因為我們相信三個基本趨勢，這些趨勢反映了我們在軟體工程和與大型語言模型協作方面的第一性原理思考：

1. 大型語言模型的能力將持續提升，逐漸超越普通的人類程式設計師。大型語言模型已經能夠理解這些極度壓縮的程式碼形式，而且它們的理解能力只會變得更強。

2. 大型語言模型的上下文視窗總是感覺不夠用。無論是32k、64k、256k、1M token還是更多，提示工程師總是希望能夠塞入更多的程式碼和上下文。以前我們只能放入兩三個檔案，最終可能希望包含數十個甚至數百個檔案。

3. 當氛圍編程或SWE Agent工具承擔主要編程任務時，程式碼可讀性的重要性逐漸降低。人類缺乏時間或意願詳細審查所有程式碼；相反，他們更關心功能是否完整。為了最大化氛圍編程或SWE Agent的效率，在某種程度上犧牲程式碼可讀性變得合理——減少不必要的冗餘，如過長的變數名、多餘的空格、換行符、制表符等。

4. 程式碼的可靠性應該越來越依賴細粒度的單元測試，而不是人工程式碼審查的結果。全面的單元測試可以幫助確保整個程式庫的程式碼品質。然而，更多的單元測試意味著更多的整體程式碼，這進一步增加了程式碼壓縮的需求。

5. 如果人類工程師希望介入進行除錯或優化，但無法理解高度壓縮的程式碼，大型語言模型可以透過解釋程式碼片段或將其重構為更詳細、更易於人類閱讀的形式來提供全面協助，以便進行詳細分析和決策。無需擔心壓縮程式碼會變得無法理解——我們應該相信大型語言模型和SWE Agent是人類的朋友和助手，隨時準備協助恢復和澄清壓縮程式碼。

## 基本編程風格規則

基於這些核心原則，我們精心設計了一套SWE Agent或氛圍編程工具應該遵循的基本規則：

1. 最小化不必要的縮排、空格和換行符，保持程式碼緊湊。

2. 對於頂層函式、類別和模組名稱，盡可能堅持正確和完整的命名約定。對於函式、類別或模組內部的程式碼——特別是臨時變數——減少變數名長度以最小化程式碼大小。

3. 為頂層函式、類別和模組提供簡潔但必要的註解，描述它們的目的、輸入和輸出。在函式內部，除非絕對必要，否則避免註解。

4. 在可能的情況下，在單一檔案中實現更多的函式、類別或模組，特別是當它們相互關聯時。只有當程式碼服務於不同的模組或功能時，才將程式碼分離到不同的檔案中。

5. 使用高階語言特性和設計來減少程式碼大小——例如，在適當的時候優先使用lambda函式而不是完整的函式定義；利用能顯著縮短程式碼的語法糖；在C++或TypeScript等靜態類型語言中，使用類型推斷來減少程式碼冗長。

6. 對於需要重用的模組、函式或類別，將它們抽象為獨立單元以實現重用並減少總體程式碼量。

7. 避免不必要的程式碼重複，如重複的邏輯或類似的函式。相反，使用高階函式、裝飾器或mixins來封裝通用邏輯。

8. 使用第三方函式庫時，優先選擇簡潔高效的函式庫，它們能提供必要的功能而不會產生過多開銷。

9. 讓大型語言模型處理程式碼壓縮過程，因為它可以自動應用這些原則以達到最佳效果。

## 壓縮級別

我們可以進一步將壓縮過程分為不同的級別，每個級別都有其自己的重點和權衡。下表概述了這些級別、它們的描述以及每個階段使用的具體技術：

| 級別 | 描述 | 空白符移除 | 程式碼壓縮 | 變數名縮短 | 匯出名稱保留 | 註解處理 | 高級重構 |
| ----- | ------------------------------------------- | --------------------------------- | ----------------------------- | ---------------------- | --------------------- | --------------------- | -------------------- |
| **1** | 移除不必要的空格和換行符 | ✅ 基本（多餘空格和換行符） | ❌ | ❌ | ✅ | ✅ 保留所有註解 | ❌ |
| **2** | 透過合併行輕微壓縮程式碼 | ✅ 基本 | ✅ 輕微合併（相同邏輯） | ❌ | ✅ | ✅ 保留所有註解 | ❌ |
| **3** | 縮短局部變數名 | ✅ 基本 | ✅ | ✅ 僅局部 | ✅ | ✅ 保留所有註解 | ❌ |
| **4** | 縮短局部和非匯出名稱 | ✅ 基本 | ✅ | ✅ 局部和非匯出 | ✅ | ✅ 保留所有註解 | ❌ |
| **5** | 移除所有空白符並縮短識別符 | ✅ 完全（無空格、換行符） | ✅ 最大化緊湊性 | ✅ 局部和非匯出 | ✅ | ✅ 僅保留註解 | ❌ |
| **6** | 移除註解（匯出部分除外） | ✅ 完全 | ✅ | ✅ 局部和非匯出 | ✅ | ☑️ 僅為匯出部分 | ❌ |
| **7** | 移除所有註解 | ✅ 完全 | ✅ | ✅ 局部和非匯出 | ✅ | ❌ 移除所有註解 | ❌ |
| **8** | 使用語言特性最小化程式碼 | ✅ 完全 | ✅ 最大化+重構 | ✅ 局部和非匯出 | ✅ | ❌ 移除所有註解 | ✅ 使用任何特性 |

## 範例1：KMP字串匹配演算法

### TypeScript原始程式碼（1216個字元）

以下是如何在TypeScript中應用這些原則的簡單範例。下面是KMP字串匹配演算法的示範。原始程式碼有1216個字元。

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

### TypeScript輕微壓縮程式碼（795個字元，約原始大小65.4%）

在移除不必要的空格和換行符但保留所有程式碼縮排後，程式碼減少到795個字元（約原始大小的65.4%）：

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

### 深度壓縮至715個字元（約原始大小58.7%）

接下來，讓我們移除所有不必要的空格、換行符和縮排，得到高度壓縮的程式碼版本，只有715個字元（約原始大小的58.7%）：

```typescript
// Function to build the Longest Prefix Suffix (LPS) array
function buildLPS(pattern:string):number[]{const lps:number[]=new Array(pattern.length).fill(0);let len=0,i=1;while(i<pattern.length){if(pattern[i]===pattern[len]){len++;lps[i]=len;i++;}else{if(len!==0){len=lps[len-1];}else{lps[i]=0;i++;}}}return lps;}
// KMP search function: returns all starting indices where pattern is found in text
function kmpSearch(text:string,pattern:string):number[]{const lps=buildLPS(pattern);const result:number[]=[];let i=0,j=0;while(i<text.length){if(pattern[j]===text[i]){i++;j++;}if(j===pattern.length){result.push(i-j);j=lps[j-1];}else if(i<text.length&&pattern[j]!==text[i]){if(j!==0){j=lps[j-1];}else{i++;}}}return result;}
```

### 進一步壓縮至443個字元（約原始大小36.4%）

接下來，讓我們移除註解並將變數名減少到必要的最小值，同時保持它們的可理解性。最終程式碼只有443個字元（約原始大小的36.4%）：

```typescript
function buildLPS(p:string):number[]{const l:number[]=new Array(p.length).fill(0);let l0=0,i=1;while(i<p.length){if(p[i]===p[l0]){l0++;l[i]=l0;i++;}else if(l0){l0=l[l0-1];}else{l[i]=0;i++;}}return l;}
function kmpSearch(t:string,p:string):number[]{const l=buildLPS(p),r:number[]=[];let i=0,j=0;while(i<t.length){if(p[j]===t[i]){i++;j++;}if(j===p.length){r.push(i-j);j=l[j-1];}else if(i<t.length&&p[j]!==t[i]){if(j)j=l[j-1];else i++;}}return r;}
```

### 最終結果：283個字元（約原始大小23.3%）

最後，讓我們請大型語言模型進一步壓縮程式碼，提供任何可能的額外優化。最終結果只有283個字元（約原始大小的23.3%）：

```typescript
function k(t:string,p:string){let l=new Array(p.length).fill(0),r=[],i=1,j=0;while(i<p.length)p[i]===p[j]?l[i++]=++j:j?j=l[j-1]:l[i++]=0;i=j=0;while(i<t.length){if(p[j]===t[i]){i++;j++;}if(j===p.length){r.push(i-j);j=l[j-1];}else if(i<t.length&&p[j]!==t[i])j?j=l[j-1]:i++;}return r;}
```

### JSCompress壓縮的JavaScript輸出（348個字元，約原始大小28.6%）

以下是JSCompress的輸出，這是最受歡迎的JavaScript壓縮工具之一。我們將原始TypeScript程式碼編譯成JavaScript，然後使用JSCompress進行壓縮。但這個壓縮程式碼仍然包含348個字元（約原始大小的28.6%）。考慮到上面的程式碼是帶有類型註解的TypeScript，最終壓縮程式碼實際上比這還要短。

```javascript
function buildLPS(n){const t=new Array(n.length).fill(0);let e=0,l=1;for(;l<n.length;)n[l]===n[e]?(e++,t[l]=e,l++):0!==e?e=t[e-1]:(t[l]=0,l++);return t}function kmpSearch(n,t){var e=buildLPS(t);const l=[];let r=0,h=0;for(;r<n.length;)t[h]===n[r]&&(r++,h++),h===t.length?(l.push(r-h),h=e[h-1]):r<n.length&&t[h]!==n[r]&&(0!==h?h=e[h-1]:r++);return l}
```

### 解壓縮程式碼並解釋

現在深度壓縮的程式碼顯著縮短了，同時仍然保留了原始演算法的核心功能。變數名已經縮短，不必要的空白符已被移除。這展示了程式碼壓縮技術在減少檔案大小和提高載入時間方面的強大能力，而不會犧牲效能。

然而，人類可能難以理解壓縮程式碼。我們可以使用大型語言模型來解釋程式碼，並將其重構為更易讀的形式。

> 解釋這段程式碼
> 
> function k(t:string,p:string){let l=new Array(p.length).fill(0),r=[],i=1,j=0;while(i<p.length)p[i]===p[j]?l[i++]=++j:j?j=l[j-1]:l[i++]=0;i=j=0;while(i<t.length){if(p[j]===t[i]){i++;j++;}if(j===p.length){r.push(i-j);j=l[j-1];}else if(i<t.length&&p[j]!==t[i])j?j=l[j-1]:i++;}return r;}

以下是大型語言模型提供的解釋：

```markdown
以下TypeScript函式實現了**Knuth-Morris-Pratt (KMP)**字串搜尋演算法，用於在文字`t`中查找模式`p`的所有出現位置。

function k(t: string, p: string) {
    let l = new Array(p.length).fill(0), // LPS（最長前綴後綴）陣列
        r = [],                          // 結果陣列：匹配的起始索引
        i = 1,                           // 用於構建LPS的索引
        j = 0;                           // 前綴長度或模式索引

    // 構建LPS陣列
    while (i < p.length)
        if (p[i] === p[j])
            l[i++] = ++j;
        else
            j ? j = l[j - 1] : l[i++] = 0;

    i = j = 0; // 重置索引以進行搜尋

    // 在文字中搜尋
    while (i < t.length) {
        if (p[j] === t[i]) { i++; j++; }

        if (j === p.length) {
            r.push(i - j);        // 找到匹配，記錄位置
            j = l[j - 1];         // 繼續搜尋下一個匹配
        }
        else if (i < t.length && p[j] !== t[i])
            j ? j = l[j - 1] : i++;
    }
    return r;
}

程式功能  
✅ 輸入  
- t: 要搜尋的文字  
- p: 要搜尋的模式  

✅ 輸出  
- 返回陣列r，包含p在t中出現的起始索引。

✅ 步驟  
1️⃣ 構建LPS陣列(l)  
LPS陣列告訴我們對於p中每個位置，最長的既是前綴又是後綴的長度——它用於在發生不匹配時跳過字元。

2️⃣ 搜尋  
遍歷t：  
- 如果字元匹配，推進i（文字索引）和j（模式索引）。  
- 如果找到完整匹配（j == p.length），記錄起始位置並使用LPS更新j。  
- 如果不匹配：  
  - 如果j > 0，使用LPS跳過字元。  
  - 否則，移動到文字中的下一個字元。

示例用法

console.log(k("ababcabcabababd", "ababd")); 
// 輸出: [10]  （模式在文字中從索引10開始）

總結  
👉 函式k使用KMP高效搜尋模式的所有出現位置。  
👉 時間複雜度：O(t.length + p.length)  
👉 空間複雜度：O(p.length)（用於LPS陣列）  
```

從解釋中可以看出，壓縮程式碼確實是KMP演算法的有效實現，它清楚地說明了演算法的工作原理。如果需要，大型語言模型可以幫助我們將程式碼重構為更易讀的形式。這展示了大型語言模型在理解和解釋甚至高度壓縮程式碼方面的強大能力。

## 範例2：C++中的簡單JSON解析器

### C++原始程式碼（2708個字元）

這是C++中簡單JSON解析器的另一個範例。原始程式碼有2708個字元。

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

### C++壓縮程式碼（1330個字元，約原始大小49.1%）

這是程式碼的壓縮版本，有1330個字元（約原始大小的49.1%）：

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

### 通過 jsonminify.com 壓縮的 C++ 程式碼（2144字元，約原始大小79.2%）

以下是來自 jsonminify.com 的輸出，這是一個流行的 JSON 壓縮工具。原始程式碼被編譯成類似 JSON 的格式，然後進行壓縮。結果長度為2144字元（約原始大小的79.2%）。

```cpp
#include <iostream>
#include <string>
#include <map>
#include <vector>
#include <memory>
#include <cctype>
struct JsonValue { enum Type { OBJECT, ARRAY, STRING, NUMBER, BOOL, NIL } type; std::map<std::string, std::shared_ptr<JsonValue>> obj; std::vector<std::shared_ptr<JsonValue>> arr; std::string str; double num = 0; bool boolean = false; JsonValue(Type t) : type(t) {}};struct JsonParser { std::string s; size_t i = 0; JsonParser(const std::string& s) : s(s) {} void skip() { while (i < s.size() && isspace(s[i])) i++; } std::shared_ptr<JsonValue> parse() { skip(); if (s[i] == '{') return parseObject(); if (s[i] == '[') return parseArray(); if (s[i] == '"') return parseString(); if (isdigit(s[i]) || s[i] == '-') return parseNumber(); if (s.compare(i, 4, "true") == 0) { i += 4; auto v = std::make_shared<JsonValue>(JsonValue::BOOL); v->boolean = true; return v; } if (s.compare(i, 5, "false") == 0) { i += 5; auto v = std::make_shared<JsonValue>(JsonValue::BOOL); v->boolean = false; return v; } if (s.compare(i, 4, "null") == 0) { i += 4; return std::make_shared<JsonValue>(JsonValue::NIL); } return nullptr; } std::shared_ptr<JsonValue> parseObject() { auto v = std::make_shared<JsonValue>(JsonValue::OBJECT); i++; skip(); if (s[i] == '}') { i++; return v; } while (true) { skip(); auto key = parseString(); skip(); i++;  skip(); v->obj[key->str] = parse(); skip(); if (s[i] == '}') { i++; break; } i++;  } return v; } std::shared_ptr<JsonValue> parseArray() { auto v = std::make_shared<JsonValue>(JsonValue::ARRAY); i++; skip(); if (s[i] == ']') { i++; return v; } while (true) { v->arr.push_back(parse()); skip(); if (s[i] == ']') { i++; break; } i++;  } return v; } std::shared_ptr<JsonValue> parseString() { auto v = std::make_shared<JsonValue>(JsonValue::STRING); i++;  while (s[i] != '"') { if (s[i] == '\\') i++;  v->str += s[i++]; } i++;  return v; } std::shared_ptr<JsonValue> parseNumber() { auto v = std::make_shared<JsonValue>(JsonValue::NUMBER); size_t start = i; if (s[i] == '-') i++; while (isdigit(s[i])) i++; if (s[i] == '.') { i++; while (isdigit(s[i])) i++; } v->num = std::stod(s.substr(start, i - start)); return v; }};
```

## 結論

這項探索展示了將系統化程式碼壓縮技術應用於最大化大型語言模型（LLMs）在軟體工程工作流程中的實用性的巨大潛力，例如氛圍編碼和 SWE Agent 操作。透過遵循精心設計的風格指南，強調最小化不必要的空白、縮短變數名、減少結構冗餘，並利用高階語言特性，我們可以顯著減少源碼大小——通常能夠實現減少到原始字元數的20-50%，而不會犧牲核心功能。