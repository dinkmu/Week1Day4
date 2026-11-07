#!/usr/bin/env python3

"""
grade_app.py
------------
A Streamlit-based Student Grade Manager.

This application allows users to:
- Add student names and marks
- Validate student names
- Validate marks between 0 and 100
- Calculate grades using the Day 2 grading scale
- Store student records using Streamlit session state
- Display all student results in a table
- Display class average, highest mark, and lowest mark
"""

import streamlit as st


# ---------------------------------------------------------
# Grade Calculation
# ---------------------------------------------------------

def get_grade(mark):
    """
    Calculates and returns the letter grade for a given mark
    based on the same inclusive boundary rules used on Day 2.

    A: 90-100
    B: 80-89
    C: 70-79
    D: 60-69
    E: Below 60
    """

    if 90 <= mark <= 100:
        return "A"
    elif 80 <= mark < 90:
        return "B"
    elif 70 <= mark < 80:
        return "C"
    elif 60 <= mark < 70:
        return "D"
    else:
        return "E"


# ---------------------------------------------------------
# Streamlit Page Configuration
# ---------------------------------------------------------

st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="centered"
)


# ---------------------------------------------------------
# Application Title
# ---------------------------------------------------------

st.title("🎓 DK's Student Grade Manager")

st.write(
    "Add student names and marks to calculate grades "
    "and view class statistics."
)


# ---------------------------------------------------------
# Session State
# ---------------------------------------------------------

# Streamlit reruns the entire script whenever the user
# interacts with the application.
#
# Therefore, using:
#
# students = []
#
# would recreate an empty list after every rerun.
#
# st.session_state keeps the student records available
# between Streamlit reruns.

if "students" not in st.session_state:
    st.session_state.students = []


# ---------------------------------------------------------
# Add Student Form
# ---------------------------------------------------------

st.subheader("Add Student")

with st.form("add_student_form", clear_on_submit=True):

    name = st.text_input(
        "Student Name",
        placeholder="Enter student name"
    )

    mark = st.number_input(
        "Mark",
        min_value=0.0,
        max_value=100.0,
        step=1.0
    )

    submitted = st.form_submit_button("Add Student")
# ---------------------------------------------------------
# Form Validation and Student Addition
# ---------------------------------------------------------

if submitted:

    # Remove spaces before and after the name
    name = name.strip()

    # Name cannot be empty
    if not name:

        st.error(
            "⚠️ Name cannot be empty."
        )

    # Name can contain only letters and spaces
    elif not all(
        character.isalpha() or character.isspace()
        for character in name
    ):

        st.error(
            "⚠️ Name can only contain letters and spaces. "
            "Numbers and special characters are not allowed."
        )

    # Additional mark validation
    elif not 0 <= mark <= 100:

        st.error(
            "⚠️ Mark must be between 0 and 100."
        )

    else:

        # Convert values such as 90.0 to 90
        # but preserve decimal values such as 83.5
        if mark.is_integer():
            mark = int(mark)

        # Store student in session state
        st.session_state.students.append(
            {
                "name": name,
                "mark": mark
            }
        )

        st.success(
            f"✅ Added '{name}' with mark {mark}."
        )


# ---------------------------------------------------------
# Student Results
# ---------------------------------------------------------

st.subheader("Student Results")

if not st.session_state.students:

    st.info(
        "📂 No student records found yet. "
        "Add some students first!"
    )

else:

    # Create the data for the Streamlit table
    results = []

    marks = []

    for student in st.session_state.students:

        grade = get_grade(student["mark"])

        results.append(
            {
                "Name": student["name"],
                "Mark": student["mark"],
                "Grade": grade
            }
        )

        marks.append(student["mark"])


    # -----------------------------------------------------
    # Display Student Table
    # -----------------------------------------------------

    st.table(results)


    # -----------------------------------------------------
    # Calculate Class Statistics
    # -----------------------------------------------------

    average_mark = sum(marks) / len(marks)

    highest_mark = max(marks)

    lowest_mark = min(marks)


    # -----------------------------------------------------
    # Display Class Statistics
    # -----------------------------------------------------

    st.subheader("Class Statistics")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            label="Average",
            value=f"{average_mark:.1f}"
        )

    with col2:
        st.metric(
            label="Highest",
            value=highest_mark
        )

    with col3:
        st.metric(
            label="Lowest",
            value=lowest_mark
        )