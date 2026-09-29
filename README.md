# Student Grade Management System

## Project Overview

The Student Grade Management System is a simple Python project developed to
manage basic academic information of students.

The main purpose of this project is to make it easier to enter and manage
student details, subjects, marks, grades, attendance, assignments and
overall performance.

The project is made using basic Python concepts so that it is easy to
understand and use. Different parts of the system are divided into
different Python modules instead of putting the whole program in one file.

The program stores the information in Python lists while the program is
running. No database or external storage system is used.

## Features

The project contains the following modules:

1. Student Information
2. Subject Information
3. Marks Management
4. Grade Management
5. Attendance Management
6. Teacher Information
7. Result Management
8. Assignment Management
9. Performance Analysis

### Student Information

This module is used to manage basic student details such as:

- Student ID
- Student Name
- Age
- Gender
- Course
- Semester
- Phone Number

It allows the user to add, view, update, delete and search student
records.

### Subject Information

This module manages the subjects studied by students.

It stores:

- Subject ID
- Subject Name
- Subject Code
- Credits
- Teacher Name

The user can add, view, update and delete subject information.

### Marks Management

This module is used to enter and manage marks of students.

It stores:

- Student ID
- Student Name
- Subject
- Internal Marks
- Mid-Term Marks
- Final Exam Marks
- Total Marks

The total marks are calculated automatically.

### Grade Management

This module calculates the grade of a student according to the
percentage obtained.

The grading system used is:

- 90 and above - A+
- 80 to 89 - A
- 70 to 79 - B+
- 60 to 69 - B
- 50 to 59 - C
- 40 to 49 - D
- Below 40 - F

### Attendance Management

This module keeps track of student attendance.

It records:

- Student ID
- Student Name
- Total Classes
- Classes Attended
- Attendance Percentage

The attendance percentage is calculated automatically.

The system also gives an indication if the attendance is below the
required level.

### Teacher Information

This module stores basic teacher information such as:

- Teacher ID
- Teacher Name
- Subject
- Department
- Phone Number

Teachers can be added, viewed, updated and deleted.

### Result Management

This module is used to maintain subject-wise results.

It calculates the percentage and determines whether a student has passed
or failed.

A student is considered passed when the percentage is 40 or above.

### Assignment Management

This module manages student assignments.

It stores:

- Assignment ID
- Student ID
- Student Name
- Subject
- Assignment Title
- Marks
- Submission Status

It can also be used to check whether an assignment has been submitted.

### Performance Analysis

This module gives a simple overall view of a student's academic
performance.

The overall score is calculated using:

- Average Marks - 60%
- Attendance - 20%
- Assignment Average - 20%

Based on the overall score, the system displays a performance level such
as Excellent, Very Good, Good or Needs Improvement.

## Technologies Used

The project uses:

- Python
- Python Lists
- Functions
- Conditional Statements
- Loops
- User Input
- Basic Arithmetic
- Python Modules

No external Python libraries are required.

## Project Structure

```text
Student Grade Management System
│
├── 1.MAIN_PAGE.py
├── student_info.py
├── subject_info.py
├── marks_info.py
├── grade_info.py
├── attendance_info.py
├── teacher_info.py
├── result_info.py
├── assignment_info.py
├── performance_info.py
├── README.md
└── statement.md
