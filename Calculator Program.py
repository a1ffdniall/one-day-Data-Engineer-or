# Calculator Program
# Complexity: Simple
# Task: Create a basic calculator that can perform addition, subtraction, multiplication, and division.
# Created by: Muhammad Aliff Danial bin Mohd Yusuf
# Date: 30/09/2025

# This program performs basic arithmetic operations: addition, subtraction, multiplication, and division.

print("Welcome to the Simple Calculator Program!\n")
operator = input("Enter an operator (+, -, *, /): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {round(result, 3)}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {round(result, 3)}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {round(result, 3)}")
elif operator == "/":
    if num1 != 0 and num2 != 0:
        result = num1 / num2
        print(f"{num1} / {num2} = {round(result, 3)}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print(f"Error: {operator} is an invalid operator.")