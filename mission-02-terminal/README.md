# Mission 02 — Become Comfortable with the Terminal

---

## 1. Mission Title

**Mission 02: Become Comfortable with the Terminal**

---

## 2. Task / Objective

Practise using the macOS Terminal (command-line interface) inside the assignment repository to:

- Navigate folders and inspect directory contents using basic CLI commands.
- Create, write, append, copy, rename, and view text files safely inside a practice folder.
- Compare normal and flagged directory listings, and use a pipe (`|`) to limit command output.
- Check the installed package manager (Homebrew) version and managed package list without installing or removing software.

---

## 3. Work Completed

### Task 2.1 — Explore Basic Terminal Operations

All operations were executed inside the `digital-detective-8007` repository and the `mission-02-terminal/terminal-practice` folder.

| Operation / Command Name | What It Does | What I Observed |
|--------------------------|--------------|-----------------|
| Current-directory display (`pwd`) | Prints the full path of the folder I am currently inside | Displayed `/Users/[redacted]/Desktop/digital-detective-8007` |
| Directory listing (`ls`) | Lists visible files and folders in the current directory | Listed `README.md`, `evidence`, and all `mission-00` through `mission-08` folders in columns |
| Detailed listing (`ls -l`) | Shows permissions, link count, owner, group, byte size, modified date/time, and name | Displayed one line per item with byte sizes (e.g., `2059` bytes for `README.md`) and permission strings like `-rw-r--r--@` |
| Change directory (`cd ..` and `cd`) | Moves to the parent folder (`..`) or a named folder | Running `cd ..` moved one level up to `/Users/[redacted]/Desktop`, and `cd digital-detective-8007` brought me back |
| Create directory (`mkdir`) | Creates a new folder | Created the practice folder `mission-02-terminal/terminal-practice` cleanly |
| Create empty file (`touch`) | Creates a new empty file (or updates timestamp if it already exists) | Created `sample.txt` with a size of `0` bytes |
| Copy file (`cp`) | Duplicates a file to a new file name or path | Copied `sample.txt` to `sample_copy.txt`, keeping the original file intact |
| Move / rename file (`mv`) | Moves a file to another location or renames it | Renamed `sample_copy.txt` to `sample_renamed.txt` without leaving the old name behind |
| Display file contents (`cat`) | Prints the contents of a file directly in the Terminal | Printed both lines stored in `notes.txt`; returned nothing for the empty `sample.txt` |

---

### Task 2.2 — Practise File Changes Safely

Inside `mission-02-terminal/terminal-practice/`, I created `notes.txt`, wrote a first line using `>`, appended a second line using `>>`, verified both lines with `cat notes.txt`, created a backup copy (`notes_copy.txt`), and renamed the backup to `notes_backup.txt`.

Observed `cat notes.txt` output:

```text
First line: practising terminal commands
Second line: appending text safely
```

#### Answers to Questions

- **What is the difference between replacing a file's contents and adding text to the end?**
  Using `>` overwrites the file and replaces anything already inside it, whereas `>>` appends new text to the end of the file while keeping the existing lines.
- **What is the difference between copying a file and moving a file?**
  `cp` creates an independent duplicate so both the original and the copy exist, while `mv` relocates or renames the existing file so only the file at the new name/location remains.
- **What information does the current-directory display provide?**
  `pwd` shows the exact absolute path from the root directory `/` down to the folder currently open in the Terminal session.
- **Why is a directory-listing operation useful?**
  `ls` lets you confirm what files and folders exist at your current location, check file sizes and permissions with flags, and avoid typos before running other commands.

---

### Task 2.3 — Understand Flags and Pipes

#### Normal `ls` vs. `ls -lah`

- **`ls`** showed only the names of non-hidden files and folders (`README.md`, `evidence`, `mission-00-setup`, etc.).
- **`ls -lah`** combined three flags:
  - `-l` (long format): added permissions, owner, group, size, and last modified time.
  - `-a` (all): revealed hidden items starting with a dot (`.`, `..`, `.DS_Store`, `.git`, `.gitignore`).
  - `-h` (human-readable): showed file sizes with units like `12K`, `2.0K`, `512B`, and `10B` instead of raw byte counts.

#### Using a Pipe (`ls -la | head -n 5`)

- The pipe symbol `|` connects the output of the command on the left to the input of the command on the right.
- The left side (`ls -la`) produces the full detailed listing including hidden files (`16`+ lines in the repository root).
- The right side (`head -n 5`) reads that output and prints only the first 5 lines (`total 48`, `.`, `..`, `.DS_Store`, and `.git`).

---

### Task 2.4 — Understand Package Managers

Homebrew is installed on this Mac. Checking its version and managed list (without installing or removing anything) gave:

- `brew --version`: `Homebrew 7.0.10`
- `brew list`: Listed the installed formulae managed by Homebrew (including `git`, `ffmpeg`, `htop`, `openjdk`, `openssl@3`, and supporting libraries).

**Why package managers are useful:** A package manager automates finding, installing, updating, and removing software from trusted sources using simple commands. It also handles dependencies automatically, so required supporting libraries are installed and kept compatible without having to download files manually from different websites.

---

## 4. Commands / Tools Used

| Command / Tool | Purpose |
|----------------|---------|
| `pwd` | Displayed the current working directory path |
| `ls`, `ls -l`, `ls -lah` | Listed directory items in short, detailed, hidden, and human-readable formats |
| `cd` | Changed between the repository root, parent folder (`..`), and practice folder |
| `mkdir` | Created `mission-02-terminal/terminal-practice` |
| `touch` | Created empty file `sample.txt` |
| `cp` | Copied files (`sample.txt`, `notes.txt`) |
| `mv` | Renamed `sample_copy.txt` and `notes_copy.txt` |
| `cat` | Displayed file contents in Terminal |
| `echo`, `>`, `>>` | Wrote the initial line (`>`) and appended a second line (`>>`) in `notes.txt` |
| `\|` and `head -n 5` | Piped `ls -la` output to show only the first 5 lines |
| `brew --version`, `brew list` | Checked Homebrew version and listed already-installed formulae |

---

## 5. My Understanding

- The Terminal gives fast, direct control over folders and files using short commands and flags.
- Single redirection (`>`) vs. append redirection (`>>`) is an important distinction because `>` silently replaces existing file content.
- Flags modify a single command's behaviour (like `-l`, `-a`, and `-h` on `ls`), while pipes (`|`) chain multiple commands together so the output of one becomes the input of the next.
- Package managers like Homebrew keep CLI tools and their dependencies organised and easy to inspect or update.

---

## 6. Difficulties Faced

- When copying `ls -l` output for documentation, the raw output included my local macOS username and home folder path, so I had to make sure every private path and username was redacted before saving evidence.

---

## 7. How I Resolved Them

- I reviewed the saved Terminal output carefully and replaced my macOS username and home path with `[redacted]` before saving the evidence file and README.

---

## 8. Evidence / Files

| Evidence Item | Description |
|---------------|-------------|
| [Mission 02 README](README.md) | Complete command reference, answers, flags/pipes comparison, and Homebrew notes |
| [Terminal practice folder](terminal-practice/) | Practice folder containing `sample.txt`, `sample_renamed.txt`, `notes.txt`, and `notes_backup.txt` |
| [Mission 02 Terminal output](../evidence/mission-02-terminal-output.txt) | Privacy-safe copy of actual Terminal outputs observed during Mission 02 |

---

## 9. Commit Details

- Commit message: `Complete Terminal and file management mission`
- Commit hash: `c4d0f91`
- Branch: `main`
- Status: Pushed to `origin/main` and verified.
