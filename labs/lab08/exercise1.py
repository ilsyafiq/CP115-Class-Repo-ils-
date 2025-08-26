score1 = 85
score2 = 92.5
score3 = 78

average = (score1 + score2 + score3) / 3

print(f"Average score = {average} (type: {type(average)})")

average_int = int(average)
print(f"Average score (int) = {average_int} (type: {type(average_int)})")

# Question 4: Perform this calculation: score1 ** 2 / score2 + score3 % 7 and print the result and type
result = score1 ** 2 / score2 + score3 % 7
print(f"Question 4 result = {result} (type: {type(result)})")

# int(score2) vs float(score1)
# int() function rounds the value of score2 down to the nearest integer
# float() function converts score1 to a float (giving it atleast one decimal point)
print (f"int(score2) = {int(score2)} (type: {type(int(score2))})")
print (f"float(score1) = {float(score1)} (type: {type(float(score1))})")
