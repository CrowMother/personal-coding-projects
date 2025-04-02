# Text to Number Converter

A simple Python program that converts numbers written in words (e.g., `"one hundred twenty three"`) into their integer form (`123`). This was built as a resume project to demonstrate string parsing, number mapping, and logical reasoning using Python.

---

## 📦 Installation

To get started, clone the repository and make sure you have Python 3 installed.

```bash
git clone https://github.com/yourusername/text-to-number-converter.git
cd text-to-number-converter
```
This project does not require any external packages beyond Python's standard library.

## ▶️ How to Run
You can run the program directly via terminal or command line:

bash
Copy
Edit
python main.py
If you're using an IDE like VS Code or PyCharm, you can also run main.py directly from the editor.

Alternatively, if you're running it in non-interactive mode (e.g., during testing), you can import and call the run() function from another file:

python
Copy
Edit
from main import run

print(run("one hundred twenty three"))  # Output: 123
## 📄 Notes
This is a small-scale resume project designed to demonstrate problem-solving using Python. It focuses on converting simple English number phrases into integers.

- Scope
  - Small Scope Focus

  - Handles positive numbers only

  - Performs basic error checking (ignores unknown words)

  - Supports numbers from one to the multi-trillions

- ❌ Does not support:

  - Negative numbers

  - Decimals ("point five")

  - Ordinals ("first", "second", etc.)

  - Complex sentence structures

## Plan

- Start

- Entry point receives input either via the input() prompt or through a function parameter.

- User Input

- The input is a number written in plain English (e.g., "two thousand three hundred").

- Break String Into Parts

- The input string is split into words using .split().

- Word-to-Number Conversion

- Each word is checked against dictionaries for small numbers (like "three" = 3") and large multipliers (like "thousand" = 1000").

- Combining Values

- The logic assembles the values in correct numerical order based on language rules (e.g., multiplying hundreds, thousands, millions, etc., appropriately).

- Return Result

The final computed integer is returned or printed to the console.

## 🧪 Testing
Unit tests are provided in test.py. To run the tests:

```bash 
python test.py 
```
This uses Python’s built-in unittest framework to check conversions of various word-based numbers to ensure the parser is accurate.