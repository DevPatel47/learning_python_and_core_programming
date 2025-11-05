## 🔹 BASIC LEVEL — Conceptual & Syntax-Oriented

### 🧩 Python Basics
1. What is Python, and why is it called a “high-level” language?  
   **Answer:** 
2. What’s the difference between compiled and interpreted languages?  
   **Answer:** 
3. How is Python executed internally (bytecode, interpreter, PVM)?  
   **Answer:** 
4. What are identifiers, keywords, and variables in Python?  
   **Answer:** 
5. Explain Python’s indentation rule. Why is it mandatory?  
   **Answer:** 
6. What are the naming conventions in Python?  
   **Answer:** 
7. What’s the difference between expressions and statements?  
   **Answer:** 
8. How do comments work in Python? Difference between `#` and docstrings?  
   **Answer:** 

### 💡 Programming Model & REPL
1. What is the REPL, and how is it useful for Python development?  
   **Answer:** 
2. What are the four components of REPL (Read, Eval, Print, Loop)?  
   **Answer:** 
3. Difference between running a `.py` file and using the REPL shell?  
   **Answer:** 
4. Interactive vs script mode?  
   **Answer:** 
5. Can you execute multiline code in REPL? How?  
   **Answer:** 
6. How can you recall or modify previous commands in REPL?  
   **Answer:** 

### ⚙️ Setup: Python / VS Code / Git
1. How do you check the installed Python version?  
   **Answer:** 
2. How do you set up a Python virtual environment?  
   **Answer:** 
3. How do you run a Python file in VS Code?  
   **Answer:** 
4. What is PEP 8, and how do you enable linting in VS Code?  
   **Answer:** 
5. Explain Git’s three areas — working directory, staging area, and repository.  
   **Answer:** 
6. Common Git commands (`init`, `clone`, `commit`, `push`, etc.).  
   **Answer:** 
7. How do you link a repo to a remote origin?  
   **Answer:** 
8. What’s `.gitignore`, and why is it used?  
   **Answer:** 

### 🖥️ Input / Output
1. Syntax and return type of `input()`?  
   **Answer:** 
2. Convert user input from string to int or float.  
   **Answer:** 
3. Print multiple items in one line.  
   **Answer:** 
4. Difference between `print(x)` and `print(f"{x}")`.  
   **Answer:** 
5. Use of `end` and `sep` parameters in `print()`.  
   **Answer:** 
6. What happens if you call `input` incorrectly?  
   **Answer:** 
7. How to handle input errors safely?  
   **Answer:** 

### 🔢 Data Types & Casting
1. List all primitive data types.  
   **Answer:** 
2. Difference between `int`, `float`, `bool`, `str`.  
   **Answer:** 
3. Convert string `"123"` to integer.  
   **Answer:** 
4. Output of `bool("")`, `bool(0)`, `bool("0")`.  
   **Answer:** 
5. Implicit vs explicit casting.  
   **Answer:** 
6. Difference between `float("nan")` and `None`.  
   **Answer:** 
7. What does `type()` return?  
   **Answer:** 

### ⚖️ Operators & Precedence
1. List operator categories (arithmetic, logical, bitwise …).  
   **Answer:** 
2. Difference between `==` and `is`.  
   **Answer:** 
3. Explain operator precedence.  
   **Answer:** 
4. What does `//` do?  
   **Answer:** 
5. Difference between `/` and `//`.  
   **Answer:** 
6. Evaluate `3 + 2 * 4`.  
   **Answer:** 
7. Precedence of `not`, `and`, `or`.  
   **Answer:** 
8. Output of `2 ** 3 ** 2`.  
   **Answer:** 

---

## 🔸 INTERMEDIATE LEVEL — Logic & Debug-Oriented

### Python Basics
1. Why is Python dynamically typed?  
   **Answer:** 
2. Mutable vs immutable types (examples).  
   **Answer:** 
3. How does Python handle memory management?  
   **Answer:** 
