# Data Cleaner Tool

A simple Python tool that reads customer data from a CSV file, cleans it,
removes duplicates, validates emails and phone numbers, and saves the
results into separate clean and invalid files.

## Features

- Reads customer data from a CSV file
- Removes extra whitespace from text fields
- Detects and removes duplicate rows (based on name + email)
- Validates email format and phone number length
- Splits data into valid and invalid rows, with error reasons
- Saves results as CSV and JSON files
- Shows a summary of how many rows were processed

## Project Structure

```

data_cleaner_tool/
├── main.py <- Program entry point
├── cleaner.py <- DataCleaner class (cleaning & validation logic)
├── converter.py <- CSV/JSON read/write functions
├── sample_data.csv <- Sample input file for testing
└── README.md
```

## Tech Used

Pure Python (no external libraries needed) — uses only the built-in
`csv`, `json`, and `re` modules.

## How to Run

1. Make sure Python is installed on your computer.
2. Open a terminal in the project folder.
3. Run the program:
```
python main.py
```
4. When asked, type your CSV file name, or press Enter to use
   `sample_data.csv`.

## Output Files

After running, the tool creates:

- `clean_data.csv` — valid customer rows
- `invalid_data.csv` — invalid rows, with a reason for each
- `valid_data.json` — the same valid data in JSON format

## Example

**Input (`sample_data.csv`):**

| name | email | phone | city |
|---|---|---|---|
| Arif Hossain | arif@gmail.com | 01712345678 | Dhaka |
| wrong entry | not-an-email | 123 | Chattogram |

**Output (`invalid_data.csv`):**

| name | email | phone | city | error_reasons |
|---|---|---|---|---|
| wrong entry | not-an-email | 123 | Chattogram | invalid_email,invalid_phone |