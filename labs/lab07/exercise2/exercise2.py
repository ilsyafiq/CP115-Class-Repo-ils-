# Imports shopping_data and displays the information using f-strings

import shopping_data

print("=== Shopping Data ===")
print(f"Product Name: {shopping_data.product_name}")
print(f"Product Price: ${shopping_data.product_price:.2f}")
print(f"Product Quantity: {shopping_data.product_quantity}")
print(f"Total Cost: ${shopping_data.total_cost:.2f}")
