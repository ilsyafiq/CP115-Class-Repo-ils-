# Grades
grade1 = 78
grade2 = 85
grade3 = 92
grade4 = 67
grade5 = 88

full_mark = 100
total_full_mark = full_mark * 5

student_total_mark = grade1 + grade2 + grade3 + grade4 + grade5
average = student_total_mark / 5
percentage1 = (grade1 / full_mark) * 100
percentage2 = (grade2 / full_mark) * 100
percentage3 = (grade3 / full_mark) * 100
percentage4 = (grade4 / full_mark) * 100
percentage5 = (grade5 / full_mark) * 100

# Display
print("Student Test 1 Score:", grade1)
print("Student Test 2 Score:", grade2)
print("Student Test 3 Score:", grade3)
print("Student Test 4 Score:", grade4)
print("Student Test 5 Score:", grade5)
print("\nTotal Marks Obtained:", student_total_mark, "out of", total_full_mark)
print("Average Score:", average)
print("\nPercentage Contribution of Each Test:")
print(f"Test 1: {percentage1}%")
print(f"Test 2: {percentage2}%")
print(f"Test 3: {percentage3}%")
print(f"Test 4: {percentage4}%")
print(f"Test 5: {percentage5}%")