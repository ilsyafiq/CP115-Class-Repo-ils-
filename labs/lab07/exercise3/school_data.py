import random
import math

# Student information variables (name, student ID, age)
student_name = "Mohd Syafiq"
student_id = "MC2515113645"
student_age = 18

# Course information
course_code = "CP115"
course_name = "Python Programming"
total_students = 31

# Generate two random scores (70-95 and 75-100)
score1 = random.randint(70, 95)
score2 = random.randint(75, 100)

# Calculate total score by adding the two scores
total_score = score1 + score2

# String operations on student name (upper, lower, length)
student_name_upper = student_name.upper()
student_name_lower = student_name.lower()
student_name_length = len(student_name)

# Calculate square root of total score
total_score_sqrt = math.sqrt(total_score)