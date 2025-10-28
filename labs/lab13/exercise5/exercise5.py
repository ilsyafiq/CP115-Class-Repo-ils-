amount = int(input())
valid_count = 0
total_withdrawn = 0

# TODO: Your code here
while amount != 0:
    if amount >= 20 and amount <= 500 and amount % 20 == 0:
        valid_count += 1
        total_withdrawn += amount
    amount = int(input())

print(valid_count)      # Number of valid withdrawals
print(total_withdrawn)  # Total amount from valid withdrawals only
