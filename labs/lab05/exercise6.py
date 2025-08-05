# Takes time in minutes from the user
time = float(input("Enter time (minutes): "))

# Converts minutes to hours and remaining minutes
hours = time // 60
minutes = time % 60
# Displays the original minutes and converted time format
print(f"{time} minutes is equivalent to {hours} hours and {minutes} minutes.")