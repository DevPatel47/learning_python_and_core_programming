import math
from time import sleep

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def power(a, b):
    return a ** b

def sqrt(a):
    if a < 0:
        raise ValueError("Cannot take the square root of a negative number.")
    return math.sqrt(a)

def factorial(n):
    if n < 0:
        raise ValueError("Cannot take the factorial of a negative number.")
    return math.factorial(n)

def logarithm(a, base=10):
    if a <= 0:
        raise ValueError("Logarithm undefined for non-positive values.")
    return math.log(a, base)

def sine(angle_rad):
    return math.sin(angle_rad)

def cosine(angle_rad):
    return math.cos(angle_rad)

def tangent(angle_rad):
    return math.tan(angle_rad)

def cotangent(angle_rad):
    tan_value = math.tan(angle_rad)
    if tan_value == 0:
        raise ValueError("Cotangent undefined for this angle.")
    return 1 / tan_value

def degrees_to_radians(degrees):
    return math.radians(degrees)

def radians_to_degrees(radians):
    return math.degrees(radians)

def calculate(operation):
    match operation:
        case 1:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"{num1} + {num2} = {add(num1, num2)}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                sleep(3)
        case 2:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"{num1} - {num2} = {subtract(num1, num2)}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                sleep(3)
        case 3:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"{num1} * {num2} = {multiply(num1, num2)}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                sleep(3)
        case 4:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                print(f"{num1} / {num2} = {divide(num1, num2)}")
            except ValueError as e:
                print(e)
                sleep(3)
        case 5:
            try:
                num1 = float(input("Enter base number: "))
                num2 = float(input("Enter exponent number: "))
                print(f"{num1} ^ {num2} = {power(num1, num2)}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                sleep(3)
        case 6:
            try:
                num = float(input("Enter number: "))
                print(f"Square root of {num} = {sqrt(num)}")
            except ValueError as e:
                print(e)
                sleep(3)
        case 7:
            try:
                num = int(input("Enter a non-negative integer: "))
                print(f"Factorial of {num} = {factorial(num)}")
            except ValueError as e:
                print(e)
                sleep(3)
        case 8:
            try:
                num = float(input("Enter number: "))
                base = float(input("Enter base (default is 10): ") or 10)
                print(f"Logarithm of {num} with base {base} = {logarithm(num, base)}")
            except ValueError as e:
                print(e)
                sleep(3)
        case 9:
            try:
                angle = float(input("Enter angle in radians: "))
                print(f"Sine of {angle} radians = {sine(angle)}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                sleep(3)
        case 10:
            try:
                angle = float(input("Enter angle in radians: "))
                print(f"Cosine of {angle} radians = {cosine(angle)}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                sleep(3)
        case 11:
            try:
                angle = float(input("Enter angle in radians: "))
                print(f"Tangent of {angle} radians = {tangent(angle)}")
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                sleep(3)
        case 12:
            try:
                angle = float(input("Enter angle in radians: "))
                print(f"Cotangent of {angle} radians = {cotangent(angle)}")
            except ValueError as e:
                print(e)
                sleep(3)
        case 13:
            try:
                degrees = float(input("Enter angle in degrees: "))
                print(f"{degrees} degrees = {degrees_to_radians(degrees)} radians") 
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                sleep(3)
        case 14:
            try:
                radians = float(input("Enter angle in radians: "))
                print(f"{radians} radians = {radians_to_degrees(radians)} degrees") 
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                sleep(3)

while True:
    try:
        operation = int(input("""
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Power
6. Square Root
7. Factorial
8. Logarithm
9. Sine
10. Cosine
11. Tangent
12. Cotangent
13. Degrees to Radians
14. Radians to Degrees

Select operation (1-14):"""))

        if 1 <= operation <= 14:
            calculate(operation)
        else:
            print("Invalid input. Please enter a number between 1 and 14.")
            sleep(3)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 14.")
        sleep(3)
