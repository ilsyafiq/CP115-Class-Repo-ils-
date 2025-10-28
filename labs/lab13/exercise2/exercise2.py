# TODO: Your code here
i = 1
while i <= 100:
    if i % 7 == 0 and i % 13 == 0:
        found_number = i
        break
    i += 1

print(found_number)
