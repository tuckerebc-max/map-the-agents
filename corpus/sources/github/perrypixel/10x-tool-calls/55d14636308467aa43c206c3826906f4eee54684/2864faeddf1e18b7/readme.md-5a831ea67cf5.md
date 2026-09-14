# 🚀 10x-Tool-Calls

**10x-Tool-Calls** is a simple rules setup designed for the **Cursor IDE**, **Windsurf**, or any other agent-based coding assistant that supports tool calls. It helps you get the **maximum value out of your monthly tool call allowance** by running your tasks in a loop with user input—without restarting the chat every time.

Note : This only works with Agent Mode
---

## ✅ What It Does

- After the AI completes a task, it runs a small Python script that asks:
  
```

prompt:

````

- You type your next instruction (e.g., `"add comments"`, `"refactor this"`, etc.)
- The AI uses that input to continue working.
- This loop repeats until:
- You you manually stop, or
- The session hits your **tool call limit**.

---

## 💡 Why This Matters

Most AI coding tools (like Cursor) offer **500 monthly requests**, but each request can include **up to 25 tool calls**. Normally, even saying `"hi"` uses up a full request, wasting potential.

With **10x-Tool-Calls**:
- You start with one request.
- Inside that session, you can give **multiple follow-ups**.
- All follow-ups run within the same request using available tool calls.
- This means you get **10x (or more)** actual work done using the same quota.

---

## ⚙️ How To Set It Up ( Basic Version )

### 1. Copy `userinput.py` in your root directory

This script is used to collect user input between tasks.

### 2. Copy `rules.md` into your IDE

* Open your IDE's rule configuration (e.g., in Cursor: .cursorrules file or project rules - set to “always”)
* Paste in the rules from `rules.md` (included in this repo)

That’s it! The system is now set to run in an interactive loop.

---

## 🧪 Current Version

* ✅ **Supports:** plain text input only
* ❌ **Not yet supported:** image upload or file drops (coming soon!)

A more advanced version is planned that will support:

* Image uploads
* File Drops

---

## ⚠️ Important Note

**Only use this setup with tools that offer a tool call–based quota**, not token-based pricing (like OpenAI’s pay-per-token). This setup is designed to **maximize bundled tool calls**, not minimize token usage.

---

## 🧠 Example

You have **500 monthly requests** and each request allows up to **25 tool calls**:

* Normally:
  `You say "hi" → AI replies "hi" = 1 request used.`

* With 10x-Tool-Calls:
  `You say "hi" → AI replies → runs prompt → you say "add comments" → AI continues... (up to 25 calls)`
  \= still **just 1 request used**, but you did much more.

---

Get more done. Use fewer requests. Save your quota.

**→ That’s the power of 10x-Tool-Calls.**

```

Let me know if you have any other requests
```

## Support
If you find this tool helpful, you can support the development by:
- Buying me a coffee at https://ko-fi.com/perrypixel
- UPI to kevinp@apl
