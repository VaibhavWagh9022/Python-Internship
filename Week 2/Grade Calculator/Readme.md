# Student Grade Calculator
## Project Description
```
A comprehensive grade calculator that processes multiple students' marks, calculates grades with personalized comments, and provides class statistics.
```

## What I Learned
```
Conditional Logic: Using if/elif/else for decision making
Lists: Storing and manipulating collections of data
Loops: Using for and while loops for repetition
Error Handling: Using try-except to handle invalid inputs
Functions: Organizing code into reusable blocks
Features
✓- Processes multiple students
✓- Calculates grades based on custom grading system
✓- Provides personalized comments for each student
✓- Calculates class statistics (average, highest, lowest)
✓- Formatted table output with color coding
✓- Input validation for all user inputs
✓- Error handling for edge cases
✓- Search functionality for specific students
✓- Save results to file option
```
## How to Run
```bash 
# Navigate to project folder
cd ./week2-grade-calculator

# Run the program
python grade_calculator.py
```

## Output
```
--------------------------------------------------
      STUDENT GRADE CALCULATOR
--------------------------------------------------

Enter number of students: 3

=== STUDENT 1 ===
Student name: Hussen
Enter marks (0-100):
Math: 100
Science: 90
English: 60

=== STUDENT 2 ===
Student name: Vaibhav
Enter marks (0-100):
Math: 100
Science: 100
English: 100

=== STUDENT 3 ===
Student name: Sanskar
Enter marks (0-100):
Math: 100
Science: 80
English: 70

--------------------------------------------------
            RESULTS SUMMARY
--------------------------------------------------
Name                 |   Avg | Grade | Comment
------------------------------------------------------------
Hussen               |  83.3 |   B   | Very Good!
Vaibhav              | 100.0 |   A   | Excellent!
Sanskar              |  83.3 |   B   | Very Good!

--------------------------------------------------
          CLASS STATISTICS
--------------------------------------------------
Total Students: 3
Class Average: 88.9
Highest Average: 100.0 (Vaibhav)
Lowest Average: 83.3 (Hussen)

--------------------------------------------------
Thank you for using the Grade Calculator!
--------------------------------------------------

```
## Challenges & Solutions
```
1. Challenge: Handling invalid marks input

    - Solution: Used while loop with try-except to validate

2. Challenge: Formatting the results table

    - Solution: Used string formatting with fixed widths

3. Challenge: Calculating multiple statistics

    - Solution: Used list comprehensions and built-in functions
```