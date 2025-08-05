# Asks the user for their name, age, and course code && Stores this information in appropriately named variables
student_name = input("Enter your name: ")        # str (string)
student_age = int(input("Enter your age: "))     # int (integer)
course_name = input("Enter the course name: ")   # str (string)

# Displays the student information
print("Student Information System")
print("\nStudent Name: " + student_name)
print("Age: " + str(student_age))
print("Course: " + course_name)