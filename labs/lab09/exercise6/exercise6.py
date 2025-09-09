position = input()
overtime_hours = int(input())
is_weekend = input()

if position == "Manager":
    base_rate = 30
elif position == "Supervisor":
    base_rate = 20
elif position == "Staff":
    base_rate = 15
elif position == "Intern":
    base_rate = 8

if overtime_hours == 0:
    overtime_pay = 0
elif overtime_hours <= 8:
    overtime_pay = overtime_hours * base_rate * 1.5
else:
    overtime_pay = (8 * base_rate * 1.5) + ((overtime_hours - 8) * base_rate * 2.0)

if is_weekend == "Yes":
    overtime_pay += overtime_hours * 5


print(overtime_pay)