import employee_data

# Gross salary calculations, value imported from employee_data.py
gross_salary = employee_data.basic_salary + (employee_data.overtime_hours * employee_data.overtime_rate)
print(f"Gross Salary: RM {gross_salary:.2f}")

# Fixed charges
EPF = gross_salary * 0.11
SOCSO = gross_salary * 0.005
EIS = gross_salary * 0.002
medical_insurance = 50.00
parking = 30.00

# Total salary calculation and display
total_salary = (gross_salary - (EPF + SOCSO + EIS + medical_insurance + parking))
print(f"Total Salary: RM {total_salary:.2f}")