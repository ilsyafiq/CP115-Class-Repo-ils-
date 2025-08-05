# Imports the math module
import math

# Takes a radius of circle from the user
print("Circle Calculator (Area & Circumference)")
radius = int(input("Enter your radius of circle (cm): "))

# Print the area and circumference of the circle
area = math.pi * pow(radius, 2)
circumference = 2 * math.pi * radius

rounded_area = round(area, 2)
rounded_circumference = round(circumference, 2)


print("\nArea: " + str(rounded_area)+ " cm²")
print("Circumference: " + str(rounded_circumference) + " cm")