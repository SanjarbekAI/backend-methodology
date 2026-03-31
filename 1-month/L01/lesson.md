# L01 — Syntax, Output & Comments

## Why this matters
Every app you have ever used — Instagram, WhatsApp, Google Maps — started with a developer typing their very first line of code. That first line is almost always a `print()`. Understanding Python's syntax and structure is the foundation everything else is built on — skip it and nothing else makes sense.

---

## Topics

## `print()` — Talking to the screen
Python's `print()` function sends text or numbers to the screen. Think of it like texting — you write something, hit send, and it appears on the other side.

```python
print("Hello, world!")        # prints a message to the screen
print("My name is Ali")       # you can print any text you want
print(42)                      # you can also print numbers
print("I am", 20, "years old") # print can take multiple values, separated by commas
```

**Output:**
```
Hello, world!
My name is Ali
42
I am 20 years old
```

> ⚠️ **Common mistake:** Forgetting the parentheses — `print "Hello"` is Python 2 and will cause a `SyntaxError` in Python 3. Always write `print("Hello")`.

---

## Indentation — Python's rule of spacing
In most languages, blocks of code are wrapped in `{}` curly braces. Python is different — it uses **indentation** (spaces at the start of a line) to define blocks of code. Think of it like paragraphs in an essay: a new indent means a new idea that belongs to the one above it.

```python
# This is a simple if-statement — we'll learn these properly later
if True:
    print("This line is indented — it belongs to the if block")
    print("This line too!")
print("This line is NOT indented — it is outside the if block")
```

The standard is **4 spaces** per indent level. Never mix tabs and spaces.

> ⚠️ **Common mistake:** Using 2 spaces sometimes and 4 spaces other times, or mixing tabs with spaces. Python will throw an `IndentationError`. Pick 4 spaces and stick to it always.

---

## Code structure — How a Python file is organized
A Python file is read **top to bottom**, one line at a time. Order matters.

```python
# 1. Imports come first (we'll learn these in L10)
# import something

# 2. Then your code runs line by line
print("Step 1")   # this runs first
print("Step 2")   # this runs second
print("Step 3")   # this runs third
```

> ⚠️ **Common mistake:** Thinking Python skips around or runs things in a random order. It always goes top to bottom unless you explicitly tell it otherwise.

---

## Single-line comments — Notes for humans
A comment starts with `#`. Python completely ignores everything after `#` on that line. Comments are notes you write for yourself or other developers — they do not affect how the program runs.

```python
# This is a comment — Python ignores this line entirely
print("Hello")  # This comment is at the end of a code line — also ignored
# print("This line is commented out — it will NOT run")
```

**When to use comments:**
- Explain *why* you wrote something a certain way
- Temporarily disable a line of code while testing

> ⚠️ **Common mistake:** Writing comments that just repeat what the code says. `# prints hello` above `print("hello")` adds zero value. Instead, explain *why*.

---

## Multi-line comments — Longer notes
Python doesn't have a special multi-line comment syntax, but developers use **triple-quoted strings** (`"""..."""` or `'''...'''`) as a convention for writing longer descriptions. When used at the start of a function or file, they are called **docstrings**.

```python
"""
This is a multi-line string used as a comment.
You can write as many lines as you want.
Python won't execute this as code.
"""

print("The program still runs normally after the multi-line comment")

'''
You can also use single quotes.
Both triple-double and triple-single quotes work the same way.
'''
```

> ⚠️ **Common mistake:** Thinking `"""..."""` is the same as `#` comments everywhere. Inside a function, it becomes a docstring (a real string object). For quick notes, `#` is always safer and clearer.

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `print(value)` | Displays value on screen | `print("Hi")` |
| `print(a, b, c)` | Displays multiple values separated by space | `print("I am", 20)` |
| `# text` | Single-line comment — ignored by Python | `# my note` |
| `"""text"""` | Multi-line string / docstring | `"""Description"""` |
| 4 spaces indent | Defines a code block | ` print("inside")` |
| `\n` inside a string | Prints a new line | `print("a\nb")` |

---

## Task list

1. Hello, world!
2. Personal introduction card
3. The receipt printer
4. The commented blueprint
5. The story printer
6. The broken code fixer


