grade = float(input())
valid_count = 0
total = 0.0
average = 0.0

# TODO: Your code here
while grade != -1:
    if grade <= 100 and grade >= 0:
        total += grade
        valid_count += 1
    grade = float(input())

average = total / valid_count if valid_count > 0 else 0.0

print(valid_count)
print(f"{average:.2f}")
