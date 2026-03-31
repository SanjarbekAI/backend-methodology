# L34 — Git Fundamentals & Terminal Basics

## Why this matters
Every professional developer uses Git every single day — it is the difference between "I accidentally deleted my code" and "I'll just roll back to yesterday." Git also unlocks team collaboration: multiple people editing the same project simultaneously without overwriting each other's work. The terminal is the fastest way to talk to your computer, and every server in the world is managed through one.

---

## Topics

## The terminal — Your command center
The **terminal** (also called the shell or command line) is a text interface for your computer. Instead of clicking icons, you type commands. On Linux/macOS it's `bash` or `zsh`; on Windows it's PowerShell or Git Bash.

**Why developers use it:**
- Servers have no graphical interface — terminal is the only option
- Scripting and automation are much easier
- Git, databases, and most developer tools live here

```bash
# Navigate the filesystem
pwd                    # print working directory — where am I?
ls                     # list files in current folder
ls -la                 # list all files including hidden ones, with details
cd projects            # change directory into 'projects'
cd ..                  # go one level up
cd ~                   # go to home directory

# File operations
mkdir my-project       # create a new folder
touch README.md        # create an empty file (Linux/macOS)
cp file.txt copy.txt   # copy a file
mv file.txt other/     # move a file into another folder
rm file.txt            # delete a file (no trash — gone forever)
cat file.txt           # print file contents to screen
```

> ⚠️ **Common mistake:** `rm` on Linux/macOS is permanent. There is no Recycle Bin. Always double-check before pressing Enter, especially with `rm -rf`.

---

## What is Git?
Git is a **version control system** — it tracks every change you make to your code over time. Think of it like a save-point system in a video game: you can always go back to any previous save.

- **Repository (repo):** a folder tracked by Git
- **Commit:** a saved snapshot of your code at a point in time
- **Working directory:** your files as they exist right now
- **Staging area (index):** files you've marked as "ready to commit"

```
Working Directory  →  Staging Area  →  Repository (History)
  (edit files)         git add           git commit
```

> 💡 **Analogy:** Think of Git like a photographer taking portraits. Your working directory is the subject (messy hair, imperfect). `git add` is positioning the subject for the shot. `git commit` is clicking the shutter — that image is saved forever.

---

## Installing Git & first-time setup
```bash
# Check if Git is already installed
git --version

# Set your identity — this appears in every commit you make
git config --global user.name "Your Name"
git config --global user.email "you@example.com"

# Set VS Code as the default editor (optional but recommended)
git config --global core.editor "code --wait"

# See all your config settings
git config --list
```

> ⚠️ **Common mistake:** Skipping `git config` setup. Every commit will be attributed to a blank name, which looks unprofessional on GitHub and breaks team attribution.

---

## Creating a repository & making commits

```bash
# Start tracking an existing folder
cd my-project
git init                        # creates a hidden .git folder

# Check status — what has changed?
git status                      # most-used Git command — run it constantly

# Stage files for commit
git add README.md               # stage one specific file
git add .                       # stage ALL changed files in current folder

# Commit — save the snapshot
git commit -m "Initial commit: add README"

# View commit history
git log                         # full history
git log --oneline               # compact one-line-per-commit view
git log --oneline --graph       # visual branch graph
```

> ⚠️ **Common mistake:** Writing vague commit messages like `"fix"` or `"update"`. A good message completes the sentence: *"If applied, this commit will ___."* Example: `"Add login validation to user registration form"`.

---

## The .gitignore file
Tells Git which files to **never track** — secrets, dependencies, OS junk.

```bash
# .gitignore file — put this in your project root
__pycache__/          # Python bytecode cache
*.pyc                 # compiled Python files
.env                  # environment variables (passwords, API keys!)
venv/                 # virtual environment folder
.DS_Store             # macOS metadata file
*.log                 # log files
```

```bash
# Create and edit .gitignore
touch .gitignore
# Then add patterns to it, then:
git add .gitignore
git commit -m "Add .gitignore"
```

> ⚠️ **Common mistake:** Committing `.env` files with passwords or API keys to Git. Once pushed to GitHub, they are visible to the world and can never be truly erased from history.

---

## Viewing differences & undoing mistakes

```bash
# See what changed but hasn't been staged yet
git diff

# See what's staged and ready to commit
git diff --staged

# Unstage a file (remove from staging area, keep changes)
git restore --staged filename.py

# Discard changes in working directory (DANGEROUS — cannot undo)
git restore filename.py

# View a specific commit
git show abc1234                  # replace with actual commit hash

# Undo the last commit but KEEP the changes
git reset --soft HEAD~1

# Undo the last commit and DISCARD all changes (destructive)
git reset --hard HEAD~1
```

> ⚠️ **Common mistake:** Using `git reset --hard` without understanding it. This permanently deletes your uncommitted work. Use `--soft` when in doubt.

---

## Quick reference

| Command | What it does | Example |
|---|---|---|
| `git init` | Initialize a new repository | `git init` |
| `git status` | Show current state of working dir | `git status` |
| `git add <file>` | Stage file for commit | `git add main.py` |
| `git add .` | Stage all changes | `git add .` |
| `git commit -m` | Save staged snapshot | `git commit -m "message"` |
| `git log --oneline` | Compact commit history | `git log --oneline` |
| `git diff` | Show unstaged changes | `git diff` |
| `git diff --staged` | Show staged changes | `git diff --staged` |
| `git restore --staged` | Unstage a file | `git restore --staged app.py` |
| `git reset --soft HEAD~1` | Undo last commit, keep changes | `git reset --soft HEAD~1` |
| `.gitignore` | Exclude files from tracking | add `*.env` to file |

---

## Task list
1. Terminal navigation — the file explorer
2. First repository — a Python project
3. Staging area deep dive
4. Commit message discipline
5. The .gitignore guardian

---

## SQL LeetCode
- [Recyclable and Low Fat Products](https://leetcode.com/problems/recyclable-and-low-fat-products/) — 🟢 Easy
- [Find Customer Referee](https://leetcode.com/problems/find-customer-referee/) — 🟢 Easy