4. Explain variables under the hood (namespaces & scopes).  
   **Answer:** 
5. Shallow vs deep copy.  
   **Answer:** 

### Programming Model & REPL
1. Describe Python’s execution model (source → bytecode → execution).  
   **Answer:** 
2. Difference between interpreter loop and REPL loop.  
   **Answer:** 
3. Handling syntax errors interactively.  
   **Answer:** 

### Setup / Git / VS Code
1. Purpose of `.venv` folders.  
   **Answer:** 
2. Debugging a Python script in VS Code.  
   **Answer:** 
3. Configuring `launch.json` for debugging.  
   **Answer:** 
4. Rollback or undo commits in Git.  
   **Answer:** 
5. `git merge` vs `git rebase`.  
   **Answer:** 
6. Resolving merge conflicts.  
   **Answer:** 
7. Workflow: clone → branch → edit → commit → push → PR.  
   **Answer:** 

### Input / Output
1. Handle multiple inputs in a single line (`map()`).  
   **Answer:** 
2. Read multiple lines efficiently.  
   **Answer:** 
3. Redirect input/output in terminal.  
   **Answer:** 
4. f-strings vs `.format()` vs `%` formatting.  
   **Answer:** 
5. Print to stderr instead of stdout.  
   **Answer:** 

### Data Types & Casting
1. Cast `"3.5"` to int — what happens?  
   **Answer:** 
2. Results of `int(True)` and `int(False)`.  
   **Answer:** 
3. Output of `str([1,2,3])` and `list("123")`.  
   **Answer:** 
4. Convert between ASCII and chars (`ord()`, `chr()`).  
   **Answer:** 
5. Mixing numeric & boolean ops: `1 + True`, `1 + False`.  
   **Answer:** 

### Operators & Precedence
1. Explain short-circuit evaluation.  
   **Answer:** 
2. Output of `not True == False`.  
   **Answer:** 
3. Bitwise vs logical operators.  
   **Answer:** 
4. Operator overloading (`__add__`, `__mul__`).  
   **Answer:** 
5. Example of precedence causing a bug.  
   **Answer:** 

---

## 🔺 PROFESSIONAL LEVEL — Deep / Google-Style

### Python Internals & Execution Model
1. Explain Python’s LEGB rule.  
   **Answer:** 
2. How does the interpreter compile to bytecode and execute?  
   **Answer:** 
3. What is the Global Interpreter Lock (GIL)?  
   **Answer:** 
4. CPython vs PyPy vs Jython vs IronPython.  
   **Answer:** 
5. How REPL stores previous outputs (`_`, `__`, `___`).  
   **Answer:** 
6. Explain Python’s call-stack model simply.  
   **Answer:** 

### Setup / Tooling / Git Workflow
1. Detached HEAD vs normal commit.  
   **Answer:** 
2. Interactive rebase and squash.  
   **Answer:** 
3. `git fetch` vs `git pull`.  
   **Answer:** 
4. Automating environment setup for new devs.  
   **Answer:** 
5. Use of `.editorconfig`, `.env`, `.gitconfig`, `requirements.txt`.  
   **Answer:** 

### Input / Output & Type Systems
1. Handle encoding/decoding (UTF-8 vs ASCII).  
   **Answer:** 
2. Validate user input type dynamically.  
   **Answer:** 
3. Difference between `raw_input()` and `input()`.  
   **Answer:** 
4. Measure I/O performance.  
   **Answer:** 
5. Logging output instead of printing.  
   **Answer:** 

### Operators & Optimization
1. How does Python evaluate chained comparisons (`1 < x < 5`)?  
   **Answer:** 
2. Precedence impact in functional expressions.  
   **Answer:** 
3. Augmented assignments (`+=`, `*=`) vs normal ones.  
   **Answer:** 
4. Difference between  
   `a = b = [1,2]; a += [3]`
   and
   `a = b = [1,2]; a = a + [3]`
   **Answer:**
5. How Python evaluates expression trees.  
   **Answer:** 
