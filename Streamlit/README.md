# DK's Student Grade Manager

A Streamlit application for recording student marks, calculating letter grades,
and viewing class statistics. The application is in [grade-app.py](grade-app.py).

## Features

- Add student names and marks through a form.
- Validate that names are nonempty and contain only letters and spaces.
- Accept marks from 0 to 100, including decimal values.
- Display student names, marks, and calculated grades in a table.
- Show the class average to one decimal place, plus the highest and lowest marks.
- Keep records across interactions using Streamlit session state.

## Setup

Python 3 is required. From this `Streamlit` folder, activate the existing virtual
environment in the parent project folder:

```bash
source ../venv/bin/activate
python -m pip install -r requirement.txt
```

For a fresh checkout without that environment, create a local one instead:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirement.txt
```

## Run

Run from this folder:

```bash
python -m streamlit run grade-app.py
```

Open the local URL printed in the terminal, usually http://localhost:8501.
Press `Ctrl+C` in the terminal to stop the app.

If port 8501 is already in use, choose another port:

```bash
python -m streamlit run grade-app.py --server.port 8502
```

## Usage

1. Enter a student's name and mark.
2. Click **Add Student**.
3. View the student's grade in **Student Results**.
4. Add more students to update **Class Statistics**.

The form clears after submission, including when validation fails. Before any
students are added, the results section displays an empty-state message and no
statistics are shown.

## Input Validation

- Leading and trailing whitespace is removed from the name.
- Blank names are rejected.
- Names may contain alphabetic characters and whitespace, but not numbers or
	punctuation. Names such as `Anne-Marie` or `O'Connor` are rejected.
- Marks must be between 0 and 100, inclusive. The input's increment is 1, but
	decimal values such as `83.5` are also accepted.
- Whole-number marks such as `90.0` are stored as integers; fractional marks are
	preserved.
- Duplicate names are allowed; each valid submission adds a separate record.

## Grading Scale

| Grade | Mark |
| --- | --- |
| A | 90 to 100 |
| B | 80 to less than 90 |
| C | 70 to less than 80 |
| D | 60 to less than 70 |
| E | 0 to less than 60 |

For example, `90` receives A, `89.5` receives B, and `59.5` receives E.

## Class Statistics

Statistics are calculated from all records in the current session:

- **Average:** Sum of marks divided by the number of students, displayed to one
	decimal place.
- **Highest:** Maximum mark.
- **Lowest:** Minimum mark.

## Data Storage

Records are stored in memory for the current Streamlit browser session, not in a
file or database. They survive normal app interactions, but refreshing the page,
starting a new session, or restarting the server can clear them.

The current app does not provide editing, deletion, export, or permanent storage
of student records.