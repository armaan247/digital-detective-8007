# Mission 03 — Understand the Operating System

---

## 1. Mission Title

**Mission 03: Understand the Operating System**

---

## 2. Task / Objective

Explore how macOS manages the computer by checking system details, running processes, disk storage, directory paths, and file permissions, and explain the core responsibilities of an operating system.

---

## 3. Work Completed

### Task 3.1 — Explore Your Operating System

All identifying details (username and personal home directory path) have been replaced with `[redacted]`.

| Information Explored | What It Tells You | Your Observation (Privacy-Safe) |
|----------------------|-------------------|---------------------------------|
| **Operating system / system details** (`sw_vers`, `uname -smr`) | Identifies the OS name, version, build, kernel, and CPU architecture | `macOS 27.2.1` (Build `26B131`), kernel `Darwin 27.2.0`, architecture `arm64` |
| **Current account identity** (`whoami`) | Shows which user account is active in the current Terminal session and determines file access rights | `[redacted]` |
| **Available and used storage** (`df -h /`) | Reports filesystem size, used space, and free space on the mounted disk | Root mount `/` (`/dev/disk3s1s1`): `460Gi` total, `13Gi` used on the system volume, `229Gi` available |
| **System activity snapshot** (`top -l 1 -n 8`) | Summarises total running/sleeping processes, CPU load, and memory consumption at a moment in time | `828` total processes (`3` running, `825` sleeping, `4032` threads); CPU `7.71%` user, `11.42%` sys, `80.85%` idle; `15G` physical memory used (`556M` unused) |

---

### Task 3.2 — Understand Processes

I inspected running processes using `top -l 1 -n 8` and `ps -eo pid,pcpu,pmem,comm | head -n 15`.

- **What is a process?**
  A process is a running instance of a program in memory, including its code, data, and execution state managed by the OS.
- **What does the PID column represent?**
  `PID` stands for **Process Identifier** — a unique number assigned by the operating system to each running process so it can schedule, monitor, or control that process individually.
- **Two examples of processes observed on my computer:**
  1. `Google Chrome Helper` (observed at PID `36773` in `top`) — a browser helper process handling web page rendering/tabs.
  2. `/sbin/launchd` (PID `1` in `ps`) and `mdworker_shared` (PID `36776` in `top`) — background OS processes that manage system services and Spotlight search indexing.

---

### Task 3.3 — Understand Paths and Permissions

#### Navigating Paths

Starting from the repository root (`/Users/[redacted]/Desktop/digital-detective-8007`), moving into `mission-02-terminal/terminal-practice` changed `pwd` to `/Users/[redacted]/Desktop/digital-detective-8007/mission-02-terminal/terminal-practice`. Running `cd ../..` moved back up two levels to `/Users/[redacted]/Desktop/digital-detective-8007`.

- **Absolute path vs. Relative path:**
  An **absolute path** gives the full location starting from the filesystem root `/`, so it points to the exact same item regardless of your current directory. A **relative path** gives the location starting from your current working directory.
  - **Absolute path example:** `/Users/[redacted]/Desktop/digital-detective-8007/mission-02-terminal/terminal-practice/notes.txt`
  - **Relative path example:** `mission-02-terminal/terminal-practice/notes.txt` (from the repository root) or `../..` (to return to the parent two levels up).

#### Checking File Permissions

Running `ls -l notes.txt` inside `mission-02-terminal/terminal-practice/` returned:

```text
-rw-r--r--@ 1 [redacted]  staff  76 Nov 25 23:59 notes.txt
```

- The leading `-` indicates a regular file.
- The next three characters (`rw-`) show the **owner's permissions**:
  - `r` — the owner **can read** the file.
  - `w` — the owner **can write (edit)** the file.
  - `-` — the owner **cannot execute** the file as a program.
- Group and other users have `r--` (read-only access). No system permissions were changed.

