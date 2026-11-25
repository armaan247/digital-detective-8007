# Mission 06 — Git and GitHub

---

## 1. Mission Title

**Mission 06: Git and GitHub**

---

## 2. Task / Objective

Practise the core Git workflow (`status`, `add`, `commit`, `log`), create and push a new branch (`update-about`) with a learning update in the root `README.md`, document the Pull Request collaboration process, and build a concise Git command glossary.

---

## 3. Work Completed

### Task 6.1 — Understand the Basic Git Workflow

Throughout the earlier missions and in this mission, I checked repository status with `git status`, staged specific files with `git add`, created meaningful commits with `git commit -m`, and inspected recent commits with `git log --oneline`.

| Git Operation | What It Does in Your Own Words |
|---------------|--------------------------------|
| **Check repository status** (`git status`) | Shows the current branch, whether it matches the remote branch, and which files are untracked, modified, or staged for commit. |
| **Stage selected changes** (`git add`) | Marks specific file changes to be included in the next commit snapshot by adding them to the staging area. |
| **Create a commit** (`git commit`) | Permanently saves a snapshot of everything currently in the staging area into local Git history with a message describing what changed. |
| **View commit history** (`git log`) | Displays the list of saved commits in chronological order, showing each commit hash and message. |

#### Difference Between Staging and Committing

**Staging (`git add`)** selects and prepares changes in a holding area (the staging area/index) so you can choose exactly which edits belong together; you can still modify or unstage files before saving. **Committing (`git commit`)** writes the staged snapshot into the repository's permanent history with a commit message and unique hash.

---

### Task 6.2 — Create and Use a Branch

1. Checked clean status on `main` and created a new branch named `update-about` using `git switch -c update-about`.
2. Opened the root [`README.md`](../README.md) and added a `## My Learning` section describing three key topics learned across Missions 01–05 (the IPOS cycle, Terminal navigation/flags/pipes/permissions, and number systems/text encoding/Python conversion).
3. Verified the change with `git status`, staged `README.md`, committed it (`fd90a66` — `"Add My Learning section to root README"`), and pushed the branch to GitHub with `git push -u origin update-about`.
4. Switched back to `main` (`git switch main`) and verified both `main` and `update-about` exist locally and on `origin`.

---

### Task 6.3 — Create a Pull Request

#### What Branches and Pull Requests Are (and Why Teams Use Them)

- **Branch:** A separate, parallel line of development inside the repository. Teams use branches so multiple people can work on different changes at the same time without breaking the stable `main` branch.
- **Pull Request (PR):** A GitHub request asking to review and merge changes from one branch (such as `update-about`) into another (such as `main`). It lets teammates inspect the exact file differences, leave comments, and verify everything before merging into the shared codebase.

#### Pull Request Status (`NEEDS USER INPUT`)

- **Branch status:** The `update-about` branch (commit `fd90a66`) has been committed and pushed to GitHub (`origin/update-about`).
- **Pull Request status:** **NEEDS USER INPUT — Not yet created on GitHub.** Opening a Pull Request on GitHub requires signing into the GitHub web interface in a browser (`gh` CLI is not installed).
- **Action needed from user:**
  1. Open `https://github.com/armaan247/digital-detective-8007/pull/new/update-about` in your browser.
  2. Enter a short description explaining the `## My Learning` update to `README.md` and click **Create pull request** (`update-about` -> `main`).
  3. Review the changed file, and merge the PR only if your instructor asked you to merge it.
  4. If you merge the PR on GitHub, run `git switch main && git pull origin main` in Terminal to bring the merged update onto your local `main` branch, then update this status section with the PR number and merge status.

---

### Task 6.4 — Build Your Git Command Glossary

| Git Operation | Command | One-Line Explanation |
|---------------|---------|----------------------|
| **Initialise a repository** | `git init` | Creates a new empty Git repository (`.git` folder) in the current project directory. |
| **Check status** | `git status` | Shows the active branch and lists modified, untracked, and staged files. |
| **Stage changes** | `git add <file>` | Adds selected changes to the staging area so they will be included in the next commit. |
| **Commit changes** | `git commit -m "..."` | Saves all staged changes as a permanent commit snapshot with a descriptive message. |
| **View history** | `git log` | Displays the commit history for the current branch, including hashes and messages. |
| **Create or list branches** | `git branch` | Lists existing local branches, or creates a new branch when given a branch name. |
| **Switch branches** | `git switch <branch>` (or `git checkout`) | Moves `HEAD` and your working files to the specified branch. |
| **Publish changes** | `git push` | Uploads local commits on a branch to the remote repository on GitHub. |
| **Retrieve remote changes** | `git pull` (or `git fetch`) | Downloads changes from the remote repository (`fetch` only downloads; `pull` downloads and merges into the current branch). |

---

## 4. Commands / Tools Used

| Command / Tool | Purpose |
|----------------|---------|
| `git status` | Verified clean working tree and tracked modified `README.md` |
| `git log --oneline -n 8` | Reviewed recent mission commits on `main` |
| `git switch -c update-about` / `git switch main` | Created `update-about` branch and later switched back to `main` |
| `git add README.md` | Staged the root README learning update on `update-about` |
| `git commit -m "Add My Learning section to root README"` | Committed the root README update (`fd90a66`) |
| `git push -u origin update-about` | Published `update-about` to GitHub and set upstream tracking |
| `git branch -a` | Verified both local and remote branches (`main` and `update-about`) |

---

## 5. My Understanding

- Separating staging (`git add`) from committing (`git commit`) gives clear control over what goes into each commit instead of dumping unrelated changes together.
- Branches let you test or prepare edits (like updating `README.md` on `update-about`) safely without touching `main` until the changes are ready.
- Pull Requests connect Git's branching model with GitHub's review workflow so collaborators can inspect diffs before merging.

---

## 6. Difficulties Faced

- Creating the Pull Request directly from Terminal was not possible because the GitHub CLI (`gh`) is not installed on this Mac, so the PR creation step on GitHub's website requires opening the browser manually.

---

## 7. How I Resolved Them

- I pushed the `update-about` branch to GitHub (`fd90a66`), recorded the exact GitHub compare/PR creation URL, and clearly documented the remaining browser step under Task 6.3 as `NEEDS USER INPUT` rather than installing unapproved tools or claiming the PR already exists.

---

## 8. Evidence / Files

| Evidence Item | Description |
|---------------|-------------|
| [Mission 06 README](README.md) | Git workflow explanations, branch/PR details, and 9-operation Git command glossary |
| [Mission 06 Git output](../evidence/mission-06-git-output.txt) | Privacy-safe log of `git log`, `git switch`, `git commit`, `git push`, and `git branch -a` |
| Remote branch `origin/update-about` (`fd90a66`) | Pushed branch containing the `## My Learning` update in [`README.md`](../README.md) |

---

## 9. Commit Details

- Commit message: `Complete Git and GitHub collaboration mission` (on `main`)
- Related branch commit: `fd90a66` (`Add My Learning section to root README` pushed to `origin/update-about`)
- Branch: `main`
- Status: Ready to commit and push to `origin/main` (Task 6.3 web PR creation marked `NEEDS USER INPUT`).
