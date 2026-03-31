# Day 2: Variables and User Input

# Taking input from user
name = input("Enter your name: ")
age = int(input("Enter your age: "))
height = float(input("Enter your height in cm: "))

# Boolean variable
is_student = input("Are you a student? (yes/no): ").lower() == "yes"

# Displaying data
print("\n--- User Details ---")
print("Name:", name)
print("Age:", age)
print("Height:", height, "cm")
print("Student:", is_student)

# Simple calculation
birth_year = 2026 - age
print("Estimated Birth Year:", birth_year)

# Condition check
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote!")