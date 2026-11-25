# Mission 05 — Numbers and Data

---

## 1. Mission Title

**Mission 05: Numbers and Data**

---

## 2. Task / Objective

Practise converting between decimal, binary, and hexadecimal numbers by hand, verify the results in Python 3, build and test [`number_converter.py`](number_converter.py), and explain how text is stored using character encodings such as ASCII and UTF-8.

---

## 3. Work Completed

### Task 5.1 — Convert Numbers by Hand

For decimal-to-binary conversions, I divided repeatedly by `2` and read the remainders from bottom to top. For binary-to-decimal and hex-to-decimal, I multiplied each digit by its positional power of `2` or `16`.

| Question | Your Working and Answer |
|----------|-------------------------|
| **Convert decimal 13 to binary.** | `13 ÷ 2 = 6` remainder `1`; `6 ÷ 2 = 3` remainder `0`; `3 ÷ 2 = 1` remainder `1`; `1 ÷ 2 = 0` remainder `1`. Reading remainders bottom-to-top gives **`1101`**. |
| **Convert decimal 25 to binary.** | `25 ÷ 2 = 12` remainder `1`; `12 ÷ 2 = 6` remainder `0`; `6 ÷ 2 = 3` remainder `0`; `3 ÷ 2 = 1` remainder `1`; `1 ÷ 2 = 0` remainder `1`. Reading remainders bottom-to-top gives **`11001`**. |
| **Convert binary 1010 to decimal.** | `(1 × 2³) + (0 × 2²) + (1 × 2¹) + (0 × 2⁰) = 8 + 0 + 2 + 0 =` **`10`**. |
| **Convert binary 1101 to decimal.** | `(1 × 2³) + (1 × 2²) + (0 × 2¹) + (1 × 2⁰) = 8 + 4 + 0 + 1 =` **`13`**. |
| **Convert hexadecimal A to decimal.** | In base 16, `A = 10`, so `10 × 16⁰ =` **`10`**. |
| **Convert hexadecimal 1F to decimal.** | `(1 × 16¹) + (F × 16⁰) = (1 × 16) + (15 × 1) = 16 + 15 =` **`31`**. |
| **Convert binary 1111 to hexadecimal.** | Group the 4 bits together: `1111₂ = 8 + 4 + 2 + 1 = 15₁₀`. Since `15` in hexadecimal is `F`, the answer is **`F`**. |

---

### Task 5.2 — Verify Using Python

I verified the Task 5.1 conversions in Python 3 using `bin()`, `hex()`, and `int(value, base)`:

| Expression Tested | Observed Python Result | Matches Manual Calculation? |
|-------------------|------------------------|-----------------------------|
| `bin(13)` | `'0b1101'` | Yes (`1101`, with Python's `0b` prefix) |
| `bin(25)` | `'0b11001'` | Yes (`11001`, with Python's `0b` prefix) |
| `int('1010', 2)` | `10` | Yes |
| `int('1101', 2)` | `13` | Yes |
| `hex(10)` | `'0xa'` | Yes (`a` / `A`, with Python's `0x` prefix) |
| `hex(31)` | `'0x1f'` | Yes (`1f` / `1F`, with Python's `0x` prefix) |
| `int('A', 16)` | `10` | Yes |
| `int('1F', 16)` | `31` | Yes |
| `hex(int('1111', 2))` | `'0xf'` | Yes (`f` / `F`, with Python's `0x` prefix) |

---

### Task 5.3 — Build a Small Number Converter

I wrote [`number_converter.py`](number_converter.py) inside `mission-05-numbers-data/`. The program asks the user for a decimal integer with `input()`, converts the string into an integer with `int()` (printing a clear message if invalid input is entered), converts it to binary and hexadecimal using `bin()` and `hex()`, and prints the results.

#### Test Results

| Test Number | Binary Output | Hexadecimal Output |
|-------------|---------------|--------------------|
| `13` | `0b1101` | `0xd` |
| `25` | `0b11001` | `0x19` |
| `31` | `0b11111` | `0x1f` |
| `255` | `0b11111111` | `0xff` |

I also ran the script from inside `mission-05-numbers-data/` with `42` (`0b101010`, `0x2a`) and tested non-numeric input (`abc`), which safely printed `Invalid input: please enter a valid whole decimal number.`

#### How Python's Conversion Functions Work

- `bin(number)` takes an integer and returns a binary string prefixed with `0b` (base 2).
- `hex(number)` takes an integer and returns a hexadecimal string prefixed with `0x` (base 16, using `0–9` and `a–f`).

---

### Task 5.4 — How Is Text Stored?

- **ASCII decimal codes:**
  - Uppercase `A`: **`65`** (verified with `ord('A')`)
  - Lowercase `a`: **`97`** (verified with `ord('a')`)
- **Why computers need an encoding standard:**
  Computers can only store numbers in binary (`0`s and `1`s), not letters or symbols directly. A character-encoding standard gives every character a consistent numeric code so any program or computer reads and displays the same text accurately.
- **Character outside basic ASCII:**
  `₹` (Indian Rupee sign). Basic ASCII only covers code points `0` through `127`, whereas `₹` has code point `8377` (`U+20B9`) and requires UTF-8 multi-byte encoding (`b'\xe2\x82\xb9'`).

---

## 4. Commands / Tools Used

| Command / Tool / Function | Purpose |
|---------------------------|---------|
| VS Code | Created and edited [`number_converter.py`](number_converter.py) |
| `python3` | Ran conversion checks and tested [`number_converter.py`](number_converter.py) in Terminal |
| `input()`, `int()`, `bin()`, `hex()` | Read user input as text, converted to decimal integer, and converted to binary and hexadecimal strings |
| `ord()`, `.encode('utf-8')` | Checked ASCII decimal values (`A`, `a`) and UTF-8 byte representation of `₹` |

---

## 5. My Understanding

- Computers store all data—whether numbers or characters—in binary (`0`s and `1`s), while hexadecimal offers a shorter, easier-to-read way to write groups of 4 binary bits.
- Manual division-by-2 and place-value expansion confirm why Python's `bin()` and `hex()` return the values they do (`0b` for binary and `0x` for hex).
- Standard encodings like ASCII and UTF-8 make text portable across machines; UTF-8 keeps backwards compatibility with basic ASCII while supporting currency symbols, accented letters, emojis, and global scripts.

---

## 6. Difficulties Faced

No major difficulties. Adding a `try`/`except ValueError` block prevented `number_converter.py` from crashing if a user enters text instead of a number.

---

## 7. How I Resolved Them

Handled invalid decimal strings cleanly inside `main()` using `try ... except ValueError` and verified it with test input `abc`.

---

## 8. Evidence / Files

| Evidence Item | Description |
|---------------|-------------|
| [Mission 05 README](README.md) | Hand-worked conversions, Python verification, converter documentation, and text-encoding notes |
| [number_converter.py](number_converter.py) | Python script converting a user-entered decimal integer to binary and hexadecimal |
| [Mission 05 output](../evidence/mission-05-converter-output.txt) | Recorded Python verification expressions and interactive converter test runs |

---

## 9. Commit Details

- Commit message: `Build number converter and practise data representation`
- Commit hash: `a4bc463`
- Branch: `main`
- Status: Pushed to `origin/main` and verified.
