# Takes three test scores from the user
test_score1 = int(input("Enter Test Score 1: "))
test_score2 = int(input("Enter Test Score 2: "))
test_score3 = int(input("Enter Test Score 3: "))

# Calculates the total score and average score
total_score = test_score1 + test_score2 + test_score3
average_score = total_score / 3

# Displays all individual scores, total, and average
print("Test Score 1: " + str(test_score1))
print("Test Score 2: " + str(test_score2))
print("Test Score 3: " + str(test_score3))
print("\nTotal Score: " + str(total_score))
print("Average Score: " + str(average_score))