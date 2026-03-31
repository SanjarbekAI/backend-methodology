# L10 — File I/O & Modules Intro

## Why this matters
Programs that only work with data typed by a user forget everything the moment they close. Files give your program **memory** — save a report, load a config, log an event. And modules let you stop reinventing the wheel by using Python's massive built-in toolkit.

---

## Topics

## `open()`, `read()`, `write()` — Working with files
To work with a file, you must first **open** it. `open()` returns a file object. Always specify the **mode**.

| Mode | Meaning |
|---|---|
| `"r"` | Read (default) — fails if file doesn't exist |
| `"w"` | Write — creates file or **overwrites** existing content |
| `"a"` | Append — adds to the end without erasing |
| `"x"` | Create — fails if file already exists |

```python
# Writing to a file
f = open("notes.txt", "w")       # open for writing (creates if not exists)
f.write("First line\n")          # write a string — \n adds a new line
f.write("Second line\n")
f.close()                        # ALWAYS close the file when done

# Reading the entire file
f = open("notes.txt", "r")
content = f.read()               # reads everything as one big string
print(content)
f.close()

# Reading line by line
f = open("notes.txt", "r")
for line in f:                   # iterate over lines directly
    print(line.strip())          # .strip() removes the \n at end of each line
f.close()
```

> ⚠️ **Common mistake:** Forgetting to call `.close()`. An unclosed file can cause data loss or locked files. The solution is the `with` statement — see next section.

---

## `with` statement — The safe way to handle files
The `with` statement automatically closes the file when the block ends — even if an error occurs. Always prefer `with` over manual `open()`/`close()`.

```python
# Writing with 'with'
with open("report.txt", "w") as f:
    f.write("Sales Report — March 2026\n")
    f.write("Total: 4,200,000 sum\n")
# file is automatically closed here

# Reading with 'with'
with open("report.txt", "r") as f:
    content = f.read()
    print(content)

# Reading all lines into a list
with open("report.txt", "r") as f:
    lines = f.readlines()           # returns a list of strings, one per line
    print(lines)

# Appending to an existing file
with open("report.txt", "a") as f:
    f.write("Status: Approved\n")   # adds to the end, does not erase
```

> ⚠️ **Common mistake:** Using `"w"` mode when you meant `"a"`. Mode `"w"` **erases the entire file** before writing. Use `"a"` to add to existing content.

---

## `import` — Bringing in extra tools
Python comes with a large **standard library** — hundreds of ready-to-use modules. You bring them into your script with `import`.

```python
import math                      # import the entire math module
print(math.pi)                   # 3.141592653589793
print(math.sqrt(144))            # 12.0
print(math.ceil(4.3))            # 5 — rounds up
print(math.floor(4.9))           # 4 — rounds down

import random                    # random number tools
print(random.randint(1, 100))    # random integer between 1 and 100
print(random.choice(["a", "b", "c"]))  # random item from a list
random.shuffle([1, 2, 3, 4, 5]) # shuffles a list in-place

import os                        # operating system tools
print(os.getcwd())               # current working directory
print(os.path.exists("report.txt"))  # True/False — does the file exist?
```

**Importing specific items to avoid typing the module name each time:**
```python
from math import sqrt, pi        # import only what you need
print(sqrt(81))                  # 9.0 — no "math." prefix needed
print(pi)                        # 3.14159...

from random import randint
print(randint(1, 6))             # simulates a dice roll
```

> ⚠️ **Common mistake:** Using `from module import *` (star import). It imports everything and pollutes your namespace with unknown names, making bugs very hard to trace. Always import only what you need.

---

## Standard library modules — A sampler
```python
import datetime
today = datetime.date.today()
print(today)                     # 2026-03-30

import sys
print(sys.version)               # Python version info

import json                      # (covered in depth in L19)
data = {"name": "Ali", "age": 25}
print(json.dumps(data))          # '{"name": "Ali", "age": 25}'

import string
print(string.ascii_letters)      # abcdefghijklmnopqrstuvwxyzABCDE...
print(string.digits)             # 0123456789
```

---

## Quick reference

| Syntax | What it does | Example |
|---|---|---|
| `open(file, mode)` | Open a file | `open("a.txt", "r")` |
| `f.read()` | Read entire file as string | `content = f.read()` |
| `f.readlines()` | Read all lines into a list | `lines = f.readlines()` |
| `f.write(str)` | Write string to file | `f.write("hello\n")` |
| `f.close()` | Close the file | `f.close()` |
| `with open(...) as f:` | Safe file handling (auto-close) | `with open("a.txt") as f:` |
| `"r"` mode | Read (default) | `open("f.txt", "r")` |
| `"w"` mode | Write (overwrites!) | `open("f.txt", "w")` |
| `"a"` mode | Append (adds to end) | `open("f.txt", "a")` |
| `import module` | Import a module | `import math` |
| `from module import x` | Import specific item | `from math import sqrt` |
| `math.sqrt(x)` | Square root | `math.sqrt(16)` → `4.0` |
| `random.randint(a, b)` | Random int between a and b | `random.randint(1, 6)` |
| `os.path.exists(path)` | Check if file/dir exists | `os.path.exists("f.txt")` |

---

## Task list

1. The daily log writer
2. The config file reader
3. The student records saver
4. The dice simulator
5. The file backup tool
6. The word count analyzer

