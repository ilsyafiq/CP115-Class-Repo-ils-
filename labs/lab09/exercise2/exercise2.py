employee_name = input()
base_salary = float(input())
overtime_hours = int(input())
tax_status = input()

# TODO your code here
overtime_pay = overtime_hours * 35
total_income = base_salary + overtime_pay
epf_deduction = 0.11
socso_deduction = 0.005

if tax_status == "Single":

    if total_income >= 5000:
        tax_rate = 0.22
    else:
        tax_rate = 0.18

elif tax_status == "Married":

    if total_income >= 6000:
        tax_rate = 0.20
    else:
        tax_rate = 0.15

elif tax_status == "Head":

    if total_income >= 5500:
        tax_rate = 0.25
    else:
        tax_rate = 0.19

net_salary = total_income * (1 - tax_rate) * (1 - (epf_deduction + socso_deduction))
tax_rate = f"{int(tax_rate * 100)}%"

print(employee_name)
print(tax_rate)
print(f"{net_salary:.2f}")