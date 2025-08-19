# Imports school_data.py and displays the information using f-strings

import school_data

print("=== School Data ===")
print(f"Student Name: {school_data.student_name}")
print(f"Student ID: {school_data.student_id}")
print(f"Student Age: {school_data.student_age}")
print(f"Course Code: {school_data.course_code}")
print(f"Course Name: {school_data.course_name}")
print(f"Total Students: {school_data.total_students}")
print(f"Score 1: {school_data.score1}")
print(f"Score 2: {school_data.score2}")
print(f"Total Score: {school_data.total_score}")
print(f"Student Name (Upper): {school_data.student_name_upper}")
print(f"Student Name (Lower): {school_data.student_name_lower}")
print(f"Student Name Length: {school_data.student_name_length}")
print(f"Square Root of Total Score: {school_data.total_score_sqrt:.2f}")
