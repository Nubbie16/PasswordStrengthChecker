# PasswordStrengthChecker
Python - Password Strength Checker

## How to Run the Program

This project is a Python command-line password strength checker. It checks an entered password against several strength rules, including password length, character variety, common passwords, weak words, keyboard patterns, repeating characters, sequential numbers, and all-numeric password rules.

---

## Requirements

Before running the program, make sure Python is installed on your computer.

Open PowerShell, Command Prompt, or a terminal and run one of the following commands:

```bash
py --version
```

or:

```bash
python --version
```

If Python is installed, a version number should appear.

Example:

```text
Python 3.14.0
```

If neither command works, Python needs to be installed before running the program.

---

## Downloading the Project from GitHub

There are two common ways to download the project files.

### Option 1: Clone the Repository

Open PowerShell, Command Prompt, or Git Bash and run:

```bash
git clone https://github.com/Nubbie16/PasswordStrengthChecker.git
```

Then move into the project folder:

```bash
cd PasswordStrengthChecker
```

### Option 2: Download ZIP

1. Go to the GitHub repository page.
2. Click the green **Code** button.
3. Click **Download ZIP**.
4. Extract the ZIP file.
5. Open the extracted project folder.

---

## Required Project Files

The program expects the following files to be in the same folder:

```text
main.py
CheckLogic.py
PasswordData.py
```

Do not move these files into separate folders unless the import statements are updated.

---

## Running the Program

Open PowerShell, Command Prompt, or a terminal inside the project folder.

Run the program with:

```bash
py main.py
```

If that does not work, try:

```bash
python main.py
```

The program will start and display:

```text
Program Start

Please enter password, or type X to exit:
```

Enter a password and press **Enter**.

The program will check the password and display either a failed requirement message or a strength score.

Example output:

```text
Score: 7
Strength: Strong
```

To exit the program, type:

```text
x
```

or:

```text
X
```

Then press **Enter**.

---

## Example Run

```text
Program Start

Please enter password, or type X to exit: Abcdefghij9!
Score: 7
Strength: Strong

Please enter password, or type X to exit: x
Program ended.
```

---

## Password Score Ratings

| Score Range | Strength    |
| ----------: | ----------- |
|         0-2 | Weak        |
|         3-5 | Average     |
|         6-7 | Strong      |
|           8 | Very Strong |

---

## Automatic Fail Checks

Some checks are automatic fail checks. If one of these fails, the program does not continue scoring the password.

| Check                      | Rule                                                        |
| -------------------------- | ----------------------------------------------------------- |
| Empty password             | Password cannot be blank.                                   |
| Invalid characters         | Spaces, emojis, and unsupported characters are not allowed. |
| Minimum length             | Password must be at least 8 characters.                     |
| Common password            | Password cannot exactly match the common password list.     |
| Short all-numeric password | Numeric-only passwords must be at least 16 digits.          |

---

## Troubleshooting

### `python` or `py` is not recognized

Python is either not installed or not added to PATH.

Try:

```bash
py --version
```

or:

```bash
python --version
```

If both commands fail, install Python and make sure the option to add Python to PATH is selected during installation.

---

### `ModuleNotFoundError`

Make sure the required files are still in the same folder:

```text
main.py
CheckLogic.py
PasswordData.py
```

The program imports `CheckLogic.py`, and `CheckLogic.py` imports `PasswordData.py`.

---

### Program closes immediately

Run the program from PowerShell, Command Prompt, or a terminal instead of double-clicking the `.py` file.

Use:

```bash
py main.py
```

Running the program from a terminal keeps the window open so the output can be viewed.



## Password Strength Rules

| # | Check | Type | Score / Penalty | Description |
|---:|---|---|---:|---|
| 1 | Empty password check | Pass/Fail | Fail | Password cannot be empty. |
| 2 | Emoji / non-ASCII check | Pass/Fail | Fail | Password cannot contain spaces, emojis, or characters outside the supported keyboard range. |
| 3 | Minimum length check | Pass/Fail | Fail if `< 8` | Password must be at least 8 characters long. |
| 4 | Common password check | Pass/Fail | Fail | Password fails if it exactly matches a password in the common password list. |
| 5 | Common weak word check | Penalty | `-2` | Password is penalized if it contains a weak word. |
| 6 | Length scoring | Score Bonus | `+1`, `+3`, or `+4` | 8-11 characters = `+1`; 12-15 characters = `+3`; 16+ characters = `+4`. |
| 7 | Lowercase check | Score Bonus | `+1` | Adds 1 point if the password contains at least one lowercase letter. |
| 8 | Uppercase check | Score Bonus | `+1` | Adds 1 point if the password contains at least one uppercase letter. |
| 9 | Number check | Score Bonus | `+1` | Adds 1 point if the password contains at least one number. |
| 10 | Special character check | Score Bonus | `+1` | Adds 1 point if the password contains at least one special character. |
| 11 | Repeating character penalty | Penalty | `-1` | Password is penalized for 3 or more repeating characters in a row. |
| 12 | Sequential number penalty | Penalty | `-1` | Password is penalized for 3 or more sequential numbers. |
| 13 | Keyboard pattern penalty | Penalty | `-2` | Password is penalized if it contains a known keyboard pattern. |
| 14 | All-numeric penalty | Pass/Fail or Penalty | Fail or `-2` | Numeric-only passwords fail if under 16 digits. Numeric-only passwords with 16+ digits receive a `-2` penalty. |
| 15/16 | Final score / strength rating | Rating | N/A | 0-2 = Weak; 3-5 = Average; 6-7 = Strong; 8 = Very Strong. |