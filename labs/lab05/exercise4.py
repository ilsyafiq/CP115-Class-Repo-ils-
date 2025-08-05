# Takes item name and price from the user
item_name = input("Enter item name: ")
item_price = float(input("Enter item price: "))

# Creates variables for quantity (3 items) and tax rate (6%)
quantity = int(3)
tax_rate = float(0.06)

# Calculates and displays subtotal, tax amount, and total cost
subtotal = item_price*quantity
tax_amount = subtotal*tax_rate
total_cost = subtotal + tax_amount

print("Subtotal: " + str(subtotal))
print("Tax amount: " + str(tax_amount))
print("Total cost: " + str(total_cost))