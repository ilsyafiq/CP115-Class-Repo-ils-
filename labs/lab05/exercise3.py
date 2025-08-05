# Imports the random module
import random

# Takes the student's class name from the user
student_class = input("Enter your class'name: ")

# Generates a random number (1 - 18) and displays class information
random_number = random.randint(1, 18)

print("Class: " + student_class)
print("Random number: " + str(random_number))
