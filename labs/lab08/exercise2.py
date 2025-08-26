n_people = 6
n_mains = 3
n_appetizers = 2
n_drinks = 4

price_main = 25
price_appetizer = 12
price_drink = 8

# Calculate total bill
total_meal_price = (n_mains * price_main) + (n_appetizers * price_appetizer) + (n_drinks * price_drink)
service_tax = 0.1
delivery_fee = 5

total_bill = total_meal_price + (total_meal_price * service_tax) + delivery_fee

# Calculate amount per person
amount_per_person = total_bill // n_people
print(f"Each person needs to pay: RM{amount_per_person:.2f}")
