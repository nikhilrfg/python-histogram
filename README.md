# Python Letter Histogram

## Project Overview

This Python program analyzes a text file, counts how many times each English alphabet letter (a–z) appears, and creates a histogram report.

The program sorts the letters by frequency in descending order and saves the results in a separate `.hist` file.

**Source:** Cisco Networking Academy (NetAcad) — Python Essentials 2.

The original exercise code was taken from Cisco NetAcad and includes additional explanatory comments and modifications for learning purposes.

## Project Structure

```text
python-histogram/
├── letter_histogram.py
├── sample.txt
├── sample.txt.hist
└── README.md
```

The `.hist` file is generated when the program runs.

## Features

- Reads text files using Python file handling.
- Counts occurrences of English letters a–z.
- Treats uppercase and lowercase letters equally.
- Ignores numbers, punctuation, whitespace, and non-English characters.
- Uses dictionary comprehension to initialize letter counters.
- Sorts letters by frequency using a lambda function.
- Displays results in descending order of frequency.
- Saves results to a `.hist` file.
- Handles file input/output errors.

## Python Concepts Used

**1. Dictionary Comprehension**

```python
counters = {chr(ch): 0 for ch in range(ord('a'), ord('z') + 1)}
```

Creates a dictionary with 26 letters, each initialized to zero.

**2. File Handling**

```python
file = open(file_name, "rt")
```

Opens the input file in text read mode.

**3. Nested Loops**

```python
for line in file:
    for char in line:
```

Processes each line and each character in the file.

**4. Letter Validation**

```python
if 'a' <= char.lower() <= 'z':
    counters[char.lower()] += 1
```

Counts only English alphabet letters and treats uppercase and lowercase letters equally.

**5. Lambda Function and Sorting**

```python
sorted(counters.keys(),
       key=lambda x: counters[x],
       reverse=True)
```

Sorts letters according to their frequency, highest first.

**6. Writing to a File**

```python
file.write(char + ' -> ' + str(c) + '\n')
```

Writes each letter and its frequency to the histogram file.

**7. Exception Handling**

```python
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))
```

Displays an error message if a file input/output operation fails.

## How to Run

### Step 1: Open the Project

Open the `python-histogram` folder in Visual Studio Code.

### Step 2: Create a Sample Text File

Create a file named `sample.txt` and enter:

```text
Hello World
```

### Step 3: Run the Python Program

Open the VS Code PowerShell terminal and run:

```powershell
python letter_histogram.py
```

### Step 4: Enter the Filename

```text
Enter the name of the file to analyze: sample.txt
Histogram created: sample.txt.hist
```

### Step 5: View the Histogram

The program automatically creates a file named `sample.txt.hist`.

Expected contents:

```text
l -> 3
o -> 2
d -> 1
e -> 1
h -> 1
r -> 1
w -> 1
```

The letter `l` appears three times, `o` appears twice, and the remaining letters appear once.

## Testing Scenarios

| Test | Input | Expected Result |
|---|---|---|
| 1 | `Hello World` | Correct letter counts |
| 2 | `AAAaaa` | `a -> 6` |
| 3 | `Python123!` | Counts letters only |
| 4 | Empty file | Creates an empty `.hist` file |
| 5 | Missing file | Displays an I/O error |
| 6 | Uppercase and lowercase letters | Counts them together |

## Requirements

- Python 3
- Visual Studio Code (recommended)
- Python extension for VS Code

No additional Python libraries are required.

## Limitations

- The program counts only English alphabet letters (a–z).
- The input file must be accessible and readable.
- An existing histogram file with the same name will be overwritten.
- Letters with equal frequencies appear in alphabetical order.

## Learning Objectives

This exercise helps demonstrate:

- Reading and writing text files.
- Working with dictionaries and dictionary comprehensions.
- Using nested loops and conditional statements.
- Sorting dictionary keys with lambda functions.
- Handling file-related exceptions.
- Generating output reports.

## Acknowledgment

**Original exercise source:** Cisco Networking Academy (NetAcad), Python Essentials 2.

This project is based on the Cisco NetAcad letter histogram exercise and is used for educational and Python programming practice. Explanatory comments and minor modifications have been added to improve understanding.