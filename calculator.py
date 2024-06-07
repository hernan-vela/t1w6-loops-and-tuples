# Simple calculator using if-else statements

# Get user inputs
num1 = input("Enter first number: ")
operation = input("Enter operation (+, -, *, /): ")
num2 = input("Enter secnond number: ")

# Perform calucalitri using if-else statments
if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error! Division by Zero"
else:
    result = "Error! Invalid Operation"

print(f"The result is: {result}")