| Permission | Meaning | Example |
|------------|---------|---------|
| `r` — Read | Allows a file's contents to be read. | Opening or printing `notes.txt` with `cat`. |
| `w` — Write | Allows a file to be modified or overwritten. | Appending text to `notes.txt`. |
| `x` — Execute | Allows a file to be run as a program; on a directory, allows entering/traversing it. | Running a shell script or entering a folder with `cd`. |

---

### Task 3.4 — Explain Operating-System Responsibilities

| OS Responsibility | Your Explanation | Example |
|-------------------|------------------|---------|
| **Process management** | Starts, schedules, tracks, and ends running programs, giving each one CPU time without letting them interfere with each other. | Assigning PID `1` to `launchd` and scheduling `Google Chrome Helper` alongside Terminal commands. |
| **Memory management** | Allocates RAM to active programs, keeps track of free vs. used memory, and prevents one program from overwriting another's memory. | Allocating `48M` of memory to `Google Chrome Helper` and managing the `15G` used physical memory shown in `top`. |
| **Device management** | Communicates with hardware devices through drivers so applications can use keyboards, screens, disks, and networks cleanly. | Reading built-in keyboard input and rendering text onto the built-in display. |
| **File management** | Organises data into files and directories on storage drives and handles reading, writing, and naming files. | Storing `notes.txt` inside `mission-02-terminal/terminal-practice/` on `/dev/disk3s1s1`. |
| **User interface / shell** | Provides a way for users to interact with the computer, either graphically or through typed commands. | Using macOS Finder (GUI) or `zsh` inside Terminal (CLI) to run `ls` and `cd`. |
| **Security and permissions** | Controls user accounts and checks read, write, and execute permissions before allowing access to files or system operations. | Allowing only the owner `[redacted]` write access (`rw-`) to `notes.txt` while blocking other users from editing it. |

---

## 4. Commands / Tools Used

| Command / Tool | Purpose |
|----------------|---------|
| `sw_vers`, `uname -smr` | Checked macOS version, build number, kernel, and CPU architecture |
| `whoami` | Checked the currently active user account name |
| `df -h /` | Checked total, used, and available disk space on the root mount |
| `top -l 1 -n 8` | Captured a single-sample snapshot of processes, CPU, and memory usage |
| `ps -eo pid,pcpu,pmem,comm \| head -n 15` | Listed running processes with their PIDs and command paths |
| `pwd`, `cd` | Inspected absolute paths and moved between repository and subfolder paths |
| `ls -l` | Viewed detailed permissions for `notes.txt` in the practice directory |

---

## 5. My Understanding

- The operating system acts as the coordinator between hardware (CPU, RAM, SSD, devices) and user programs.
- Checking `top` and `ps` showed that hundreds of background processes (`828` total on this Mac) run quietly alongside the visible apps I open, and each process gets a unique PID.
- Understanding absolute vs. relative paths helps prevent mistakes when navigating folders in Terminal, while permissions (`r`, `w`, `x`) protect files from unintended edits or execution.

---

## 6. Difficulties Faced

- Interpreting the `df -h /` numbers on macOS APFS (`460Gi` total, `13Gi` used, `229Gi` available) was slightly confusing at first because other shared APFS volumes in the same container also share the disk space, and the raw `top`, `pwd`, and `ls -l` output contained my local username.

---

## 7. How I Resolved Them

- I focused on the `/` mount's available space (`229Gi`) to understand free storage on macOS and carefully replaced every occurrence of my username and home directory path with `[redacted]` in the README and evidence file.

---

## 8. Evidence / Files

| Evidence Item | Description |
|---------------|-------------|
| [Mission 03 README](README.md) | Notes and tables covering OS exploration, processes, paths, permissions, and OS responsibilities |
| [Mission 03 OS output](../evidence/mission-03-os-output.txt) | Privacy-safe copy of `sw_vers`, `uname`, `df -h`, `top`, `ps`, and `ls -l` outputs |

---

## 9. Commit Details

- Commit message: `Document operating system and file management`
- Commit hash: `f80ecfe`
- Branch: `main`
- Status: Pushed to `origin/main` and verified.
