# 🐍 Backend Methodology — Python Engineering Curriculum

> A structured, hands-on course designed to take students from absolute zero to job-ready software engineers.

---

## 🎯 Goal

This repository is a complete, teacher-ready curriculum that guides students through the full journey of becoming a **backend software engineer** — starting from their very first `print()` statement and finishing with real-world design patterns, concurrency, and system-level Python.

Every lesson package is built to be handed directly to students, no extra preparation needed.

---

## 🗺️ Course Overview

| Duration | Lessons | Theme |
|---|---|---|
| **Month 1** | L01 – L11 | Python Basics & Instructions |
| **Month 2** | L12 – L22 | Functions & Intermediate Python |
| **Month 3** | L23 – L33 | OOP & Advanced Patterns |
| **Month 4** | L01 – L11 | *(upcoming)* |
| **Months 5–8** | — | *(upcoming)* |

**3 exams** — one at the end of each of the first three months.

---

## 📁 Repository Structure

```
backend-methodology/
├── 1-month/                  # Month 1 — Basics
│   ├── L01/                  #   lesson.md · tasks.md · homework.md
│   ├── L02/ … L11/
│   └── buggy-tasks/          #   bug_01.py … bug_06.py  (debug exercises)
│
├── 2-month/                  # Month 2 — Functions & Intermediate
│   ├── L01/ … L11/
│   └── buggy-tasks/
│
├── 3-month/                  # Month 3 — OOP & Advanced
│   ├── L01/ … L11/
│   └── buggy-tasks/
│
├── 4-month/                  # Month 4 — (in progress)
│   ├── L01/ … L11/
│   └── buggy-tasks/
│
├── exams/
│   ├── 1-month/
│   ├── 2-month/
│   └── …
│
└── should-be-added.txt       # Roadmap ideas for future additions
```

Each lesson folder contains:

| File | Purpose |
|---|---|
| `lesson.md` | Student-facing theory guide with code examples |
| `tasks.md` | Hands-on coding tasks with real-world scenarios |
| `homework.md` | Written reflection questions (no coding) |
| `leetcode.md` | LeetCode problems *(Month 3 onwards)* |

---

## 📚 What Students Learn

### Month 1 — Python Basics
`print()` · variables · data types · operators · strings · conditions · loops · lists · dicts · sets · user input · error handling · file I/O

### Month 2 — Functions & Intermediate Python
functions · scope · closures · decorators · generators · comprehensions · modules · RegEx · JSON · type hints · dataclasses

### Month 3 — OOP & Advanced
classes · inheritance · encapsulation · magic methods · abstract classes · SOLID & DRY · concurrency · context managers · metaclasses · performance & memory

---

## 🐛 Buggy Tasks

Every month includes a `buggy-tasks/` folder with **6 intentionally broken Python programs**.

Students must find every bug and fix the code — without rewriting it from scratch.
This trains **debugging skills, code reading, and attention to detail**.

| Batch | Recommended timing |
|---|---|
| `bug_01` – `bug_03` | After the 6th lesson of the month |
| `bug_04` – `bug_06` | After the 11th lesson of the month |

---

## 💡 Teaching Philosophy

- **Zero-to-engineer** — no prior programming experience required
- **Real-world scenarios** — every task is framed as a genuine problem (pharmacy stock, hotel pricing, taxi fares, e-commerce discounts …)
- **Theory + practice + reflection** — each lesson has code, tasks, and written homework
- **Progressive difficulty** — concepts build on each other lesson by lesson
- **LeetCode integration** — algorithm challenges introduced in Month 3 (2 problems/lesson + 2 SQL problems/lesson)
- **Debugging practice** — dedicated buggy-task sets every month

---

## 🚀 Planned Additions

Ideas tracked in [`should-be-added.txt`](notes/should-be-added.txt):

- 🎤 Student project presentations (communication & confidence)
- 👥 Pair programming sessions
- 🔍 Code review & refactoring workshops
- 🏗️ System design exercises
- 🎙️ Mock interviews & coding challenges
- 🏆 Hackathons & competitions
- 🗄️ Database replication & sharding labs

---

## 🛠️ Requirements

- Python **3.10+**
- No third-party packages required for Month 1 & 2
- Standard library only unless otherwise noted in the lesson

---

## 📄 License

This curriculum is for educational use. All lesson content, tasks, and materials were created for student learning purposes.

---

*Built with ❤️ to help the next generation of software engineers write their first line of code — and their thousandth.*

