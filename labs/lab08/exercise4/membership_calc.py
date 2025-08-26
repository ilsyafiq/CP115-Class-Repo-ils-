membership_fee = 120.00
personal_training_fee = 80.00
registration_fee = 50.00

# Number of Personal Training Sessions taken from question
n_training_sessions = 6

locker_rental = 25.00
towel_service = 15.00
additional_charges = locker_rental + towel_service

# Total first-month cost
total_first_month_cost = (registration_fee + membership_fee + (personal_training_fee * n_training_sessions) + additional_charges)

# Total monthly (not first-month)
total_after_first_month = (membership_fee + (personal_training_fee * n_training_sessions) + additional_charges)

# Annual cost (12 months including first month)
annual_cost = total_first_month_cost + (total_after_first_month * 11)

print(f"Total First Month Cost: RM {total_first_month_cost:.2f}")
print(f"Total Monthly Cost (After First Month): RM {total_after_first_month:.2f}")
print(f"Total Annual Cost: RM {annual_cost:.2f}")