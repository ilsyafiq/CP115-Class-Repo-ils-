correct_password = "python123"
login_successful = False
attempts_used = 0

# TODO: Your code here
for i in range(3):
    entered_password = input()
    if entered_password == correct_password:
        login_successful = True
        attempts_used += 1
        break
    attempts_used += 1


print(login_successful)
print(attempts_used)
