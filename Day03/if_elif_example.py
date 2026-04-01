# if_elif_example.py

marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade A+")
elif marks >= 75:
    print("Grade A")
elif marks >= 50:
    print("Grade B")
else:
    print("Fail")