# # Simple calculator using if-else statements

# # Get user inputs
# num1 = float(input("Enter first number: "))
# operation = input("Enter operation (+, -, *, /): ")
# num2 = float(input("Enter secnond number: "))

# # # Perform calculation using if-else statments
# if operation == '+':
#     result = num1 + num2
# elif operation == '-':
#     result = num1 - num2
# elif operation == '*':
#     result = num1 * num2
# elif operation == '/':
#     if num2 != 0:
#         result = num1 / num2
#     else:
#         result = "Error! Division by Zero"
# else:
#     result = "Error! Invalid Operation"

# print(f"The result is: {result}")

# Next, a simple calculator using if-else statements

num1 = float(input("Enter your first number: "))
operation = input("What operation you want to perform (+, -, *, /): ")
num2 = float(input("Enter your second number: "))


if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    if num2 == 0:
        result = "Error! Division by Zero"
    else:
        result = num1 / num2
else:
    result = "Error! What the hell are you doing?"

print(f"The result of this operation is: {result}")

