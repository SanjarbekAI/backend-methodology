# L17 — Modules, Packages & Venv

## Why this matters
Real projects are never one file. They are organized into modules and packages, use dozens of third-party libraries, and need isolated environments so dependencies don't clash between projects. This is the infrastructure that every professional Python project is built on.

---

## Topics

## Creating modules — Your own reusable code files
A **module** is simply a `.py` file. Any Python file can be imported by another file. This lets you split a large project into logical, manageable pieces.

```python
# File: math_utils.py  ← this IS the module
def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

PI = 3.14159
```

```python
# File: main.py  ← this imports the module
import math_utils

print(math_utils.add(5, 3))        # 8
print(math_utils.PI)                # 3.14159

# Import specific items
from math_utils import multiply, PI
print(multiply(4, 5))               # 20

# Import with alias
import math_utils as mu
print(mu.add(10, 2))                # 12
```

> ⚠️ **Common mistake:** Having two files with the same name as a standard library module (e.g., naming your file `math.py` or `random.py`). Python might import your file instead of the standard library, causing confusing errors.

---

## Packages — Organizing modules into folders
A **package** is a folder containing multiple modules plus a special `__init__.py` file that tells Python "this folder is a package."

```
my_project/
├── main.py
└── utils/
    ├── __init__.py       ← makes 'utils' a package
    ├── math_utils.py
    ├── string_utils.py
    └── file_utils.py
```

```python
# In main.py
from utils.math_utils import add
from utils import string_utils      # import the whole module

print(add(3, 4))
print(string_utils.clean("  hello  "))
```

```python
# In utils/__init__.py — you can expose things at the package level
from .math_utils import add, multiply   # the . means "this package"
```

---

## `__name__` — Running a file vs importing it
Every Python file has a `__name__` attribute. When a file is run directly, `__name__` equals `"__main__"`. When it is imported, `__name__` equals the module name.

```python
# File: calculator.py

def calculate(a, b):
    return a + b

# This block only runs when you execute the file directly
# It does NOT run when another file imports calculator
if __name__ == "__main__":
    print("Running calculator directly")
    result = calculate(10, 5)
    print(f"Test result: {result}")
```

> ⚠️ **Common mistake:** Not using `if __name__ == "__main__":`. Without it, any code at the top level of a module runs on import — including print statements, network calls, or test code — which is almost never what you want.

---

## `pip` — Installing third-party packages
`pip` is Python's package manager. Third-party packages extend Python with extra functionality.

```bash
# In terminal:
pip install requests          # install a package
pip install requests==2.31.0  # install a specific version
pip uninstall requests        # remove a package
pip list                      # see all installed packages
pip show requests             # info about a specific package
```

---

## `virtualenv` / `venv` — Isolated environments
A **virtual environment** is an isolated Python installation for one project. It prevents dependency conflicts between projects.

```bash
# Create a virtual environment (built into Python 3)
python -m venv .venv

# Activate it (Windows PowerShell)
.venv\Scripts\Activate.ps1

# Activate it (Mac/Linux)
source .venv/bin/activate

# Now install packages — they go into .venv, not globally
pip install requests flask

# Deactivate when done
deactivate
```

---

## `requirements.txt` — Saving and sharing dependencies
```bash
# Save all installed packages to a file
pip freeze > requirements.txt

# Install all packages from the file (for teammates or deployment)
pip install -r requirements.txt
```

**Sample `requirements.txt`:**
```
requests==2.31.0
flask==3.0.2
python-dotenv==1.0.1
```

> ⚠️ **Common mistake:** Committing your `.venv/` folder to Git. Add it to `.gitignore` and share `requirements.txt` instead. The virtual environment can be recreated from `requirements.txt` on any machine.

---

## Quick reference

| Syntax / Command | What it does | Example |
|---|---|---|
| `import module` | Import a module | `import math_utils` |
| `from module import x` | Import specific item | `from utils import add` |
| `import module as alias` | Import with alias | `import numpy as np` |
| `__init__.py` | Makes a folder a package | Empty or with imports |
| `if __name__ == "__main__":` | Run only when file is executed directly | Standard pattern |
| `pip install pkg` | Install a package | `pip install requests` |
| `pip freeze > req.txt` | Save dependencies | — |
| `pip install -r req.txt` | Install from file | — |
| `python -m venv .venv` | Create virtual environment | — |
| `.venv\Scripts\Activate.ps1` | Activate venv (Windows) | — |

---

## Task list

1. The math utilities module
2. The string tools package
3. The project bootstrapper
4. The requirements analyzer
5. The module runner guard

