# Imports the math module
import math

# Takes one number from the user
number = float(input("Enter a number: "))

# Calculates square root, square, cube, and sine of the number
square_root = math.sqrt(number)
square = math.pow(number, 2)
cube = math.pow(number, 3)
sine = math.sin(number)

# Calculates and displays: square root, square (power of 2), cube (power of 3), and sine value
print(f"Square root: {square_root}")
print(f"Square (power of 2): {square}")
print(f"Cube (power of 3): {cube}")
print(f"Sine value: {sine}")