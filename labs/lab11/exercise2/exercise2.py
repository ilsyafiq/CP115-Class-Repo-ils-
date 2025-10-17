num_days = int(input())
danger_threshold = float(input())
danger_days = 0
average_temp = 0.0

# TODO: Your code here
# Use input() inside the loop to get each day's temperature
for day in range(num_days):
    daily_temp = float(input())
    if daily_temp > danger_threshold:
        danger_days += 1
    average_temp += daily_temp
if num_days > 0:
    average_temp = average_temp / num_days

print(danger_days)
print(f"{average_temp:.1f}")