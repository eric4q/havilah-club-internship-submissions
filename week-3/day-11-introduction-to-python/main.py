# Day 11 — Introduction to Python
# Task: Complete exercises on variables, data types, operators, and basic input/output.
# Submit this .py file with all working programs.

# ── Exercise 1: Variables and Data Types ─────────────────────────────────────
# Create variables of 4 different types: string, integer, float, and boolean.
# Print all of them with descriptive labels.

# TODO: 
student_name = "Eric"
student_age = 21
student_gpa = 4.5
is_enrolled = True
 
print("Name:", student_name)
print("Age:", student_age)
print("GPA:", student_gpa)
print("Enrolled:", is_enrolled)
 
print(type(student_name))
print(type(student_age))
print(type(student_gpa))
print(type(is_enrolled))


# ── Exercise 2: Temperature Converter ────────────────────────────────────────
# Ask the user to enter a temperature in Celsius, then print the Fahrenheit equivalent.
# Also convert in the opposite direction (Fahrenheit to Celsius).

# TODO: 
celsius = float(input("Enter a temperature in Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32
print("In Fahrenheit:", fahrenheit)
 
fahrenheit_input = float(input("Enter a temperature in Fahrenheit: "))
celsius_from_f = (fahrenheit_input - 32) * 5 / 9
print("In Celsius:", celsius_from_f)


# ── Exercise 3: Age Calculator ────────────────────────────────────────────────
# Ask for the user's name and birth year.
# Calculate and print their current age and the year they will turn 30.

# TODO: 
# Exercise 3: Age Calculator
name = input("Enter your name: ")
birth_year = int(input("Enter your birth year: "))

current_year = 2026
age = current_year - birth_year
year_turns_30 = birth_year + 30

print("Name:", name)
print("Current Age:", age)
print("Year you turn 30:", year_turns_30)
