# Mission 04 — How Programs Run

---

## 1. Mission Title

**Mission 04: How Programs Run**

---

## 2. Task / Objective

Create and run a one-line Python 3 program (`hello.py`) from the Terminal, and compare how compilers and interpreters translate and execute programs.

---

## 3. Work Completed

### Task 4.1 — Create and Run a Python Program

I created [`hello.py`](hello.py) inside `mission-04-programs/` with the following single line of code:

```python
print("Hello from Python")
```

Running `python3 hello.py` from Terminal (using Python `3.14.6`) produced:

```text
Hello from Python
```

---

### Task 4.2 — Compare Compiler and Interpreter

| Point | Compiler | Interpreter |
|-------|----------|-------------|
| **When translation / execution happens** | Translates the entire source code file into machine code before the program starts running; the compiled binary is executed afterwards. | Reads and executes the program instruction by instruction at runtime without creating a separate machine-code executable first. |
| **Typical output** | Produces a standalone compiled executable file (or machine-code binary) that can run directly on the OS. | Produces the program's output directly during execution (no separate standalone executable file). |
| **One example** | C (`gcc` / `clang`) | Python (`python3`) |
| **One advantage** | Compiled programs usually run faster because translation is already done beforehand. | Easy to test and debug quickly because changes can be run right away without a separate compile step. |

#### Difference Between a Compiler and an Interpreter

As shown in the comparison table above, the main difference between a compiler and an interpreter is when translation happens. A compiler translates the whole program into machine code ahead of time and produces an executable file, which helps compiled programs run faster at runtime. An interpreter, like Python (`python3`), reads and carries out instructions directly while the program is running instead of generating a separate standalone binary first. This makes it quicker to write, edit, and test small scripts like `hello.py` immediately from the Terminal.

---

## 4. Commands / Tools Used

| Command / Tool | Purpose |
|----------------|---------|
| VS Code | Created and saved `mission-04-programs/hello.py` |
| `python3 --version` | Verified Python `3.14.6` was active in Terminal |
| `python3 mission-04-programs/hello.py` / `python3 hello.py` | Executed the Python script and verified it printed `Hello from Python` |
| `print()` (Python function) | Displayed text output to the Terminal screen |

---

## 5. My Understanding

- Computers cannot run human-readable source code directly; it has to be translated or interpreted into instructions the CPU can carry out.
- Running `hello.py` with `python3` showed how an interpreted workflow lets you edit a `.py` file and run it immediately with one command.
- Real language runtimes can also mix ideas from both approaches (for instance, Python compiles source code to bytecode internally before its virtual machine interprets it), while the core contrast between pre-compiling an executable and runtime execution remains clear.

---

## 6. Difficulties Faced

No major difficulties.

---

## 7. How I Resolved Them

Not applicable.

---

## 8. Evidence / Files

| Evidence Item | Description |
|---------------|-------------|
| [Mission 04 README](README.md) | Documents `hello.py` execution and the compiler vs. interpreter comparison |
| [hello.py](hello.py) | One-line Python program printing `Hello from Python` |
| [Mission 04 output](../evidence/mission-04-hello-output.txt) | Recorded `python3` version and `hello.py` execution output |

---

## 9. Commit Details

- Commit message: `Compare compilers and interpreters`
- Branch: `main`
- Status: Ready to commit and push to `origin/main`.
