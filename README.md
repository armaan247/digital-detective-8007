# The Digital Detective

Welcome to **The Digital Detective**, a college assignment exploring how computers work from fundamentals through networking, Python programming, and version control. Each mission is documented in its own folder with hands-on Terminal outputs, verification results, and written reflections.

## Purpose

The purpose of this assignment is to build practical computer literacy by exploring real system behaviour on macOS and documenting each concept in clear, own-words notes inside a public GitHub repository.

## Mission Index

| Mission | Link | Short Description |
|---------|------|-------------------|
| Mission 00 | [Setup](mission-00-setup/README.md) | Repository creation, folder layout, and checking Python and Git versions |
| Mission 01 | [Computer Basics](mission-01-computer-basics/README.md) | IPOS trace in VS Code, Mac hardware/software classification, and everyday computer systems |
| Mission 02 | [Terminal](mission-02-terminal/README.md) | Basic CLI operations, safe file practice (`terminal-practice`), flags, pipes, and Homebrew check |
| Mission 03 | [Operating System](mission-03-operating-system/README.md) | macOS system info, processes and PIDs, absolute vs. relative paths, permissions, and OS roles |
| Mission 04 | [Programs](mission-04-programs/README.md) | Creating and running [`hello.py`](mission-04-programs/hello.py) and comparing compilers vs. interpreters |
| Mission 05 | [Numbers and Data](mission-05-numbers-data/README.md) | Manual conversions, Python verification, [`number_converter.py`](mission-05-numbers-data/number_converter.py), and ASCII/UTF-8 text encoding |
| Mission 06 | [Git and GitHub](mission-06-git-github/README.md) | Git workflow, creating and pushing branch `update-about`, Pull Request notes, and command glossary |
| Mission 07 | [Networking](mission-07-networking/README.md) | Network concepts (`LAN`–`Client-server`), privacy-safe `ping`/`nslookup` checks, and website loading steps |
| Mission 08 | [Final Report](mission-08-final-report/README.md) | Complete repository verification, mission status review, final checklist, and submission steps |

## Topics Covered

- Computer fundamentals, IPOS cycle, hardware/software, and embedded everyday systems
- Terminal navigation, file operations, flags, pipes (`|`), and package managers
- Operating system responsibilities, running processes/PIDs, paths, storage, and permissions
- Program execution (`hello.py`) and compiler vs. interpreter differences
- Binary/hexadecimal conversions, Python converter scripting, and ASCII/UTF-8 encoding
- Version control with Git, branching, and GitHub Pull Requests
- Computer networking, DNS resolution, connectivity testing, and client-server communication

## Running the Python Programs

### Number Converter (Mission 05)

Run [`number_converter.py`](mission-05-numbers-data/number_converter.py) from its mission folder:

```bash
cd mission-05-numbers-data
python3 number_converter.py
```

Or run it directly from the repository root:

```bash
python3 mission-05-numbers-data/number_converter.py
```

Enter any whole decimal number when prompted (for example `13`, `25`, or `255`) to display its binary and hexadecimal values.

### Hello Script (Mission 04)

Run [`hello.py`](mission-04-programs/hello.py) from its mission folder or the repository root:

```bash
cd mission-04-programs
python3 hello.py
```

```bash
python3 mission-04-programs/hello.py
```

## Mission Documentation and Commits

Each mission has a dedicated `README.md` inside its mission folder, with privacy-safe command outputs stored in [`evidence/`](evidence/). Each completed mission was documented and committed separately.

## Project Completion Status

- **Missions 00–05 and 07:** Completed, verified with real outputs, documented in each mission's `README.md`, committed separately, and pushed to `origin/main`.
- **Mission 06:** Core Git workflow, command glossary, and branch `update-about` are committed and pushed to GitHub. Creating/merging the Pull Request on GitHub (`https://github.com/armaan247/digital-detective-8007/pull/new/update-about`) remains `NEEDS USER INPUT`.
- **Mission 08:** Final repository review, checklist, and report completed and pushed; submitting the public repository URL via the instructor's Google Form remains for the student.

## Learning Summary

Across the nine missions, I connected everyday computer usage with what happens underneath: how input flows through CPU, RAM, screen, and SSD in the IPOS cycle; how macOS schedules processes and enforces permissions; how numbers and text map to binary, hexadecimal, ASCII, and UTF-8; how Python runs scripts; how Git branches track history safely; and how DNS and IP routing load websites.
