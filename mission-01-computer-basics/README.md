# Mission 01 — Know Your Computer

---

## 1. Mission Title

**Mission 01: Know Your Computer**

---

## 2. Task / Objective

Demonstrate an understanding of core computer concepts by:

- Tracing a real activity through the IPOS (Input → Processing → Output → Storage) cycle.
- Identifying hardware components and software applications on a Mac computer.
- Recognising computer-based systems encountered in everyday life.

---

## 3. Work Completed

### Task 1.1 — Trace One Activity Using IPOS

**Chosen activity:** Typing and saving a document in VS Code on macOS.

#### IPOS Table

| Stage          | What Happens in My Example                                                                  | Hardware / Component Involved |
|----------------|---------------------------------------------------------------------------------------------|-------------------------------|
| **Input**      | I press keys on the built-in keyboard to type text into a file in VS Code                   | Built-in keyboard             |
| **Processing** | The CPU processes each keystroke using RAM, and macOS with VS Code updates the text in memory | CPU, RAM                      |
| **Output**     | The updated text appears immediately on the screen inside the VS Code editor window          | Built-in display (screen)     |
| **Storage**    | Pressing `Cmd + S` writes the file from temporary RAM to permanent storage on the SSD       | Internal SSD                  |

#### How the activity moves from input to output and storage

1. **Input to Processing:** Pressing a key sends an electrical signal to the CPU. macOS passes the input to VS Code, which processes the character and keeps the unsaved text temporarily in RAM.
2. **Processing to Output:** The system renders the updated characters onto the built-in display so I can see what I am typing right away.
3. **Processing to Storage:** When I press `Cmd + S`, VS Code asks macOS to save the document from RAM onto the internal SSD so the changes stay saved even after the Mac is shut down.

---

### Task 1.2 — Identify Hardware and Software

#### Hardware and Software Table

| Item / Software Name              | Hardware or Software | Software Type    | Purpose                                                                       |
|-----------------------------------|----------------------|------------------|-------------------------------------------------------------------------------|
| Built-in keyboard                 | Hardware             | Not Applicable   | Primary input device; used to type text and issue commands                    |
| Built-in trackpad                 | Hardware             | Not Applicable   | Pointing and gesture input device for navigating the interface                |
| Built-in display (screen)         | Hardware             | Not Applicable   | Outputs visual information — text, graphics, and the desktop UI               |
| FaceTime camera (webcam)          | Hardware             | Not Applicable   | Captures video and still images for video calls and online meetings           |
| macOS                             | Software             | Operating System | Manages hardware resources and provides the environment for all applications  |
| VS Code                           | Software             | Application      | Source code editor used to write, edit, and save files                        |
| Google Chrome / Safari            | Software             | Application      | Web browser used to access websites and online resources                      |
| Terminal                          | Software             | Utility          | Command-line interface for running shell commands and scripts                 |
| Activity Monitor                  | Software             | Utility          | Displays real-time CPU, RAM, disk, and network usage for system diagnostics   |

---

### Task 1.3 — Computer Systems Around You

The following are computer-based systems encountered in everyday life (not laptops or mobile phones).

| System                              | Main Purpose                                                | One Input                                        | One Output                                                         |
|-------------------------------------|-------------------------------------------------------------|--------------------------------------------------|--------------------------------------------------------------------|
| ATM (Automated Teller Machine)      | Allows users to withdraw cash and check account balance     | Card insertion and PIN entered via keypad        | Cash dispensed and a printed receipt                               |
| Smart TV                            | Streams and displays video and audio content                | Remote control button press / voice command      | Audio and video displayed on the TV screen                         |
| Traffic Light Control System        | Manages the flow of road traffic at intersections           | Vehicle presence detected by road sensors        | Traffic lights switching between red, amber, and green             |
| Digital Blood Pressure Monitor      | Measures and displays blood pressure and heart rate         | User pressing the Start button on the device     | Systolic/diastolic pressure and pulse rate shown on the display    |
| Smartwatch / Fitness Tracker        | Tracks health metrics and delivers notifications            | Heart rate sensor data and step counter input    | Health statistics and notifications shown on the watch face        |

---

## 4. Commands / Tools Used

| Tool / Command | Purpose                                              |
|----------------|------------------------------------------------------|
| VS Code        | Used as the editor to open and save the README file  |
| `Cmd + S`      | Keyboard shortcut to save the file in VS Code        |

> No terminal commands were executed as part of this mission.

---

## 5. My Understanding

- Every task on a computer follows the **IPOS cycle** (Input, Processing, Output, Storage). Even typing a line in VS Code and saving it relies on all four stages working together: keyboard input goes to the CPU and RAM, appears on the screen as output, and is saved onto the SSD for permanent storage.
- **Hardware** means the physical parts I can touch (keyboard, trackpad, display, camera), while **software** means the programs and instructions running on that hardware.
- Software can be grouped by its main role:
  - **Operating System** manages hardware and lets other programs run (macOS).
  - **Application** helps the user do specific work (VS Code, Google Chrome / Safari).
  - **Utility** helps manage, monitor, or interact with the system itself (Terminal, Activity Monitor).
- Everyday devices like ATMs, smart TVs, traffic light controllers, digital blood pressure monitors, and smartwatches also work like computer systems because they take input, process data, and produce output.

---

## 6. Difficulties Faced

- Deciding whether Terminal should be classified as application software or utility software was slightly confusing at first, because it is an app I open directly, yet it is used to run system and command-line tasks.

---

## 7. How I Resolved Them

- I focused on the main purpose of each program: programs built for end-user tasks like editing files or browsing (VS Code, Chrome/Safari) were listed as **Application**, while tools meant for managing, monitoring, or issuing system commands (Activity Monitor, Terminal) were listed as **Utility**.

---

## 8. Evidence / Files

| Evidence Item | Description |
|---------------|-------------|
| [Mission 01 README](README.md) | Completed IPOS, hardware/software, and everyday-systems tables with explanations |

---

## 9. Commit Details

- Commit message: `Complete computer basics and IPOS mission`
- Branch: `main`
- Status: Ready to commit and push to `origin/main`.
