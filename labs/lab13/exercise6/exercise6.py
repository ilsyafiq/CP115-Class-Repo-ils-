age = int(input())
tickets_sold = 0
total_revenue = 0

# TODO: Your code here
while age != -1:
    if age <= 12:
        total_revenue += 8
    elif age <= 17:
        total_revenue += 10
    elif age <= 64:
        total_revenue += 15
    else:
        total_revenue += 10
    tickets_sold += 1
    age = int(input())
    

print(tickets_sold)
print(total_revenue)
