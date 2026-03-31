# L35 — Git Branching, Merging & Team Workflows

## Why this matters
In a real team, five developers cannot all edit the same file on the same branch simultaneously — chaos would result. Branches are what make parallel development possible. You build your feature in isolation, then merge it in when it's ready. This is how every software company on earth — from a 2-person startup to Google — manages their code.

---

## Topics

## Branches — Parallel universes for your code
A **branch** is an independent line of development. The default branch is called `main` (or `master` in older repos). When you create a new branch, you get an exact copy of the code at that moment — changes you make there do not affect `main` until you merge.

```
main:    A --- B --- C
                      \
feature:               D --- E --- F
```

```bash
# List all branches (* marks the current one)
git branch

# Create a new branch
git branch feature/user-login

# Switch to a branch
git switch feature/user-login       # modern syntax (Git 2.23+)
git checkout feature/user-login     # older syntax (still works)

# Create AND switch in one command
git switch -c feature/payment       # -c = create

# Delete a branch (after merging)
git branch -d feature/user-login

# Force delete (even if not merged — be careful)
git branch -D feature/experiment
```

> ⚠️ **Common mistake:** Working directly on `main` instead of creating a feature branch. The `main` branch should always contain only tested, working code. All new work goes on a separate branch.

---

## Merging branches
Once your feature is complete and tested, you merge it back into `main`.

```bash
# Step 1: switch to the branch you want to merge INTO
git switch main

# Step 2: merge the feature branch into current branch
git merge feature/user-login

# Fast-forward merge (no divergence — Git just moves the pointer forward)
# Merge commit (branches diverged — Git creates a new commit joining them)

# After successful merge, delete the old branch
git branch -d feature/user-login
```

> 💡 **Analogy:** Branches are like separate whiteboards in an office. Everyone works on their own whiteboard. When someone's design is approved, you copy their work onto the main whiteboard. The separate whiteboard gets erased.

---

## Resolving merge conflicts
A **conflict** happens when two branches changed the **same line** of the same file. Git cannot decide which version to keep — it asks you.

```bash
# Git marks the conflict in the file like this:
<<<<<<< HEAD              # your current branch (main)
total = price * 1.12      # your version
=======
total = price * tax_rate  # incoming branch version
>>>>>>> feature/tax-calc

# You must:
# 1. Open the file
# 2. Delete the conflict markers
# 3. Keep the correct code (or combine both)
# 4. git add the file
# 5. git commit to finish the merge
```

```bash
# Abort a merge if you want to start over
git merge --abort
```

> ⚠️ **Common mistake:** Panicking when you see `<<<<<<< HEAD`. This is not broken — Git is just asking for your decision. Read both versions carefully, pick the right one, remove the markers, and commit.

---

## Remote repositories & GitHub/GitLab
A **remote** is a copy of your repository hosted on a server (GitHub, GitLab, Bitbucket). This is how teams share code.

```bash
# Connect your local repo to a remote
git remote add origin https://github.com/yourname/repo.git

# See existing remotes
git remote -v

# Push your branch to the remote for the first time
git push -u origin main         # -u sets upstream, only needed first time

# Push after the first time
git push

# Download remote changes without merging
git fetch origin

# Download AND merge remote changes into current branch
git pull                        # = git fetch + git merge

# Clone an existing repository from GitHub
git clone https://github.com/someone/project.git
```

> ⚠️ **Common mistake:** Running `git push` without `git pull` first when working in a team. If someone else pushed changes since your last pull, your push will be rejected. Always `git pull` before `git push`.

---

## The team workflow — Feature Branch Workflow
This is the standard workflow used in professional teams:

```
1.  git switch main && git pull          # start from latest main
2.  git switch -c feature/my-feature    # create feature branch
3.  ... make changes, commit often ...
4.  git push -u origin feature/my-feature
5.  Open a Pull Request (PR) on GitHub
6.  Team reviews your code
7.  After approval → merge PR into main on GitHub
8.  git switch main && git pull          # get the merged changes
9.  git branch -d feature/my-feature    # clean up
```

```bash
# Useful status commands when collaborating
git log --oneline --graph --all   # see all branches and their history
git branch -a                     # list local AND remote branches
git diff main..feature/my-feature # compare two branches
```

---

## Stashing — saving work temporarily
Sometimes you need to switch branches but you're not ready to commit. `git stash` saves your uncommitted work temporarily.

```bash
git stash                         # save current changes away
git stash list                    # see all stashes
git stash pop                     # restore the most recent stash
git stash apply stash@{1}         # restore a specific stash
git stash drop stash@{0}          # delete a stash
```

> ⚠️ **Common mistake:** Forgetting about stashes. `git stash list` can accumulate stashes over weeks. Always pop or drop them once you no longer need them.

---

## Quick reference

| Command | What it does | Example |
|---|---|---|
| `git branch` | List all local branches | `git branch` |
| `git switch -c <name>` | Create + switch to new branch | `git switch -c feature/auth` |
| `git switch <name>` | Switch to existing branch | `git switch main` |
| `git merge <branch>` | Merge branch into current | `git merge feature/auth` |
| `git branch -d <name>` | Delete merged branch | `git branch -d feature/auth` |
| `git remote add origin` | Connect local to remote | `git remote add origin <url>` |
| `git push -u origin <b>` | Push branch to remote | `git push -u origin main` |
| `git pull` | Fetch + merge from remote | `git pull` |
| `git clone <url>` | Copy a remote repo locally | `git clone <url>` |
| `git stash` | Temporarily save changes | `git stash` |
| `git stash pop` | Restore saved changes | `git stash pop` |
| `git log --graph --all` | Visual branch history | `git log --oneline --graph --all` |

---

## Task list
1. Branch and merge — the clean path
2. Simulating a merge conflict
3. Remote workflow — push and pull
4. The feature branch workflow end-to-end
5. Stash and recover

---

## SQL LeetCode
- [Big Countries](https://leetcode.com/problems/big-countries/) — 🟢 Easy
- [Article Views I](https://leetcode.com/problems/article-views-i/) — 🟢 Easy

